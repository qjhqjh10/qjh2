# UI 规格审计: Inbox Menu

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Inbox Menu [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Content [godot(x72.1 y40.0 w1775.8 h1040.0)]
    Generic Window Red Background Big [godot(x76.1 y36.8 w1780.8 h1031.2)]
    Title [txt=Inbox godot(x121.5 y115.0 w250.0 h60.0)]
    Message List [godot(x99.6 y212.0 w628.7 h778.8)]
      Viewport [godot(x99.6 y212.0 w628.7 h778.8)]
        Content [godot(x99.6 y212.0 w628.7 h0.0)]
    Message Display [godot(x735.8 y93.9 w1059.8 h896.9)]
      Title [txt=WELCOME TO WARPFORGE CLOSED ALPHA! godot(x791.0 y132.1 w959.8 h60.5)]
      Content [godot(x785.8 y214.9 w989.8 h775.9)]
        Scroll View [godot(x785.8 y214.9 w989.8 h775.9)]
          Viewport [godot(x785.8 y990.8 w0.0 h0.0)]
            Content [godot(x785.8 y990.8 w1.6 h0.0)]
              Header [godot(x299.4 y869.2 w972.8 h243.2)]
              Message [txt=Lorem ipsum dolor sit amet, consectetur  godot(x785.8 y990.8 w974.3 h0.0)]
              Claim Button [godot(x306.4 y882.7 w958.8 h216.2)]
                Claim reward warning [txt=You will be able to claim your purchase  godot(x306.4 y985.8 w958.8 h0.0)]
                Claim Button [godot(x663.3 y910.3 w245.0 h67.6)]
                  Button Text [txt=Claim godot(x675.0 y916.9 w220.8 h54.4)]
              Footer [godot(x299.4 y869.2 w972.8 h243.2)]
          Scrollbar Vertical [godot(x1755.6 y214.9 w20.0 h758.9)]
            Sliding Area [godot(x1765.6 y224.9 w0.0 h738.9)]
              Handle [godot(x1755.6 y953.8 w20.0 h20.0)]
    Generic Close Button Orange [godot(x1785.5 y33.0 w74.4 h75.6)]
      Background [godot(x1793.7 y41.0 w56.9 h58.1)]
      Icon [godot(x1793.7 y41.0 w56.9 h58.1)]
    Reset Button [godot(x399.1 y125.6 w141.9 h70.8)]
      Button Text [txt=DEBUG RESET godot(x407.1 y132.5 w125.4 h57.0)]
    No News Warning [txt=Game announcements will be displayed her godot(x249.7 y520.0 w1420.6 h80.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Inbox Menu | ✅ `scripts\inbox.gd:2 ## 收件箱界面 (原版 Inbox Menu 说明书 15716 行: 大窗 1781x1031 + Title 'Inbox' +; scripts\main_menu.gd:929 ## 收件箱按钮: 打开收件箱界面` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Message List | ✅ `scripts\inbox.gd:3 ## Message List [100,212 629x779] 左侧消息列表 + Message Display [736,94 1060x897] 右侧详情; scripts\inbox.gd:62 # 左侧消息列表` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Message Display | ✅ `scripts\inbox.gd:3 ## Message List [100,212 629x779] 左侧消息列表 + Message Display [736,94 1060x897] 右侧详情; scripts\inbox.gd:77 # 右侧详情 (` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Message | ✅ `scripts\choose_name.gd:61 # 提示 (原版 MessageText "Choose your player name"); scripts\inbox.gd:3 ## Message List [100,212 629x779] 左侧` |
| Claim Button | ⚠️ 未命中 |
| Claim reward warning | ⚠️ 未命中 |
| Claim Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Footer | ✅ `scripts\deck_builder.gd:464 # 底部 Footer (原版 [0,1010 335x70]: Done [12.8..201.3, 9.3..59.5] 188.5x50.2 + 卡数图标 [201.3..251.3] 50x4; ` |
| Scrollbar Vertical | ⚠️ 未命中 |
| Sliding Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:146 # 关闭按钮 (原版 Generic Close Button Orange); scripts\deck_info_popup.gd:212 # 关闭按钮 (原版 Generic Close` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Reset Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| No News Warning | ⚠️ 未命中 |

## 摘要

- 规格元素: 30
- 代码命中: 23
- ⚠️未命中: 7 (以下需人工判断)

- `Claim Button`
- `Claim reward warning`
- `Claim Button`
- `Scrollbar Vertical`
- `Sliding Area`
- `Reset Button`
- `No News Warning`