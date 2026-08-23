# UI 规格审计: Campaign Tab

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Campaign Tab [inactive godot(x330.7 y70.9 w1589.3 h1009.1)]
  Campaign Background [godot(x330.3 y70.9 w1589.7 h1009.1)]
    Background Image [inactive godot(x330.3 y-45.2 w1589.7 h1589.7)]
  Campaign Army Selector [godot(x745.9 y70.9 w1174.4 h137.0)]
    Background [godot(x643.2 y71.4 w1277.1 h136.0)]
    Viewport [godot(x745.9 y70.9 w1174.4 h137.0)]
      Army Content [godot(x916.1 y70.9 w0.0 h137.0)]
  Campaign Header [godot(x330.7 y60.9 w460.2 h165.0)]
    Debug Point Button [inactive godot(x1146.2 y91.6 w245.0 h67.7)]
      Button Text [txt=Change Deck godot(x1157.9 y98.2 w220.8 h54.4)]
    Army Icon [godot(x345.7 y60.9 w135.0 h165.0)]
    Title [txt=ULTRAMARINES godot(x480.7 y60.9 w225.0 h74.3)]
    Premium Button Container [inactive godot(x743.2 y60.9 w262.5 h82.5)]
      Premium Button [godot(x743.2 y143.4 w0.0 h0.0)]
        Button Text [txt=Premium godot(x743.2 y143.4 w0.0 h0.0)]
      Premium pruchased [sprite=40k_campaign_Premium-icon godot(x811.2 y92.5 w54.1 h54.1)]
        Text (TMP) [txt=Premium godot(x865.3 y92.5 w141.9 h54.1)]
    Points [txt=Points: 69 godot(x480.7 y151.7 w368.2 h33.0)]
      Point Icon [godot(x828.1 y135.2 w100.0 h66.0)]
        Campaign Point Background [godot(x818.1 y128.6 w120.0 h79.2)]
        Army Icon [godot(x828.1 y135.2 w100.0 h66.0)]
    Info Button [godot(x719.8 y94.0 w41.2 h41.2)]
  Campaign Track [godot(x330.7 y335.5 w1589.6 h709.0)]
    Viewport [godot(x330.7 y285.5 w1589.6 h759.0)]
      Content [godot(x330.7 y335.5 w200.0 h659.0)]
  Premium Panel [godot(x344.3 y1080.0 w376.0 h0.0)]
    Background [godot(x344.3 y1080.0 w376.0 h0.0)]
    Title [txt=Premium Campaign daily bonus godot(x166.4 y1058.8 w355.8 h42.4)]
    Points [godot(x206.6 y1051.0 w275.4 h58.0)]
      Quantity [txt=200 godot(x270.4 y1051.0 w77.0 h58.0)]
      Points [godot(x141.6 y1074.1 w65.0 h69.7)]
        Icon Campaign Points Drawer Variant [godot(x141.6 y1143.8 w0.0 h0.0)]
          Content [godot(x141.6 y1143.8 w0.0 h0.0)]
            Campaign Glow [godot(x141.6 y1143.8 w0.0 h0.0)]
            Image [godot(x141.6 y1143.8 w0.0 h0.0)]
            Converted Drawer [inactive godot(x141.6 y1143.8 w0.0 h0.0)]
              Price Display [godot(x141.6 y1143.8 w0.0 h0.0)]
                icon [godot(x141.6 y1143.8 w0.0 h0.0)]
                text [txt=2000 godot(x141.6 y1143.8 w0.0 h0.0)]
              AlreadyOwned [txt=Already Owned godot(x141.6 y1143.8 w0.0 h0.0)]
            Ephemeral Drawer [inactive godot(x141.6 y1143.8 w0.0 h0.0)]
              Price Display [godot(x141.6 y1143.8 w0.0 h0.0)]
                icon [godot(x141.6 y1143.8 w0.0 h0.0)]
                text [txt=24 hours godot(x141.6 y1143.8 w0.0 h0.0)]
    Generic Simplified UI Button [godot(x216.3 y1052.3 w256.0 h55.4)]
      Button Text [txt=Continue godot(x225.2 y1057.6 w238.1 h46.8)]
    Timer [godot(x344.3 y1080.0 w348.4 h39.3)]
      Icon [godot(x344.3 y1100.0 w38.5 h38.6)]
      Timer Text [txt=Siguiente: 5d 20h 15m godot(x394.8 y1087.4 w285.9 h24.5)]
  Tutorial Message [inactive godot(x1184.1 y220.4 w567.1 h120.2)]
    Background [godot(x1142.1 y250.5 w651.0 h60.1)]
    Mask [godot(x1189.2 y255.1 w557.1 h50.5)]
      Background fill [sprite=40k_popup_texture godot(x1189.2 y255.1 w557.1 h50.5)]
    ChooseArmyText [txt=Choose your favourite faction. You can l godot(x1160.5 y255.3 w618.1 h51.4)]
    Highlight Down [sprite=Border Line Only Horizontal FX godot(x1031.4 y222.2 w898.3 h28.3)]
    Highlight Up [sprite=Border Line Only Horizontal FX godot(x1031.4 y160.0 w898.3 h28.2)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Campaign Tab | ✅ `scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaign Header + Campaign Track); scripts\quests.gd:` |
| Campaign Background | ⚠️ 未命中 |
| Background Image | ✅ `scripts\main_menu.gd:394 ##   Background Image(1x2: anchor(-0.294,0,1.294,1) 溢出卡面 ±157px / 1x1: 全贴, COVER)` |
| Campaign Army Selector | ✅ `scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaign Header + Campaign Track); scripts\campaign.g` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Army Content | ⚠️ 未命中 |
| Campaign Header | ✅ `scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaign Header + Campaign Track); scripts\campaign.g` |
| Debug Point Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Army Icon | ✅ `scripts\campaign.gd:190 # 阵营图标 (原版 Army Icon); scripts\card_displayer.gd:489 # 阵营图标 (场景 Army Icon 80x85)` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Premium Button Container | ⚠️ 未命中 |
| Premium Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Premium pruchased | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Points | ✅ `scripts\battle.gd:1759 # 敌方 QP 任务点 (原版 GO726 x[1816.1,1913.8] y[150.2,247.9] UI_Quest_Points + '0/3' 40.5px — 2026-08-21 审查; scrip` |
| Point Icon | ⚠️ 未命中 |
| Campaign Point Background | ⚠️ 未命中 |
| Army Icon | ✅ `scripts\campaign.gd:190 # 阵营图标 (原版 Army Icon); scripts\card_displayer.gd:489 # 阵营图标 (场景 Army Icon 80x85)` |
| Info Button | ⚠️ 未命中 |
| Campaign Track | ✅ `scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaign Header + Campaign Track); scripts\campaign.g` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Premium Panel | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Points | ✅ `scripts\battle.gd:1759 # 敌方 QP 任务点 (原版 GO726 x[1816.1,1913.8] y[150.2,247.9] UI_Quest_Points + '0/3' 40.5px — 2026-08-21 审查; scrip` |
| Quantity | ✅ `scripts\battle.gd:3203 # 奖励数 (RewardsHolder Quantity '2000': 胜利 2000 / 失败 0); scripts\ranked.gd:216 # 计数 (原版 Numer Of Army Decks [` |
| Points | ✅ `scripts\battle.gd:1759 # 敌方 QP 任务点 (原版 GO726 x[1816.1,1913.8] y[150.2,247.9] UI_Quest_Points + '0/3' 40.5px — 2026-08-21 审查; scrip` |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Generic Simplified UI Button | ✅ `scripts\two_sides_event.gd:386 # Collect 按钮 (原版 Generic Simplified UI Button)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Timer Text | ⚠️ 未命中 |
| Tutorial Message | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ⚠️ 未命中 |
| ChooseArmyText | ⚠️ 未命中 |
| Highlight Down | ⚠️ 未命中 |
| Highlight Up | ⚠️ 未命中 |

## 摘要

- 规格元素: 56
- 代码命中: 35
- ⚠️未命中: 21 (以下需人工判断)

- `Campaign Background`
- `Army Content`
- `Debug Point Button`
- `Premium Button Container`
- `Premium Button`
- `Premium pruchased`
- `Text (TMP)`
- `Point Icon`
- `Campaign Point Background`
- `Info Button`
- `Premium Panel`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Timer Text`
- `Tutorial Message`
- `Background fill`
- `ChooseArmyText`
- `Highlight Down`
- `Highlight Up`