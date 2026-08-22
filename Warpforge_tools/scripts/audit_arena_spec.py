#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_arena_spec.py — 生成场景 vs 原始 Unity JSON 逐项审计 (只读)

用法: py312/python.exe audit_arena_spec.py battlearena1 battlearenatauviorla ...
说明: 解析 d:/2/战场演示/scenes/unity_arena_<arena>.gd 的每节点
(position/quaternion/scale/相机 fov-near-far) 与 07_场景/<arena>/Transform 原始 JSON 比对.
已知预期差异 (文档化手性转换, 非错误):
  - BoardCamera: 位置=镜像世界坐标 200-wp.x, 旋转 conjX(q_u)⊗Y180 (相机移出 MirrorX 根)
  - Directional Light: quaternion⊗RotX(-90) (Unity 灯照向 R·(0,-1,0) / Godot B·(0,0,-1))
"""
import json, os, re, sys

SCENE = 'd:/2/解包整理/07_场景'
DEMO = 'd:/2/战场演示/scenes'
PID = re.compile(r'^.+?_(\d+)\.json$')


def load(d):
    out = {}
    for fn in os.listdir(d):
        m = PID.match(fn)
        if not m:
            continue
        try:
            out[int(m.group(1))] = json.load(open(os.path.join(d, fn), encoding='utf-8'))
        except Exception:
            pass
    return out


def parse_gd(path):
    nodes = []
    cur = None
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        m = re.match(r'n_\d+\.name = (.+)$', line)
        if m and "'" in m.group(1):
            cur = {'name': m.group(1).strip("'")}
            nodes.append(cur)
            continue
        if cur is None:
            continue
        m = re.match(r'n_\d+\.position = Vector3\((.*)\)$', line)
        if m:
            try:
                cur['pos'] = tuple(float(x) for x in m.group(1).split(','))
            except Exception:
                pass
            continue
        m = re.match(r'n_\d+\.quaternion = Quaternion\((.*)\)$', line)
        if m:
            try:
                cur['quat'] = tuple(float(x) for x in m.group(1).split(','))
            except Exception:
                pass
            continue
        m = re.match(r'n_\d+\.scale = Vector3\((.*)\)$', line)
        if m:
            try:
                cur['scale'] = tuple(float(x) for x in m.group(1).split(','))
            except Exception:
                pass
        m = re.match(r'n_\d+\.(fov|near|far) = ([-\d.e]+)$', line)
        if m:
            cur[m.group(1)] = float(m.group(2))
    return nodes


def audit(arena):
    d = os.path.join(SCENE, arena)
    TF = load(os.path.join(d, 'Transform'))
    GO = load(os.path.join(d, 'GameObject'))
    tf_by_name = {}
    for t, td in TF.items():
        g = GO.get(td.get('m_GameObject', {}).get('m_PathID'), {})
        nm = g.get('m_Name', 'GO%d' % t)
        lp = td.get('m_LocalPosition', {})
        lq = td.get('m_LocalRotation', {})
        ls = td.get('m_LocalScale', {})
        tf_by_name.setdefault(nm, []).append(
            ((lp.get('x', 0), lp.get('y', 0), lp.get('z', 0)),
             (lq.get('x', 0), lq.get('y', 0), lq.get('z', 0), lq.get('w', 1)),
             (ls.get('x', 1), ls.get('y', 1), ls.get('z', 1))))
    rad = os.path.join(DEMO, 'unity_arena_%s.gd' % arena)
    nodes = parse_gd(rad)
    bad, checked = [], 0
    unused = {k: [list(v2) for v2 in v] for k, v in tf_by_name.items()}
    for n in nodes:
        nm = n.get('name', '?')
        if 'pos' not in n:
            continue
        checked += 1
        cands = unused.get(nm)
        if not cands:
            bad.append((nm, 'NO_TF_NAME'))
            continue
        best, bestd = None, 1e9
        for c in cands:
            p, qq, s = c
            dd = sum(abs(a - b) for a, b in zip(p, n['pos'])) + \
                sum(abs(a - b) for a, b in zip(qq, n.get('quat', (0, 0, 0, 1)))) + \
                sum(abs(a - b) for a, b in zip(s, n.get('scale', (1, 1, 1))))
            if dd < bestd:
                bestd, best = dd, c
        if bestd > 1e-3:
            bad.append((nm, 'VAL_DIFF %.4f' % bestd))
        else:
            unused[nm].remove(best)
    print('%-34s 节点 %d | 不符 %d | %s' % (arena, checked, len(bad),
          str(bad[:4]) if bad else '全部符合说明书局部变换'))
    txt = open(rad, encoding='utf-8').read()
    for mm in re.finditer(r"n_\d+\.name = 'BoardCamera'", txt):
        seg = txt[mm.start():mm.start() + 900]
        fov = re.search(r'\.fov = ([\d.]+)', seg)
        far = re.search(r'\.far = ([\d.]+)', seg)
        print('    BoardCamera fov=%s (JSON 46.397) far=%s' % (fov.group(1) if fov else '?', far.group(1) if far else '?'))
    for mm in re.finditer(r'\t\S+\.light_color = Color\(([^)]*)\)', txt):
        print('    light_color = %s' % mm.group(1))
    for mm in re.finditer(r'ambient_light_color = Color\(([^)]*)\)', txt):
        print('    ambient = %s' % mm.group(1))
    for mm in re.finditer(r'background_color = Color\(([^)]*)\)', txt):
        print('    background = %s' % mm.group(1))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for a in sys.argv[1:]:
        audit(a)
