#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scan_bundles_scenes.py — 全量扫描 bundle 的 GameObject 名称, 找场景所在"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
KEYWORDS = sys.argv[1:] or ['chat tab', 'rowbackground', 'sender', 'friend header']


def main() -> int:
    import UnityPy
    for f in sorted(os.listdir(BUNDLE_DIR)):
        if not f.endswith('.bundle'):
            continue
        try:
            env = UnityPy.load(os.path.join(BUNDLE_DIR, f))
        except Exception:
            continue
        names = set()
        for obj in env.objects:
            try:
                if obj.type.name == 'GameObject':
                    nm = obj.read_typetree().get('m_Name', '')
                    if nm:
                        names.add(nm)
            except Exception:
                continue
        hits = [n for n in names if any(k.lower() in n.lower() for k in KEYWORDS)]
        if hits:
            print(f'◆ {f}: {sorted(hits)[:15]}')
    print('扫描完成')
    return 0


if __name__ == '__main__':
    sys.exit(main())
