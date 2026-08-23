# UI 规格审计: Deck Editing Menu

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 08:19
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Deck Editing Menu [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Content Area [godot(x167.2 y71.0 w1752.8 h1009.0)]
    Background [godot(x167.2 y71.0 w1752.8 h1009.0)]
    Header [godot(x167.2 y71.0 w1752.8 h85.0)]
      Filters [godot(x367.2 y88.5 w50.0 h50.0)]
        Label [txt=Filters godot(x437.2 y88.5 w150.0 h50.0)]
        Icon [godot(x377.2 y98.5 w30.0 h30.0)]
      Instructions [inactive godot(x1420.0 y88.5 w400.0 h50.0)]
      Separator Line [godot(x167.2 y151.0 w1752.8 h10.0)]
      Filters [godot(x592.2 y71.0 w876.4 h85.0)]
        Generic Simplified UI Button_updated [godot(x1488.6 y83.5 w250.0 h60.0)]
          Button Text [txt=Clear filters godot(x1502.5 y89.4 w221.4 h48.2)]
      Filler [godot(x-202.3 y71.0 w443.3 h85.0)]
      label [inactive txt=Edit your deck godot(x1320.0 y81.0 w500.0 h60.0)]
      WIldcard Counter [godot(x1470.0 y71.0 w400.0 h85.0)]
        Background [godot(x1550.0 y91.5 w320.0 h44.0)]
        Counters [godot(x1555.0 y91.5 w315.0 h44.0)]
          Common [godot(x1555.0 y135.5 w0.0 h0.0)]
            Icon [godot(x1540.0 y135.5 w30.0 h0.0)]
            Counter [txt=999 godot(x1534.5 y135.5 w41.0 h0.0)]
          Rare [godot(x1555.0 y135.5 w0.0 h0.0)]
            Icon [godot(x1540.0 y135.5 w30.0 h0.0)]
            Counter [txt=999 godot(x1534.5 y135.5 w41.0 h0.0)]
          Epic [godot(x1555.0 y135.5 w0.0 h0.0)]
            Icon [godot(x1540.0 y135.5 w30.0 h0.0)]
            Counter [txt=999 godot(x1534.5 y135.5 w41.0 h0.0)]
          Legendary [godot(x1555.0 y135.5 w0.0 h0.0)]
            Icon [godot(x1540.0 y135.5 w30.0 h0.0)]
            Counter [txt=999 godot(x1534.5 y135.5 w41.0 h0.0)]
        Army Icon [godot(x1470.0 y71.0 w80.0 h85.0)]
      Close [godot(x192.2 y83.5 w150.0 h60.0)]
        Button Text [txt=Back godot(x200.5 y89.3 w133.2 h48.2)]
    Sidebar [godot(x0.3 y156.0 w335.3 h924.0)]
      Background [godot(x-203.0 y156.0 w538.6 h924.0)]
      Window Options [godot(x0.3 y156.0 w326.8 h205.0)]
        Buttons [godot(x0.3 y156.0 w326.8 h150.0)]
          Cards [godot(x0.3 y306.0 w0.0 h0.0)]
            Highlight [godot(x0.3 y306.0 w0.0 h0.0)]
            Icon [godot(x0.3 y306.0 w0.0 h0.0)]
            Label [godot(x5.3 y261.0 w-10.0 h40.0)]
              Text [txt=Cards godot(x5.3 y261.0 w-10.0 h40.0)]
          Info [godot(x0.3 y306.0 w0.0 h0.0)]
            Highlight [godot(x0.3 y306.0 w0.0 h0.0)]
            Icon [godot(x0.3 y306.0 w0.0 h0.0)]
            Label [godot(x5.3 y261.0 w-10.0 h40.0)]
              Text [txt=Deck info godot(x5.3 y261.0 w-10.0 h40.0)]
          Cosmetics [godot(x0.3 y306.0 w0.0 h0.0)]
            Highlight [godot(x0.3 y306.0 w0.0 h0.0)]
            Icon [godot(x0.3 y306.0 w0.0 h0.0)]
            Label [godot(x5.3 y261.0 w-10.0 h40.0)]
              Text [txt=Cosmetics godot(x5.3 y261.0 w-10.0 h40.0)]
        Deck Name [godot(x9.5 y311.0 w307.7 h50.0)]
          Text Area [godot(x19.5 y318.0 w287.7 h37.0)]
            Placeholder [txt=Tap to edit deck name godot(x19.5 y318.0 w287.7 h37.0)]
            Text [txt=​ godot(x19.5 y318.0 w287.7 h37.0)]
          Image [inactive godot(x277.2 y316.0 w35.0 h40.0)]
      Deck Details [godot(x0.3 y361.0 w335.3 h649.0)]
        Deck List drawer [godot(x0.4 y366.0 w325.0 h644.0)]
          Scroll View [godot(x0.4 y366.0 w325.0 h644.0)]
            Viewport [godot(x0.4 y366.0 w325.0 h644.0)]
              Content [godot(x0.4 y366.0 w325.0 h0.0)]
                Deck Selector Hero Card Info button [godot(x0.4 y338.1 w0.0 h55.7)]
                  Content [godot(x0.4 y338.1 w0.0 h55.7)]
                    Background [godot(x0.4 y338.1 w0.0 h55.7)]
                    Rarity Gradient [godot(x0.4 y338.1 w0.0 h55.7)]
                    Background Border [godot(x0.4 y338.1 w0.0 h55.7)]
                    Card Name [txt=Card name godot(x20.4 y338.1 w-75.0 h55.7)]
                    Count [txt=2 godot(x-49.6 y338.1 w50.0 h55.7)]
                    Ban Icon [godot(x238.3 y338.1 w-241.7 h55.7)]
                    Background Slot Free [godot(x0.4 y338.1 w0.0 h55.7)]
                    Slot Free Text [txt=-- Warlord -- godot(x0.4 y338.1 w0.0 h55.7)]
                Deck Selector Defensive Card Slot [godot(x0.4 y338.1 w0.0 h55.7)]
                  Content [godot(x0.4 y338.1 w0.0 h55.7)]
                    Background [godot(x0.4 y338.1 w0.0 h55.7)]
                    Background Slot Free [godot(x0.4 y338.1 w0.0 h55.7)]
                    Slot Free Text [txt=-- Defensive -- godot(x0.4 y338.1 w0.0 h55.7)]
                    Rarity Gradient [godot(x6.8 y338.1 w-6.4 h55.6)]
                    Background Border [godot(x0.4 y338.1 w0.0 h55.7)]
                    Cost Image [godot(x17.0 y335.1 w0.0 h61.7)]
                      Cost [txt=5 godot(x-7.4 y342.0 w48.8 h47.9)]
                    banned Icon [godot(x14.1 y332.0 w0.0 h61.7)]
                    Text fill [godot(x15.5 y342.0 w-19.9 h47.9)]
                      Card Name [txt=Card Name godot(x15.5 y389.9 w0.0 h0.0)]
                      Count [txt=x2 godot(x15.5 y389.9 w0.0 h0.0)]
                Deck Selector Card Info button [godot(x0.4 y338.1 w0.0 h55.7)]
                  Content [godot(x0.4 y338.1 w0.0 h55.7)]
                    Background [godot(x0.4 y338.1 w0.0 h55.7)]
                      Rarity Gradient [godot(x-0.0 y338.1 w0.4 h55.6)]
                      Background Border [godot(x-15.9 y338.1 w16.3 h55.7)]
                      Cost Image [godot(x0.2 y335.1 w0.0 h61.7)]
                        Cost [txt=5 godot(x-24.2 y342.0 w48.8 h47.9)]
                      banned Icon [godot(x-2.7 y332.0 w0.0 h61.7)]
                      Text fill [godot(x0.4 y342.0 w-5.0 h47.9)]
                        Card Name [txt=Card Name godot(x0.4 y389.9 w0.0 h0.0)]
                        Count [txt=x2 godot(x0.4 y389.9 w0.0 h0.0)]
          Empty Warning [inactive txt=Arraste as cartas aqui para criar seu de godot(x20.3 y445.0 w295.2 h186.0)]
        Deck Information cost drawer [inactive godot(x50.9 y315.4 w234.0 h294.6)]
          Background [godot(x50.9 y315.4 w234.0 h294.6)]
          Content [godot(x2.4 y315.4 w331.0 h294.6)]
            Deck CostQuanityt Row Drawer [godot(x2.4 y315.4 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y314.7 w37.9 h29.4)]
              Cards in deck [txt=0 godot(x289.9 y314.6 w37.9 h29.6)]
              Slider [godot(x55.9 y314.6 w224.0 h29.6)]
                Background [godot(x55.9 y317.6 w224.0 h24.5)]
                Fill [godot(x55.9 y318.1 w0.0 h22.6)]
            Deck CostQuanityt Row Drawer (1) [godot(x2.4 y348.5 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y347.7 w37.9 h29.5)]
              Cards in deck [txt=0 godot(x289.9 y347.7 w37.9 h29.6)]
              Slider [godot(x55.9 y347.7 w224.0 h29.6)]
                Background [godot(x55.9 y350.6 w224.0 h24.5)]
                Fill [godot(x55.9 y351.2 w0.0 h22.6)]
            Deck CostQuanityt Row Drawer (2) [godot(x2.4 y381.5 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y380.8 w37.9 h29.5)]
              Cards in deck [txt=0 godot(x289.9 y380.7 w37.9 h29.6)]
              Slider [godot(x55.9 y380.7 w224.0 h29.6)]
                Background [godot(x55.9 y383.7 w224.0 h24.5)]
                Fill [godot(x55.9 y384.2 w0.0 h22.6)]
            Deck CostQuanityt Row Drawer (3) [godot(x2.4 y414.6 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y413.9 w37.9 h29.4)]
              Cards in deck [txt=0 godot(x289.9 y413.8 w37.9 h29.6)]
              Slider [godot(x55.9 y413.8 w224.0 h29.6)]
                Background [godot(x55.9 y416.7 w224.0 h24.6)]
                Fill [godot(x55.9 y417.3 w0.0 h22.6)]
            Deck CostQuanityt Row Drawer (4) [godot(x2.4 y447.7 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y446.9 w37.9 h29.5)]
              Cards in deck [txt=0 godot(x289.9 y446.9 w37.9 h29.6)]
              Slider [godot(x55.9 y446.9 w224.0 h29.6)]
                Background [godot(x55.9 y449.8 w224.0 h24.5)]
                Fill [godot(x55.9 y450.4 w0.0 h22.6)]
            Deck CostQuanityt Row Drawer (5) [godot(x2.4 y480.7 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y480.0 w37.9 h29.5)]
              Cards in deck [txt=0 godot(x289.9 y479.9 w37.9 h29.6)]
              Slider [godot(x55.9 y479.9 w224.0 h29.6)]
                Background [godot(x55.9 y482.9 w224.0 h24.5)]
                Fill [godot(x55.9 y483.4 w0.0 h22.6)]
            Deck CostQuanityt Row Drawer (6) [godot(x2.4 y513.8 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y513.1 w37.9 h29.4)]
              Cards in deck [txt=0 godot(x289.9 y513.0 w37.9 h29.6)]
              Slider [godot(x55.9 y513.0 w224.0 h29.6)]
                Background [godot(x55.9 y515.9 w224.0 h24.6)]
                Fill [godot(x55.9 y516.5 w0.0 h22.6)]
            Deck CostQuanityt Row Drawer (7) [godot(x2.4 y546.9 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y546.1 w37.9 h29.5)]
              Cards in deck [txt=0 godot(x289.9 y546.1 w37.9 h29.6)]
              Slider [godot(x55.9 y546.1 w224.0 h29.6)]
                Background [godot(x55.9 y549.0 w224.0 h24.5)]
                Fill [godot(x55.9 y549.6 w0.0 h22.5)]
            Deck CostQuanityt Row Drawer (8) [godot(x2.4 y579.9 w331.0 h28.0)]
              Card Cost [txt=0 godot(x7.4 y579.2 w37.9 h29.5)]
              Cards in deck [txt=0 godot(x289.9 y579.1 w37.9 h29.6)]
              Slider [godot(x55.9 y579.1 w224.0 h29.6)]
                Background [godot(x55.9 y582.1 w224.0 h24.5)]
                Fill [godot(x55.9 y582.6 w0.0 h22.6)]
        Deck Counter Drawer [inactive godot(x0.3 y761.0 w335.3 h100.0)]
          Text (TMP) [txt=Troops godot(x25.3 y811.0 w310.3 h50.0)]
          Text (TMP) (1) [txt=Stratagems godot(x25.3 y761.0 w310.3 h50.0)]
        Cosmetic Drawer [inactive godot(x0.3 y485.5 w335.3 h400.0)]
          Cosmetic [godot(x0.3 y485.5 w335.3 h400.0)]
      Footer [godot(x0.3 y1010.0 w335.3 h70.0)]
        Done [godot(x13.0 y1020.5 w188.6 h50.2)]
          Button Text [txt=Done godot(x22.7 y1025.5 w168.6 h40.3)]
          Done Highlight [sprite=FX Square UI SDF godot(x67.2 y933.5 w81.3 h223.2)]
        Counter [txt=30/30 godot(x251.6 y1020.0 w75.0 h50.0)]
        Image [godot(x201.6 y1025.0 w50.0 h40.0)]
        GameObject [inactive godot(x117.9 y995.0 w100.0 h100.0)]
    Card Display [godot(x167.2 y71.0 w1752.8 h1009.0)]
      Scroll View [godot(x330.2 y156.0 w1589.8 h924.0)]
        Viewport [godot(x330.2 y156.0 w1589.8 h924.0)]
          Content [godot(x330.2 y156.0 w1589.8 h300.0)]
        Empty Collection Warning [inactive godot(x135.2 y71.0 w1834.8 h1009.0)]
          Warning [txt=There are no cards in your collection fo godot(x135.2 y71.0 w1834.8 h1009.0)]
        Reference Card Pointer [inactive godot(x417.7 y261.0 w193.8 h45.0)]
      Card Filters [godot(x2.2 y156.0 w331.7 h924.0)]
        Shadow [godot(x2.2 y156.0 w331.7 h924.0)]
        Scroll View [godot(x2.2 y156.0 w331.7 h924.0)]
          Viewport [godot(x2.2 y156.0 w331.7 h924.0)]
            Filters [godot(x2.2 y156.0 w331.7 h0.0)]
              Name FIlter [godot(x2.2 y116.5 w0.0 h79.0)]
                Input Field [godot(x-138.5 y136.0 w281.3 h40.0)]
                  Text Area [godot(x-128.5 y143.0 w231.3 h27.0)]
                    Placeholder [txt=Search godot(x-128.5 y143.0 w231.3 h27.0)]
                    Text [txt=​ godot(x-128.5 y143.0 w231.3 h27.0)]
                  Image [godot(x102.8 y141.0 w35.0 h30.0)]
              Owned Toggle [godot(x2.2 y131.0 w0.0 h50.0)]
                Image [godot(x7.2 y131.0 w-30.0 h50.0)]
                Label [txt=Owned only godot(x27.2 y131.0 w-25.0 h50.0)]
              Upgradable Toggle [godot(x2.2 y131.0 w0.0 h50.0)]
                Image [godot(x7.2 y131.0 w-30.0 h50.0)]
                Label [txt=Upgradable only godot(x27.2 y131.0 w-25.0 h50.0)]
              Army Filter [godot(x2.2 y335.0 w331.7 h0.0)]
                Title [txt=Army godot(x2.2 y310.0 w0.0 h50.0)]
                Content [godot(x2.2 y385.0 w331.7 h0.0)]
                  Toggle [godot(x2.2 y385.0 w0.0 h0.0)]
                    Background [godot(x2.2 y385.0 w0.0 h0.0)]
                      Checkmark [inactive godot(x2.2 y385.0 w0.0 h0.0)]
              Rarity FIlter [godot(x2.2 y16.0 w0.0 h280.0)]
                Title [txt=Rarity godot(x27.2 y41.0 w-25.0 h50.0)]
                Content [godot(x2.2 y81.0 w0.0 h215.0)]
                  Toggle [godot(x2.2 y296.0 w0.0 h0.0)]
                    Background [godot(x-22.8 y271.0 w50.0 h50.0)]
                      Checkmark [inactive godot(x-22.8 y271.0 w50.0 h50.0)]
                    Label [txt=Legendary godot(x2.2 y274.0 w0.0 h22.0)]
              Cost Filter [godot(x2.2 y41.0 w0.0 h230.0)]
                Title [txt=Energy Cost godot(x27.2 y56.0 w-25.0 h50.0)]
                Content [godot(x2.2 y106.0 w0.0 h165.0)]
                  Toggle [godot(x2.2 y271.0 w0.0 h0.0)]
                    Background [godot(x2.2 y271.0 w0.0 h0.0)]
                      Checkmark [inactive godot(x2.2 y271.0 w0.0 h0.0)]
                      Label [txt=0 godot(x2.2 y271.0 w0.0 h0.0)]
              Type Filter [godot(x2.2 y81.0 w0.0 h150.0)]
                Title [txt=Type godot(x27.2 y86.0 w-25.0 h50.0)]
                Content [godot(x2.2 y81.0 w0.0 h150.0)]
                  Toggle [godot(x-37.8 y181.0 w80.0 h100.0)]
                    Background [godot(x-22.8 y206.0 w50.0 h50.0)]
                      Checkmark [inactive godot(x-22.8 y206.0 w50.0 h50.0)]
                    Label [txt=Warlord godot(x-37.8 y259.0 w80.0 h22.0)]
      Card Drag Controller [godot(x993.6 y525.5 w100.0 h100.0)]
        Deck Selector Card Info button [inactive godot(x414.4 y555.2 w287.9 h55.7)]
          Content [godot(x414.4 y555.2 w287.9 h55.7)]
            Background [godot(x445.4 y555.2 w256.9 h55.7)]
            Card Name [txt=Card name godot(x479.4 y555.2 w167.9 h55.7)]
            Cost Image [godot(x414.4 y552.1 w62.0 h62.0)]
              Cost [txt=5 godot(x414.4 y552.1 w60.5 h62.0)]
    Cosmetic Display [inactive godot(x167.2 y71.0 w1752.8 h1009.0)]
      Scroll View [godot(x330.2 y156.0 w1589.8 h924.0)]
        Viewport [godot(x330.2 y156.0 w1589.8 h924.0)]
          Content [godot(x330.2 y156.0 w1589.8 h300.0)]
        Empty Collection Warning [inactive godot(x135.2 y71.0 w1834.8 h1009.0)]
          Warning [txt=There are no cards in your collection fo godot(x135.2 y71.0 w1834.8 h1009.0)]
      Cosmetic FIlter [inactive godot(x2.2 y156.0 w331.7 h924.0)]
        Shadow [godot(x2.2 y156.0 w331.7 h924.0)]
        Filters [godot(x2.2 y156.0 w331.7 h924.0)]
          Spacing [godot(x2.2 y156.0 w331.7 h15.0)]
          Army Filter [godot(x2.2 y171.0 w331.7 h150.0)]
            Title [txt=Army godot(x2.2 y171.0 w330.1 h50.0)]
            Content [godot(x2.2 y221.0 w330.1 h100.0)]
              Toggle [godot(x16.2 y221.0 w100.0 h100.0)]
                Background [godot(x16.2 y221.0 w100.0 h100.0)]
                  Checkmark [inactive godot(x16.2 y221.0 w100.0 h100.0)]
          Spacing (1) [godot(x2.2 y321.0 w331.7 h12.8)]
          Owned Toggle [godot(x2.2 y333.8 w331.7 h50.0)]
            Image [godot(x228.9 y333.8 w80.0 h50.0)]
            Label [txt=Owned only godot(x27.2 y333.8 w230.0 h50.0)]
      Cosmetic Drag Controller [godot(x993.6 y525.5 w100.0 h100.0)]
        Collection Cosmetic [inactive godot(x993.6 y525.5 w150.0 h243.0)]
          content [godot(x993.6 y525.5 w150.0 h243.0)]
            Image [godot(x1002.6 y547.7 w132.0 h198.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Deck Editing Menu | ✅ `scripts\deck_builder.gd:88 # 注: 原版 Deck Editing Menu 无导航 — Header 黑 Filler x[-202.3,241] y[71,156] + Sidebar; scripts\deck_builder` |
| Content Area | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\rewards.gd:145` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Header | ✅ `scripts\battle.gd:1447 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Instructions | ✅ `scripts\deck_builder.gd:216 # 注: 原版 label 'Edit your deck' / Instructions m_IsActive=false 默认隐藏 (2026-08-21 专项审查` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Generic Simplified UI Button_updated | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Filler | ✅ `scripts\deck_builder.gd:88 # 注: 原版 Deck Editing Menu 无导航 — Header 黑 Filler x[-202.3,241] y[71,156] + Sidebar; scripts\deck_builder` |
| label | ✅ `scripts\achievements.gd:113 _make_label(self, "Achievements", Vector2(240, 40), Vector2(400, 44), 28, Color(0.969, 0.914, 0.714); ` |
| WIldcard Counter | ✅ `scripts\card_displayer.gd:500 # 通配符计数 (场景 WIldcard Counter x1470-1870 400 宽; pitch 75 起点 85, 数字 32.6px); scripts\deck_builder.gd:2` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Counters | ✅ `scripts\card_displayer.gd:509 # 原版 Counters 组相对 1555: Common 10 / Rare 85 / Epic 160 / Legendary 235 (pitch 75); scripts\collectio` |
| Common | ✅ `scripts\booster_info_popup.gd:85 desc.text = "Each pack opened adds +1 to the \"packs since last Legendary\" counter.\n\nA Legenda` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Rare | ✅ `scripts\booster_info_popup.gd:85 desc.text = "Each pack opened adds +1 to the \"packs since last Legendary\" counter.\n\nA Legenda` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Epic | ✅ `scripts\booster_info_popup.gd:85 desc.text = "Each pack opened adds +1 to the \"packs since last Legendary\" counter.\n\nA Legenda` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Legendary | ✅ `scripts\achievements.gd:32 ["upgrade_legendary", "Legendary Forger", "Upgrade 3 Legendary cards", "upgrade", 3, 350],; scripts\ach` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Army Icon | ✅ `scripts\campaign.gd:190 # 阵营图标 (原版 Army Icon); scripts\card_displayer.gd:489 # 阵营图标 (场景 Army Icon 80x85)` |
| Close | ✅ `scripts\battle.gd:81 const TEX_CLOSE := BATTLE_UI + "40k_bt_close.png"                      # Close按钮 175²; scripts\battle.gd:1258` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Sidebar | ✅ `scripts\deck_builder.gd:21 var _window_opts: Dictionary = {}  # 原版 Sidebar Window Options 3 键 (Cards/Deck info/Cosmetics); scripts` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Window Options | ✅ `scripts\deck_builder.gd:21 var _window_opts: Dictionary = {}  # 原版 Sidebar Window Options 3 键 (Cards/Deck info/Cosmetics); scripts` |
| Buttons | ✅ `scripts\battle.gd:2047 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Cards | ✅ `scripts\battle.gd:154 var _hand_box: Control   # 手牌容器 (原版 CardsInHand 弧形布局, 位置由 _layout_hand 计算); scripts\battle.gd:272 # 对战音效: 开局` |
| Highlight | ✅ `scripts\battle.gd:41 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:464 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Info | ✅ `scripts\achievements.gd:10 const TEX_CONTAINER := SPR + "UI_Deck_Information_submenu_Back.png"; scripts\base_event_popup.gd:40 # 红` |
| Highlight | ✅ `scripts\battle.gd:41 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:464 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Cosmetics | ✅ `scripts\collection.gd:206 ["Cosmetics", SPR + "40k_collection_bt_cosmetics.png", "res://scenes/cosmetics.tscn"],; scripts\deck_bui` |
| Highlight | ✅ `scripts\battle.gd:41 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:464 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1847 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Deck Name | ✅ `scripts\deck_builder.gd:219 # ===== Sidebar [0,156 335x924] (原版: Window Options + Deck Name + 卡组列表 + Done/30-30) =====; scripts\de` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Deck Details | ✅ `scripts\deck_info_popup.gd:4 ## 布局: 大窗口(UI_Deck_Information_Back) + 督军立绘 + Deck Details(卡组名/阵营图标/督军名); scripts\deck_info_popup.gd:` |
| Deck List drawer | ✅ `scripts\deck_builder.gd:433 # 卡组列表 (原版 Deck List drawer [0,366 325x644] Scroll View; 存引用供视图切换显隐)` |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Deck Selector Hero Card Info button | ✅ `scripts\deck_builder.gd:1952 # 督军行 (原版 Deck Selector Hero Card Info button 55.7px: -- Warlord -- 空槽或督军名, 点击选督军)` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Rarity Gradient | ✅ `scripts\deck_builder.gd:1477 # 稀有度渐变条 (原版 Rarity Gradient anchor(0.606,0,1,1) 右 40% 区域稀有度着色); scripts\deck_builder.gd:1651 # 稀有度渐变` |
| Background Border | ✅ `scripts\deck_builder.gd:1469 # 卡行边框 (原版 Background Border 40k_deck_cardlist_border 四边线); scripts\deck_builder.gd:1643 # 边框 (原版 Bac` |
| Card Name | ✅ `scripts\deck_builder.gd:1514 # 卡名 + 类型/稀有度 (锚定左 112 右 70, 原版 Card Name 34px); scripts\deck_builder.gd:1709 # 卡名 (原版 Card Name 34px` |
| Count | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Ban Icon | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —` |
| Background Slot Free | ✅ `scripts\deck_builder.gd:1666 # 空槽虚线底 (原版 Background Slot Free 40k_deck_cardlist_doted_bg 0.44 灰; 有卡时隐藏)` |
| Slot Free Text | ✅ `scripts\deck_builder.gd:1698 # 空槽提示 '-- Defensive --' (原版 Slot Free Text 34px)` |
| Deck Selector Defensive Card Slot | ✅ `scripts\deck_builder.gd:1599 # ---------- 防御卡槽 (原版 Deck Selector Defensive Card Slot, m_IsActive=true) ----------; scripts\deck_bu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Background Slot Free | ✅ `scripts\deck_builder.gd:1666 # 空槽虚线底 (原版 Background Slot Free 40k_deck_cardlist_doted_bg 0.44 灰; 有卡时隐藏)` |
| Slot Free Text | ✅ `scripts\deck_builder.gd:1698 # 空槽提示 '-- Defensive --' (原版 Slot Free Text 34px)` |
| Rarity Gradient | ✅ `scripts\deck_builder.gd:1477 # 稀有度渐变条 (原版 Rarity Gradient anchor(0.606,0,1,1) 右 40% 区域稀有度着色); scripts\deck_builder.gd:1651 # 稀有度渐变` |
| Background Border | ✅ `scripts\deck_builder.gd:1469 # 卡行边框 (原版 Background Border 40k_deck_cardlist_border 四边线); scripts\deck_builder.gd:1643 # 边框 (原版 Bac` |
| Cost Image | ✅ `scripts\deck_builder.gd:1492 # 费用图标 (原版 Cost Image: Card Frame Cost Icon 左竖条 + 数字 50px); scripts\deck_builder.gd:1676 # 费用图标 (原版 C` |
| Cost | ✅ `scripts\battle.gd:434 # 实时数值层 (原版 2DCard Card Info: Cost/Health/Melee/Armour 文字实时更新 —; scripts\battle.gd:437 ["Cost", Vector3(0.28` |
| banned Icon | ✅ `scripts\deck_info_popup.gd:416 # banned Icon (原版 40k_Combat_Icon_Cross 卡被禁时显示 X — 2026-08-21 审查补; 数据无禁用标记 → 常隐)` |
| Text fill | ⚠️ 未命中 |
| Card Name | ✅ `scripts\deck_builder.gd:1514 # 卡名 + 类型/稀有度 (锚定左 112 右 70, 原版 Card Name 34px); scripts\deck_builder.gd:1709 # 卡名 (原版 Card Name 34px` |
| Count | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Deck Selector Card Info button | ✅ `scripts\deck_builder.gd:1420 ## 原版卡行 (Deck Selector Card Info button, 86px 行高): PnP 卡面缩略+渐变条+费用图标+卡名+数量; scripts\deck_builder.gd:1` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Rarity Gradient | ✅ `scripts\deck_builder.gd:1477 # 稀有度渐变条 (原版 Rarity Gradient anchor(0.606,0,1,1) 右 40% 区域稀有度着色); scripts\deck_builder.gd:1651 # 稀有度渐变` |
| Background Border | ✅ `scripts\deck_builder.gd:1469 # 卡行边框 (原版 Background Border 40k_deck_cardlist_border 四边线); scripts\deck_builder.gd:1643 # 边框 (原版 Bac` |
| Cost Image | ✅ `scripts\deck_builder.gd:1492 # 费用图标 (原版 Cost Image: Card Frame Cost Icon 左竖条 + 数字 50px); scripts\deck_builder.gd:1676 # 费用图标 (原版 C` |
| Cost | ✅ `scripts\battle.gd:434 # 实时数值层 (原版 2DCard Card Info: Cost/Health/Melee/Armour 文字实时更新 —; scripts\battle.gd:437 ["Cost", Vector3(0.28` |
| banned Icon | ✅ `scripts\deck_info_popup.gd:416 # banned Icon (原版 40k_Combat_Icon_Cross 卡被禁时显示 X — 2026-08-21 审查补; 数据无禁用标记 → 常隐)` |
| Text fill | ⚠️ 未命中 |
| Card Name | ✅ `scripts\deck_builder.gd:1514 # 卡名 + 类型/稀有度 (锚定左 112 右 70, 原版 Card Name 34px); scripts\deck_builder.gd:1709 # 卡名 (原版 Card Name 34px` |
| Count | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Empty Warning | ✅ `scripts\deck_builder.gd:2003 # 注: 原版 Empty Warning 'Arraste as cartas aqui...' m_IsActive=false 默认隐藏 (2026-08-21 前` |
| Deck Information cost drawer | ✅ `scripts\deck_builder.gd:460 # 费用曲线 (原版 Deck Information cost drawer [88.8,411 158.1x199.1]: 9 行 18.9 高,; scripts\deck_builder.gd:4` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Deck CostQuanityt Row Drawer | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (1) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (2) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (3) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (4) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (5) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (6) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (7) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (8) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1248 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck Counter Drawer | ✅ `scripts\deck_builder.gd:446 # Troops/Stratagems 计数抽屉 (原版 Deck Counter Drawer x[0.3,335.6] y[761,861] 100 高,; scripts\deck_builder.` |
| Text (TMP) | ⚠️ 未命中 |
| Text (TMP) (1) | ⚠️ 未命中 |
| Cosmetic Drawer | ⚠️ 未命中 |
| Cosmetic | ✅ `scripts\collection.gd:206 ["Cosmetics", SPR + "40k_collection_bt_cosmetics.png", "res://scenes/cosmetics.tscn"],; scripts\cosmetic` |
| Footer | ✅ `scripts\deck_builder.gd:464 # 底部 Footer (原版 [0,1010 335x70]: Done [12.8..201.3, 9.3..59.5] 188.5x50.2 + 卡数图标 [201.3..251.3] 50x4; ` |
| Done | ✅ `scripts\deck_builder.gd:219 # ===== Sidebar [0,156 335x924] (原版: Window Options + Deck Name + 卡组列表 + Done/30-30) =====; scripts\de` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Done Highlight | ⚠️ 未命中 |
| Counter | ✅ `scripts\battle.gd:4441 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4479 # 攻击伤害数字 (原版 Damag` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| GameObject | ✅ `scenes\unity_arena_battlearena1.gd:2227 n_680.name = 'GameObject'` |
| Card Display | ✅ `scripts\battle.gd:1385 # ---------- 卡牌/督军详情弹窗 (原版 Card Display Window) ----------; scripts\battle.gd:1411 # 弹窗 (原版 Card Display 75` |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Reference Card Pointer | ⚠️ 未命中 |
| Card Filters | ✅ `scripts\collection.gd:153 # ---- 筛选栏 (原版 Card Filters [0.3,155.9 335.3x924.1] 覆盖 Tab 栏 — RectTransform_-2969573818119822635) -; sc` |
| Shadow | ✅ `scripts\battle.gd:41 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2758 # 悬浮` |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Name FIlter | ⚠️ 未命中 |
| Input Field | ✅ `scripts\choose_name.gd:8 const TEX_INPUT := SPR + "40K_dropdown_bg.png"              # Choose Name Input Field 底; scripts\choose_n` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Owned Toggle | ✅ `scripts\deck_builder.gd:608 # 拥有/可升级 Toggle (原版 Owned Toggle [50 高] 40_main_bt_toggle_on + 'Owned only' 32px)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Upgradable Toggle | ✅ `scripts\collection.gd:438 # 拥有/可升级 Toggle (原版 Owned/Upgradable Toggle 50 高: 40_main_bt_toggle_on 70.6 宽右 + 文字 32px 左)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Army Filter | ✅ `scripts\collection.gd:446 # 阵营 (原版 Army Filter: Title 'Army' 32px 50 高 + 100x100 图标块); scripts\collection.gd:573 ## 原版图标块 Toggle (` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Checkmark | ⚠️ 未命中 |
| Rarity FIlter | ✅ `scripts\deck_builder.gd:626 # 稀有度 (原版 Rarity FIlter 'Rarity' 32px + 4_40k_cardframe_rarity_* 50x50 + 名 23.2px); scripts\deck_build` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Checkmark | ⚠️ 未命中 |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Cost Filter | ✅ `scripts\collection.gd:471 # 能量费用筛选 (原版 Cost Filter: Title 50 高 + 65x65 Toggle 内 45px 数字); scripts\collection.gd:538 ## 能量费用筛选按钮 (原` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Checkmark | ⚠️ 未命中 |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Type Filter | ✅ `scripts\collection.gd:484 # 类型 (原版 Type Filter: Title 50 高 + 80x100 Toggle 内 50x50 图标 + 22 高名); scripts\collection.gd:673 ## 类型筛选图` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Checkmark | ⚠️ 未命中 |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Card Drag Controller | ⚠️ 未命中 |
| Deck Selector Card Info button | ✅ `scripts\deck_builder.gd:1420 ## 原版卡行 (Deck Selector Card Info button, 86px 行高): PnP 卡面缩略+渐变条+费用图标+卡名+数量; scripts\deck_builder.gd:1` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Card Name | ✅ `scripts\deck_builder.gd:1514 # 卡名 + 类型/稀有度 (锚定左 112 右 70, 原版 Card Name 34px); scripts\deck_builder.gd:1709 # 卡名 (原版 Card Name 34px` |
| Cost Image | ✅ `scripts\deck_builder.gd:1492 # 费用图标 (原版 Cost Image: Card Frame Cost Icon 左竖条 + 数字 50px); scripts\deck_builder.gd:1676 # 费用图标 (原版 C` |
| Cost | ✅ `scripts\battle.gd:434 # 实时数值层 (原版 2DCard Card Info: Cost/Health/Melee/Armour 文字实时更新 —; scripts\battle.gd:437 ["Cost", Vector3(0.28` |
| Cosmetic Display | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Cosmetic FIlter | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:41 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2758 # 悬浮` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Spacing | ✅ `scripts\battle.gd:1710 # MonoBehaviour_5271: m_useRotation=1 / m_betweenElementsSpacing=1.45×卡宽 / m_maxHeight=0.7×卡高 /; scripts\ba` |
| Army Filter | ✅ `scripts\collection.gd:446 # 阵营 (原版 Army Filter: Title 'Army' 32px 50 高 + 100x100 图标块); scripts\collection.gd:573 ## 原版图标块 Toggle (` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Checkmark | ⚠️ 未命中 |
| Spacing (1) | ⚠️ 未命中 |
| Owned Toggle | ✅ `scripts\deck_builder.gd:608 # 拥有/可升级 Toggle (原版 Owned Toggle [50 高] 40_main_bt_toggle_on + 'Owned only' 32px)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Cosmetic Drag Controller | ⚠️ 未命中 |
| Collection Cosmetic | ✅ `scripts\cosmetics.gd:2 ## 美容品界面 (原版 Collection Cosmetic 说明书: 250x405 卡背方块网格)` |
| content | ✅ `scripts\achievements.gd:138 sb.content_margin_left = 16; scripts\achievements.gd:139 sb.content_margin_right = 16` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |

## 摘要

- 规格元素: 247
- 代码命中: 219
- ⚠️未命中: 28 (以下需人工判断)

- `Generic Simplified UI Button_updated`
- `Text fill`
- `Text fill`
- `Deck CostQuanityt Row Drawer`
- `Deck CostQuanityt Row Drawer (1)`
- `Deck CostQuanityt Row Drawer (2)`
- `Deck CostQuanityt Row Drawer (3)`
- `Deck CostQuanityt Row Drawer (4)`
- `Deck CostQuanityt Row Drawer (5)`
- `Deck CostQuanityt Row Drawer (6)`
- `Deck CostQuanityt Row Drawer (7)`
- `Deck CostQuanityt Row Drawer (8)`
- `Text (TMP)`
- `Text (TMP) (1)`
- `Cosmetic Drawer`
- `Done Highlight`
- `Reference Card Pointer`
- `Name FIlter`
- `Checkmark`
- `Checkmark`
- `Checkmark`
- `Checkmark`
- `Card Drag Controller`
- `Cosmetic Display`
- `Cosmetic FIlter`
- `Checkmark`
- `Spacing (1)`
- `Cosmetic Drag Controller`