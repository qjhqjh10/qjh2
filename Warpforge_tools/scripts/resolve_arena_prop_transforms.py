#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resolve_arena_prop_transforms.py — 解析阵营战场每个模型的原始世界变换 (说明书 Transform 链)
GameObject name -> Transform -> m_Father 链累积 world position/rotation/scale
输出: 模型名 -> (世界位置, 世界旋转euler度, 世界缩放)
"""
import json
import math
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SCENE_ROOT = 'd:/2/解包整理/07_场景/'
ARENAS = ['battlearena2', 'battlearena3', 'battlearenaaeldari', 'battlearenaastramilitarum',
          'battlearenadarkangels', 'battlearenaemperorschildren', 'battlearenagenestealers',
          'battlearenaleviathan', 'battlearenasororitas', 'battlearenaspacewolves',
          'battlearenatauviorla']


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
    """四元数相乘 (a * b)"""
    ax, ay, az, aw = a
    bx, by, bz, bw = b
    return (
        aw * bx + ax * bw + ay * bz - az * by,
        aw * by - ax * bz + ay * bw + az * bx,
        aw * bz + ax * by - ay * bx + az * bw,
        aw * bw - ax * bx - ay * by - az * bz,
    )


def qeuler(q):
    """四元数 -> (x, y, z) 欧拉角 (ZXY 顺序, Unity/Godot 视觉一致)"""
    x, y, z, w = q
    # roll (x), pitch (y), yaw (z) 按 Unity 约定
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
    # 需要查朝向的模型 (每阵营已选)
    WANT = {
        'battlearena2': ['Banner1', 'Skull_Left1', 'Skull_Right1', 'Tower_Silk_11', 'Rubble1'],
        'battlearena3': ['Monolith Front Left1', 'Monolith Front Right1', 'Broken Monolith 11',
                         'Ground Lights1', 'Props 1.0011'],
        'battlearenaaeldari': ['Banner 1', 'Banner 2', 'Tower 1', 'Bridge 1', 'Platform 1'],
        'battlearenaastramilitarum': ['Banner 1', 'Banner 4', 'Statue 1', 'Barricade 1', 'Bunker Antenna 1'],
        'battlearenadarkangels': ['Turret 1 Banner', 'Skull vent 1', 'Generator', 'Container 1'],
        'battlearenaemperorschildren': ['Curtain 1', 'Cauldron 1', 'Cauldron 2', 'Glass Tube 1', 'Spike 1'],
        'battlearenagenestealers': ['Banner 3', 'Genestaler Fan', 'Machinery Center', 'Hanging Hook'],
        'battlearenaleviathan': ['Thorn_5', 'Capillary_1', 'Prop_front_1', 'Floor Tentacle'],
        'battlearenasororitas': ['Banner 1', 'Statue L', 'Statue R', 'Cauldron L', 'Candle 2'],
        'battlearenaspacewolves': ['Banner 1', 'Wolf Left', 'Wolf Right', 'Cauldron 1', 'Rock 1'],
        'battlearenatauviorla': ['Plasma Generator', 'Drone 1', 'Railgun Tower', 'Bunker console'],
    }
    for arena in ARENAS:
        root = os.path.join(SCENE_ROOT, arena)
        transforms = load_dir(os.path.join(root, 'Transform'))
        gameobjects = load_dir(os.path.join(root, 'GameObject'))
        # go pid -> transform pid
        go_transform = {}
        for tpid, tdata in transforms.items():
            gopid = tdata.get('m_GameObject', {}).get('m_PathID')
            if gopid is not None:
                go_transform[gopid] = tpid
        # go name -> transform data (累积世界变换)
        found = {}
        for gopid, gdata in gameobjects.items():
            name = gdata.get('m_Name', '')
            for w in WANT.get(arena, []):
                if name.startswith(w) or w in name:
                    tpid = go_transform.get(gopid)
                    if tpid is None:
                        continue
                    # 世界变换: 沿父链累积
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
                        # 累积: 父级先转, 本地后
                        # pos = parent_pos + parent_q * (local_pos * parent_scale)
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
                    eul = qeuler(q)
                    found.setdefault(w, []).append((name, pos, eul, scale, chain))
        print(f'=== {arena}')
        for w in WANT.get(arena, []):
            for name, pos, eul, scale, chain in found.get(w, [])[:3]:
                print(f'  [{w}] {name}: pos=({pos[0]:.2f},{pos[1]:.2f},{pos[2]:.2f}) '
                      f'rot=({eul[0]:.0f},{eul[1]:.0f},{eul[2]:.0f}) scale=({scale[0]:.2f},{scale[1]:.2f},{scale[2]:.2f}) 链{chain}')
            if w not in found:
                print(f'  [{w}] 未找到')
    return 0


if __name__ == '__main__':
    sys.exit(main())
