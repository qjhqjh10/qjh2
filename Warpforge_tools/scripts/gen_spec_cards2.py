#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_cards2.py — 卡牌定义/卡组数据说明书 (01_卡牌/卡组数据)

输出: d:/2/解包整理/说明书/03_卡牌/卡牌定义与卡组数据.md
  - 数据对象统计 (包定义/卡定义/卡组)
  - 字段结构说明 (ScriptableObject m_字段)
  - 卡包清单 (packId/army/tier/cardIds)
  - 卡组模板清单 (deckId/cards)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

U = 'd:/2/解包整理/01_卡牌/卡组数据/MonoBehaviour'
OUT = 'd:/2/解包整理/说明书/03_卡牌/卡牌定义与卡组数据.md'
CARD_INDEX = 'd:/2/解包整理/card_index.json'


def load(f):
    try:
        return json.load(open(os.path.join(U, f), encoding='utf-8'))
    except Exception:
        return None


def main():
    # 收集所有对象 (跳过 _pid 副本: 文件名尾缀 -?\d+ 为副本)
    objs = []
    for f in sorted(os.listdir(U)):
        if not f.endswith(".json"):
            continue
        base = f[:-5]
        parts = base.rsplit("_", 1)
        if len(parts) == 2 and parts[1].lstrip("-").isdigit():
            continue
        d = load(f)
        if d and d.get("m_Name"):
            objs.append(d)
    print("主对象数:", len(objs))

    # 按字段签名分类
    sigs = {}
    for d in objs:
        keys = tuple(sorted(k for k in d.keys() if k not in ('m_GameObject', 'm_Enabled', 'm_Script')))
        sigs.setdefault(keys, []).append(d)
    lines = ['# 卡牌定义与卡组数据说明书 (01_卡牌/卡组数据)\n',
             '> 来源: 解包整理/01_卡牌/卡组数据/MonoBehaviour/ (Unity ScriptableObject 序列化)',
             '> 生成: gen_spec_cards2.py\n',
             '## 对象统计\n',
             '- 主对象 (无 _pid 副本): **%d**' % len(objs),
             '- ScriptableObject 类型 (经 m_Script 字段, 按字段集合分类): %d' % len(sigs),
             '']
    lines.append('## 字段结构类型\n')
    lines.append('| 类 | 对象数 | 字段 |')
    lines.append('|---|---|---|')
    for keys, ob in sorted(sigs.items(), key=lambda x: -len(x[1])):
        lines.append('| %s | %d | %s |' % (ob[0].get('m_Name', '?'), len(ob), ', '.join(keys)))
    lines.append('')

    # 特定结构: 卡包 (packId/cardIds) 与 卡组 (deckId/cards)
    packs = [d for d in objs if 'packId' in d and 'cardIds' in d]
    decks = [d for d in objs if 'cards' in d and ('deckId' in d or 'nameRefId' in d)]
    cards_def = [d for d in objs if 'cardId' in d]

    lines.append('## 卡包定义 (packId/cardIds) — %d 个\n' % len(packs))
    if packs:
        lines.append('| packName | packId | packArmy | packTier | cardIds |')
        lines.append('|---|---|---|---|---|')
        for d in packs:
            lines.append('| %s | %s | %s | %s | %s |' % (
                d.get('packName', ''), d.get('packId', ''), d.get('packArmy', ''),
                d.get('packTier', ''), ','.join(d.get('cardIds', []) or [])))
        lines.append('')
    lines.append('## 卡组模板 (deckId/cards) — %d 个\n' % len(decks))
    if decks:
        lines.append('| deckId | deckName | cards |')
        lines.append('|---|---|---|')
        for d in decks[:400]:
            lines.append('| %s | %s | %s |' % (
                d.get('deckId', ''), d.get('deckName', d.get('m_Name', '')),
                ','.join(d.get('cards', []) or [])))
        if len(decks) > 400:
            lines.append('| ... (其余 %d 个) | | |' % (len(decks) - 400))
        lines.append('')

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print('✓', OUT, len(lines), '行')


if __name__ == '__main__':
    main()
