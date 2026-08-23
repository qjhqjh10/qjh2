# -*- coding: utf-8 -*-
"""particles3d JSON 贴图四角 alpha 检测: 损坏贴图 (四角 alpha>200) → texture 置空 (soft_dot 降级)
用法: py312/python.exe scripts/fix_broken_tex_refs.py"""
import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ASSETS = r'd:\warpforge\assets\particles'
JSON3D = r'd:\warpforge\data\particles3d'

from PIL import Image

fixed = 0
for fp in glob.glob(os.path.join(JSON3D, '*.json')):
    d = json.load(open(fp, encoding='utf-8'))
    tex = d.get('texture', '')
    if not tex:
        continue
    p = os.path.join(ASSETS, os.path.basename(tex))
    if not os.path.exists(p):
        d['texture'] = ''
        fixed += 1
        print(f'{os.path.basename(fp)}: 贴图缺失 -> soft_dot')
        json.dump(d, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        continue
    img = Image.open(p).convert('RGBA')
    w, h = img.size
    corners = [img.getpixel((0, 0))[3], img.getpixel((w-1, 0))[3],
               img.getpixel((0, h-1))[3], img.getpixel((w-1, h-1))[3]]
    if all(a > 200 for a in corners):
        d['texture'] = ''
        fixed += 1
        print(f'{os.path.basename(fp)}: 四角alpha {corners} 损坏 -> soft_dot')
        json.dump(d, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'共修复 {fixed} 个 JSON')
