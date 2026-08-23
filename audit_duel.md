# UI 规格审计: MessagePopupWindowDuel

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 17:46
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
MessagePopupWindowDuel [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Window [godot(x535.0 y245.0 w850.0 h430.0)]
    Generic Popup Background [godot(x535.0 y245.0 w850.0 h430.0)]
      Mask [godot(x545.4 y254.4 w829.7 h410.8)]
        Background fill [sprite=40k_popup_texture godot(x545.4 y254.4 w829.7 h410.8)]
    MessageText [txt=Do you want to challenge <b><color=#FCDE godot(x575.0 y363.1 w770.0 h126.7)]
    Buttons [godot(x572.3 y560.0 w775.4 h90.0)]
      Button Skirmish [godot(x397.3 y612.0 w350.0 h76.0)]
        Button Text [txt=Skirmish godot(x499.7 y618.5 w234.6 h63.0)]
        Skirmish image [godot(x405.9 y598.2 w100.0 h100.0)]
      Button Classic [godot(x397.3 y612.0 w350.0 h76.0)]
        Button Text [txt=Continue godot(x505.4 y618.5 w228.9 h63.0)]
        Classic Image [godot(x412.9 y599.1 w100.0 h100.0)]
  Generic Rounded Button Green [godot(x1341.8 y212.1 w75.0 h75.0)]
    Icon [godot(x1351.1 y222.4 w56.4 h54.4)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| MessagePopupWindowDuel | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Window | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:362 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ✅ `scripts\gacha.gd:256 # 右栏底 (原版 Rewards Panel: Background fill = 40k_popup_texture, 无木纹层 — 2026-08-23 删自创木纹); scripts\settings.gd:1` |
| MessageText | ✅ `scripts\choose_name.gd:61 # 提示 (原版 MessageText "Choose your player name" fontsize=40)` |
| Buttons | ✅ `scripts\battle.gd:2087 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Button Skirmish | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Skirmish image | ⚠️ 未命中 |
| Button Classic | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Classic Image | ⚠️ 未命中 |
| Generic Rounded Button Green | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1886 #` |

## 摘要

- 规格元素: 16
- 代码命中: 10
- ⚠️未命中: 6 (以下需人工判断)

- `MessagePopupWindowDuel`
- `Button Skirmish`
- `Skirmish image`
- `Button Classic`
- `Classic Image`
- `Generic Rounded Button Green`