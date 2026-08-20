#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chain_rect.py — 从原始 Unity JSON 沿 m_Father 链式换算任意 GO 的绝对屏幕坐标
用法: py312 chain_rect.py <场景目录> <GO PathID 或 GO 名>
输出: GO名 [父链] -> Godot 屏幕坐标 x[y1,y2]
"""
import json, os, sys, glob

sys.stdout.reconfigure(encoding='utf-8')
SRC = sys.argv[1]
TARGET = sys.argv[2]
W, H = 1920.0, 1080.0

go_index = {}   # GO PathID -> GO data
rt_index = {}   # RT PathID -> RT data
go_name = {}    # GO PathID -> name
name_idx = {}   # name -> [GO PathID]

for t in ['GameObject', 'RectTransform']:
    td = os.path.join(SRC, t)
    if not os.path.isdir(td):
        continue
    for f in glob.glob(os.path.join(td, '*.json')):
        base = os.path.basename(f).rsplit('.json', 1)[0]
        m = base.rsplit('_', 1)
        pid = None
        if len(m) == 2 and m[1].lstrip('-').isdigit():
            pid = int(m[1])
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if pid is None:
            continue
        if t == 'GameObject':
            if pid not in go_index:
                go_index[pid] = d
                go_name[pid] = d.get('m_Name', '?')
                nm = d.get('m_Name')
                if isinstance(nm, str) and nm:
                    name_idx.setdefault(nm, []).append(pid)
        else:
            if pid not in rt_index:
                rt_index[pid] = d


def find_goid(target):
    if target.lstrip('-').isdigit():
        return int(target)
    cands = name_idx.get(target, [])
    if not cands:
        for nm, pids in name_idx.items():
            if target.lower() in nm.lower():
                cands += pids
    return cands[0] if cands else None


def go_rt(goid):
    """GO -> 它的 RT PathID"""
    d = go_index.get(goid)
    if not d:
        return None
    for c in d.get('m_Component', []):
        pid = c.get('component', {}).get('m_PathID')
        if pid in rt_index:
            return pid
    return None


def rt_rect(rtid):
    """RT -> (Godot x1,y1,x2,y2) 绝对坐标; 断链返回 None"""
    rt = rt_index.get(rtid)
    if rt is None:
        return None
    fid = rt.get('m_Father', {}).get('m_PathID')
    if fid is not None and fid in rt_index:
        parent = rt_rect(fid)
        if parent is None:
            return None
    else:
        # 根元素 (父不是 RT): 父参照 = 全屏 1920x1080 (Canvas), 但自身 anchoredPosition/sizeDelta 仍有效
        # (如 Gacha Tab: anchor(0,0,1,1) anchoredPos(82,0) sizeDelta(-163.6,0) → x[163.8,1920])
        # 特判: 场景根 Canvas (anchor 收缩 0,0 + sizeDelta 0 + anchoredPos 0) 恒为全屏
        amn0 = rt.get('m_AnchorMin') or {}
        amx0 = rt.get('m_AnchorMax') or {}
        ap0 = rt.get('m_AnchoredPosition') or {}
        sd0 = rt.get('m_SizeDelta') or {}
        if (amn0.get('x', 0) == 0 and amn0.get('y', 0) == 0
                and amx0.get('x', 0) == 0 and amx0.get('y', 0) == 0
                and ap0.get('x', 0) == 0 and ap0.get('y', 0) == 0
                and sd0.get('x', 0) == 0 and sd0.get('y', 0) == 0):
            return (0.0, 0.0, W, H)
        parent = (0.0, 0.0, W, H)
    px1, py1, px2, py2 = parent
    pw, ph = px2 - px1, py2 - py1
    amn = rt.get('m_AnchorMin') or {}
    amx = rt.get('m_AnchorMax') or {}
    ap = rt.get('m_AnchoredPosition') or {}
    sd = rt.get('m_SizeDelta') or {}
    pv = rt.get('m_Pivot') or {}
    ax0, ay0 = amn.get('x', 0), amn.get('y', 0)
    ax1, ay1 = amx.get('x', ax0), amx.get('y', ay0)
    apx, apy = ap.get('x', 0), ap.get('y', 0)
    sdx, sdy = sd.get('x', 0), sd.get('y', 0)
    pvx, pvy = pv.get('x', 0.5), pv.get('y', 0.5)
    # 2026-08-20 修复拉伸锚点 bug (anchorMin≠anchorMax 且 pivot≠0.5 时旧算法差 ~67px):
    # Unity 语义: offsetMin = anchoredPosition - pivot*sizeDelta (相对锚点 min 点),
    #            offsetMax = anchoredPosition + (1-pivot)*sizeDelta (相对锚点 max 点)
    # 收缩锚点 (min==max) 时与旧"锚点中心+pivot 展开"数学等价; 拉伸时以 offsetMin/Max 为准
    # 锚点 min/max 点 (Godot y 向下): Unity y 向上 -> Godot gy = py1 + (1-ay)*ph
    amin_x = px1 + ax0 * pw
    amax_x = px1 + ax1 * pw
    amin_gy = py1 + (1.0 - ay0) * ph
    amax_gy = py1 + (1.0 - ay1) * ph
    # offsetMin/offsetMax: Unity y 向上为正 -> Godot 顶/底边 = 锚点 y - 偏移
    gx1 = amin_x + (apx - pvx * sdx)
    gx2 = amax_x + (apx + (1.0 - pvx) * sdx)
    gy1 = amax_gy - (apy + (1.0 - pvy) * sdy)
    gy2 = amin_gy - (apy - pvy * sdy)
    return (gx1, gy1, gx2, gy2)


def main():
    goid = find_goid(TARGET)
    if goid is None:
        print('未找到 GO:', TARGET)
        return
    name = go_name.get(goid, '?')
    rtid = go_rt(goid)
    if rtid is None:
        print('%s (GO %s) 无 RectTransform' % (name, goid))
        return
    rect = rt_rect(rtid)
    chain, n = [], rtid
    for _ in range(40):
        rt = rt_index.get(n)
        if rt is None:
            break
        f = rt.get('m_Father', {}).get('m_PathID')
        if f is None or f not in rt_index:
            break
        fgo = rt_index[f].get('m_GameObject', {}).get('m_PathID')
        chain.append('%s(%s)' % (go_name.get(fgo, '?'), f))
        n = f
    if rect:
        print('%s (GO %s)\n  父链: %s\n  Godot: x[%.1f, %.1f] y[%.1f, %.1f] (宽 %.1f 高 %.1f)' % (
            name, goid, ' <- '.join(chain[::-1]) if chain else '(根)',
            rect[0], rect[2], rect[1], rect[3], rect[2] - rect[0], rect[3] - rect[1]))
    else:
        print('%s (GO %s) 换算失败' % (name, goid))


if __name__ == '__main__':
    main()
