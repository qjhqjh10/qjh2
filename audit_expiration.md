# UI 规格审计: Base Expiration Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:12
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Base Expiration Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Generic Window Red Background Big [godot(x442.6 y146.3 w1052.8 h733.4)]
  Event image [godot(x281.6 y34.1 w858.8 h858.8)]
  Texts [godot(x1005.0 y190.0 w450.0 h580.0)]
    TitleText [txt=Welcome to Warpforge! godot(x1005.0 y190.0 w450.0 h105.0)]
    DescriptionText [txt=War rages across the stars. Ancient civi godot(x1025.0 y308.6 w410.0 h425.0)]
    Tap To continue [txt=Clique para continuar godot(x1005.0 y730.4 w450.0 h79.2)]
  Collider [godot(x0.0 y0.0 w1920.0 h1080.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Base Expiration Popup | ✅ `scripts\expiration_popup.gd:2 ## 通用过期弹窗 (原版 Base Expiration Popup [3282] 说明书):; scripts\quests.gd:35 const EXPIRATION_POPUP := pre` |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Event image | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Texts | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| TitleText | ✅ `scripts\expiration_popup.gd:5 ##   Texts [1005,190 450x580]: TitleText 34px 白 / DescriptionText 28px 白 / 'Click to continue' 30px ` |
| DescriptionText | ✅ `scripts\expiration_popup.gd:5 ##   Texts [1005,190 450x580]: TitleText 34px 白 / DescriptionText 28px 白 / 'Click to continue' 30px ` |
| Tap To continue | ⚠️ 未命中 |
| Collider | ✅ `scripts\base_event_popup.gd:5 ##   Collider 全屏按钮 (点击继续); scripts\base_event_popup.gd:25 # 全屏 Collider 按钮 (点击继续/关闭)` |

## 摘要

- 规格元素: 9
- 代码命中: 8
- ⚠️未命中: 1 (以下需人工判断)

- `Tap To continue`