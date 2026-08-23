# UI 规格审计: Tutorial Message Window PopUp

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:12
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Tutorial Message Window PopUp [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Generic Window Red Background Big [godot(x442.6 y146.3 w1052.8 h733.4)]
  Event image [godot(x281.6 y34.1 w858.8 h858.8)]
  Container Campaign Points [godot(x566.5 y340.1 w321.0 h323.8)]
    Icon Campaign Points Drawer Variant [godot(x566.5 y663.9 w0.0 h0.0)]
      Content [godot(x566.5 y663.9 w0.0 h0.0)]
        Campaign Glow [godot(x566.5 y663.9 w0.0 h0.0)]
        Image [godot(x566.5 y663.9 w0.0 h0.0)]
        Converted Drawer [inactive godot(x566.5 y663.9 w0.0 h0.0)]
          Price Display [godot(x566.5 y663.9 w0.0 h0.0)]
            icon [godot(x566.5 y663.9 w0.0 h0.0)]
            text [txt=2000 godot(x566.5 y663.9 w0.0 h0.0)]
          AlreadyOwned [txt=Already Owned godot(x566.5 y663.9 w0.0 h0.0)]
        Ephemeral Drawer [inactive godot(x566.5 y663.9 w0.0 h0.0)]
          Price Display [godot(x566.5 y663.9 w0.0 h0.0)]
            icon [godot(x566.5 y663.9 w0.0 h0.0)]
            text [txt=24 hours godot(x566.5 y663.9 w0.0 h0.0)]
  Texts [godot(x1005.0 y190.0 w450.0 h580.0)]
    TitleText [txt=Welcome to Warpforge! godot(x1005.0 y190.0 w450.0 h105.0)]
    DescriptionText [txt=War rages across the stars. Ancient civi godot(x1025.0 y308.6 w410.0 h425.0)]
    Tap To continue [txt=Click to continue godot(x1005.0 y730.4 w450.0 h79.2)]
  Collider [godot(x0.0 y0.0 w1920.0 h1080.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Tutorial Message Window PopUp | ✅ `scripts\tutorial.gd:13 const TUT_POPUP := preload("res://scripts/tutorial_msg_popup.gd")   # 开场欢迎弹窗 (原版 Tutorial Message Wi; scrip` |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Event image | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Container Campaign Points | ✅ `scripts\tutorial_msg_popup.gd:4 ##   Event image [281.6,34.1 858.8x858.8] (color 0.8 灰) + Container Campaign Points [566.5,340.1 3` |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_collectio` |
| Campaign Glow | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:199 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| Texts | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| TitleText | ✅ `scripts\expiration_popup.gd:5 ##   Texts [1005,190 450x580]: TitleText 34px 白 / DescriptionText 28px 白 / 'Click to continue' 30px ` |
| DescriptionText | ✅ `scripts\expiration_popup.gd:5 ##   Texts [1005,190 450x580]: TitleText 34px 白 / DescriptionText 28px 白 / 'Click to continue' 30px ` |
| Tap To continue | ⚠️ 未命中 |
| Collider | ✅ `scripts\base_event_popup.gd:5 ##   Collider 全屏按钮 (点击继续); scripts\base_event_popup.gd:25 # 全屏 Collider 按钮 (点击继续/关闭)` |

## 摘要

- 规格元素: 23
- 代码命中: 18
- ⚠️未命中: 5 (以下需人工判断)

- `Icon Campaign Points Drawer Variant`
- `Campaign Glow`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Tap To continue`