#!/usr/bin/env python3
"""Warpforge 视觉副模型 MCP Server（stdio）。

通过 MiniMax M3（OpenCode Go 订阅，OpenAI 兼容 API）识别本地卡图/图片/视频。
- 环境变量：
  MINIMAX_API_KEY  必填（key 只从环境读取，绝不写入任何文件/日志）
  MINIMAX_BASE_URL 默认 https://opencode.ai/zen/go/v1（OpenCode Go；可覆盖为官方或中转）
  MINIMAX_MODEL    默认 MiniMax-M3（首次真实调用自动探测 /models 修正）
  MINIMAX_MOCK     =1 时进入 mock 模式（不调 API，供无 key 冒烟测试）
- 工具：
  vision_analyze(image_path, prompt)        单图/单视频识别（视频自动抽帧）
  vision_batch(inputs|directory, template)  批量识别（并发/错误隔离/摘要）
  vision_compare(images, prompt)            多图对比
  vision_media(media_path, prompt)          通用媒体识别：图片直发；视频 PyAV 抽帧(≤8帧)多图分析
- 视频处理：PyAV 内置 ffmpeg 抽帧（每 2s 一帧，长边 1024 JPEG，≤8 帧），
  走已验证的图像多图能力，不依赖 API 的视频 content 类型。
  若未来实测 API 原生支持视频 content（MINIMAX_VIDEO_DIRECT=1 可切换直发）。
安全：stdout 只输出 JSON-RPC 帧；日志走 stderr（WARNING，不含 key）；API 错误截断 500 字符。
"""
import os
import sys
import json
import time
import base64
import logging
import io
import urllib.request
import urllib.error
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

logging.basicConfig(stream=sys.stderr, level=logging.WARNING,
                    format="%(levelname)s %(message)s")
log = logging.getLogger("vision")

# ---------------- 配置 ----------------
BASE_URL = os.environ.get("MINIMAX_BASE_URL", "https://opencode.ai/zen/go/v1").strip().rstrip("/")
DEFAULT_MODEL = os.environ.get("MINIMAX_MODEL", "MiniMax-M3").strip()
MOCK = os.environ.get("MINIMAX_MOCK") == "1"
ART_ROOT = r"d:/2/解包整理"
ALLOWED_EXT = {".png", ".jpg", ".jpeg", ".webp"}
MAX_BYTES = 6 * 1024 * 1024
MAX_BATCH = 50
DEFAULT_CONCURRENCY = 2
DEFAULT_TIMEOUT = 180

# 视频支持（PyAV 抽帧管线）
VIDEO_EXT = {".mp4", ".webm", ".mov", ".mkv"}
MAX_VIDEO_FRAMES = 8          # 最多抽帧数 (控制 token)
VIDEO_SAMPLE_SEC = 2.0        # 抽样间隔
VIDEO_MAX_BYTES = 120 * 1024 * 1024  # 视频上限 120MB (抽帧后只传 JPEG)
FRAME_MAX_SIDE = 1024         # 抽帧长边
VIDEO_DIRECT = os.environ.get("MINIMAX_VIDEO_DIRECT") == "1"  # 未来直发视频开关

try:
    import av  # PyAV (内置 ffmpeg): 视频抽帧
    HAS_AV = True
except ImportError:
    HAS_AV = False
    log.warning("未安装 PyAV，视频工具将不可用 (pip install av)")

_model_lock = threading.Lock()
_model_checked = False
_model_final = DEFAULT_MODEL


_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def _headers(key):
    return {"Authorization": "Bearer " + key, "Content-Type": "application/json",
            "User-Agent": _UA}


def _endpoints():
    """返回 (chat端点, models端点)。容忍三种 base_url 形态。"""
    b = BASE_URL
    if b.endswith("/chat/completions"):
        return b, b[: -len("/chat/completions")] + "/models"
    if b.endswith("/v1"):
        return b + "/chat/completions", b + "/models"
    return b + "/v1/chat/completions", b + "/v1/models"


def _api_key():
    return os.environ.get("MINIMAX_API_KEY") or ""


