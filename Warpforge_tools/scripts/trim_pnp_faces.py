#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trim_pnp_faces.py — 批量裁掉 PnP 卡面四周透明边距 (卡图破框立绘外是透明区, 非白圈)
2026-08-21: 原版卡面 Sprite textureRect 已裁透明边 (如 Nork 裁左 176.5px), 项目直接用整图
导致卡面"缩在框内/位置偏"、破框张力丢失。本脚本按 alpha>8 边界裁切后覆盖 faces + faces_thumbs。
用法: py312 trim_pnp_faces.py [目录]  — 默认 d:/warpforge/assets/cards/
"""
import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

BASE = sys.argv[1] if len(sys.argv) > 1 else 'D:/warpforge/assets/cards'
FACES = os.path.join(BASE, 'faces')
THUMBS = os.path.join(BASE, 'faces_thumbs')
ALPHA = 8   # alpha 阈值 (内容/噪点)

def trim_bounds(img):
    """按 alpha>ALPHA 的边界裁切 → (box, 原尺寸)"""
    w, h = img.size
    px = img.load()
    minx, miny, maxx, maxy = w, h, -1, -1
    step = 2
    for y in range(0, h, step):
        for x in range(0, w, step):
            a = px[x, y][3]
            if a > ALPHA:
                if x < minx: minx = x
                if x > maxx: maxx = x
                if y < miny: miny = y
                if y > maxy: maxy = y
    if maxx < 0:
        return None   # 全透明
    # 边界精确化: 在粗扫边界附近逐像素精扫
    for x in range(maxx + 1, min(w, maxx + step)):
        for y in range(miny, min(h, maxy + 1), 1):
            if px[x, y][3] > ALPHA: maxx = x
    for x in range(minx - 1, max(-1, minx - step), -1):
        for y in range(miny, min(h, maxy + 1), 1):
            if px[x, y][3] > ALPHA: minx = x
    for y in range(maxy + 1, min(h, maxy + step)):
        for x in range(minx, min(w, maxx + 1), 1):
            if px[x, y][3] > ALPHA: maxy = y
    for y in range(miny - 1, max(-1, miny - step), -1):
        for x in range(minx, min(w, maxx + 1), 1):
            if px[x, y][3] > ALPHA: miny = y
    return (minx, miny, maxx + 1, maxy + 1)

def main():
    total = skipped = trimmed = 0
    stats = []
    for root, _, files in os.walk(FACES):
        for fn in sorted(files):
            if not fn.lower().endswith('.png'):
                continue
            total += 1
            path = os.path.join(root, fn)
            img = Image.open(path).convert('RGBA')
            box = trim_bounds(img)
            if box is None:
                skipped += 1
                continue
            w, h = img.size
            if box == (0, 0, w, h):
                skipped += 1
                continue
            trimmed += 1
            nw, nh = box[2] - box[0], box[3] - box[1]
            # 边距占比 (只裁 >1% 的边)
            left, top = box[0] / w, box[1] / h
            right, bottom = (w - box[2]) / w, (h - box[3]) / h
            if max(left, top, right, bottom) < 0.01:
                skipped += 1
                continue
            cropped = img.crop(box)
            cropped.save(path)
            stats.append((fn, round(left * 100, 1), round(top * 100, 1),
                          round(right * 100, 1), round(bottom * 100, 1)))
    print(f'faces: 总 {total} / 裁切 {trimmed} / 跳过 {skipped}')
    for s in stats[:8]:
        print(f'  {s[0]}: 左{s[1]}% 上{s[2]}% 右{s[3]}% 下{s[4]}%')
    if len(stats) > 8:
        print(f'  ... 共 {len(stats)} 张被裁')
    # 缩略图同步 (同一文件名)
    thumb_trimmed = 0
    for root, _, files in os.walk(THUMBS):
        for fn in sorted(files):
            if not fn.lower().endswith('.png'):
                continue
            path = os.path.join(root, fn)
            img = Image.open(path).convert('RGBA')
            box = trim_bounds(img)
            if box is None or box == (0, 0, img.size[0], img.size[1]):
                continue
            img.crop(box).save(path)
            thumb_trimmed += 1
    print(f'faces_thumbs: 裁切 {thumb_trimmed}')

if __name__ == '__main__':
    main()
