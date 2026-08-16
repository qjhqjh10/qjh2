#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scan_bundles_sprites.py — 扫描所有 bundle 的 Texture2D/Sprite 名称, 按关键字找资源位置"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
KEYWORDS = sys.argv[1:] or ['profile', 'chat', 'border', 'background', 'tab', 'header', 'sender', 'row', 'message']


def main() -> int:
    import UnityPy
    found = {}
    bundles = sorted(f for f in os.listdir(BUNDLE_DIR) if f.endswith('.bundle'))
    for f in bundles:
        try:
            env = UnityPy.load(os.path.join(BUNDLE_DIR, f))
        except Exception:
            continue
        names = set()
        for obj in env.objects:
            try:
                t = obj.type.name
                if t in ('Texture2D', 'Sprite'):
                    names.add(obj.read().m_Name)
            except Exception:
                continue
        hits = [n for n in names if any(k.lower() in n.lower() for k in KEYWORDS)]
        if hits:
            found[f] = sorted(hits)
    for f, hits in sorted(found.items()):
        print(f'◆ {f}:')
        for h in hits[:40]:
            print(f'   {h}')
    print(f'共 {len(found)} 个 bundle 含匹配资源')
    return 0


if __name__ == '__main__':
    sys.exit(main())
