# UI 规格审计: Daily Reward Popup

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 16:44
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Daily Reward Popup [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
    Image [inactive godot(x0.0 y0.0 w1920.0 h1080.0)]
  Tracks [godot(x231.0 y152.8 w1716.6 h812.1)]
    bg [godot(x242.4 y159.3 w1676.4 h399.6)]
    Separator Line Top [godot(x245.7 y153.5 w1673.1 h14.9)]
    Separator Line Bottom [godot(x245.7 y949.3 w1673.1 h14.9)]
    Rewards Scroll View [godot(x242.4 y159.3 w1705.2 h805.6)]
      Viewport [godot(x242.4 y159.3 w1705.2 h805.6)]
        Rewards Content [godot(x242.4 y132.1 w0.0 h812.1)]
          Daily Reward Popup Entry [godot(x84.9 y538.1 w315.0 h812.1)]
            NormalReward [godot(x111.4 y574.9 w261.9 h338.5)]
              BG [godot(x124.5 y591.9 w235.7 h304.6)]
              Highlight [sprite=OctagonUI Border SDF 2 godot(x59.9 y525.9 w364.9 h436.5)]
              Reward Holder [godot(x127.7 y608.9 w229.3 h234.6)]
                Icon Container Drawer Variant [godot(x127.7 y608.9 w229.3 h234.6)]
                  Content [godot(x127.7 y608.9 w229.3 h234.6)]
                    Image [godot(x116.3 y597.2 w252.2 h258.1)]
                    Converted Drawer [inactive godot(x192.7 y894.7 w99.3 h5.4)]
                      Price Display [godot(x212.7 y891.5 w365.6 h74.8)]
                        icon [godot(x314.5 y891.5 w74.9 h74.8)]
                        text [txt=2000 godot(x389.4 y891.5 w87.1 h74.8)]
                      AlreadyOwned [txt=Already Owned godot(x39.6 y943.3 w405.6 h86.4)]
                    Ephemeral Drawer [inactive godot(x192.7 y894.7 w99.3 h5.4)]
                      Price Display [godot(x212.7 y928.9 w365.6 h0.0)]
                        icon [godot(x175.3 y928.9 w74.9 h0.0)]
                        text [txt=24 hours godot(x432.9 y928.9 w0.0 h74.8)]
              EverguildTextMeshPro [txt=1 Booster pack godot(x128.2 y843.5 w228.3 h42.1)]
              Extra Reward Indicator [inactive godot(x284.4 y589.2 w80.0 h80.0)]
              Shadow [inactive godot(x124.5 y591.9 w235.7 h304.6)]
              Premium Indicator [godot(x119.5 y589.2 w101.3 h100.5)]
                Image [godot(x136.7 y602.5 w26.8 h37.0)]
              Gacha Reward Claimed [godot(x122.9 y610.7 w192.3 h53.3)]
                Claimed Tex [txt=Recogido godot(x128.3 y621.3 w173.0 h31.8)]
              colider [godot(x124.5 y591.9 w235.7 h304.6)]
            Premium Reward [godot(x111.4 y969.4 w261.9 h338.5)]
              BG [godot(x124.5 y986.4 w235.7 h304.6)]
              Highlight [sprite=OctagonUI Border SDF 2 godot(x59.9 y920.4 w364.9 h436.5)]
              Reward Holder [godot(x127.7 y1003.4 w229.3 h234.6)]
                Icon Container Drawer Variant [godot(x127.7 y1003.4 w229.3 h234.6)]
                  Content [godot(x127.7 y1003.4 w229.3 h234.6)]
                    Image [godot(x116.3 y991.7 w252.2 h258.0)]
                    Converted Drawer [inactive godot(x192.7 y1289.2 w99.3 h5.4)]
                      Price Display [godot(x212.7 y1285.9 w365.6 h74.9)]
                        icon [godot(x314.5 y1285.9 w74.9 h74.9)]
                        text [txt=2000 godot(x389.4 y1285.9 w87.1 h74.9)]
                      AlreadyOwned [txt=Already Owned godot(x39.6 y1337.8 w405.6 h86.4)]
                    Ephemeral Drawer [inactive godot(x192.7 y1289.2 w99.3 h5.4)]
                      Price Display [godot(x212.7 y1323.4 w365.6 h0.0)]
                        icon [godot(x175.3 y1323.4 w74.9 h0.0)]
                        text [txt=24 hours godot(x432.9 y1323.4 w0.0 h74.8)]
              EverguildTextMeshPro [txt=1 Booster pack godot(x128.2 y1238.0 w228.3 h42.1)]
              Extra Reward Indicator [inactive godot(x284.4 y983.7 w80.0 h80.0)]
              Shadow [inactive godot(x124.5 y986.4 w235.7 h304.6)]
              Premium Indicator [godot(x119.5 y983.7 w101.3 h100.5)]
                Image [godot(x136.7 y997.0 w26.8 h37.0)]
              Gacha Reward Claimed [godot(x122.9 y1005.2 w192.3 h53.3)]
                Claimed Tex [txt=Recogido godot(x128.3 y1015.7 w173.0 h31.9)]
              colider [godot(x124.5 y986.4 w235.7 h304.6)]
            Personal Progression [godot(x84.9 y894.2 w315.0 h100.0)]
              Progress Bar [inactive godot(x20.4 y934.8 w222.0 h10.5)]
                Background [godot(x20.4 y934.8 w222.0 h10.5)]
                Fill [godot(x20.4 y934.8 w222.0 h10.5)]
                Handle Slide Area [inactive godot(x20.4 y934.8 w212.0 h10.5)]
                  Handle [godot(x226.5 y923.6 w11.7 h32.9)]
              Image [godot(x208.4 y896.9 w68.0 h88.0)]
                Counter [txt=1 godot(x199.9 y896.9 w85.0 h88.0)]
            Culling Reference Object [godot(x1.4 y538.1 w398.5 h812.1)]
            Day Title [txt=Day 3 godot(x112.4 y548.8 w259.9 h42.8)]
          Daily Reward Popup Entry (1) [godot(x84.9 y538.1 w315.0 h812.1)]
            NormalReward [godot(x111.4 y574.9 w261.9 h338.5)]
              BG [godot(x124.5 y591.9 w235.7 h304.6)]
              Highlight [sprite=OctagonUI Border SDF 2 godot(x59.9 y525.9 w364.9 h436.5)]
              Reward Holder [godot(x127.7 y608.9 w229.3 h234.6)]
                Icon Container Drawer Variant [godot(x127.7 y608.9 w229.3 h234.6)]
                  Content [godot(x127.7 y608.9 w229.3 h234.6)]
                    Image [godot(x116.3 y597.2 w252.2 h258.1)]
                    Converted Drawer [inactive godot(x192.7 y894.7 w99.3 h5.4)]
                      Price Display [godot(x212.7 y891.5 w365.6 h74.8)]
                        icon [godot(x314.5 y891.5 w74.9 h74.8)]
                        text [txt=2000 godot(x389.4 y891.5 w87.1 h74.8)]
                      AlreadyOwned [txt=Already Owned godot(x39.6 y943.3 w405.6 h86.4)]
                    Ephemeral Drawer [inactive godot(x192.7 y894.7 w99.3 h5.4)]
                      Price Display [godot(x212.7 y928.9 w365.6 h0.0)]
                        icon [godot(x175.3 y928.9 w74.9 h0.0)]
                        text [txt=24 hours godot(x432.9 y928.9 w0.0 h74.8)]
              EverguildTextMeshPro [txt=1 Booster pack godot(x128.2 y843.5 w228.3 h42.1)]
              Extra Reward Indicator [inactive godot(x284.4 y589.2 w80.0 h80.0)]
              Shadow [inactive godot(x124.5 y591.9 w235.7 h304.6)]
              Premium Indicator [godot(x119.5 y589.2 w101.3 h100.5)]
                Image [godot(x136.7 y602.5 w26.8 h37.0)]
              Gacha Reward Claimed [godot(x122.9 y610.7 w192.3 h53.3)]
                Claimed Tex [txt=Recogido godot(x128.3 y621.3 w173.0 h31.8)]
              colider [godot(x124.5 y591.9 w235.7 h304.6)]
            Premium Reward [godot(x111.4 y969.4 w261.9 h338.5)]
              BG [godot(x124.5 y986.4 w235.7 h304.6)]
              Highlight [sprite=OctagonUI Border SDF 2 godot(x59.9 y920.4 w364.9 h436.5)]
              Reward Holder [godot(x127.7 y1003.4 w229.3 h234.6)]
                Icon Container Drawer Variant [godot(x127.7 y1003.4 w229.3 h234.6)]
                  Content [godot(x127.7 y1003.4 w229.3 h234.6)]
                    Image [godot(x116.3 y991.7 w252.2 h258.0)]
                    Converted Drawer [inactive godot(x192.7 y1289.2 w99.3 h5.4)]
                      Price Display [godot(x212.7 y1285.9 w365.6 h74.9)]
                        icon [godot(x314.5 y1285.9 w74.9 h74.9)]
                        text [txt=2000 godot(x389.4 y1285.9 w87.1 h74.9)]
                      AlreadyOwned [txt=Already Owned godot(x39.6 y1337.8 w405.6 h86.4)]
                    Ephemeral Drawer [inactive godot(x192.7 y1289.2 w99.3 h5.4)]
                      Price Display [godot(x212.7 y1323.4 w365.6 h0.0)]
                        icon [godot(x175.3 y1323.4 w74.9 h0.0)]
                        text [txt=24 hours godot(x432.9 y1323.4 w0.0 h74.8)]
              EverguildTextMeshPro [txt=1 Booster pack godot(x128.2 y1238.0 w228.3 h42.1)]
              Extra Reward Indicator [inactive godot(x284.4 y983.7 w80.0 h80.0)]
              Shadow [inactive godot(x124.5 y986.4 w235.7 h304.6)]
              Premium Indicator [godot(x119.5 y983.7 w101.3 h100.5)]
                Image [godot(x136.7 y997.0 w26.8 h37.0)]
              Gacha Reward Claimed [godot(x122.9 y1005.2 w192.3 h53.3)]
                Claimed Tex [txt=Recogido godot(x128.3 y1015.7 w173.0 h31.9)]
              colider [godot(x124.5 y986.4 w235.7 h304.6)]
            Personal Progression [godot(x84.9 y894.2 w315.0 h100.0)]
              Progress Bar [godot(x20.4 y934.8 w222.0 h10.5)]
                Background [godot(x20.4 y934.8 w222.0 h10.5)]
                Fill [godot(x20.4 y945.3 w0.0 h0.0)]
                Handle Slide Area [inactive godot(x20.4 y934.8 w212.0 h10.5)]
                  Handle [godot(x14.6 y934.1 w11.7 h22.4)]
              Image [godot(x208.4 y896.9 w68.0 h88.0)]
                Counter [txt=1 godot(x199.9 y896.9 w85.0 h88.0)]
            Culling Reference Object [godot(x1.4 y538.1 w398.5 h812.1)]
            Day Title [txt=Day 3 godot(x112.4 y548.8 w259.9 h42.8)]
          Daily Reward Popup Entry (2) [godot(x84.9 y538.1 w315.0 h812.1)]
            NormalReward [godot(x111.4 y574.9 w261.9 h338.5)]
              BG [godot(x124.5 y591.9 w235.7 h304.6)]
              Highlight [sprite=OctagonUI Border SDF 2 godot(x59.9 y525.9 w364.9 h436.5)]
              Reward Holder [godot(x127.7 y608.9 w229.3 h234.6)]
                Icon Container Drawer Variant [godot(x127.7 y608.9 w229.3 h234.6)]
                  Content [godot(x127.7 y608.9 w229.3 h234.6)]
                    Image [godot(x116.3 y597.2 w252.2 h258.1)]
                    Converted Drawer [inactive godot(x192.7 y894.7 w99.3 h5.4)]
                      Price Display [godot(x212.7 y891.5 w365.6 h74.8)]
                        icon [godot(x314.5 y891.5 w74.9 h74.8)]
                        text [txt=2000 godot(x389.4 y891.5 w87.1 h74.8)]
                      AlreadyOwned [txt=Already Owned godot(x39.6 y943.3 w405.6 h86.4)]
                    Ephemeral Drawer [inactive godot(x192.7 y894.7 w99.3 h5.4)]
                      Price Display [godot(x212.7 y928.9 w365.6 h0.0)]
                        icon [godot(x175.3 y928.9 w74.9 h0.0)]
                        text [txt=24 hours godot(x432.9 y928.9 w0.0 h74.8)]
              EverguildTextMeshPro [txt=1 Booster pack godot(x128.2 y843.5 w228.3 h42.1)]
              Extra Reward Indicator [inactive godot(x284.4 y589.2 w80.0 h80.0)]
              Shadow [inactive godot(x124.5 y591.9 w235.7 h304.6)]
              Premium Indicator [godot(x119.5 y589.2 w101.3 h100.5)]
                Image [godot(x136.7 y602.5 w26.8 h37.0)]
              Gacha Reward Claimed [godot(x122.9 y610.7 w192.3 h53.3)]
                Claimed Tex [txt=Recogido godot(x128.3 y621.3 w173.0 h31.8)]
              colider [godot(x124.5 y591.9 w235.7 h304.6)]
            Premium Reward [godot(x111.4 y969.4 w261.9 h338.5)]
              BG [godot(x124.5 y986.4 w235.7 h304.6)]
              Highlight [sprite=OctagonUI Border SDF 2 godot(x59.9 y920.4 w364.9 h436.5)]
              Reward Holder [godot(x127.7 y1003.4 w229.3 h234.6)]
                Icon Container Drawer Variant [godot(x127.7 y1003.4 w229.3 h234.6)]
                  Content [godot(x127.7 y1003.4 w229.3 h234.6)]
                    Image [godot(x116.3 y991.7 w252.2 h258.0)]
                    Converted Drawer [inactive godot(x192.7 y1289.2 w99.3 h5.4)]
                      Price Display [godot(x212.7 y1285.9 w365.6 h74.9)]
                        icon [godot(x314.5 y1285.9 w74.9 h74.9)]
                        text [txt=2000 godot(x389.4 y1285.9 w87.1 h74.9)]
                      AlreadyOwned [txt=Already Owned godot(x39.6 y1337.8 w405.6 h86.4)]
                    Ephemeral Drawer [inactive godot(x192.7 y1289.2 w99.3 h5.4)]
                      Price Display [godot(x212.7 y1323.4 w365.6 h0.0)]
                        icon [godot(x175.3 y1323.4 w74.9 h0.0)]
                        text [txt=24 hours godot(x432.9 y1323.4 w0.0 h74.8)]
              EverguildTextMeshPro [txt=1 Booster pack godot(x128.2 y1238.0 w228.3 h42.1)]
              Extra Reward Indicator [inactive godot(x284.4 y983.7 w80.0 h80.0)]
              Shadow [inactive godot(x124.5 y986.4 w235.7 h304.6)]
              Premium Indicator [godot(x119.5 y983.7 w101.3 h100.5)]
                Image [godot(x136.7 y997.0 w26.8 h37.0)]
              Gacha Reward Claimed [godot(x122.9 y1005.2 w192.3 h53.3)]
                Claimed Tex [txt=Recogido godot(x128.3 y1015.7 w173.0 h31.9)]
              colider [godot(x124.5 y986.4 w235.7 h304.6)]
            Personal Progression [godot(x84.9 y894.2 w315.0 h100.0)]
              Progress Bar [godot(x20.4 y934.8 w222.0 h10.5)]
                Background [godot(x20.4 y934.8 w222.0 h10.5)]
                Fill [godot(x20.4 y945.3 w0.0 h0.0)]
                Handle Slide Area [inactive godot(x20.4 y934.8 w212.0 h10.5)]
                  Handle [godot(x14.6 y934.1 w11.7 h22.4)]
              Image [godot(x208.4 y896.9 w68.0 h88.0)]
                Counter [txt=1 godot(x199.9 y896.9 w85.0 h88.0)]
            Culling Reference Object [godot(x1.4 y538.1 w398.5 h812.1)]
            Day Title [txt=Day 3 godot(x112.4 y548.8 w259.9 h42.8)]
          Daily Reward Popup Entry (3) [godot(x84.9 y538.1 w315.0 h812.1)]
            NormalReward [godot(x111.4 y574.9 w261.9 h338.5)]
              BG [godot(x124.5 y591.9 w235.7 h304.6)]
              Highlight [sprite=OctagonUI Border SDF 2 godot(x59.9 y525.9 w364.9 h436.5)]
              Reward Holder [godot(x127.7 y608.9 w229.3 h234.6)]
                Icon Container Drawer Variant [godot(x127.7 y608.9 w229.3 h234.6)]
                  Content [godot(x127.7 y608.9 w229.3 h234.6)]
                    Image [godot(x116.3 y597.2 w252.2 h258.1)]
                    Converted Drawer [inactive godot(x192.7 y894.7 w99.3 h5.4)]
                      Price Display [godot(x212.7 y891.5 w365.6 h74.8)]
                        icon [godot(x314.5 y891.5 w74.9 h74.8)]
                        text [txt=2000 godot(x389.4 y891.5 w87.1 h74.8)]
                      AlreadyOwned [txt=Already Owned godot(x39.6 y943.3 w405.6 h86.4)]
                    Ephemeral Drawer [inactive godot(x192.7 y894.7 w99.3 h5.4)]
                      Price Display [godot(x212.7 y928.9 w365.6 h0.0)]
                        icon [godot(x175.3 y928.9 w74.9 h0.0)]
                        text [txt=24 hours godot(x432.9 y928.9 w0.0 h74.8)]
              EverguildTextMeshPro [txt=1 Booster pack godot(x128.2 y843.5 w228.3 h42.1)]
              Extra Reward Indicator [inactive godot(x284.4 y589.2 w80.0 h80.0)]
              Shadow [inactive godot(x124.5 y591.9 w235.7 h304.6)]
              Premium Indicator [godot(x119.5 y589.2 w101.3 h100.5)]
                Image [godot(x136.7 y602.5 w26.8 h37.0)]
              Gacha Reward Claimed [godot(x122.9 y610.7 w192.3 h53.3)]
                Claimed Tex [txt=Recogido godot(x128.3 y621.3 w173.0 h31.8)]
              colider [godot(x124.5 y591.9 w235.7 h304.6)]
            Premium Reward [godot(x111.4 y969.4 w261.9 h338.5)]
              BG [godot(x124.5 y986.4 w235.7 h304.6)]
              Highlight [sprite=OctagonUI Border SDF 2 godot(x59.9 y920.4 w364.9 h436.5)]
              Reward Holder [godot(x127.7 y1003.4 w229.3 h234.6)]
                Icon Container Drawer Variant [godot(x127.7 y1003.4 w229.3 h234.6)]
                  Content [godot(x127.7 y1003.4 w229.3 h234.6)]
                    Image [godot(x116.3 y991.7 w252.2 h258.0)]
                    Converted Drawer [inactive godot(x192.7 y1289.2 w99.3 h5.4)]
                      Price Display [godot(x212.7 y1285.9 w365.6 h74.9)]
                        icon [godot(x314.5 y1285.9 w74.9 h74.9)]
                        text [txt=2000 godot(x389.4 y1285.9 w87.1 h74.9)]
                      AlreadyOwned [txt=Already Owned godot(x39.6 y1337.8 w405.6 h86.4)]
                    Ephemeral Drawer [inactive godot(x192.7 y1289.2 w99.3 h5.4)]
                      Price Display [godot(x212.7 y1323.4 w365.6 h0.0)]
                        icon [godot(x175.3 y1323.4 w74.9 h0.0)]
                        text [txt=24 hours godot(x432.9 y1323.4 w0.0 h74.8)]
              EverguildTextMeshPro [txt=1 Booster pack godot(x128.2 y1238.0 w228.3 h42.1)]
              Extra Reward Indicator [inactive godot(x284.4 y983.7 w80.0 h80.0)]
              Shadow [inactive godot(x124.5 y986.4 w235.7 h304.6)]
              Premium Indicator [godot(x119.5 y983.7 w101.3 h100.5)]
                Image [godot(x136.7 y997.0 w26.8 h37.0)]
              Gacha Reward Claimed [godot(x122.9 y1005.2 w192.3 h53.3)]
                Claimed Tex [txt=Recogido godot(x128.3 y1015.7 w173.0 h31.9)]
              colider [godot(x124.5 y986.4 w235.7 h304.6)]
            Personal Progression [godot(x84.9 y894.2 w315.0 h100.0)]
              Progress Bar [godot(x20.4 y934.8 w222.0 h10.5)]
                Background [godot(x20.4 y934.8 w222.0 h10.5)]
                Fill [godot(x20.4 y945.3 w0.0 h0.0)]
                Handle Slide Area [inactive godot(x20.4 y934.8 w212.0 h10.5)]
                  Handle [godot(x14.6 y934.1 w11.7 h22.4)]
              Image [godot(x208.4 y896.9 w68.0 h88.0)]
                Counter [txt=1 godot(x199.9 y896.9 w85.0 h88.0)]
            Culling Reference Object [godot(x1.4 y538.1 w398.5 h812.1)]
            Day Title [txt=Day 3 godot(x112.4 y548.8 w259.9 h42.8)]
  Tracks Side Bar [godot(x-10.0 y152.8 w260.5 h812.1)]
    BG [godot(x-17.6 y143.0 w290.6 h824.7)]
      Free Track [godot(x0.0 y226.6 w236.2 h252.4)]
        Icon [godot(x-6.9 y254.2 w250.0 h117.3)]
        Title [txt=Ruta Gratuita godot(x18.1 y356.2 w200.0 h50.0)]
      Premium Track [godot(x0.0 y631.6 w236.2 h252.4)]
        Icon [sprite=40k_icon_DailyReward_Premium godot(x-6.9 y659.2 w250.0 h117.3)]
        Title [txt=Ruta Premium godot(x18.1 y761.2 w200.0 h50.0)]
        Price Display Button 2 Variant [godot(x31.1 y811.2 w174.0 h48.0)]
          Generic UI Button [godot(x31.1 y811.2 w174.0 h48.0)]
            Button Text [inactive godot(x44.1 y837.3 w148.0 h-4.3)]
            Price Display [godot(x40.0 y816.8 w155.2 h36.7)]
              icon [godot(x52.4 y853.5 w38.2 h0.0)]
              text [txt=300,00 godot(x71.5 y816.8 w92.2 h31.8)]
    Generic Round Button Variant [godot(x58.2 y902.9 w124.0 h124.0)]
      Button Text [inactive txt=X godot(x66.2 y902.9 w108.0 h124.0)]
      Image [inactive godot(x58.2 y903.9 w122.0 h122.0)]
  Army Selector [godot(x541.2 y-0.0 w1378.8 h152.8)]
    Separator Line [inactive godot(x541.2 y133.7 w1378.8 h6.0)]
    Viewport [godot(x541.2 y-0.0 w1378.8 h187.8)]
      Army Content [godot(x1230.6 y-0.0 w0.0 h130.0)]
  Header Header [godot(x0.0 y0.0 w604.8 h152.8)]
    Army Icon [godot(x0.0 y0.0 w132.4 h152.8)]
    Title [txt=Orks godot(x132.4 y21.6 w234.9 h52.5)]
    Sub-Title [txt=Recompensas al Iniciar Sesión godot(x132.4 y77.0 w410.7 h39.1)]
  Timer [godot(x598.3 y964.9 w723.4 h115.1)]
    EverguildTextMeshPro [txt=Más Recompensas En godot(x245.5 y990.8 w689.5 h63.3)]
    Image [godot(x938.6 y995.8 w53.2 h53.3)]
    EverguildTextMeshPro (1) [txt=19h 23m godot(x990.2 y990.8 w463.8 h63.3)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Daily Reward Popup | ✅ `scripts\daily_reward_popup.gd:2 ## 每日签到奖励弹层 (原版 Daily Reward Popup, 2026-08-23 从 rewards.gd 拆出; 入口=任务中心 Missions Tab 的 Daily Login` |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Tracks | ✅ `scripts\daily_reward_popup.gd:164 # 每日奖励区 (场景 Tracks x231-1948 y153-965)` |
| bg | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Separator Line Top | ⚠️ 未命中 |
| Separator Line Bottom | ⚠️ 未命中 |
| Rewards Scroll View | ✅ `scripts\daily_reward_popup.gd:3 ## 原版: Rewards Scroll View [242,159 1705x806]; 每个 Entry = Day 标题 + Normal 奖励卡 295x381 + 进度 + Premi` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:279 # 物品池 (原版 Re` |
| Rewards Content | ⚠️ 未命中 |
| Daily Reward Popup Entry | ✅ `scripts\daily_reward_popup.gd:246 ## 单日条目 (原版 Daily Reward Popup Entry: Day 标题 + Normal 卡 + 进度 + Premium 卡)` |
| NormalReward | ✅ `scripts\daily_reward_popup.gd:258 # Normal 奖励卡 (原版 NormalReward 295x381); scripts\daily_reward_popup.gd:332 ## 奖励卡 (原版 NormalRewar` |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Reward Holder | ✅ `scripts\daily_reward_popup.gd:364 # 奖励图标区 (原版 Reward Holder 287x293); scripts\daily_streak_popup.gd:212 ##   Entry (全树 14295): BG ` |
| Icon Container Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\daily_reward_popup.gd:175 # 左侧 Tab 栏 (原版 Rewards Base Submenu Variant 原始 JSON: Content Area [167.2,70.9 1752.8x1009.1],; s` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:198 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Extra Reward Indicator | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2760 # 悬浮` |
| Premium Indicator | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Gacha Reward Claimed | ✅ `scripts\gacha.gd:374 ## 特殊物品卡 (原版 Gacha Drawer Holder + Gacha Reward Claimed 徽章); scripts\gacha.gd:417 # Claimed 飘带 (原版 Gacha Rewa` |
| Claimed Tex | ⚠️ 未命中 |
| colider | ⚠️ 未命中 |
| Premium Reward | ✅ `scripts\campaign.gd:437 # 右栏 Premium Rewards [960,285 960x650] (单机版锁定); scripts\campaign.gd:438 _build_reward_panel(layer, "Premiu` |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Reward Holder | ✅ `scripts\daily_reward_popup.gd:364 # 奖励图标区 (原版 Reward Holder 287x293); scripts\daily_streak_popup.gd:212 ##   Entry (全树 14295): BG ` |
| Icon Container Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\daily_reward_popup.gd:175 # 左侧 Tab 栏 (原版 Rewards Base Submenu Variant 原始 JSON: Content Area [167.2,70.9 1752.8x1009.1],; s` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:198 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Extra Reward Indicator | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2760 # 悬浮` |
| Premium Indicator | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Gacha Reward Claimed | ✅ `scripts\gacha.gd:374 ## 特殊物品卡 (原版 Gacha Drawer Holder + Gacha Reward Claimed 徽章); scripts\gacha.gd:417 # Claimed 飘带 (原版 Gacha Rewa` |
| Claimed Tex | ⚠️ 未命中 |
| colider | ⚠️ 未命中 |
| Personal Progression | ✅ `scripts\daily_reward_popup.gd:263 # 个人进度条 (原版 Personal Progression 315x100: 里程碑 + 进度)` |
| Progress Bar | ✅ `scripts\quests.gd:354 # 进度 '52/500' 40px + bar (原版 Mission Milestones Progress Bar)` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Counter | ✅ `scripts\battle.gd:4455 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4493 # 攻击伤害数字 (原版 Damag` |
| Culling Reference Object | ⚠️ 未命中 |
| Day Title | ✅ `scripts\daily_reward_popup.gd:253 # Day 标题 (原版 Day Title "Day 3")` |
| Daily Reward Popup Entry (1) | ⚠️ 未命中 |
| NormalReward | ✅ `scripts\daily_reward_popup.gd:258 # Normal 奖励卡 (原版 NormalReward 295x381); scripts\daily_reward_popup.gd:332 ## 奖励卡 (原版 NormalRewar` |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Reward Holder | ✅ `scripts\daily_reward_popup.gd:364 # 奖励图标区 (原版 Reward Holder 287x293); scripts\daily_streak_popup.gd:212 ##   Entry (全树 14295): BG ` |
| Icon Container Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\daily_reward_popup.gd:175 # 左侧 Tab 栏 (原版 Rewards Base Submenu Variant 原始 JSON: Content Area [167.2,70.9 1752.8x1009.1],; s` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:198 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Extra Reward Indicator | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2760 # 悬浮` |
| Premium Indicator | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Gacha Reward Claimed | ✅ `scripts\gacha.gd:374 ## 特殊物品卡 (原版 Gacha Drawer Holder + Gacha Reward Claimed 徽章); scripts\gacha.gd:417 # Claimed 飘带 (原版 Gacha Rewa` |
| Claimed Tex | ⚠️ 未命中 |
| colider | ⚠️ 未命中 |
| Premium Reward | ✅ `scripts\campaign.gd:437 # 右栏 Premium Rewards [960,285 960x650] (单机版锁定); scripts\campaign.gd:438 _build_reward_panel(layer, "Premiu` |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Reward Holder | ✅ `scripts\daily_reward_popup.gd:364 # 奖励图标区 (原版 Reward Holder 287x293); scripts\daily_streak_popup.gd:212 ##   Entry (全树 14295): BG ` |
| Icon Container Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\daily_reward_popup.gd:175 # 左侧 Tab 栏 (原版 Rewards Base Submenu Variant 原始 JSON: Content Area [167.2,70.9 1752.8x1009.1],; s` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:198 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Extra Reward Indicator | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2760 # 悬浮` |
| Premium Indicator | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Gacha Reward Claimed | ✅ `scripts\gacha.gd:374 ## 特殊物品卡 (原版 Gacha Drawer Holder + Gacha Reward Claimed 徽章); scripts\gacha.gd:417 # Claimed 飘带 (原版 Gacha Rewa` |
| Claimed Tex | ⚠️ 未命中 |
| colider | ⚠️ 未命中 |
| Personal Progression | ✅ `scripts\daily_reward_popup.gd:263 # 个人进度条 (原版 Personal Progression 315x100: 里程碑 + 进度)` |
| Progress Bar | ✅ `scripts\quests.gd:354 # 进度 '52/500' 40px + bar (原版 Mission Milestones Progress Bar)` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Counter | ✅ `scripts\battle.gd:4455 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4493 # 攻击伤害数字 (原版 Damag` |
| Culling Reference Object | ⚠️ 未命中 |
| Day Title | ✅ `scripts\daily_reward_popup.gd:253 # Day 标题 (原版 Day Title "Day 3")` |
| Daily Reward Popup Entry (2) | ⚠️ 未命中 |
| NormalReward | ✅ `scripts\daily_reward_popup.gd:258 # Normal 奖励卡 (原版 NormalReward 295x381); scripts\daily_reward_popup.gd:332 ## 奖励卡 (原版 NormalRewar` |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Reward Holder | ✅ `scripts\daily_reward_popup.gd:364 # 奖励图标区 (原版 Reward Holder 287x293); scripts\daily_streak_popup.gd:212 ##   Entry (全树 14295): BG ` |
| Icon Container Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\daily_reward_popup.gd:175 # 左侧 Tab 栏 (原版 Rewards Base Submenu Variant 原始 JSON: Content Area [167.2,70.9 1752.8x1009.1],; s` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:198 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Extra Reward Indicator | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2760 # 悬浮` |
| Premium Indicator | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Gacha Reward Claimed | ✅ `scripts\gacha.gd:374 ## 特殊物品卡 (原版 Gacha Drawer Holder + Gacha Reward Claimed 徽章); scripts\gacha.gd:417 # Claimed 飘带 (原版 Gacha Rewa` |
| Claimed Tex | ⚠️ 未命中 |
| colider | ⚠️ 未命中 |
| Premium Reward | ✅ `scripts\campaign.gd:437 # 右栏 Premium Rewards [960,285 960x650] (单机版锁定); scripts\campaign.gd:438 _build_reward_panel(layer, "Premiu` |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Reward Holder | ✅ `scripts\daily_reward_popup.gd:364 # 奖励图标区 (原版 Reward Holder 287x293); scripts\daily_streak_popup.gd:212 ##   Entry (全树 14295): BG ` |
| Icon Container Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\daily_reward_popup.gd:175 # 左侧 Tab 栏 (原版 Rewards Base Submenu Variant 原始 JSON: Content Area [167.2,70.9 1752.8x1009.1],; s` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:198 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Extra Reward Indicator | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2760 # 悬浮` |
| Premium Indicator | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Gacha Reward Claimed | ✅ `scripts\gacha.gd:374 ## 特殊物品卡 (原版 Gacha Drawer Holder + Gacha Reward Claimed 徽章); scripts\gacha.gd:417 # Claimed 飘带 (原版 Gacha Rewa` |
| Claimed Tex | ⚠️ 未命中 |
| colider | ⚠️ 未命中 |
| Personal Progression | ✅ `scripts\daily_reward_popup.gd:263 # 个人进度条 (原版 Personal Progression 315x100: 里程碑 + 进度)` |
| Progress Bar | ✅ `scripts\quests.gd:354 # 进度 '52/500' 40px + bar (原版 Mission Milestones Progress Bar)` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Counter | ✅ `scripts\battle.gd:4455 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4493 # 攻击伤害数字 (原版 Damag` |
| Culling Reference Object | ⚠️ 未命中 |
| Day Title | ✅ `scripts\daily_reward_popup.gd:253 # Day 标题 (原版 Day Title "Day 3")` |
| Daily Reward Popup Entry (3) | ⚠️ 未命中 |
| NormalReward | ✅ `scripts\daily_reward_popup.gd:258 # Normal 奖励卡 (原版 NormalReward 295x381); scripts\daily_reward_popup.gd:332 ## 奖励卡 (原版 NormalRewar` |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Reward Holder | ✅ `scripts\daily_reward_popup.gd:364 # 奖励图标区 (原版 Reward Holder 287x293); scripts\daily_streak_popup.gd:212 ##   Entry (全树 14295): BG ` |
| Icon Container Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\daily_reward_popup.gd:175 # 左侧 Tab 栏 (原版 Rewards Base Submenu Variant 原始 JSON: Content Area [167.2,70.9 1752.8x1009.1],; s` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:198 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Extra Reward Indicator | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2760 # 悬浮` |
| Premium Indicator | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Gacha Reward Claimed | ✅ `scripts\gacha.gd:374 ## 特殊物品卡 (原版 Gacha Drawer Holder + Gacha Reward Claimed 徽章); scripts\gacha.gd:417 # Claimed 飘带 (原版 Gacha Rewa` |
| Claimed Tex | ⚠️ 未命中 |
| colider | ⚠️ 未命中 |
| Premium Reward | ✅ `scripts\campaign.gd:437 # 右栏 Premium Rewards [960,285 960x650] (单机版锁定); scripts\campaign.gd:438 _build_reward_panel(layer, "Premiu` |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Reward Holder | ✅ `scripts\daily_reward_popup.gd:364 # 奖励图标区 (原版 Reward Holder 287x293); scripts\daily_streak_popup.gd:212 ##   Entry (全树 14295): BG ` |
| Icon Container Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\daily_reward_popup.gd:175 # 左侧 Tab 栏 (原版 Rewards Base Submenu Variant 原始 JSON: Content Area [167.2,70.9 1752.8x1009.1],; s` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Converted Drawer | ✅ `scripts\where_cards_popup.gd:198 # Card Drawer 卡行 (原版 Card Drawer 191.6 宽: 2DCard 卡面 + Converted Drawer Price '2000'); scripts\whe` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Extra Reward Indicator | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2760 # 悬浮` |
| Premium Indicator | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Gacha Reward Claimed | ✅ `scripts\gacha.gd:374 ## 特殊物品卡 (原版 Gacha Drawer Holder + Gacha Reward Claimed 徽章); scripts\gacha.gd:417 # Claimed 飘带 (原版 Gacha Rewa` |
| Claimed Tex | ⚠️ 未命中 |
| colider | ⚠️ 未命中 |
| Personal Progression | ✅ `scripts\daily_reward_popup.gd:263 # 个人进度条 (原版 Personal Progression 315x100: 里程碑 + 进度)` |
| Progress Bar | ✅ `scripts\quests.gd:354 # 进度 '52/500' 40px + bar (原版 Mission Milestones Progress Bar)` |
| Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:114 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_DIR + "OctagonUI Filled SDF.png"        # 升级特效; scripts\daily_streak_popup.gd` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Counter | ✅ `scripts\battle.gd:4455 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4493 # 攻击伤害数字 (原版 Damag` |
| Culling Reference Object | ⚠️ 未命中 |
| Day Title | ✅ `scripts\daily_reward_popup.gd:253 # Day 标题 (原版 Day Title "Day 3")` |
| Tracks Side Bar | ⚠️ 未命中 |
| BG | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Free Track | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1848 #` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Premium Track | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:230 # 奖励行 (原版 rewards '2 points' 白 @(402.7,102) + rewardIcon seal @(374.1,97.2)); scripts\battle.gd:1848 #` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Price Display Button 2 Variant | ⚠️ 未命中 |
| Generic UI Button | ✅ `scripts\quests.gd:498 ## Collect 按钮 (原版 Generic UI Button: 40K_button 底 + tint 色; 未达成禁用)` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\booster_info_popup.gd:146 # 购买区 (原版 Price Display [831.3,746.5 232x71] '300,00' + WebShop Button [826.7,756 241x52] 'Save ` |
| icon | ✅ `scripts\achievements.gd:13 const TEX_SEAL := SPR + "40k_Achievements_icon_seal points.png" # 奖励点数印章 28.5x39.1; scripts\achievement` |
| text | ✅ `scripts\achievements.gd:157 bg.texture = load(TEX_CONTAINER); scripts\achievements.gd:178 icon.texture = load(icon_path)` |
| Generic Round Button Variant | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| Army Selector | ✅ `scripts\battle.gd:171 # 原版 battlearena1 场景树无阵营选择弹窗 (Army Selector 在模式选择界面) —; scripts\campaign.gd:126 # Campaign Army Selector (原版` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:279 # 物品池 (原版 Re` |
| Army Content | ⚠️ 未命中 |
| Header Header | ⚠️ 未命中 |
| Army Icon | ✅ `scripts\campaign.gd:195 # 阵营图标 (原版 Army Icon 135×165 @ (345.7,60.9)); scripts\card_displayer.gd:493 # 阵营图标 (场景 Army Icon 80x85)` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Sub-Title | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4570 var _clock_timer: Timer = null; scripts\battle.gd:4589 _clock_timer = Timer.new()` |
| EverguildTextMeshPro | ⚠️ 未命中 |
| Image | ✅ `scripts\achievements.gd:141 ## 成就容器 (原版 Achievement Container 520x150: Image 130x130@(15,10) + 标题/描述 + 进度条四件套 + 奖励行); scripts\achi` |
| EverguildTextMeshPro (1) | ⚠️ 未命中 |

## 摘要

- 规格元素: 275
- 代码命中: 187
- ⚠️未命中: 88 (以下需人工判断)

- `Separator Line Top`
- `Separator Line Bottom`
- `Rewards Content`
- `Icon Container Drawer Variant`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `EverguildTextMeshPro`
- `Extra Reward Indicator`
- `Premium Indicator`
- `Claimed Tex`
- `colider`
- `Icon Container Drawer Variant`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `EverguildTextMeshPro`
- `Extra Reward Indicator`
- `Premium Indicator`
- `Claimed Tex`
- `colider`
- `Handle Slide Area`
- `Culling Reference Object`
- `Daily Reward Popup Entry (1)`
- `Icon Container Drawer Variant`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `EverguildTextMeshPro`
- `Extra Reward Indicator`
- `Premium Indicator`
- `Claimed Tex`
- `colider`
- `Icon Container Drawer Variant`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `EverguildTextMeshPro`
- `Extra Reward Indicator`
- `Premium Indicator`
- `Claimed Tex`
- `colider`
- `Handle Slide Area`
- `Culling Reference Object`
- `Daily Reward Popup Entry (2)`
- `Icon Container Drawer Variant`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `EverguildTextMeshPro`
- `Extra Reward Indicator`
- `Premium Indicator`
- `Claimed Tex`
- `colider`
- `Icon Container Drawer Variant`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `EverguildTextMeshPro`
- `Extra Reward Indicator`
- `Premium Indicator`
- `Claimed Tex`
- `colider`
- `Handle Slide Area`
- `Culling Reference Object`
- `Daily Reward Popup Entry (3)`
- `Icon Container Drawer Variant`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `EverguildTextMeshPro`
- `Extra Reward Indicator`
- `Premium Indicator`
- `Claimed Tex`
- `colider`
- `Icon Container Drawer Variant`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `EverguildTextMeshPro`
- `Extra Reward Indicator`
- `Premium Indicator`
- `Claimed Tex`
- `colider`
- `Handle Slide Area`
- `Culling Reference Object`
- `Tracks Side Bar`
- `Free Track`
- `Premium Track`
- `Price Display Button 2 Variant`
- `Generic Round Button Variant`
- `Army Content`
- `Header Header`
- `Sub-Title`
- `EverguildTextMeshPro`
- `EverguildTextMeshPro (1)`