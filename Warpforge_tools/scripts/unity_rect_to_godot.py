#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unity_rect_to_godot.py — 把 Unity 场景 JSON 树换算成 Godot 屏幕坐标矩形
Unity: y 向上, anchorMin/Max + anchoredPosition + sizeDelta + pivot (1920x1080 参考)
Godot: y 向下, 左上原点, 同分辨率下直接等价 (用户已查证 CanvasScaler 1920x1080 匹配宽度)

用法: py312 unity_rect_to_godot.py <解包目录> <根GO JSON文件|根GO名> [只列出含关键词的节点]
输出: 缩进树: GO名 → Godot position/size (屏幕坐标), 带 x/y 范围
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SRC = sys.argv[1]
ROOT = sys.argv[2]
FILTER = sys.argv[3] if len(sys.argv) > 3 else ''
H = 1080.0
W = 1920.0

_index = {}
_name_idx = {}
TYPES = ['GameObject', 'RectTransform', 'Transform', 'MonoBehaviour', 'Sprite']


def _build_index():
    global _index, _name_idx
    for t in TYPES:
        td = os.path.join(SRC, t)
        if not os.path.isdir(td):
            continue
        for f in os.listdir(td):
            if not f.endswith('.json'):
                continue
            m = f.rsplit('_', 1)
            pid = None
            if len(m) == 2 and m[1].replace('.json', '').lstrip('-').isdigit():
                pid = int(m[1].replace('.json', ''))
            try:
                d = json.load(open(os.path.join(td, f), encoding='utf-8'))
            except Exception:
                continue
            if pid is not None and pid not in _index:
                _index[pid] = {'type': t, 'path': os.path.join(td, f), 'data': d}
            nm = d.get('m_Name')
            if isinstance(nm, str) and nm:
                _name_idx.setdefault(nm, []).append(pid)


def load(pid):
    e = _index.get(pid)
    return e['data'] if e else None


def load_rt(pid):
    """GO → 它的 RectTransform JSON"""
    d = load(pid)
    if not d:
        return None, None
    for c in d.get('m_Component', []):
        ref = c.get('component', {})
        cid = ref.get('m_PathID')
        e = _index.get(cid)
        if e and e['type'] == 'RectTransform':
            return e['data'], cid
    return None, None


def get_rt_file(pid):
    e = _index.get(pid)
    return e['path'] if e else None


def walk(pid, depth, parent_rect, lines):
    """parent_rect = (xmin, ymin_unity, w, h) Unity 坐标系 (y 从底向上)"""
    d = load(pid)
    if not d:
        return
    name = d.get('m_Name', '?')
    rt, rtpid = load_rt(pid)
    pwx, pwy, pww, pwh = parent_rect
    pos = size = None
    if rt:
        amin = rt.get('m_AnchorMin') or {}
        amax = rt.get('m_AnchorMax') or {}
        a = rt.get('m_AnchoredPosition') or {}
        s = rt.get('m_SizeDelta') or {}
        p = rt.get('m_Pivot') or {}
        ax, ay = amin.get('x', 0), amin.get('y', 0)
        bx, by = amax.get('x', 1), amax.get('y', 1)
        apx, apy = a.get('x', 0), a.get('y', 0)
        sdx, sdy = s.get('x', 0), s.get('y', 0)
        px, py = p.get('x', 0.5), p.get('y', 0.5)
        xmin = pwx + ax * pww + (apx - sdx * px)
        xmax = pwx + bx * pww + (apx + sdx * (1 - px))
        ymin = pwy + ay * pwh + (apy - sdy * py)
        ymax = pwy + by * pwh + (apy + sdy * (1 - py))
        top = H - ymax
        bottom = H - ymin
        pos = (xmin, top)
        size = (xmax - xmin, bottom - top)
        rect_u = (xmin, ymin, xmax - xmin, ymax - ymin)
    else:
        rect_u = parent_rect
    if FILTER == '' or FILTER.lower() in name.lower():
        rt_src = get_rt_file(rtpid) if rtpid else ''
        lines.append('%s%s :: pos(%.1f,%.1f) size(%.1f,%.1f) x[%.1f,%.1f] y[%.1f,%.1f] %s' % (
            '  ' * depth, name,
            pos[0] if pos else -1, pos[1] if pos else -1,
            size[0] if size else -1, size[1] if size else -1,
            rect_u[0], rect_u[0] + rect_u[2],
            H - rect_u[1] - rect_u[3], H - rect_u[1],
            os.path.basename(rt_src)))
    # 子节点 (m_Children: rt_pid 列表 → GO pid)
    for rcid in _rt_children.get(rtpid, []):
        child_go = _rt_to_go.get(rcid)
        if child_go is not None:
            walk(child_go, depth + 1, rect_u, lines)


# 预构建: RT pid -> 子 RT pid 列表; RT pid -> GO pid
def _build_father():
    global _rt_children, _rt_to_go
    _rt_children = {}
    _rt_to_go = {}
    seen = set()
    for t in ['RectTransform', 'Transform']:
        td = os.path.join(SRC, t)
        if not os.path.isdir(td):
            continue
        for f in os.listdir(td):
            if not f.endswith('.json'):
                continue
            m = f.rsplit('_', 1)
            pid = None
            if len(m) == 2 and m[1].replace('.json', '').lstrip('-').isdigit():
                pid = int(m[1].replace('.json', ''))
            if pid is None or pid in seen:
                continue
            seen.add(pid)
            try:
                d = json.load(open(os.path.join(td, f), encoding='utf-8'))
            except Exception:
                continue
            go = d.get('m_GameObject') or {}
            gopid = go.get('m_PathID')
            if gopid is not None:
                _rt_to_go[pid] = gopid
            for ch in d.get('m_Children', []):
                cpid = ch.get('m_PathID')
                if cpid is not None:
                    _rt_children.setdefault(pid, []).append(cpid)


def main():
    _build_index()
    _build_father()
    # 根 GO
    root_pid = None
    if os.path.exists(ROOT):
        base = os.path.basename(ROOT)
        m = base.rsplit('_', 1)
        if len(m) == 2 and m[1].replace('.json', '').lstrip('-').isdigit():
            root_pid = int(m[1].replace('.json', ''))
    else:
        root_pid = _name_idx.get(ROOT, [None])[0]
    if root_pid is None:
        print('未找到根 GO: %s' % ROOT)
        sys.exit(1)
    lines = []
    walk(root_pid, 0, (0.0, 0.0, W, H), lines)
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
