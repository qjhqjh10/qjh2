# -*- coding: utf-8 -*-
"""更新 CLAUDE.md: 修正坐标换算矛盾 + 新增 UI 英文准则"""
import io

p = 'd:/2/CLAUDE.md'
s = io.open(p, encoding='utf-8').read()

old = '''② **分辨率依据（2026-08-19 已查证）**：原版 CanvasScaler `m_ReferenceResolution = {x:1920.0, y:1080.0}`（m_UiScaleMode=1 ScaleWithScreenSize、m_MatchWidthOrHeight=0 匹配宽度，见 `07_场景/battlearena1/MonoBehaviour/MonoBehaviour_4731.json`），即**原版 UI 坐标基于 1920×1080**；当前项目 `project.godot` viewport 同为 1920×1080 → **Unity JSON 的坐标/尺寸数值可直接照抄使用，无需换算**（同一参考分辨率、同一匹配方式）。'''

new = '''② **分辨率依据（2026-08-19 查证；2026-08-20 修正"直接照抄"错误结论）**：原版 CanvasScaler 参考分辨率 1920×1080（匹配宽度），当前项目 viewport 同为 1920×1080 → **分辨率相同、数值可直接换算（≠直接照抄）**。**m_AnchoredPosition 不可直接照抄进 Godot offset**：① Unity y 向上、Godot y 向下 → 必须 y 翻转（godot_top = 1080 - unity_top - h）② anchoredPosition 是 **pivot 点**相对锚点（锚点拉伸时相对**锚点矩形中心**）的位置，pivot≠(0.5,0.5) 必须修正（如 PlayerDeck pivot(0.5,0)）③ 子元素坐标相对父，需**沿 m_Father 链式累加** ④ 根元素（m_Father=0，如 Gacha/Forge/Packs Tab）的 anchoredPosition/sizeDelta 仍相对全屏 Canvas 有效（x+163.8 之类偏移不可丢）。**权威换算工具：`Warpforge_tools/scripts/chain_rect.py`**（沿 m_Father 链式累加 → Godot 绝对屏幕坐标；同名 GO 多变体必须用 PathID）。子代理/整理文档给的坐标一律用 chain_rect 交叉验证后再用（实测子代理报告有 2 处坐标错误、整理文档沿袭错误如 social 积分面板）。'''

assert old in s, '分辨率依据段未找到'
s = s.replace(old, new)

# 新增 UI 文字语言准则 (用户 2026-08-20 指令)
add = '''- **UI 文字语言（用户指定 2026-08-20）**：UI 显示文字一律用 **Unity JSON 里的英文**（m_text，如 TurnText 'END TURN'、'Cards left: X/Y'），**不用中文替代**；中文以后另做本地化。卡牌名/描述（游戏数据）保持原样。**改日志/事件文本必须同步 `battle.gd _fx_from_event` 的关键词解析**（中文 2-4 字符 vs 英文 8-13 字符，偏移/索引不同——实测英文化后 VFX 解析偏移导致部署/战术动画全灭；`%` 格式串参数顺序也必须同步调整）。批量替换中文→英文时**只替换用户可见字符串**（引号内），注释不动；替换后跑 battle_sim/rule_test 验证事件文本与解析同步。
'''
anchor = '- **视频截图分析暂停（用户指定 2026-08-19，最高优先）**'
assert anchor in s
s = s.replace(anchor, add + anchor)

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('CLAUDE.md 更新完成')
