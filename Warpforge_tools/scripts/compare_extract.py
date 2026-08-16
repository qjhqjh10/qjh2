#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compare_extract.py — 新旧解包完整度对比
用法: py312 python.exe compare_extract.py --old <旧解包目录> --new <新解包目录> [--sample N]
对比维度:
  1. 按包统计 (读 _stats.json): 对象数/导出/JSON/fail
  2. 文件规模: 总数/总大小/扩展名分布 (png/ogg/wav/obj/ttf/mp4/json)
  3. 哈希抽样: 同名同扩展文件 md5 一致性 (默认 300 个)
  4. 缺项检查: 旧有新无 / 新有旧无 的包
输出: <新目录>/_compare_report.md
"""
import argparse
import hashlib
import json
import os
import random
from collections import Counter

EXT_INTEREST = (".png", ".jpg", ".jpeg", ".webp", ".ogg", ".wav", ".vorbis",
                ".obj", ".ttf", ".mp4", ".json", ".txt", ".bin")


def walk_stats(root):
    """返回 (文件数, 总大小, 扩展名计数)"""
    n = 0
    size = 0
    ext = Counter()
    for dirpath, _, fns in os.walk(root):
        for fn in fns:
            p = os.path.join(dirpath, fn)
            try:
                size += os.path.getsize(p)
            except OSError:
                continue
            n += 1
            ext[os.path.splitext(fn)[1].lower()] += 1
    return n, size, ext


def md5(p, chunk=1 << 20):
    h = hashlib.md5()
    try:
        with open(p, "rb") as f:
            while True:
                b = f.read(chunk)
                if not b:
                    break
                h.update(b)
        return h.hexdigest()
    except OSError:
        return None


def index_by_name(root, exts):
    """name -> [相对路径...] (同名文件可能有多个)"""
    idx = {}
    for dirpath, _, fns in os.walk(root):
        for fn in fns:
            if os.path.splitext(fn)[1].lower() in exts:
                idx.setdefault(fn, []).append(os.path.join(dirpath, fn))
    return idx


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", required=True)
    ap.add_argument("--new", required=True)
    ap.add_argument("--sample", type=int, default=300)
    args = ap.parse_args()
    old_root, new_root = args.old.rstrip("/\\"), args.new.rstrip("/\\")
    lines = [f"# 新旧解包完整度对比", "",
             f"- 旧: {old_root}", f"- 新: {new_root}", "",
             f"生成时间: 2026-08-16 (compare_extract.py)", ""]

    # 1) 按包统计
    lines += ["## 1. 按包统计 (_stats.json)", "", "| 包 | 对象 | 导出 | JSON | fail |", "|---|---|---|---|---|"]
    old_stats = new_stats = {}
    osp = os.path.join(old_root, "_stats.json")
    nsp = os.path.join(new_root, "_stats.json")
    if os.path.exists(osp):
        old_stats = json.load(open(osp, encoding="utf-8"))
    if os.path.exists(nsp):
        new_stats = json.load(open(nsp, encoding="utf-8"))
    for pkg in sorted(set(old_stats) | set(new_stats)):
        o, n = old_stats.get(pkg, {}), new_stats.get(pkg, {})
        lines.append(f"| {pkg} | {o.get('objects','-')} / {n.get('objects','-')} | "
                     f"{o.get('exported','-')} / {n.get('exported','-')} | "
                     f"{o.get('json','-')} / {n.get('json','-')} | "
                     f"{o.get('fail','-')} / {n.get('fail','-')} |")
    # fail 汇总
    o_fail = sum(s.get("fail", 0) for s in old_stats.values())
    n_fail = sum(s.get("fail", 0) for s in new_stats.values())
    lines.append("")
    lines.append(f"fail 合计: 旧 {o_fail} / 新 {n_fail}")

    # 2) 文件规模
    lines += ["", "## 2. 文件规模", ""]
    for tag, root in (("旧", old_root), ("新", new_root)):
        n, size, ext = walk_stats(root)
        lines.append(f"- **{tag}**: 文件 {n:,}, 总大小 {size/1e6:.0f}MB")
        interesting = {k: v for k, v in sorted(ext.items()) if k in EXT_INTEREST}
        lines.append(f"  关键扩展名: {interesting}")
    lines.append("")

    # 3) 哈希抽样对比 (同名同扩展)
    lines += ["", "## 3. 哈希抽样 (同名文件 md5 一致性)", ""]
    old_idx = index_by_name(old_root, set(EXT_INTEREST))
    new_idx = index_by_name(new_root, set(EXT_INTEREST))
    common = sorted(set(old_idx) & set(new_idx))
    if common:
        sample = random.sample(common, min(args.sample, len(common)))
        match = 0
        diff = []
        for fn in sample:
            o, n = old_idx[fn][0], new_idx[fn][0]
            ho, hn = md5(o), md5(n)
            if ho == hn and ho is not None:
                match += 1
            else:
                diff.append(fn)
        lines.append(f"抽样 {len(sample)} 个同名文件: md5 一致 {match}, 不一致 {len(diff)}")
        for fn in diff[:10]:
            lines.append(f"  - 差异: {fn}")
    else:
        lines.append("无可比同名文件")

    # 4) 缺项
    lines += ["", "## 4. 包级缺项", ""]
    missing_old = sorted(set(old_stats) - set(new_stats))
    missing_new = sorted(set(new_stats) - set(old_stats))
    lines.append(f"- 旧有新无: {missing_old or '无'}")
    lines.append(f"- 新有旧无: {missing_new or '无'}")

    report = os.path.join(new_root, "_compare_report.md")
    with open(report, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"\n报告: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