def _detect_model():
    """GET /models 探测实际型号名（lazy，首次真实调用前执行一次）。"""
    global _model_checked, _model_final
    with _model_lock:
        if _model_checked:
            return _model_final
        _model_checked = True
        key = _api_key()
        if not key:
            return _model_final
        try:
            _, models_url = _endpoints()
            req = urllib.request.Request(models_url, headers=_headers(key))
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read().decode("utf-8", errors="replace"))
            ids = []
            for m in data.get("data", []):
                mid = m.get("id") or m.get("model") or ""
                if mid:
                    ids.append(mid)
            if not ids:
                return _model_final
            if DEFAULT_MODEL in ids:
                _model_final = DEFAULT_MODEL
                return _model_final
            cand = [i for i in ids if "minimax" in i.lower() and ("m3" in i.lower() or "m2" in i.lower())]
            if cand:
                _model_final = cand[0]
                log.warning("模型 %s 不在列表，已切换为探测到的 %s", DEFAULT_MODEL, _model_final)
            else:
                log.warning("模型 %s 不在列表(共 %d 个)，仍使用默认值", DEFAULT_MODEL, len(ids))
        except Exception as e:
            log.warning("模型探测失败(%s)，使用默认 %s", str(e)[:120], _model_final)
        return _model_final


# ---------------- 图片读取 ----------------
def _resolve_path(p):
    if os.path.isabs(p) and os.path.isfile(p):
        return p
    for base in (ART_ROOT, os.getcwd()):
        cand = os.path.join(base, p)
        if os.path.isfile(cand):
            return cand
    return None


def _read_image(p):
    """返回 (data_uri, error_code, error_msg)。"""
    path = _resolve_path(p)
    if not path:
        return None, "file", f"文件不存在: {p}"
    ext = os.path.splitext(path)[1].lower()
    if ext not in ALLOWED_EXT:
        return None, "file", f"不支持的图片格式: {ext}"
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        return None, "size", f"图片过大 {size // (1024*1024)}MB（上限 6MB）: {os.path.basename(path)}"
    try:
        with open(path, "rb") as f:
            raw = f.read()
    except OSError as e:
        return None, "file", f"读取失败: {e}"
    return "data:image/" + ext[1:] + ";base64," + base64.b64encode(raw).decode("ascii"), None, None


# ---------------- 视频处理 (PyAV 抽帧) ----------------
def _video_frames_to_data_uris(path):
    """视频 → JPEG data URI 列表（均匀抽样, 长边 1024, ≤MAX_VIDEO_FRAMES 帧）。
    返回 (uris, error_code, error_msg)。"""
    if not HAS_AV:
        return None, "api", "未安装 PyAV，无法处理视频 (pip install av)"
    if not os.path.isfile(path):
        return None, "file", f"文件不存在: {path}"
    size = os.path.getsize(path)
    if size > VIDEO_MAX_BYTES:
        return None, "size", f"视频过大 {size // (1024*1024)}MB（上限 {VIDEO_MAX_BYTES//(1024*1024)}MB）"
    try:
        container = av.open(path)
    except Exception as e:
        return None, "file", f"无法打开视频: {str(e)[:200]}"
    uris = []
    try:
        stream = container.streams.video[0]
        fps = float(stream.average_rate) if stream.average_rate else 30.0
        step = max(1, int(fps * VIDEO_SAMPLE_SEC))
        idx = 0
        for frame in container.decode(video=0):
            if idx % step != 0:
                idx += 1
                continue
            idx += 1
            img = frame.to_image()
            # 等比缩到长边 FRAME_MAX_SIDE
            w, h = img.size
            if max(w, h) > FRAME_MAX_SIDE:
                s = FRAME_MAX_SIDE / float(max(w, h))
                img = img.resize((int(w * s), int(h * s)))
            buf = io.BytesIO()
            img.save(buf, "JPEG", quality=82)
            uris.append("data:image/jpeg;base64," +
                        base64.b64encode(buf.getvalue()).decode("ascii"))
            if len(uris) >= MAX_VIDEO_FRAMES:
                break
    except Exception as e:
        if not uris:
            return None, "file", f"抽帧失败: {str(e)[:200]}"
    finally:
        try:
            container.close()
        except Exception:
            pass
    if not uris:
        return None, "file", "视频无有效帧"
    return uris, None, None


def _read_media(p):
    """图片直读; 视频抽帧。返回 (data_uris, error_code, error_msg)。"""
    path = _resolve_path(p)
    if not path:
        return None, "file", f"文件不存在: {p}"
    ext = os.path.splitext(path)[1].lower()
    if ext in VIDEO_EXT:
        return _video_frames_to_data_uris(path)
    if ext in ALLOWED_EXT:
        uri, ec, err = _read_image(path)
        return ([uri], ec, err) if uri else (None, ec, err)
    return None, "file", f"不支持的媒体格式: {ext} (支持 {sorted(ALLOWED_EXT | VIDEO_EXT)})"


