# UI 规格审计: Card Drawer

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:32
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Card Drawer [inactive godot(x405.3 y319.6 w284.1 h430.4)]
  Content [godot(x405.3 y319.6 w284.1 h430.4)]
    CardUI [godot(x547.4 y534.8 w0.0 h0.0)]
      CreatedByText [inactive txt=Created by someone fancy godot(x547.4 y534.8 w0.0 h0.0)]
      2DCard [godot(x547.4 y534.8 w0.0 h0.0)]
        UI Collider [inactive godot(x547.4 y534.8 w0.0 h0.0)]
        Front [godot(x547.4 y534.8 w0.0 h0.0)]
          Card Highlight And Shadow [godot(x547.4 y534.8 w0.0 h0.0)]
          CardImage [godot(x547.4 y534.8 w0.0 h0.0)]
          CardFrame [godot(x547.4 y534.8 w0.0 h0.0)]
        Cardback Container [inactive godot(x547.4 y534.8 w0.0 h0.0)]
          Cardback Shadow SDF [godot(x547.4 y534.8 w0.0 h0.0)]
          Cardback [godot(x547.4 y534.8 w0.0 h0.0)]
      Card Ready for level up [inactive godot(x547.4 y534.8 w0.0 h0.0)]
      New Card Badge [godot(x547.4 y534.8 w0.0 h0.0)]
        Text [txt=Новинка! godot(x547.4 y534.8 w0.0 h0.0)]
      Ban Icon [godot(x547.4 y534.8 w0.0 h0.0)]
        Banned Text [txt=Запрещено godot(x547.4 y534.8 w0.0 h0.0)]
    Ban Icon [godot(x439.3 y356.6 w516.3 h382.8)]
    Converted Drawer [inactive godot(x486.4 y779.7 w121.9 h20.5)]
      Price Display [godot(x511.4 y775.6 w457.0 h93.6)]
        icon [godot(x638.7 y775.6 w93.5 h93.6)]
        text [txt=2000 godot(x732.2 y775.6 w109.0 h93.6)]
      AlreadyOwned [txt=Already Owned godot(x293.9 y854.2 w507.0 h108.0)]
    Ephemeral Drawer [inactive godot(x486.4 y779.7 w121.9 h20.5)]
      Price Display [godot(x511.4 y775.6 w457.0 h93.6)]
        icon [godot(x597.8 y775.6 w93.6 h93.6)]
        text [txt=24 hours godot(x691.4 y775.6 w190.6 h93.6)]
    Collected Badge [inactive godot(x433.7 y687.0 w227.3 h43.0)]
      Image [godot(x433.7 y687.0 w227.3 h43.0)]
        Text (TMP) [txt=Claimed godot(x456.5 y691.3 w181.8 h34.4)]
  Event Catcher [godot(x405.3 y319.6 w284.1 h430.4)]
  Premium Highlight [inactive godot(x405.3 y319.6 w284.1 h430.4)]
    Highlight [godot(x380.3 y294.6 w334.1 h480.4)]
    Blackout [godot(x405.3 y319.6 w284.1 h430.4)]
    Badge [sprite=40k_campaign_Premium-icon godot(x405.3 y319.6 w85.3 h129.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Card Drawer | ✅ `scripts\packs.gd:2 ## 卡包开包界面 (原版 Packs Tab 说明书: 横向滚动卡包列表 + Card Drawer 开包展示); scripts\packs.gd:217 # 开包结果区 (原版 Card Drawer)` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_collectio` |
| CardUI | ✅ `scripts\card_displayer.gd:151 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| CreatedByText | ⚠️ 未命中 |
| 2DCard | ✅ `scripts\battle.gd:42 const CARD3D_W := 0.75   # 3D 卡牌平面尺寸 (原版 2DCard 2.0927×3.3313 × 玩家 desiredScale 0.36 = 0.753×1.199 ≈; scripts` |
| UI Collider | ⚠️ 未命中 |
| Front | ✅ `scripts\battle.gd:392 ##   原版 2D 层 (BackCanvas/FrontCanvas) 无任何背景元素, 背景 100% 来自 3D 烘焙场景 = 冻结帧等效, 见 战斗2D层改造规格_0823.md §3); scripts\` |
| Card Highlight And Shadow | ✅ `scripts\battle.gd:52 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2812 # 悬浮` |
| CardImage | ✅ `scripts\battle.gd:935 ## 立绘 cover-crop 到卡框内窗纵横比 (495/813) — 2DCard CardImage 层 (LRU 缓存)` |
| CardFrame | ⚠️ 未命中 |
| Cardback Container | ⚠️ 未命中 |
| Cardback Shadow SDF | ⚠️ 未命中 |
| Cardback | ✅ `scripts\battle.gd:453 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:194 b.tooltip_text = file.get` |
| Card Ready for level up | ⚠️ 未命中 |
| New Card Badge | ✅ `scripts\card_displayer.gd:151 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Text | ✅ `scripts\achievements.gd:153 var bg := TextureRect.new(); scripts\achievements.gd:155 bg.expand_mode = TextureRect.EXPAND_IGNORE_SI` |
| Ban Icon | ✅ `scripts\card_displayer.gd:151 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
| Banned Text | ⚠️ 未命中 |
| Ban Icon | ✅ `scripts\card_displayer.gd:151 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
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
| Event Catcher | ⚠️ 未命中 |
| Premium Highlight | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:52 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:493 var h` |
| Blackout | ✅ `scripts\scene_transition.gd:2 ## 场景过渡 (原版 07_场景/simpletransition: Blackout 全屏 + fadeDuration 1.0s 淡入 → 切场景 → 淡出); scripts\scene_tr` |
| Badge | ✅ `scripts\campaign.gd:398 ## Unlock [772,850 245x45]×2 + Badge [1025,295 100x100] + 'Click to continue' [576,965 768x80]); scripts\c` |

## 摘要

- 规格元素: 36
- 代码命中: 23
- ⚠️未命中: 13 (以下需人工判断)

- `CreatedByText`
- `UI Collider`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Collected Badge`
- `Text (TMP)`
- `Event Catcher`
- `Premium Highlight`