# UI 规格审计: PlayerRankingRow

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 18:23
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
PlayerRankingRow [godot(x0.0 y1030.0 w1920.0 h100.0)]
  Background [godot(x0.0 y1026.8 w1920.0 h106.4)]
  BackgroundHighlight [godot(x0.0 y1026.8 w1920.0 h106.4)]
  Ranking [txt=1 godot(x12.0 y1044.0 w100.0 h72.0)]
  border [godot(x135.0 y1031.0 w120.0 h106.4)]
    Icon [godot(x81.2 y989.6 w204.6 h167.2)]
  Name Holder [godot(x290.0 y1030.0 w734.0 h100.0)]
    Name [txt=Lorem Ipsum godot(x-65.4 y1130.0 w710.8 h0.0)]
    Guild Name [txt=Bando del Ventris godot(x-65.4 y1130.0 w710.8 h0.0)]
  RankingIcon [godot(x1661.7 y998.9 w108.3 h165.6)]
  Points [txt=4500 godot(x1780.0 y1041.3 w140.0 h77.9)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| PlayerRankingRow | ✅ `scripts\draft_leaderboard_popup.gd:8 ##   Content [249,147.6 1422x790.2] 排行列表 (PlayerRankingRow 行高 100 间距 15); scripts\draft_leade` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| BackgroundHighlight | ✅ `scripts\draft_leaderboard_popup.gd:264 # 行背景 (原版 Background color(0.83,0.19,0.43,0.16) + 自排名行 BackgroundHighlight` |
| Ranking | ✅ `scripts\draft_leaderboard_popup.gd:5 ##   Ranking Display [202.4,16.3 1515.2x990.6]: Generic Window Red Background Big; scripts\dr` |
| border | ✅ `scripts\battle.gd:1243 sb.set_border_width_all(4); scripts\battle.gd:1244 sb.border_color = Color("e8c76a")` |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1886 #` |
| Name Holder | ✅ `scripts\draft_leaderboard_popup.gd:315 # 玩家名 (原版 Name Holder (290,0) 734x100 40px 白)` |
| Name | ✅ `scripts\battle.gd:57 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
| Guild Name | ⚠️ 未命中 |
| RankingIcon | ✅ `scripts\draft_leaderboard_popup.gd:327 # 骷髅印章 (原版 RankingIcon 槽位 (990,4.1) 60x91.8; Rank Skull 印章资源)` |
| Points | ✅ `scripts\battle.gd:1797 # 敌方 QP 任务点 (原版 GO726 x[1816.1,1913.8] y[150.2,247.9] UI_Quest_Points + '0/3' 40.5px — 2026-08-21 审查; scrip` |

## 摘要

- 规格元素: 11
- 代码命中: 10
- ⚠️未命中: 1 (以下需人工判断)

- `Guild Name`