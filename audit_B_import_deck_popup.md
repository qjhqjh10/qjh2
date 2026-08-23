# UI 规格审计: Import Deck Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:49
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Import Deck Popup [godot(x0.5 y0.5 w1919.0 h1079.0)]
  Background [godot(x-620.6 y-348.7 w3161.2 h1777.4)]
  Window [godot(x560.0 y234.1 w800.0 h451.8)]
    Generic Popup Background [godot(x560.0 y234.1 w800.0 h451.8)]
      Mask [godot(x570.4 y243.5 w779.7 h432.6)]
        Background fill [sprite=40k_popup_texture godot(x570.4 y243.5 w779.7 h432.6)]
    Main Search message [txt=Paste your deck godot(x610.0 y280.0 w700.0 h60.0)]
    Buttons [godot(x593.0 y562.4 w734.0 h90.0)]
      Generic UI Button [godot(x353.9 y614.9 w478.3 h75.0)]
        Button Text [txt=Confirm godot(x366.6 y614.3 w452.3 h75.0)]
    Error msg [txt=error msg godot(x593.0 y527.5 w734.0 h35.0)]
    Input Field [godot(x610.0 y370.0 w700.0 h141.1)]
      Text Area [godot(x620.0 y377.0 w680.0 h128.1)]
        Placeholder [txt=Enter text... godot(x620.0 y377.0 w680.0 h128.1)]
        Text [txt=​ godot(x620.0 y377.0 w680.0 h128.1)]
    Generic Close Button Green [godot(x1317.3 y202.1 w75.0 h75.0)]
      Icon [godot(x1326.6 y212.4 w56.4 h54.4)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Import Deck Popup | ✅ `scripts\deck_collection.gd:426 # 原版 Import Deck Popup: 粘贴卡组代码导入; scripts\import_deck_popup.gd:3 ## 导入卡组弹窗 (原版 Import Deck Popup, 菜` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Window | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ⚠️ 未命中 |
| Main Search message | ✅ `scripts\import_deck_popup.gd:60 # 标题 (原版 Main Search message 'Paste your deck' 50px, 弹窗内 y[46,106] 居中)` |
| Buttons | ✅ `scripts\battle.gd:2048 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Error msg | ✅ `scripts\import_deck_popup.gd:84 # 错误信息 (原版 Error msg 28px, 弹窗内 y[293,329])` |
| Input Field | ✅ `scripts\choose_name.gd:8 const TEX_INPUT := SPR + "40K_dropdown_bg.png"              # Choose Name Input Field 底; scripts\choose_n` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Generic Close Button Green | ✅ `scripts\import_deck_popup.gd:120 # 关闭 (原版 Generic Close Button Green: Window 中心 (960,620), anchor(0.5,0.5) ap(394.8,220.4) 75x75` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |

## 摘要

- 规格元素: 17
- 代码命中: 16
- ⚠️未命中: 1 (以下需人工判断)

- `Background fill`