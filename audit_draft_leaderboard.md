# UI 规格审计: DraftLeaderboardPopup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 17:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
DraftLeaderboardPopup [godot(x-0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Tab Buttons [godot(x38.6 y104.7 w172.0 h823.8)]
    Armies [godot(x-43.9 y849.6 w165.0 h157.7)]
      button_bg [godot(x-43.9 y849.6 w165.0 h157.7)]
      Icon [godot(x-43.9 y867.0 w160.0 h125.3)]
      Label [inactive godot(x-38.9 y955.7 w155.0 h40.0)]
        Tab Toggle Title [txt=General godot(x-38.9 y955.7 w155.0 h40.0)]
    Alliances [godot(x-43.9 y849.6 w165.0 h157.7)]
      button_bg [godot(x-43.9 y849.6 w165.0 h157.7)]
      Icon [godot(x-43.9 y867.0 w160.0 h125.3)]
      Label [inactive godot(x-38.9 y955.7 w155.0 h40.0)]
        Tab Toggle Title [txt=General godot(x-38.9 y955.7 w155.0 h40.0)]
  Ranking Display [godot(x202.4 y16.3 w1515.2 h990.6)]
    Generic Window Red Background Big [godot(x202.4 y16.3 w1515.2 h990.6)]
    Title [txt=TOP PLAYERS godot(x643.5 y37.0 w632.9 h109.5)]
    TopBar [godot(x282.9 y141.6 w1354.1 h6.0)]
    Content [godot(x249.0 y147.6 w1422.0 h790.2)]
      Army Selector [godot(x249.0 y937.8 w0.0 h0.0)]
        Separator Line [godot(x249.0 y995.1 w0.0 h6.0)]
        Viewport [godot(x249.0 y937.8 w0.0 h0.0)]
          Army Content [godot(x249.0 y872.8 w0.0 h130.0)]
      Scroll View [godot(x249.0 y937.8 w0.0 h0.0)]
        Viewport [godot(x249.0 y937.8 w0.0 h0.0)]
          Content [godot(x-351.0 y937.8 w1200.0 h0.0)]
            AllianceRankingRow Skulls Variant [godot(x-351.0 y887.8 w0.0 h100.0)]
              Background [godot(x-351.0 y884.6 w0.0 h106.5)]
              BackgroundHighlight [godot(x-351.0 y884.6 w0.0 h106.5)]
              BadgeDrawer [godot(x-225.1 y883.9 w110.8 h103.9)]
                Frame [godot(x-225.1 y883.9 w110.8 h103.9)]
                Badge [godot(x-225.1 y883.9 w110.8 h103.9)]
              Ranking [txt=1 godot(x-339.0 y901.9 w100.0 h71.9)]
              Name Holder [godot(x-61.0 y887.8 w733.9 h100.0)]
                Name [txt=Lorem Ipsum godot(x-416.4 y987.8 w710.8 h0.0)]
                Guild Name [inactive txt=Bando del Ventris godot(x-416.4 y987.8 w710.8 h0.0)]
              RankingIcon [godot(x-561.0 y893.6 w60.0 h91.8)]
              Points [txt=4500 godot(x-491.0 y899.1 w140.0 h78.0)]
            PlayerRankingRow [godot(x-351.0 y887.8 w0.0 h100.0)]
              Background [godot(x-351.0 y884.6 w0.0 h106.5)]
              BackgroundHighlight [godot(x-351.0 y884.6 w0.0 h106.5)]
              Ranking [txt=1 godot(x-339.0 y901.9 w100.0 h71.9)]
              border [godot(x-216.0 y888.8 w120.0 h106.5)]
                Icon [godot(x-269.8 y847.5 w204.6 h167.1)]
              Name Holder [godot(x-61.0 y887.8 w733.9 h100.0)]
                Name [txt=Lorem Ipsum godot(x-416.4 y987.8 w710.8 h0.0)]
                Guild Name [txt=Bando del Ventris godot(x-416.4 y987.8 w710.8 h0.0)]
              RankingIcon [godot(x-609.3 y856.7 w108.3 h165.7)]
              Points [txt=4500 godot(x-491.0 y899.1 w140.0 h78.0)]
    Highlight Mount Point [inactive godot(x254.9 y806.9 w1369.3 h100.0)]
    Generic Simplified UI Button_updated [godot(x264.7 y62.2 w245.0 h59.1)]
      Button Text [txt=Last season godot(x276.4 y68.0 w220.8 h47.5)]
    Last Season Text [txt=Last season godot(x1251.6 y51.4 w408.8 h80.6)]
    Timer [godot(x1257.0 y51.4 w398.0 h80.6)]
      Timer Icon [godot(x1229.0 y104.1 w55.9 h55.9)]
      Timer [txt=Ends in: 23d 5h\n godot(x1550.2 y40.3 w0.0 h102.9)]
  Generic Close Button Orange [godot(x1656.8 y9.2 w74.4 h75.6)]
    Background [godot(x1665.0 y17.2 w56.8 h58.1)]
    Icon [godot(x1665.0 y17.2 w56.8 h58.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| DraftLeaderboardPopup | ✅ `scripts\social.gd:84 # 2026-08-21 修正: 此前误抄 DraftLeaderboardPopup 的 x38.6 — 与主导航 (x0-164) 重叠盖住 PLAY 键` |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Tab Buttons | ✅ `scripts\collection.gd:150 # ---- Tab Buttons (原版 [167.2,158.6 165x921.4] 左竖排 4 tab — RectTransform_-1995773233925987627) ----; scr` |
| Armies | ✅ `scripts\choose_army.gd:3 ##   Title 'SELECT ARMY' [0,55 1920x110] + SubTitle [0,140] + Armies 横滚 [0,186 1920x762] +; scripts\choos` |
| button_bg | ✅ `scripts\player_profile.gd:1040 # 分类按钮选中高亮 (选中 alpha 1, 未选中 0.71 — 原版 button_bg color(1,0.57,0,0.71)); scripts\ranked.gd:737 bg.mod` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1886 #` |
| Label | ✅ `scripts\achievements.gd:248 font_size: int, color: Color) -> Label:; scripts\achievements.gd:249 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:180 # 文字 (原版 Tab T` |
| Alliances | ✅ `scripts\social.gd:2 ## 社交界面 (原版 Social Submenu Variant 说明书 [0,0 1920x1080]: Alliances 联盟 + Friends 好友双 Tab); scripts\social.gd:156` |
| button_bg | ✅ `scripts\player_profile.gd:1040 # 分类按钮选中高亮 (选中 alpha 1, 未选中 0.71 — 原版 button_bg color(1,0.57,0,0.71)); scripts\ranked.gd:737 bg.mod` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1886 #` |
| Label | ✅ `scripts\achievements.gd:248 font_size: int, color: Color) -> Label:; scripts\achievements.gd:249 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:180 # 文字 (原版 Tab T` |
| Ranking Display | ✅ `scripts\ranked.gd:758 # Ranking Display (说明书 [202,16 1515x991]: 红窗底 UI_Deck_Information_Back)` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| TopBar | ✅ `scripts\main_menu.gd:495 ##   TopBarButtons(HorizontalLayoutGroup spacing 9.75 MiddleLeft @x[425.3,736.7] y[-0.2,71.2]):; scripts\` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_collectio` |
| Army Selector | ✅ `scripts\battle.gd:181 # 原版 battlearena1 场景树无阵营选择弹窗 (Army Selector 在模式选择界面) —; scripts\campaign.gd:126 # Campaign Army Selector (原版` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:279 # 物品池 (原版 Re` |
| Army Content | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:279 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_collectio` |
| AllianceRankingRow Skulls Variant | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| BackgroundHighlight | ⚠️ 未命中 |
| BadgeDrawer | ✅ `scripts\social.gd:171 # 徽章 (BadgeDrawer 251x235; 原版 AllianceBadge 定义数据 → 22 张 Alliance_Trophies_*, 2026-08-23 接入)` |
| Frame | ✅ `scripts\battle.gd:80 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:81 co` |
| Badge | ✅ `scripts\campaign.gd:398 ## Unlock [772,850 245x45]×2 + Badge [1025,295 100x100] + 'Click to continue' [576,965 768x80]); scripts\c` |
| Ranking | ✅ `scripts\player_profile.gd:37 const TEX_ADMIRAL := "res://assets/ui/ranked/04-Admiral.png"        # Ranking 中央段位图; scripts\player_p` |
| Name Holder | ⚠️ 未命中 |
| Name | ✅ `scripts\battle.gd:57 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
| Guild Name | ⚠️ 未命中 |
| RankingIcon | ⚠️ 未命中 |
| Points | ✅ `scripts\battle.gd:1797 # 敌方 QP 任务点 (原版 GO726 x[1816.1,1913.8] y[150.2,247.9] UI_Quest_Points + '0/3' 40.5px — 2026-08-21 审查; scrip` |
| PlayerRankingRow | ✅ `scripts\ranked.gd:846 # 排行列表 (原版 Content x[249,1671] y[147.6,937.8] 1422×790.2, PlayerRankingRow 行高 100 间距 15); scripts\ranked.gd:` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| BackgroundHighlight | ⚠️ 未命中 |
| Ranking | ✅ `scripts\player_profile.gd:37 const TEX_ADMIRAL := "res://assets/ui/ranked/04-Admiral.png"        # Ranking 中央段位图; scripts\player_p` |
| border | ✅ `scripts\battle.gd:1243 sb.set_border_width_all(4); scripts\battle.gd:1244 sb.border_color = Color("e8c76a")` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1886 #` |
| Name Holder | ⚠️ 未命中 |
| Name | ✅ `scripts\battle.gd:57 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
| Guild Name | ⚠️ 未命中 |
| RankingIcon | ⚠️ 未命中 |
| Points | ✅ `scripts\battle.gd:1797 # 敌方 QP 任务点 (原版 GO726 x[1816.1,1913.8] y[150.2,247.9] UI_Quest_Points + '0/3' 40.5px — 2026-08-21 审查; scrip` |
| Highlight Mount Point | ⚠️ 未命中 |
| Generic Simplified UI Button_updated | ✅ `scripts\draft.gd:991 bg.texture = load(TEX_BTN_YELLOW)   # 原版 Generic Simplified UI Button_updated 系=UI_Button_Mulligan 黄` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Last Season Text | ✅ `scripts\ranked.gd:808 # Last Season 静态文本 (原版 Last Season Text x[1251.6,1660.4] y[51.4,132] 409×81 fontsize 40 白;` |
| Timer | ✅ `scripts\battle.gd:4622 var _clock_timer: Timer = null; scripts\battle.gd:4641 _clock_timer = Timer.new()` |
| Timer Icon | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4622 var _clock_timer: Timer = null; scripts\battle.gd:4641 _clock_timer = Timer.new()` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:197 # 关闭按钮 (原版 Generic Close Button Orange 三层; 权威 y181.3 — 修正仅 X 图标+159.8); scripts\deck_info_popup.` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1886 #` |

## 摘要

- 规格元素: 58
- 代码命中: 46
- ⚠️未命中: 12 (以下需人工判断)

- `Army Content`
- `AllianceRankingRow Skulls Variant`
- `BackgroundHighlight`
- `Name Holder`
- `Guild Name`
- `RankingIcon`
- `BackgroundHighlight`
- `Name Holder`
- `Guild Name`
- `RankingIcon`
- `Highlight Mount Point`
- `Timer Icon`