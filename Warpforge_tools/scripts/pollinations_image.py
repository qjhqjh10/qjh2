#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pollinations_image.py — 免费文生图工具 (pollinations.ai, 无需key/注册, 任何项目可用)
用法:
  python pollinations_image.py "战锤40K星际战士图标" -o out.png [--size 256]
  python pollinations_image.py "描述" --list-models

说明:
  - 纯 HTTP GET, 不依赖任何 key/配置/项目路径
  - 免费服务有速率限制: 生成间隔建议 >= 5 秒, 批量请加 --sleep
  - 生成是公开服务, 不要生成敏感/侵权内容
"""
import argparse
import os
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = "https://image.pollinations.ai/prompt/"


def gen(prompt: str, out: str, size: int = 512, seed: int = None,
        model: str = "", enhance: bool = True) -> str:
    """生成单张图。返回输出路径。"""
    q = urllib.parse.quote(prompt)
    url = f"{BASE}{q}?width={size}&height={size}&nologo=true&enhance={str(enhance).lower()}"
    if seed is not None:
        url += f"&seed={seed}"
    if model:
        url += f"&model={urllib.parse.quote(model)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "wb") as f:
        f.write(data)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="pollinations.ai 免费文生图")
    ap.add_argument("prompt", help="图像描述 (中文/英文均可)")
    ap.add_argument("-o", "--out", default="generated.png", help="输出路径")
    ap.add_argument("--size", type=int, default=512, help="边长 (默认512)")
    ap.add_argument("--seed", type=int, default=None, help="固定种子(可复现)")
    ap.add_argument("--model", default="", help="模型(默认turbo, 如flux)")
    ap.add_argument("--no-enhance", action="store_true", help="关闭自动增强")
    ap.add_argument("--sleep", type=float, default=0, help="生成前等待秒数(限速用)")
    ap.add_argument("--list-models", action="store_true", help="列出可用模型")
    args = ap.parse_args()

    if args.list_models:
        # 模型列表文档页
        print("常见模型: turbo (默认) / flux / flux-pro / pixray")
        print("详细见: https://pollinations.ai (免费无需key)")
        return 0

    if args.sleep:
        time.sleep(args.sleep)
    try:
        out = gen(args.prompt, args.out, args.size, args.seed,
                  args.model, not args.no_enhance)
        print(f"✓ 已生成: {out} ({os.path.getsize(out)//1024} KB)")
        return 0
    except Exception as e:
        print(f"✗ 失败: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
