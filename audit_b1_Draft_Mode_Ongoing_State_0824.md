# UI 规格审计: Draft Mode Ongoing State

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-24 19:57
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Draft Mode Ongoing State [godot(x0.0 y0.0 w1920.0 h1080.0)]
  MainContent [godot(x118.7 y156.6 w1387.2 h723.9)]
    Warlord Image [inactive godot(x-77.4 y-32.4 w940.8 h940.8)]
    Game Mode Title [txt=Draft Mode godot(x681.7 y210.0 w775.3 h60.0)]
    Timer [godot(x681.7 y260.5 w775.3 h43.6)]
      Timer Icon [godot(x665.2 y287.6 w33.0 h33.0)]
      Timer [txt=Ends in: 23d 5h godot(x1088.7 y256.9 w0.0 h55.9)]
    Victories text [txt=Victories: godot(x903.7 y338.6 w218.7 h43.4)]
      Victories text Number [txt=0 godot(x1129.4 y315.6 w140.8 h89.3)]
    Win Marks [godot(x704.4 y382.0 w729.9 h316.0)]
      Background Back [godot(x727.8 y382.0 w692.4 h325.8)]
        Background [godot(x737.1 y400.2 w674.1 h288.8)]
      Stages Container [godot(x750.4 y415.0 w640.0 h259.2)]
        Stage Info UI_ref [godot(x750.4 y674.2 w0.0 h0.0)]
          Glow [inactive godot(x702.6 y626.6 w95.5 h95.1)]
          Completed [godot(x737.5 y661.2 w25.7 h33.5)]
    Defeat Marks [txt=Defeats: godot(x704.4 y729.9 w120.3 h52.2)]
      Losses container [godot(x824.7 y716.2 w233.1 h79.6)]
        Losses Info UI_ref [godot(x790.8 y761.9 w67.7 h67.8)]
          Fail [godot(x792.7 y763.8 w64.0 h64.0)]
    Quote End [inactive txt="Battles like this are what I was made f godot(x507.6 y260.5 w955.0 h57.1)]
    Glows [godot(x-8.7 y0.0 w2112.0 h1080.0)]
      Border Glow Up [godot(x693.1 y382.7 w770.0 h73.7)]
        Glow [godot(x693.1 y360.4 w770.0 h59.2)]
      Border Glow Down [godot(x693.1 y633.2 w770.0 h73.8)]
        Glow [godot(x693.1 y670.8 w770.0 h59.2)]
  Reset Event Button [godot(x1236.0 y727.5 w176.0 h53.0)]
    Button Text [txt=Abandonar godot(x1245.3 y732.7 w156.9 h42.6)]
  Reward Info Panel [godot(x1505.9 y168.3 w390.2 h712.2)]
    Generic Window Red Background Small [godot(x1505.9 y174.8 w390.2 h685.7)]
    Reward Info [godot(x1505.9 y168.3 w390.2 h712.2)]
      Crate [godot(x1505.9 y311.9 w390.2 h325.0)]
      Collect Button [godot(x1576.0 y719.4 w250.0 h60.0)]
        Button Text [txt=Collect reward godot(x1587.9 y725.3 w225.4 h48.2)]
  Debug Win [godot(x1262.0 y218.0 w150.0 h50.0)]
    Button Text [txt=Change Deck godot(x1270.3 y222.9 w132.9 h40.2)]
  Battle Button Button [godot(x1087.1 y934.2 w832.9 h49.8)]
    Button [godot(x1346.9 y934.2 w577.5 h49.8)]
      CircleButton [godot(x1820.0 y927.1 w-64.7 h64.0)]
      Text [txt=Battle godot(x1470.6 y934.2 w263.8 h49.8)]
  Debug Battle Button Button [godot(x854.4 y934.2 w577.5 h49.8)]
    CircleButton [godot(x1327.5 y927.1 w-64.6 h64.0)]
    Text [txt=Battle godot(x978.1 y934.2 w263.8 h49.8)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Draft Mode Ongoing State | ⚠️ 未命中 |
| MainContent | ⚠️ 未命中 |
| Warlord Image | ✅ `scripts\deck_info_popup.gd:80 # 督军立绘 (原版 Warlord Image 1108x1108, pivot(0.5,0) 原始 JSON RectTransform_8411164374367242664:; scripts` |
| Game Mode Title | ✅ `scripts\draft_expiring_popup.gd:4 ##   Game Mode Title 'The Space Marine event has finished!' +; scripts\draft_expiring_popup.gd:6` |
| Timer | ✅ `scripts\battle.gd:4918 var _clock_timer: Timer = null; scripts\battle.gd:4937 _clock_timer = Timer.new()` |
| Timer Icon | ✅ `scripts\season_banner_popup.gd:22 const TEX_CLOCK := SPR + "WF_icon_clock.png"                    # 原版 Timer Icon (New Season)` |
| Timer | ✅ `scripts\battle.gd:4918 var _clock_timer: Timer = null; scripts\battle.gd:4937 _clock_timer = Timer.new()` |
| Victories text | ⚠️ 未命中 |
| Victories text Number | ⚠️ 未命中 |
| Win Marks | ✅ `scripts\draft.gd:494 # Win Marks 12 格 (说明书 Stages Container [750,415 640x259] + Stage 80²)` |
| Background Back | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Stages Container | ✅ `scripts\draft.gd:494 # Win Marks 12 格 (说明书 Stages Container [750,415 640x259] + Stage 80²)` |
| Stage Info UI_ref | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:530 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:535 ["Glow Acum` |
| Completed | ✅ `scripts\battle.gd:3056 # 教程胜利 → 记录完成关卡 (tutorial.gd 'Completed: N/6' 数据源; 2026-08-21); scripts\battle.gd:3315 ## tutorial.gd 读取显示 ` |
| Defeat Marks | ✅ `scripts\draft.gd:524 # Defeat Marks (说明书 [704,730] 'Defeats:' + Losses 68²)` |
| Losses container | ⚠️ 未命中 |
| Losses Info UI_ref | ⚠️ 未命中 |
| Fail | ✅ `scripts\battle.gd:3452 _log("Failed to play tactic: " + ERR_MSGS.get(err, str(err))); scripts\battle.gd:3691 _log("Failed to play ` |
| Quote End | ⚠️ 未命中 |
| Glows | ⚠️ 未命中 |
| Border Glow Up | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:530 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:535 ["Glow Acum` |
| Border Glow Down | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:530 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:535 ["Glow Acum` |
| Reset Event Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Reward Info Panel | ✅ `scripts\draft.gd:556 # Reward Info Panel (说明书 [1506,168 390x712]: Crate + Collect reward)` |
| Generic Window Red Background Small | ⚠️ 未命中 |
| Reward Info | ✅ `scripts\draft.gd:556 # Reward Info Panel (说明书 [1506,168 390x712]: Crate + Collect reward)` |
| Crate | ✅ `scripts\battle.gd:645 # 装饰扩展: 箱堆两侧 (说明书 Crates 4/Crates 18 左侧近场, 镜像右侧); scripts\battle.gd:645 # 装饰扩展: 箱堆两侧 (说明书 Crates 4/Crates 18` |
| Collect Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Debug Win | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:412 # Button Text '1' 40px (原版 x[-0.05,122.85] 左对齐) = 通配符消耗数; 按钮内通配符小图标; scripts\deck_builder.gd:123 # 原` |
| Battle Button Button | ⚠️ 未命中 |
| Button | ✅ `scripts\ally_badge_drawer.gd:68 if ev is InputEventMouseButton and ev.pressed:; scripts\ally_badge_drawer.gd:116 var cell := Butto` |
| CircleButton | ✅ `scripts\mode_select.gd:708 # 右侧 CircleButton [1679,886 90x90] 40k_UI_bt_play — 2026-08-21 审查修正染色/字号); scripts\mode_select.gd:723 #` |
| Text | ✅ `scripts\achievements.gd:153 var bg := TextureRect.new(); scripts\achievements.gd:155 bg.expand_mode = TextureRect.EXPAND_IGNORE_SI` |
| Debug Battle Button Button | ⚠️ 未命中 |
| CircleButton | ✅ `scripts\mode_select.gd:708 # 右侧 CircleButton [1679,886 90x90] 40k_UI_bt_play — 2026-08-21 审查修正染色/字号); scripts\mode_select.gd:723 #` |
| Text | ✅ `scripts\achievements.gd:153 var bg := TextureRect.new(); scripts\achievements.gd:155 bg.expand_mode = TextureRect.EXPAND_IGNORE_SI` |

## 摘要

- 规格元素: 43
- 代码命中: 25
- ⚠️未命中: 18 (以下需人工判断)

- `Draft Mode Ongoing State`
- `MainContent`
- `Victories text`
- `Victories text Number`
- `Background Back`
- `Stage Info UI_ref`
- `Losses container`
- `Losses Info UI_ref`
- `Quote End`
- `Glows`
- `Border Glow Up`
- `Border Glow Down`
- `Reset Event Button`
- `Generic Window Red Background Small`
- `Collect Button`
- `Debug Win`
- `Battle Button Button`
- `Debug Battle Button Button`