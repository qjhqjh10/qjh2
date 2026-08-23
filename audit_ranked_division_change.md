# UI 规格审计: Ranked Division Change Window

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:35
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Ranked Division Change Window [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Title [txt=PROMOTED! godot(x960.0 y0.0 w0.0 h112.0)]
    Game Mode Icon Left [godot(x860.0 y6.0 w100.0 h100.0)]
    Game Mode Icon Right [godot(x960.0 y6.0 w100.0 h100.0)]
  Division Image [godot(x534.3 y149.3 w851.4 h851.4)]
    Rank Icon [godot(x923.8 y421.3 w73.6 h73.6)]
      Rank Icon Glow [inactive godot(x923.5 y421.0 w74.2 h74.2)]
  Text Content [godot(x0.0 y0.0 w1920.0 h1080.0)]
    New division reached Text [txt=You have reached the Legenday Division! godot(x257.9 y105.1 w1404.2 h98.1)]
    Ranking Points Title [inactive txt=Rating: godot(x469.3 y655.7 w981.4 h79.3)]
    Rank Points [inactive godot(x758.2 y735.0 w403.6 h100.0)]
      Background [godot(x627.3 y743.5 w665.4 h83.0)]
      Rank Icon [godot(x857.6 y735.0 w100.0 h100.0)]
      Ranking Points Quantity Text [txt=44795 godot(x957.6 y745.4 w104.8 h79.3)]
    Tap To continue [txt=Click to continue godot(x336.9 y1000.7 w1246.2 h79.3)]
  Particles DivisionUp [godot(x0.0 y0.0 w1920.0 h1080.0)]
    Glow below [godot(x-11541.0 y-12001.0 w25000.0 h25000.0)]
    Sparks background [godot(x-11541.0 y-12001.0 w25000.0 h25000.0)]
    Sparks Burn [godot(x-11541.0 y-12001.0 w25000.0 h25000.0)]
      Glow Big [godot(x-11541.0 y-12001.0 w25000.0 h25000.0)]
      Promote Letter Effect [godot(x-11582.3 y-12002.5 w25000.1 h25000.0)]
      Sparks fast [godot(x-11541.0 y-12001.0 w25000.0 h25000.0)]
  Mission Milestones Progress [godot(x292.5 y418.7 w1335.0 h242.6)]
    steps [godot(x-708.7 y236.7 w3337.4 h606.6)]
      RankedSealStep [godot(x-708.7 y843.3 w0.0 h0.0)]
        Empty [godot(x-708.7 y843.3 w0.0 h0.0)]
        Fill [godot(x-708.7 y843.3 w0.0 h0.0)]
      RankedSealStep (1) [godot(x-708.7 y843.3 w0.0 h0.0)]
        Empty [godot(x-708.7 y843.3 w0.0 h0.0)]
        Fill [godot(x-708.7 y843.3 w0.0 h0.0)]
      RankedSealStep (2) [godot(x-708.7 y843.3 w0.0 h0.0)]
        Empty [godot(x-708.7 y843.3 w0.0 h0.0)]
        Fill [godot(x-708.7 y843.3 w0.0 h0.0)]
      RankedSealStep (3) [godot(x-708.7 y843.3 w0.0 h0.0)]
        Empty [godot(x-708.7 y843.3 w0.0 h0.0)]
        Fill [godot(x-708.7 y843.3 w0.0 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Ranked Division Change Window | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Game Mode Icon Left | ⚠️ 未命中 |
| Game Mode Icon Right | ⚠️ 未命中 |
| Division Image | ⚠️ 未命中 |
| Rank Icon | ⚠️ 未命中 |
| Rank Icon Glow | ⚠️ 未命中 |
| Text Content | ⚠️ 未命中 |
| New division reached Text | ⚠️ 未命中 |
| Ranking Points Title | ⚠️ 未命中 |
| Rank Points | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Rank Icon | ⚠️ 未命中 |
| Ranking Points Quantity Text | ⚠️ 未命中 |
| Tap To continue | ⚠️ 未命中 |
| Particles DivisionUp | ⚠️ 未命中 |
| Glow below | ⚠️ 未命中 |
| Sparks background | ⚠️ 未命中 |
| Sparks Burn | ⚠️ 未命中 |
| Glow Big | ⚠️ 未命中 |
| Promote Letter Effect | ⚠️ 未命中 |
| Sparks fast | ⚠️ 未命中 |
| Mission Milestones Progress | ✅ `scripts\quests.gd:434 # 进度 '52/500' 40px + bar (原版 Mission Milestones Progress Bar)` |
| steps | ✅ `scripts\battle.gd:2329 var steps: Array = _tutorial_data.get(stage_key, {}).get("steps", []); scripts\battle.gd:2329 var steps: Ar` |
| RankedSealStep | ✅ `scripts\ranked.gd:160 # footer (原版 '4879'/'32'/'16' 40px + RankedSealStep); scripts\ranked.gd:170 # RankedSealStep ×5 (原版 Rank Sku` |
| Empty | ✅ `scripts\battle.gd:2553 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:235 var isb := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| RankedSealStep (1) | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2553 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:235 var isb := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| RankedSealStep (2) | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2553 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:235 var isb := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| RankedSealStep (3) | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2553 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:235 var isb := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |

## 摘要

- 规格元素: 37
- 代码命中: 14
- ⚠️未命中: 23 (以下需人工判断)

- `Ranked Division Change Window`
- `Game Mode Icon Left`
- `Game Mode Icon Right`
- `Division Image`
- `Rank Icon`
- `Rank Icon Glow`
- `Text Content`
- `New division reached Text`
- `Ranking Points Title`
- `Rank Points`
- `Rank Icon`
- `Ranking Points Quantity Text`
- `Tap To continue`
- `Particles DivisionUp`
- `Glow below`
- `Sparks background`
- `Sparks Burn`
- `Glow Big`
- `Promote Letter Effect`
- `Sparks fast`
- `RankedSealStep (1)`
- `RankedSealStep (2)`
- `RankedSealStep (3)`