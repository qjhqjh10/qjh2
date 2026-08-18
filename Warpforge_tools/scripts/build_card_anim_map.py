#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_card_anim_map.py — 01_卡牌 12 阵营卡牌动画定义 → 映射表
输入: 01_卡牌/<阵营>/动画/MonoBehaviour/*.json (animInfo: animAdressable GUID + VFX 运动参数)
输出: D:/warpforge/data/card_anim_map.json
      { "<阵营>": { "<VFX名>": {startPosOption, endPosOption, timeMoving, vfxDelayTime, ...} },
        "_guid_summary": { "<GUID>": 使用次数 } }
用途: battle 施放卡牌时按 VFX 名查映射 → 触发对应动画/特效 (说明书: 卡名_动画类型 ability/self/quick)
"""
import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

ROOT = 'd:/2/解包整理/01_卡牌/'
OUT = 'd:/warpforge/data/card_anim_map.json'

KEYS = ['startPosOption', 'endPosOption', 'pointTowardsOption', 'vfxDelayTime',
        'startDelay', 'timeAtStartPos', 'timeMoving', 'timeAtEndPos',
        'shouldMoveVFX']


def main() -> int:
    out = {}
    guids = Counter()
    total = 0
    for d in os.listdir(ROOT):
        anim_dir = os.path.join(ROOT, d, '动画', 'MonoBehaviour')
        if not os.path.isdir(anim_dir):
            continue
        faction = d.split('_')[0]
        entries = {}
        for fn in os.listdir(anim_dir):
            if not fn.endswith('.json'):
                continue
            # 去 _<pid> 副本 (正负整数后缀)
            stem = fn[:-5]
            if '_' in stem:
                parts = stem.rsplit('_', 1)
                if parts[1].isdigit() or (parts[1].startswith('-') and parts[1][1:].isdigit()):
                    stem = parts[0]
            try:
                with open(os.path.join(anim_dir, fn), encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                continue
            info = data.get('animInfo') or {}
            if not info:
                continue
            guid = (info.get('animAdressable') or {}).get('m_AssetGUID', '')
            if guid:
                guids[guid] += 1
            entry = {k: info.get(k, 0) for k in KEYS}
            entry['guid'] = guid
            entry['ease_points'] = len((info.get('easeCurve') or {}).get('m_Curve', []))
            entries[stem] = entry
        if entries:
            out[faction] = entries
            total += len(entries)
        print(f'{faction}: {len(entries)} 个动画定义')
    out['_guid_summary'] = dict(guids)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f'\n共 {total} 个动画定义, {len(guids)} 个唯一 VFX GUID -> {OUT}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
