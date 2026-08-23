#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spec_cover_audit.py — 说明书覆盖门禁 (12 解包类 ↔ 说明书 11 类)

每次会话开头跑一次: 输出"无说明书覆盖的解包子目录"清单, 让体系缺口自己暴露
(2026-08-22 人肉排查才发现 02_装饰品 整类缺失 — 本工具让这类缺口变机器可见)

用法: py312 spec_cover_audit.py [--out 报告.md]
"""
import os
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

U = 'd:/2/解包整理/'
W = 'd:/2/解包整理/说明书/'

# 说明书覆盖映射: 解包类 -> 已说明书化的子目录 (README 数据源标注; 更新说明书体系时同步)
COVERED = {
    '01_卡牌': ('*',),                      # 13 阵营说明书 + 定义 + card_index
    '02_装饰品': ('卡背', '头像', '督军立绘', '联盟徽章', '战役奖励背景', '边框', '定义数据'),   # 09_装饰品
    '03_界面UI': ('菜单', '主菜单', '通用窗口', '通用静态资源', '图集', '去重资源', '光标',
                  '军队图标', '排位图标', '收件箱横幅', '特惠内容', '运营图标', '运营菜单图',
                  '共享资源', '卡组选择按钮'),                                             # 04_界面UI 索引
    '04_音频': ('督军语音', '音乐', '音效库', '音频控制'),                                  # 10_资源清单/音频
    '05_视频': ('menus', 'sharedassets0', 'videos', 'AssetBundle'),                        # 10_资源清单/视频
    '06_模型': ('*',),                      # 07_模型 逐OBJ清单 (1030)
    '07_场景': ('*',),                      # 02_战场_场景 15 场景说明书
    '08_预制体特效': ('战斗预制体', '共享资源'),   # 06_特效 (VFX 977 根 + 共享 303)
    '09_游戏数据': ('*',),                  # 05_游戏数据 4 文件
    '10_字体': ('fonts', 'resources', '字体资源'),                                         # 10_资源清单/字体
    '11_着色器': ('*',),
    '12_主程序资源': ('*',),                # 08 说明书 (引擎设置 + 84 管理器)
}


def main():
    out_path = None
    if '--out' in sys.argv:
        out_path = sys.argv[sys.argv.index('--out') + 1]
    lines = ['# 说明书覆盖门禁 (%s)' % datetime.now().strftime('%Y-%m-%d %H:%M'), '',
             '> 12 解包大类 ↔ 说明书 11 类; 未覆盖子目录 = 潜在缺口 (按需再析/补全)',
             '', '| 解包类 | 未覆盖子目录 | 说明 |', '|---|---|---|']
    gaps = []
    for cat, cov in sorted(COVERED.items()):
        d = os.path.join(U, cat)
        subs = sorted([s for s in os.listdir(d) if os.path.isdir(os.path.join(d, s))])
        if cov == ('*',):
            uncovered = []
        else:
            uncovered = [s for s in subs if s not in cov]
        if uncovered:
            gaps.append(cat)
            lines.append('| %s | %s | %s |' % (cat, ', '.join('`%s`' % s for s in uncovered),
                                               '11_着色器=Godot 无直接转换(已知豁免)' if cat == '11_着色器' else ''))
        else:
            lines.append('| %s | — | ✅ 全覆盖 |' % cat)
    lines += ['', '## 结论', '']
    if gaps:
        lines.append('- ⚠️ %d 类存在未覆盖子目录: %s' % (len(gaps), ', '.join(gaps)))
    else:
        lines.append('- ✅ 12 类全部有说明书覆盖 (11_着色器为已知豁免)')
    out = '\n'.join(lines)
    if out_path:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(out)
        print('✓ 输出: %s' % out_path)
    else:
        print(out)


if __name__ == '__main__':
    main()
