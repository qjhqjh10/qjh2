# UI 规格审计: Choose Army Deck FTUE Window

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-24 19:56
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Choose Army Deck FTUE Window [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Title [txt=SELECT ARMY godot(x0.0 y55.0 w1920.0 h110.3)]
  SubTitle [txt=You will receive a full deck and a Warlo godot(x0.0 y140.0 w1920.0 h79.4)]
  Continue Group [godot(x585.7 y969.0 w748.6 h84.6)]
    War ParticleSystemUI Left [godot(x649.0 y1011.3 w0.0 h0.0)]
      Rays [godot(x649.0 y1011.3 w0.0 h0.0)]
        Glow (1) [godot(x649.0 y1011.3 w0.0 h0.0)]
    War ParticleSystemUI Right [godot(x1290.1 y1001.7 w0.0 h0.0)]
      Rays [godot(x1290.1 y1001.7 w0.0 h0.0)]
        Glow (1) [godot(x1290.1 y1001.7 w0.0 h0.0)]
    Continue Button [godot(x585.7 y969.0 w748.6 h84.6)]
      Text (TMP) [txt=Continue godot(x793.8 y968.5 w217.1 h85.6)]
      Selected Faction Icon [godot(x533.0 y1000.9 w105.3 h105.3)]
  Armies [godot(x0.0 y186.1 w1920.0 h762.1)]
    Viewport [godot(x0.0 y186.1 w1920.0 h745.1)]
      Content [godot(x0.0 y186.1 w1920.0 h522.0)]
        Deck Container FTUE [godot(x-181.3 y708.1 w362.6 h0.0)]
          Glow [godot(x-261.9 y446.2 w523.8 h523.8)]
          Warlord Image [godot(x-261.9 y446.2 w523.8 h523.8)]
          Army Icon [godot(x-116.5 y807.6 w233.0 h233.0)]
            Army Icon Shadow [godot(x-116.5 y807.6 w233.0 h233.0)]
            Army Icon [godot(x-104.7 y819.4 w206.7 h208.6)]
          Army Text [godot(x-220.5 y951.8 w441.0 h89.0)]
            Army Text Shadow [godot(x-220.5 y951.8 w441.0 h89.0)]
            Army Text [txt=ULTRAMARINES godot(x-263.2 y965.0 w526.4 h75.2)]
          Selected Text [inactive godot(x-186.5 y681.0 w371.0 h128.3)]
            SelectedTextBg [godot(x-186.5 y684.9 w371.0 h120.5)]
            SelectedText [txt=Selected godot(x-167.8 y712.0 w333.6 h66.2)]
          Army Description [txt=- Balanced and adaptable\n-Strong defense godot(x-199.5 y1040.8 w398.6 h138.2)]
          Select Button [godot(x-261.9 y427.5 w523.8 h774.8)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Choose Army Deck FTUE Window | ✅ `scripts\choose_army.gd:2 ## 新手选阵营窗 (原版 Choose Army Deck FTUE Window [6576] 说明书):; scripts\main_menu.gd:153 # 首启链: ① 新手指引选阵营 (原版 Ch` |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\ally_badge_drawer.gd:65 # 遮罩: 纯黑 ` |
| Title | ✅ `scripts\ally_badge_drawer.gd:90 title.name = "Title"; scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [100` |
| SubTitle | ✅ `scripts\choose_army.gd:3 ##   Title 'SELECT ARMY' [0,55 1920x110] + SubTitle [0,140] + Armies 横滚 [0,186 1920x762] +; scripts\choos` |
| Continue Group | ✅ `scripts\choose_army.gd:5 ##   Description 3 行 + Selected 印) + Continue Group [586,969 749x85] (光粒子+Continue 钮+Selected Factio; scr` |
| War ParticleSystemUI Left | ⚠️ 未命中 |
| Rays | ✅ `scripts\packs.gd:726 var flash_tex := PT + ("Glow.png" if (rarity == "epic" or rarity == "legendary") else "Glow Rays.png; scripts` |
| Glow (1) | ⚠️ 未命中 |
| War ParticleSystemUI Right | ⚠️ 未命中 |
| Rays | ✅ `scripts\packs.gd:726 var flash_tex := PT + ("Glow.png" if (rarity == "epic" or rarity == "legendary") else "Glow Rays.png; scripts` |
| Glow (1) | ⚠️ 未命中 |
| Continue Button | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Selected Faction Icon | ✅ `scripts\choose_army.gd:5 ##   Description 3 行 + Selected 印) + Continue Group [586,969 749x85] (光粒子+Continue 钮+Selected Factio; scr` |
| Armies | ✅ `scripts\choose_army.gd:3 ##   Title 'SELECT ARMY' [0,55 1920x110] + SubTitle [0,140] + Armies 横滚 [0,186 1920x762] +; scripts\choos` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:279 # 物品池 (原版 Re` |
| Content | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |
| Deck Container FTUE | ✅ `scripts\choose_army.gd:4 ##   Deck Container FTUE 363x522 军队卡 (Warlord 立绘 524² + Army Icon 233² + Army Text 75px +; scripts\choose` |
| Glow | ✅ `scripts\battle.gd:530 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:535 ["Glow Acum` |
| Warlord Image | ✅ `scripts\deck_info_popup.gd:80 # 督军立绘 (原版 Warlord Image 1108x1108, pivot(0.5,0) 原始 JSON RectTransform_8411164374367242664:; scripts` |
| Army Icon | ✅ `scripts\campaign.gd:195 # 阵营图标 (原版 Army Icon 135×165 @ (345.7,60.9)); scripts\card_displayer.gd:607 # 阵营图标 (场景 Army Icon 80x85)` |
| Army Icon Shadow | ⚠️ 未命中 |
| Army Icon | ✅ `scripts\campaign.gd:195 # 阵营图标 (原版 Army Icon 135×165 @ (345.7,60.9)); scripts\card_displayer.gd:607 # 阵营图标 (场景 Army Icon 80x85)` |
| Army Text | ✅ `scripts\choose_army.gd:4 ##   Deck Container FTUE 363x522 军队卡 (Warlord 立绘 524² + Army Icon 233² + Army Text 75px +; scripts\choose` |
| Army Text Shadow | ⚠️ 未命中 |
| Army Text | ✅ `scripts\choose_army.gd:4 ##   Deck Container FTUE 363x522 军队卡 (Warlord 立绘 524² + Army Icon 233² + Army Text 75px +; scripts\choose` |
| Selected Text | ⚠️ 未命中 |
| SelectedTextBg | ⚠️ 未命中 |
| SelectedText | ⚠️ 未命中 |
| Army Description | ⚠️ 未命中 |
| Select Button | ✅ `scripts\choose_army.gd:126 ## + Description 3 行 + Select Button 整卡点击 + Selected 印)` |

## 摘要

- 规格元素: 31
- 代码命中: 19
- ⚠️未命中: 12 (以下需人工判断)

- `War ParticleSystemUI Left`
- `Glow (1)`
- `War ParticleSystemUI Right`
- `Glow (1)`
- `Continue Button`
- `Text (TMP)`
- `Army Icon Shadow`
- `Army Text Shadow`
- `Selected Text`
- `SelectedTextBg`
- `SelectedText`
- `Army Description`