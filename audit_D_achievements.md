# UI 规格审计: Achievements Tab

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Achievements Tab [godot(x-0.5 y-1.7 w1920.5 h1081.7)]
  Scroll [godot(x199.0 y129.1 w1523.6 h928.0)]
    Viewport [godot(x199.0 y129.1 w1523.6 h911.0)]
      ContainerHolder [godot(x199.0 y129.1 w1523.6 h0.0)]
        Achievement Container [godot(x199.0 y54.1 w0.0 h150.0)]
          title [txt=Victorious 1/5 godot(x195.0 y75.1 w-5.0 h32.7)]
          description [txt=Upgrade Ultramarines cards to tier 2 godot(x195.0 y107.8 w-5.0 h48.4)]
          rewards [txt=2 points godot(x445.7 y156.2 w-255.7 h29.5)]
            rewardIcon [godot(x417.2 y151.4 w28.5 h39.1)]
          Progress [godot(x195.0 y156.2 w-143.3 h29.5)]
            Slider [godot(x195.0 y148.0 w-143.3 h43.6)]
              Background [godot(x195.0 y156.7 w-143.3 h26.2)]
                Fill Area [godot(x195.0 y158.6 w-143.3 h22.3)]
                  Fill [godot(x195.0 y180.9 w0.0 h0.0)]
                    end [godot(x171.3 y166.0 w29.4 h31.8)]
              counter [txt=100/200 godot(x166.4 y161.0 w-86.0 h21.9)]
              Outline [godot(x195.0 y156.7 w-143.3 h26.2)]
          Image [godot(x214.0 y64.1 w130.0 h130.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Achievements Tab | ✅ `scripts\achievements.gd:2 ## 成就界面 (原版 Achievements Tab 说明书: 类型筛选按钮 + Achievement Container 520x150 网格); scripts\quests.gd:193 # 成就` |
| Scroll | ✅ `scripts\achievements.gd:150 # 成就网格 (原版 Scroll [199,129 1524x928] + Achievement Container 520x150); scripts\achievements.gd:151 var` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| ContainerHolder | ⚠️ 未命中 |
| Achievement Container | ✅ `scripts\achievements.gd:2 ## 成就界面 (原版 Achievements Tab 说明书: 类型筛选按钮 + Achievement Container 520x150 网格); scripts\achievements.gd:15` |
| title | ✅ `scripts\achievements.gd:189 var title := str(a[1]); scripts\achievements.gd:226 # 标题 (原版 title)` |
| description | ✅ `scripts\achievements.gd:229 # 描述 (原版 description); scripts\battle.gd:468 # 名字/描述层 (原版 Name and description (0,-0.77) 1.3×0.68; 名字 ` |
| rewards | ✅ `scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter + rewards); scripts\campaign.gd:243 _open_node_rewards(i))` |
| rewardIcon | ⚠️ 未命中 |
| Progress | ✅ `scripts\deck_builder.gd:523 var bar := TextureProgressBar.new(); scripts\deck_builder.gd:565 (_cost_bars[i] as TextureProgressBar)` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| end | ✅ `scripts\achievements.gd:1 extends Control; scripts\achievements.gd:32 ["upgrade_legendary", "Legendary Forger", "Upgrade 3 Legenda` |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| Outline | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |

## 摘要

- 规格元素: 18
- 代码命中: 14
- ⚠️未命中: 4 (以下需人工判断)

- `ContainerHolder`
- `rewardIcon`
- `Fill Area`
- `Outline`