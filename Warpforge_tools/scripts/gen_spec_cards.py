#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_cards.py — 卡牌说明书批量生成器 (01_卡牌 + card_index)

按 card_index factions (13 子阵营) 生成说明书:
  - 资源目录归属 (01_卡牌/<阵营目录>)
  - Sprite 明细 (m_Rect 尺寸/m_Pivot) — 卡框/宝石/立绘等
  - Texture2D 清单 / 语音 / 动画
  - 卡牌统计 (unit/tactic/hero, 无立绘数)
  - 卡框 frames 路径 (troop/stratagem tier1-4)

输出: d:/2/解包整理/说明书/03_卡牌/<faction>.md + README.md
"""
import collections
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(100000)

U = 'd:/2/解包整理/01_卡牌'
OUT = 'd:/2/解包整理/说明书/03_卡牌'
CARD_INDEX = 'd:/2/解包整理/card_index.json'

# card_index faction -> 01_卡牌 目录名
DIR_MAP = {
    'SaimHann': 'Aeldari_灵族', 'AstraMilitarum': 'AstraMilitarum_星界军',
    'BlackLegion': 'BlackLegion_黑色军团', 'DarkAngels': 'DarkAngels_暗黑天使',
    'EmperorsChildren': 'EmperorsChildren_帝皇之子', 'Genestealers': 'GenestealerCults_基因窃取者教派',
    'Sautekh': 'Necrons_死灵族', 'Goff': 'Orks_兽人', 'Sororitas': 'Sororitas_战斗修女',
    'SpaceWolves': 'SpaceWolves_太空野狼', 'TauEmpire': 'Tau_钛帝国',
    'Leviathan': 'Tyranids_泰伦虫族', 'Ultramarines': 'Ultramarines_极限战士',
}


def load_json(path):
    try:
        return json.load(open(path, encoding='utf-8'))
    except Exception:
        return None


def gen_faction(faction, root_dir, ci):
    root = os.path.join(U, root_dir)
    lines = []
    w = lines.append
    w('# %s 卡牌资源说明书\n' % faction)
    w('> 来源: 解包整理/01_卡牌/%s/ (Sprite/Texture2D JSON+PNG; card_index.json)' % root_dir)
    w('> 生成: gen_spec_cards.py\n')

    w('## 资源目录统计\n')
    w('| 子目录 | 文件数 | 说明 |\n|---|---|---|')
    for sub in sorted(os.listdir(root)):
        p = os.path.join(root, sub)
        if os.path.isdir(p):
            n = sum(1 for f in os.listdir(p))
            w('| %s | %d | %s |' % (sub, n, {
                'AudioClip': '语音/督军语音 (ogg)',
                'Sprite': '精灵元数据 (卡框 SDF/图标/立绘角标等, JSON)',
                'Texture2D': '贴图 PNG (立绘/卡框/宝石)',
                '动画': '卡牌动画 (AnimationClip)',
                'AssetBundle': 'bundle 清单'}.get(sub, '')))
    w('')

    sp_dir = os.path.join(root, 'Sprite')
    if os.path.isdir(sp_dir):
        w('## Sprite 明细 (m_Rect/m_Pivot — 复用资源尺寸权威)\n')
        w('| 精灵名 | 宽×高 | pivot | 图集 |\n|---|---|---|---|')
        seen = set()
        for fn in sorted(os.listdir(sp_dir)):
            if not fn.endswith('.json'):
                continue
            d = load_json(os.path.join(sp_dir, fn))
            if not d:
                continue
            nm = d.get('m_Name')
            if not nm or nm in seen:
                continue
            seen.add(nm)
            r = d.get('m_Rect', {}) or {}
            pv = d.get('m_Pivot', {}) or {}
            w('| %s | %s×%s | (%s,%s) | %s |' % (
                nm, r.get('width', ''), r.get('height', ''),
                pv.get('x', ''), pv.get('y', ''), ','.join(d.get('m_AtlasTags', []) or [])))
        w('')

    tx_dir = os.path.join(root, 'Texture2D')
    if os.path.isdir(tx_dir):
        w('## Texture2D 清单 (PNG)\n')
        w('| 贴图 |\n|---|')
        for f in sorted(os.listdir(tx_dir)):
            if f.endswith('.png'):
                w('| %s |' % f)
        w('')

    au_dir = os.path.join(root, 'AudioClip')
    if os.path.isdir(au_dir):
        w('## 语音 (%d)\n' % len([f for f in os.listdir(au_dir)]))
        for f in sorted(os.listdir(au_dir)):
            w('- %s' % f)
        w('')

    an_dir = os.path.join(root, '动画')
    if os.path.isdir(an_dir):
        anims = sorted(os.listdir(an_dir))
        w('## 卡牌动画 (%d 文件)\n' % len(anims))
        for f in anims:
            w('- %s' % f)
        w('')

    # 卡牌统计
    cards = [c for c in ci['cards'] if c.get('faction') == faction]
    kinds = collections.Counter(c.get('type', '?') for c in cards)
    w('## 卡牌统计 (card_index.json, faction=%s)\n' % faction)
    for k in ('unit', 'tactic', 'hero'):
        w('- %s: %d' % (k, kinds.get(k, 0)))
    no_art = [c for c in cards if not c.get('art')]
    if no_art:
        w('- 无立绘 (PnP 兜底): %d' % len(no_art))
    w('')

    # 卡框
    frames = (ci.get('frames') or {}).get(faction) or {}
    if frames:
        w('## 卡框 frames (tier1-4 路径)\n')
        for role in ('troop', 'stratagem'):
            if role in frames:
                w('### %s' % role)
                for t in sorted(frames[role]):
                    w('- tier%s: `%s`' % (t, frames[role][t]))
        w('')
    return '\n'.join(lines)


def gen_readme(ci):
    lines = ['# 卡牌说明书 (01_卡牌 + card_index.json)\n',
             '> 13 子阵营 × (立绘/卡框/语音/动画), card_index.json 1193 卡 (unit 656 / tactic 484 / hero 53)\n',
             '> 数值 OCR: card_index.json stats/view 口径见各阵营说明书; 卡组模板 236 套见 09_游戏数据\n',
             '', '## 阵营索引\n', '| 阵营 | 卡数 | 资源目录 | 说明书 |', '|---|---|---|---|']
    by_faction = collections.Counter(c.get('faction') for c in ci['cards'])
    for f in ci['factions']:
        nm = f['name']
        lines.append('| %s (id %d) | %d | %s | [%s.md](%s.md) |' % (
            nm, f['id'], by_faction.get(nm, 0), DIR_MAP.get(nm, '?'), nm, nm))
    lines.append('')
    lines.append('## 配套')
    lines.append('- `解包整理/card_index.json` — 全量索引: cards(1193) / factions(13) / frames(卡框) / decks(2210 模板) / stats')
    lines.append('- `解包整理/01_卡牌/卡组数据/` — 卡牌&卡组 MonoBehaviour (2210)')
    lines.append('- `解包整理/01_卡牌/卡牌动画/` — 卡牌动画 AnimationClip')
    return '\n'.join(lines)


def main():
    os.makedirs(OUT, exist_ok=True)
    ci = load_json(CARD_INDEX)
    if not ci:
        print('!! card_index 读取失败')
        return 1
    for f in ci['factions']:
        nm = f['name']
        root_dir = DIR_MAP.get(nm)
        if not root_dir or not os.path.isdir(os.path.join(U, root_dir)):
            print('!! 跳过 %s (目录 %s 缺失)' % (nm, root_dir))
            continue
        txt = gen_faction(nm, root_dir, ci)
        with open(os.path.join(OUT, nm + '.md'), 'w', encoding='utf-8') as fh:
            fh.write(txt)
        print('✓ %s (%d 行)' % (nm, txt.count(chr(10))))
    with open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8') as fh:
        fh.write(gen_readme(ci))
    print('✓ README')
    return 0


if __name__ == '__main__':
    sys.exit(main())
