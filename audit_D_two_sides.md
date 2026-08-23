# UI 规格审计: Two Sides Event Window

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Two Sides Event Window [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Select Team Tab [inactive godot(x0.0 y0.0 w1920.0 h1080.0)]
    Scan Lines [godot(x615.9 y148.0 w688.2 h740.1)]
    Glow [godot(x764.2 y378.0 w391.6 h400.0)]
    Two Side Event Select Team A [godot(x379.5 y164.0 w535.0 h737.8)]
      Background [godot(x379.5 y164.0 w535.0 h737.8)]
        Background noise [sprite=UI Dirt And Noise skratches godot(x332.7 y101.3 w700.6 h800.5)]
        Foreground Image [godot(x200.2 y164.0 w893.6 h893.6)]
        Bottom Glow [godot(x280.6 y166.4 w732.8 h732.8)]
      Bottom Text [godot(x381.6 y793.4 w530.8 h105.9)]
        Team Name [txt=Red Team godot(x360.7 y752.3 w529.3 h77.8)]
        Tap to select [txt=Select godot(x355.2 y834.2 w524.6 h55.7)]
      Border [godot(x379.5 y164.0 w535.0 h737.8)]
      Top [godot(x404.0 y164.0 w533.2 h100.0)]
        Team captain [txt=#squidmar godot(x423.6 y175.1 w504.9 h77.8)]
    Two Side Event Select Team B [godot(x1025.5 y164.0 w535.0 h737.8)]
      Background [godot(x1025.5 y164.0 w535.0 h737.8)]
        Background noise [sprite=UI Dirt And Noise skratches godot(x978.7 y101.3 w700.6 h800.5)]
        Foreground Image [godot(x846.2 y164.0 w893.6 h893.6)]
        Bottom Glow [godot(x926.6 y166.4 w732.8 h732.8)]
      Bottom Text [godot(x1027.6 y793.4 w530.8 h105.9)]
        Team Name [txt=Red Team godot(x1006.7 y752.3 w529.3 h77.8)]
        Tap to select [txt=Select godot(x1001.2 y834.2 w524.6 h55.7)]
      Border [godot(x1025.5 y164.0 w535.0 h737.8)]
      Top [godot(x1050.0 y164.0 w533.2 h100.0)]
        Team captain [txt=#squidmar godot(x1069.6 y175.1 w504.9 h77.8)]
    War ParticleSystemUI Up [godot(x954.0 y559.0 w0.0 h0.0)]
      Rays [godot(x954.0 y559.0 w0.0 h0.0)]
        Glow (1) [godot(x954.0 y559.0 w0.0 h0.0)]
    War ParticleSystemUI Down [godot(x954.0 y559.0 w0.0 h0.0)]
      Rays [godot(x954.0 y559.0 w0.0 h0.0)]
        Glow (1) [godot(x954.0 y559.0 w0.0 h0.0)]
    Title Background [godot(x465.8 y31.0 w988.4 h100.0)]
      Title [txt=BATTLE FOR WARPFORGE godot(x291.2 y31.0 w1337.6 h100.0)]
    VS Text [godot(x837.7 y432.7 w244.6 h252.6)]
    Description [txt=<color=#E27E1B>Choose your side. Fight f godot(x160.8 y921.6 w1598.4 h146.8)]
    Back button [godot(x35.0 y995.8 w64.2 h63.2)]
      Icon [godot(x43.4 y1004.0 w47.4 h46.7)]
      Text [txt=Back godot(x108.3 y995.8 w305.3 h63.2)]
  Event On Going Tab [godot(x0.0 y0.0 w1920.0 h1080.0)]
    General Red Background [godot(x0.0 y634.3 w1920.0 h-159.7)]
      Menu Dark Background [inactive godot(x-1327.3 y-759.2 w4574.6 h2572.4)]
      Reward Background Get Reward [godot(x-960.0 y93.6 w3840.0 h921.8)]
      Noise [sprite=UI Dirt And Noise skratches godot(x-960.0 y93.6 w3840.0 h921.8)]
      Menu Vignette [godot(x-960.0 y-28.2 w3840.0 h1110.5)]
    Game Mode Header With Back Button [godot(x0.0 y40.9 w550.0 h109.5)]
      Header Background [godot(x0.0 y40.9 w0.0 h115.3)]
        Window Title [txt=Game mode godot(x155.0 y57.2 w369.4 h82.7)]
        Game Mode Icon [godot(x0.0 y106.2 w100.0 h100.0)]
          tooltip trigger [godot(x12.3 y120.4 w75.4 h71.7)]
      Header Background (1) [godot(x-462.1 y40.9 w550.0 h115.3)]
      Header Back Button [godot(x-24.4 y42.9 w167.9 h111.3)]
    Battle Background [godot(x-134.8 y145.4 w1745.6 h867.7)]
    Team A [godot(x-122.8 y174.8 w731.6 h871.1)]
      Team A Image [godot(x-215.6 y121.7 w887.2 h887.2)]
      Team A captain name [txt=#squidmar godot(x69.6 y705.9 w529.3 h77.9)]
    Teams B [godot(x795.9 y174.8 w684.2 h871.1)]
      Team B Image [godot(x635.9 y121.7 w887.3 h887.2)]
      Team B captain name [txt=#squidmar godot(x771.2 y706.9 w529.3 h77.9)]
    Reward Display [godot(x1352.0 y133.9 w638.0 h812.2)]
      Scoring Bar Event Score Info [godot(x1471.0 y406.9 w360.0 h470.4)]
        Progress Bar [godot(x1609.5 y415.9 w83.0 h452.8)]
          Fill Area [godot(x1636.2 y439.8 w28.9 h402.5)]
            Fill [godot(x1636.2 y836.8 w0.0 h5.5)]
          Background [godot(x1630.2 y415.9 w41.6 h452.8)]
        Score Levels [godot(x1588.2 y390.8 w125.6 h406.7)]
          Score Bar Line Level 1 [godot(x1402.5 y759.6 w371.4 h75.9)]
            Highlight Crate [sprite=Crate Border Highlight godot(x1598.8 y728.7 w150.9 h134.4)]
            Chest [godot(x1626.7 y753.2 w99.4 h88.7)]
            Skull [godot(x1497.6 y765.3 w64.5 h64.5)]
              Score [txt=1256 godot(x1364.1 y770.2 w126.9 h54.7)]
          Score Bar Line Level 2 [godot(x1402.5 y759.6 w371.4 h75.9)]
            Highlight Crate [sprite=Crate Border Highlight godot(x1598.8 y728.7 w150.9 h134.4)]
            Chest [godot(x1626.7 y753.2 w99.4 h88.7)]
            Skull [godot(x1497.6 y765.3 w64.5 h64.5)]
              Score [txt=1256 godot(x1364.1 y770.2 w126.9 h54.7)]
          Score Bar Line Level 3 [godot(x1402.5 y759.6 w371.4 h75.9)]
            Highlight Crate [sprite=Crate Border Highlight godot(x1598.8 y728.7 w150.9 h134.4)]
            Chest [godot(x1626.7 y753.2 w99.4 h88.7)]
            Skull [godot(x1497.6 y765.3 w64.5 h64.5)]
              Score [txt=1256 godot(x1364.1 y770.2 w126.9 h54.7)]
          Score Bar Line Level 4 [godot(x1402.5 y759.6 w371.4 h75.9)]
            Highlight Crate [sprite=Crate Border Highlight godot(x1598.8 y728.7 w150.9 h134.4)]
            Chest [godot(x1626.7 y753.2 w99.4 h88.7)]
            Skull [godot(x1497.6 y765.3 w64.5 h64.5)]
              Score [txt=1256 godot(x1364.1 y770.2 w126.9 h54.7)]
          Score Bar Line Level 5 [godot(x1402.5 y759.6 w371.4 h75.9)]
            Highlight Crate [sprite=Crate Border Highlight godot(x1598.8 y728.7 w150.9 h134.4)]
            Chest [godot(x1626.7 y753.2 w99.4 h88.7)]
            Skull [godot(x1497.6 y765.3 w64.5 h64.5)]
              Score [txt=1256 godot(x1364.1 y770.2 w126.9 h54.7)]
        Generic Simplified UI Button [godot(x1507.4 y889.8 w287.2 h86.5)]
          Button Text [txt=Collect godot(x1517.4 y898.2 w267.3 h69.6)]
      Reward Tile [txt=Progression godot(x1390.0 y151.3 w522.0 h54.6)]
      Reward Help [txt=Get skulls to progress in the event and  godot(x1374.6 y205.9 w530.0 h105.6)]
      Player victories [godot(x1373.6 y303.9 w546.6 h90.5)]
        Vicotries title [txt=Skulls: godot(x1367.2 y324.1 w236.6 h50.0)]
        Skull Victories [godot(x1610.2 y312.5 w73.4 h73.3)]
          Total Victories [txt=125 godot(x1690.8 y324.1 w180.8 h50.0)]
    Scoring slider [godot(x58.3 y745.3 w1230.3 h173.4)]
      Background [godot(x58.3 y788.7 w1230.3 h86.6)]
      Fill Area [godot(x63.3 y788.7 w1230.1 h86.6)]
        Fill [godot(x58.3 y875.3 w0.1 h0.0)]
      Center Mark [godot(x670.1 y788.7 w6.7 h86.6)]
    Your Team Text_Team A [txt=Your Team godot(x49.1 y875.7 w301.8 h57.1)]
    Your Team Text_Team B [txt=Your Team godot(x971.1 y875.7 w301.8 h57.1)]
    Team A Name [godot(x71.7 y793.1 w581.4 h77.8)]
      Team Bonus [godot(x21.7 y820.9 w100.0 h100.0)]
        Skull SDF [sprite=40k_battle_Win Skull SDF godot(x-3.6 y804.3 w147.8 h137.4)]
        Skull [godot(x33.7 y833.8 w75.3 h75.2)]
      Team A Name [txt=Blue Team godot(x-176.4 y793.1 w496.2 h77.8)]
    Team B Name [godot(x691.3 y793.1 w581.4 h77.8)]
      Team B Name [txt=Blue Team godot(x443.1 y793.1 w496.3 h77.8)]
      Team Bonus [godot(x641.3 y820.9 w100.0 h100.0)]
        Skull SDF [sprite=40k_battle_Win Skull SDF godot(x616.0 y804.3 w147.8 h137.4)]
        Skull [godot(x653.3 y833.8 w75.2 h75.2)]
    Timer With Time Description [godot(x471.3 y914.6 w404.3 h38.0)]
      Timer Description [txt=Starts in: godot(x471.3 y906.5 w0.0 h54.1)]
        Clock Icon [sprite=WF_icon_clock for shader godot(x471.3 y910.0 w47.2 h47.2)]
          Timer Text [txt=5d 20h 15m godot(x518.5 y906.5 w291.4 h54.1)]
    VS Text [godot(x532.7 y503.7 w244.6 h252.6)]
      Glow [godot(x517.1 y489.2 w275.8 h281.6)]
      VS Text [godot(x532.7 y503.7 w244.6 h252.6)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Two Sides Event Window | ✅ `scripts\two_sides_event.gd:2 ## 双边事件窗口 (原版 Two Sides Event Window [10020] 说明书):` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Select Team Tab | ✅ `scripts\two_sides_event.gd:3 ##   Select Team Tab: Title 'BATTLE FOR WARPFORGE' + Team A/B 卡 (535x738 立绘+队名+Select+队长名) + VS + Ba;` |
| Scan Lines | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| Two Side Event Select Team A | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Background noise | ✅ `scripts\two_sides_event.gd:158 # 底 (原版 Background noise 噪声纹理)` |
| Foreground Image | ✅ `scripts\two_sides_event.gd:167 # 立绘 (原版 Foreground Image; 阵营督军立绘)` |
| Bottom Glow | ✅ `scripts\two_sides_event.gd:149 ## 队伍卡 (原版 Two Side Event Select Team: 噪声底 + 立绘 + Bottom Glow + 队名 + Select + Border + 队长名)` |
| Bottom Text | ⚠️ 未命中 |
| Team Name | ✅ `scripts\two_sides_event.gd:179 # 队名 (原版 Team Name)` |
| Tap to select | ✅ `scripts\two_sides_event.gd:191 # Select 提示 (原版 Tap to select)` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Top | ✅ `scripts\battle.gd:1350 ## 原版日志框四边拼边框 (Top 740×68 + Bottom 740×49 + Left/Right 拉伸); scripts\main_menu.gd:489 ##   TopBarButtons(Hor` |
| Team captain | ✅ `scripts\two_sides_event.gd:201 # 队长名 (原版 Team captain)` |
| Two Side Event Select Team B | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Background noise | ✅ `scripts\two_sides_event.gd:158 # 底 (原版 Background noise 噪声纹理)` |
| Foreground Image | ✅ `scripts\two_sides_event.gd:167 # 立绘 (原版 Foreground Image; 阵营督军立绘)` |
| Bottom Glow | ✅ `scripts\two_sides_event.gd:149 ## 队伍卡 (原版 Two Side Event Select Team: 噪声底 + 立绘 + Bottom Glow + 队名 + Select + Border + 队长名)` |
| Bottom Text | ⚠️ 未命中 |
| Team Name | ✅ `scripts\two_sides_event.gd:179 # 队名 (原版 Team Name)` |
| Tap to select | ✅ `scripts\two_sides_event.gd:191 # Select 提示 (原版 Tap to select)` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Top | ✅ `scripts\battle.gd:1350 ## 原版日志框四边拼边框 (Top 740×68 + Bottom 740×49 + Left/Right 拉伸); scripts\main_menu.gd:489 ##   TopBarButtons(Hor` |
| Team captain | ✅ `scripts\two_sides_event.gd:201 # 队长名 (原版 Team captain)` |
| War ParticleSystemUI Up | ⚠️ 未命中 |
| Rays | ⚠️ 未命中 |
| Glow (1) | ⚠️ 未命中 |
| War ParticleSystemUI Down | ⚠️ 未命中 |
| Rays | ⚠️ 未命中 |
| Glow (1) | ⚠️ 未命中 |
| Title Background | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| VS Text | ✅ `scripts\two_sides_event.gd:120 # VS 贴图 (原版 VS Text GO 实为 Image → VS icon.png 244.6x252.6 @ 屏幕 [838,433])` |
| Description | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Back button | ✅ `scripts\mode_select.gd:676 # Back (原版 Back button [216,893 64x63]: 圆钮底 UI_Button_Round_background + Icon 40k_UI_bt_back, 文字 'Ba` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Event On Going Tab | ✅ `scripts\two_sides_event.gd:4 ##   Event On Going Tab: Header + Battle Background (两队立绘) + Reward Display (竖进度条+5 级宝箱+骷髅计数+Collect;` |
| General Red Background | ✅ `scripts\draft.gd:123 # 背景 (原版 General Red Background: Reward Background 红底 + Noise 划痕 + 晕影)` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Reward Background Get Reward | ⚠️ 未命中 |
| Noise | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Menu Vignette | ✅ `scripts\menu_bg.gd:4 ## 还原依据: 菜单全树.md — 各二级界面根下均挂 Menu Dark Background [-1327,-746 4575x2572] + 专属背景 + Noise + Menu Vigne` |
| Game Mode Header With Back Button | ✅ `scripts\draft.gd:141 # Header (说明书 Game Mode Header With Back Button [0,14 550x110])` |
| Header Background | ⚠️ 未命中 |
| Window Title | ✅ `scripts\tutorial.gd:4 ## Window Title 'Game mode' + Back) + Warlod Image [411,-9 1098x1098] (督军立绘+Darkening) +` |
| Game Mode Icon | ✅ `scripts\deck_collection.gd:791 # 5) 模式图标 (右下, 原版 Game Mode Icon [171,274 84x86]; 玩家自建卡组=经典模式; 网格 0.9 倍 → offsets(153.45,229.5)); s` |
| tooltip trigger | ✅ `scripts\ranked.gd:140 # 段位说明 tooltip (原版 tooltip trigger 51x48 sprite:6885921657055102575 = 40K_generic_bt_info)` |
| Header Background (1) | ⚠️ 未命中 |
| Header Back Button | ✅ `scripts\tutorial.gd:64 # 返回按钮 (原版 Header Back Button 168x111)` |
| Battle Background | ✅ `scripts\two_sides_event.gd:4 ##   Event On Going Tab: Header + Battle Background (两队立绘) + Reward Display (竖进度条+5 级宝箱+骷髅计数+Collect;` |
| Team A | ✅ `scripts\two_sides_event.gd:3 ##   Select Team Tab: Title 'BATTLE FOR WARPFORGE' + Team A/B 卡 (535x738 立绘+队名+Select+队长名) + VS + Ba;` |
| Team A Image | ⚠️ 未命中 |
| Team A captain name | ⚠️ 未命中 |
| Teams B | ⚠️ 未命中 |
| Team B Image | ⚠️ 未命中 |
| Team B captain name | ⚠️ 未命中 |
| Reward Display | ✅ `scripts\quests.gd:315 # 里程碑奖励 (原版 Reward Display Mission 250x113 之一, 缩小版); scripts\two_sides_event.gd:4 ##   Event On Going Tab: H` |
| Scoring Bar Event Score Info | ⚠️ 未命中 |
| Progress Bar | ✅ `scripts\quests.gd:227 ## 周常挑战条 (说明书 Weekly Mission Container: header + Mission Progress Bar 1008x23 + 4 里程碑 70x70 + Reward; script` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Score Levels | ⚠️ 未命中 |
| Score Bar Line Level 1 | ✅ `scripts\social.gd:228 # 竖进度条 (MiniBar_01) + 5 级宝箱 (说明书 Alliance Score Bar Line Level 1-5); scripts\two_sides_event.gd:331 # 5 级宝箱 ` |
| Highlight Crate | ✅ `scripts\gacha.gd:180 # 宝箱高亮光晕 (说明书 Highlight Crate [177,163 846x754])` |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Score Bar Line Level 2 | ⚠️ 未命中 |
| Highlight Crate | ✅ `scripts\gacha.gd:180 # 宝箱高亮光晕 (说明书 Highlight Crate [177,163 846x754])` |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Score Bar Line Level 3 | ⚠️ 未命中 |
| Highlight Crate | ✅ `scripts\gacha.gd:180 # 宝箱高亮光晕 (说明书 Highlight Crate [177,163 846x754])` |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Score Bar Line Level 4 | ⚠️ 未命中 |
| Highlight Crate | ✅ `scripts\gacha.gd:180 # 宝箱高亮光晕 (说明书 Highlight Crate [177,163 846x754])` |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Score Bar Line Level 5 | ⚠️ 未命中 |
| Highlight Crate | ✅ `scripts\gacha.gd:180 # 宝箱高亮光晕 (说明书 Highlight Crate [177,163 846x754])` |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Generic Simplified UI Button | ✅ `scripts\two_sides_event.gd:386 # Collect 按钮 (原版 Generic Simplified UI Button)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Reward Tile | ⚠️ 未命中 |
| Reward Help | ⚠️ 未命中 |
| Player victories | ✅ `scripts\two_sides_event.gd:312 # 骷髅计数 (原版 Player victories Skulls: 125)` |
| Vicotries title | ⚠️ 未命中 |
| Skull Victories | ⚠️ 未命中 |
| Total Victories | ⚠️ 未命中 |
| Scoring slider | ✅ `scripts\two_sides_event.gd:4 ##   Event On Going Tab: Header + Battle Background (两队立绘) + Reward Display (竖进度条+5 级宝箱+骷髅计数+Collect;` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Center Mark | ✅ `scripts\two_sides_event.gd:404 # Scoring slider [58,745 1230x173]: 红蓝比分条 + Center Mark + Your Team; scripts\two_sides_event.gd:424` |
| Your Team Text_Team A | ⚠️ 未命中 |
| Your Team Text_Team B | ⚠️ 未命中 |
| Team A Name | ⚠️ 未命中 |
| Team Bonus | ⚠️ 未命中 |
| Skull SDF | ⚠️ 未命中 |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Team A Name | ⚠️ 未命中 |
| Team B Name | ⚠️ 未命中 |
| Team B Name | ⚠️ 未命中 |
| Team Bonus | ⚠️ 未命中 |
| Skull SDF | ⚠️ 未命中 |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Timer With Time Description | ⚠️ 未命中 |
| Timer Description | ⚠️ 未命中 |
| Clock Icon | ⚠️ 未命中 |
| Timer Text | ⚠️ 未命中 |
| VS Text | ✅ `scripts\two_sides_event.gd:120 # VS 贴图 (原版 VS Text GO 实为 Image → VS icon.png 244.6x252.6 @ 屏幕 [838,433])` |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| VS Text | ✅ `scripts\two_sides_event.gd:120 # VS 贴图 (原版 VS Text GO 实为 Image → VS icon.png 244.6x252.6 @ 屏幕 [838,433])` |

## 摘要

- 规格元素: 124
- 代码命中: 77
- ⚠️未命中: 47 (以下需人工判断)

- `Scan Lines`
- `Two Side Event Select Team A`
- `Bottom Text`
- `Two Side Event Select Team B`
- `Bottom Text`
- `War ParticleSystemUI Up`
- `Rays`
- `Glow (1)`
- `War ParticleSystemUI Down`
- `Rays`
- `Glow (1)`
- `Title Background`
- `Reward Background Get Reward`
- `Header Background`
- `Header Background (1)`
- `Team A Image`
- `Team A captain name`
- `Teams B`
- `Team B Image`
- `Team B captain name`
- `Scoring Bar Event Score Info`
- `Fill Area`
- `Score Levels`
- `Score Bar Line Level 2`
- `Score Bar Line Level 3`
- `Score Bar Line Level 4`
- `Score Bar Line Level 5`
- `Reward Tile`
- `Reward Help`
- `Vicotries title`
- `Skull Victories`
- `Total Victories`
- `Fill Area`
- `Your Team Text_Team A`
- `Your Team Text_Team B`
- `Team A Name`
- `Team Bonus`
- `Skull SDF`
- `Team A Name`
- `Team B Name`
- `Team B Name`
- `Team Bonus`
- `Skull SDF`
- `Timer With Time Description`
- `Timer Description`
- `Clock Icon`
- `Timer Text`