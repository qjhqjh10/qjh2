# UI 规格审计: Ranked Division Info

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:49
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Ranked Division Info [godot(x251.9 y213.1 w434.2 h694.4)]
  info [godot(x259.9 y144.5 w55.2 h55.2)]
  LeaderboardButton [godot(x323.5 y145.5 w291.0 h53.2)]
    Button Text [txt=Leaderboard godot(x336.9 y150.7 w263.3 h42.8)]
  Generic Window Red Background Small [godot(x251.9 y213.1 w434.2 h694.4)]
  Content [godot(x280.2 y230.0 w377.6 h622.8)]
    RankTitleBG [godot(x51.6 y852.8 w457.2 h0.0)]
      DivisionText [txt=Division V godot(x102.5 y822.8 w355.4 h60.0)]
    Timer [godot(x99.7 y852.8 w361.0 h0.0)]
      Timer Icon [godot(x83.2 y836.3 w33.0 h33.0)]
      Timer [txt=Ends in: 23d 5h godot(x215.8 y857.8 w167.7 h55.9)]
    DivisionImage [godot(x69.1 y852.8 w422.2 h0.0)]
      RankImage [godot(x238.0 y861.4 w84.4 h-8.6)]
    footer [godot(x75.2 y852.8 w410.0 h0.0)]
      Highest Faction Rating [inactive godot(x-102.5 y832.9 w355.4 h39.8)]
        Rating Text [godot(x-102.5 y843.1 w0.0 h59.2)]
          Secondary Icon [godot(x-102.5 y902.3 w0.0 h0.0)]
          Main Icon [godot(x-102.5 y902.3 w0.0 h0.0)]
          Individual rating value [txt=4879 godot(x-102.5 y902.3 w0.0 h0.0)]
      FactionScoreSmall [godot(x-102.5 y794.0 w355.4 h117.7)]
        icon [godot(x-104.8 y794.0 w180.0 h117.7)]
        Alliance Rating Display [godot(x56.5 y806.2 w196.4 h55.8)]
          Secondary Icon [inactive godot(x56.5 y806.2 w22.4 h29.8)]
          Main Icon [godot(x56.5 y862.0 w0.0 h0.0)]
          Individual rating value [txt=4879 godot(x56.5 y862.0 w0.0 h0.0)]
        Alliance Rating Display (1) [godot(x56.5 y862.4 w196.4 h36.4)]
          Secondary Icon [inactive godot(x56.5 y862.4 w22.4 h29.8)]
          Main Icon [godot(x56.5 y898.8 w0.0 h0.0)]
          Individual rating value [txt=5000 godot(x56.5 y898.8 w0.0 h0.0)]
      MainRating [inactive godot(x87.0 y981.7 w386.4 h60.3)]
        Mission Milestones Progress [inactive godot(x87.0 y968.6 w355.5 h86.5)]
          counter [inactive txt=16 godot(x91.3 y741.2 w80.0 h52.2)]
          steps [godot(x87.0 y968.6 w355.5 h86.5)]
            RankedSealStep [godot(x87.0 y938.5 w71.1 h60.3)]
              Empty [godot(x87.0 y938.5 w71.1 h60.3)]
              Fill [godot(x87.0 y938.5 w71.1 h60.3)]
        Global Rating [inactive godot(x186.0 y983.2 w256.5 h57.4)]
          Secondary Icon [godot(x230.5 y983.2 w40.0 h57.4)]
          Main Icon [godot(x270.5 y983.2 w60.0 h57.4)]
          Individual rating value [txt=2500 godot(x330.5 y983.2 w67.5 h57.4)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Ranked Division Info | ✅ `scripts\ranked.gd:2 ## 排位界面 (原版 Ranked Division Info + SearchingOpponentWindow 说明书); scripts\ranked.gd:71 # 段位面板 (原版 Ranked Divisi` |
| info | ✅ `scripts\base_event_popup.gd:56 img.texture = load(SPR + "40k_shop_popup_info_bg.png"); scripts\battle.gd:1453 var info := _make_la` |
| LeaderboardButton | ✅ `scripts\ranked.gd:81 # 排行榜按钮 (原版 LeaderboardButton [241,73 291x53], +62 → [303,73])` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Window Red Background Small | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| RankTitleBG | ⚠️ 未命中 |
| DivisionText | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Timer Icon | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| DivisionImage | ✅ `scripts\ranked.gd:115 # 段位图标 (原版 DivisionImage [2,768] RankImage 78²: Roman I-V 原版贴图); scripts\ranked.gd:468 var _division_icon: T` |
| RankImage | ✅ `scripts\ranked.gd:115 # 段位图标 (原版 DivisionImage [2,768] RankImage 78²: Roman I-V 原版贴图); scripts\ranked.gd:468 var _division_icon: T` |
| footer | ✅ `scripts\deck_builder.gd:466 var footer := Control.new(); scripts\deck_builder.gd:467 footer.custom_minimum_size = Vector2(0, 70)` |
| Highest Faction Rating | ⚠️ 未命中 |
| Rating Text | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| FactionScoreSmall | ✅ `scripts\player_profile.gd:1237 # AllFactions 右列 (x1303-1747): 'Faction Rating' 标题 + info 钮 + 滚动列表 (FactionScoreSmall 行); scripts\p` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| Alliance Rating Display | ✅ `scripts\player_profile.gd:1227 # Alliance Rating Display 行 (rank 图标 + 40px 数字); scripts\player_profile.gd:1362 # Alliance Rating D` |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Alliance Rating Display (1) | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| MainRating | ⚠️ 未命中 |
| Mission Milestones Progress | ⚠️ 未命中 |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| steps | ✅ `scripts\battle.gd:2290 var steps: Array = _tutorial_data.get(stage_key, {}).get("steps", []); scripts\battle.gd:2290 var steps: Ar` |
| RankedSealStep | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2511 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:426 var csb2 := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Global Rating | ✅ `scripts\player_profile.gd:1184 # 中央列 (584.4-953.7): 'Global Rating' 标题 + 段位图 04-Admiral + 主段位条; scripts\player_profile.gd:1185 var` |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |

## 摘要

- 规格元素: 40
- 代码命中: 22
- ⚠️未命中: 18 (以下需人工判断)

- `Generic Window Red Background Small`
- `RankTitleBG`
- `DivisionText`
- `Timer Icon`
- `Highest Faction Rating`
- `Rating Text`
- `Secondary Icon`
- `Individual rating value`
- `Secondary Icon`
- `Individual rating value`
- `Alliance Rating Display (1)`
- `Secondary Icon`
- `Individual rating value`
- `MainRating`
- `Mission Milestones Progress`
- `RankedSealStep`
- `Secondary Icon`
- `Individual rating value`