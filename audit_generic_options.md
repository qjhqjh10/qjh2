# UI 规格审计: Generic Options Panel

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 17:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Generic Options Panel [godot(x766.3 y636.7 w387.4 h0.0)]
  Menu Dark Background [godot(x-1327.3 y-649.5 w4574.6 h2572.4)]
  bg shadow [godot(x733.9 y597.2 w450.5 h79.0)]
  bg [godot(x766.3 y636.7 w387.4 h0.0)]
  Name [txt=Pepito el de siempre godot(x588.8 y636.7 w355.0 h0.0)]
  Template [godot(x587.7 y636.7 w357.3 h0.0)]
    Button Text [txt=Template godot(x600.4 y636.7 w330.8 h0.0)]
  Buttons [godot(x766.3 y636.7 w0.0 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Generic Options Panel | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| bg shadow | ⚠️ 未命中 |
| bg | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Name | ✅ `scripts\battle.gd:57 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
| Template | ✅ `scripts\deck_info_popup.gd:581 _Toast("Template decks cannot be edited; create your own"); scripts\deck_info_popup.gd:591 _Toast("` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Buttons | ✅ `scripts\battle.gd:2087 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |

## 摘要

- 规格元素: 8
- 代码命中: 6
- ⚠️未命中: 2 (以下需人工判断)

- `Generic Options Panel`
- `bg shadow`