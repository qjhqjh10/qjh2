#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全库 PNG 新旧对比: 解包整理(旧) vs 新解包资源(新) — 按文件名索引 + md5 比对
输出差异清单: 同名不同内容(=被修改) / 仅旧有(=改/删) / 仅新有
"""
import os, hashlib, json, glob

OLD = r"d:/2/解包整理"
NEW = r"d:/2/新解包资源/assets_full"
OUT = r"d:/2/新解包资源/png_diff_report.txt"

def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def index(root):
    idx = {}  # basename -> list[(path, md5, size)]
    for p in glob.glob(os.path.join(root, "**", "*.png"), recursive=True):
        b = os.path.basename(p)
        try:
            d = md5(p)
        except Exception:
            continue
        if b not in idx:
            idx[b] = []
        idx[b].append((p, d, os.path.getsize(p)))
    return idx

print("[1/3] 索引旧库...", flush=True)
old_idx = index(OLD)
print(f"  旧库 PNG: {sum(len(v) for v in old_idx.values())}", flush=True)
print("[2/3] 索引新库...", flush=True)
new_idx = index(NEW)
print(f"  新库 PNG: {sum(len(v) for v in new_idx.values())}", flush=True)

lines = []
# 同名比对: 名称集合
old_names = set(old_idx); new_names = set(new_idx)
only_old = old_names - new_names
only_new = new_names - old_names
both = old_names & new_names
mod = 0; same = 0
for b in sorted(both):
    om = {x[1] for x in old_idx[b]}   # 旧 md5 集合
    nm = {x[1] for x in new_idx[b]}
    if not (om & nm):  # 无共同 md5 → 内容全不同
        mod += 1
        lines.append(f"【被修改?】{b}\n    旧:{len(om)}版本 新:{len(nm)}版本\n")
    else:
        same += 1
# 旧有但新无 (可能被改名)
missing = []
for b in sorted(only_old):
    missing.append(b)
lines.insert(0, f"同名且内容一致: {same} | 同名但内容不同: {mod} | 仅旧有: {len(only_old)} | 仅新有: {len(only_new)}\n")
lines.append(f"\n=== 仅旧有(新库无同名, 疑似改名/删除, 前300) ===\n")
lines.extend(missing[:300])
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"[3/3] 完成 → {OUT}")
