#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_scene_sprites.py — 跨 bundle 提取场景引用的全部 Sprite 图像
原理: UnityPy 多文件共用一个 Environment 时, Sprite.image 可跨 bundle 解析 cab 纹理
用法: d:/2/Warpforge_tools/py312/python.exe extract_scene_sprites.py <场景bundle名> [更多bundle名...]
输出: data/ui_extract/<场景名>_sprites/<sprite名>.png (+json 含 pathid)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
OUT_DIR = 'd:/2/Warpforge_tools/data/ui_extract/'
# 默认加载: 主菜单相关 bundle 集 (共享 cab 纹理)
DEFAULT_BUNDLES = [
    'scenes_scenes_mainmenuwarpforge', 'mainmenualwaysloaded_assets_all',
    'menus_assets_all', 'menusharedresources_assets_all',
    'atlasindividual_assets_0_mainmenu', 'atlasgroup_assets_all',
    'duplicateassetisolation_assets_all', 'cosmeticavatarsimages_assets_all',
    'generalgamewindows_assets_all', 'armyicons_assets_all',
]


def main() -> int:
    import UnityPy
    scene = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_BUNDLES[0]
    bundles = [scene] + (sys.argv[2:] or [b for b in DEFAULT_BUNDLES if b != scene])
    files = [os.path.join(BUNDLE_DIR, b + '.bundle') for b in bundles]
    missing = [f for f in files if not os.path.exists(f)]
    if missing:
        print('[跳过缺失]', missing)
    print(f'加载 {len(files)} 个 bundle (共享环境, 跨 bundle 解析 cab)...')
    env = UnityPy.Environment()
    for f in files:
        if os.path.exists(f):
            try:
                env.load_file(f)
            except Exception as e:
                print(f'  [跳过] {os.path.basename(f)}: {e}')
    out = os.path.join(OUT_DIR, scene + '_sprites')
    os.makedirs(os.path.join(out, 'Sprite'), exist_ok=True)
    n = 0
    fail = 0
    for obj in env.objects:
        try:
            if obj.type.name != 'Sprite':
                continue
            d = obj.read()
            sname = d.m_Name
            if not sname:
                continue
            img = d.image
            if img is None:
                fail += 1
                continue
            fp = os.path.join(out, 'Sprite', sname + '.png')
            if not os.path.exists(fp):
                img.save(fp)
                n += 1
            # pathid 索引 json (供布局解析器反查)
            info = {'m_Name': sname, 'pathid': getattr(obj, 'path_id', None)}
            jp = os.path.join(out, 'Sprite', sname + '.json')
            if not os.path.exists(jp):
                with open(jp, 'w', encoding='utf-8') as f:
                    json.dump(info, f, ensure_ascii=False)
        except Exception:
            fail += 1
    print(f'✓ {scene}: 提取 {n} 张, 失败 {fail} -> {out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
