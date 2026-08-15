#!/usr/bin/env python3
"""Summarize per-bundle key content from enum_result.json.
Superseded by verify_extract.py; kept for historical checks."""
import json, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "enum_result.json")

data = json.load(open(DATA, encoding="utf-8"))

tot = Counter()
per_file = {}
for entry in data:
    if "error" in entry:
        print("ERROR", entry["file"], entry["error"]); continue
    per_file[entry["file"]] = entry["counts"]
    for cls, n in entry["counts"].items():
        tot[cls] += n

print("=== SOURCE TOTALS (all files) ===")
for cls, n in sorted(tot.items(), key=lambda x: -x[1]):
    if n > 0:
        print(f"  {cls}: {n}")

print("\n=== PER-BUNDLE key content (Texture2D | AudioClip | Mesh | Font | Shader | VideoClip | Sprite | GameObject | Material | MonoBehaviour | TextAsset | AnimationClip) ===")
keys = ["Texture2D","AudioClip","Mesh","Font","Shader","VideoClip","Sprite","GameObject","Material","MonoBehaviour","TextAsset","AnimationClip"]
for fn in sorted(per_file):
    c = per_file[fn]
    if not c:
        continue
    parts = [f"{k}={c.get(k,0)}" for k in keys if c.get(k,0)]
    if parts:
        print(f"  {fn[:60]:60s} " + " ".join(parts))
