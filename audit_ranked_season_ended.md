# UI 规格审计: Ranked Season Ended Window

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:35
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Ranked Season Ended Window [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Division Image [godot(x582.5 y266.1 w755.0 h755.0)]
    Rank Icon [godot(x923.8 y489.9 w73.6 h73.6)]
  Title [txt=SEASON ENDED! godot(x53.2 y0.0 w1813.6 h111.5)]
  Percentage Or Score text [txt=You are in the top {0}% of players. godot(x-0.1 y200.2 w1920.2 h65.9)]
  Tap To Continue [txt=Click to continue godot(x-0.1 y985.5 w1920.2 h94.5)]
  Glow below [godot(x-11541.0 y-11907.0 w25000.0 h25000.0)]
  Rank Points [godot(x237.8 y100.2 w1444.4 h100.0)]
    Ranking Points Title [txt=Rating: godot(x797.9 y110.5 w119.4 h79.3)]
    GameMode Icon [godot(x187.8 y150.2 w100.0 h100.0)]
    Ranking Points Quantity Text [txt=12153 godot(x1017.3 y110.5 w104.8 h79.3)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Ranked Season Ended Window | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Division Image | ⚠️ 未命中 |
| Rank Icon | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Percentage Or Score text | ⚠️ 未命中 |
| Tap To Continue | ⚠️ 未命中 |
| Glow below | ⚠️ 未命中 |
| Rank Points | ⚠️ 未命中 |
| Ranking Points Title | ⚠️ 未命中 |
| GameMode Icon | ⚠️ 未命中 |
| Ranking Points Quantity Text | ⚠️ 未命中 |

## 摘要

- 规格元素: 12
- 代码命中: 2
- ⚠️未命中: 10 (以下需人工判断)

- `Ranked Season Ended Window`
- `Division Image`
- `Rank Icon`
- `Percentage Or Score text`
- `Tap To Continue`
- `Glow below`
- `Rank Points`
- `Ranking Points Title`
- `GameMode Icon`
- `Ranking Points Quantity Text`