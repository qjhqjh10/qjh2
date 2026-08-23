#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dump_arena_prop_all.py — 解析阵营战场所有带 Mesh 装饰的 GameObject 世界变换 (说明书 Transform 链)
输出: 近场/中景装饰 GO名 -> (world pos, rot euler, scale)
近场判定: x 在 [80, 130] 内 (相机基准 100, 战场区域), 排除 Floor/Ground/Background 等大件
"""
import json
import math
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SCENE_ROOT = 'd:/2/解包整理/07_场景/'
ARENAS = ['battlearena2', 'battlearena3', 'battlearenaaeldari', 'battlearenaastramilitarum',
          'battlearenablacklegion', 'battlearenadarkangels', 'battlearenaemperorschildren',
          'battlearenagenestealers', 'battlearenaleviathan', 'battlearenasororitas',
          'battlearenaspacewolves', 'battlearenatauviorla']
SKIP = ['Floor', 'Ground', 'Background', 'Sky', 'Plane', 'Moon', 'Cave', 'Light shaft', 'LightShaft',
        'Valkyrie', 'Ship', 'Dock', 'Crane', 'Chimera', 'Missiles', 'Buildings', 'Ring', 'Ships',
        'Circle', 'Data', 'Dynamic', 'Candles', 'Rope', 'Chain', 'Hook', 'Ornament', 'Moon', 'Midground',
        'Foreground', 'Railgun', 'Cylinder', 'Gun', 'Keep', 'Altar', 'Pillar', 'Stairs', 'Trophy', 'Weapon']


def pid_of(fn):
    stem = fn[:-5]
    try:
        return int(stem.rsplit('_', 1)[1])
    except Exception:
        return None


def load_dir(d):
    out = {}
    if not os.path.isdir(d):
        return out
    for fn in os.listdir(d):
        if not fn.endswith('.json'):
            continue
        p = pid_of(fn)
        if p is None:
            continue
        try:
            with open(os.path.join(d, fn), encoding='utf-8') as f:
                out[p] = json.load(f)
        except Exception:
            continue
    return out


def qmul(a, b):
    ax, ay, az, aw = a
    bx, by, bz, bw = b
    return (
        aw * bx + ax * bw + ay * bz - az * by,
        aw * by - ax * bz + ay * bw + az * bx,
        aw * bz + ax * by - ay * bx + az * bw,
        aw * bw - ax * bx - ay * by - az * bz,
    )


def qeuler(q):
    x, y, z, w = q
    sinr = 2.0 * (w * x + y * z)
    cosr = 1.0 - 2.0 * (x * x + y * y)
    rx = math.atan2(sinr, cosr)
    sinp = 2.0 * (w * y - z * x)
    if abs(sinp) >= 1.0:
        ry = math.copysign(math.pi / 2, sinp)
    else:
        ry = math.asin(sinp)
    siny = 2.0 * (w * z + x * y)
    cosy = 1.0 - 2.0 * (y * y + z * z)
    rz = math.atan2(siny, cosy)
    return (math.degrees(rx), math.degrees(ry), math.degrees(rz))


def main() -> int:
    for arena in ARENAS:
        root = os.path.join(SCENE_ROOT, arena)
        transforms = load_dir(os.path.join(root, 'Transform'))
        gameobjects = load_dir(os.path.join(root, 'GameObject'))
        meshfilters = load_dir(os.path.join(root, 'MeshFilter'))
        go_transform = {}
        go_has_mesh = set()
        for tpid, tdata in transforms.items():
            gopid = tdata.get('m_GameObject', {}).get('m_PathID')
            if gopid is not None:
                go_transform[gopid] = tpid
        for mf in meshfilters.values():
            gopid = mf.get('m_GameObject', {}).get('m_PathID')
            if gopid is not None:
                go_has_mesh.add(gopid)
        rows = []
        for gopid, gdata in gameobjects.items():
            name = gdata.get('m_Name', '')
            if not name or name in ('scene', 'root'):
                continue
            if gopid not in go_has_mesh:
                continue
            if any(s in name for s in SKIP):
                continue
            tpid = go_transform.get(gopid)
            if tpid is None:
                continue
            pos = [0.0, 0.0, 0.0]
            q = (0.0, 0.0, 0.0, 1.0)
            scale = [1.0, 1.0, 1.0]
            cur = tpid
            chain = 0
            while cur is not None and chain < 64:
                td = transforms.get(cur)
                if td is None:
                    break
                lp = td.get('m_LocalPosition', {})
                lr = td.get('m_LocalRotation', {})
                ls = td.get('m_LocalScale', {})
                lx, ly, lz = lp.get('x', 0), lp.get('y', 0), lp.get('z', 0)
                pos[0] += lx * scale[0]
                pos[1] += ly * scale[1]
                pos[2] += lz * scale[2]
                q = qmul(q, (lr.get('x', 0), lr.get('y', 0), lr.get('z', 0), lr.get('w', 1)))
                scale[0] *= ls.get('x', 1)
                scale[1] *= ls.get('y', 1)
                scale[2] *= ls.get('z', 1)
                cur = td.get('m_Father', {}).get('m_PathID')
                chain += 1
            # 近场过滤: x 相机基准 100 附近
            if not (78 <= pos[0] <= 130):
                continue
            eul = qeuler(q)
            rows.append((name, pos, eul, scale, chain))
        rows.sort(key=lambda r: r[1][0])
        print(f'=== {arena} ({len(rows)} 近场)')
        for name, pos, eul, scale, chain in rows:
            print(f'  {name}: pos=({pos[0]:.2f},{pos[1]:.2f},{pos[2]:.2f}) '
                  f'rot=({eul[0]:.0f},{eul[1]:.0f},{eul[2]:.0f}) scale=({scale[0]:.2f},{scale[1]:.2f},{scale[2]:.2f}) 链{chain}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
