# UI 规格审计: Deck Selector Card Info button

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 08:20
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Deck Selector Card Info button [godot(x0.4 y338.1 w0.0 h55.7)]
  Content [godot(x0.4 y338.1 w0.0 h55.7)]
    Background [godot(x0.4 y338.1 w0.0 h55.7)]
      Rarity Gradient [godot(x-0.0 y338.1 w0.4 h55.6)]
      Background Border [godot(x-15.9 y338.1 w16.3 h55.7)]
      Cost Image [godot(x0.2 y335.1 w0.0 h61.7)]
        Cost [txt=5 godot(x-24.2 y342.0 w48.8 h47.9)]
      banned Icon [godot(x-2.7 y332.0 w0.0 h61.7)]
      Text fill [godot(x0.4 y342.0 w-5.0 h47.9)]
        Card Name [txt=Card Name godot(x0.4 y389.9 w0.0 h0.0)]
        Count [txt=x2 godot(x0.4 y389.9 w0.0 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Deck Selector Card Info button | ✅ `scripts\deck_builder.gd:1420 ## 原版卡行 (Deck Selector Card Info button, 86px 行高): PnP 卡面缩略+渐变条+费用图标+卡名+数量; scripts\deck_builder.gd:1` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Rarity Gradient | ✅ `scripts\deck_builder.gd:1477 # 稀有度渐变条 (原版 Rarity Gradient anchor(0.606,0,1,1) 右 40% 区域稀有度着色); scripts\deck_builder.gd:1651 # 稀有度渐变` |
| Background Border | ✅ `scripts\deck_builder.gd:1469 # 卡行边框 (原版 Background Border 40k_deck_cardlist_border 四边线); scripts\deck_builder.gd:1643 # 边框 (原版 Bac` |
| Cost Image | ✅ `scripts\deck_builder.gd:1492 # 费用图标 (原版 Cost Image: Card Frame Cost Icon 左竖条 + 数字 50px); scripts\deck_builder.gd:1676 # 费用图标 (原版 C` |
| Cost | ✅ `scripts\battle.gd:434 # 实时数值层 (原版 2DCard Card Info: Cost/Health/Melee/Armour 文字实时更新 —; scripts\battle.gd:437 ["Cost", Vector3(0.28` |
| banned Icon | ✅ `scripts\deck_info_popup.gd:416 # banned Icon (原版 40k_Combat_Icon_Cross 卡被禁时显示 X — 2026-08-21 审查补; 数据无禁用标记 → 常隐)` |
| Text fill | ⚠️ 未命中 |
| Card Name | ✅ `scripts\deck_builder.gd:1514 # 卡名 + 类型/稀有度 (锚定左 112 右 70, 原版 Card Name 34px); scripts\deck_builder.gd:1709 # 卡名 (原版 Card Name 34px` |
| Count | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |

## 摘要

- 规格元素: 11
- 代码命中: 10
- ⚠️未命中: 1 (以下需人工判断)

- `Text fill`