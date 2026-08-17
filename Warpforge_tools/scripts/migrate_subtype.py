#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""migrate_subtype.py — 2026-08-18 类型核查修正: card_stats.json subtype 规范化
① OCR type 误读为 Warlord 的单位 (卡面芯片实为 Infantry, 如 Turyan Ghauze/Adelaide the Serene/Hrolf the Ironhowl)
② 大小写统一: spell→Spell / ability→Ability
③ hero 卡 subtype 空 → Warlord
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
OUT = 'd:/warpforge/data/card_stats.json'

WARLORD_MISREAD = {'Turyan Ghauze', 'Adelaide the Serene', 'Hrolf the Ironhowl'}


def main():
    with open(OUT, encoding='utf-8') as f:
        data = json.load(f)
    cards = data['cards']
    fixed = 0
    for c in cards:
        sub = c.get('subtype') or ''
        if c.get('name') in WARLORD_MISREAD:
            c['subtype'] = 'Infantry'
            fixed += 1
            continue
        if sub == 'spell':
            c['subtype'] = 'Spell'
            fixed += 1
        elif sub == 'ability':
            c['subtype'] = 'Ability'
            fixed += 1
        elif c.get('type') == 'hero' and sub == '':
            c['subtype'] = 'Warlord'
            fixed += 1
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'subtype 修正 {fixed} 张; 总 {len(cards)} 张')


if __name__ == '__main__':
    main()
