# UI 规格审计: TrophyDisplay

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:43
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
TrophyDisplay [godot(x-115.0 y930.0 w230.0 h300.0)]
  Collectable Highlight [inactive godot(x-146.1 y888.6 w292.5 h372.8)]
  bg [godot(x-115.0 y930.0 w230.0 h300.0)]
  BadgeDrawer [godot(x-115.0 y910.0 w230.0 h230.0)]
    Frame [godot(x-115.0 y910.0 w230.0 h230.0)]
    Badge [godot(x-115.0 y910.0 w230.0 h230.0)]
  title [txt=Trophy Name  godot(x-125.1 y1140.0 w249.1 h40.8)]
  Progress [godot(x-90.0 y1202.1 w180.0 h25.4)]
    ProgressBar [godot(x-91.3 y1185.9 w181.3 h47.6)]
      Background [godot(x-91.3 y1195.4 w181.3 h28.5)]
        Fill Area [godot(x-91.3 y1197.8 w181.3 h23.7)]
          Fill [godot(x-91.3 y1221.5 w0.0 h0.0)]
            end [godot(x-115.0 y1206.6 w29.4 h31.8)]
      Outline [godot(x-91.3 y1195.4 w181.3 h28.5)]
      counter [txt=100/200 godot(x-81.2 y1197.9 w162.9 h25.5)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| TrophyDisplay | ⚠️ 未命中 |
| Collectable Highlight | ⚠️ 未命中 |
| bg | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| BadgeDrawer | ✅ `scripts\drawer.gd:14 ##   AllianceBadgeDrawer / DeckDrawer / ForgePointIconDrawer / WildcardIconDrawer /; scripts\rank_row.gd:6 ##` |
| Frame | ✅ `scripts\battle.gd:80 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:81 co` |
| Badge | ✅ `scripts\campaign.gd:398 ## Unlock [772,850 245x45]×2 + Badge [1025,295 100x100] + 'Click to continue' [576,965 768x80]); scripts\c` |
| title | ✅ `scripts\achievements.gd:144 var title := str(a[1]); scripts\achievements.gd:181 # 标题 (原版 title @(152,20.9) 359x32.7 Bold)` |
| Progress | ✅ `scripts\daily_reward_popup.gd:278 # 个人进度条 (原版 Personal Progression 315x100: 里程碑 + 进度); scripts\deck_builder.gd:523 var bar := Text` |
| ProgressBar | ✅ `scripts\deck_builder.gd:523 var bar := TextureProgressBar.new(); scripts\deck_builder.gd:565 (_cost_bars[i] as TextureProgressBar)` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| end | ✅ `scripts\achievements.gd:1 extends Control; scripts\achievements.gd:11 const TEX_BAR_END := SPR + "40k_campaign_bar_end.png"      #` |
| Outline | ✅ `scripts\achievements.gd:218 # 描边 (原版 Outline 220.7x26.2 叠顶)` |
| counter | ✅ `scripts\achievements.gd:228 # 进度数字 (原版 counter '100/200' @(196.1,106.9) 132.4x21.8); scripts\battle.gd:4567 if msg.contains("count` |

## 摘要

- 规格元素: 15
- 代码命中: 12
- ⚠️未命中: 3 (以下需人工判断)

- `TrophyDisplay`
- `Collectable Highlight`
- `Fill Area`