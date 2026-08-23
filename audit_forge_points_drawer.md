# UI 规格审计: Forge Points Drawer

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:32
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Forge Points Drawer [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Content [godot(x960.0 y540.0 w0.0 h0.0)]
    Background [godot(x960.0 y540.0 w0.0 h0.0)]
    Image [godot(x960.0 y540.0 w0.0 h0.0)]
    Label [godot(x960.0 y540.0 w0.0 h0.0)]
      Quantity [txt=2 godot(x960.0 y540.0 w0.0 h0.0)]
      Name [txt=Forge Points godot(x960.0 y540.0 w0.0 h0.0)]
    Converted Drawer [inactive godot(x960.0 y540.0 w0.0 h0.0)]
      Price Display [godot(x960.0 y540.0 w0.0 h0.0)]
        icon [godot(x960.0 y540.0 w0.0 h0.0)]
        text [txt=2000 godot(x960.0 y540.0 w0.0 h0.0)]
      AlreadyOwned [txt=Already Owned godot(x960.0 y540.0 w0.0 h0.0)]
    Ephemeral Drawer [inactive godot(x960.0 y540.0 w0.0 h0.0)]
      Price Display [godot(x960.0 y540.0 w0.0 h0.0)]
        icon [godot(x960.0 y540.0 w0.0 h0.0)]
        text [txt=24 hours godot(x960.0 y540.0 w0.0 h0.0)]
    Collected Badge [inactive godot(x960.0 y540.0 w0.0 h0.0)]
      Image [godot(x960.0 y540.0 w0.0 h0.0)]
        Text (TMP) [txt=Claimed godot(x960.0 y540.0 w0.0 h0.0)]
    Army [txt=Leviathan godot(x960.0 y540.0 w0.0 h0.0)]
  Premium Highlight [inactive godot(x0.0 y0.0 w1920.0 h1080.0)]
    Highlight [godot(x-25.0 y-25.0 w1970.0 h1130.0)]
    Blackout [godot(x0.0 y0.0 w1920.0 h1080.0)]
    Badge [sprite=40k_campaign_Premium-icon godot(x0.0 y0.0 w576.0 h324.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Forge Points Drawer | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_collectio` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Label | ✅ `scripts\achievements.gd:248 font_size: int, color: Color) -> Label:; scripts\achievements.gd:249 var lb := Label.new()` |
| Quantity | ✅ `scripts\battle.gd:3256 # 奖励数 (RewardsHolder Quantity '2000': 胜利 2000 / 失败 0); scripts\forge.gd:342 # 数量 (原版 Quantity 独立元素: Name 75` |
| Name | ✅ `scripts\battle.gd:57 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:199 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| Collected Badge | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Text (TMP) | ⚠️ 未命中 |
| Army | ✅ `scripts\battle.gd:181 # 原版 battlearena1 场景树无阵营选择弹窗 (Army Selector 在模式选择界面) —; scripts\battle.gd:3216 # HolderRating x[568.8,755.8]` |
| Premium Highlight | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:52 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:493 var h` |
| Blackout | ✅ `scripts\scene_transition.gd:2 ## 场景过渡 (原版 07_场景/simpletransition: Blackout 全屏 + fadeDuration 1.0s 淡入 → 切场景 → 淡出); scripts\scene_tr` |
| Badge | ✅ `scripts\campaign.gd:398 ## Unlock [772,850 245x45]×2 + Badge [1025,295 100x100] + 'Click to continue' [576,965 768x80]); scripts\c` |

## 摘要

- 规格元素: 24
- 代码命中: 18
- ⚠️未命中: 6 (以下需人工判断)

- `Forge Points Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Collected Badge`
- `Text (TMP)`
- `Premium Highlight`