# ---------------- MiniMax 调用 ----------------
def _call_once(prompt, data_uris, timeout):
    """单次调用（支持多图）。返回 (text, error_code, error_msg)。"""
    if MOCK:
        time.sleep(0.05)
        if "mock_fail" in prompt:
            return None, "api", "mock 模拟失败"
        return ("(mock) 这是一张卡牌立绘，包含一名星际战士角色，背景为战场场景。"
                f"图片 {len(data_uris)} 张，数据长度 {sum(len(u) for u in data_uris)} 字符。"), None, None
    key = _api_key()
    if not key:
        return None, "api", "MINIMAX_API_KEY 未设置。请先在系统环境变量设置（setx MINIMAX_API_KEY <key>），然后重启 Claude Code。"
    model = _detect_model()
    content = [{"type": "text", "text": prompt}]
    content += [{"type": "image_url", "image_url": {"url": u}} for u in data_uris]
    body = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "temperature": 0.2,
        "max_tokens": 1024,
    }
    url, _ = _endpoints()
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers=_headers(key),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            resp = json.loads(r.read().decode("utf-8", errors="replace"))
        text = (resp.get("choices") or [{}])[0].get("message", {}).get("content", "")
        if not text:
            return None, "api", f"空响应: {json.dumps(resp, ensure_ascii=False)[:300]}"
        return text, None, None
    except urllib.error.HTTPError as e:
        detail = e.read(500).decode("utf-8", errors="replace")[:500]
        return None, f"http_{e.code}", f"HTTP {e.code}: {detail}"
    except TimeoutError:
        return None, "timeout", f"请求超时(>{timeout}s)"
    except Exception as e:
        return None, "api", f"{type(e).__name__}: {str(e)[:300]}"


def _call_with_retry(prompt, data_uris, timeout):
    """429 重试1次(Retry-After 封顶30s)；5xx 退避(1s,3s)重试2次。"""
    text, ec, err = _call_once(prompt, data_uris, timeout)
    if ec == "http_429":
        for _ in range(1):
            ra = 0
            if err and "Retry-After" in err:
                try:
                    ra = min(int(err.split("Retry-After")[1].split()[0].strip(": ")), 30)
                except Exception:
                    ra = 5
            time.sleep(max(ra, 2))
            text, ec, err = _call_once(prompt, data_uris, timeout)
            if ec != "http_429":
                break
    elif ec == "http_5xx" or (ec and ec.startswith("http_5")):
        for wait in (1, 3):
            time.sleep(wait)
            text, ec, err = _call_once(prompt, data_uris, timeout)
            if ec is None:
                break
    return text, ec, err


def _analyze_one(image_path, prompt, timeout):
    t0 = time.time()
    data_uri, ec, err = _read_image(image_path)
    if ec:
        return {"file": image_path, "ok": False, "text": None, "error": err,
                "error_code": ec, "duration_ms": int((time.time() - t0) * 1000)}
    text, ec2, err2 = _call_with_retry(prompt, [data_uri], timeout)
    return {"file": image_path, "ok": ec2 is None, "text": text,
            "error": err2, "error_code": ec2, "duration_ms": int((time.time() - t0) * 1000)}


# ---------------- MCP Server ----------------
from fastmcp import FastMCP  # noqa: E402

mcp = FastMCP("vision")


@mcp.tool()
def vision_analyze(image_path: str, prompt: str) -> str:
    """识别单张本地图片。image_path 可为绝对路径，或相对 d:/2/解包整理/ 的路径；
    prompt 是给视觉模型的指示（如"描述这张卡图"、"提取卡面文字"）。"""
    r = _analyze_one(image_path, prompt, DEFAULT_TIMEOUT)
    return json.dumps(r, ensure_ascii=False)


@mcp.tool()
def vision_media(media_path: str, prompt: str) -> str:
    """识别本地媒体文件：图片直发；视频（mp4/webm/mov/mkv）自动抽帧 ≤8 帧后多图分析。
    media_path 可为绝对路径，或相对 d:/2/解包整理/ 的路径；
    prompt 是给视觉模型的指示（如"描述这个视频的内容"、"提取画面中的文字"）。
    适合：开包动画、主菜单背景视频、战斗结算动画的内容识别。"""
    uris, ec, err = _read_media(media_path)
    if ec:
        return json.dumps({"file": media_path, "ok": False, "text": None,
                           "error": err, "error_code": ec, "duration_ms": 0},
                          ensure_ascii=False)
    t0 = time.time()
    text, ec2, err2 = _call_with_retry(prompt, uris, DEFAULT_TIMEOUT)
    n_frame = len(uris)
    return json.dumps({"file": media_path, "ok": ec2 is None, "text": text,
                       "frames": n_frame, "error": err2, "error_code": ec2,
                       "duration_ms": int((time.time() - t0) * 1000)}, ensure_ascii=False)


