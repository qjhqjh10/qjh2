#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""无数值卡清单 (2026-08-24, 用户"拉清单逐张确认"裁决)
判据: card_stats.json 中 noise!=true 且 hasStats!=true (= GameData 运行时判据;
    运行时日志 "1192 卡 (1126 有 OCR 数值, 15 噪音剔除)" — 无数值=66)
输出: D:\\2\\87张无数值卡清单_0824.md
"""
import json, sys

IDX = r"D:/2/解包整理/card_index.json"
STATS = r"D:/warpforge/data/card_stats.json"
OUT = r"D:/2/无数值卡清单_0824.md"

idx = json.load(open(IDX, encoding="utf-8"))
stats = json.load(open(STATS, encoding="utf-8"))
idx_by_name = {c.get("name", ""): c for c in idx.get("cards", [])}

rows = []
n_noise = 0
for c in stats.get("cards", []):
    name = c.get("name", "")
    if c.get("noise", False):
        n_noise += 1
        continue
    if c.get("hasStats", False):
        continue
    ic = idx_by_name.get(name, {})
    rows.append({
        "name": name,
        "faction": c.get("faction", ""),
        "factionId": c.get("factionId", ""),
        "type": c.get("type", ""),
        "art": ic.get("art", ""),
        "cost": c.get("cost", ""),
        "rarity": c.get("rarity", ""),
    })

rows.sort(key=lambda r: (r["faction"], r["name"]))
lines = [
    "# 无数值卡清单 (2026-08-24)",
    "",
    "> 判据: card_stats.json noise!=true 且 hasStats!=true (GameData 运行时同判据)",
    f"> 无数值卡合计: {len(rows)} (噪音剔除 {n_noise} 张不在此列)",
    "",
    "| # | 卡名 | 阵营 | 类型 | 卡面(相对解包整理/) | cost | rarity |",
    "|---|---|---|---|---|---|---|",
]
for i, r in enumerate(rows, 1):
    art = r["art"].replace("01_卡牌\\", "").replace("01_卡牌/", "")
    lines.append(f"| {i} | {r['name']} | {r['faction']} | {r['type']} | {art} | {r['cost']} | {r['rarity']} |")

open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"written {OUT}: {len(rows)} rows, noise={n_noise}")
