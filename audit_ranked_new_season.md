# UI 规格审计: Ranked New Season WIndow

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:35
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Ranked New Season WIndow [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Back Background [godot(x-761.3 y-427.1 w3442.6 h1934.2)]
  Title [txt=NEW RANKED SEASON godot(x53.2 y0.0 w1813.6 h207.7)]
  Timer [godot(x211.5 y977.0 w1497.0 h103.0)]
    Timer Icon [godot(x179.2 y1047.7 w64.6 h64.6)]
    Timer [txt=Ends in: 23d 5h\n godot(x999.8 y977.0 w0.0 h103.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Ranked New Season WIndow | ⚠️ 未命中 |
| Back Background | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Timer | ✅ `scripts\battle.gd:4622 var _clock_timer: Timer = null; scripts\battle.gd:4641 _clock_timer = Timer.new()` |
| Timer Icon | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4622 var _clock_timer: Timer = null; scripts\battle.gd:4641 _clock_timer = Timer.new()` |

## 摘要

- 规格元素: 6
- 代码命中: 3
- ⚠️未命中: 3 (以下需人工判断)

- `Ranked New Season WIndow`
- `Back Background`
- `Timer Icon`