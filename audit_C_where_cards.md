# UI 规格审计: WhereToGetCardsPopup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
WhereToGetCardsPopup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1290.3 y-746.2 w4574.6 h2572.4)]
  Generic Window Red Background Big [godot(x204.7 y16.3 w1510.6 h990.6)]
  Title [txt=Where to get Beast Snaggas cards godot(x283.0 y37.0 w1354.0 h109.5)]
  TopBar [godot(x283.0 y141.6 w1354.0 h6.0)]
  Scroll View [godot(x304.5 y159.3 w1277.0 h803.7)]
    Viewport [godot(x304.5 y159.3 w1277.0 h803.7)]
      Content [godot(x248.9 y159.3 w1388.1 h0.0)]
        Section For Reference [godot(x317.8 y159.3 w1250.4 h0.0)]
          Header [godot(x317.8 y133.0 w0.0 h52.5)]
            Background [godot(x317.8 y133.0 w0.0 h52.5)]
            Title [txt=Booster packs godot(x375.2 y133.0 w-30.8 h52.5)]
            Counter [txt=5/5 godot(x-1048.9 y133.0 w1366.7 h52.5)]
            Toggle [godot(x324.1 y144.0 w42.3 h30.5)]
          Content [godot(x317.8 y213.8 w1250.4 h0.0)]
            Card Drawer [godot(x325.3 y213.8 w191.6 h0.0)]
              Content [godot(x325.3 y213.8 w191.6 h0.0)]
                CardUI [godot(x421.1 y213.8 w0.0 h0.0)]
                  CreatedByText [inactive txt=Created by someone fancy godot(x421.1 y213.8 w0.0 h0.0)]
                  2DCard [godot(x421.1 y213.8 w0.0 h0.0)]
                    UI Collider [inactive godot(x421.1 y213.8 w0.0 h0.0)]
                    Front [godot(x421.1 y213.8 w0.0 h0.0)]
                      Card Highlight And Shadow [godot(x421.1 y213.8 w0.0 h0.0)]
                      CardImage [godot(x421.1 y213.8 w0.0 h0.0)]
                      CardFrame [godot(x421.1 y213.8 w0.0 h0.0)]
                    Cardback Container [inactive godot(x421.1 y213.8 w0.0 h0.0)]
                      Cardback Shadow SDF [godot(x421.1 y213.8 w0.0 h0.0)]
                      Cardback [godot(x421.1 y213.8 w0.0 h0.0)]
                  Card Ready for level up [inactive godot(x421.1 y213.8 w0.0 h0.0)]
                  New Card Badge [godot(x421.1 y213.8 w0.0 h0.0)]
                    Text [txt=Новинка! godot(x421.1 y213.8 w0.0 h0.0)]
                  Ban Icon [godot(x421.1 y213.8 w0.0 h0.0)]
                    Banned Text [txt=Запрещено godot(x421.1 y213.8 w0.0 h0.0)]
                Ban Icon [godot(x359.2 y250.8 w488.6 h253.7)]
                Converted Drawer [inactive godot(x401.8 y351.0 w38.6 h-22.5)]
                  Price Display [godot(x426.8 y347.0 w456.9 h93.5)]
                    icon [godot(x554.0 y347.0 w93.5 h93.5)]
                    text [txt=2000 godot(x647.5 y347.0 w109.0 h93.5)]
                  AlreadyOwned [txt=Already Owned godot(x167.6 y382.5 w507.0 h108.0)]
                Ephemeral Drawer [inactive godot(x401.8 y351.0 w38.6 h-22.5)]
                  Price Display [godot(x426.8 y347.0 w456.9 h93.5)]
                    icon [godot(x513.2 y347.0 w93.5 h93.5)]
                    text [txt=24 hours godot(x606.7 y347.0 w190.6 h93.5)]
                Collected Badge [inactive godot(x344.4 y193.8 w153.4 h0.0)]
                  Image [godot(x344.4 y193.8 w153.4 h0.0)]
                    Text (TMP) [txt=Claimed godot(x359.8 y193.8 w122.6 h0.0)]
              Event Catcher [godot(x325.3 y213.8 w191.6 h0.0)]
              Premium Highlight [inactive godot(x325.3 y213.8 w191.6 h0.0)]
                Highlight [godot(x300.3 y188.8 w241.6 h50.0)]
                Blackout [godot(x325.3 y213.8 w191.6 h0.0)]
                Badge [sprite=40k_campaign_Premium-icon godot(x325.3 y213.8 w57.5 h0.0)]
  Generic Close Button Orange [godot(x1656.8 y9.2 w74.4 h75.6)]
    Background [godot(x1665.0 y17.2 w56.8 h58.1)]
    Icon [godot(x1665.0 y17.2 w56.8 h58.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| WhereToGetCardsPopup | ✅ `scripts\collection.gd:836 ## 打开卡牌获取途径弹窗 (原版 WhereToGetCardsPopup); scripts\gacha.gd:231 # Where get cards 按钮 (说明书 [422,941 357x58]` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| TopBar | ✅ `scripts\main_menu.gd:489 ##   TopBarButtons(HorizontalLayoutGroup spacing 9.75 MiddleLeft @x[425.3,736.7] y[-0.2,71.2]):; scripts\` |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Section For Reference | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Card Drawer | ✅ `scripts\packs.gd:2 ## 卡包开包界面 (原版 Packs Tab 说明书: 横向滚动卡包列表 + Card Drawer 开包展示); scripts\packs.gd:194 # 开包结果区 (原版 Card Drawer)` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| CardUI | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| CreatedByText | ⚠️ 未命中 |
| 2DCard | ✅ `scripts\battle.gd:32 const CARD3D_W := 0.75   # 3D 卡牌平面尺寸 (原版 2DCard 2.0927×3.3313 × 玩家 desiredScale 0.36 = 0.753×1.199 ≈; scripts` |
| UI Collider | ⚠️ 未命中 |
| Front | ✅ `scripts\battle.gd:578 ["sautekh/Monolith Front Left1.obj", -9, 9, 0, 400.0, 90, 90], ["sautekh/Monolith Front Right1.obj",; script` |
| Card Highlight And Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| CardImage | ✅ `scripts\battle.gd:902 ## 立绘 cover-crop 到卡框内窗纵横比 (495/813) — 2DCard CardImage 层 (LRU 缓存)` |
| CardFrame | ⚠️ 未命中 |
| Cardback Container | ⚠️ 未命中 |
| Cardback Shadow SDF | ⚠️ 未命中 |
| Cardback | ✅ `scripts\battle.gd:425 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:102 b.tooltip_text = file.get` |
| Card Ready for level up | ⚠️ 未命中 |
| New Card Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Ban Icon | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
| Banned Text | ⚠️ 未命中 |
| Ban Icon | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Collected Badge | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Text (TMP) | ⚠️ 未命中 |
| Event Catcher | ⚠️ 未命中 |
| Premium Highlight | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Blackout | ✅ `scripts\scene_transition.gd:2 ## 场景过渡 (原版 07_场景/simpletransition: Blackout 全屏 + fadeDuration 1.0s 淡入 → 切场景 → 淡出); scripts\scene_tr` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:146 # 关闭按钮 (原版 Generic Close Button Orange); scripts\deck_info_popup.gd:212 # 关闭按钮 (原版 Generic Close` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |

## 摘要

- 规格元素: 54
- 代码命中: 39
- ⚠️未命中: 15 (以下需人工判断)

- `Section For Reference`
- `CreatedByText`
- `UI Collider`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Collected Badge`
- `Text (TMP)`
- `Event Catcher`
- `Premium Highlight`