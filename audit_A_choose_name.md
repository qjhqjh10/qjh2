# UI 规格审计: ChooseNameWindow

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
ChooseNameWindow [inactive godot(x-0.1 y0.0 w1920.2 h1080.0)]
  Dark Background [godot(x-620.6 y-213.7 w3161.2 h1777.4)]
  Generic Popup Background [godot(x519.5 y395.0 w881.0 h301.0)]
    Mask [godot(x529.9 y404.4 w860.7 h281.8)]
      Background fill [sprite=40k_popup_texture godot(x529.9 y404.4 w860.7 h281.8)]
  Choose Name Input Field [godot(x540.1 y496.0 w836.2 h60.0)]
    Text Area [godot(x550.1 y503.0 w816.2 h47.0)]
      Placeholder [godot(x550.1 y503.0 w816.2 h47.0)]
      Text [txt=​ godot(x550.1 y503.0 w816.2 h47.0)]
  MessageText [txt=Choose your player name godot(x540.1 y426.9 w836.2 h74.2)]
  Change Name Button [godot(x822.8 y578.2 w274.4 h67.6)]
    Generic UI Button [godot(x822.8 y578.2 w274.4 h67.6)]
      Button Text [txt=Free godot(x835.8 y587.8 w248.4 h48.4)]
      Price Display [inactive godot(x833.2 y586.8 w251.4 h51.4)]
        icon [godot(x881.9 y581.6 w61.8 h61.8)]
        text [txt=300,00 godot(x943.7 y586.8 w92.2 h51.4)]
  Generic Close Button Green [godot(x1358.3 y362.5 w75.0 h75.0)]
    Icon [godot(x1367.6 y372.8 w56.4 h54.4)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| ChooseNameWindow | ✅ `scripts\choose_name.gd:2 ## 选名窗口 (原版 ChooseNameWindow 说明书: Choose name Window 1209x400 + 输入框 + OK); scripts\main_menu.gd:512 # 点击名` |
| Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ⚠️ 未命中 |
| Choose Name Input Field | ✅ `scripts\choose_name.gd:8 const TEX_INPUT := SPR + "40K_dropdown_bg.png"              # Choose Name Input Field 底; scripts\choose_n` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| MessageText | ✅ `scripts\choose_name.gd:61 # 提示 (原版 MessageText "Choose your player name")` |
| Change Name Button | ⚠️ 未命中 |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Generic Close Button Green | ✅ `scripts\import_deck_popup.gd:120 # 关闭 (原版 Generic Close Button Green: Window 中心 (960,620), anchor(0.5,0.5) ap(394.8,220.4) 75x75` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |

## 摘要

- 规格元素: 18
- 代码命中: 16
- ⚠️未命中: 2 (以下需人工判断)

- `Background fill`
- `Change Name Button`