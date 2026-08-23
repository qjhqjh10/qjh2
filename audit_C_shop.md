# UI 规格审计: Shop Menu Variant

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Shop Menu Variant [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Content Area [godot(x167.2 y70.9 w1752.8 h1009.1)]
    Background [godot(x167.2 y70.9 w1752.8 h1009.1)]
    Tab Buttons [godot(x167.2 y70.9 w165.0 h1009.1)]
      Shop Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Pacotes godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1014.6 w35.0 h35.0)]
          OneText [godot(x201.4 y1015.5 w35.0 h35.0)]
      Shadow [godot(x167.2 y70.9 w47.6 h1009.1)]
    Tabs [godot(x167.2 y70.9 w1752.8 h1009.1)]
      Shop Tab [godot(x167.2 y70.9 w1752.8 h1009.1)]
        daily shop header [godot(x167.2 y70.9 w1752.8 h85.0)]
          Line [inactive godot(x167.2 y150.9 w1752.8 h10.0)]
          TimeCounter [godot(x367.5 y70.9 w311.4 h80.0)]
            RefreshText [txt=Atualiza em: godot(x367.5 y150.9 w0.0 h0.0)]
            Time [txt=12h 24m godot(x367.5 y150.9 w0.0 h0.0)]
        Packs Scroll View [godot(x329.8 y127.6 w1590.2 h952.4)]
          Viewport [godot(x329.8 y127.6 w1590.2 h952.4)]
            Content [godot(x329.8 y127.6 w1590.2 h952.4)]
              Comsetic Item Shop Container [godot(x329.8 y1080.0 w0.0 h0.0)]
                raycast target [inactive godot(x329.8 y1080.0 w0.0 h0.0)]
                background [godot(x328.8 y1079.0 w2.0 h2.0)]
                  Available Counter [inactive txt=Available: 1/5 godot(x328.9 y1080.7 w1.7 h0.2)]
                  price-bg [godot(x328.8 y1080.4 w2.0 h0.5)]
                    Price Display Button [godot(x329.2 y1080.6 w1.1 h0.2)]
                      Generic UI Button [godot(x329.2 y1080.6 w1.1 h0.2)]
                        Button Text [inactive godot(x342.2 y1106.8 w-24.9 h-52.1)]
                        Price Display [godot(x329.3 y1080.6 w0.9 h0.2)]
                          icon [godot(x309.4 y1080.8 w39.7 h0.0)]
                          text [txt=300,00 godot(x369.0 y1080.6 w124.5 h33.1)]
                    WebShop Button Square Variant [inactive godot(x330.0 y1080.7 w0.7 h0.4)]
                      Highlight [sprite=OctagonUI Filled Fade SDF godot(x308.7 y1062.5 w43.3 h36.8)]
                      Button Image [godot(x330.0 y1080.7 w0.7 h0.4)]
                      Icon [godot(x343.9 y1085.2 w-27.1 h-8.6)]
                  Counter [inactive godot(x328.8 y1080.6 w2.0 h0.1)]
                    Text (TMP) [txt=x14 godot(x388.2 y1089.8 w-116.9 h-10.6)]
                  DrawerHolder [godot(x339.2 y1062.5 w-18.9 h18.1)]
                    Cardback Drawer [inactive godot(x339.2 y1062.5 w-18.9 h18.1)]
                      Content [godot(x329.8 y1071.5 w0.0 h0.0)]
                        Image [godot(x329.8 y1071.5 w0.0 h0.0)]
                        Label [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Quantity [txt=2 godot(x329.8 y1071.5 w0.0 h0.0)]
                          Name [txt=Legendary Wildcard godot(x329.8 y1071.5 w0.0 h0.0)]
                        Converted Drawer [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Price Display [godot(x329.8 y1071.5 w0.0 h0.0)]
                            icon [godot(x329.8 y1071.5 w0.0 h0.0)]
                            text [txt=2000 godot(x329.8 y1071.5 w0.0 h0.0)]
                          AlreadyOwned [txt=Already Owned godot(x329.8 y1071.5 w0.0 h0.0)]
                        Ephemeral Drawer [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Price Display [godot(x329.8 y1071.5 w0.0 h0.0)]
                            icon [godot(x329.8 y1071.5 w0.0 h0.0)]
                            text [txt=24 hours godot(x329.8 y1071.5 w0.0 h0.0)]
                        Collected Badge [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Image [godot(x329.8 y1071.5 w0.0 h0.0)]
                            Text (TMP) [txt=Claimed godot(x329.8 y1071.5 w0.0 h0.0)]
                      Premium Highlight [inactive godot(x339.2 y1062.5 w-18.9 h18.1)]
                        Highlight [godot(x314.2 y1037.5 w31.1 h68.1)]
                        Blackout [godot(x339.2 y1062.5 w-18.9 h18.1)]
                        Badge [sprite=40k_campaign_Premium-icon godot(x339.2 y1062.5 w-5.7 h5.4)]
                    Title Drawer [inactive godot(x339.2 y1062.5 w-18.9 h18.1)]
                      Content [godot(x329.8 y1071.5 w0.0 h0.0)]
                        Background [godot(x329.8 y1071.5 w0.0 h0.0)]
                        Image [godot(x329.8 y1071.5 w0.0 h0.0)]
                          Image Top [godot(x329.8 y1071.5 w0.0 h0.0)]
                        Label [godot(x329.8 y1071.5 w0.0 h0.0)]
                          Quantity [inactive txt=500 godot(x329.8 y1071.5 w0.0 h0.0)]
                          Name [txt=TITLE godot(x329.8 y1071.5 w0.0 h0.0)]
                        Converted Drawer [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Price Display [godot(x329.8 y1071.5 w0.0 h0.0)]
                            icon [godot(x329.8 y1071.5 w0.0 h0.0)]
                            text [txt=2000 godot(x329.8 y1071.5 w0.0 h0.0)]
                          AlreadyOwned [txt=Already Owned godot(x329.8 y1071.5 w0.0 h0.0)]
                        Ephemeral Drawer [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Price Display [godot(x329.8 y1071.5 w0.0 h0.0)]
                            icon [godot(x329.8 y1071.5 w0.0 h0.0)]
                            text [txt=24 hours godot(x329.8 y1071.5 w0.0 h0.0)]
                        Collected Badge [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Image [godot(x329.8 y1071.5 w0.0 h0.0)]
                            Text (TMP) [txt=Claimed godot(x329.8 y1071.5 w0.0 h0.0)]
                        Army [txt=Leviathan godot(x329.8 y1071.5 w0.0 h0.0)]
                        Title [txt="Warrior of the raging winds " godot(x329.8 y1071.5 w0.0 h0.0)]
                      Premium Highlight [inactive godot(x339.2 y1062.5 w-18.9 h18.1)]
                        Highlight [godot(x314.2 y1037.5 w31.1 h68.1)]
                        Blackout [godot(x339.2 y1062.5 w-18.9 h18.1)]
                        Badge [sprite=40k_campaign_Premium-icon godot(x339.2 y1062.5 w-5.7 h5.4)]
                    Avatar Drawer Shop Variant [godot(x339.2 y1062.5 w-18.9 h18.1)]
                      Content [godot(x329.8 y1071.5 w0.0 h0.0)]
                        Background [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                        Army [txt=Goff godot(x329.8 y1071.5 w0.0 h0.0)]
                        avatarBG [godot(x329.8 y1071.5 w0.0 h0.0)]
                          avatar [godot(x329.8 y1071.5 w0.0 h0.0)]
                        Label [godot(x329.8 y1071.5 w0.0 h0.0)]
                          Name [txt=Legendary Wildcard godot(x329.8 y1071.5 w0.0 h0.0)]
                        Converted Drawer [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Price Display [godot(x329.8 y1071.5 w0.0 h0.0)]
                            icon [godot(x329.8 y1071.5 w0.0 h0.0)]
                            text [txt=2000 godot(x329.8 y1071.5 w0.0 h0.0)]
                          AlreadyOwned [txt=Already Owned godot(x329.8 y1071.5 w0.0 h0.0)]
                        Ephemeral Drawer [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Price Display [godot(x329.8 y1071.5 w0.0 h0.0)]
                            icon [godot(x329.8 y1071.5 w0.0 h0.0)]
                            text [txt=24 hours godot(x329.8 y1071.5 w0.0 h0.0)]
                        Collected Badge [inactive godot(x329.8 y1071.5 w0.0 h0.0)]
                          Image [godot(x329.8 y1071.5 w0.0 h0.0)]
                            Text (TMP) [txt=Claimed godot(x329.8 y1071.5 w0.0 h0.0)]
                      Premium Highlight [inactive godot(x339.2 y1062.5 w-18.9 h18.1)]
                        Highlight [godot(x314.2 y1037.5 w31.1 h68.1)]
                        Blackout [godot(x339.2 y1062.5 w-18.9 h18.1)]
                        Badge [sprite=40k_campaign_Premium-icon godot(x339.2 y1062.5 w-5.7 h5.4)]
                TimedOffer [inactive godot(x79.8 y691.5 w250.0 h50.0)]
                  Text (TMP) [txt=Limited time offer!! godot(x104.8 y696.5 w200.0 h40.0)]
                  Text (TMP) (1) [txt=<sprite name=Atlas_trait_icon_fast>5d 20 godot(x104.8 y741.2 w200.0 h28.5)]
                New [inactive godot(x329.8 y691.5 w146.7 h50.0)]
                  Text (TMP) [txt=New! godot(x344.4 y696.5 w117.4 h40.0)]
                  Text (TMP) (1) [txt=-30% godot(x344.4 y741.2 w117.4 h28.5)]
          Empty Collection Warning [inactive godot(x164.8 y42.6 w1805.2 h1037.4)]
            Warning [txt=There are no deck in your collection for godot(x164.8 y42.6 w1805.2 h1037.4)]
    Shadow (1) [inactive godot(x330.4 y70.9 w49.4 h1009.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Shop Menu Variant | ✅ `scripts\shop.gd:2 ## 商店界面 (原版 Shop Menu Variant 说明书: 左侧 Tab Buttons + Shop Tab 商品网格)` |
| Content Area | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\rewards.gd:145` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Tab Buttons | ✅ `scripts\collection.gd:150 # ---- Tab Buttons (原版 [167.2,158.6 165x921.4] 左竖排 4 tab — RectTransform_-1995773233925987627) ----; scr` |
| Shop Icon | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| Tabs | ✅ `scripts\shop.gd:163 # 3 个标签页 (Tabs 区 x330-1920)` |
| Shop Tab | ✅ `scripts\shop.gd:2 ## 商店界面 (原版 Shop Menu Variant 说明书: 左侧 Tab Buttons + Shop Tab 商品网格)` |
| daily shop header | ✅ `scripts\shop.gd:197 # 每日商店头部 (原版 daily shop header 85 高: TimeCounter 'Atualiza em:' 30号 + 实时倒计时` |
| Line | ✅ `scripts\battle.gd:106 var _drag_line: Line2D = null      # 攻击拖线 (近战红 / 远程紫 / 技能金); scripts\battle.gd:3715 # 准星 (原版 Attack Target R` |
| TimeCounter | ✅ `scripts\shop.gd:197 # 每日商店头部 (原版 daily shop header 85 高: TimeCounter 'Atualiza em:' 30号 + 实时倒计时; scripts\shop.gd:198 # 位于 (367,71)` |
| RefreshText | ⚠️ 未命中 |
| Time | ✅ `scripts\battle.gd:1392 var now := Time.get_ticks_msec(); scripts\battle.gd:3320 "date": Time.get_date_string_from_system(),` |
| Packs Scroll View | ✅ `scripts\packs.gd:162 # 横向滚动卡包列表 (原版 Packs Scroll View x[163.5,1920] y[0,1080] 全高, pack 行垂直居中); scripts\shop.gd:234 # 原版 Packs Scro` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Comsetic Item Shop Container | ✅ `scripts\shop.gd:469 # ---------------- 商品卡 (场景 Comsetic Item Shop Container 220x356) ----------------` |
| raycast target | ⚠️ 未命中 |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| Available Counter | ⚠️ 未命中 |
| price-bg | ⚠️ 未命中 |
| Price Display Button | ✅ `scripts\gacha.gd:216 # 开箱价格按钮 (说明书 Price Display Button [385,794 429x110]: Open Chest Button + 门票 icon + '1'); scripts\packs.gd:23` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| WebShop Button Square Variant | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Button Image | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Text (TMP) | ⚠️ 未命中 |
| DrawerHolder | ✅ `scripts\shop.gd:495 # 卡背大图 (原版 DrawerHolder 中部 712x1080 大图区域, 2 张错位卡背)` |
| Cardback Drawer | ✅ `scripts\packs.gd:217 # 卡背大图 (原版 Cardback Drawer 2 张错位卡背)` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Quantity | ✅ `scripts\battle.gd:3203 # 奖励数 (RewardsHolder Quantity '2000': 胜利 2000 / 失败 0); scripts\ranked.gd:216 # 计数 (原版 Numer Of Army Decks [` |
| Name | ✅ `scripts\battle.gd:47 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
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
| Premium Highlight | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Blackout | ✅ `scripts\scene_transition.gd:2 ## 场景过渡 (原版 07_场景/simpletransition: Blackout 全屏 + fadeDuration 1.0s 淡入 → 切场景 → 淡出); scripts\scene_tr` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Title Drawer | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Image Top | ⚠️ 未命中 |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Quantity | ✅ `scripts\battle.gd:3203 # 奖励数 (RewardsHolder Quantity '2000': 胜利 2000 / 失败 0); scripts\ranked.gd:216 # 计数 (原版 Numer Of Army Decks [` |
| Name | ✅ `scripts\battle.gd:47 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
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
| Army | ✅ `scripts\battle.gd:171 # 原版 battlearena1 场景树无阵营选择弹窗 (Army Selector 在模式选择界面) —; scripts\battle.gd:3163 # HolderRating x[568.8,755.8]` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Premium Highlight | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Blackout | ✅ `scripts\scene_transition.gd:2 ## 场景过渡 (原版 07_场景/simpletransition: Blackout 全屏 + fadeDuration 1.0s 淡入 → 切场景 → 淡出); scripts\scene_tr` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Avatar Drawer Shop Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Army | ✅ `scripts\battle.gd:171 # 原版 battlearena1 场景树无阵营选择弹窗 (Army Selector 在模式选择界面) —; scripts\battle.gd:3163 # HolderRating x[568.8,755.8]` |
| avatarBG | ⚠️ 未命中 |
| avatar | ✅ `scripts\battle.gd:140 var _top_avatar: TextureRect    # 敌方圆形头像 (原版玩家框左竖区); scripts\battle.gd:141 var _bottom_avatar: TextureRect  ` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Name | ✅ `scripts\battle.gd:47 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
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
| Premium Highlight | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Blackout | ✅ `scripts\scene_transition.gd:2 ## 场景过渡 (原版 07_场景/simpletransition: Blackout 全屏 + fadeDuration 1.0s 淡入 → 切场景 → 淡出); scripts\scene_tr` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| TimedOffer | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Text (TMP) (1) | ⚠️ 未命中 |
| New | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Text (TMP) | ⚠️ 未命中 |
| Text (TMP) (1) | ⚠️ 未命中 |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Shadow (1) | ✅ `scripts\collection.gd:219 # 右缘阴影 (原版 Shadow (1) [330.4,70.9 49.4x1009.1] 黑 0.47 — 2026-08-21 审查修正 0.31)` |

## 摘要

- 规格元素: 121
- 代码命中: 85
- ⚠️未命中: 36 (以下需人工判断)

- `Shop Icon`
- `OneText`
- `RefreshText`
- `raycast target`
- `Available Counter`
- `price-bg`
- `WebShop Button Square Variant`
- `Button Image`
- `Text (TMP)`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Collected Badge`
- `Text (TMP)`
- `Premium Highlight`
- `Title Drawer`
- `Image Top`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Collected Badge`
- `Text (TMP)`
- `Premium Highlight`
- `Avatar Drawer Shop Variant`
- `avatarBG`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Collected Badge`
- `Text (TMP)`
- `Premium Highlight`
- `TimedOffer`
- `Text (TMP)`
- `Text (TMP) (1)`
- `Text (TMP)`
- `Text (TMP) (1)`