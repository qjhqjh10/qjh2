# UI 规格审计: Battle Log Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-24 19:56
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Battle Log Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Content [godot(x135.0 y55.0 w1650.0 h1000.0)]
    Background [godot(x135.0 y55.0 w1650.0 h1000.0)]
    Close Button [godot(x1685.0 y25.0 w130.0 h130.0)]
      Background [godot(x1699.5 y39.1 w99.1 h99.6)]
      Icon [godot(x1699.5 y39.1 w99.1 h99.6)]
    Matches [godot(x235.0 y130.0 w1475.0 h850.0)]
      Viewport [godot(x235.0 y130.0 w1475.0 h833.0)]
        Content [godot(x235.0 y130.0 w1475.0 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Battle Log Popup | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\ally_badge_drawer.gd:65 # 遮罩: 纯黑 ` |
| Content | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Close Button | ✅ `scripts\booster_info_popup.gd:197 # 关闭按钮 (原版 Generic Close Button Orange 三层; 权威 y181.3 — 修正仅 X 图标+159.8); scripts\collection.gd:78` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\ally_badge_drawe` |
| Matches | ✅ `scripts\player_profile.gd:801 # 记录列表区 (场景 Matches x326-1772 y163-905; 原版 Viewport y[162.8,887.5])` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:279 # 物品池 (原版 Re` |
| Content | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |

## 摘要

- 规格元素: 10
- 代码命中: 9
- ⚠️未命中: 1 (以下需人工判断)

- `Battle Log Popup`