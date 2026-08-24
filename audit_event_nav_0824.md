# UI 规格审计: Event Navigation Button

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-24 19:58
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Event Navigation Button [godot(x876.9 y80.1 w164.3 h169.7)]
  Selected highlight [godot(x876.9 y80.1 w164.3 h169.7)]
  Image [godot(x890.0 y81.8 w140.0 h140.0)]
    Over Image [godot(x901.1 y92.9 w117.8 h117.9)]
  Timer [godot(x848.3 y236.7 w221.5 h25.0)]
    Timer Text [inactive txt=5d 20h 15m godot(x848.3 y236.7 w221.5 h25.0)]
    Icon [inactive godot(x848.3 y236.7 w30.0 h25.0)]
  Text Background [godot(x886.5 y198.4 w147.0 h39.4)]
    Text (TMP) [godot(x886.5 y198.4 w147.0 h39.4)]
  Badge Highlight [godot(x995.0 y171.8 w35.0 h35.0)]
    OneText [godot(x995.0 y172.8 w35.0 h35.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Event Navigation Button | ⚠️ 未命中 |
| Selected highlight | ✅ `scripts\main_menu.gd:237 ##   键内: [Selected highlight 红底 164.3x169.7] + [图标: Home 156.3x137.4 / 其他 140² 中心(83.1,71.7)]; scripts\ma` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Over Image | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4918 var _clock_timer: Timer = null; scripts\battle.gd:4937 _clock_timer = Timer.new()` |
| Timer Text | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\ally_badge_drawe` |
| Text Background | ✅ `scripts\main_menu.gd:238 ##         + [Text Background nametag 146.9x39.4 中心(0.9,53.1)] + [Badge 35² 右上(-11.2,-91.7)]; scripts\mai` |
| Text (TMP) | ⚠️ 未命中 |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |

## 摘要

- 规格元素: 11
- 代码命中: 6
- ⚠️未命中: 5 (以下需人工判断)

- `Event Navigation Button`
- `Over Image`
- `Timer Text`
- `Text (TMP)`
- `OneText`