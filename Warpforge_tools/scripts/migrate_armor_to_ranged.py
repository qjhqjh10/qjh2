#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""migrate_armor_to_ranged.py — 2026-08-18 数值核查修正: card_stats.json 的 armor 字段实为远程攻击值
验证: 卡面左下紫色圆形(子弹图标)= 远程攻击; OCR 视觉模型误读为护甲 (7/7 抽样 vision 验证吻合)
原版护甲机制 = Armour X 关键词 (伤害减免 X 最低 1), 卡面无独立护甲图标
迁移: armor 值 → ranged_attack; armor 置 null (护甲全部来自关键词)
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
OUT = 'd:/warpforge/data/card_stats.json'


def main():
    with open(OUT, encoding='utf-8') as f:
        data = json.load(f)
    cards = data['cards']
    moved = 0
    for c in cards:
        if 'armor' in c and c.get('armor') is not None:
            c['ranged_attack'] = c['armor']
            c['armor'] = None
            moved += 1
        elif 'ranged_attack' not in c:
            c['ranged_attack'] = None
            c['armor'] = None
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'迁移完成: {moved} 张卡 armor→ranged_attack; 总 {len(cards)} 张')


if __name__ == '__main__':
    main()
