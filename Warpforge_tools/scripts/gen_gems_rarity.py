#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""宝石稀有度表 → 项目数据 (2026-08-24 定案: 宝石色=稀有度权威)
输入: D:\\2\\Warpforge部队卡片\\卡牌宝石稀有度_0824.md
输出: D:\\warpforge\\data\\gems_rarity.json  {"cards": {卡名: {"gem": 宝石色, "rarity": 稀有度}}}
"""
import json, re

SRC = r"D:/2/Warpforge部队卡片/卡牌宝石稀有度_0824.md"
OUT = r"D:/warpforge/data/gems_rarity.json"

out = {}
n = 0
for line in open(SRC, encoding="utf-8"):
    m = re.match(r"^\|\s*(\w)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|", line)
    if not m:
        continue
    _, fname, cname, gem, rarity = m.groups()
    cname, gem, rarity = cname.strip(), gem.strip(), rarity.strip()
    if gem == "宝石色" or not gem:
        continue
    out[cname] = {"gem": gem, "rarity": rarity}
    n += 1

json.dump({"cards": out}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"written {OUT}: {n} cards")
