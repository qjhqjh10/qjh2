#!/usr/bin/env python3
"""Post-extraction verification: per-bundle coverage vs source enumeration."""
import json, os
from collections import Counter

data = json.load(open(r"d:/2/enum_names.json", encoding="utf-8"))
src_types = json.load(open(r"d:/2/enum_result.json", encoding="utf-8"))
FULL = r"d:/2/Warpforge_assets_full"

# build per-source-file object type counts from enum_result
src = {}
for e in src_types:
    if "error" in e:
        continue
    src[e["file"]] = e["counts"]

# extraction: per output dir, count files by extension and class subfolder
ext = {}
for d in os.listdir(FULL):
    dd = os.path.join(FULL, d)
    if not os.path.isdir(dd):
        continue
    counts = Counter()
    for cls in os.listdir(dd):
        cdir = os.path.join(dd, cls)
        if not os.path.isdir(cdir):
            continue
        n = len(os.listdir(cdir))
        counts[cls] = n
    ext[d] = counts

rows = []
for file, counts in src.items():
    stem = os.path.splitext(file)[0].replace(":", "_")
    e = ext.get(stem)
    if e is None:
        rows.append((file, counts, None))
        continue
    rows.append((file, counts, e))

print(f"{'SOURCE FILE':68s} {'TEX':>5s} {'AUD':>5s} {'MSH':>5s} {'SO/MB':>7s} {'GO':>6s} {'MAT':>5s} | extracted: tex aud mesh so/mb go mat")
for file, c, e in rows:
    tex_s, aud_s, msh_s, so_s, go_s, mat_s = (c.get(k, 0) for k in
        ("Texture2D", "AudioClip", "Mesh", "MonoBehaviour", "GameObject", "Material"))
    if e is None:
        print(f"{file[:68]:68s} {tex_s:5d} {aud_s:5d} {msh_s:5d} {so_s:7d} {go_s:6d} {mat_s:5d} | ** NOT EXTRACTED **")
        continue
    tex_e = e.get("Texture2D", 0) + e.get("Sprite", 0)  # textures+sprites both png/json
    aud_e = e.get("AudioClip", 0)
    msh_e = e.get("Mesh", 0)
    so_e = e.get("MonoBehaviour", 0)
    go_e = e.get("GameObject", 0)
    mat_e = e.get("Material", 0)
    print(f"{file[:68]:68s} {tex_s:5d} {aud_s:5d} {msh_s:5d} {so_s:7d} {go_s:6d} {mat_s:5d} | {tex_e:5d} {aud_e:5d} {msh_e:5d} {so_e:7d} {go_e:6d} {mat_e:5d}")

# totals
print("\n=== TOTALS ===")
t_src = Counter()
t_ext = Counter()
for file, c, e in rows:
    for k, v in c.items():
        t_src[k] += v
    if e:
        for k, v in e.items():
            t_ext[k] += v
for k in ("Texture2D", "Sprite", "SpriteAtlas", "AudioClip", "Mesh", "MonoBehaviour",
          "GameObject", "Material", "AnimationClip", "Shader", "Font", "TextAsset", "VideoClip"):
    s, x = t_src.get(k, 0), t_ext.get(k, 0)
    pct = 100.0 * x / s if s else 0
    print(f"  {k:16s} source={s:6d} extracted={x:6d} ({pct:.1f}%)")
