#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""arena_hud_layout.py — 从解包 battlearena1 场景 JSON 精确计算 HUD 元素屏幕位置
权威依据: GameObject → RectTransform JSON (m_AnchorMin/Max + m_Pivot + m_AnchoredPosition + m_SizeDelta)
Canvas 基准: 1920×1080 (原版 CanvasScaler reference)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'd:/2/解包整理/07_场景/battlearena1'
GO_DIR = os.path.join(BASE, 'GameObject')
RT_DIR = os.path.join(BASE, 'RectTransform')

W, H = 1920.0, 1080.0

TARGETS = [
    'EnemyInfo', 'PlayerInfo', 'Milestones', 'MatchSkulls Icon', 'MatchSkulls Score',
    'Energy And turn holder', 'TurnBtn', 'Energy Player',
    'PlayerDeck', 'EnemyDeck', 'DeckAndEnergyImage',
    'ShowCemeteryBtn', 'CardsInHandText', 'CardsInHandText (1)',
    'Card Display', 'Drag Attack Selector', 'Select Melee Button', 'Select Range Button',
    'Replay', 'ChatButton', 'MulliganContinueButton', 'SkipTutorial Button',
    'PlayerCardAreaSizeHelper To Use', 'HandArea', 'PlayerArea', 'EnemyArea',
]


def find_go(name: str):
    """按 m_Name 找 GameObject JSON (文件名 = <m_Name>.json 或 <m_Name>_<pid>.json)"""
    for f in os.listdir(GO_DIR):
        if not (f == name + '.json' or f.startswith(name + '_')):
            continue
        try:
            d = json.load(open(os.path.join(GO_DIR, f), encoding='utf-8'))
        except Exception:
            continue
        if d.get('m_Name') == name:
            return d
    return None


def get_rt(go: dict):
    for c in go.get('m_Component', []):
        comp = c.get('component') if isinstance(c, dict) else None
        if not comp:
            continue
        pid = comp.get('m_PathID')
        if pid is None:
            continue
        for cand in [f'RectTransform_{pid}.json', f'RectTransform_{pid}_{pid}.json']:
            p = os.path.join(RT_DIR, cand)
            if os.path.exists(p):
                return json.load(open(p, encoding='utf-8'))
    return None


def screen_rect(rt: dict):
    """Unity RectTransform → Godot 屏幕矩形 (x,y,width,height)"""
    amin = rt.get('m_AnchorMin', {})
    amax = rt.get('m_AnchorMax', {})
    piv = rt.get('m_Pivot', {})
    pos = rt.get('m_AnchoredPosition', {})
    sd = rt.get('m_SizeDelta', {})
    ax = amin.get('x', 0); ay = amin.get('y', 0)
    px = piv.get('x', 0.5); py = piv.get('y', 0.5)
    ox = pos.get('x', 0); oy = pos.get('y', 0)
    # 尺寸 = sizeDelta + 锚点矩形 (锚点固定时 = sizeDelta)
    w = sd.get('x', 0); h = sd.get('y', 0)
    # Unity: 左下原点 y 向上; Godot: 左上原点 y 向下
    left = ax * W + ox - px * w
    bottom = ay * H + oy - py * h
    top = H - (bottom + h)
    return (round(left), round(top), round(w), round(h))


def main():
    print(f"{'元素':<32} {'屏幕位置 (x,y,w×h)':<28} 锚点 min/max")
    for name in TARGETS:
        go = find_go(name)
        if go is None:
            print(f"{name:<32} 未找到 GameObject")
            continue
        rt = get_rt(go)
        if rt is None:
            print(f"{name:<32} 未找到 RectTransform")
            continue
        rect = screen_rect(rt)
        amin = rt.get('m_AnchorMin', {}); amax = rt.get('m_AnchorMax', {})
        print(f"{name:<32} ({rect[0]},{rect[1]}) {rect[2]}×{rect[3]}   "
              f"min({amin.get('x')},{amin.get('y')}) max({amax.get('x')},{amax.get('y')})")


if __name__ == '__main__':
    main()
