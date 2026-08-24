# UI 规格审计: Deck Selection Popup with Tabs

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-24 19:57
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Deck Selection Popup with Tabs [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Alliance Header Buttons [godot(x167.5 y35.1 w1589.0 h72.1)]
    Tab buttons [godot(x196.3 y35.1 w1057.3 h68.5)]
      Generic Tab UI Button [godot(x66.3 y69.7 w260.0 h67.7)]
        Button Text [godot(x89.8 y74.4 w213.0 h67.7)]
      Generic Tab UI Button 1 [godot(x66.3 y69.7 w260.0 h67.7)]
        Button Text [godot(x89.8 y74.4 w213.0 h67.7)]
  Generic Window Red Background Big [godot(x134.5 y82.0 w1705.0 h950.0)]
  Deck Display [godot(x144.5 y124.9 w1665.0 h848.3)]
    Collection Display [godot(x144.5 y208.6 w1665.0 h764.6)]
      Deck Scroll View [godot(x194.5 y208.6 w1565.0 h778.1)]
        Viewport [godot(x194.5 y208.6 w1565.0 h778.1)]
          Content [godot(x194.5 y208.6 w1565.0 h200.0)]
        Empty Collection Warning [inactive godot(x194.5 y208.6 w1565.0 h778.1)]
          Warning [txt=There are no deck in your collection for godot(x194.5 y208.6 w1565.0 h778.1)]
    Header [godot(x184.5 y124.9 w1585.0 h85.0)]
      Separator Line [godot(x184.5 y204.9 w1585.0 h10.0)]
      Instructions [inactive txt=Select deck godot(x618.7 y124.9 w716.6 h85.0)]
      Instructions 2 [godot(x1236.1 y124.9 w534.1 h85.0)]
      Practice buttons [godot(x184.5 y117.5 w259.1 h99.9)]
        Generic Simplified UI Button [godot(x78.4 y185.4 w212.2 h64.0)]
          Button Text [godot(x89.6 y191.7 w189.8 h51.4)]
      Filter Buttons [inactive godot(x442.9 y127.4 w253.6 h80.0)]
        Generic Round Button Variant [godot(x455.2 y137.4 w60.0 h60.0)]
          Button Text [inactive txt=X godot(x463.2 y137.4 w44.0 h60.0)]
          Image [godot(x465.0 y147.3 w40.3 h40.3)]
        Generic Round Button Variant (1) [godot(x539.7 y137.4 w60.0 h60.0)]
          Button Text [inactive txt=X godot(x547.7 y137.4 w44.0 h60.0)]
          Image [godot(x549.6 y151.2 w40.2 h40.3)]
          Image (1) [godot(x549.6 y138.1 w40.2 h40.3)]
        Generic Round Button Variant (2) [godot(x624.3 y137.4 w60.0 h60.0)]
          Button Text [inactive txt=X godot(x632.3 y137.4 w44.0 h60.0)]
          Image [godot(x638.2 y157.1 w32.2 h36.3)]
          Image (1) [godot(x638.2 y146.3 w32.2 h36.3)]
          Image (2) [godot(x638.2 y136.3 w32.2 h36.3)]
      Collection Menu Input Field [inactive godot(x727.0 y142.9 w500.0 h49.1)]
        Text Area [godot(x737.0 y149.9 w450.0 h36.1)]
          Placeholder [txt=Search godot(x737.0 y149.9 w450.0 h36.1)]
          Text [txt=​ godot(x737.0 y149.9 w450.0 h36.1)]
        Image [godot(x1187.0 y147.9 w35.0 h39.1)]
  Generic Close Button Orange [godot(x1783.1 y62.9 w74.4 h75.6)]
    Background [godot(x1791.3 y70.9 w56.8 h58.1)]
    Icon [godot(x1791.3 y70.9 w56.8 h58.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Deck Selection Popup with Tabs | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\ally_badge_drawer.gd:65 # 遮罩: 纯黑 ` |
| Alliance Header Buttons | ✅ `scripts\social.gd:325 # 头部 Tab 键 (原版 AllianceMemberVariant > Alliance Header Buttons (1) [331,117 1589x72]:` |
| Tab buttons | ⚠️ 未命中 |
| Generic Tab UI Button | ✅ `scripts\social.gd:24 const TEX_TAB_BTN := SPR + "40K_tab_button_overwindow.png"          # Generic Tab UI Button; scripts\social.g` |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Generic Tab UI Button 1 | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Deck Display | ⚠️ 未命中 |
| Collection Display | ⚠️ 未命中 |
| Deck Scroll View | ✅ `scripts\deck_collection.gd:173 # ---- 网格 (原版 Select Deck Tab Deck Scroll View [330.9,155.9 1589.1x924.1] 直达右缘 — RectTransform_6413` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:279 # 物品池 (原版 Re` |
| Content | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\card_displayer.gd:447 # 内容组 (原版 UpgradePanel.content; 满级切 No Upgrade Warning); scripts\card_displayer.gd:503 # 满级警告层 (原版 N` |
| Header | ✅ `scripts\battle.gd:1483 # 名字 (原版 Header Text); scripts\campaign.gd:3 ## 原版 Campaign Tab (330.7,70.9) 1589.3×1009.1: 左上 Header(WF_Ca` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Instructions | ✅ `scripts\deck_builder.gd:216 # 注: 原版 label 'Edit your deck' / Instructions m_IsActive=false 默认隐藏 (2026-08-21 专项审查` |
| Instructions 2 | ⚠️ 未命中 |
| Practice buttons | ⚠️ 未命中 |
| Generic Simplified UI Button | ✅ `scripts\daily_streak_popup.gd:173 # Reset Streak 按钮 [728,657 465x103] (原版 Generic Simplified UI Button = UI_Button_Mulligan 黄钮, 55` |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Filter Buttons | ⚠️ 未命中 |
| Generic Round Button Variant | ✅ `scripts\daily_reward_popup.gd:66 # 关闭按钮 (原版 Generic Round Button Variant 124x124: 40k_UI_bt_back + 'X' 30pt 白 +` |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Generic Round Button Variant (1) | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Image (1) | ⚠️ 未命中 |
| Generic Round Button Variant (2) | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Image (1) | ⚠️ 未命中 |
| Image (2) | ⚠️ 未命中 |
| Collection Menu Input Field | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖); scripts\gener` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:153 var bg := TextureRect.new(); scripts\achievements.gd:155 bg.expand_mode = TextureRect.EXPAND_IGNORE_SI` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:197 # 关闭按钮 (原版 Generic Close Button Orange 三层; 权威 y181.3 — 修正仅 X 图标+159.8); scripts\deck_info_popup.` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\ally_badge_drawe` |

## 摘要

- 规格元素: 44
- 代码命中: 30
- ⚠️未命中: 14 (以下需人工判断)

- `Deck Selection Popup with Tabs`
- `Tab buttons`
- `Generic Tab UI Button 1`
- `Deck Display`
- `Collection Display`
- `Instructions 2`
- `Practice buttons`
- `Filter Buttons`
- `Generic Round Button Variant (1)`
- `Image (1)`
- `Generic Round Button Variant (2)`
- `Image (1)`
- `Image (2)`
- `Collection Menu Input Field`