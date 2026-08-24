# UI 规格审计: ChatPanel

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-24 19:56
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
ChatPanel [godot(x-78.1 y0.0 w1972.0 h1080.0)]
  Holder [godot(x-78.1 y-4.0 w1972.0 h1080.0)]
    CloseBackground [godot(x-2056.5 y-651.2 w5928.8 h2374.4)]
    Chat [godot(x563.9 y146.0 w1300.0 h930.0)]
      Tab Buttons [godot(x229.5 y182.8 w361.2 h823.8)]
        Orange Tab Toggle [inactive godot(x425.7 y182.8 w165.0 h157.7)]
          button_bg [godot(x425.7 y182.8 w165.0 h157.7)]
          Icon [godot(x425.7 y200.2 w160.0 h125.3)]
          Label [inactive godot(x430.7 y288.9 w155.0 h40.0)]
            Tab Toggle Title [txt=General godot(x430.7 y288.9 w155.0 h40.0)]
      ChatBackground [godot(x563.9 y146.0 w1300.0 h930.0)]
      Tabs [godot(x613.9 y161.0 w1200.0 h750.0)]
      Enter Text [godot(x613.9 y1026.0 w1200.0 h0.0)]
        Background [godot(x613.9 y1026.0 w1200.0 h0.0)]
        InputField (TMP) [godot(x653.9 y1059.3 w1120.0 h0.0)]
          Text Area [godot(x653.9 y1059.3 w1120.0 h0.0)]
            Placeholder [txt=Type message godot(x653.9 y1046.0 w1120.0 h26.5)]
            Text [txt=​ godot(x653.9 y1059.3 w1120.0 h0.0)]
        Button [godot(x1750.4 y1006.0 w40.0 h40.0)]
      Generic Close Button Orange [godot(x1799.3 y122.8 w74.4 h75.6)]
        Background [godot(x1807.4 y130.8 w56.9 h58.1)]
        Icon [godot(x1807.4 y130.8 w56.9 h58.1)]
      Player Options Panel [inactive godot(x176.6 y349.0 w387.3 h390.0)]
        Buttons [godot(x176.6 y399.0 w387.3 h328.0)]
          Add as a friend [godot(x191.6 y404.9 w357.3 h44.4)]
            Button Text [txt=Add as a friend godot(x204.3 y384.0 w330.7 h86.2)]
          Challenge [godot(x191.6 y446.4 w357.3 h44.4)]
            Button Text [txt=Challenge godot(x204.3 y425.5 w330.7 h86.1)]
          Report [godot(x191.6 y493.8 w357.3 h44.4)]
            Button Text [txt=Report message godot(x204.3 y472.8 w330.7 h86.2)]
          Block [godot(x191.6 y541.2 w357.3 h44.4)]
            Button Text [txt=Block player godot(x204.3 y520.2 w330.7 h86.2)]
          Profile [godot(x191.6 y588.6 w357.3 h44.3)]
            Button Text [txt=Profile godot(x204.3 y567.6 w330.7 h86.2)]
        Name [txt=Fulanito Name godot(x186.2 y349.0 w368.1 h50.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| ChatPanel | ✅ `scripts\main_menu.gd:771 # 聊天面板 (原版 ChatPanel 预制体: 1300x930 @ 屏幕 [616,1916]x[0,930]; 左 Tab 列 + 消息区 + 底部全宽输入); scripts\main_menu.gd` |
| Holder | ✅ `scripts\battle.gd:141 var _your_turn_img: TextureRect = null   # 玩家回合绿色提示 (原版 YourTurnImage 40k_DeckHolder_light_green); scripts\b` |
| CloseBackground | ⚠️ 未命中 |
| Chat | ✅ `scripts\battle.gd:2046 # 语音按钮 (原版 ChatButton 64×62 @ x[51,115] y[880,942] 贴图 40k_UI_bt_voicelines;; scripts\battle.gd:2444 # Mute ` |
| Tab Buttons | ✅ `scripts\collection.gd:150 # ---- Tab Buttons (原版 [167.2,158.6 165x921.4] 左竖排 4 tab — RectTransform_-1995773233925987627) ----; scr` |
| Orange Tab Toggle | ✅ `scripts\main_menu.gd:781 # 左侧 Tab 列 (原版 Orange Tab Toggle 165x157.7 图标 40K_icon_menu_chat 160x125.3 + 'General' 35px)` |
| button_bg | ✅ `scripts\draft_leaderboard_popup.gd:191 # button_bg (原版 40K_settings_button_hover 染橙 (1,0.43,0); 选中 alpha 1, 未选中 0.5); scripts\lead` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\ally_badge_drawe` |
| Label | ✅ `scripts\achievements.gd:248 font_size: int, color: Color) -> Label:; scripts\achievements.gd:249 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\draft_leaderboard_popup.gd:210 # Tab Toggle Title (原版 Label (5,106.1) 155x40 35px 白); scripts\leaderboard_popup.gd:7 ##   ` |
| ChatBackground | ⚠️ 未命中 |
| Tabs | ✅ `scripts\shop.gd:160 # 3 个标签页 (Tabs 区 x330-1920)` |
| Enter Text | ✅ `scripts\main_menu.gd:842 # 输入 + 发送 (原版 Enter Text 底部全宽: 'Type message' 28px + send 40k_UI_Chat_send 40x40)` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| InputField (TMP) | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖); scripts\gener` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:153 var bg := TextureRect.new(); scripts\achievements.gd:155 bg.expand_mode = TextureRect.EXPAND_IGNORE_SI` |
| Button | ✅ `scripts\ally_badge_drawer.gd:68 if ev is InputEventMouseButton and ev.pressed:; scripts\ally_badge_drawer.gd:116 var cell := Butto` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:197 # 关闭按钮 (原版 Generic Close Button Orange 三层; 权威 y181.3 — 修正仅 X 图标+159.8); scripts\deck_info_popup.` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\ally_badge_drawe` |
| Player Options Panel | ⚠️ 未命中 |
| Buttons | ✅ `scripts\battle.gd:2091 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Add as a friend | ✅ `scripts\member_options_panel.gd:15 ## 文字: UI 一律英文 (节点名: Challenge/Add as a friend/Profile/Promote/Demote/Kick/Quit/Debug Add Skull` |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Challenge | ✅ `scripts\main_menu.gd:23 const TOP_CHALLENGE := "res://assets/ui/mainmenu/scenes_sprites/40K_icon_duel.png"  # Challenge butt; scri` |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Report | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Block | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Profile | ✅ `scripts\draft_leaderboard_popup.gd:76 _make_tab(TAB_POS_1, MNU + "40K_Profile_icon_title.png", "Armies"); scripts\draft_leaderboar` |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Name | ✅ `scripts\ally_badge_drawer.gd:9 ##   Label [640,810 641x108] nametag 条 40k_main_bt_nametag: Quantity 75pt + Name 75pt; scripts\ally` |

## 摘要

- 规格元素: 35
- 代码命中: 29
- ⚠️未命中: 6 (以下需人工判断)

- `CloseBackground`
- `ChatBackground`
- `InputField (TMP)`
- `Player Options Panel`
- `Report`
- `Block`