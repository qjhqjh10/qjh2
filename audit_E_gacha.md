# UI 规格审计: Gacha Tab

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Gacha Tab [godot(x163.8 y0.2 w1756.4 h1079.6)]
  Chest panel [godot(x56.8 y0.1 w1086.5 h1079.7)]
    Mask [godot(x59.3 y-7.3 w1081.5 h1198.5)]
      Background [godot(x-184.4 y-296.4 w1708.6 h1778.1)]
    Crate Shadow [godot(x162.0 y590.5 w753.5 h254.5)]
    Crate Shadow [godot(x103.0 y533.7 w622.1 h254.5)]
    Highlight Crate [sprite=Crate Border Highlight godot(x177.1 y163.1 w845.9 h753.7)]
    Crate [godot(x344.0 y283.9 w512.0 h512.0)]
    Price Display Button [godot(x385.4 y794.2 w429.3 h109.6)]
      Button Higlight border [godot(x341.1 y761.5 w514.9 h175.0)]
      Open Chest Button [godot(x385.4 y794.2 w429.3 h109.6)]
        Button Text [inactive godot(x398.4 y820.4 w403.3 h57.2)]
        Price Display [godot(x401.6 y807.7 w393.5 h84.2)]
          icon [godot(x353.3 y891.9 w96.7 h0.0)]
          text [txt=1 godot(x646.7 y807.7 w0.0 h80.6)]
    Video Player [godot(x550.0 y489.9 w100.0 h100.0)]
    Header [godot(x56.8 y0.1 w1086.5 h293.8)]
      Background [inactive godot(x56.8 y23.2 w1086.5 h176.0)]
      Title [txt=The Vault godot(x600.0 y41.9 w0.0 h138.2)]
        Help Icon Player [inactive godot(x619.9 y84.9 w52.1 h52.2)]
      Army Icon [inactive godot(x61.8 y57.0 w120.0 h120.0)]
      Time Remaining [txt=Ends in: godot(x600.0 y162.0 w0.0 h50.0)]
        Time image [sprite=WF_icon_clock for shader godot(x600.0 y162.2 w49.6 h49.6)]
        Time [txt=19d 15h godot(x652.4 y162.0 w110.3 h50.0)]
    Generic Simplified UI Button (1) [godot(x421.7 y940.7 w356.6 h58.5)]
      Button Text [txt=Where get cards godot(x434.2 y946.4 w331.3 h47.1)]
  Rewards Panel [godot(x1042.0 y-0.4 w878.2 h1080.2)]
    Background Border [godot(x1042.0 y-0.4 w878.2 h1080.2)]
    Background fill [sprite=40k_popup_texture godot(x1042.0 y-0.4 w878.2 h1080.2)]
    BackgroundTop [inactive godot(x1051.1 y8.8 w860.9 h1061.9)]
    Header [godot(x1051.1 y10.0 w858.6 h229.4)]
      Header Title [txt=Special Items godot(x1064.7 y10.1 w845.0 h229.3)]
      Reward Timer [txt=Ends in: godot(x1480.4 y161.4 w0.0 h51.0)]
        Time image [sprite=WF_icon_clock for shader godot(x1480.4 y162.2 w49.6 h49.5)]
        Time [txt=19d 15h godot(x1532.8 y161.4 w110.3 h50.0)]
    Rewards [godot(x1042.0 y239.4 w878.4 h569.7)]
      bg [godot(x1042.0 y239.4 w878.4 h569.7)]
      Viewport [godot(x1042.0 y239.4 w878.4 h569.7)]
        Content [godot(x1042.0 y269.4 w878.4 h509.7)]
          Gacha Drawer Holder [godot(x892.0 y779.1 w300.0 h0.0)]
            Gacha Reward Claimed (1) [godot(x901.9 y796.0 w225.6 h67.8)]
              Claimed Tex [txt=Claimed godot(x945.2 y810.7 w112.6 h38.4)]
    Footer [godot(x1042.0 y787.9 w878.4 h292.3)]
      Reward count [txt=2/5 godot(x1056.4 y815.0 w854.8 h87.0)]
      Player doesn't have all items [godot(x1174.2 y874.9 w614.0 h187.0)]
        Footer Text [txt=You’ll receive at least one Special Item godot(x1174.2 y974.4 w614.0 h72.0)]
        ProgressBar [godot(x1224.2 y904.6 w514.0 h62.5)]
          Background [godot(x1224.2 y917.1 w514.0 h37.5)]
            Fill Area [godot(x1224.2 y921.4 w514.0 h29.0)]
              Fill [godot(x1224.2 y950.4 w0.0 h0.0)]
                end [godot(x1192.2 y925.1 w39.9 h54.3)]
          Outline [godot(x1224.2 y917.1 w514.0 h37.5)]
          counter [txt=5/10 godot(x1327.0 y914.7 w308.4 h47.2)]
      Player has all items [inactive godot(x1052.0 y874.9 w858.4 h205.3)]
        Footer Text [txt=You've collected all the Special Items,  godot(x1052.0 y894.2 w858.4 h160.3)]
    Completed [inactive godot(x1042.0 y-0.4 w878.2 h1080.2)]
      Background [godot(x1042.0 y-0.4 w878.2 h1080.2)]
      Message container [godot(x1042.0 y217.2 w878.2 h645.5)]
        Background [godot(x1042.0 y387.9 w878.2 h303.8)]
        Complete Text Title [txt=Complete! godot(x1042.0 y387.9 w878.2 h302.1)]
        Complete Tex Info [txt=You have collected all the available Spe godot(x1042.0 y613.3 w878.2 h233.4)]
    Rewards [godot(x1042.0 y-0.4 w878.2 h1080.2)]
  Video Background [inactive godot(x-2986.3 y-1359.2 w8046.3 h3885.5)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Gacha Tab | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度)` |
| Chest panel | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Crate Shadow | ✅ `scripts\gacha.gd:168 # 宝箱下方辉光阴影 (原版 Crate Shadow ×2: 阴影1 x[162,915.6] 753.5宽 / 阴影2 x[103,725.1] 622.1宽)` |
| Crate Shadow | ✅ `scripts\gacha.gd:168 # 宝箱下方辉光阴影 (原版 Crate Shadow ×2: 阴影1 x[162,915.6] 753.5宽 / 阴影2 x[103,725.1] 622.1宽)` |
| Highlight Crate | ✅ `scripts\gacha.gd:180 # 宝箱高亮光晕 (说明书 Highlight Crate [177,163 846x754])` |
| Crate | ✅ `scripts\battle.gd:617 # 装饰扩展: 箱堆两侧 (说明书 Crates 4/Crates 18 左侧近场, 镜像右侧); scripts\battle.gd:617 # 装饰扩展: 箱堆两侧 (说明书 Crates 4/Crates 18` |
| Price Display Button | ✅ `scripts\gacha.gd:216 # 开箱价格按钮 (说明书 Price Display Button [385,794 429x110]: Open Chest Button + 门票 icon + '1'); scripts\packs.gd:23` |
| Button Higlight border | ⚠️ 未命中 |
| Open Chest Button | ✅ `scripts\gacha.gd:216 # 开箱价格按钮 (说明书 Price Display Button [385,794 429x110]: Open Chest Button + 门票 icon + '1')` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Video Player | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Help Icon Player | ⚠️ 未命中 |
| Army Icon | ✅ `scripts\campaign.gd:190 # 阵营图标 (原版 Army Icon); scripts\card_displayer.gd:489 # 阵营图标 (场景 Army Icon 80x85)` |
| Time Remaining | ✅ `scripts\gacha.gd:202 # Header (说明书 [57,0 1086x294]: Title 'The Vault' + Time Remaining)` |
| Time image | ⚠️ 未命中 |
| Time | ✅ `scripts\battle.gd:1392 var now := Time.get_ticks_msec(); scripts\battle.gd:3320 "date": Time.get_date_string_from_system(),` |
| Generic Simplified UI Button (1) | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Rewards Panel | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Background Border | ✅ `scripts\deck_builder.gd:1471 # 卡行边框 (原版 Background Border 40k_deck_cardlist_border 11x11 m_Border=(5,5,5,5) 四边线 9-slice); scripts\` |
| Background fill | ⚠️ 未命中 |
| BackgroundTop | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Header Title | ⚠️ 未命中 |
| Reward Timer | ⚠️ 未命中 |
| Time image | ⚠️ 未命中 |
| Time | ✅ `scripts\battle.gd:1392 var now := Time.get_ticks_msec(); scripts\battle.gd:3320 "date": Time.get_date_string_from_system(),` |
| Rewards | ✅ `scripts\battle.gd:3141 # 统计 (原版 AllRewardsHolder: 骷髅 + 奖励); scripts\battle.gd:3161 # 底部奖励条 (原版 EndBattlePanel → AllRewardsHolder, ` |
| bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\achievements.gd:198 var bg :=` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Gacha Drawer Holder | ✅ `scripts\gacha.gd:288 # 物品池 (原版 Rewards Viewport [1042,239 878x570] → 5 个 Gacha Drawer Holder 300 宽横排可滚动); scripts\gacha.gd:383 ## ` |
| Gacha Reward Claimed (1) | ⚠️ 未命中 |
| Claimed Tex | ⚠️ 未命中 |
| Footer | ✅ `scripts\deck_builder.gd:464 # 底部 Footer (原版 [0,1010 335x70]: Done [12.8..201.3, 9.3..59.5] 188.5x50.2 + 卡数图标 [201.3..251.3] 50x4; ` |
| Reward count | ⚠️ 未命中 |
| Player doesn't have all items | ⚠️ 未命中 |
| Footer Text | ⚠️ 未命中 |
| ProgressBar | ✅ `scripts\deck_builder.gd:523 var bar := TextureProgressBar.new(); scripts\deck_builder.gd:565 (_cost_bars[i] as TextureProgressBar)` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| end | ✅ `scripts\achievements.gd:1 extends Control; scripts\achievements.gd:32 ["upgrade_legendary", "Legendary Forger", "Upgrade 3 Legenda` |
| Outline | ⚠️ 未命中 |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| Player has all items | ⚠️ 未命中 |
| Footer Text | ⚠️ 未命中 |
| Completed | ✅ `scripts\battle.gd:2987 # 教程胜利 → 记录完成关卡 (tutorial.gd 'Completed: N/6' 数据源; 2026-08-21); scripts\battle.gd:3245 ## tutorial.gd 读取显示 ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Message container | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Complete Text Title | ⚠️ 未命中 |
| Complete Tex Info | ⚠️ 未命中 |
| Rewards | ✅ `scripts\battle.gd:3141 # 统计 (原版 AllRewardsHolder: 骷髅 + 奖励); scripts\battle.gd:3161 # 底部奖励条 (原版 EndBattlePanel → AllRewardsHolder, ` |
| Video Background | ⚠️ 未命中 |

## 摘要

- 规格元素: 63
- 代码命中: 40
- ⚠️未命中: 23 (以下需人工判断)

- `Button Higlight border`
- `Video Player`
- `Help Icon Player`
- `Time image`
- `Generic Simplified UI Button (1)`
- `Background fill`
- `BackgroundTop`
- `Header Title`
- `Reward Timer`
- `Time image`
- `Gacha Reward Claimed (1)`
- `Claimed Tex`
- `Reward count`
- `Player doesn't have all items`
- `Footer Text`
- `Fill Area`
- `Outline`
- `Player has all items`
- `Footer Text`
- `Message container`
- `Complete Text Title`
- `Complete Tex Info`
- `Video Background`