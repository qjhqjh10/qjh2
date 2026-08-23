# UI 规格审计: Tutorial Mode Menu

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Tutorial Mode Menu [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Generic Window Red Background Big [godot(x-601.3 y105.8 w3122.6 h922.5)]
  Header With Back Button [godot(x0.0 y40.9 w550.0 h109.5)]
    Header Background [godot(x0.0 y40.9 w0.0 h115.3)]
      Window Title [txt=Game mode godot(x155.0 y57.2 w275.1 h82.7)]
    Header Background (1) [godot(x-462.1 y40.9 w550.0 h115.3)]
    Header Back Button [godot(x-24.4 y42.9 w167.9 h111.3)]
  Warlod Image [godot(x410.9 y-9.1 w1098.2 h1098.2)]
    Warlord Darkening [godot(x490.0 y627.9 w940.0 h319.9)]
  PlayTutorialButton [godot(x1387.8 y902.7 w440.4 h120.6)]
    Button Text [txt=Play Tutorial godot(x1403.3 y914.5 w408.8 h96.9)]
  TutorialInfo [godot(x1344.3 y244.9 w521.9 h586.2)]
    TutorialTitle [txt=TUTORIAL 01 godot(x1344.2 y265.0 w503.0 h105.7)]
    TutorialSubTitle [txt=The Basics godot(x1343.7 y392.2 w504.1 h0.0)]
    TutorialWarlordTitle [txt=Warlord: <color=orange>Uriel Ventris</co godot(x1344.2 y475.9 w503.0 h77.0)]
    TutorialDescription [txt=Start here! Spar with your Chapter Maste godot(x1344.3 y576.5 w521.9 h254.6)]
  Army Selector [godot(x60.0 y244.9 w589.7 h657.8)]
    Viewport [godot(x60.0 y244.9 w589.7 h657.8)]
      Filters [godot(x60.0 y244.9 w589.7 h657.8)]
  Completed Text [txt=Completed: 1/6 godot(x-0.0 y215.3 w658.3 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Tutorial Mode Menu | ✅ `scripts\main_menu.gd:968 # 教程模式 (原版 Tutorial Mode Menu, 重做计划步骤 12 最小版: 6 关选择→引导对局); scripts\tutorial.gd:2 ## 教程模式选择界面 (原版 Tutorial` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Header With Back Button | ✅ `scripts\daily_streak_popup.gd:5 ##   Header With Back Button: 'Daily Streak' + Back; scripts\daily_streak_popup.gd:94 # Header Wit` |
| Header Background | ⚠️ 未命中 |
| Window Title | ✅ `scripts\tutorial.gd:4 ## Window Title 'Game mode' + Back) + Warlod Image [411,-9 1098x1098] (督军立绘+Darkening) +` |
| Header Background (1) | ⚠️ 未命中 |
| Header Back Button | ✅ `scripts\tutorial.gd:64 # 返回按钮 (原版 Header Back Button 168x111)` |
| Warlod Image | ✅ `scripts\ranked.gd:192 # 督军立绘 (原版 Warlod Image [451,-95 1098x1098] 裁切显示; 无卡组时隐藏); scripts\tutorial.gd:4 ## Window Title 'Game mode'` |
| Warlord Darkening | ✅ `scripts\tutorial.gd:94 # 立绘暗化 (原版 Warlord Darkening 940x320 @(490,628))` |
| PlayTutorialButton | ✅ `scripts\tutorial.gd:6 ## PlayTutorialButton [1388,903] 440x121 + Army Selector [60,245 590x658] (6 关列表) +; scripts\tutorial.gd:153` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| TutorialInfo | ✅ `scripts\tutorial.gd:5 ## TutorialInfo [1344,245 522x586] (TUTORIAL 01 / The Basics / Warlord / 描述) +; scripts\tutorial.gd:25 # Tut` |
| TutorialTitle | ⚠️ 未命中 |
| TutorialSubTitle | ⚠️ 未命中 |
| TutorialWarlordTitle | ⚠️ 未命中 |
| TutorialDescription | ⚠️ 未命中 |
| Army Selector | ✅ `scripts\battle.gd:171 # 原版 battlearena1 场景树无阵营选择弹窗 (Army Selector 在模式选择界面) —; scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: ` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Completed Text | ✅ `scripts\tutorial.gd:7 ## Completed Text 'Completed: 1/6'; scripts\tutorial.gd:108 # 完成进度 (原版 Completed Text 'Completed: 1/6'; 2026` |

## 摘要

- 规格元素: 21
- 代码命中: 15
- ⚠️未命中: 6 (以下需人工判断)

- `Header Background`
- `Header Background (1)`
- `TutorialTitle`
- `TutorialSubTitle`
- `TutorialWarlordTitle`
- `TutorialDescription`