# UI 规格审计: Collection Menu Variant

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Collection Menu Variant [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Content Area [godot(x167.2 y70.9 w1752.8 h1009.1)]
    Background [godot(x167.2 y70.9 w1752.8 h1009.1)]
    Tab Buttons [godot(x167.2 y158.6 w165.0 h921.4)]
      Deck [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Deck godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1014.6 w35.0 h35.0)]
          OneText [godot(x201.4 y1015.5 w35.0 h35.0)]
      Cards [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Cards godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1014.6 w35.0 h35.0)]
          OneText [godot(x201.4 y1015.5 w35.0 h35.0)]
      CardBacks [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Cosmetics godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1014.6 w35.0 h35.0)]
          OneText [godot(x201.4 y1015.5 w35.0 h35.0)]
      Alternate Art [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Styles godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1014.6 w35.0 h35.0)]
          OneText [godot(x201.4 y1015.5 w35.0 h35.0)]
      Shadow [godot(x167.2 y158.6 w47.6 h921.4)]
    Tabs [godot(x167.2 y70.9 w1752.8 h1009.1)]
      Select Deck Tab [inactive godot(x167.2 y70.9 w1752.8 h1009.1)]
        Decks Tab [godot(x167.2 y70.9 w1752.8 h1009.1)]
          Collection Display [godot(x167.2 y70.9 w1752.8 h1009.1)]
            Deck Scroll View [godot(x330.9 y155.9 w1589.1 h924.1)]
              Viewport [godot(x330.9 y155.9 w1589.1 h924.1)]
                Content [godot(x330.9 y155.9 w1589.1 h200.0)]
              Empty Collection Warning [inactive godot(x165.9 y70.9 w1804.1 h1009.1)]
                Warning [txt=There are no deck in your collection for godot(x165.9 y70.9 w1804.1 h1009.1)]
            Deck Filters [godot(x0.1 y155.9 w335.5 h924.1)]
              Shadow [godot(x0.1 y155.9 w153.0 h924.1)]
              Filters [godot(x0.1 y155.9 w335.5 h924.1)]
                Deck Name Filter [godot(x0.1 y155.9 w335.5 h80.0)]
                  Input Field [godot(x27.2 y175.9 w281.2 h40.0)]
                    Text Area [godot(x37.2 y182.9 w231.2 h27.0)]
                      Placeholder [txt=Search godot(x37.2 y177.9 w231.2 h37.0)]
                      Text [txt=​ godot(x37.2 y177.9 w231.2 h37.0)]
                    Image [godot(x268.4 y180.9 w35.0 h30.0)]
                Army Filter [godot(x0.1 y235.9 w335.5 h345.0)]
                  Title [txt=Army godot(x25.1 y240.9 w310.5 h50.0)]
                  Content [godot(x0.1 y300.9 w335.5 h280.0)]
                    Toggle [godot(x14.1 y300.9 w100.0 h100.0)]
                      Background [godot(x14.1 y300.9 w100.0 h100.0)]
                        Checkmark [inactive godot(x14.1 y300.9 w100.0 h100.0)]
        Select Game Mode Deck Tab [godot(x330.8 y155.9 w1589.2 h924.1)]
          Title Header [txt=SELECT GAME MODE DECK godot(x426.1 y155.9 w1398.6 h87.6)]
          Scroll View [godot(x330.8 y260.9 w1589.2 h802.3)]
            Viewport [godot(x330.8 y260.9 w1589.2 h802.3)]
              Content [godot(x1125.4 y261.1 w0.0 h802.0)]
        Header [godot(x167.2 y70.9 w1752.8 h85.0)]
          Filter Toggle [godot(x367.2 y88.4 w50.0 h50.0)]
            label [txt=Filters godot(x437.2 y88.4 w150.0 h50.0)]
            icon detail [godot(x377.2 y98.4 w30.0 h30.0)]
          Control Buttons [godot(x1180.0 y80.9 w740.0 h60.0)]
            Create [godot(x1661.0 y80.9 w245.0 h60.0)]
              Button Text [txt=Create Deck godot(x1672.7 y82.2 w220.8 h57.5)]
            Import [godot(x1391.0 y80.9 w245.0 h60.0)]
              Button Text [txt=Import Deck godot(x1402.7 y82.2 w220.8 h57.5)]
            Unlock [godot(x1180.0 y80.9 w186.0 h60.0)]
              Button Outline [godot(x1180.5 y80.9 w185.0 h60.0)]
              Text [txt=Debug Unlock godot(x1188.4 y89.5 w169.2 h42.8)]
          Separator Line [godot(x167.2 y150.9 w1752.8 h10.0)]
          Filters [godot(x592.2 y70.9 w0.0 h85.0)]
            Clear Filter Button [godot(x612.2 y83.4 w250.0 h60.0)]
              Button Text [txt=Clear filters godot(x626.1 y84.6 w221.4 h57.7)]
      CardsTab [inactive godot(x167.2 y70.9 w1752.8 h1009.1)]
        Collection Display [godot(x167.2 y70.9 w1752.8 h1009.1)]
          Scroll View [godot(x330.2 y155.9 w1589.8 h924.1)]
            Viewport [godot(x330.2 y155.9 w1589.8 h924.1)]
              Content [godot(x330.2 y155.9 w1589.8 h300.0)]
            Empty Collection Warning [inactive godot(x135.2 y70.9 w1834.8 h1009.1)]
              Warning [txt=There are no cards in your collection fo godot(x135.2 y70.9 w1834.8 h1009.1)]
          Card Filters [godot(x0.3 y155.9 w335.3 h924.1)]
            Shadow [godot(x0.3 y155.9 w152.8 h924.1)]
            Scroll View [godot(x0.3 y155.9 w335.3 h924.1)]
              Viewport [godot(x0.3 y155.9 w335.3 h924.1)]
                Filters [godot(x0.3 y155.9 w335.3 h989.1)]
                  Name FIlter [godot(x0.3 y155.9 w335.3 h79.1)]
                    Input Field [godot(x27.3 y175.4 w281.2 h40.0)]
                      Text Area [godot(x37.3 y182.4 w231.2 h27.0)]
                        Placeholder [txt=Search godot(x37.3 y177.4 w231.2 h37.0)]
                        Text [txt=​ godot(x37.3 y177.4 w231.2 h37.0)]
                      Image [godot(x268.5 y180.4 w35.0 h30.0)]
                  Owned Toggle [godot(x0.3 y235.0 w335.3 h50.0)]
                    Image [godot(x240.0 y235.0 w70.6 h50.0)]
                    Label [txt=Owned only godot(x25.3 y235.0 w209.7 h50.0)]
                  Upgradable Toggle [godot(x0.3 y285.0 w335.3 h50.0)]
                    Image [godot(x240.0 y285.0 w70.6 h50.0)]
                    Label [txt=Upgradable only godot(x25.3 y285.0 w209.7 h50.0)]
                  Army Filter [godot(x0.3 y335.0 w335.3 h150.0)]
                    Title [txt=Army godot(x0.3 y335.0 w335.3 h50.0)]
                    Content [godot(x0.3 y385.0 w335.3 h100.0)]
                      Toggle [godot(x14.3 y385.0 w100.0 h100.0)]
                        Background [godot(x14.3 y385.0 w100.0 h100.0)]
                          Checkmark [inactive godot(x14.3 y385.0 w100.0 h100.0)]
                  Rarity FIlter [godot(x0.3 y485.0 w335.3 h280.0)]
                    Title [txt=Rarity godot(x25.3 y510.0 w310.3 h50.0)]
                    Content [godot(x0.3 y550.0 w335.3 h215.0)]
                      Toggle [godot(x14.3 y550.0 w100.0 h100.0)]
                        Background [godot(x39.3 y575.0 w50.0 h50.0)]
                          Checkmark [inactive godot(x39.3 y575.0 w50.0 h50.0)]
                        Label [txt=Legendary godot(x14.3 y628.0 w100.0 h22.0)]
                  Cost Filter [godot(x0.3 y765.0 w335.3 h230.0)]
                    Title [txt=Energy Cost godot(x25.3 y780.0 w310.3 h50.0)]
                    Content [godot(x0.3 y830.0 w335.3 h165.0)]
                      Toggle [godot(x15.3 y830.0 w65.0 h65.0)]
                        Background [godot(x15.3 y830.0 w65.0 h65.0)]
                          Checkmark [inactive godot(x15.3 y830.0 w65.0 h65.0)]
                          Label [txt=0 godot(x15.3 y830.0 w65.0 h65.0)]
                  Type Filter [godot(x0.3 y995.0 w335.3 h150.0)]
                    Title [txt=Type godot(x25.3 y1000.0 w310.3 h50.0)]
                    Content [godot(x0.3 y995.0 w335.3 h150.0)]
                      Toggle [godot(x15.3 y1045.0 w80.0 h100.0)]
                        Background [godot(x30.3 y1070.0 w50.0 h50.0)]
                          Checkmark [inactive godot(x30.3 y1070.0 w50.0 h50.0)]
                        Label [txt=Warlord godot(x15.3 y1123.0 w80.0 h22.0)]
          Reference Card Pointer [godot(x402.3 y236.4 w193.8 h45.0)]
        Header Filters [godot(x167.2 y70.9 w1752.8 h85.0)]
          Filter Toggle [godot(x367.2 y88.4 w50.0 h50.0)]
            label [txt=Filters godot(x437.2 y88.4 w150.0 h50.0)]
            icon detail [godot(x377.2 y98.4 w30.0 h30.0)]
          Separator Line [godot(x167.2 y150.9 w1752.8 h10.0)]
          Filters [godot(x592.2 y70.9 w0.0 h85.0)]
            Clear Filter Button [godot(x612.2 y83.4 w250.0 h60.0)]
              Button Text [txt=Clear filters godot(x626.1 y84.6 w221.4 h57.7)]
          WIldcard Display [godot(x1470.0 y70.9 w400.0 h85.0)]
            Background [godot(x1550.0 y91.4 w320.0 h44.0)]
            Counters [godot(x1555.0 y91.4 w315.0 h44.0)]
              Common [godot(x1565.0 y91.4 w65.0 h44.0)]
                Icon [godot(x1565.0 y91.4 w30.0 h44.0)]
                Counter [txt=999 godot(x1595.0 y91.4 w41.0 h44.0)]
              Rare [godot(x1640.0 y91.4 w65.0 h44.0)]
                Icon [godot(x1640.0 y91.4 w30.0 h44.0)]
                Counter [txt=999 godot(x1670.0 y91.4 w41.0 h44.0)]
              Epic [godot(x1715.0 y91.4 w65.0 h44.0)]
                Icon [godot(x1715.0 y91.4 w30.0 h44.0)]
                Counter [txt=999 godot(x1745.0 y91.4 w41.0 h44.0)]
              Legendary [godot(x1790.0 y91.4 w65.0 h44.0)]
                Icon [godot(x1790.0 y91.4 w30.0 h44.0)]
                Counter [txt=999 godot(x1820.0 y91.4 w41.0 h44.0)]
            Army Icon [godot(x1470.0 y70.9 w80.0 h85.0)]
      Cardback Tab [godot(x167.2 y70.9 w1752.8 h1009.1)]
        Cardback Display [godot(x167.2 y70.9 w1752.8 h1009.1)]
          Scroll View [godot(x335.4 y155.9 w1584.6 h924.1)]
            Viewport [godot(x335.4 y155.9 w1584.6 h924.1)]
              Content [godot(x335.4 y155.9 w1584.6 h200.0)]
            Empty Collection Warning [inactive godot(x170.4 y70.9 w1799.6 h1009.1)]
              Warning [txt=There are no cardbacks in your collectio godot(x170.4 y70.9 w1799.6 h1009.1)]
          Cosmetic FIlter [inactive godot(x0.1 y155.9 w335.5 h924.1)]
            Shadow [godot(x0.1 y155.9 w153.0 h924.1)]
            Filters [godot(x0.1 y155.9 w335.5 h924.1)]
              Spacing [godot(x0.1 y155.9 w335.5 h15.0)]
              Owned Toggle (1) [godot(x0.1 y170.9 w335.5 h50.0)]
                Image [godot(x239.9 y170.9 w70.7 h50.0)]
                Label [txt=Owned only godot(x25.1 y170.9 w209.8 h50.0)]
              Army Filter [godot(x0.1 y220.9 w335.5 h345.0)]
                Title [txt=Army godot(x25.1 y225.9 w310.5 h50.0)]
                Content [godot(x0.1 y285.9 w335.5 h280.0)]
                  Toggle [godot(x14.1 y285.9 w100.0 h100.0)]
                    Background [godot(x14.1 y285.9 w100.0 h100.0)]
                      Checkmark [inactive godot(x14.1 y285.9 w100.0 h100.0)]
        Header [godot(x167.2 y70.9 w1752.8 h85.0)]
          Filter Toggle [godot(x367.2 y88.4 w50.0 h50.0)]
            label [txt=Filters godot(x437.2 y88.4 w150.0 h50.0)]
            icon detail [godot(x377.2 y98.4 w30.0 h30.0)]
          Separator Line [godot(x167.2 y150.9 w1752.8 h10.0)]
          label [txt=Your cosmetics collection godot(x1821.0 y80.9 w0.0 h60.0)]
          Filters [godot(x592.2 y70.9 w876.4 h85.0)]
            Clear Filter Button [godot(x1488.6 y83.4 w250.0 h60.0)]
              Button Text [txt=Clear filters godot(x1502.5 y89.3 w221.4 h48.3)]
      Alternate Art Tab [inactive godot(x167.2 y70.9 w1752.8 h1009.1)]
        Collection Display [godot(x167.2 y70.9 w1752.8 h1009.1)]
          Scroll View [godot(x330.2 y287.7 w1589.8 h792.3)]
            Viewport [godot(x330.2 y287.7 w1589.8 h792.3)]
              Content [godot(x330.2 y287.7 w1589.8 h300.0)]
            Empty Collection Warning [inactive godot(x330.2 y287.7 w1589.8 h792.3)]
              Warning [txt=There are no cards in your collection fo godot(x330.2 y287.7 w1589.8 h792.3)]
          Card Filters [godot(x0.3 y155.9 w335.3 h924.1)]
            Shadow [godot(x0.3 y155.9 w152.8 h924.1)]
            Scroll View [godot(x0.3 y155.9 w335.3 h924.1)]
              Viewport [godot(x0.3 y155.9 w335.3 h924.1)]
                Filters [godot(x0.3 y155.9 w335.3 h989.1)]
                  Name FIlter [godot(x0.3 y155.9 w335.3 h79.1)]
                    Input Field [godot(x27.3 y175.4 w281.2 h40.0)]
                      Text Area [godot(x37.3 y182.4 w231.2 h27.0)]
                        Placeholder [txt=Search godot(x37.3 y177.4 w231.2 h37.0)]
                        Text [txt=​ godot(x37.3 y177.4 w231.2 h37.0)]
                      Image [godot(x268.5 y180.4 w35.0 h30.0)]
                  Owned Toggle [godot(x0.3 y235.0 w335.3 h50.0)]
                    Image [godot(x240.0 y235.0 w70.6 h50.0)]
                    Label [txt=Owned only godot(x25.3 y235.0 w209.7 h50.0)]
                  Upgradable Toggle [godot(x0.3 y285.0 w335.3 h50.0)]
                    Image [godot(x240.0 y285.0 w70.6 h50.0)]
                    Label [txt=Upgradable only godot(x25.3 y285.0 w209.7 h50.0)]
                  Army Filter [godot(x0.3 y335.0 w335.3 h150.0)]
                    Title [txt=Army godot(x0.3 y335.0 w335.3 h50.0)]
                    Content [godot(x0.3 y385.0 w335.3 h100.0)]
                      Toggle [godot(x14.3 y385.0 w100.0 h100.0)]
                        Background [godot(x14.3 y385.0 w100.0 h100.0)]
                          Checkmark [inactive godot(x14.3 y385.0 w100.0 h100.0)]
                  Rarity FIlter [godot(x0.3 y485.0 w335.3 h280.0)]
                    Title [txt=Rarity godot(x25.3 y510.0 w310.3 h50.0)]
                    Content [godot(x0.3 y550.0 w335.3 h215.0)]
                      Toggle [godot(x14.3 y550.0 w100.0 h100.0)]
                        Background [godot(x39.3 y575.0 w50.0 h50.0)]
                          Checkmark [inactive godot(x39.3 y575.0 w50.0 h50.0)]
                        Label [txt=Legendary godot(x14.3 y628.0 w100.0 h22.0)]
                  Cost Filter [godot(x0.3 y765.0 w335.3 h230.0)]
                    Title [txt=Energy Cost godot(x25.3 y780.0 w310.3 h50.0)]
                    Content [godot(x0.3 y830.0 w335.3 h165.0)]
                      Toggle [godot(x15.3 y830.0 w65.0 h65.0)]
                        Background [godot(x15.3 y830.0 w65.0 h65.0)]
                          Checkmark [inactive godot(x15.3 y830.0 w65.0 h65.0)]
                          Label [txt=0 godot(x15.3 y830.0 w65.0 h65.0)]
                  Type Filter [godot(x0.3 y995.0 w335.3 h150.0)]
                    Title [txt=Type godot(x25.3 y1000.0 w310.3 h50.0)]
                    Content [godot(x0.3 y995.0 w335.3 h150.0)]
                      Toggle [godot(x15.3 y1045.0 w80.0 h100.0)]
                        Background [godot(x30.3 y1070.0 w50.0 h50.0)]
                          Checkmark [inactive godot(x30.3 y1070.0 w50.0 h50.0)]
                        Label [txt=Warlord godot(x15.3 y1123.0 w80.0 h22.0)]
        Header Filters [godot(x167.2 y70.9 w1752.8 h85.0)]
          Filter Toggle [godot(x367.2 y88.4 w50.0 h50.0)]
            label [txt=Filters godot(x437.2 y88.4 w150.0 h50.0)]
            icon detail [godot(x377.2 y98.4 w30.0 h30.0)]
          Separator Line [godot(x167.2 y150.9 w1752.8 h10.0)]
          Filters [godot(x592.2 y70.9 w-0.2 h85.0)]
            Clear Filter Button [godot(x612.0 y83.4 w250.0 h60.0)]
              Button Text [txt=Clear filters godot(x625.9 y84.6 w221.4 h57.7)]
        Header [godot(x332.3 y155.9 w1587.7 h128.0)]
          Select Art Button Right [godot(x1320.4 y190.7 w74.4 h75.6)]
            Background [godot(x1328.5 y198.6 w56.9 h58.2)]
            Icon [godot(x1328.5 y198.6 w56.9 h58.2)]
          Select Art Button Left [godot(x683.4 y190.7 w74.4 h75.6)]
            Background [godot(x691.5 y198.6 w56.9 h58.2)]
            Icon [godot(x691.5 y198.6 w56.9 h58.2)]
          Art Style Logo [godot(x787.6 y155.9 w512.0 h128.0)]
          Separator Line (1) [godot(x339.4 y281.9 w1580.6 h8.5)]
      Shared [godot(x167.2 y70.9 w1752.8 h1009.1)]
        Close Button [godot(x192.2 y83.4 w150.0 h60.0)]
          Button Text [txt=Back godot(x200.5 y89.3 w132.9 h48.2)]
    Shadow (1) [inactive godot(x330.4 y70.9 w49.4 h1009.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Collection Menu Variant | ⚠️ 未命中 |
| Content Area | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\rewards.gd:145` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Tab Buttons | ✅ `scripts\collection.gd:150 # ---- Tab Buttons (原版 [167.2,158.6 165x921.4] 左竖排 4 tab — RectTransform_-1995773233925987627) ----; scr` |
| Deck | ✅ `scripts\achievements.gd:10 const TEX_CONTAINER := SPR + "UI_Deck_Information_submenu_Back.png"; scripts\achievements.gd:36 ["deck_` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Cards | ✅ `scripts\battle.gd:155 var _hand_box: Control   # 手牌容器 (原版 CardsInHand 弧形布局, 位置由 _layout_hand 计算); scripts\battle.gd:273 # 对战音效: 开局` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| CardBacks | ✅ `scripts\collection.gd:198 ## 左侧 4 Tab (说明书 Tab Buttons: Deck/Cards/CardBacks/Alternate Art 4 键各 165x180,; scripts\deck_collection.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Alternate Art | ✅ `scripts\collection.gd:198 ## 左侧 4 Tab (说明书 Tab Buttons: Deck/Cards/CardBacks/Alternate Art 4 键各 165x180,; scripts\collection.gd:20` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| Tabs | ✅ `scripts\shop.gd:163 # 3 个标签页 (Tabs 区 x330-1920)` |
| Select Deck Tab | ✅ `scripts\deck_collection.gd:7 ## 网格参数 = 原版 Select Deck Tab GridLayoutGroup (cellSize 225×364.5, spacing 20, padding L10;; scripts\d` |
| Decks Tab | ⚠️ 未命中 |
| Collection Display | ⚠️ 未命中 |
| Deck Scroll View | ✅ `scripts\deck_collection.gd:173 # ---- 网格 (原版 Select Deck Tab Deck Scroll View [330.9,155.9 1589.1x924.1] 直达右缘 — RectTransform_6413` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Deck Filters | ✅ `scripts\deck_collection.gd:170 # ---- 筛选栏 (原版 Deck Filters [0.1,155.9 335.5x924.1] 覆盖 Tab 栏 — RectTransform_6750859933904003797) -` |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Deck Name Filter | ✅ `scripts\deck_collection.gd:328 ## 内容仅 Deck Name Filter 搜索 + Army Filter 阵营图标 — RectTransform_6750859933904003797); scripts\deck_co` |
| Input Field | ✅ `scripts\choose_name.gd:8 const TEX_INPUT := SPR + "40K_dropdown_bg.png"              # Choose Name Input Field 底; scripts\choose_n` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Army Filter | ✅ `scripts\collection.gd:446 # 阵营 (原版 Army Filter: Title 'Army' 32px 50 高 + 100x100 图标块); scripts\collection.gd:573 ## 原版图标块 Toggle (` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Checkmark | ⚠️ 未命中 |
| Select Game Mode Deck Tab | ⚠️ 未命中 |
| Title Header | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Filter Toggle | ✅ `scripts\collection.gd:93 # Filter Toggle (原版 [367.2,88.4 50x50] 40k_menu_bt + 40k_bt_icon_search 30x30 — RectTransform_300943; scr` |
| label | ✅ `scripts\achievements.gd:113 _make_label(self, "Achievements", Vector2(240, 40), Vector2(400, 44), 28, Color(0.969, 0.914, 0.714); ` |
| icon detail | ⚠️ 未命中 |
| Control Buttons | ✅ `scripts\deck_collection.gd:124 # Control Buttons (原版 [1180,80.9 740x60]: Unlock 186x60 @ x[1180,1366] / Import 245x60 @ x[1391,163` |
| Create | ✅ `scripts\card_displayer.gd:595 SFX.play("CreateCard")  # 原版音效库 CreateCard_1 (卡牌生成); scripts\card_displayer.gd:595 SFX.play("CreateC` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Import | ✅ `scripts\deck_collection.gd:124 # Control Buttons (原版 [1180,80.9 740x60]: Unlock 186x60 @ x[1180,1366] / Import 245x60 @ x[1391,163` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Unlock | ✅ `scripts\deck_collection.gd:124 # Control Buttons (原版 [1180,80.9 740x60]: Unlock 186x60 @ x[1180,1366] / Import 245x60 @ x[1391,163` |
| Button Outline | ⚠️ 未命中 |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Clear Filter Button | ✅ `scripts\collection.gd:809 ## 清除全部筛选 (原版 Clear Filter Button 'Clear filters'); scripts\deck_builder.gd:186 # 清除筛选 (原版 Clear Filter ` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| CardsTab | ✅ `scripts\collection.gd:11 const ITEM_SIZE := Vector2(393.75, 576)  # JSON CardsTab 网格 _cellWidth 262.5 _cellHeight 384 _segmen; scr` |
| Collection Display | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Card Filters | ✅ `scripts\collection.gd:153 # ---- 筛选栏 (原版 Card Filters [0.3,155.9 335.3x924.1] 覆盖 Tab 栏 — RectTransform_-2969573818119822635) -; sc` |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
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
| Reference Card Pointer | ⚠️ 未命中 |
| Header Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Filter Toggle | ✅ `scripts\collection.gd:93 # Filter Toggle (原版 [367.2,88.4 50x50] 40k_menu_bt + 40k_bt_icon_search 30x30 — RectTransform_300943; scr` |
| label | ✅ `scripts\achievements.gd:113 _make_label(self, "Achievements", Vector2(240, 40), Vector2(400, 44), 28, Color(0.969, 0.914, 0.714); ` |
| icon detail | ⚠️ 未命中 |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Clear Filter Button | ✅ `scripts\collection.gd:809 ## 清除全部筛选 (原版 Clear Filter Button 'Clear filters'); scripts\deck_builder.gd:186 # 清除筛选 (原版 Clear Filter ` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| WIldcard Display | ✅ `scripts\collection.gd:138 # 通配符计数条 (原版 WIldcard Display [1470,70.9 400x85] — RectTransform_-4030683010239044907); scripts\collecti` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Counters | ✅ `scripts\card_displayer.gd:509 # 原版 Counters 组相对 1555: Common 10 / Rare 85 / Epic 160 / Legendary 235 (pitch 75); scripts\collectio` |
| Common | ✅ `scripts\booster_info_popup.gd:85 desc.text = "Each pack opened adds +1 to the \"packs since last Legendary\" counter.\n\nA Legenda` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Rare | ✅ `scripts\booster_info_popup.gd:85 desc.text = "Each pack opened adds +1 to the \"packs since last Legendary\" counter.\n\nA Legenda` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Epic | ✅ `scripts\booster_info_popup.gd:85 desc.text = "Each pack opened adds +1 to the \"packs since last Legendary\" counter.\n\nA Legenda` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Legendary | ✅ `scripts\achievements.gd:32 ["upgrade_legendary", "Legendary Forger", "Upgrade 3 Legendary cards", "upgrade", 3, 350],; scripts\ach` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Counter | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Army Icon | ✅ `scripts\campaign.gd:190 # 阵营图标 (原版 Army Icon); scripts\card_displayer.gd:489 # 阵营图标 (场景 Army Icon 80x85)` |
| Cardback Tab | ⚠️ 未命中 |
| Cardback Display | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Cosmetic FIlter | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Spacing | ✅ `scripts\battle.gd:1711 # MonoBehaviour_5271: m_useRotation=1 / m_betweenElementsSpacing=1.45×卡宽 / m_maxHeight=0.7×卡高 /; scripts\ba` |
| Owned Toggle (1) | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Army Filter | ✅ `scripts\collection.gd:446 # 阵营 (原版 Army Filter: Title 'Army' 32px 50 高 + 100x100 图标块); scripts\collection.gd:573 ## 原版图标块 Toggle (` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Checkmark | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Filter Toggle | ✅ `scripts\collection.gd:93 # Filter Toggle (原版 [367.2,88.4 50x50] 40k_menu_bt + 40k_bt_icon_search 30x30 — RectTransform_300943; scr` |
| label | ✅ `scripts\achievements.gd:113 _make_label(self, "Achievements", Vector2(240, 40), Vector2(400, 44), 28, Color(0.969, 0.914, 0.714); ` |
| icon detail | ⚠️ 未命中 |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| label | ✅ `scripts\achievements.gd:113 _make_label(self, "Achievements", Vector2(240, 40), Vector2(400, 44), 28, Color(0.969, 0.914, 0.714); ` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Clear Filter Button | ✅ `scripts\collection.gd:809 ## 清除全部筛选 (原版 Clear Filter Button 'Clear filters'); scripts\deck_builder.gd:186 # 清除筛选 (原版 Clear Filter ` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Alternate Art Tab | ✅ `scripts\collection.gd:207 # 原版 Alternate Art Tab 显示 'Styles'` |
| Collection Display | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Empty Collection Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Warning | ✅ `scripts\collection.gd:744 # 空态警告 (原版 Empty Collection Warning 'There are no cards in your collection for the selected filte'; scri` |
| Card Filters | ✅ `scripts\collection.gd:153 # ---- 筛选栏 (原版 Card Filters [0.3,155.9 335.3x924.1] 覆盖 Tab 栏 — RectTransform_-2969573818119822635) -; sc` |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
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
| Header Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Filter Toggle | ✅ `scripts\collection.gd:93 # Filter Toggle (原版 [367.2,88.4 50x50] 40k_menu_bt + 40k_bt_icon_search 30x30 — RectTransform_300943; scr` |
| label | ✅ `scripts\achievements.gd:113 _make_label(self, "Achievements", Vector2(240, 40), Vector2(400, 44), 28, Color(0.969, 0.914, 0.714); ` |
| icon detail | ⚠️ 未命中 |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Filters | ✅ `scripts\collection.gd:77 # ===== Header (原版 Header Filters [167.2,70.9 1752.8x85] — 原始 JSON RectTransform_-323071777530210641; scr` |
| Clear Filter Button | ✅ `scripts\collection.gd:809 ## 清除全部筛选 (原版 Clear Filter Button 'Clear filters'); scripts\deck_builder.gd:186 # 清除筛选 (原版 Clear Filter ` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Select Art Button Right | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Select Art Button Left | ✅ `scripts\card_displayer.gd:453 # 左右选择按钮 (原版 Select Art Button Left/Right 74x76, 无替换样式 → 禁用)` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Art Style Logo | ⚠️ 未命中 |
| Separator Line (1) | ⚠️ 未命中 |
| Shared | ✅ `scripts\collection.gd:78 # Close/Back (原版 Shared Close Button [192.2,83.4 150x60] UI_Button_Mulligan 'Back' 40px — RectTransf; scr` |
| Close Button | ✅ `scripts\booster_info_popup.gd:146 # 关闭按钮 (原版 Generic Close Button Orange); scripts\collection.gd:78 # Close/Back (原版 Shared Close ` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Shadow (1) | ✅ `scripts\collection.gd:219 # 右缘阴影 (原版 Shadow (1) [330.4,70.9 49.4x1009.1] 黑 0.47 — 2026-08-21 审查修正 0.31)` |

## 摘要

- 规格元素: 255
- 代码命中: 219
- ⚠️未命中: 36 (以下需人工判断)

- `Collection Menu Variant`
- `OneText`
- `OneText`
- `OneText`
- `OneText`
- `Decks Tab`
- `Collection Display`
- `Checkmark`
- `Select Game Mode Deck Tab`
- `Title Header`
- `icon detail`
- `Button Outline`
- `Collection Display`
- `Name FIlter`
- `Checkmark`
- `Checkmark`
- `Checkmark`
- `Checkmark`
- `Reference Card Pointer`
- `icon detail`
- `Cardback Tab`
- `Cardback Display`
- `Cosmetic FIlter`
- `Owned Toggle (1)`
- `Checkmark`
- `icon detail`
- `Collection Display`
- `Name FIlter`
- `Checkmark`
- `Checkmark`
- `Checkmark`
- `Checkmark`
- `icon detail`
- `Select Art Button Right`
- `Art Style Logo`
- `Separator Line (1)`