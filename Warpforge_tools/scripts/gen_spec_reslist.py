#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_reslist.py — 04_音频 / 05_视频 / 10_字体 说明书生成器 (10_资源清单)

输出 (说明书/10_资源清单/):
  README.md  — 三类总览 + 使用状态
  音频.md    — 04_音频 四子目录 (督军语音/音乐/音效库/音频控制) 全量清单
  视频.md    — 05_视频 8 mp4 + VideoClip 引用
  字体.md    — 10_字体 4 ttf 全清单 + 字体资源/图集化包

用法: py312/python.exe Warpforge_tools/scripts/gen_spec_reslist.py
"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

U = 'd:/2/解包整理/'
W = 'd:/2/解包整理/说明书/10_资源清单/'


def wfile(fp, txt):
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(txt)
    print('✓ %s (%d 行)' % (os.path.relpath(fp, 'd:/2/解包整理/说明书'), txt.count(chr(10))))


def walk_files(p):
    out = []
    for root, _dirs, fs in os.walk(p):
        for f in sorted(fs):
            out.append(os.path.relpath(os.path.join(root, f), p))
    return out


def gen_audio():
    A = os.path.join(U, '04_音频')
    lines = ['# 音频说明书 (04_音频, 1940 文件)', '',
             '> 权威= 各 AudioClip JSON/音频文件; 使用状态见 解包资源列表清单.md',
             '',
             '## 目录总览', '',
             '| 子目录 | 文件数 | 内容 | 在用状态 |',
             '|---|---|---|---|',
             '| 督军语音 | %d | 督军/教程语音 ogg | ✅ 在 (battle/card_displayer 语音按钮) |' % len(walk_files(os.path.join(A, '督军语音'))),
             '| 音乐 | %d | 主题音乐 (Main Theme/Menu Idle Theme) | ✅ 在 (sfx.gd 跨场景) |' % len(walk_files(os.path.join(A, '音乐'))),
             '| 音效库 | %d | 战斗/UI 音效 wav+ogg (含 AudioSource/GO 预制体引用) | ⚠️ 部分 (16 UI+28 战斗在用) |' % len(walk_files(os.path.join(A, '音效库'))),
             '| 音频控制 | %d | AudioMixerController (音量分组骨架) | 参考 |' % len(walk_files(os.path.join(A, '音频控制'))),
             '', '## 督军语音全清单', '']
    for f in walk_files(os.path.join(A, '督军语音')):
        if f.endswith('.ogg'):
            lines.append('- `%s`' % os.path.basename(f))
    lines += ['', '## 音乐', '']
    for f in walk_files(os.path.join(A, '音乐')):
        if f.endswith('.ogg'):
            lines.append('- `%s`' % os.path.basename(f))
    lines += ['', '## 音效库 (AudioClip: wav %d / ogg %d)' % (
        len([f for f in walk_files(os.path.join(A, '音效库')) if f.endswith('.wav')]),
        len([f for f in walk_files(os.path.join(A, '音效库')) if f.endswith('.ogg')])),
              '']
    # 仅列 wav/ogg 文件本身 (bundle json 与预制体引用不列)
    for f in walk_files(os.path.join(A, '音效库')):
        if f.endswith(('.wav', '.ogg')):
            lines.append('- `%s`' % os.path.basename(f))
    wfile(os.path.join(W, '音频.md'), '\n'.join(lines) + '\n')


