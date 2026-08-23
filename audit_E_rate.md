# UI 规格审计: Rate Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Rate Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Background [godot(x-500.0 y0.0 w2920.0 h1080.0)]
  Generic Window Red Background Big [godot(x442.6 y146.3 w1052.8 h733.4)]
  Event image [godot(x281.6 y36.6 w858.8 h858.8)]
  Texts [godot(x1005.0 y190.0 w450.0 h580.0)]
    TitleText [inactive txt=Welcome to Warpforge! godot(x1005.0 y190.0 w450.0 h105.0)]
    DescriptionText [txt=Please share your thoughts before enteri godot(x1025.0 y293.5 w410.0 h324.0)]
  Buttons [godot(x1002.4 y621.0 w453.2 h90.0)]
    Generic Simplified UI Button_updated [godot(x897.4 y677.2 w210.0 h67.6)]
      Button Text [txt=1-4 stars godot(x907.8 y683.8 w188.4 h54.4)]
    Generic Simplified UI Button_updated (1) [godot(x897.4 y677.2 w210.0 h67.6)]
      Button Text [txt=5 stars godot(x907.8 y683.8 w188.4 h54.4)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Rate Popup | ✅ `scripts\rate_popup.gd:2 ## 评分弹窗 (原版 Rate Popup [11603] 说明书):; scripts\settings.gd:417 # 反馈问卷 + 评分 (原版 Give Feedback Popup [8609] /` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Event image | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Texts | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| TitleText | ⚠️ 未命中 |
| DescriptionText | ⚠️ 未命中 |
| Buttons | ✅ `scripts\battle.gd:2048 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Generic Simplified UI Button_updated | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Simplified UI Button_updated (1) | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |

## 摘要

- 规格元素: 12
- 代码命中: 8
- ⚠️未命中: 4 (以下需人工判断)

- `TitleText`
- `DescriptionText`
- `Generic Simplified UI Button_updated`
- `Generic Simplified UI Button_updated (1)`