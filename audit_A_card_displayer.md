# UI 规格审计: Card Displayer Menu For Menu

> 来源: d:/2/解包整理/07_场景/mainmenuwarpforge (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Card Displayer Menu For Menu [inactive godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Card Options Panel [godot(x0.0 y0.0 w1920.0 h1080.0)]
    Panel [godot(x1294.0 y146.4 w450.0 h757.0)]
      Crafting Panel [godot(x1294.0 y146.7 w450.0 h263.7)]
        Content [godot(x1294.0 y146.7 w450.0 h263.7)]
          Craft [godot(x1384.0 y244.3 w270.0 h60.6)]
            Button Text [txt=1 godot(x1384.0 y249.3 w122.9 h50.6)]
            Icon
          Image
          Explanation [txt=This will consume a wildcard godot(x1307.5 y315.5 w418.5 h63.3)]
          Info Icon [godot(x1740.6 y161.9 w41.4 h41.4)]
      Upgrade Panel [godot(x1294.0 y411.1 w450.0 h261.6)]
        Content [godot(x1294.0 y411.1 w450.0 h261.6)]
          Glow
          Title [txt=Upgrade this card\nto level {0} godot(x1307.5 y437.3 w418.5 h78.5)]
          Explanation [godot(x1309.0 y594.5 w420.0 h64.8)]
            Text Explanation [txt=Will get: +350 godot(x1417.7 y595.9 w159.9 h62.0)]
            Icon Forge Points Drawer Variant [godot(x1577.6 y599.5 w36.3 h54.8)]
              Content [godot(x1577.6 y599.5 w36.3 h54.8)]
                Army [godot(x1577.6 y599.5 w36.3 h54.8)]
                Converted Drawer [inactive godot(x1636.3 y757.3 w-81.1 h-13.7)]
                  Price Display [godot(x1657.6 y753.9 w388.4 h79.5)]
                    Glow (2)
                    text [txt=2000 godot(x1845.2 y753.9 w92.7 h79.5)]
                  AlreadyOwned [txt=Already Owned godot(x1380.3 y789.5 w430.9 h91.8)]
                Ephemeral Drawer [inactive godot(x1636.3 y757.3 w-81.1 h-13.7)]
                  Price Display [godot(x1657.6 y753.9 w388.4 h79.5)]
                    icon [godot(x1731.0 y753.9 w79.5 h79.5)]
                    text [txt=24 hours godot(x1810.5 y753.9 w162.1 h79.5)]
          Info Icon [godot(x1740.6 y426.4 w41.4 h41.4)]
        No Upgrade Warning [godot(x1294.0 y411.1 w450.0 h261.6)]
          Title [txt=Maximum card tier reached godot(x1314.0 y430.6 w410.0 h214.3)]
        Debug Add cards [godot(x1744.0 y433.1 w119.4 h169.3)]
          Button Add 1 [godot(x1744.0 y433.1 w119.4 h56.4)]
            Text (TMP) [txt=Add +1 card godot(x1744.0 y433.1 w119.4 h56.4)]
          Button Add 10 [godot(x1744.0 y489.5 w119.4 h56.5)]
            Glow (1)
          Button Add 100 [godot(x1744.0 y546.0 w119.4 h56.4)]
            Sparks
      Alternate Art Panel [godot(x1294.0 y673.4 w450.0 h229.6)]
        Background [godot(x1294.0 y673.4 w450.0 h229.6)]
        Title [txt=Upgrade this card\nto level {0} godot(x1379.1 y693.2 w274.6 h60.1)]
        Current Style [godot(x1316.0 y764.3 w406.0 h101.5)]
        Lock Background [godot(x1716.6 y722.1 w65.8 h124.9)]
          Lock icon [godot(x1740.2 y763.4 w28.2 h42.2)]
        Select Art Button Right [godot(x1653.7 y685.4 w74.4 h75.6)]
          Background [godot(x1661.9 y693.4 w56.8 h58.1)]
          Icon [godot(x1661.9 y693.4 w56.8 h58.1)]
        Select Art Button Left [godot(x1304.7 y685.4 w74.4 h75.6)]
          Background [godot(x1312.8 y693.4 w56.9 h58.1)]
          Icon [godot(x1312.8 y693.4 w56.9 h58.1)]
        Buy Original Card Button [godot(x1354.6 y778.3 w328.8 h73.4)]
          Generic UI Button [godot(x1354.6 y778.3 w328.8 h73.4)]
            Button Text [inactive godot(x1367.6 y804.5 w302.8 h21.0)]
            Price Display [godot(x1371.4 y785.0 w293.2 h60.0)]
              icon [godot(x1435.9 y779.0 w72.0 h72.0)]
              text [txt=300,00 godot(x1471.9 y785.0 w92.2 h60.0)]
    Wildcard Segment [godot(x0.0 y71.0 w1920.0 h85.0)]
      WIldcard Counter [godot(x1470.0 y71.0 w400.0 h85.0)]
        Background [godot(x1550.0 y91.5 w320.0 h44.0)]
        Counters [godot(x1555.0 y91.5 w315.0 h44.0)]
          Common [godot(x1565.0 y91.5 w65.0 h44.0)]
            Icon [godot(x1565.0 y91.5 w30.0 h44.0)]
            Counter [txt=999 godot(x1595.0 y91.5 w41.0 h44.0)]
          Lightning
          Epic [godot(x1715.0 y91.5 w65.0 h44.0)]
            Icon [godot(x1715.0 y91.5 w30.0 h44.0)]
            Counter [txt=999 godot(x1745.0 y91.5 w41.0 h44.0)]
          Legendary [godot(x1790.0 y91.5 w65.0 h44.0)]
            Icon [godot(x1790.0 y91.5 w30.0 h44.0)]
            Counter [txt=999 godot(x1820.0 y91.5 w41.0 h44.0)]
        Army Icon [godot(x1470.0 y71.0 w80.0 h85.0)]
    Card Counter [godot(x825.1 y829.8 w269.8 h79.4)]
      Duplicate Counter [godot(x840.0 y834.2 w240.0 h70.6)]
        Background [godot(x840.0 y834.2 w240.0 h70.6)]
        Counters [godot(x836.7 y841.1 w240.0 h70.6)]
          Counter [txt=x2 godot(x869.4 y846.6 w73.3 h70.6)]
          Handle
      Single Counter [inactive godot(x875.0 y844.5 w170.0 h50.0)]
        Background [godot(x875.0 y844.5 w170.0 h50.0)]
        Counter [txt=x2 godot(x875.0 y844.5 w170.0 h50.0)]
  Card Display [godot(x584.0 y106.0 w752.0 h868.0)]
    LowerSection [godot(x300.0 y921.3 w1320.0 h137.0)]
      FlavourTextBG [godot(x300.0 y900.8 w1320.0 h178.0)]
        LoreText [txt=Ghazghkull Mag Uruk Thraka is a mighty p godot(x335.0 y943.1 w1250.0 h93.5)]
      Voice Over Button [godot(x1650.0 y945.5 w88.7 h88.7)]
        Button Text [inactive txt=X godot(x1658.0 y945.5 w72.7 h88.7)]
        Image [inactive godot(x1650.0 y946.5 w86.7 h86.7)]
      Show Card Text [godot(x181.3 y945.5 w88.7 h88.7)]
    Cards [godot(x910.0 y490.0 w100.0 h100.0)]
      CardUI (4) [godot(x642.0 y58.9 w636.0 h842.2)]
        CreatedByText [inactive txt=Created by someone fancy godot(x647.5 y20.0 w625.0 h95.0)]
        2DCard [godot(x698.4 y63.6 w523.2 h832.8)]
          UI Collider [godot(x723.4 y123.6 w473.2 h722.8)]
          Front [godot(x698.4 y23.6 w523.2 h872.8)]
            Card Highlight And Shadow [godot(x406.5 y-90.4 w1107.0 h1107.1)]
            CardImage [godot(x616.5 y127.5 w687.0 h687.0)]
            CardFrame [godot(x679.4 y60.3 w561.2 h814.4)]
          Cardback Container [inactive godot(x835.0 y355.0 w250.0 h250.0)]
            Cardback Shadow SDF [godot(x594.8 y3.5 w730.4 h953.0)]
            Cardback [godot(x688.3 y88.0 w543.4 h784.0)]
        Card Ready for level up [inactive godot(x737.1 y133.6 w445.8 h684.4)]
        New Card Badge [godot(x721.3 y145.5 w302.5 h98.0)]
          Text [txt=Новинка! godot(x721.3 y167.7 w287.9 h53.6)]
        Ban Icon [godot(x705.6 y201.2 w508.8 h557.6)]
          Banned Text [txt=Запрещено godot(x756.5 y424.2 w407.0 h111.6)]
      CardUI (3) [godot(x642.0 y58.9 w636.0 h842.2)]
        CreatedByText [inactive txt=Created by someone fancy godot(x647.5 y20.0 w625.0 h95.0)]
        2DCard [godot(x698.4 y63.6 w523.2 h832.8)]
          UI Collider [godot(x723.4 y123.6 w473.2 h722.8)]
          Front [godot(x698.4 y23.6 w523.2 h872.8)]
            Card Highlight And Shadow [godot(x406.5 y-90.4 w1107.0 h1107.1)]
            CardImage [godot(x616.5 y127.5 w687.0 h687.0)]
            CardFrame [godot(x679.4 y60.3 w561.2 h814.4)]
          Cardback Container [inactive godot(x835.0 y355.0 w250.0 h250.0)]
            Cardback Shadow SDF [godot(x594.8 y3.5 w730.4 h953.0)]
            Cardback [godot(x688.3 y88.0 w543.4 h784.0)]
        Card Ready for level up [inactive godot(x737.1 y133.6 w445.8 h684.4)]
        Glow
        Ban Icon [godot(x705.6 y201.2 w508.8 h557.6)]
          Banned Text [txt=Запрещено godot(x756.5 y424.2 w407.0 h111.6)]
      CardUI (2) [godot(x642.0 y58.9 w636.0 h842.2)]
        CreatedByText [inactive txt=Created by someone fancy godot(x647.5 y20.0 w625.0 h95.0)]
        2DCard [godot(x698.4 y63.6 w523.2 h832.8)]
          Fill Area
          Front [godot(x698.4 y23.6 w523.2 h872.8)]
            Card Highlight And Shadow [godot(x406.5 y-90.4 w1107.0 h1107.1)]
            CardImage [godot(x616.5 y127.5 w687.0 h687.0)]
            CardFrame [godot(x679.4 y60.3 w561.2 h814.4)]
          Cardback Container [inactive godot(x835.0 y355.0 w250.0 h250.0)]
            Cardback Shadow SDF [godot(x594.8 y3.5 w730.4 h953.0)]
            Cardback [godot(x688.3 y88.0 w543.4 h784.0)]
        Card Ready for level up [inactive godot(x737.1 y133.6 w445.8 h684.4)]
        New Card Badge [godot(x721.3 y145.5 w302.5 h98.0)]
          Text [txt=Новинка! godot(x721.3 y167.7 w287.9 h53.6)]
        Ban Icon [godot(x705.6 y201.2 w508.8 h557.6)]
          Banned Text [txt=Запрещено godot(x756.5 y424.2 w407.0 h111.6)]
      CardUI (1) [godot(x642.0 y58.9 w636.0 h842.2)]
        CreatedByText [inactive txt=Created by someone fancy godot(x647.5 y20.0 w625.0 h95.0)]
        2DCard [godot(x698.4 y63.6 w523.2 h832.8)]
          UI Collider [godot(x723.4 y123.6 w473.2 h722.8)]
          Front [godot(x698.4 y23.6 w523.2 h872.8)]
            Card Highlight And Shadow [godot(x406.5 y-90.4 w1107.0 h1107.1)]
            CardImage [godot(x616.5 y127.5 w687.0 h687.0)]
            CardFrame [godot(x679.4 y60.3 w561.2 h814.4)]
          Cardback Container [inactive godot(x835.0 y355.0 w250.0 h250.0)]
            Cardback Shadow SDF [godot(x594.8 y3.5 w730.4 h953.0)]
            Cardback [godot(x688.3 y88.0 w543.4 h784.0)]
        Card Ready for level up [inactive godot(x737.1 y133.6 w445.8 h684.4)]
        New Card Badge [godot(x721.3 y145.5 w302.5 h98.0)]
          Text [txt=Новинка! godot(x721.3 y167.7 w287.9 h53.6)]
        Ban Icon [godot(x705.6 y201.2 w508.8 h557.6)]
          Banned Text [txt=Запрещено godot(x756.5 y424.2 w407.0 h111.6)]
      Background Level Up Darkener [inactive godot(x-1005.7 y-1425.7 w3931.4 h3931.4)]
      CardUI [godot(x642.0 y58.9 w636.0 h842.2)]
        CreatedByText [inactive txt=Created by someone fancy godot(x647.5 y20.0 w625.0 h95.0)]
        2DCard [godot(x698.4 y63.6 w523.2 h832.8)]
          Mask
          Glow Explosion [inactive godot(x-11772.7 y-12028.0 w25000.0 h25000.0)]
            Glow Explosion R [godot(x-11772.7 y-11554.5 w25000.0 h25000.0)]
            Glow Explosion Up [godot(x-11429.0 y-11778.5 w25000.0 h25000.0)]
            Glow Explosion Down [godot(x-12140.3 y-11778.5 w25000.0 h25000.0)]
            Sparks R  [godot(x-11772.7 y-11554.5 w25000.0 h25000.0)]
            Sparks RL [godot(x-11772.7 y-12025.3 w25000.0 h25000.0)]
            Glow Big [godot(x-11797.0 y-11752.8 w25000.0 h25000.0)]
          icon
          Front [godot(x698.4 y23.6 w523.2 h872.8)]
            Card Highlight And Shadow [godot(x406.5 y-90.4 w1107.0 h1107.1)]
            CardImage [godot(x616.5 y127.5 w687.0 h687.0)]
            CardFrame [godot(x679.4 y60.3 w561.2 h814.4)]
          Background Darkener
        Card Ready for level up [inactive godot(x737.1 y133.6 w445.8 h684.4)]
        New Card Badge [godot(x721.3 y145.5 w302.5 h98.0)]
          Text [txt=Новинка! godot(x721.3 y167.7 w287.9 h53.6)]
        Ban Icon [godot(x705.6 y201.2 w508.8 h557.6)]
          Banned Text [txt=Запрещено godot(x756.5 y424.2 w407.0 h111.6)]
        Lighting Rays [inactive godot(x-11545.7 y-11645.0 w25000.0 h25000.0)]
          Glow [godot(x-11545.7 y-11645.0 w25000.0 h25000.0)]
          Glow (1)
    TutorialObjs [godot(x-1213.2 y-1043.9 w4253.3 h3159.0)]
      UnitObjs [godot(x863.4 y485.6 w100.0 h100.0)]
        MeleeText [txt=Melee Attack godot(x249.4 y726.1 w380.0 h55.0)]
          Arrow [godot(x690.5 y670.4 w-206.2 h76.2)]
        RangedText [txt=Ranged Attack godot(x313.4 y797.7 w380.0 h55.0)]
          Arrow [godot(x772.3 y907.0 w-206.2 h-76.2)]
        HealthText [txt=Health Points godot(x1204.4 y781.1 w380.0 h55.0)]
          Arrow [godot(x1188.3 y893.7 w206.2 h-76.2)]
      EnergyText [txt=Energy Cost godot(x1240.3 y254.0 w340.3 h59.3)]
        Arrow [godot(x1218.1 y195.9 w206.2 h76.2)]
  Item Information Panel [inactive godot(x1263.5 y298.4 w393.0 h500.0)]
    Title [txt=Title godot(x1302.8 y323.4 w314.4 h50.0)]
    Description [txt=New Text godot(x1302.8 y373.4 w314.4 h300.0)]
    Type [txt=Type godot(x1302.8 y673.4 w314.4 h50.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Card Displayer Menu For Menu | ✅ `scripts\card_displayer.gd:2 ## 卡牌详情弹窗 (原版 3-PopUp Holder → Card Displayer Menu For Menu 说明书)` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Card Options Panel | ⚠️ 未命中 |
| Panel | ✅ `scripts\battle.gd:1242 # ---------- Cemetery (原版 ShowCemeteryBtn → CemeteryLogPanel) ----------; scripts\battle.gd:1247 ## Cemeter` |
| Crafting Panel | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Craft | ✅ `scripts\card_displayer.gd:377 craft.name = "CraftPanel"; scripts\card_displayer.gd:403 _cost_label = _add_label(cost_row, "Craft C` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Explanation | ⚠️ 未命中 |
| Info Icon | ✅ `scripts\card_displayer.gd:386 # Info 问号图标 (原版 Info Icon 40K_generic_bt_info 41.4x41.4 @ 制作面板 [1740.6,1782] y[161.9,203.3]` |
| Upgrade Panel | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Explanation | ⚠️ 未命中 |
| Text Explanation | ⚠️ 未命中 |
| Icon Forge Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Army | ✅ `scripts\battle.gd:171 # 原版 battlearena1 场景树无阵营选择弹窗 (Army Selector 在模式选择界面) —; scripts\battle.gd:3163 # HolderRating x[568.8,755.8]` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| Glow (2) | ⚠️ 未命中 |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Info Icon | ✅ `scripts\card_displayer.gd:386 # Info 问号图标 (原版 Info Icon 40K_generic_bt_info 41.4x41.4 @ 制作面板 [1740.6,1782] y[161.9,203.3]` |
| No Upgrade Warning | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Debug Add cards | ⚠️ 未命中 |
| Button Add 1 | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Button Add 10 | ⚠️ 未命中 |
| Glow (1) | ⚠️ 未命中 |
| Button Add 100 | ⚠️ 未命中 |
| Sparks | ✅ `scenes\unity_arena_battlearena1.gd:373 n_23.name = 'ElectricalSparks'` |
| Alternate Art Panel | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Current Style | ⚠️ 未命中 |
| Lock Background | ✅ `scripts\card_displayer.gd:467 lock.position = Vector2(422.6, 48.7)   # 原版 Lock Background local y 48.7 (722.1-673.4) — 2026-08-21` |
| Lock icon | ⚠️ 未命中 |
| Select Art Button Right | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Select Art Button Left | ✅ `scripts\card_displayer.gd:453 # 左右选择按钮 (原版 Select Art Button Left/Right 74x76, 无替换样式 → 禁用)` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Buy Original Card Button | ✅ `scripts\card_displayer.gd:460 # 购买原版按钮 (原版 Buy Original Card Button x[1354.6,1683.4] y[778.3,851.7] → local y 104.9 —; scripts\car` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Wildcard Segment | ✅ `scripts\card_displayer.gd:187 # 底部通配符条 (场景 Wildcard Segment x0-1920 y71-156); scripts\card_displayer.gd:480 ## 底部通配符条 (场景 Wildcard` |
| WIldcard Counter | ✅ `scripts\card_displayer.gd:500 # 通配符计数 (场景 WIldcard Counter x1470-1870 400 宽; pitch 75 起点 85, 数字 32.6px); scripts\deck_builder.gd:2` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Counters | ✅ `scripts\card_displayer.gd:509 # 原版 Counters 组相对 1555: Common 10 / Rare 85 / Epic 160 / Legendary 235 (pitch 75); scripts\collectio` |
| Common | ✅ `scripts\booster_info_popup.gd:85 desc.text = "Each pack opened adds +1 to the \"packs since last Legendary\" counter.\n\nA Legenda` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Lightning | ✅ `scripts\battle.gd:776 "Sautekh": [["battlearena3", "Lightning"], ["battlearena3", "Monolith_Glow"], ["battlearena3", "Scar; script` |
| Epic | ✅ `scripts\booster_info_popup.gd:85 desc.text = "Each pack opened adds +1 to the \"packs since last Legendary\" counter.\n\nA Legenda` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Legendary | ✅ `scripts\achievements.gd:32 ["upgrade_legendary", "Legendary Forger", "Upgrade 3 Legendary cards", "upgrade", 3, 350],; scripts\ach` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Army Icon | ✅ `scripts\campaign.gd:190 # 阵营图标 (原版 Army Icon); scripts\card_displayer.gd:489 # 阵营图标 (场景 Army Icon 80x85)` |
| Card Counter | ✅ `scripts\card_displayer.gd:172 # 重复计数 (场景 Card Counter x825-1095 y830-909); scripts\collection.gd:1000 # 副本数角标 (原版 Collection Card ` |
| Duplicate Counter | ✅ `scripts\card_displayer.gd:343 _dup_label.add_theme_font_size_override("font_size", 52)   # 原版 Duplicate Counter fontsize=52.6` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Counters | ✅ `scripts\card_displayer.gd:509 # 原版 Counters 组相对 1555: Common 10 / Rare 85 / Epic 160 / Legendary 235 (pitch 75); scripts\collectio` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Single Counter | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Card Display | ✅ `scripts\battle.gd:1386 # ---------- 卡牌/督军详情弹窗 (原版 Card Display Window) ----------; scripts\battle.gd:1412 # 弹窗 (原版 Card Display 75` |
| LowerSection | ✅ `scripts\card_displayer.gd:167 # 卡面下方 Lore 背景故事区 (原版 Card Display LowerSection:; scripts\card_displayer.gd:178 # 底部按钮行 (场景 LowerSec` |
| FlavourTextBG | ✅ `scripts\card_displayer.gd:168 # FlavourTextBG RectTransform_*-4471848433362871389 1320x178 锚(0.5,0.5) pivot(0.5,0) pos(0,-518.34);` |
| LoreText | ✅ `scripts\card_displayer.gd:169 # → 链式换算 Godot x[300,1620] y[880.3,1058.3]; LoreText 子 1250x93.5 居中 y[922.6,1016.1] 32px 白字居中); scri` |
| Voice Over Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Show Card Text | ⚠️ 未命中 |
| Cards | ✅ `scripts\battle.gd:155 var _hand_box: Control   # 手牌容器 (原版 CardsInHand 弧形布局, 位置由 _layout_hand 计算); scripts\battle.gd:273 # 对战音效: 开局` |
| CardUI (4) | ⚠️ 未命中 |
| CreatedByText | ⚠️ 未命中 |
| 2DCard | ✅ `scripts\battle.gd:32 const CARD3D_W := 0.75   # 3D 卡牌平面尺寸 (原版 2DCard 2.0927×3.3313 × 玩家 desiredScale 0.36 = 0.753×1.199 ≈; scripts` |
| UI Collider | ⚠️ 未命中 |
| Front | ✅ `scripts\battle.gd:578 ["sautekh/Monolith Front Left1.obj", -9, 9, 0, 400.0, 90, 90], ["sautekh/Monolith Front Right1.obj",; script` |
| Card Highlight And Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| CardImage | ✅ `scripts\battle.gd:902 ## 立绘 cover-crop 到卡框内窗纵横比 (495/813) — 2DCard CardImage 层 (LRU 缓存)` |
| CardFrame | ⚠️ 未命中 |
| Cardback Container | ⚠️ 未命中 |
| Cardback Shadow SDF | ⚠️ 未命中 |
| Cardback | ✅ `scripts\battle.gd:425 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:102 b.tooltip_text = file.get` |
| Card Ready for level up | ⚠️ 未命中 |
| New Card Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Ban Icon | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
| Banned Text | ⚠️ 未命中 |
| CardUI (3) | ⚠️ 未命中 |
| CreatedByText | ⚠️ 未命中 |
| 2DCard | ✅ `scripts\battle.gd:32 const CARD3D_W := 0.75   # 3D 卡牌平面尺寸 (原版 2DCard 2.0927×3.3313 × 玩家 desiredScale 0.36 = 0.753×1.199 ≈; scripts` |
| UI Collider | ⚠️ 未命中 |
| Front | ✅ `scripts\battle.gd:578 ["sautekh/Monolith Front Left1.obj", -9, 9, 0, 400.0, 90, 90], ["sautekh/Monolith Front Right1.obj",; script` |
| Card Highlight And Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| CardImage | ✅ `scripts\battle.gd:902 ## 立绘 cover-crop 到卡框内窗纵横比 (495/813) — 2DCard CardImage 层 (LRU 缓存)` |
| CardFrame | ⚠️ 未命中 |
| Cardback Container | ⚠️ 未命中 |
| Cardback Shadow SDF | ⚠️ 未命中 |
| Cardback | ✅ `scripts\battle.gd:425 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:102 b.tooltip_text = file.get` |
| Card Ready for level up | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| Ban Icon | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
| Banned Text | ⚠️ 未命中 |
| CardUI (2) | ⚠️ 未命中 |
| CreatedByText | ⚠️ 未命中 |
| 2DCard | ✅ `scripts\battle.gd:32 const CARD3D_W := 0.75   # 3D 卡牌平面尺寸 (原版 2DCard 2.0927×3.3313 × 玩家 desiredScale 0.36 = 0.753×1.199 ≈; scripts` |
| Fill Area | ⚠️ 未命中 |
| Front | ✅ `scripts\battle.gd:578 ["sautekh/Monolith Front Left1.obj", -9, 9, 0, 400.0, 90, 90], ["sautekh/Monolith Front Right1.obj",; script` |
| Card Highlight And Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| CardImage | ✅ `scripts\battle.gd:902 ## 立绘 cover-crop 到卡框内窗纵横比 (495/813) — 2DCard CardImage 层 (LRU 缓存)` |
| CardFrame | ⚠️ 未命中 |
| Cardback Container | ⚠️ 未命中 |
| Cardback Shadow SDF | ⚠️ 未命中 |
| Cardback | ✅ `scripts\battle.gd:425 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:102 b.tooltip_text = file.get` |
| Card Ready for level up | ⚠️ 未命中 |
| New Card Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Ban Icon | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
| Banned Text | ⚠️ 未命中 |
| CardUI (1) | ⚠️ 未命中 |
| CreatedByText | ⚠️ 未命中 |
| 2DCard | ✅ `scripts\battle.gd:32 const CARD3D_W := 0.75   # 3D 卡牌平面尺寸 (原版 2DCard 2.0927×3.3313 × 玩家 desiredScale 0.36 = 0.753×1.199 ≈; scripts` |
| UI Collider | ⚠️ 未命中 |
| Front | ✅ `scripts\battle.gd:578 ["sautekh/Monolith Front Left1.obj", -9, 9, 0, 400.0, 90, 90], ["sautekh/Monolith Front Right1.obj",; script` |
| Card Highlight And Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| CardImage | ✅ `scripts\battle.gd:902 ## 立绘 cover-crop 到卡框内窗纵横比 (495/813) — 2DCard CardImage 层 (LRU 缓存)` |
| CardFrame | ⚠️ 未命中 |
| Cardback Container | ⚠️ 未命中 |
| Cardback Shadow SDF | ⚠️ 未命中 |
| Cardback | ✅ `scripts\battle.gd:425 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:102 b.tooltip_text = file.get` |
| Card Ready for level up | ⚠️ 未命中 |
| New Card Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Ban Icon | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
| Banned Text | ⚠️ 未命中 |
| Background Level Up Darkener | ⚠️ 未命中 |
| CardUI | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| CreatedByText | ⚠️ 未命中 |
| 2DCard | ✅ `scripts\battle.gd:32 const CARD3D_W := 0.75   # 3D 卡牌平面尺寸 (原版 2DCard 2.0927×3.3313 × 玩家 desiredScale 0.36 = 0.753×1.199 ≈; scripts` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Glow Explosion | ⚠️ 未命中 |
| Glow Explosion R | ⚠️ 未命中 |
| Glow Explosion Up | ⚠️ 未命中 |
| Glow Explosion Down | ⚠️ 未命中 |
| Sparks R  | ⚠️ 未命中 |
| Sparks RL | ⚠️ 未命中 |
| Glow Big | ⚠️ 未命中 |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| Front | ✅ `scripts\battle.gd:578 ["sautekh/Monolith Front Left1.obj", -9, 9, 0, 400.0, 90, 90], ["sautekh/Monolith Front Right1.obj",; script` |
| Card Highlight And Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| CardImage | ✅ `scripts\battle.gd:902 ## 立绘 cover-crop 到卡框内窗纵横比 (495/813) — 2DCard CardImage 层 (LRU 缓存)` |
| CardFrame | ⚠️ 未命中 |
| Background Darkener | ⚠️ 未命中 |
| Card Ready for level up | ⚠️ 未命中 |
| New Card Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Ban Icon | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\deck_info` |
| Banned Text | ⚠️ 未命中 |
| Lighting Rays | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| Glow (1) | ⚠️ 未命中 |
| TutorialObjs | ⚠️ 未命中 |
| UnitObjs | ⚠️ 未命中 |
| MeleeText | ⚠️ 未命中 |
| Arrow | ✅ `scripts\where_cards_popup.gd:142 arrow.name = "Arrow"` |
| RangedText | ⚠️ 未命中 |
| Arrow | ✅ `scripts\where_cards_popup.gd:142 arrow.name = "Arrow"` |
| HealthText | ⚠️ 未命中 |
| Arrow | ✅ `scripts\where_cards_popup.gd:142 arrow.name = "Arrow"` |
| EnergyText | ⚠️ 未命中 |
| Arrow | ✅ `scripts\where_cards_popup.gd:142 arrow.name = "Arrow"` |
| Item Information Panel | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Description | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Type | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |

## 摘要

- 规格元素: 194
- 代码命中: 115
- ⚠️未命中: 79 (以下需人工判断)

- `Card Options Panel`
- `Crafting Panel`
- `Explanation`
- `Upgrade Panel`
- `Explanation`
- `Text Explanation`
- `Icon Forge Points Drawer Variant`
- `Converted Drawer`
- `Glow (2)`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `No Upgrade Warning`
- `Debug Add cards`
- `Button Add 1`
- `Text (TMP)`
- `Button Add 10`
- `Glow (1)`
- `Button Add 100`
- `Alternate Art Panel`
- `Current Style`
- `Lock icon`
- `Select Art Button Right`
- `Single Counter`
- `Voice Over Button`
- `Show Card Text`
- `CardUI (4)`
- `CreatedByText`
- `UI Collider`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `CardUI (3)`
- `CreatedByText`
- `UI Collider`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `CardUI (2)`
- `CreatedByText`
- `Fill Area`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `CardUI (1)`
- `CreatedByText`
- `UI Collider`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `Background Level Up Darkener`
- `CreatedByText`
- `Glow Explosion`
- `Glow Explosion R`
- `Glow Explosion Up`
- `Glow Explosion Down`
- `Sparks R `
- `Sparks RL`
- `Glow Big`
- `CardFrame`
- `Background Darkener`
- `Card Ready for level up`
- `Banned Text`
- `Lighting Rays`
- `Glow (1)`
- `TutorialObjs`
- `UnitObjs`
- `MeleeText`
- `RangedText`
- `HealthText`
- `EnergyText`
- `Item Information Panel`