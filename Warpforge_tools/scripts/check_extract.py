#!/usr/bin/env python3
"""Enumerate Unity asset files/bundles: per-file type counts + SO/MB names.
Writes enum_result.json (per-file object-type counts)."""
import os, sys, json
from collections import Counter
import UnityPy

GAME = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data"
BUNDLES = os.path.join(GAME, "StreamingAssets", "aa", "StandaloneWindows64")
OUTJSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "enum_result.json")

def enumerate_file(path, short):
    try:
        env = UnityPy.load(path)
    except Exception as e:
        return {"file": short, "error": str(e)[:120]}
    counts = Counter()
    so_names = []
    total = 0
    for obj in env.objects:
        total += 1
        counts[obj.type.name] += 1
        if obj.type.name in ("MonoBehaviour", "ScriptableObject", "TextAsset") and len(so_names) < 4000:
            try:
                so_names.append(obj.read().m_Name or "<null>")
            except Exception:
                pass
    return {"file": short, "objects": total, "counts": dict(counts), "so_names": so_names}

if __name__ == "__main__":
    files = []
    for fn in sorted(os.listdir(GAME)):
        if fn.endswith((".assets", ".resource", "globalgamemanagers", "level0", "level1")) or fn.startswith("sharedassets"):
            files.append((os.path.join(GAME, fn), fn))
    for fn in sorted(os.listdir(BUNDLES)):
        if fn.endswith(".bundle"):
            files.append((os.path.join(BUNDLES, fn), "bundle:" + fn))
    out = []
    for i, (path, short) in enumerate(files):
        print(f"[{i+1}/{len(files)}] {short}", flush=True)
        out.append(enumerate_file(path, short))
    os.makedirs(os.path.dirname(OUTJSON), exist_ok=True)
    with open(OUTJSON, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print("DONE ->", OUTJSON)