@mcp.tool()
def vision_batch(
    inputs: list | None = None,
    directory: str | None = None,
    prompt_template: str = "",
    concurrency: int = DEFAULT_CONCURRENCY,
    max_files: int = 20,
    timeout: int = DEFAULT_TIMEOUT,
    retry_failed: bool = True,
) -> str:
    """批量识别图片。inputs 为文件列表，或 directory 递归收集 png/jpg/webp（二选一）；
    prompt_template 为任务模板，可用 {file} 占位文件名。并发默认 2（上限 4），
    max_files 默认 20（上限 50，超出请分批）。单张失败不影响整体。"""
    files = []
    if inputs:
        files = [str(f) for f in inputs]
    elif directory:
        for dirpath, _, fns in os.walk(directory):
            for fn in sorted(fns):
                if os.path.splitext(fn)[1].lower() in ALLOWED_EXT:
                    files.append(os.path.join(dirpath, fn))
    if not files:
        return json.dumps({"ok": False, "results": [], "summary": {
            "total": 0, "succeeded": 0, "failed": 0, "total_ms": 0},
            "error": "未提供有效文件（inputs 或 directory 二选一）"}, ensure_ascii=False)
    files = files[: max(min(max_files, MAX_BATCH), 1)]
    conc = max(1, min(concurrency, 4))
    t0 = time.time()
    results = []
    rate_hits = {"n": 0}

    def one(f):
        prompt = prompt_template.replace("{file}", os.path.basename(f))
        r = _analyze_one(f, prompt, timeout)
        if r.get("error_code") == "http_429":
            rate_hits["n"] += 1
        return r

    with ThreadPoolExecutor(max_workers=conc) as ex:
        futs = {ex.submit(one, f): f for f in files}
        for fut in as_completed(futs):
            try:
                results.append(fut.result())
            except Exception as e:
                results.append({"file": futs[fut], "ok": False, "text": None,
                                "error": str(e)[:300], "error_code": "api",
                                "duration_ms": 0})
    results.sort(key=lambda r: files.index(r["file"]) if r["file"] in files else 0)
    if retry_failed:
        for r in results:
            if not r["ok"]:
                r2 = _analyze_one(r["file"], prompt_template.replace("{file}", os.path.basename(r["file"])), timeout)
                r2["retried"] = True
                r.update(r2)
    total_ms = int((time.time() - t0) * 1000)
    ok_n = sum(1 for r in results if r["ok"])
    summary = {"total": len(results), "succeeded": ok_n, "failed": len(results) - ok_n,
               "total_ms": total_ms}
    if rate_hits["n"] >= conc and conc > 1:
        summary["note"] = f"检测到 {rate_hits['n']} 次限流，下次建议降低并发"
    return json.dumps({"ok": True, "results": results, "summary": summary}, ensure_ascii=False)


@mcp.tool()
def vision_compare(images: list, prompt: str) -> str:
    """多图对比（一次请求携带多张图，适合'哪张更好/找差异/排序'类任务）。
    images 为 2-6 个图片路径（绝对路径或相对 d:/2/解包整理/ 的路径）；
    单张上限 4MB，总载荷上限 16MB。"""
    if not images or len(images) < 2:
        return json.dumps({"ok": False, "text": None, "error": "至少需要 2 张图",
                           "error_code": "file", "duration_ms": 0}, ensure_ascii=False)
    if len(images) > 6:
        return json.dumps({"ok": False, "text": None, "error": f"最多 6 张图（收到 {len(images)}）",
                           "error_code": "file", "duration_ms": 0}, ensure_ascii=False)
    t0 = time.time()
    uris = []
    for p in images:
        uri, ec, err = _read_image(p)
        if ec:
            return json.dumps({"ok": False, "text": None, "error": f"{p}: {err}",
                               "error_code": ec, "duration_ms": int((time.time() - t0) * 1000)},
                              ensure_ascii=False)
        uris.append(uri)
    total = sum(len(u) for u in uris)
    if total > 16 * 1024 * 1024:
        return json.dumps({"ok": False, "text": None, "error": "总图片载荷超限(>16MB)",
                           "error_code": "size", "duration_ms": int((time.time() - t0) * 1000)},
                          ensure_ascii=False)
    text, ec, err = _call_with_retry(prompt, uris, DEFAULT_TIMEOUT)
    return json.dumps({"ok": ec is None, "images": list(images), "text": text,
                       "error": err, "error_code": ec,
                       "duration_ms": int((time.time() - t0) * 1000)}, ensure_ascii=False)


if __name__ == "__main__":
    mcp.run(transport="stdio")
