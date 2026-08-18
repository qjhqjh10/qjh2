#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mark_noise_cards.py — 标记无数值卡中的索引噪音 (占位/条件牌) → noise=true
依据: 原版数据实体性核查 (2026-08-19) —— 占位名 (Normal Conditions×9/Normal×3/Default Conditions/v2)
     不在任何预组卡组引用、无 PnP 卡面、无 OCR 数值 → 索引噪音, 从可玩卡池剔除
输出: card_stats.json 加 noise 标记; GameData 加载时过滤 (图鉴/卡组组建不再显示)
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

PATH = 'd:/warpforge/data/card_stats.json'

# 占位噪音名单 (名称 + 阵营)
NOISE = {
    ('Normal Conditions', 'SaimHann'), ('Normal Conditions', 'BlackLegion'),
    ('Normal Conditions', 'DarkAngels'), ('Normal Conditions', 'Genestealers'),
    ('Normal Conditions', 'Sautekh'), ('Normal Conditions', 'Goff'),
    ('Normal Conditions', 'TauEmpire'), ('Normal Conditions', 'Leviathan'),
    ('Normal Conditions', 'Ultramarines'),
    ('Normal', 'AstraMilitarum'), ('Normal', 'EmperorsChildren'), ('Normal', 'Sororitas'),
    ('Default Conditions', 'SpaceWolves'),
    ('v2', 'DarkAngels'),
}


def main() -> int:
    data = json.load(open(PATH, encoding='utf-8'))
    cards = data.get('cards', [])
    marked = 0
    for c in cards:
        if (c.get('name'), c.get('faction')) in NOISE:
            c['noise'] = True
            c['noise_reason'] = '占位/条件牌索引噪音 (无卡面/无数值/不在卡组引用)'
            marked += 1
    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'标记 {marked} 张噪音卡')
    return 0


if __name__ == '__main__':
    sys.exit(main())