def gen_video():
    V = os.path.join(U, '05_视频')
    files = walk_files(V)
    mp4s = [f for f in files if f.endswith('.mp4')]
    vids = [f for f in files if f.endswith('.json') and 'VideoClip' in f]
    uses = {
        'Warpforge Intro.mp4': '开场 Logo 动画 (8-12s; 主项目已实现 main_menu._play_intro)',
        'Victory Video.mp4': '胜利结算',
        'Defeat Video.mp4': '失败结算',
        'Draw Video.mp4': '平局结算',
        'Main Menu Practice Video.mp4': '模式卡 hover (原版; 主项目已移除 hover 视频)',
        'Main Menu Multiplayer Video.mp4': '模式卡 hover (同上)',
        'Gacha Crate Opening.mp4': 'Gacha 开箱 (已解包, 按需)',
        'Menu_Chronomancer_Animation.mp4': 'Chronomancer 菜单动画 (未用)',
    }
    lines = ['# 视频说明书 (05_视频, 18 文件)', '',
             '| 视频 | 用途 | 状态 |', '|---|---|---|']
    for m in mp4s:
        lines.append('| %s | %s | %s |' % (os.path.basename(m), uses.get(os.path.basename(m), ''),
                      '✅ 在' if os.path.basename(m) in uses and uses[os.path.basename(m)].startswith(('开场', '胜利', '失败', '平局'))
                      else ('曾用(已移除)' if 'hover' in uses.get(os.path.basename(m), '') else '未用')))
    lines += ['',
              '> VideoClip json %d 个 = mp4 的 Unity 引用容器 (同名无 mp4 的为未导出片段)' % len(vids),
              '> 视频不入 git (大文件), 路径引用记录在 解包资源使用地图.md', '']
    wfile(os.path.join(W, '视频.md'), '\n'.join(lines))


def gen_fonts():
    F = os.path.join(U, '10_字体')
    ttf = walk_files(F)
    lines = ['# 字体说明书 (10_字体, 189 文件)', '',
             '> 项目实际使用: 4 个 ttf → assets/fonts/ (sfx/UI 全局字体)',
             '', '## TTF 全清单', '', '| 字体 | 说明 |', '|---|---|']
    fonts = {
        'NotoSerifCJK-Regular.ttf': '中文/日文界面字体 (UI 中文后备; 当前 UI 文字=JSON 英文, 中文待本地化)',
        'LiberationSans.ttf': '英文无衬线 (主字体)',
        'PerfectDOSVGA437.ttf': '像素/终端风格 (数字与图标字形, 排位/计数)',
    }
    for f in sorted(set(f for f in ttf if f.endswith('.ttf'))):
        lines.append('| %s | %s |' % (os.path.basename(f), fonts.get(os.path.basename(f), '')))
    lines += ['',
              '## 结构',
              '',
              '- `fonts/` / `resources/` — Font json (Font_*.json 引用 ttf) + ttf 原件',
              '- `字体资源/` — Unity 图集化字体内存包 (AssetBundle/Material/MonoBehaviour/Texture2D, 181 文件) — Godot 不用 (直接用 ttf)',
              '',
              '> Godot 项目只取 ttf; Font json/LegacyRuntime/图集化资源跳过', '']
    wfile(os.path.join(W, '字体.md'), '\n'.join(lines))


def gen_readme():
    A = os.path.join(U, '04_音频')
    V = os.path.join(U, '05_视频')
    F = os.path.join(U, '10_字体')
    lines = ['# 资源清单说明书 (04_音频/05_视频/10_字体/11_着色器)', '',
             '> 补全 2026-08-22: 原 00_总览 "未覆盖(按需再析)" 的 3 类资源 → 本目录索引化',
             '',
             '| 类别 | 文件数 | 说明书 | 状态 |',
             '|---|---|---|---|',
             '| 04_音频 | %d | [音频.md](音频.md) | ✅ 在用 |' % (sum(len(walk_files(os.path.join(A, d))) for d in os.listdir(A))),
             '| 05_视频 | %d | [视频.md](视频.md) | ✅ 8 mp4 (6 用/2 待) |' % len(walk_files(V)),
             '| 10_字体 | %d | [字体.md](字体.md) | ✅ 4 ttf 在用 |' % len(walk_files(F)),
             '| 11_着色器 | 527 | — | ❌ Godot 无直接转换 (Unity Shader→Godot shader 需手译; 战场后处理已在 lut_vignette.gdshader 近似) |',
             '',
             '## 其他小类现状',
             '',
             '- 02_装饰品 → 见 [09_装饰品](../09_装饰品/README.md)',
             '- 01_卡牌 语音: 已在各阵营说明书 (03_卡牌/<阵营>.md) 引用; 督军语音另见 音频.md',
             '', '## 生成器',
             '',
             '- gen_spec_reslist.py (本目录) / gen_spec_cosmetics.py (09_装饰品)', '']
    wfile(os.path.join(W, 'README.md'), '\n'.join(lines))


def main():
    os.makedirs(W, exist_ok=True)
    gen_audio()
    gen_video()
    gen_fonts()
    gen_readme()


if __name__ == '__main__':
    main()
