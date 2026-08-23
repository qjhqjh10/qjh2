# UI 规格审计: Daily Streak Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Daily Streak Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  bg [godot(x0.0 y152.8 w1920.0 h812.1)]
  Separator Line Top [godot(x-5.0 y152.8 w1930.0 h14.9)]
  Separator Line Bottom [godot(x-5.0 y950.0 w1930.0 h14.9)]
  Streak Failed [godot(x910.0 y490.0 w100.0 h100.0)]
    Daily Streak Broken [txt=STREAK BROKEN godot(x47.4 y338.6 w1825.2 h136.8)]
    Current Streak Lost count [txt=Streak lost: 10 godot(x47.4 y465.4 w1825.2 h87.0)]
    Info [txt=Log in daily and keep your streak going  godot(x47.4 y583.0 w1825.2 h50.0)]
    Generic Simplified UI Button [godot(x727.7 y656.5 w464.6 h103.0)]
      Button Text [txt=Reset Streak godot(x744.0 y666.6 w431.2 h82.8)]
  Streak Successful [inactive godot(x0.0 y152.8 w1920.0 h812.1)]
    Fill Line [godot(x134.4 y519.1 w1785.6 h79.6)]
    Current Streak [txt=Current streak: godot(x43.0 y212.4 w490.9 h82.7)]
      Current Streak Value [txt=7 godot(x545.9 y212.4 w37.9 h82.7)]
    Rewards Scroll View [godot(x0.0 y159.3 w1920.0 h805.6)]
      Viewport [godot(x0.0 y159.3 w1920.0 h805.6)]
        Rewards Content [godot(x-0.0 y132.1 w2.0 h812.1)]
    Info [txt=Log in daily and keep your streak going  godot(x47.5 y830.0 w1825.0 h50.0)]
    Timer [godot(x598.3 y964.9 w723.4 h115.1)]
      Next Rewards text [txt=More Rewards In godot(x573.3 y997.5 w361.7 h50.0)]
      Image [godot(x940.0 y1002.5 w40.0 h40.0)]
      Timer Text [txt=19h 23m godot(x985.0 y997.5 w361.7 h50.0)]
  Header With Back Button [godot(x0.0 y21.7 w550.0 h109.5)]
    Header Background [godot(x0.0 y21.7 w0.0 h115.3)]
      Window Title [txt=Daily Streak godot(x155.0 y38.0 w379.3 h82.7)]
    Header Background (1) [godot(x-462.1 y21.7 w550.0 h115.3)]
    Header Back Button [godot(x-24.4 y23.7 w167.9 h111.3)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Daily Streak Popup | ✅ `scripts\daily_streak_popup.gd:2 ## 每日连胜弹窗 (原版 Daily Streak Popup [7107] 说明书):` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\achievements.gd:198 var bg :=` |
| Separator Line Top | ⚠️ 未命中 |
| Separator Line Bottom | ⚠️ 未命中 |
| Streak Failed | ✅ `scripts\daily_streak_popup.gd:3 ##   Streak Failed: 'STREAK BROKEN' + 'Streak lost: 10' + 'Reset Streak' 按钮; scripts\daily_streak_` |
| Daily Streak Broken | ⚠️ 未命中 |
| Current Streak Lost count | ⚠️ 未命中 |
| Info | ✅ `scripts\achievements.gd:10 const TEX_CONTAINER := SPR + "UI_Deck_Information_submenu_Back.png"; scripts\base_event_popup.gd:40 # 红` |
| Generic Simplified UI Button | ✅ `scripts\two_sides_event.gd:386 # Collect 按钮 (原版 Generic Simplified UI Button)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Streak Successful | ✅ `scripts\daily_streak_popup.gd:4 ##   Streak Successful: 'Current streak: 7' + Rewards Scroll View + 'More Rewards In 19h 23m'; scr` |
| Fill Line | ⚠️ 未命中 |
| Current Streak | ⚠️ 未命中 |
| Current Streak Value | ⚠️ 未命中 |
| Rewards Scroll View | ✅ `scripts\daily_streak_popup.gd:4 ##   Streak Successful: 'Current streak: 7' + Rewards Scroll View + 'More Rewards In 19h 23m'; scr` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Rewards Content | ⚠️ 未命中 |
| Info | ✅ `scripts\achievements.gd:10 const TEX_CONTAINER := SPR + "UI_Deck_Information_submenu_Back.png"; scripts\base_event_popup.gd:40 # 红` |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Next Rewards text | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Timer Text | ⚠️ 未命中 |
| Header With Back Button | ✅ `scripts\daily_streak_popup.gd:5 ##   Header With Back Button: 'Daily Streak' + Back; scripts\daily_streak_popup.gd:94 # Header Wit` |
| Header Background | ⚠️ 未命中 |
| Window Title | ✅ `scripts\tutorial.gd:4 ## Window Title 'Game mode' + Back) + Warlod Image [411,-9 1098x1098] (督军立绘+Darkening) +` |
| Header Background (1) | ⚠️ 未命中 |
| Header Back Button | ✅ `scripts\tutorial.gd:64 # 返回按钮 (原版 Header Back Button 168x111)` |

## 摘要

- 规格元素: 28
- 代码命中: 16
- ⚠️未命中: 12 (以下需人工判断)

- `Separator Line Top`
- `Separator Line Bottom`
- `Daily Streak Broken`
- `Current Streak Lost count`
- `Fill Line`
- `Current Streak`
- `Current Streak Value`
- `Rewards Content`
- `Next Rewards text`
- `Timer Text`
- `Header Background`
- `Header Background (1)`