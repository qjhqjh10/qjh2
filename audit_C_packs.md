# UI 规格审计: Packs Tab

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Packs Tab [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Packs Scroll View [godot(x163.5 y0.0 w1756.5 h1080.0)]
    Scrollbar Horizontal [inactive godot(x337.2 y1059.4 w1247.3 h5.5)]
      Sliding Area [godot(x337.1 y1051.3 w1247.5 h21.6)]
        Handle [godot(x337.1 y1051.3 w1247.5 h21.6)]
      Arrow Right 1 [godot(x1584.5 y1043.8 w36.5 h36.7)]
      Arrow Right 2 [godot(x1575.1 y1043.8 w36.5 h36.7)]
      Arrow Left 1 [godot(x300.6 y1043.8 w36.6 h36.7)]
      Arrow Left 1 2 [godot(x310.6 y1043.8 w36.6 h36.7)]
    Viewport [godot(x163.5 y0.0 w1756.5 h1080.0)]
      Content [godot(x163.5 y20.0 w103.0 h1060.0)]
    Empty Collection Warning [inactive godot(x-1.5 y-85.0 w1971.5 h1165.0)]
      Warning [txt=There are no deck in your collection for godot(x-1.5 y-85.0 w1971.5 h1165.0)]
  Header [inactive godot(x0.0 y0.0 w1920.0 h85.0)]
    Line [godot(x0.0 y80.0 w1920.0 h10.0)]
  Empty Collection Warning [inactive godot(x-77.6 y1026.2 w96.7 h106.2)]
    Warning [txt=There are no deck in your collection for godot(x-77.6 y1026.2 w96.7 h106.2)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Packs Tab | ✅ `scripts\packs.gd:2 ## 卡包开包界面 (原版 Packs Tab 说明书: 横向滚动卡包列表 + Card Drawer 开包展示); scripts\packs.gd:100 # 原版 Packs Tab Header (y[0,85] ` |
| Packs Scroll View | ✅ `scripts\packs.gd:162 # 横向滚动卡包列表 (原版 Packs Scroll View x[163.5,1920] y[0,1080] 全高, pack 行垂直居中); scripts\shop.gd:234 # 原版 Packs Scro` |
| Scrollbar Horizontal | ⚠️ 未命中 |
| Sliding Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Arrow Right 1 | ⚠️ 未命中 |
| Arrow Right 2 | ⚠️ 未命中 |
| Arrow Left 1 | ⚠️ 未命中 |
| Arrow Left 1 2 | ⚠️ 未命中 |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Line | ✅ `scripts\battle.gd:106 var _drag_line: Line2D = null      # 攻击拖线 (近战红 / 远程紫 / 技能金); scripts\battle.gd:3715 # 准星 (原版 Attack Target R` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |

## 摘要

- 规格元素: 17
- 代码命中: 11
- ⚠️未命中: 6 (以下需人工判断)

- `Scrollbar Horizontal`
- `Sliding Area`
- `Arrow Right 1`
- `Arrow Right 2`
- `Arrow Left 1`
- `Arrow Left 1 2`