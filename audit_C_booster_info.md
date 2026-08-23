# UI 规格审计: Booster Info Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Booster Info Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  window [godot(x395.7 y188.4 w1128.6 h663.2)]
    Generic Window Red Background Big [godot(x395.7 y178.4 w1151.6 h717.4)]
    Generic Close Button Orange [godot(x1487.1 y159.8 w74.4 h75.7)]
      Background [godot(x1495.2 y167.8 w56.9 h58.2)]
      Icon [godot(x1495.2 y167.8 w56.9 h58.2)]
    Artwork [godot(x395.7 y188.4 w564.3 h663.2)]
      background [godot(x405.7 y198.4 w544.3 h643.2)]
      foreground [godot(x395.7 y198.4 w564.3 h653.2)]
    Text [godot(x960.0 y204.4 w548.3 h631.2)]
      Title [txt=Necron Sautekh godot(x976.0 y260.6 w516.7 h52.0)]
      Category [txt=Legendary Booster Pack godot(x976.0 y307.9 w516.7 h45.0)]
      Descripton [txt=Contains 5 cards for the Sautekh army.\n\n godot(x976.0 y356.5 w500.0 h254.7)]
      CrateCounter [txt=Boosters opened since last Legendary  godot(x976.0 y619.7 w485.3 h45.0)]
      Booster pack guarantee Slider [godot(x1004.4 y664.6 w406.6 h50.0)]
        Background [godot(x1004.4 y674.6 w406.6 h30.0)]
          Fill Area [godot(x1004.4 y677.4 w406.6 h24.5)]
            Fill [godot(x1004.4 y701.9 w0.0 h0.0)]
              end [godot(x980.7 y687.0 w29.4 h31.9)]
        counter [txt=100/200 godot(x1085.7 y679.6 w244.0 h25.0)]
        Outline [godot(x1004.4 y674.6 w406.6 h30.0)]
        Tooltip [godot(x1411.0 y667.2 w44.9 h44.9)]
      Purchase buttons [godot(x947.3 y721.6 w520.8 h60.4)]
        Price Display [godot(x831.3 y746.5 w232.1 h71.0)]
          Generic UI Button [godot(x831.3 y746.5 w232.1 h71.0)]
            Button Text [inactive godot(x844.3 y772.7 w206.1 h18.6)]
            Price Display [godot(x840.0 y755.3 w212.8 h54.5)]
              icon [godot(x813.9 y809.8 w52.3 h0.0)]
              text [txt=300,00 godot(x926.5 y755.3 w92.2 h43.5)]
        WebShop Button [godot(x826.7 y756.0 w241.3 h51.9)]
          Highlight [sprite=OctagonUI Filled Fade SDF godot(x789.7 y717.4 w315.3 h129.1)]
          Button Image [godot(x826.7 y756.0 w241.3 h51.9)]
          Icon [godot(x795.6 y807.9 w62.3 h0.0)]
          Button Text [txt=Save More! godot(x912.5 y756.0 w132.0 h51.9)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Booster Info Popup | ✅ `scripts\booster_info_popup.gd:2 ## 卡包信息弹窗 (原版 Booster Info Popup [13378] 说明书):; scripts\packs.gd:120 # 保底信息按钮 (原版 Booster Info Pop` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| window | ✅ `scripts\achievements.gd:9 const TEX_TAB_HL := MNU + "40K_tab_button_overwindow.png"; scripts\battle.gd:901 func _art_window_tex(pa` |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:146 # 关闭按钮 (原版 Generic Close Button Orange); scripts\deck_info_popup.gd:212 # 关闭按钮 (原版 Generic Close` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Artwork | ✅ `scripts\booster_info_popup.gd:3 ##   window [396,188 1129x663] 红窗 + Artwork [396,188 564x663] 星空底 +; scripts\booster_info_popup.gd` |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| foreground | ⚠️ 未命中 |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Category | ✅ `scripts\booster_info_popup.gd:4 ##   Text [960,204 548x631] Title/Category/Description +` |
| Descripton | ⚠️ 未命中 |
| CrateCounter | ✅ `scripts\booster_info_popup.gd:5 ##   CrateCounter [976,620] 'Boosters opened since last Legendary...' +; scripts\booster_info_popu` |
| Booster pack guarantee Slider | ✅ `scripts\booster_info_popup.gd:6 ##   Booster pack guarantee Slider [1004,665 407x50] 保底进度条 (counter '100/200' + Tooltip)` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| end | ✅ `scripts\achievements.gd:1 extends Control; scripts\achievements.gd:32 ["upgrade_legendary", "Legendary Forger", "Upgrade 3 Legenda` |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| Outline | ⚠️ 未命中 |
| Tooltip | ✅ `scripts\booster_info_popup.gd:6 ##   Booster pack guarantee Slider [1004,665 407x50] 保底进度条 (counter '100/200' + Tooltip); scripts\` |
| Purchase buttons | ✅ `scripts\offer_popup.gd:117 # 购买按钮 (原版 Purchase buttons x842-1082 y685-759: 金币图标 + 价格)` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| WebShop Button | ✅ `scripts\shop.gd:602 # 右侧方钮 (原版 WebShop Button Square 在 name-bg 内 77.6×51.5: (248.6,331.2) — 2026-08-20 核查)` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Button Image | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |

## 摘要

- 规格元素: 35
- 代码命中: 30
- ⚠️未命中: 5 (以下需人工判断)

- `foreground`
- `Descripton`
- `Fill Area`
- `Outline`
- `Button Image`