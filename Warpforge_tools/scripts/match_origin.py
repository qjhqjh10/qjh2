#!/usr/bin/env python3
"""Match extraction file stems against source SO names per bundle (origin tracing)."""
import json, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "enum_names.json")
EXTRACT = r"d:/2/Warpforge_assets_full"

data = json.load(open(DATA, encoding="utf-8"))

files = []
for dirpath, _, fns in os.walk(EXTRACT):
    for f in fns:
        stem = f.rsplit(".", 1)[0] if "." in f else f
        files.append(stem)
json_stems = set(files)

matched_by_bundle = Counter()
for e in data:
    short = e["file"]
    so_names = e.get("so_names") or []
    found_so = [n for n in so_names if n and n in json_stems]
    for n in found_so:
        matched_by_bundle[short] += 1

print("=== extraction stems matched to SO names per bundle ===")
for k, v in matched_by_bundle.most_common():
    print(f"  {v:6d}  {k}")

print(f"\nmatched: {sum(matched_by_bundle.values())}, total stems: {len(json_stems)}")
