#!/usr/bin/env python3
"""Refined per-bundle enumeration: SO vs component, and names of key assets.
Writes enum_names.json (per-file SO names + asset type names)."""
import os, json
from collections import Counter
import UnityPy

GAME = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data"
BUNDLES = os.path.join(GAME, "StreamingAssets", "aa", "StandaloneWindows64")
OUTJSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "enum_names.json")

def enum_file(path, short):
    try:
        env = UnityPy.load(path)
    except Exception as e:
        return {"file": short, "error": str(e)[:150]}
    so_names, comp_count = [], 0
    names = {"Texture2D": [], "AudioClip": [], "Mesh": [], "Sprite": [], "Font": [], "Shader": [], "VideoClip": []}
    for obj in env.objects:
        tn = obj.type.name
        if tn == "MonoBehaviour":
            try:
                d = obj.read()
                if hasattr(d, "m_GameObject") and d.m_GameObject and getattr(d.m_GameObject, "m_PathID", 0):
                    comp_count += 1
                elif len(so_names) < 20000:
                    so_names.append(getattr(d, "m_Name", None) or "<null>")
            except Exception:
                comp_count += 1
        elif tn in names and len(names[tn]) < 20000:
            try:
                n = obj.read().m_Name or ""
                names[tn].append(n)
            except Exception:
                names[tn].append("")
    return {"file": short, "so_count": len(so_names), "component_count": comp_count,
            "so_names": so_names, "asset_names": names}

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
        out.append(enum_file(path, short))
    os.makedirs(os.path.dirname(OUTJSON), exist_ok=True)
    with open(OUTJSON, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print("DONE ->", OUTJSON)
