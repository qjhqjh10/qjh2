#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vfx_ref_audit.py — 战斗 VFX 覆盖率审计 (说明书 977 根 ↔ 已转换/已接入)

输出缺口报告: 说明书 VFX 清单中"未转换/未接入"的根 — 这是"原版引用图里该有但我们没有"的机器清单
(答"11.9 万文件全用"问题: 用 JSON 文件数不对, 用 977 根 + 本审计才对)

用法: py312 vfx_ref_audit.py [--out 报告.md]
数据源:
  - 说明书/06_特效_预制体/战斗VFX预制体清单.md  (977 VFX 根)
  - d:/warpforge/data/particles/ + particles3d/   (已转换粒子 json)
  - d:/warpforge/assets/particles/                (已提取贴图/资源)
  - d:/warpforge/scripts/battle.gd                (事件接入)
"""
import json
import os
import re
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

LIST = 'd:/2/解包整理/说明书/06_特效_预制体/战斗VFX预制体清单.md'
PROJ = 'd:/warpforge'


def load_vfx_list():
    names = []
    for l in open(LIST, encoding='utf-8'):
        m = re.match(r'^\| ([^|]+?) \| .*\|$', l.strip())
        if m and m.group(1) not in ('VFX 名',):
            nm = m.group(1).strip()
            if nm and '---' not in nm:
                names.append(nm)
    return names


def load_converted():
    done = set()
    for sub in ('data/particles', 'data/particles3d'):
        d = os.path.join(PROJ, sub)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'):
                    done.add(fn[:-5])
    ad = os.path.join(PROJ, 'assets/particles')
    if os.path.isdir(ad):
        for fn in os.listdir(ad):
            done.add(fn.rsplit('.', 1)[0])
    return done


def load_battle_refs():
    """battle.gd 中引用的特效名 (字符串字面量 + dict key)"""
    refs = set()
    p = os.path.join(PROJ, 'scripts/battle.gd')
    if not os.path.exists(p):
        return refs
    txt = open(p, encoding='utf-8', errors='ignore').read()
    for m in re.finditer(r'"([A-Za-z][A-Za-z0-9 _./-]{3,80})"', txt):
        refs.add(m.group(1))
    return refs


def main():
    out_path = None
    if '--out' in sys.argv:
        out_path = sys.argv[sys.argv.index('--out') + 1]
    vfx = load_vfx_list()
    done = load_converted()
    refs = load_battle_refs()
    # 归一化比较: 引用的可能是文件名/触发名, 做"包含集合"匹配
    def hit(name):
        k = name.lower().replace(' ', '')
        for d in done:
            if k in d.lower().replace(' ', '') or d.lower().replace(' ', '') in k:
                return True
        return False
    converted = [n for n in vfx if hit(n)]
    missing = [n for n in vfx if not hit(n)]
    # 高频关键词 (疑似战斗主路径, 优先接)
    KEY = ('hit', 'impact', 'death', 'explod', 'blast', 'bullet', 'attack', 'summon',
           'buff', 'debuff', 'heal', 'shield', 'stun', 'energy', 'psychic')
    prio = sorted([n for n in missing if any(k in n.lower() for k in KEY)])
    lines = ['# VFX 覆盖率审计 (%s)' % datetime.now().strftime('%Y-%m-%d %H:%M'), '',
             '- 说明书 VFX 根: **%d**' % len(vfx),
             '- 已转换(particles/particles3d/assets 命中): **%d**' % len(converted),
             '- 未命中: **%d** (含事件引用/近似名未对齐的, 需人工判读)' % len(missing), '',
             '## 优先级未接入 (关键词: hit/impact/death/explosion/attack/summon/buff/heal...)', '',
             '(%d 个)' % len(prio), '']
    for n in prio:
        lines.append('- `%s`' % n)
    lines += ['', '## 全部未命中 (%d)' % len(missing), '']
    for n in missing:
        lines.append('- `%s`' % n)
    out = '\n'.join(lines)
    if out_path:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(out)
        print('✓ 输出: %s (%d VFX, 已转 %d, 未命中 %d, 优先 %d)' % (out_path, len(vfx), len(converted), len(missing), len(prio)))
    else:
        print(out[:3500])


if __name__ == '__main__':
    main()
