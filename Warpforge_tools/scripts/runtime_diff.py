#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原版↔项目 运行时 dump TSV 对照器 (2026-08-25)
用法: py312/python.exe runtime_diff.py <原版.tsv> <项目.tsv> [--out 报告.md]
按 path 对齐 → 输出 缺失/多余/坐标差/字号差/文字差/可见性差
"""
import sys, argparse
from pathlib import Path


def load(tsv):
    lines = Path(tsv).read_text(encoding='utf-8-sig').splitlines()
    if not lines:
        return {}
    return [l.split('\t') for l in lines if l.strip()]


def norm_path(p):
    # 归一: 去根重复/前缀 (BattlePrefab/BattlePrefab/ 与 Battle/), 统一分隔
    p = p.replace('\\', '/')
    segs = [s for s in p.split('/') if s and s != 'BattlePrefab' or s == 'BattlePrefab']
    out = []
    for s in segs:
        if not out or out[-1] != s:
            out.append(s)
    # 去双桥 (root/root)
    while len(out) > 1 and out[0] == out[1]:
        out.pop(0)
    return '/'.join(out)


def parse_rows(rows):
    hdr = rows[0]
    idx = {n: i for i, n in enumerate(hdr)}
    data = {}
    for r in rows[1:]:
        if len(r) < 2:
            continue
        p = norm_path(r[0])
        data[p] = r
    return data, idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('orig')
    ap.add_argument('proj')
    ap.add_argument('--out', default='d:/2/Unity参照管线_0825/data/runtime_diff_report.md')
    args = ap.parse_args()

    orows = load(args.orig)
    prows = load(args.proj)
    od, oi = parse_rows(orows)
    pd, pi = parse_rows(prows)

    def get(r, idx, name, default=''):
        i = idx.get(name)
        return r[i] if i is not None and i < len(r) else default

    rep = ['# 运行时对照报告\n', '| 项目 | 数量 |', '|---|---|',
           '| 原版条目 | %d |' % len(od), '| 项目条目 | %d |' % len(pd),
           '| 仅原版 | %d |' % len(set(od) - set(pd)), '| 仅项目 | %d |' % len(set(pd) - set(od)),
           '']
    MISS = 40   # 报告上限
    missing = sorted(set(od) - set(pd))[:MISS]
    if missing:
        rep.append('## 仅原版 (%d, 前 %d 条)' % (len(set(od) - set(pd)), len(missing)))
        rep.append('| path | 类型 |')
        rep.append('|---|---|')
        for p in missing:
            r = od[p]
            rep.append('| %s | %s |' % (p, get(r, oi, 'name', '')))
        rep.append('')
    extra = sorted(set(pd) - set(od))[:MISS]
    if extra:
        rep.append('## 仅项目 (%d, 前 %d 条)' % (len(set(pd) - set(od)), len(extra)))
        rep.append('| path | 类型 |')
        rep.append('|---|---|')
        for p in extra:
            r = pd[p]
            rep.append('| %s | %s |' % (p, get(r, pi, 'name', '')))
        rep.append('')
    # 共项数值差 (坐标/字号 相近路径)
    rep.append('## 共项数值差 (path 相同, 坐标/字号差>2 或文字不同; 前 60 条)\n| path | 字段 | 原版 | 项目 |')
    rep.append('|---|---|---|---|')
    diffs = 0
    for p in sorted(set(od) & set(pd)):
        a, b = od[p], pd[p]
        for field in ('pos', 'size', 'fontSize', 'text'):
            va, vb = get(a, oi, field), get(b, pi, field)
            if va == '' and vb == '':
                continue
            if field in ('pos', 'size') and va and vb:
                try:
                    ax, ay = [float(x) for x in va.split(',')]
                    bx, by = [float(x) for x in vb.split(',')]
                except Exception:
                    continue
                if abs(ax - bx) < 2 and abs(ay - by) < 2:
                    continue
            elif va == vb:
                continue
            if field == 'text' and vb == '':
                continue
            diffs += 1
            if diffs <= 60:
                rep.append('| %s | %s | %s | %s |' % (p, field, va, vb))
    rep.append('\n共 %d 处数值差异' % diffs)
    Path(args.out).write_text('\n'.join(rep), encoding='utf-8')
    print('报告:', args.out, '| 仅原版 %d / 仅项目 %d / 数值差 %d' % (
        len(set(od) - set(pd)), len(set(pd) - set(od)), diffs))


if __name__ == '__main__':
    main()
