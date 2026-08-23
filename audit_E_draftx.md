# UI 规格审计: Draft Mode Expiring Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Draft Mode Expiring Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Content [godot(x328.8 y156.6 w1262.4 h723.9)]
    Generic Window Red Background Big [godot(x328.8 y156.6 w1262.4 h723.9)]
    Warlord Image [godot(x70.3 y-32.4 w940.8 h940.8)]
    Game Mode Title [txt=The Space Marine event has finished! godot(x892.0 y247.6 w650.0 h56.8)]
    subtitle [txt=Alliance Name godot(x1017.0 y304.4 w400.0 h34.2)]
    Alliance Content [godot(x1017.0 y351.6 w400.0 h44.9)]
      Alliance Name [txt=Alliance Name: godot(x917.0 y371.5 w200.0 h50.0)]
      Alliance Skull Count [godot(x945.0 y373.3 w144.0 h46.3)]
        Secondary Icon [inactive godot(x945.0 y373.3 w44.4 h59.2)]
        Main Icon [godot(x945.0 y419.6 w0.0 h0.0)]
        Individual rating value [txt=3400 godot(x945.0 y419.6 w0.0 h0.0)]
    Victories text [inactive txt=Victories: godot(x1042.1 y366.8 w218.6 h43.5)]
      Victories text Number [txt=9\n godot(x1267.7 y343.9 w140.8 h89.3)]
    Crate Image [godot(x1009.1 y389.6 w407.9 h407.9)]
      x10 text [txt=x10 godot(x1363.4 y691.6 w103.9 h41.7)]
    Generic Simplified UI Button_updated [godot(x821.4 y759.2 w277.2 h53.7)]
      Button Text [txt=Leaderboard godot(x834.3 y764.5 w250.5 h43.1)]
  Tap To Continue [txt=Tap to continue godot(x-0.1 y922.7 w1920.2 h94.6)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Draft Mode Expiring Popup | ✅ `scripts\draft.gd:908 # 满 12 胜或 3 败: 轮抽结束弹窗 (原版 Draft Mode Expiring Popup [11847]); scripts\draft_expiring_popup.gd:2 ## 轮抽模式结束弹窗 (` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Warlord Image | ✅ `scripts\deck_info_popup.gd:79 # 督军立绘 (原版 Warlord Image 1108x1108, pivot(0.5,0) 原始 JSON RectTransform_8411164374367242664:; scripts` |
| Game Mode Title | ✅ `scripts\draft_expiring_popup.gd:4 ##   Game Mode Title 'The Space Marine event has finished!' +; scripts\draft_expiring_popup.gd:6` |
| subtitle | ✅ `scripts\card_displayer.gd:198 ## 数据: 卡数据无独立 lore 字段 → 用长描述 desc + 副标题 subtitle 组合 (原版 LoreText 展示背景故事); scripts\card_displayer.gd:` |
| Alliance Content | ⚠️ 未命中 |
| Alliance Name | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Alliance Skull Count | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +` |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Victories text | ⚠️ 未命中 |
| Victories text Number | ⚠️ 未命中 |
| Crate Image | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| x10 text | ⚠️ 未命中 |
| Generic Simplified UI Button_updated | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Tap To Continue | ⚠️ 未命中 |

## 摘要

- 规格元素: 20
- 代码命中: 12
- ⚠️未命中: 8 (以下需人工判断)

- `Alliance Content`
- `Secondary Icon`
- `Individual rating value`
- `Victories text`
- `Victories text Number`
- `x10 text`
- `Generic Simplified UI Button_updated`
- `Tap To Continue`