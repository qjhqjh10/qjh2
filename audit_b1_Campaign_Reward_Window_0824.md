# UI 规格审计: Campaign Reward Window

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-24 19:56
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Campaign Reward Window [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Content [godot(x0.0 y165.0 w1920.0 h800.0)]
    Reward Background Get Reward [inactive godot(x0.0 y165.0 w1920.0 h800.0)]
    Reward Background Preview Reward [godot(x0.0 y165.0 w1920.0 h800.0)]
    Scroll View [godot(x0.0 y285.0 w1920.0 h650.0)]
      Viewport [godot(x0.0 y285.0 w1920.0 h650.0)]
        Content [godot(x0.0 y285.0 w1920.0 h650.0)]
          Base Rewards [godot(x0.0 y285.0 w960.0 h650.0)]
            Rewards [godot(x895.0 y295.0 w0.0 h615.0)]
              Unlock Button [godot(x772.5 y850.0 w245.0 h45.0)]
                Icon Campaign Points Drawer Variant [inactive godot(x827.5 y838.8 w67.5 h67.4)]
                  Content [godot(x861.2 y872.5 w0.0 h0.0)]
                    Campaign Glow [godot(x861.2 y872.5 w0.0 h0.0)]
                    Image [godot(x861.2 y872.5 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x861.2 y872.5 w0.0 h0.0)]
                      Price Display [godot(x861.2 y872.5 w0.0 h0.0)]
                        icon [godot(x861.2 y872.5 w0.0 h0.0)]
                        text [txt=2000 godot(x861.2 y872.5 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x861.2 y872.5 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x861.2 y872.5 w0.0 h0.0)]
                      Price Display [godot(x861.2 y872.5 w0.0 h0.0)]
                        icon [godot(x861.2 y872.5 w0.0 h0.0)]
                        text [txt=24 hours godot(x861.2 y872.5 w0.0 h0.0)]
                Point Count [inactive txt=100 godot(x900.0 y857.2 w117.5 h30.6)]
                Claimed Text [txt=Change Deck godot(x772.5 y895.0 w0.0 h0.0)]
          Premium Rewards [godot(x960.0 y285.0 w960.0 h650.0)]
            Rewards [godot(x1025.0 y295.0 w0.0 h615.0)]
              Unlock Button [godot(x902.5 y850.0 w245.0 h45.0)]
                Icon Campaign Points Drawer Variant [inactive godot(x957.5 y838.8 w67.5 h67.4)]
                  Content [godot(x991.2 y872.5 w0.0 h0.0)]
                    Campaign Glow [godot(x991.2 y872.5 w0.0 h0.0)]
                    Image [godot(x991.2 y872.5 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x991.2 y872.5 w0.0 h0.0)]
                      Price Display [godot(x991.2 y872.5 w0.0 h0.0)]
                        icon [godot(x991.2 y872.5 w0.0 h0.0)]
                        text [txt=2000 godot(x991.2 y872.5 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x991.2 y872.5 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x991.2 y872.5 w0.0 h0.0)]
                      Price Display [godot(x991.2 y872.5 w0.0 h0.0)]
                        icon [godot(x991.2 y872.5 w0.0 h0.0)]
                        text [txt=24 hours godot(x991.2 y872.5 w0.0 h0.0)]
                Point Count [inactive txt=100 godot(x1030.0 y857.2 w117.5 h30.6)]
                Claimed Text [txt=Change Deck godot(x902.5 y895.0 w0.0 h0.0)]
              Warning [inactive txt=Warning or Tip godot(x1010.0 y850.0 w30.0 h45.0)]
              Badge [sprite=40k_campaign_Premium-icon godot(x1025.0 y295.0 w100.0 h100.0)]
    Title [godot(x660.0 y193.3 w600.0 h75.0)]
      Glow Get reward [inactive godot(x660.0 y187.4 w600.0 h75.0)]
        Text Get Reward [txt=Campaign Rewards godot(x660.0 y187.4 w600.0 h75.0)]
      Glow Preview reward [godot(x660.0 y187.4 w600.0 h75.0)]
        Text Preview Reward [txt=Available rewards godot(x660.0 y187.4 w600.0 h75.0)]
    Tap To Continue [inactive txt=Click to continue godot(x576.0 y965.0 w768.0 h80.0)]
  Menu Vignette [godot(x0.0 y0.0 w1920.0 h1080.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Campaign Reward Window | ✅ `scripts\campaign.gd:5 ## + Premium Mark + Border Thick Circle FX 可领光圈 + Node Line 连线) + 奖励弹窗 Campaign Reward Window; scripts\campa` |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\ally_badge_drawer.gd:65 # 遮罩: 纯黑 ` |
| Content | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |
| Reward Background Get Reward | ⚠️ 未命中 |
| Reward Background Preview Reward | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:279 # 物品池 (原版 Re` |
| Content | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |
| Base Rewards | ✅ `scripts\campaign.gd:435 # 左栏 Base Rewards [0,285 960x650] (原版 Scroll 区)` |
| Rewards | ✅ `scripts\ally_badge_drawer.gd:5 ##   Background 40k_Rewards_icon_base card (328x498 m_Border=0 → 直接拉伸); scripts\ally_badge_drawer.g` |
| Unlock Button | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |
| Campaign Glow | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\card_displayer.gd:33 const UPGRADE_GOLD := 2000   # 升级金币费用 (原版 UpgradePanel Converted Drawer 价格 '2000'); scripts\drawer.gd` |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ✅ `scripts\ally_badge_drawer.gd:10 ##   Converted/Ephemeral Drawer + Collected Badge = 商店变体条 (原版 m_IsActive=false 运行时开关; 本选择器不用); scr` |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| Point Count | ⚠️ 未命中 |
| Claimed Text | ⚠️ 未命中 |
| Premium Rewards | ✅ `scripts\campaign.gd:437 # 右栏 Premium Rewards [960,285 960x650] (单机版锁定); scripts\campaign.gd:438 _build_reward_panel(layer, "Premiu` |
| Rewards | ✅ `scripts\ally_badge_drawer.gd:5 ##   Background 40k_Rewards_icon_base card (328x498 m_Border=0 → 直接拉伸); scripts\ally_badge_drawer.g` |
| Unlock Button | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |
| Campaign Glow | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\card_displayer.gd:33 const UPGRADE_GOLD := 2000   # 升级金币费用 (原版 UpgradePanel Converted Drawer 价格 '2000'); scripts\drawer.gd` |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ✅ `scripts\ally_badge_drawer.gd:10 ##   Converted/Ephemeral Drawer + Collected Badge = 商店变体条 (原版 m_IsActive=false 运行时开关; 本选择器不用); scr` |
| Price Display | ✅ `scripts\booster_info_popup.gd:150 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| Point Count | ⚠️ 未命中 |
| Claimed Text | ⚠️ 未命中 |
| Warning | ✅ `scripts\card_displayer.gd:447 # 内容组 (原版 UpgradePanel.content; 满级切 No Upgrade Warning); scripts\card_displayer.gd:503 # 满级警告层 (原版 N` |
| Badge | ✅ `scripts\ally_badge_drawer.gd:2 ## 联盟徽章选择抽屉 (原版 "Alliance Badge Drawer" [0,0 1920x1080] Content [604,0 712x1080] —; scripts\ally_ba` |
| Title | ✅ `scripts\ally_badge_drawer.gd:90 title.name = "Title"; scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [100` |
| Glow Get reward | ⚠️ 未命中 |
| Text Get Reward | ⚠️ 未命中 |
| Glow Preview reward | ⚠️ 未命中 |
| Text Preview Reward | ⚠️ 未命中 |
| Tap To Continue | ✅ `scripts\season_banner_popup.gd:44 const R_TAP_ENDED := Rect2(-0.1, 985.5, 1920.2, 94.5)  # Tap To Continue (Season Ended); scripts` |
| Menu Vignette | ✅ `scripts\menu_bg.gd:4 ## 还原依据: 菜单全树.md — 各二级界面根下均挂 Menu Dark Background [-1327,-746 4575x2572] + 专属背景 + Noise + Menu Vigne` |

## 摘要

- 规格元素: 53
- 代码命中: 35
- ⚠️未命中: 18 (以下需人工判断)

- `Reward Background Get Reward`
- `Reward Background Preview Reward`
- `Unlock Button`
- `Icon Campaign Points Drawer Variant`
- `Campaign Glow`
- `AlreadyOwned`
- `Point Count`
- `Claimed Text`
- `Unlock Button`
- `Icon Campaign Points Drawer Variant`
- `Campaign Glow`
- `AlreadyOwned`
- `Point Count`
- `Claimed Text`
- `Glow Get reward`
- `Text Get Reward`
- `Glow Preview reward`
- `Text Preview Reward`