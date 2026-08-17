# -*- coding: utf-8 -*-
"""
extract_battle_sprites.py — 提取 battlearena1 场景引用的全部 UI sprite → assets/ui/battle/
原理: 多 bundle 共享 Environment (跨 bundle 解析 cab 纹理)
用法: py312/python.exe scripts/extract_battle_sprites.py
前置: data/ui_extract/battlearena1_sprite_map.json (PathID→sprite名, 已生成)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
OUT_DIR = 'd:/warpforge/assets/ui/battle/'
MAP_FILE = 'd:/2/Warpforge_tools/data/ui_extract/battlearena1_sprite_map.json'


def main() -> int:
    import UnityPy
    mapping = json.load(open(MAP_FILE, encoding='utf-8'))
    print(f'映射 {len(mapping)} 个 sprite')
    env = UnityPy.Environment()
    files = [os.path.join(BUNDLE_DIR, f) for f in os.listdir(BUNDLE_DIR) if f.endswith('.bundle')]
    loaded = 0
    for p in files:
        try:
            env.load_file(p)
            loaded += 1
        except Exception:
            pass
    print(f'加载 {loaded} 个 bundle')
    os.makedirs(OUT_DIR, exist_ok=True)
    n_new, n_have, fail = 0, 0, 0
    for obj in env.objects:
        if obj.type.name != 'Sprite':
            continue
        sname = mapping.get(str(obj.path_id))
        if not sname:
            continue
        fp = os.path.join(OUT_DIR, sname + '.png')
        if os.path.exists(fp):
            n_have += 1
            continue
        try:
            d = obj.read()
            img = d.image
            if img is None:
                fail += 1
                continue
            img.save(fp)
            n_new += 1
        except Exception:
            fail += 1
    print(f'✓ 新增 {n_new} 张, 已有 {n_have} 张, 失败 {fail} -> {OUT_DIR}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
