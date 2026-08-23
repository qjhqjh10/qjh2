# UI 规格审计: Practice Mode Menu

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:49
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Practice Mode Menu [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Back button [godot(x215.8 y892.9 w64.2 h63.2)]
    Icon [godot(x224.2 y901.2 w47.4 h46.6)]
    Text [txt=Back godot(x289.1 y892.9 w305.3 h63.2)]
  DeckSelectionContinueButton [godot(x1062.9 y906.3 w832.9 h49.8)]
    Continue Button [godot(x1384.9 y906.3 w453.1 h49.8)]
    Text [txt=Battle! godot(x1385.1 y911.2 w287.3 h44.9)]
    CircleButton [godot(x1678.7 y886.2 w90.0 h90.0)]
    GameModeText [inactive txt=Game mode: Multiplayer godot(x1225.0 y968.2 w444.9 h50.0)]
  Deck Selector [godot(x77.1 y165.3 w533.8 h692.9)]
    Deck Buttons [godot(x242.9 y146.8 w432.6 h711.4)]
      Generic Window Red Background Small [godot(x242.9 y208.8 w415.1 h652.5)]
      tooltip [txt=Select deck to play godot(x283.8 y170.8 w333.4 h38.0)]
      Selected Army Title [txt=ULTRAMARINES godot(x279.0 y223.0 w342.9 h49.0)]
      Decks Scroll view [godot(x261.3 y262.6 w373.6 h540.8)]
        Viewport [godot(x261.3 y262.6 w373.6 h540.8)]
          Content [godot(x262.1 y262.6 w372.0 h0.0)]
    Army Selector [godot(x69.4 y182.2 w177.1 h698.0)]
      Background [godot(x69.4 y182.2 w177.1 h698.0)]
      Viewport [godot(x69.4 y149.1 w177.1 h764.2)]
        Filters [godot(x69.4 y149.1 w177.1 h764.2)]
  Deck info [godot(x638.4 y78.8 w1204.0 h785.0)]
    Generic Window Red Background Big [godot(x761.6 y187.0 w1070.3 h682.0)]
    Character Image [godot(x586.9 y-9.7 w905.0 h905.0)]
    Background Info [inactive godot(x1258.1 y316.0 w531.0 h484.4)]
    Warlord Name [txt=Warlord name godot(x1373.8 y269.6 w0.0 h34.0)]
    Deck Name [txt=DECK NAME godot(x1371.6 y224.1 w355.0 h47.7)]
    Army Image [godot(x1258.9 y210.1 w105.2 h104.0)]
    General container [godot(x1240.4 y207.6 w569.8 h619.6)]
      Lore Text [txt=Start here! Overwhelm your opponent with godot(x1280.3 y647.4 w490.0 h144.0)]
      Cardback [godot(x1542.4 y329.6 w209.5 h302.4)]
        Cardback Front [godot(x1553.6 y324.7 w209.5 h302.4)]
      Deck Information Cost/balance text [txt=Card / Energy cost godot(x1276.3 y327.0 w264.0 h54.3)]
      Deck Information cost drawer [godot(x1313.4 y385.3 w189.8 h238.9)]
        Background [godot(x1313.4 y385.3 w189.8 h238.9)]
        Content [godot(x1274.1 y385.3 w268.3 h238.9)]
          Deck CostQuanityt Row Drawer [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
          Deck CostQuanityt Row Drawer (1) [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
          Deck CostQuanityt Row Drawer (2) [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
          Deck CostQuanityt Row Drawer (3) [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
          Deck CostQuanityt Row Drawer (4) [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
          Deck CostQuanityt Row Drawer (5) [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
          Deck CostQuanityt Row Drawer (6) [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
          Deck CostQuanityt Row Drawer (7) [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
          Deck CostQuanityt Row Drawer (8) [godot(x1140.0 y612.8 w268.3 h22.7)]
            Card Cost [txt=0 godot(x1144.0 y612.2 w30.7 h23.9)]
            Cards in deck [txt=0 godot(x1373.1 y612.2 w30.6 h24.0)]
            Slider [godot(x1183.3 y612.2 w181.6 h24.0)]
              Background [godot(x1183.3 y614.5 w181.6 h19.9)]
              Fill [godot(x1183.3 y639.0 w0.0 h-5.7)]
      Show Deck Content Button [godot(x1729.3 y238.2 w64.2 h63.2)]
        Icon [godot(x1737.7 y246.5 w47.4 h46.6)]
      Generic Simplified UI Button [godot(x1398.0 y680.8 w254.5 h83.3)]
        Button Text [txt=Change Deck godot(x1406.9 y688.9 w236.7 h67.0)]
    Deck List Drawer [godot(x1240.4 y207.6 w569.8 h619.6)]
      Content [godot(x1261.3 y318.4 w526.1 h475.5)]
        Deck Selector Card Info button_ref [godot(x1261.3 y793.9 w0.0 h0.0)]
          Content [godot(x1261.3 y793.9 w0.0 h0.0)]
            Background [godot(x1261.3 y793.9 w0.0 h0.0)]
              Rarity Gradient [godot(x1260.8 y793.9 w0.5 h-0.1)]
              Background Border [godot(x1244.9 y793.9 w16.4 h0.0)]
              Cost Image [godot(x1261.1 y790.9 w0.0 h6.0)]
                Cost [txt=5 godot(x1236.7 y791.5 w48.8 h4.7)]
              banned Icon [godot(x1258.2 y787.8 w0.0 h6.0)]
              Text fill [godot(x1261.3 y793.9 w-5.0 h0.0)]
                Card Name [txt=Card Name godot(x1261.3 y793.9 w0.0 h0.0)]
                Count [txt=x2 godot(x1261.3 y793.9 w0.0 h0.0)]
      Show Deck General Info button [godot(x1729.3 y238.2 w64.2 h63.2)]
        Icon [godot(x1737.7 y246.5 w47.4 h46.6)]
  Searching Oponent Popup [inactive godot(x0.5 y0.5 w1919.0 h1079.0)]
    Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
    Window [godot(x560.0 y234.1 w800.0 h451.8)]
      Generic Popup Background [godot(x560.0 y234.1 w800.0 h451.8)]
        Mask [godot(x570.4 y243.5 w779.7 h432.6)]
          Background fill [sprite=40k_popup_texture godot(x570.4 y243.5 w779.7 h432.6)]
      Skull [godot(x668.3 y176.3 w567.4 h567.4)]
        Cog [godot(x668.3 y176.2 w567.4 h567.6)]
      Main Search message [txt=Searching godot(x610.0 y293.1 w700.0 h148.2)]
      Buttons [godot(x593.0 y562.4 w734.0 h90.0)]
        Generic UI Button [godot(x720.8 y569.9 w478.4 h75.0)]
          Button Text [txt=Cancel godot(x733.5 y561.2 w452.4 h91.2)]
      Few players online message [txt=If no opponent is found in a few seconds godot(x593.0 y460.0 w734.0 h100.0)]
  Toggle [godot(x813.2 y906.3 w293.6 h57.8)]
    Background [godot(x915.5 y915.2 w89.0 h40.0)]
    Skirmish toggle Image [godot(x813.2 y887.9 w94.7 h94.6)]
    Classic toggle Image [godot(x1012.1 y887.9 w94.7 h94.6)]
    Label Background [godot(x799.9 y853.2 w320.2 h40.0)]
      Label [txt=Game mode godot(x854.7 y853.2 w210.6 h40.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Practice Mode Menu | ✅ `scripts\mode_select.gd:2 ## 模式选择界面 (P2.5 原版 UI): 按 Practice Mode Menu 说明书 (菜单全树.md) 重建; scripts\mode_select.gd:184 ## 卡组列表 (原版 Pra` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Back button | ✅ `scripts\mode_select.gd:676 # Back (原版 Back button [216,893 64x63]: 圆钮底 UI_Button_Round_background + Icon 40k_UI_bt_back, 文字 'Ba` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| DeckSelectionContinueButton | ⚠️ 未命中 |
| Continue Button | ⚠️ 未命中 |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| CircleButton | ✅ `scripts\mode_select.gd:708 # 右侧 CircleButton [1679,886 90x90] 40k_UI_bt_play — 2026-08-21 审查修正染色/字号); scripts\mode_select.gd:723 #` |
| GameModeText | ✅ `scripts\mode_select.gd:830 # GameModeText 模式文字 (原版 [1225,968 445x50] 'Game mode: Multiplayer'; 我们显示 Classic/Skirmish); scripts\mod` |
| Deck Selector | ✅ `scripts\deck_builder.gd:1420 ## 原版卡行 (Deck Selector Card Info button, 86px 行高): PnP 卡面缩略+渐变条+费用图标+卡名+数量; scripts\deck_builder.gd:1` |
| Deck Buttons | ✅ `scripts\ranked.gd:226 # 4 圆钮 (原版 Deck Buttons [641,816 624x218]: Previous/Change/View/Next 161x128)` |
| Generic Window Red Background Small | ⚠️ 未命中 |
| tooltip | ✅ `scripts\battle.gd:1122 b.tooltip_text = "%s (cost %d)" % [card.get("name", "?"), RuleCore._to_int(card.get("cost"))]; scripts\batt` |
| Selected Army Title | ✅ `scripts\mode_select.gd:189 # Selected Army Title (原版 [279,223 343x49] 当前阵营标题, 选中卡组时更新); scripts\mode_select.gd:190 _army_title_lb ` |
| Decks Scroll view | ⚠️ 未命中 |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Army Selector | ✅ `scripts\battle.gd:171 # 原版 battlearena1 场景树无阵营选择弹窗 (Army Selector 在模式选择界面) —; scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Deck info | ✅ `scripts\deck_builder.gd:21 var _window_opts: Dictionary = {}  # 原版 Sidebar Window Options 3 键 (Cards/Deck info/Cosmetics); scripts` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Character Image | ✅ `scripts\mode_select.gd:381 # 督军立绘区 (场景 Character Image 587,-10 905x905)` |
| Background Info | ✅ `scripts\mode_select.gd:376 # 副面板底 (原版 Background Info UI_Deck_Information_submenu_Back active (1258.1,316)-(1789.1,800.4)` |
| Warlord Name | ✅ `scripts\deck_info_popup.gd:148 # 督军名可点 (原版 Warlord Name GO 挂 Button — 2026-08-21 审查补); scripts\draft.gd:696 # Cards in deck 视图: 列表` |
| Deck Name | ✅ `scripts\deck_builder.gd:219 # ===== Sidebar [0,156 335x924] (原版: Window Options + Deck Name + 卡组列表 + Done/30-30) =====; scripts\de` |
| Army Image | ✅ `scripts\mode_select.gd:392 # 阵营图标 (场景 Army Image 1259,210 105x104); scripts\mode_select.gd:887 # 阵营图标 (原版 Army Image, 文件名 40k_Deck` |
| General container | ⚠️ 未命中 |
| Lore Text | ✅ `scripts\deck_info_popup.gd:703 # Lore Text (原版 x[1014,1458.2] y[667.3,807.7] 28px 白换行; m_IsActive=false 运行时按卡组 lore 激活 —` |
| Cardback | ✅ `scripts\battle.gd:425 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:102 b.tooltip_text = file.get` |
| Cardback Front | ⚠️ 未命中 |
| Deck Information Cost/balance text | ✅ `scripts\mode_select.gd:402 # 法力曲线 (原版 Deck Information Cost/balance text 'Card / Energy cost' 34号 @[1276,327] +` |
| Deck Information cost drawer | ✅ `scripts\deck_builder.gd:460 # 费用曲线 (原版 Deck Information cost drawer [88.8,411 158.1x199.1]: 9 行 18.9 高,; scripts\deck_builder.gd:4` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Deck CostQuanityt Row Drawer | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (1) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (2) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (3) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (4) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (5) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (6) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (7) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (8) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Show Deck Content Button | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Generic Simplified UI Button | ✅ `scripts\two_sides_event.gd:386 # Collect 按钮 (原版 Generic Simplified UI Button)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Deck List Drawer | ✅ `scripts\mode_select.gd:458 # 卡组内容抽屉 (原版 Deck List Drawer [1240,208 570x620], 默认隐藏)` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Deck Selector Card Info button_ref | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Rarity Gradient | ✅ `scripts\deck_builder.gd:1481 # 稀有度渐变条 (原版 Rarity Gradient anchor(0.606,0,1,1) 右 40% 区域稀有度着色); scripts\deck_builder.gd:1657 # 稀有度渐变` |
| Background Border | ✅ `scripts\deck_builder.gd:1471 # 卡行边框 (原版 Background Border 40k_deck_cardlist_border 11x11 m_Border=(5,5,5,5) 四边线 9-slice); scripts\` |
| Cost Image | ✅ `scripts\deck_builder.gd:1496 # 费用图标 (原版 Cost Image: Card Frame Cost Icon 左竖条 + 数字 50px); scripts\deck_builder.gd:1684 # 费用图标 (原版 C` |
| Cost | ✅ `scripts\battle.gd:435 # 实时数值层 (原版 2DCard Card Info: Cost/Health/Melee/Armour 文字实时更新 —; scripts\battle.gd:438 ["Cost", Vector3(0.28` |
| banned Icon | ✅ `scripts\deck_info_popup.gd:473 # banned Icon: 原版卡行模板 banned Icon [343,514 0x62] (行内 x+23/y-6, 62 高挂出贴底,; scripts\deck_info_popup.g` |
| Text fill | ⚠️ 未命中 |
| Card Name | ✅ `scripts\deck_builder.gd:1518 # 卡名 + 类型/稀有度 (锚定左 112 右 70, 原版 Card Name 34px); scripts\deck_builder.gd:1717 # 卡名 (原版 Card Name 34px` |
| Count | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Show Deck General Info button | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Searching Oponent Popup | ✅ `scripts\mode_select.gd:1109 # 搜索对手弹窗 (原版 Searching Oponent Popup: 40k_popup 窗 (560,286)-(1360,738) 800x452 +; scripts\mode_select.` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Window | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ⚠️ 未命中 |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Cog | ✅ `scripts\loading.gd:4 ## (40K_icon_searching_skull) + Cog 270x270 (40K_icon_searching_cog) 同心覆盖旋转; scripts\loading.gd:30 # 齿轮 (原版 C` |
| Main Search message | ✅ `scripts\import_deck_popup.gd:60 # 标题 (原版 Main Search message 'Paste your deck' 50px, 弹窗内 y[46,106] 居中)` |
| Buttons | ✅ `scripts\battle.gd:2048 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Few players online message | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Skirmish toggle Image | ⚠️ 未命中 |
| Classic toggle Image | ⚠️ 未命中 |
| Label Background | ⚠️ 未命中 |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |

## 摘要

- 规格元素: 129
- 代码命中: 105
- ⚠️未命中: 24 (以下需人工判断)

- `DeckSelectionContinueButton`
- `Continue Button`
- `Generic Window Red Background Small`
- `Decks Scroll view`
- `General container`
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
- `Show Deck Content Button`
- `Deck Selector Card Info button_ref`
- `Text fill`
- `Show Deck General Info button`
- `Background fill`
- `Few players online message`
- `Skirmish toggle Image`
- `Classic toggle Image`
- `Label Background`