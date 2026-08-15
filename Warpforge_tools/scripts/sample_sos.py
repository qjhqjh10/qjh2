#!/usr/bin/env python3
"""Sample SO names from key bundles (cosmetics, draftpacks, cardanims, menus...)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "enum_names.json")

data = json.load(open(DATA, encoding="utf-8"))

KEY = ["cosmeticsso", "draftpacks", "prebuiltdecks", "cardanimsgeneral",
       "soundcollection", "tweenandshakes", "menus_assets_all", "staticgeneralassets",
       "battleprefabs", "resources.assets", "sharedassets0", "duplicateassetisolation"]

for e in data:
    short = e["file"]
    if not any(k in short for k in KEY):
        continue
    so = e["so_names"]
    print(f"=== {short} (SOs={len(so)}) ===")
    for n in so[:25]:
        print(f"   {repr(n)}")
    print()
