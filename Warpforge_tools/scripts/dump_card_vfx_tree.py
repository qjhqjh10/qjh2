#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dump_card_vfx_tree.py — battleprefabs_vfxandmisc bundle 卡牌动画 VFX 预制体反查评估
输入: card_anim_map.json (动画定义名→GUID) + bundle 文件
输出: D:/warpforge/data/card_vfx_tree.json
      { "<GUID>": {"names": [动画定义名...], "root": "VFX GO 名", "gameobjects": N,
                   "particles": [{"go": 路径, "main": {...}}], "tex": [贴图名...]} }
用途: 评估 400 个 VFX 预制体 → 按卡名转换接线 (任务⑩)
"""
import json
import os
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

BUNDLE = 'D:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/battleprefabs_vfxandmisc_assets_all.bundle'
ANIM_MAP = 'D:/warpforge/data/card_anim_map.json'
OUT = 'D:/warpforge/data/card_vfx_tree.json'


def main() -> int:
    import UnityPy
    env = UnityPy.load(BUNDLE)
    sf = env.file
    cont = sf.container
    by_pathid = {}
    for o in env.objects:
        by_pathid[o.path_id] = o

    am = json.load(open(ANIM_MAP, encoding='utf-8'))
    guid_names = defaultdict(list)
    for fac, defs in am.items():
        if fac.startswith('_'):
            continue
        for name, v in defs.items():
            if isinstance(v, dict) and v.get('guid'):
                guid_names[v['guid']].append('%s:%s' % (fac, name))

    # 构建 GO 子树: path_id -> {name, type, children_transforms}
    go_by_pathid = {}
    trans_children = defaultdict(list)   # transform path_id -> [child transform path_id]
    trans_go = {}                        # transform path_id -> gameobject path_id
    ps_by_go = defaultdict(list)         # gameobject path_id -> [ParticleSystem path_id]
    for o in env.objects:
        t = o.type.name
        if t == 'GameObject':
            try:
                r = o.read()
                go_by_pathid[o.path_id] = str(r.m_Name)
            except Exception:
                pass
        elif t == 'Transform':
            try:
                r = o.read()
                trans_go[o.path_id] = r.m_GameObject.m_PathID
                for c in (r.m_Children or []):
                    trans_children[o.path_id].append(c.m_PathID)
            except Exception:
                pass
        elif t == 'ParticleSystem':
            try:
                r = o.read()
                ps_by_go[r.m_GameObject.m_PathID].append(o.path_id)
            except Exception:
                pass

    out = {}
    n_missing = 0
    total_particles = 0
    for guid, names in guid_names.items():
        pptr = cont.get(guid)
        if not pptr:
            n_missing += 1
            continue
        root_path = pptr.m_PathID
        root_name = go_by_pathid.get(root_path, '?')
        # BFS 沿 Transform 子链
        seen_go = set()
        seen_t = set()
        queue_t = []
        # 根 GO 的 Transform: 遍历所有 transform 找 m_GameObject == root
        for tid, gid in trans_go.items():
            if gid == root_path:
                queue_t.append(tid)
                break
        go_order = []
        particles = []
        while queue_t:
            tid = queue_t.pop(0)
            if tid in seen_t:
                continue
            seen_t.add(tid)
            gid = trans_go.get(tid)
            if gid is None or gid in seen_go:
                continue
            seen_go.add(gid)
            go_order.append(gid)
            for ps in ps_by_go.get(gid, []):
                try:
                    pr = by_pathid[ps].read()
                    main = pr.m_ParticleSystem
                    em = pr.m_Emission
                    sh = pr.m_Shape
                    pts = {'main': {'looping': bool(getattr(main, 'm_Loop', False)),
                                    'duration': getattr(main, 'm_Duration', 0.0),
                                    'startLifetime': str(getattr(main, 'm_StartLifetime', '')),
                                    'startSpeed': str(getattr(main, 'm_StartSpeed', '')),
                                    'maxParticles': getattr(main, 'm_MaxNumParticles', 0)},
                           'emission': getattr(em, 'm_RateOverTime', '') if em else '',
                           'shape': getattr(getattr(sh, 'm_Shape', None), 'm_ShapeType', '') if sh else ''}
                    particles.append({'go': go_by_pathid.get(gid, '?'), 'data': pts})
                    total_particles += 1
                except Exception:
                    particles.append({'go': go_by_pathid.get(gid, '?'), 'data': {}})
            for c in trans_children.get(tid, []):
                if c not in seen_t:
                    queue_t.append(c)
        out[guid] = {
            'names': names,
            'root': root_name,
            'gos': len(go_order),
            'particles': particles,
        }

    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n_ps = sum(len(v['particles']) for v in out.values())
    n_go = sum(v['gos'] for v in out.values())
    print('GUID 总数: %d | bundle 命中: %d (miss %d) | 预制体 GO 总数: %d | 粒子系统总数: %d' % (
        len(guid_names), len(out), n_missing, n_go, n_ps))
    # 规模分布
    sizes = defaultdict(int)
    for v in out.values():
        sizes['1粒子' if len(v['particles']) <= 1 else '2-5' if len(v['particles']) <= 5 else '6+'] += 1
    print('粒子规模分布:', dict(sizes))
    return 0


if __name__ == '__main__':
    sys.exit(main())
