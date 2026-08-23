# UI 规格审计: Deck info Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 08:19
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Deck info Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Generic Window Red Background Big [godot(x134.5 y82.0 w1705.0 h950.0)]
  Warlord Image [godot(x-109.0 y-34.0 w1108.0 h1108.0)]
  Deck Details [godot(x659.0 y106.1 w670.8 h111.2)]
    Game Mode Icon [godot(x659.0 y162.3 w100.0 h110.0)]
    Game Mode Separator [sprite=40k_Generic Smooth line godot(x659.0 y162.3 w8.9 h110.0)]
    Deck Details [godot(x363.1 y161.7 w591.8 h111.2)]
      Deck Name [txt=DECK NAME godot(x468.1 y170.0 w485.6 h54.5)]
      Army Icon [godot(x363.1 y162.3 w100.0 h110.0)]
      Warlord Name [txt=Warlord name godot(x468.1 y222.3 w487.0 h50.0)]
  Buttons [godot(x669.3 y885.8 w1101.4 h80.1)]
    Practice Deck [godot(x344.8 y925.9 w324.5 h80.1)]
      Button Text [txt=Práctica godot(x359.3 y933.7 w294.4 h64.4)]
    Edit Deck [godot(x344.8 y925.9 w324.5 h80.1)]
      Button Text [txt=Editar godot(x359.3 y933.7 w294.4 h64.4)]
    Select Deck [godot(x344.8 y925.9 w324.5 h80.1)]
      Button Text [txt=Seleccionar godot(x359.3 y933.7 w294.4 h64.4)]
  Deck Options [godot(x1263.7 y93.0 w519.9 h150.0)]
    Switch Deck Info Button [godot(x1226.5 y205.2 w74.4 h75.6)]
      Background [godot(x1234.7 y213.2 w56.9 h58.1)]
      Icon [godot(x1234.7 y213.2 w56.9 h58.1)]
    Duplicate Button [godot(x1226.5 y205.2 w74.4 h75.6)]
      Background [godot(x1234.7 y213.2 w56.9 h58.1)]
      Icon [godot(x1234.7 y213.2 w56.9 h58.1)]
    Share Button [godot(x1226.5 y205.2 w74.4 h75.6)]
      Background [godot(x1234.7 y213.2 w56.9 h58.1)]
      Icon [godot(x1234.7 y213.2 w56.9 h58.1)]
    Share On Chat [godot(x1226.5 y205.2 w74.4 h75.6)]
      Background [godot(x1234.7 y213.2 w56.9 h58.1)]
      Icon [godot(x1234.7 y213.2 w56.9 h58.1)]
    Delete Button [godot(x1226.5 y205.2 w74.4 h75.6)]
      Background [godot(x1234.7 y213.2 w56.9 h58.1)]
      Icon [godot(x1234.7 y213.2 w56.9 h58.1)]
  Info Panel [godot(x659.0 y218.1 w1140.0 h650.0)]
    Deck List [godot(x659.0 y218.1 w1140.0 h650.0)]
      Content [godot(x659.0 y218.1 w1140.0 h650.0)]
        Deck Selector Card Info button [godot(x659.0 y868.1 w0.0 h0.0)]
          Content [godot(x659.0 y868.1 w0.0 h0.0)]
            Background [godot(x659.0 y868.1 w0.0 h0.0)]
              Rarity Gradient [godot(x658.5 y868.1 w0.5 h-0.1)]
              Background Border [godot(x642.7 y868.1 w16.3 h0.0)]
              Cost Image [godot(x658.8 y865.1 w0.0 h6.0)]
                Cost [txt=5 godot(x634.4 y865.8 w48.8 h4.6)]
              banned Icon [godot(x655.9 y862.0 w0.0 h6.0)]
              Text fill [godot(x659.0 y868.1 w-5.0 h0.0)]
                Card Name [txt=Card Name godot(x659.0 y868.1 w0.0 h0.0)]
                Count [txt=x2 godot(x659.0 y868.1 w0.0 h0.0)]
    Deck Info [godot(x659.0 y218.1 w1140.0 h650.0)]
      Lore Text [inactive txt=Start here! Overwhelm your opponent with godot(x1014.0 y667.3 w444.2 h140.4)]
      Cardback [godot(x1271.7 y270.5 w388.5 h564.2)]
        Cardback Front [godot(x1292.9 y263.9 w387.7 h559.3)]
      Deck Information Cost/balance text [txt=Cartas / Coste godot(x740.0 y305.6 w473.8 h60.0)]
      Deck Information cost drawer [godot(x825.4 y378.8 w288.0 h360.0)]
        Background [godot(x827.1 y379.7 w284.6 h358.3)]
        Content [godot(x768.2 y379.7 w402.4 h358.3)]
          Deck CostQuanityt Row Drawer [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
          Deck CostQuanityt Row Drawer (1) [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
          Deck CostQuanityt Row Drawer (2) [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
          Deck CostQuanityt Row Drawer (3) [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
          Deck CostQuanityt Row Drawer (4) [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
          Deck CostQuanityt Row Drawer (5) [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
          Deck CostQuanityt Row Drawer (6) [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
          Deck CostQuanityt Row Drawer (7) [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
          Deck CostQuanityt Row Drawer (8) [godot(x566.9 y721.0 w402.5 h34.0)]
            Card Cost [txt=0 godot(x573.0 y720.1 w46.0 h35.8)]
            Cards in deck [txt=0 godot(x916.6 y720.0 w46.0 h36.0)]
            Slider [godot(x632.0 y720.0 w272.4 h36.0)]
              Background [godot(x632.0 y723.6 w272.4 h29.8)]
              Fill [godot(x632.0 y760.2 w0.0 h-8.5)]
  Generic Close Button Orange [godot(x1782.8 y63.2 w74.4 h75.6)]
    Background [godot(x1791.0 y71.2 w56.8 h58.1)]
    Icon [godot(x1791.0 y71.2 w56.8 h58.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Deck info Popup | ✅ `scripts\deck_collection.gd:617 "cards": parsed.get("cards", []),   # 完整卡列表 (Deck info Popup 用); scripts\deck_collection.gd:951 # 原` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Warlord Image | ✅ `scripts\deck_info_popup.gd:75 # 督军立绘 (原版 Warlord Image 1108x1108, pivot(0.5,0) 原始 JSON RectTransform_8411164374367242664:; scripts` |
| Deck Details | ✅ `scripts\deck_info_popup.gd:4 ## 布局: 大窗口(UI_Deck_Information_Back) + 督军立绘 + Deck Details(卡组名/阵营图标/督军名); scripts\deck_info_popup.gd:` |
| Game Mode Icon | ✅ `scripts\deck_collection.gd:791 # 5) 模式图标 (右下, 原版 Game Mode Icon [171,274 84x86]; 玩家自建卡组=经典模式; 网格 0.9 倍 → offsets(153.45,229.5)); s` |
| Game Mode Separator | ✅ `scripts\deck_info_popup.gd:115 # Game Mode Separator (原版 40k_Generic Smooth line 8.9x110 深红(0.42,0.16,0.14) @ x[659,667.9] y[162.3` |
| Deck Details | ✅ `scripts\deck_info_popup.gd:4 ## 布局: 大窗口(UI_Deck_Information_Back) + 督军立绘 + Deck Details(卡组名/阵营图标/督军名); scripts\deck_info_popup.gd:` |
| Deck Name | ✅ `scripts\deck_builder.gd:219 # ===== Sidebar [0,156 335x924] (原版: Window Options + Deck Name + 卡组列表 + Done/30-30) =====; scripts\de` |
| Army Icon | ✅ `scripts\campaign.gd:190 # 阵营图标 (原版 Army Icon); scripts\card_displayer.gd:489 # 阵营图标 (场景 Army Icon 80x85)` |
| Warlord Name | ✅ `scripts\deck_info_popup.gd:144 # 督军名可点 (原版 Warlord Name GO 挂 Button — 2026-08-21 审查补); scripts\draft.gd:696 # Cards in deck 视图: 列表` |
| Buttons | ✅ `scripts\battle.gd:2047 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Practice Deck | ✅ `scripts\deck_info_popup.gd:160 _btn("Practice Deck", 725.0, y0, 1049.7, y0 + 80.0, _on_practice); scripts\deck_info_popup.gd:553 #` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Edit Deck | ✅ `scripts\deck_builder.gd:2060 # 编辑模式: deck_info_popup 'Edit Deck' 写入 editing_deck.json (DeckStore) → 加载该卡组; scripts\deck_info_popup` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Select Deck | ✅ `scripts\deck_collection.gd:7 ## 网格参数 = 原版 Select Deck Tab GridLayoutGroup (cellSize 225×364.5, spacing 20, padding L10;; scripts\d` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Deck Options | ✅ `scripts\deck_info_popup.gd:5 ##       + 底部三键(Practice/Edit/Select) + Deck Options 圆钮 + 卡组内容列表; scripts\deck_info_popup.gd:164 # De` |
| Switch Deck Info Button | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Duplicate Button | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Share Button | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Share On Chat | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Delete Button | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Info Panel | ✅ `scripts\deck_info_popup.gd:242 # Info Panel 卡组内容列表 (原版绝对坐标 [659,218 1140x650] UI_Deck_Information_submenu_Back); scripts\deck_info` |
| Deck List | ✅ `scripts\deck_builder.gd:433 # 卡组列表 (原版 Deck List drawer [0,366 325x644] Scroll View; 存引用供视图切换显隐); scripts\mode_select.gd:458 # 卡组内` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Deck Selector Card Info button | ✅ `scripts\deck_builder.gd:1420 ## 原版卡行 (Deck Selector Card Info button, 86px 行高): PnP 卡面缩略+渐变条+费用图标+卡名+数量; scripts\deck_builder.gd:1` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Rarity Gradient | ✅ `scripts\deck_builder.gd:1477 # 稀有度渐变条 (原版 Rarity Gradient anchor(0.606,0,1,1) 右 40% 区域稀有度着色); scripts\deck_builder.gd:1651 # 稀有度渐变` |
| Background Border | ✅ `scripts\deck_builder.gd:1469 # 卡行边框 (原版 Background Border 40k_deck_cardlist_border 四边线); scripts\deck_builder.gd:1643 # 边框 (原版 Bac` |
| Cost Image | ✅ `scripts\deck_builder.gd:1492 # 费用图标 (原版 Cost Image: Card Frame Cost Icon 左竖条 + 数字 50px); scripts\deck_builder.gd:1676 # 费用图标 (原版 C` |
| Cost | ✅ `scripts\battle.gd:434 # 实时数值层 (原版 2DCard Card Info: Cost/Health/Melee/Armour 文字实时更新 —; scripts\battle.gd:437 ["Cost", Vector3(0.28` |
| banned Icon | ✅ `scripts\deck_info_popup.gd:416 # banned Icon (原版 40k_Combat_Icon_Cross 卡被禁时显示 X — 2026-08-21 审查补; 数据无禁用标记 → 常隐)` |
| Text fill | ⚠️ 未命中 |
| Card Name | ✅ `scripts\deck_builder.gd:1514 # 卡名 + 类型/稀有度 (锚定左 112 右 70, 原版 Card Name 34px); scripts\deck_builder.gd:1709 # 卡名 (原版 Card Name 34px` |
| Count | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Deck Info | ✅ `scripts\deck_builder.gd:460 # 费用曲线 (原版 Deck Information cost drawer [88.8,411 158.1x199.1]: 9 行 18.9 高,; scripts\deck_builder.gd:4` |
| Lore Text | ✅ `scripts\deck_info_popup.gd:691 # Lore Text (原版 x[1014,1458.2] y[667.3,807.7] 28px 白换行; m_IsActive=false 运行时按卡组 lore 激活 —` |
| Cardback | ✅ `scripts\battle.gd:424 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:102 b.tooltip_text = file.get` |
| Cardback Front | ⚠️ 未命中 |
| Deck Information Cost/balance text | ✅ `scripts\mode_select.gd:402 # 法力曲线 (原版 Deck Information Cost/balance text 'Card / Energy cost' 34号 @[1276,327] +` |
| Deck Information cost drawer | ✅ `scripts\deck_builder.gd:460 # 费用曲线 (原版 Deck Information cost drawer [88.8,411 158.1x199.1]: 9 行 18.9 高,; scripts\deck_builder.gd:4` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Deck CostQuanityt Row Drawer | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (1) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (2) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (3) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (4) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (5) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (6) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (7) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (8) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:146 # 关闭按钮 (原版 Generic Close Button Orange); scripts\deck_info_popup.gd:208 # 关闭按钮 (原版 Generic Close` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |

## 摘要

- 规格元素: 113
- 代码命中: 97
- ⚠️未命中: 16 (以下需人工判断)

- `Switch Deck Info Button`
- `Duplicate Button`
- `Share Button`
- `Share On Chat`
- `Delete Button`
- `Text fill`
- `Cardback Front`
- `Deck CostQuanityt Row Drawer`
- `Deck CostQuanityt Row Drawer (1)`
- `Deck CostQuanityt Row Drawer (2)`
- `Deck CostQuanityt Row Drawer (3)`
- `Deck CostQuanityt Row Drawer (4)`
- `Deck CostQuanityt Row Drawer (5)`
- `Deck CostQuanityt Row Drawer (6)`
- `Deck CostQuanityt Row Drawer (7)`
- `Deck CostQuanityt Row Drawer (8)`