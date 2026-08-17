#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""migrate_desc.py — 2026-08-18 效果文字补全: card_stats.json desc 空但 keywords 有的卡
验证: 卡面"效果文字区"实际显示的就是关键词列表 (Dire Avenger 卡面只有 Waystone/Shuriken 2;
      Howling Banshee Exarch 的 desc = 'Waystone. Camouflage. Strike: Give +1 to your units' = keywords join;
      Ghazghkull Thraka 只有 Talent 无独立段落 → 关键词也空的卡 desc 保持空)
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
OUT = 'd:/warpforge/data/card_stats.json'


def main():
    with open(OUT, encoding='utf-8') as f:
        data = json.load(f)
    cards = data['cards']
    filled = 0
    for c in cards:
        if not (c.get('desc') or '').strip():
            kws = [str(k) for k in (c.get('keywords') or []) if str(k).strip()]
            if kws:
                c['desc'] = '. '.join(kws)
                filled += 1
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'desc 合成 {filled} 张; 总 {len(cards)} 张')


if __name__ == '__main__':
    main()
