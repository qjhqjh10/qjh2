# UI 规格审计: GenericPromptWindow

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 17:46
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
GenericPromptWindow [godot(x0.5 y0.5 w1919.0 h1079.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Window [godot(x510.0 y540.0 w900.0 h0.0)]
    Generic Popup Background [godot(x460.0 y490.0 w1000.0 h100.0)]
      Mask [godot(x470.4 y499.4 w979.7 h80.8)]
        Background fill [sprite=40k_popup_texture godot(x470.4 y499.4 w979.7 h80.8)]
    MessageText [txt=Text goes here godot(x60.0 y540.0 w900.0 h0.0)]
    inputs [godot(x60.0 y540.0 w900.0 h0.0)]
      template [godot(x60.0 y495.0 w0.0 h90.0)]
        Text Area [godot(x70.0 y502.0 w-20.0 h77.0)]
          Placeholder [txt=TESTE godot(x70.0 y502.0 w-20.0 h77.0)]
          Text [txt=​ godot(x70.0 y502.0 w-20.0 h77.0)]
    Error Message [txt=INVALID PASSWORD ERROR godot(x60.0 y540.0 w900.0 h0.0)]
    Buttons [godot(x60.0 y540.0 w900.0 h0.0)]
      CancelButton [godot(x60.0 y500.0 w0.0 h80.0)]
        Button Text [txt=Cancel godot(x72.7 y499.4 w-26.0 h80.0)]
      OkButton [godot(x60.0 y500.0 w0.0 h80.0)]
        Button Text [txt=CONFIRM godot(x72.7 y499.4 w-26.0 h80.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| GenericPromptWindow | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Window | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:362 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ✅ `scripts\gacha.gd:256 # 右栏底 (原版 Rewards Panel: Background fill = 40k_popup_texture, 无木纹层 — 2026-08-23 删自创木纹); scripts\settings.gd:1` |
| MessageText | ✅ `scripts\choose_name.gd:61 # 提示 (原版 MessageText "Choose your player name" fontsize=40)` |
| inputs | ⚠️ 未命中 |
| template | ✅ `scripts\battle.gd:138 var _pending_template_faction := ""  # 模式选择模板卡组阵营 (卡ID映射缺失 → 按阵营随机); scripts\battle.gd:275 deck1 = _build_te` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:153 var bg := TextureRect.new(); scripts\achievements.gd:155 bg.expand_mode = TextureRect.EXPAND_IGNORE_SI` |
| Error Message | ⚠️ 未命中 |
| Buttons | ✅ `scripts\battle.gd:2087 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| CancelButton | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| OkButton | ✅ `scripts\choose_name.gd:81 # OK 按钮 (原版 OkButton 307x60; 子 TextureRect 铺底 + 文字 Label 盖其上)` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |

## 摘要

- 规格元素: 18
- 代码命中: 14
- ⚠️未命中: 4 (以下需人工判断)

- `GenericPromptWindow`
- `inputs`
- `Error Message`
- `CancelButton`