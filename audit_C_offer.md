# UI 规格审计: Base Offer Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Base Offer Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  window [godot(x395.7 y188.4 w1128.6 h663.2)]
    Generic Window Red Background Big [godot(x395.7 y178.4 w1151.6 h717.4)]
    Generic Close Button Orange [godot(x1487.1 y159.8 w74.4 h75.7)]
      Background [godot(x1495.2 y167.8 w56.9 h58.2)]
      Icon [godot(x1495.2 y167.8 w56.9 h58.2)]
    Artwork [godot(x395.7 y188.4 w564.3 h663.2)]
      background [godot(x405.7 y198.4 w544.3 h643.2)]
      foreground [godot(x395.7 y218.4 w564.3 h643.2)]
    Text [godot(x960.0 y204.4 w548.3 h631.2)]
      Title [txt=Necron Sautekh godot(x976.0 y260.6 w516.7 h52.0)]
      Category [txt=Legendary Booster Pack godot(x976.0 y307.9 w516.7 h45.0)]
      Descripton [txt=Contains 5 cards for the Sautekh army.\n\n godot(x976.0 y356.6 w501.2 h315.5)]
      Available Counter [txt=Available: 1/5 godot(x422.0 y282.8 w308.0 h31.6)]
      Timer [godot(x1103.0 y766.5 w197.6 h26.7)]
        Icon [godot(x1103.0 y778.2 w0.0 h30.0)]
        Timer Text [txt=23h 34m godot(x1103.0 y793.2 w0.0 h25.0)]
      Offer Badge [godot(x403.5 y217.4 w406.0 h78.8)]
        Text (TMP) [txt=+60% value godot(x419.5 y233.4 w379.2 h46.8)]
      Purchase buttons [godot(x975.0 y701.9 w501.2 h60.4)]
        Price Display [godot(x855.2 y725.5 w239.6 h73.5)]
          Generic UI Button [godot(x855.2 y725.5 w239.6 h73.5)]
            Button Text [inactive godot(x868.2 y751.7 w213.6 h21.2)]
            Price Display [godot(x864.2 y734.6 w219.7 h56.5)]
              icon [godot(x911.8 y730.1 w0.0 h54.0)]
              text [txt=300,00 godot(x938.8 y734.6 w124.5 h45.0)]
          Offer Price Discount Badge [godot(x807.5 y626.3 w0.0 h179.0)]
            Discount Title [txt=Previous Price godot(x807.3 y668.4 w0.1 h53.4)]
            Discount Price [txt=$19.99 godot(x807.7 y721.8 w-0.1 h37.0)]
        WebShop Button [godot(x854.4 y736.3 w241.2 h51.9)]
          Highlight [sprite=OctagonUI Filled Fade SDF godot(x817.4 y697.7 w315.2 h129.1)]
          Button Image [godot(x854.4 y736.3 w241.2 h51.9)]
          Icon [godot(x909.0 y731.2 w0.0 h62.2)]
          Button Text [txt=Save More! godot(x940.1 y736.3 w132.0 h51.9)]
  Preview [godot(x422.0 y795.0 w170.0 h50.0)]
    Button Text [txt=Preview godot(x431.0 y799.9 w151.4 h40.2)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Base Offer Popup | ⚠️ 未命中 |
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
| Available Counter | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Timer Text | ⚠️ 未命中 |
| Offer Badge | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Purchase buttons | ✅ `scripts\offer_popup.gd:117 # 购买按钮 (原版 Purchase buttons x842-1082 y685-759: 金币图标 + 价格)` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Offer Price Discount Badge | ⚠️ 未命中 |
| Discount Title | ⚠️ 未命中 |
| Discount Price | ⚠️ 未命中 |
| WebShop Button | ✅ `scripts\shop.gd:602 # 右侧方钮 (原版 WebShop Button Square 在 name-bg 内 77.6×51.5: (248.6,331.2) — 2026-08-20 核查)` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Button Image | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Preview | ✅ `scripts\main_menu.gd:6 ##   ③ Safe area Only Horizontal: Navigation Panel / ChatPreview / Upper bar(顶栏)/ 3 个 Holder / 弹窗层; scripts` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |

## 摘要

- 规格元素: 37
- 代码命中: 26
- ⚠️未命中: 11 (以下需人工判断)

- `Base Offer Popup`
- `foreground`
- `Descripton`
- `Available Counter`
- `Timer Text`
- `Offer Badge`
- `Text (TMP)`
- `Offer Price Discount Badge`
- `Discount Title`
- `Discount Price`
- `Button Image`