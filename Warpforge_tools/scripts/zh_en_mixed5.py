# -*- coding: utf-8 -*-
"""混合串英文化第五批(补漏): rewards 通配符 / quests 漏网 / settings 长串"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

MAP = {
    r'd:\warpforge\scripts\rewards.gd': {
        '"Common通配符"': '"Common Wildcard"',
        '"Rare通配符"': '"Rare Wildcard"',
        '"Epic通配符"': '"Epic Wildcard"',
        '"Legendary通配符"': '"Legendary Wildcard"',
    },
    r'd:\warpforge\scripts\quests.gd': {
        '"每日重置"': '"Resets daily"',
        '"%d金"': '"%d Gold"',
        '"尚未达成下一个里程碑"': '"Next milestone not reached yet"',
        '"领取Rewards: %s x%d"': '"Claim Rewards: %s x%d"',
        '"未达成"': '"Not reached"',
    },
    r'd:\warpforge\scripts\settings.gd': {
        '"Warhammer 40,000: Warpforge · Godot single-player build\\n基于解包资源还原 · 规则书 1.5-3 · 1193 张Card"':
            '"Warhammer 40,000: Warpforge · Godot single-player build\\nrecreated from unpacked assets · rulebook 1.5-3 · 1193 cards"',
    },
}

total = 0
for fp, pairs in MAP.items():
    txt = open(fp, encoding='utf-8').read()
    n = 0
    for old, new in pairs.items():
        if old in txt:
            txt = txt.replace(old, new)
            n += 1
        else:
            print(f'  !! 未找到: {fp} :: {old[:50]}')
    open(fp, 'w', encoding='utf-8').write(txt)
    total += n
    print(f'{fp.split(chr(92))[-1]}: 替换 {n}/{len(pairs)}')
print('共', total)
