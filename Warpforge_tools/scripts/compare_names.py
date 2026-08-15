#!/usr/bin/env python3
"""Compare extraction coverage: source enumeration vs extracted files (flat or per-bundle dirs).
Superseded by verify_extract.py for the current per-bundle layout; kept for historical checks."""
import json, os, re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "enum_names.json")
FULL = r"d:/2/Warpforge_assets_full"   # current extraction (per-bundle dirs)
OLD = r"d:/2/Warpforge_assets/Assets"   # old flat extraction (deleted; only if re-created)

data = json.load(open(DATA, encoding="utf-8"))

def collect_stems(root):
    stems = Counter()
    if not os.path.isdir(root):
        return stems
    for dirpath, _, files in os.walk(root):
        for f in files:
            stem = f.rsplit(".", 1)[0] if "." in f else f
            stems[stem] += 1
    return stems

def norm(s):
    if not s:
        return None
    return s.replace("\\", "/")

def report(extract_root, label):
    ext_stems = collect_stems(extract_root)
    print(f"=== {label} ===")
    tot_so, tot_found = 0, 0
    for e in data:
        if "error" in e or not e["so_names"]:
            continue
        so = e["so_names"]
        found = sum(1 for n in so if n and n in ext_stems)
        tot_so += len(so); tot_found += found
        pct = 100.0 * found / len(so) if so else 0
        flag = "OK" if pct >= 95 else ("PARTIAL" if pct >= 50 else "MISSING")
        print(f"  {e['file'][:58]:58s} SO={len(so):6d} found={found:6d} {pct:5.1f}%  {flag}")
    print(f"\nTOTAL SOs: {tot_so}, matched: {tot_found} ({100.0*tot_found/tot_so:.1f}%)\n")

report(OLD, "OLD flat extraction (needs d:/2/Warpforge_assets to exist)")
report(FULL, "CURRENT per-bundle extraction")
