# UI 规格审计: Profile Cosmetic Tab

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Profile Cosmetic Tab [godot(x-32.7 y0.0 w1952.7 h1080.0)]
  Selected Item Panel [godot(x-32.7 y291.6 w269.0 h466.8)]
    Avatar Menu Item [godot(x-32.7 y359.7 w267.1 h273.6)]
      Raycast Target [godot(x11.4 y380.1 w178.9 h214.5)]
      Image Container [godot(x-32.7 y359.7 w267.1 h213.6)]
        Highlight [inactive godot(x-154.3 y258.2 w513.7 h409.3)]
        Border [godot(x-66.0 y354.4 w333.8 h266.9)]
        Image [godot(x-166.2 y250.2 w534.2 h427.2)]
      Avatar Name [txt=TEST NAME godot(x-47.7 y252.7 w297.1 h67.9)]
    Select Avatar Button [godot(x-7.5 y670.0 w218.7 h66.0)]
      Button Text [txt=Selecionar godot(x3.2 y676.4 w196.5 h53.1)]
    Toggle borde [godot(x-7.5 y771.0 w218.7 h66.0)]
      Button Text [txt=Toggle Border godot(x3.2 y777.4 w196.5 h53.1)]
  Item Display Panel [godot(x543.8 y210.2 w1068.7 h658.0)]
    Select Item [txt=Select your avatar godot(x565.2 y147.1 w512.4 h63.1)]
    Background [godot(x543.8 y210.2 w1068.7 h658.0)]
    Scroll Rect [godot(x565.2 y210.2 w1025.9 h644.8)]
      Item Drawer [godot(x565.2 y210.2 w1044.6 h0.0)]
        Avatar Item Small_Ref [godot(x565.2 y210.2 w0.0 h0.0)]
          Raycast Target [godot(x475.7 y93.9 w178.9 h214.4)]
          Image Container [godot(x565.2 y210.2 w0.0 h-37.3)]
            Highlight [godot(x563.7 y222.7 w6.3 h-67.5)]
            Border [godot(x565.2 y211.2 w0.0 h-46.7)]
            Image [godot(x565.2 y226.2 w0.0 h-74.7)]
          Avatar Name [inactive txt=Avatar name godot(x565.2 y210.2 w0.0 h41.4)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Profile Cosmetic Tab | ⚠️ 未命中 |
| Selected Item Panel | ✅ `scripts\player_profile.gd:500 # 选中预览 (场景 Selected Item Panel x318-587 y292-759; Avatar Menu Item 267.1x273.6 @(0,68)); scripts\pla` |
| Avatar Menu Item | ✅ `scripts\player_profile.gd:500 # 选中预览 (场景 Selected Item Panel x318-587 y292-759; Avatar Menu Item 267.1x273.6 @(0,68))` |
| Raycast Target | ⚠️ 未命中 |
| Image Container | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Avatar Name | ⚠️ 未命中 |
| Select Avatar Button | ✅ `scripts\player_profile.gd:509 # 原版 Select Avatar Button / Toggle borde 218.7x66.1 @(25,378)/(25,479) (Selected Item Panel 底部)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Toggle borde | ✅ `scripts\player_profile.gd:509 # 原版 Select Avatar Button / Toggle borde 218.7x66.1 @(25,378)/(25,479) (Selected Item Panel 底部)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Item Display Panel | ✅ `scripts\player_profile.gd:513 # 头像网格区 (场景 Item Display Panel x633-1702 y211-869); scripts\player_profile.gd:715 # 称号列表 (场景 Item Di` |
| Select Item | ✅ `scripts\player_profile.gd:522 # 标题 'Select your avatar' 35px 白 (原版 Select Item @(654,148))` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Scroll Rect | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\give_feedback_popup.gd:70 # ` |
| Item Drawer | ✅ `scripts\player_profile.gd:533 # 原版 Item Drawer: GridLayoutGroup cellSize 180x180 spacing(25,50) padding(left 13, top 40)` |
| Avatar Item Small_Ref | ⚠️ 未命中 |
| Raycast Target | ⚠️ 未命中 |
| Image Container | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Avatar Name | ⚠️ 未命中 |

## 摘要

- 规格元素: 25
- 代码命中: 17
- ⚠️未命中: 8 (以下需人工判断)

- `Profile Cosmetic Tab`
- `Raycast Target`
- `Image Container`
- `Avatar Name`
- `Avatar Item Small_Ref`
- `Raycast Target`
- `Image Container`
- `Avatar Name`