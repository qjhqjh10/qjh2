# UI 规格审计: Alliance Trophy Info Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:43
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Alliance Trophy Info Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  window [godot(x395.7 y188.4 w1128.6 h663.2)]
    Generic Window Red Background Big [godot(x395.7 y178.4 w1151.6 h717.4)]
    BadgeDrawer [godot(x435.9 y267.5 w508.2 h477.0)]
      Frame [godot(x435.9 y267.5 w508.2 h477.0)]
      Badge [godot(x435.9 y267.5 w508.2 h477.0)]
    Generic Close Button Orange [godot(x1487.1 y159.8 w74.4 h75.7)]
      Background [godot(x1495.2 y167.8 w56.9 h58.2)]
      Icon [godot(x1495.2 y167.8 w56.9 h58.2)]
    RightSide [godot(x960.0 y204.4 w548.3 h631.2)]
      Title [txt=Trophy Name godot(x976.1 y307.9 w516.7 h52.0)]
      Category [inactive txt=Sub-title godot(x976.0 y307.9 w516.7 h45.0)]
      Descripton [txt=Reach milestones Ultramarines Forge poin godot(x976.0 y352.8 w501.2 h180.1)]
      Controls [godot(x976.1 y569.0 w501.0 h188.0)]
        Progress [godot(x976.1 y729.8 w501.0 h54.4)]
          ProgressBar [godot(x976.1 y721.5 w501.0 h68.6)]
            Background [godot(x976.1 y735.2 w501.0 h41.2)]
              Fill Area [godot(x976.1 y740.2 w501.0 h31.2)]
                Fill [godot(x976.1 y771.4 w0.0 h0.0)]
                  end [godot(x952.4 y756.5 w29.4 h31.9)]
            Outline [godot(x976.1 y735.2 w501.0 h41.2)]
            counter [txt=100/200 godot(x1076.3 y742.1 w300.6 h34.3)]
          Next Tier [txt=Next Tier: godot(x976.1 y693.5 w501.0 h36.3)]
        selectButton [godot(x976.1 y729.8 w501.0 h54.4)]
          Checkbox [godot(x990.4 y736.6 w486.7 h58.2)]
            Toggle [godot(x990.4 y794.8 w0.0 h0.0)]
              CheckMark [godot(x990.4 y794.8 w0.0 h0.0)]
            Label [txt=Alliance featured trophy godot(x990.4 y794.8 w0.0 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Alliance Trophy Info Popup | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| window | ✅ `scripts\battle.gd:934 func _art_window_tex(path: String) -> Texture2D:; scripts\battle.gd:1046 var art_tex := _art_window_tex(str(` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| BadgeDrawer | ✅ `scripts\drawer.gd:14 ##   AllianceBadgeDrawer / DeckDrawer / ForgePointIconDrawer / WildcardIconDrawer /; scripts\rank_row.gd:6 ##` |
| Frame | ✅ `scripts\battle.gd:80 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:81 co` |
| Badge | ✅ `scripts\campaign.gd:398 ## Unlock [772,850 245x45]×2 + Badge [1025,295 100x100] + 'Click to continue' [576,965 768x80]); scripts\c` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:197 # 关闭按钮 (原版 Generic Close Button Orange 三层; 权威 y181.3 — 修正仅 X 图标+159.8); scripts\deck_info_popup.` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1886 #` |
| RightSide | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Category | ✅ `scripts\booster_info_popup.gd:5 ##   Text [960,204 548x631] Title/Category/Description +` |
| Descripton | ⚠️ 未命中 |
| Controls | ⚠️ 未命中 |
| Progress | ✅ `scripts\daily_reward_popup.gd:278 # 个人进度条 (原版 Personal Progression 315x100: 里程碑 + 进度); scripts\deck_builder.gd:523 var bar := Text` |
| ProgressBar | ✅ `scripts\deck_builder.gd:523 var bar := TextureProgressBar.new(); scripts\deck_builder.gd:565 (_cost_bars[i] as TextureProgressBar)` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| end | ✅ `scripts\achievements.gd:1 extends Control; scripts\achievements.gd:11 const TEX_BAR_END := SPR + "40k_campaign_bar_end.png"      #` |
| Outline | ✅ `scripts\achievements.gd:218 # 描边 (原版 Outline 220.7x26.2 叠顶)` |
| counter | ✅ `scripts\achievements.gd:228 # 进度数字 (原版 counter '100/200' @(196.1,106.9) 132.4x21.8); scripts\battle.gd:4567 if msg.contains("count` |
| Next Tier | ⚠️ 未命中 |
| selectButton | ⚠️ 未命中 |
| Checkbox | ✅ `scripts\settings.gd:267 # 3 个开关 (原版 Checkboxes VGroup: 行 (632.9,455.5/528.0/600.6) 视觉 → page 相对 y 322.6+i×80.6;; scripts\settings.` |
| Toggle | ✅ `scripts\battle.gd:2440 # Mute opponent (原版 ChatToggle 'Mute opponent' 42px 开关); scripts\collection.gd:93 # Filter Toggle (原版 [367.` |
| CheckMark | ✅ `scripts\quests.gd:19 const TEX_CRATE := SPR + "40k_Crate_Tier1_Iron.png"                      # 周常里程碑宝箱 (原版 CheckMark); scripts\qu` |
| Label | ✅ `scripts\achievements.gd:248 font_size: int, color: Color) -> Label:; scripts\achievements.gd:249 var lb := Label.new()` |

## 摘要

- 规格元素: 29
- 代码命中: 22
- ⚠️未命中: 7 (以下需人工判断)

- `Alliance Trophy Info Popup`
- `RightSide`
- `Descripton`
- `Controls`
- `Fill Area`
- `Next Tier`
- `selectButton`