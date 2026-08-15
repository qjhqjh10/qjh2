#!/usr/bin/env python3
"""vision MCP server 无头 JSON-RPC 测试（mock 模式，无需 API key）。
用法:
  py312/python.exe test_vision_mcp.py             # mock 冒烟测试
  py312/python.exe test_vision_mcp.py --live <图片路径>   # 真实调用（需 MINIMAX_API_KEY）
"""
import os
import sys
import json
import subprocess

SERVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vision_mcp_server.py")
PY = r"d:/2/Warpforge_tools/py312/python.exe"
TEST_IMG = r"d:/2/解包整理/01_卡牌/Ultramarines_极限战士/Texture2D/40k_Cardframe_troop_Ultramarines_tier1.png"
FAILS = []


def check(name, cond, extra=""):
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {name}" + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


class MCPClient:
    def __init__(self, env_extra=None):
        env = dict(os.environ)
        env["MINIMAX_MOCK"] = "1"
        env["PYTHONUTF8"] = "1"
        env["PYTHONIOENCODING"] = "utf-8"
        if env_extra:
            env.update(env_extra)
        self.proc = subprocess.Popen(
            [PY, SERVER], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, env=env)
        self.seq = 0

    def send(self, method, params=None):
        self.seq += 1
        msg = {"jsonrpc": "2.0", "id": self.seq, "method": method}
        if params is not None:
            msg["params"] = params
        self.proc.stdin.write((json.dumps(msg) + "\n").encode("utf-8"))
        self.proc.stdin.flush()
        line = self.proc.stdout.readline()
        if not line:
            return None
        return json.loads(line.decode("utf-8"))

    def notify(self, method, params=None):
        self.seq += 1
        msg = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            msg["params"] = params
        self.proc.stdin.write((json.dumps(msg) + "\n").encode("utf-8"))
        self.proc.stdin.flush()

    def close(self):
        try:
            self.proc.stdin.close()
        except Exception:
            pass
        try:
            self.proc.wait(timeout=5)
        except Exception:
            self.proc.kill()


def main():
    live = False
    live_img = TEST_IMG
    if "--live" in sys.argv:
        live = True
        i = sys.argv.index("--live")
        if i + 1 < len(sys.argv):
            live_img = sys.argv[i + 1]
        print("== 真实调用模式 (--live) ==")
    else:
        print("== mock 冒烟测试 ==")

    c = MCPClient()
    # 1. initialize
    r = c.send("initialize", {"protocolVersion": "2025-06-18",
                              "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}})
    check("initialize 握手", r and "result" in r and "serverInfo" in r.get("result", {}),
          json.dumps(r, ensure_ascii=False)[:200])
    c.notify("notifications/initialized")

    # 2. tools/list
    r = c.send("tools/list")
    tools = {}
    if r and "result" in r:
        for t in r["result"].get("tools", []):
            tools[t["name"]] = t
    check("tools/list 返回三个工具", set(tools) == {"vision_analyze", "vision_batch", "vision_compare"},
          f"got={list(tools)}")
    check("vision_analyze 参数 schema 完整",
          all(k in tools.get("vision_analyze", {}).get("inputSchema", {}).get("properties", {})
              for k in ("image_path", "prompt")))
    check("vision_batch 参数 schema 完整",
          all(k in tools.get("vision_batch", {}).get("inputSchema", {}).get("properties", {})
              for k in ("inputs", "directory", "prompt_template", "concurrency", "max_files")))

    if not live:
        # 3. analyze（mock）
        r = c.send("tools/call", {"name": "vision_analyze",
                                  "arguments": {"image_path": TEST_IMG, "prompt": "描述这张图"}})
        out = ""
        if r and "result" in r:
            for item in r["result"].get("content", []):
                out += item.get("text", "")
        check("vision_analyze mock 返回成功", "ok" in out and '"ok": true' in out, out[:200])

        # 4. analyze 错误隔离：不存在的文件
        r = c.send("tools/call", {"name": "vision_analyze",
                                  "arguments": {"image_path": "不存在的文件.png", "prompt": "x"}})
        out = ""
        if r and "result" in r:
            for item in r["result"].get("content", []):
                out += item.get("text", "")
        check("不存在文件返回 ok=false", '"ok": false' in out and "文件不存在" in out, out[:200])

        # 5. compare（mock）
        r = c.send("tools/call", {"name": "vision_compare",
                                  "arguments": {"images": [TEST_IMG, TEST_IMG], "prompt": "对比"}})
        out = ""
        if r and "result" in r:
            for item in r["result"].get("content", []):
                out += item.get("text", "")
        check("vision_compare mock 返回成功", '"ok": true' in out, out[:200])

        # 6. compare 参数校验：1 张图应报错
        r = c.send("tools/call", {"name": "vision_compare",
                                  "arguments": {"images": [TEST_IMG], "prompt": "x"}})
        out = ""
        if r and "result" in r:
            for item in r["result"].get("content", []):
                out += item.get("text", "")
        check("vision_compare 单图报错", '"至少需要 2 张图"' in out, out[:200])

        # 7. batch 错误隔离：1 真图 + 1 假文件
        r = c.send("tools/call", {"name": "vision_batch",
                                  "arguments": {"inputs": [TEST_IMG, "假文件.png"],
                                                "prompt_template": "检查 {file}"}})
        out = ""
        if r and "result" in r:
            for item in r["result"].get("content", []):
                out += item.get("text", "")
        check("batch 返回 summary", '"summary"' in out and '"total": 2' in out, out[:300])
        check("batch 错误隔离(1成功1失败)", '"succeeded": 1' in out and '"failed": 1' in out, out[:300])
    else:
        # live：真实调用
        c.proc.kill()
        c = MCPClient({"MINIMAX_MOCK": ""})
        r = c.send("initialize", {"protocolVersion": "2025-06-18",
                                  "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}})
        check("live initialize", r and "result" in r)
        c.notify("notifications/initialized")
        r = c.send("tools/call", {"name": "vision_analyze",
                                  "arguments": {"image_path": live_img, "prompt": "用一句话描述这张图片的内容"}})
        out = ""
        if r and "result" in r:
            for item in r["result"].get("content", []):
                out += item.get("text", "")
        try:
            d = json.loads(out)
        except Exception:
            d = {}
        check("live 调用返回 ok=true", d.get("ok") is True, out[:300])
        # live compare（多图单请求）
        r = c.send("tools/call", {"name": "vision_compare",
                                  "arguments": {"images": [live_img, TEST_IMG], "prompt": "各用一句话描述"}})
        out = ""
        if r and "result" in r:
            for item in r["result"].get("content", []):
                out += item.get("text", "")
        try:
            d2 = json.loads(out)
        except Exception:
            d2 = {}
        check("live compare 返回 ok=true", d2.get("ok") is True, out[:300])
        if d2.get("ok"):
            print(f"
  compare 回答: {d2.get('text', '')[:150]}")
        if d.get("ok"):
            print(f"\n  副模型回答: {d.get('text', '')[:200]}")
            check("返回内容非空且有实际描述", len(d.get("text", "")) > 10)
        else:
            print(f"\n  API 错误: {d.get('error', '')[:300]}")

    c.close()
    print(f"\n结果: {len(FAILS)} 项失败 / 共检查项")
    if FAILS:
        print("失败项:", FAILS)
        sys.exit(1)
    print("全部通过 ✅")


if __name__ == "__main__":
    main()
