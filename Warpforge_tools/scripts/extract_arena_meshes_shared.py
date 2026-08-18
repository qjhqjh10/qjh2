#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_arena_meshes_shared.py — 从 battlesharedresources bundle 导出 4 个场景引用的 Mesh -> OBJ
输出: d:/2/解包整理/06_模型/scenes_scenes_<arena>/
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import UnityPy

ARENAS = ['battlearena3', 'battlearenaaeldari', 'battlearenaleviathan', 'battlearenasororitas']
SHARED = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/battlesharedresources_assets_all.bundle'
SCENE_ROOT = 'd:/2/解包整理/07_场景/'
OUT_ROOT = 'd:/2/解包整理/06_模型/'


def main() -> int:
    want = {}
    for arena in ARENAS:
        pids = set()
        d = os.path.join(SCENE_ROOT, arena, 'MeshFilter')
        for fn in os.listdir(d):
            if not fn.endswith('.json'):
                continue
            with open(os.path.join(d, fn), encoding='utf-8') as f:
                data = json.load(f)
            m = data.get('m_Mesh')
            if m and m.get('m_FileID') != 0:
                pids.add(m['m_PathID'])
        want[arena] = pids

    env = UnityPy.load(SHARED)
    mesh_obj = {}
    for o in env.objects:
        if o.type.name != 'Mesh':
            continue
        mesh_obj[o.path_id] = o

    total = 0
    for arena, pids in want.items():
        out = os.path.join(OUT_ROOT, 'scenes_scenes_' + arena)
        os.makedirs(out, exist_ok=True)
        n = 0
        for pid in sorted(pids):
            o = mesh_obj.get(pid)
            if o is None:
                print(f'  缺失 pid {pid} 在 {arena}')
                continue
            try:
                name = str(o.read().m_Name)
            except Exception:
                name = str(pid)
            fname = name.replace('/', '_')[:80]
            fp = os.path.join(out, fname + '.obj')
            if os.path.exists(fp):
                n += 1
                continue
            try:
                raw = o.read().export()
            except Exception as e:
                print(f'  export 失败 {fname}: {e}')
                continue
            if not raw:
                print(f'  export 空 {fname}')
                continue
            with open(fp, 'w', encoding='utf-8', errors='replace') as f:
                f.write(raw)
            n += 1
        print(f'✓ {arena}: {n}/{len(pids)} 个 OBJ -> {out}')
        total += n
    print(f'共导出 {total} 个')
    return 0


if __name__ == '__main__':
    sys.exit(main())
