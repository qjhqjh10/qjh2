#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_ui_bundle.py — 从游戏本体 AssetBundle 提取 UI 纹理/Sprite (补解 03_界面UI 缺失资源)
来源: d:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/*.bundle
输出: d:/2/Warpforge_tools/data/ui_extract/<bundle名>/
      - Texture2D/*.png   (含 Sprite 切片 JSON: Sprite/<名>.json 带 rect)
用法: d:/2/Warpforge_tools/py312/python.exe extract_ui_bundle.py [bundle名...]
      (默认: menus_assets_all mainmenualwaysloaded_assets_all menusharedresources_assets_all)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
OUT_DIR = 'd:/2/Warpforge_tools/data/ui_extract/'

DEFAULTS = ['menus_assets_all', 'mainmenualwaysloaded_assets_all',
            'menusharedresources_assets_all']


def main() -> int:
    names = sys.argv[1:] or DEFAULTS
    import UnityPy
    total_tex = 0
    total_spr = 0
    for name in names:
        path = os.path.join(BUNDLE_DIR, name + '.bundle')
        if not os.path.exists(path):
            print(f'[跳过] {path} 不存在')
            continue
        out = os.path.join(OUT_DIR, name)
        os.makedirs(os.path.join(out, 'Texture2D'), exist_ok=True)
        os.makedirs(os.path.join(out, 'Sprite'), exist_ok=True)
        n_tex = 0
        n_spr = 0
        try:
            env = UnityPy.load(path)
        except Exception as e:
            print(f'[错误] {name}: {e}')
            continue
        for obj in env.objects:
            try:
                t = obj.type.name
                if t == 'Texture2D':
                    data = obj.read()
                    fname = data.m_Name
                    if not fname:
                        continue
                    img = data.image
                    dest = os.path.join(out, 'Texture2D', fname + '.png')
                    if not os.path.exists(dest):
                        img.save(dest)
                        n_tex += 1
                elif t == 'Sprite':
                    data = obj.read()
                    sname = data.m_Name
                    if not sname:
                        continue
                    # 用 UnityPy 的 image 属性 (自动处理图集 UV/rect 裁切)
                    dest = os.path.join(out, 'Sprite', sname + '.png')
                    if not os.path.exists(dest):
                        img = data.image
                        if img is not None:
                            img.save(dest)
                            n_spr += 1
                    # 仍存 rect 信息 + PathID (供布局解析器反查)
                    rect = data.m_Rect
                    info = {'m_Name': sname,
                            'pathid': getattr(obj, 'path_id', None),
                            'm_Rect': {'x': rect.x, 'y': rect.y,
                                       'width': rect.width, 'height': rect.height},
                            'm_AtlasTags': ['Atlas'],
                            'textureRect': {'x': rect.x, 'y': rect.y,
                                            'width': rect.width, 'height': rect.height}}
                    dest = os.path.join(out, 'Sprite', sname + '.json')
                    if not os.path.exists(dest):
                        with open(dest, 'w', encoding='utf-8') as f:
                            json.dump(info, f, ensure_ascii=False, indent=1)
            except Exception:
                continue
        total_tex += n_tex
        total_spr += n_spr
        print(f'✓ {name}: 纹理 {n_tex} / Sprite {n_spr} -> {out}')
    print(f'完成: 纹理 {total_tex}, Sprite {total_spr}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
