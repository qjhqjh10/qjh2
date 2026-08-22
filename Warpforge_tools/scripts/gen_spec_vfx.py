#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_vfx.py — 战斗预制体 VFX 说明书 (08_预制体特效/战斗预制体)

输出: d:/2/解包整理/说明书/06_特效_预制体/战斗VFX预制体清单.md
  - VFX 根 GO 全集 (977 个): 名 + 组件统计 — _fx_from_event 接线对照表
"""
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

ROOT = 'd:/2/解包整理/08_预制体特效/战斗预制体'
OUT = 'd:/2/解包整理/说明书/06_特效_预制体/战斗VFX预制体清单.md'
PID_RE = re.compile(r'^(.+?)_(-?\d+)\.json$')

NL = chr(10)


def load_dir(t):
    d = {}
    p = os.path.join(ROOT, t)
    if not os.path.isdir(p):
        return d
    for f in os.listdir(p):
        m = PID_RE.match(f)
        if not m:
            continue
        try:
            d[int(m.group(2))] = json.load(open(os.path.join(p, f), encoding='utf-8'))
        except Exception:
            pass
    return d


def main():
    GO = load_dir('GameObject')
    TF = load_dir('Transform')
    names = {pid: (d.get('m_Name'), d.get('m_Component', [])) for pid, d in GO.items()}
    # PathID -> 组件类型 (跨目录扫描)
    pid_type = {}
    for sub in sorted(os.listdir(ROOT)):
        pp = os.path.join(ROOT, sub)
        if not os.path.isdir(pp) or sub in ('GameObject', 'Transform'):
            continue
        for f in os.listdir(pp):
            m = PID_RE.match(f)
            if m:
                pid_type[int(m.group(2))] = sub
    # TF: tpid -> (gopid, father_tpid)
    parent = {}
    for tpid, d in TF.items():
        parent[tpid] = (d.get('m_GameObject', {}).get('m_PathID'),
                        d.get('m_Father', {}).get('m_PathID'))
    roots = [(tpid, g) for tpid, (g, fa) in parent.items() if fa not in parent]
    print('VFX roots:', len(roots))

    comp_names = {'ParticleSystem': 'PS', 'ParticleSystemRenderer': 'PSR',
                  'AudioSource': 'AU', 'MeshFilter': 'MF', 'MeshRenderer': 'MR',
                  'SpriteRenderer': 'SR', 'Camera': 'CAM', 'Light': 'LIG',
                  'SkinnedMeshRenderer': 'SMR', 'TrailRenderer': 'TR', 'VisualEffect': 'VFX'}
    comp_counter = Counter()
    rows = []
    for tpid, gopid in sorted(roots, key=lambda x: (names.get(x[1], ('', None))[0] or '').lower()):
        nm, comps = names.get(gopid, ('?', []))
        tags = []
        for c in comps:
            if isinstance(c, dict):
                pid = (c.get('component') or {}).get('m_PathID')
                t = pid_type.get(pid)
                if t in comp_names:
                    tags.append(comp_names[t])
        comp_counter.update(tags)
        rows.append((nm, ','.join(tags) if tags else '-'))

    comps_txt = ' '.join('%s=%d' % (k, v) for k, v in comp_counter.most_common())
    lines = ['# 战斗 VFX 预制体清单 (08_预制体特效/战斗预制体)', '',
             '> 来源: 战斗预制体/GameObject+Transform (根 GO = 无父 Transform)',
             '> 生成: gen_spec_vfx.py | **%d 个 VFX 根**, 组件: %s' % (len(rows), comps_txt),
             '> 用途: battle.gd _fx_from_event VFX 触发名对照; 转换脚本 convert_card_vfx_bundle.py', '',
             '## 前缀/主题分类 (速查)', '',
             '- **BulletImpact_*** — 枪弹命中 (按武器/阵营)',
             '- **Buff_/Debuff_/WhileInPlay_*** — 增益/减益/持续效果',
             '- **Atk_*** — 攻击特效; **Blast_/Explosion*** — 爆炸',
             '- **CreateCard / Summon*** — 召唤/发牌',
             '- **Environment Condition*** — 阵营环境特效',
             '- **Screen_*** — 屏幕级 (红/绿/顶)',
             '- **Psychic_/Shadow_/Sword_*** — 灵能/暗影/剑击',
             '- **Tap** — 点击反馈; **Ranged/Orbit** — 远程', '',
             '## 完整清单 (%d 个, 按名排序)' % len(rows), '',
             '| VFX 名 | 组件 |',
             '|---|---|']
    for nm, tags in rows:
        lines.append('| %s | %s |' % (nm, tags))
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(NL.join(lines))
    print('OK', OUT, len(lines), 'lines')


if __name__ == '__main__':
    main()
