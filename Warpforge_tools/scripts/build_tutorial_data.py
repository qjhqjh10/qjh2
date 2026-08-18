#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_tutorial_data.py — 原版教程 turnScriptedData → 逐条引导数据
输入: 09_游戏数据/教程/MonoBehaviour/Warpforge_TutorialStage{1-6}.json
输出: D:/warpforge/data/tutorial_stages.json
      { "<StageN>": { "<回合序>": {"tips": [提示文本...], "actions": ["动作名", ...]} } }
用途: battle.gd 教程模式按关卡+回合显示下一条提示/玩家动作要求 (说明书: turnScriptedData)
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SRC = 'd:/2/解包整理/09_游戏数据/教程/MonoBehaviour/'
OUT = 'd:/warpforge/data/tutorial_stages.json'


def clean_text(t: str) -> str:
    """清洗教程文本: 去 <link=..>..</link> / <sprite> / <nobr>, <br>→换行"""
    if not t:
        return ''
    t = re.sub(r'<link=[^>]*>', '', t)
    t = t.replace('</link>', '')
    t = re.sub(r'<sprite[^>]*>', '', t)
    t = t.replace('<nobr>', '').replace('</nobr>', '')
    t = t.replace('<br>', '\n').replace('<br/>', '\n')
    return t.strip()


def parse_action(a: dict) -> dict:
    """scriptedActionData[0] 的 actionType 数字 → 动作名; actionType 文本如 'SmallTip (...)'"""
    at = a.get('actionType', '')
    player = str(a.get('playerAction', '0')) == '1'
    tip = ''
    if at.startswith('SmallTip'):
        m = re.match(r'SmallTip \((.*)\)\s*$', at, re.S)
        if m:
            tip = clean_text(m.group(1))
    # scriptedActionData[0] 里的 actionType 数字
    num = None
    try:
        sd = a.get('scriptedActionData')
        if isinstance(sd, str):
            sd = json.loads(sd.replace("'", '"'))
        if isinstance(sd, list) and sd and isinstance(sd[0], dict):
            num = sd[0].get('actionType')
    except Exception:
        pass
    return {'name': at.split(' (')[0], 'player': player, 'tip': tip, 'num': num}


def main() -> int:
    out = {}
    for i in range(1, 7):
        p = os.path.join(SRC, f'Warpforge_TutorialStage{i}.json')
        if not os.path.exists(p):
            print(f'✗ Stage{i} 缺失')
            continue
        j = json.load(open(p, encoding='utf-8'))
        steps = []
        for t in j.get('turnScriptedData', []):
            tips = []
            actions = []
            for a in t.get('scriptedActions', []):
                if not isinstance(a, dict):
                    continue
                pa = parse_action(a)
                if pa['tip']:
                    tips.append(pa['tip'])
                if pa['player']:
                    actions.append(pa['name'])
            tn = t.get('turnName', '')
            steps.append({
                'turn': str(t.get('scriptedTurn', 0)),
                'name': tn,
                'is_player': str(tn).startswith('Player'),
                'tips': tips,
                'actions': actions,
            })
        out[f'Stage{i}'] = {'steps': steps}
        n_tips = sum(len(s['tips']) for s in steps)
        n_ply = sum(1 for s in steps if s['is_player'])
        print(f'Stage{i}: {len(steps)} 步 (玩家 {n_ply}) / {n_tips} 提示')
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f'-> {OUT}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
