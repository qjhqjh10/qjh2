#!/usr/bin/env python3
"""Map extraction jsons and source SOs to script class names via the monoscripts bundle.
Classifies what each extracted JSON actually is (Sprite/MonoBehaviour/Shader/...)."""
import json, os, re
from collections import Counter, defaultdict
import UnityPy

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "enum_names.json")
BUNDLES = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64"
GAME = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data"
EXTRACT = r"d:/2/Warpforge_assets_full"

def load_monoscript_map():
    path = os.path.join(BUNDLES, "Waprforge_monoscripts.bundle")
    env = UnityPy.load(path)
    m = {}
    for obj in env.objects:
        if obj.type.name == "MonoScript":
            try:
                d = obj.read()
                m[obj.path_id] = getattr(d, "m_ClassName", "?")
            except Exception:
                pass
    return m

ms_map = load_monoscript_map()
print("MonoScripts:", len(ms_map))

def script_class_of_json(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            content = f.read()
        m = re.search(r'"m_Script"\s*:\s*\{\s*"m_Collection"\s*:\s*"(?:cab-[a-f0-9]+)?",\s*"m_PathID"\s*:\s*(-?\d+)', content)
        if m:
            return ms_map.get(int(m.group(1)), f"script#{m.group(1)}")
    except Exception:
        pass
    return None

if __name__ == "__main__":
    ext_classes = Counter()
    ext_unparsed = []
    for dirpath, _, files in os.walk(EXTRACT):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            c = script_class_of_json(os.path.join(dirpath, fn))
            if c:
                ext_classes[c] += 1
            else:
                ext_unparsed.append(fn)
    print("\n=== EXTRACTED json classes (top 40) ===")
    for c, n in ext_classes.most_common(40):
        print(f"  {n:6d}  {c}")
    print(f"  unparsed (no m_Script): {len(ext_unparsed)}")
