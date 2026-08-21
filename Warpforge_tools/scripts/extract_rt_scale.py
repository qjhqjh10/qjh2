#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_rt_scale.py — 从游戏本体 bundle 提取所有 RectTransform 的 m_LocalScale (≠1) 映射
输出: D:/2/Warpforge_tools/data/ui_layout/rt_scale_map.json  {pid: {x, y}}
用途: chain_rect.py 读取此映射补 scale (JSON 导出丢失 Transform 字段, 坑 37)
"""
import UnityPy, json, os, sys

sys.stdout.reconfigure(encoding='utf-8')
BUNDLE_DIR = "D:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64"
OUT = "D:/2/Warpforge_tools/data/ui_layout/rt_scale_map.json"

scale_map = {}
scanned = 0
for f in sorted(os.listdir(BUNDLE_DIR)):
    if not f.endswith('.bundle'):
        continue
    try:
        env = UnityPy.load(os.path.join(BUNDLE_DIR, f))
    except Exception:
        continue
    for obj in env.objects:
        if obj.type.name != 'RectTransform':
            continue
        try:
            tree = obj.read_typetree()
        except Exception:
            continue
        sc = tree.get('m_LocalScale') or {}
        sx = sc.get('x', 1)
        sy = sc.get('y', 1)
        if abs(sx - 1) > 1e-4 or abs(sy - 1) > 1e-4:
            scale_map[str(obj.path_id)] = {"x": round(sx, 6), "y": round(sy, 6)}
        scanned += 1
print('扫描 RectTransform 总数:', scanned)
print('非 1 scale 节点数:', len(scale_map))
json.dump(scale_map, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('已输出:', OUT)
