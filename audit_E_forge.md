# UI 规格审计: Forge Tab

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Forge Tab [inactive godot(x330.7 y71.1 w1589.3 h1008.7)]
  Background [godot(x330.7 y71.1 w1589.3 h1008.7)]
    Warp [godot(x741.8 y88.5 w767.0 h974.0)]
    War ParticleSystemUI [godot(x1125.3 y575.5 w0.0 h0.0)]
      Warp Particle System [godot(x1125.3 y575.5 w0.0 h0.0)]
  Ready for level up [godot(x1028.1 y424.1 w194.5 h302.8)]
    Glow [godot(x775.3 y225.5 w700.0 h700.0)]
    War ParticleSystemUI Down [godot(x1125.3 y949.5 w0.0 h0.0)]
      Rays [godot(x1125.3 y949.5 w0.0 h0.0)]
        Glow (1) [godot(x1125.3 y949.5 w0.0 h0.0)]
    War ParticleSystem Up [godot(x1125.3 y191.5 w0.0 h0.0)]
      Rays [godot(x1125.3 y191.5 w0.0 h0.0)]
        Glow [godot(x1125.3 y191.5 w0.0 h0.0)]
  Rewards Scroll View [godot(x331.0 y318.6 w1588.7 h761.4)]
    Viewport [godot(x331.0 y318.6 w1588.7 h761.4)]
      Rewards Content [godot(x331.0 y318.6 w122.0 h761.4)]
  Forge Army Selector [godot(x588.2 y71.6 w1074.3 h125.1)]
    Separator Line [godot(x491.4 y191.4 w1267.9 h6.0)]
    Viewport [godot(x588.2 y71.6 w1074.3 h125.1)]
      Army Content [godot(x1125.3 y71.6 w0.0 h126.0)]
  Background Elements [godot(x330.7 y71.1 w1589.3 h1008.7)]
    Decoration Top [godot(x444.7 y185.1 w273.0 h210.0)]
    Column Left [godot(x330.7 y15.2 w373.0 h1452.9)]
      Culumn Top [godot(x330.7 y8.5 w331.8 h478.4)]
        Candle [godot(x458.5 y188.3 w40.0 h59.0)]
        Culumn Mid [godot(x330.7 y486.9 w214.2 h479.4)]
          Culumn Down [godot(x330.7 y966.3 w221.5 h493.0)]
        Light Candle [godot(x358.8 y154.2 w142.6 h175.5)]
    Column Right [godot(x1920.0 y15.2 w-373.0 h1452.9)]
      Culumn Top [godot(x1920.0 y2927.6 w-331.8 h-478.4)]
        Candle (1) [godot(x1753.7 y2747.8 w40.0 h-59.0)]
        Light Candle (1) [godot(x1891.9 y2781.9 w-142.4 h-175.5)]
        Culumn Mid [godot(x1920.0 y2449.2 w-214.2 h-479.4)]
          Culumn Down [godot(x1920.0 y1969.8 w-221.5 h-493.0)]
  Selected Army Info [godot(x619.4 y195.8 w621.3 h122.7)]
    ArmyText [txt=Ultramarines godot(x762.9 y209.4 w320.9 h50.0)]
    LevelText [txt=Level 1/50 godot(x766.1 y252.8 w331.0 h50.0)]
    Army Icon [godot(x621.8 y188.4 w125.2 h125.3)]
    Xp Points Icon [inactive godot(x758.1 y292.5 w53.0 h53.0)]
      TotalXp Points [txt=154748 godot(x811.1 y294.0 w232.3 h50.0)]
  Debug Add points [inactive godot(x947.4 y214.2 w203.7 h53.9)]
    Text (TMP) [txt=Debug add points godot(x947.4 y214.2 w203.7 h53.9)]
    InputField (TMP) [godot(x1161.2 y214.2 w84.5 h53.9)]
      Text Area [godot(x1171.2 y221.2 w64.5 h40.9)]
        Placeholder [txt=Enter text... godot(x1171.2 y221.2 w64.5 h40.9)]
        Text [txt=5​ godot(x1171.2 y221.2 w64.5 h40.9)]
  Debug Set Forge [inactive godot(x1278.5 y215.9 w203.7 h53.9)]
    Text (TMP) [txt=Set Forge Level godot(x1278.5 y215.9 w203.7 h53.9)]
    InputField (TMP) [godot(x1492.3 y215.9 w84.5 h53.9)]
      Text Area [godot(x1502.3 y222.9 w64.5 h40.9)]
        Placeholder [txt=Enter text... godot(x1502.3 y222.9 w64.5 h40.9)]
        Text [txt=5​ godot(x1502.3 y222.9 w64.5 h40.9)]
  Help Icon [godot(x1685.2 y215.9 w52.2 h52.2)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Forge Tab | ✅ `scripts\battle.gd:2992 # 熔炉点结算 (Forge Tab 数据源: 胜利 +50 / Defeat +20); scripts\forge.gd:3 ## 熔炉页 (原版 Forge Tab 说明书 [164,0 1756x1080]` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Warp | ✅ `scripts\base_event_popup.gd:10 var _title_text := "Welcome to Warpforge!"; scripts\base_event_popup.gd:11 var _desc_text := "Welco` |
| War ParticleSystemUI | ⚠️ 未命中 |
| Warp Particle System | ⚠️ 未命中 |
| Ready for level up | ✅ `scripts\forge.gd:179 # Ready for level up 光效 (说明书 Glow [692,190 700x700], 可领取时显示)` |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| War ParticleSystemUI Down | ⚠️ 未命中 |
| Rays | ⚠️ 未命中 |
| Glow (1) | ⚠️ 未命中 |
| War ParticleSystem Up | ⚠️ 未命中 |
| Rays | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| Rewards Scroll View | ✅ `scripts\daily_streak_popup.gd:4 ##   Streak Successful: 'Current streak: 7' + Rewards Scroll View + 'More Rewards In 19h 23m'; scr` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Rewards Content | ⚠️ 未命中 |
| Forge Army Selector | ✅ `scripts\forge.gd:3 ## 熔炉页 (原版 Forge Tab 说明书 [164,0 1756x1080]: Warp 涡旋背景 + 石柱蜡烛装饰 + Forge Army Selector + Selected Army; scripts\f` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Army Content | ⚠️ 未命中 |
| Background Elements | ✅ `scripts\forge.gd:120 # 左右石柱蜡烛装饰 (说明书 Background Elements, Column Right 右缘对齐镜像)` |
| Decoration Top | ⚠️ 未命中 |
| Column Left | ✅ `scripts\forge.gd:220 ## 石柱蜡烛 (说明书 Column Left [164,0]/Column Right 右缘镜像); scripts\forge.gd:234 # Column_down 段 (2026-08-22 曾删; 复核 ` |
| Culumn Top | ⚠️ 未命中 |
| Candle | ✅ `scripts\battle.gd:688 ["sororitas/Candle 202.obj", -7.5, 0.5, 0, 800.0, 90, 0], ["sororitas/Candle 202.obj", 7.5, 0.5, 0, ; script` |
| Culumn Mid | ⚠️ 未命中 |
| Culumn Down | ⚠️ 未命中 |
| Light Candle | ⚠️ 未命中 |
| Column Right | ✅ `scripts\forge.gd:120 # 左右石柱蜡烛装饰 (说明书 Background Elements, Column Right 右缘对齐镜像); scripts\forge.gd:220 ## 石柱蜡烛 (说明书 Column Left [164` |
| Culumn Top | ⚠️ 未命中 |
| Candle (1) | ⚠️ 未命中 |
| Light Candle (1) | ⚠️ 未命中 |
| Culumn Mid | ⚠️ 未命中 |
| Culumn Down | ⚠️ 未命中 |
| Selected Army Info | ✅ `scripts\forge.gd:3 ## 熔炉页 (原版 Forge Tab 说明书 [164,0 1756x1080]: Warp 涡旋背景 + 石柱蜡烛装饰 + Forge Army Selector + Selected Army; scripts\f` |
| ArmyText | ✅ `scripts\forge.gd:241 ## 首字母大写 (原版 ArmyText 显示 Title Case)` |
| LevelText | ✅ `scripts\forge.gd:38 const MAX_LEVEL := 50          # 说明书 LevelText 'Level 1/50'` |
| Army Icon | ✅ `scripts\campaign.gd:190 # 阵营图标 (原版 Army Icon); scripts\card_displayer.gd:489 # 阵营图标 (场景 Army Icon 80x85)` |
| Xp Points Icon | ⚠️ 未命中 |
| TotalXp Points | ⚠️ 未命中 |
| Debug Add points | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| InputField (TMP) | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Debug Set Forge | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| InputField (TMP) | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Help Icon | ✅ `scripts\forge.gd:208 # Help Icon (说明书 [1685,145 52x52])` |

## 摘要

- 规格元素: 53
- 代码命中: 26
- ⚠️未命中: 27 (以下需人工判断)

- `War ParticleSystemUI`
- `Warp Particle System`
- `War ParticleSystemUI Down`
- `Rays`
- `Glow (1)`
- `War ParticleSystem Up`
- `Rays`
- `Rewards Content`
- `Army Content`
- `Decoration Top`
- `Culumn Top`
- `Culumn Mid`
- `Culumn Down`
- `Light Candle`
- `Culumn Top`
- `Candle (1)`
- `Light Candle (1)`
- `Culumn Mid`
- `Culumn Down`
- `Xp Points Icon`
- `TotalXp Points`
- `Debug Add points`
- `Text (TMP)`
- `InputField (TMP)`
- `Debug Set Forge`
- `Text (TMP)`
- `InputField (TMP)`