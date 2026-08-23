# UI 规格审计: ReRollPopup Variant

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:12
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
ReRollPopup Variant [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Window [godot(x535.0 y245.0 w850.0 h430.0)]
    Generic Popup Background [godot(x535.0 y245.0 w850.0 h430.0)]
      Mask [godot(x545.4 y254.4 w829.7 h410.8)]
        Background fill [sprite=40k_popup_texture godot(x545.4 y254.4 w829.7 h410.8)]
    MessageText [txt=Discard this mission and receive a new o godot(x575.0 y273.8 w770.0 h272.4)]
    Buttons [godot(x572.3 y534.0 w775.4 h90.0)]
      ButtonLeft [godot(x397.3 y586.0 w350.0 h76.0)]
        Button Text [txt=Cancel godot(x410.3 y586.0 w324.0 h76.0)]
      Price Display [godot(x397.3 y586.0 w350.0 h76.0)]
        Generic UI Button [godot(x397.3 y586.0 w350.0 h76.0)]
          Button Text [txt=Confirm  godot(x517.2 y586.0 w0.0 h76.0)]
          Price Display [godot(x628.7 y586.0 w0.0 h76.0)]
            icon [godot(x595.1 y662.0 w67.2 h0.0)]
            text [txt=300,00 godot(x747.5 y596.0 w0.0 h56.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| ReRollPopup Variant | ✅ `scripts\quests.gd:34 const REROLL_POPUP := preload("res://scripts/reroll_popup.gd")        # 任务重抽确认弹窗 (原版 ReRollPopup Var; scripts` |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Window | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\generic_p` |
| Mask | ✅ `scripts\draft.gd:362 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ✅ `scripts\gacha.gd:256 # 右栏底 (原版 Rewards Panel: Background fill = 40k_popup_texture, 无木纹层 — 2026-08-23 删自创木纹); scripts\settings.gd:1` |
| MessageText | ✅ `scripts\choose_name.gd:61 # 提示 (原版 MessageText "Choose your player name" fontsize=40); scripts\duel_popup.gd:5 ##   MessageText [5` |
| Buttons | ✅ `scripts\battle.gd:2087 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| ButtonLeft | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| Generic UI Button | ✅ `scripts\quests.gd:623 ## Collect 按钮 (原版 Generic UI Button: 40K_button 底 + tint 色; 未达成禁用)` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |

## 摘要

- 规格元素: 16
- 代码命中: 15
- ⚠️未命中: 1 (以下需人工判断)

- `ButtonLeft`