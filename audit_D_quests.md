# UI 规格审计: Missions Tab

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Missions Tab [godot(x166.7 y69.2 w1753.3 h1010.8)]
  Normal Missions [godot(x372.4 y95.8 w1519.0 h723.8)]
    Special Missions [godot(x372.4 y12.4 w896.1 h639.7)]
      Daily Login Container [inactive godot(x372.4 y652.1 w0.0 h0.0)]
        raycast target [inactive godot(x372.4 y652.1 w0.0 h0.0)]
        background [godot(x372.4 y652.1 w0.0 h0.0)]
          header [godot(x375.5 y654.6 w-3.1 h60.7)]
            name [txt=Daily Login Bonus godot(x375.4 y656.2 w-2.5 h57.5)]
            info [godot(x313.7 y661.4 w47.2 h47.2)]
          body [godot(x185.5 y404.4 w373.7 h300.3)]
            description [inactive godot(x185.5 y404.4 w373.7 h300.3)]
            image [godot(x185.5 y437.8 w373.7 h300.3)]
          progress [inactive godot(x185.5 y637.9 w373.7 h84.7)]
            Mission Milestones Progress Bar [godot(x198.4 y637.9 w347.9 h70.8)]
              Progress Bar [godot(x201.9 y685.3 w344.4 h23.4)]
                Background [godot(x201.9 y685.3 w344.4 h23.4)]
                Fill [godot(x201.9 y685.3 w344.4 h23.4)]
                Handle Slide Area [inactive godot(x201.9 y685.3 w344.4 h23.4)]
                  Handle [godot(x195.2 y679.6 w13.4 h34.8)]
              progress [txt=52/500 godot(x198.4 y637.9 w347.9 h47.4)]
          footer [godot(x183.7 y724.4 w373.8 h209.2)]
            Rewards [godot(x183.7 y724.4 w373.8 h89.3)]
              Reward Display Mission [godot(x183.7 y813.7 w0.0 h0.0)]
                drawerHolder [godot(x183.7 y813.7 w0.0 h0.0)]
                  Currency [godot(x186.5 y824.5 w0.0 h-21.6)]
                    Content [godot(x186.5 y824.5 w0.0 h-21.6)]
                      Image [godot(x191.7 y829.8 w-10.5 h-32.1)]
                count [txt=100 godot(x183.7 y813.7 w0.0 h0.0)]
              Reward Display Mission [godot(x183.7 y813.7 w0.0 h0.0)]
                drawerHolder [godot(x183.7 y813.7 w0.0 h0.0)]
                  Campaign Points  [godot(x183.7 y813.7 w0.0 h0.0)]
                    Content [godot(x183.7 y813.7 w0.0 h0.0)]
                      Campaign Glow [godot(x183.7 y813.7 w0.0 h0.0)]
                      Image [inactive godot(x183.7 y813.7 w0.0 h0.0)]
                count [txt=? godot(x183.7 y813.7 w0.0 h0.0)]
            Generic UI Button [godot(x227.1 y813.7 w294.4 h85.8)]
              Button Text [txt=Collect godot(x235.1 y813.7 w278.3 h85.8)]
            TimerHolder [godot(x183.7 y899.5 w373.8 h65.8)]
              Timer [txt=Resets in 12h 34 m godot(x183.7 y899.5 w373.8 h65.8)]
          debug_buttons [godot(x407.9 y404.4 w151.3 h156.7)]
            Reset [godot(x407.9 y536.5 w0.0 h49.1)]
              Button Text [txt=Reset godot(x422.8 y536.5 w-29.9 h49.1)]
            Re-Roll [godot(x407.9 y536.5 w0.0 h49.1)]
              Button Text [txt=Re-Roll godot(x422.8 y536.5 w-29.9 h49.1)]
            GameObject [godot(x407.9 y538.0 w0.0 h46.1)]
              Increase one [godot(x407.9 y584.1 w0.0 h0.0)]
                Button Text [txt=+1 godot(x422.8 y584.1 w-29.9 h0.0)]
              Increase half [godot(x407.9 y584.1 w0.0 h0.0)]
                Button Text [txt=+5 godot(x422.8 y584.1 w-29.9 h0.0)]
            Complete [godot(x407.9 y536.5 w0.0 h49.1)]
              Button Text [txt=Complete godot(x422.8 y536.5 w-29.9 h49.1)]
            GameObject (1) [inactive godot(x407.9 y566.1 w151.3 h46.1)]
              Text (TMP) [txt=00:00 godot(x407.9 y566.1 w151.3 h46.1)]
      Daily Skulls Mission Container [godot(x372.4 y652.1 w0.0 h0.0)]
        raycast target [inactive godot(x372.4 y652.1 w0.0 h0.0)]
        background [godot(x372.4 y652.1 w0.0 h0.0)]
          header [godot(x375.5 y654.6 w-3.1 h60.7)]
            name [txt=Daily Skulls godot(x375.4 y656.2 w-2.5 h57.5)]
            info [godot(x313.7 y661.4 w47.2 h47.2)]
          body [godot(x185.5 y404.4 w373.7 h263.3)]
            description [inactive godot(x185.5 y404.4 w373.7 h263.3)]
            Image [godot(x185.5 y397.2 w76.1 h74.4)]
            counter [txt=x160000 godot(x243.3 y428.9 w78.1 h36.6)]
            image [godot(x261.6 y422.0 w254.9 h263.3)]
          progress [godot(x185.5 y637.9 w373.7 h84.7)]
            milestones [godot(x185.5 y637.9 w373.7 h84.7)]
              steps [godot(x185.5 y637.9 w373.7 h84.7)]
                Mission Milestones Step [godot(x162.5 y699.6 w46.0 h46.0)]
                  holder [godot(x162.5 y699.6 w46.0 h46.0)]
                    Image [godot(x162.5 y699.6 w46.0 h46.0)]
                    CheckMark [godot(x186.6 y666.8 w46.0 h48.7)]
                    text [txt=1 godot(x162.5 y699.6 w46.0 h46.0)]
                Mission Milestones Step (1) [godot(x162.5 y699.6 w46.0 h46.0)]
                  holder [godot(x162.5 y699.6 w46.0 h46.0)]
                    Image [godot(x162.5 y699.6 w46.0 h46.0)]
                    CheckMark [godot(x186.6 y666.8 w46.0 h48.7)]
                    text [txt=1 godot(x162.5 y699.6 w46.0 h46.0)]
                Mission Milestones Step (2) [godot(x162.5 y699.6 w46.0 h46.0)]
                  holder [godot(x162.5 y699.6 w46.0 h46.0)]
                    Image [godot(x162.5 y699.6 w46.0 h46.0)]
                    CheckMark [godot(x186.6 y666.8 w46.0 h48.7)]
                    text [txt=1 godot(x162.5 y699.6 w46.0 h46.0)]
                Mission Milestones Step (3) [godot(x162.5 y699.6 w46.0 h46.0)]
                  holder [godot(x162.5 y699.6 w46.0 h46.0)]
                    Image [godot(x162.5 y699.6 w46.0 h46.0)]
                    CheckMark [godot(x186.6 y666.8 w46.0 h48.7)]
                    text [txt=1 godot(x162.5 y699.6 w46.0 h46.0)]
                Mission Milestones Step (4) [godot(x162.5 y699.6 w46.0 h46.0)]
                  holder [godot(x162.5 y699.6 w46.0 h46.0)]
                    Image [godot(x162.5 y699.6 w46.0 h46.0)]
                    CheckMark [godot(x186.6 y666.8 w46.0 h48.7)]
                    text [txt=1 godot(x162.5 y699.6 w46.0 h46.0)]
          footer [godot(x183.7 y724.4 w373.8 h209.2)]
            Rewards [godot(x183.7 y724.4 w373.8 h89.3)]
              Reward Display Mission [godot(x183.7 y813.7 w0.0 h0.0)]
                drawerHolder [godot(x183.7 y813.7 w0.0 h0.0)]
                  Icon Campaign Points Drawer Variant [godot(x183.7 y813.7 w0.0 h0.0)]
                    Content [godot(x183.7 y813.7 w0.0 h0.0)]
                      Campaign Glow [godot(x183.7 y813.7 w0.0 h0.0)]
                      Image [godot(x183.7 y813.7 w0.0 h0.0)]
                      Converted Drawer [inactive godot(x183.7 y813.7 w0.0 h0.0)]
                        Price Display [godot(x183.7 y813.7 w0.0 h0.0)]
                          icon [godot(x183.7 y813.7 w0.0 h0.0)]
                          text [txt=2000 godot(x183.7 y813.7 w0.0 h0.0)]
                        AlreadyOwned [txt=Already Owned godot(x183.7 y813.7 w0.0 h0.0)]
                      Ephemeral Drawer [inactive godot(x183.7 y813.7 w0.0 h0.0)]
                        Price Display [godot(x183.7 y813.7 w0.0 h0.0)]
                          icon [godot(x183.7 y813.7 w0.0 h0.0)]
                          text [txt=24 hours godot(x183.7 y813.7 w0.0 h0.0)]
                count [txt=200 godot(x183.7 y813.7 w0.0 h0.0)]
              Reward Display Mission [godot(x183.7 y813.7 w0.0 h0.0)]
                drawerHolder [godot(x183.7 y813.7 w0.0 h0.0)]
                  Icon Campaign Points Drawer Variant [godot(x183.7 y813.7 w0.0 h0.0)]
                    Content [godot(x183.7 y813.7 w0.0 h0.0)]
                      Campaign Glow [godot(x183.7 y813.7 w0.0 h0.0)]
                      Image [godot(x183.7 y813.7 w0.0 h0.0)]
                      Converted Drawer [inactive godot(x183.7 y813.7 w0.0 h0.0)]
                        Price Display [godot(x183.7 y813.7 w0.0 h0.0)]
                          icon [godot(x183.7 y813.7 w0.0 h0.0)]
                          text [txt=2000 godot(x183.7 y813.7 w0.0 h0.0)]
                        AlreadyOwned [txt=Already Owned godot(x183.7 y813.7 w0.0 h0.0)]
                      Ephemeral Drawer [inactive godot(x183.7 y813.7 w0.0 h0.0)]
                        Price Display [godot(x183.7 y813.7 w0.0 h0.0)]
                          icon [godot(x183.7 y813.7 w0.0 h0.0)]
                          text [txt=24 hours godot(x183.7 y813.7 w0.0 h0.0)]
                count [txt=100 godot(x183.7 y813.7 w0.0 h0.0)]
            Generic UI Button [godot(x227.1 y813.7 w294.4 h85.8)]
              Button Text [txt=Collect godot(x242.0 y813.7 w264.5 h85.8)]
            TimerHolder [godot(x183.7 y899.5 w373.8 h65.8)]
              Timer [txt=Resets in 12h 34 m godot(x183.7 y899.5 w373.8 h65.8)]
          debug_buttons [godot(x407.9 y404.4 w151.3 h156.7)]
            Reset [godot(x407.9 y536.5 w0.0 h49.1)]
              Button Text [txt=Reset godot(x422.8 y536.5 w-29.9 h49.1)]
            Re-Roll [godot(x407.9 y536.5 w0.0 h49.1)]
              Button Text [txt=Re-Roll godot(x422.8 y536.5 w-29.9 h49.1)]
            GameObject [godot(x407.9 y538.0 w0.0 h46.1)]
              Increase one [godot(x407.9 y584.1 w0.0 h0.0)]
                Button Text [txt=+1 godot(x422.8 y584.1 w-29.9 h0.0)]
              Increase half [godot(x407.9 y584.1 w0.0 h0.0)]
                Button Text [txt=+5 godot(x422.8 y584.1 w-29.9 h0.0)]
            Complete [godot(x407.9 y536.5 w0.0 h49.1)]
              Button Text [txt=Complete godot(x422.8 y536.5 w-29.9 h49.1)]
            GameObject (1) [godot(x407.9 y538.0 w0.0 h46.1)]
              Text (TMP) [txt=00:00 godot(x407.9 y584.1 w0.0 h0.0)]
    Daily Missions [godot(x1271.3 y12.5 w620.1 h639.2)]
      Daily Missions Holder [godot(x1271.3 y75.1 w620.1 h576.6)]
        Daily Mission Container [godot(x1271.3 y565.5 w0.0 h172.5)]
          title [inactive txt=Deal 500 damage to enemy units godot(x1428.5 y580.1 w-156.8 h71.6)]
          description [txt=Deal 500 damage to enemy units godot(x1428.5 y580.1 w-156.8 h71.6)]
          timer [txt=Available in 64h godot(x1428.5 y580.1 w-307.2 h71.6)]
          Separator Line [godot(x1409.8 y567.3 w1.9 h169.0)]
          Rewards [godot(x1271.3 y565.5 w145.3 h172.5)]
            Reward Display Mission Vertical Variant [godot(x1271.3 y565.5 w145.3 h172.5)]
              drawerHolder [godot(x1291.8 y565.5 w104.3 h123.7)]
                Icon Campaign Points Drawer Variant [godot(x1291.8 y689.2 w0.0 h0.0)]
                  Content [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Campaign Glow [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Image [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x1291.8 y689.2 w0.0 h0.0)]
                      Price Display [godot(x1291.8 y689.2 w0.0 h0.0)]
                        icon [godot(x1291.8 y689.2 w0.0 h0.0)]
                        text [txt=2000 godot(x1291.8 y689.2 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x1291.8 y689.2 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x1291.8 y689.2 w0.0 h0.0)]
                      Price Display [godot(x1291.8 y689.2 w0.0 h0.0)]
                        icon [godot(x1291.8 y689.2 w0.0 h0.0)]
                        text [txt=24 hours godot(x1291.8 y689.2 w0.0 h0.0)]
              count [txt=100 godot(x1271.3 y679.1 w145.3 h58.9)]
          Mission Milestones Progress Bar [godot(x1428.5 y655.3 w-88.9 h59.6)]
            Progress Bar [godot(x1434.8 y701.6 w-95.2 h13.3)]
              Background [godot(x1434.8 y701.6 w-95.2 h13.3)]
              Fill [godot(x1434.8 y714.9 w0.0 h0.0)]
              Handle Slide Area [inactive godot(x1434.8 y701.6 w-106.7 h13.3)]
                Handle [godot(x1428.1 y702.0 w13.4 h25.8)]
            progress [txt=52/500 godot(x1428.5 y651.8 w-88.9 h46.9)]
          Generic UI Button [godot(x957.8 y658.7 w292.8 h64.9)]
            Button Text [txt=Collect godot(x965.9 y658.7 w276.7 h64.9)]
          Trash mission [godot(x889.5 y662.8 w56.5 h56.7)]
            Button Text [inactive txt=X godot(x898.7 y662.8 w38.1 h56.7)]
            Image [godot(x889.5 y663.9 w54.2 h54.5)]
          Mission Debug Buttons [godot(x983.3 y548.6 w906.1 h38.8)]
            Reset [godot(x923.9 y587.4 w118.7 h0.0)]
              Button Text [txt=Reset godot(x938.8 y587.4 w88.9 h0.0)]
            Re-Roll [godot(x923.9 y587.4 w118.7 h0.0)]
              Button Text [txt=Re-Roll godot(x938.8 y587.4 w88.9 h0.0)]
            GameObject [godot(x923.9 y587.4 w118.7 h0.0)]
              Increase one [godot(x923.9 y587.4 w0.0 h0.0)]
                Button Text [txt=+1 godot(x938.8 y587.4 w-29.9 h0.0)]
              Increase half [godot(x923.9 y587.4 w0.0 h0.0)]
                Button Text [txt=+5 godot(x938.8 y587.4 w-29.9 h0.0)]
            Complete [godot(x897.6 y587.4 w171.3 h0.0)]
              Button Text [txt=Complete godot(x912.6 y587.4 w141.4 h0.0)]
            GameObject (1) [godot(x913.7 y587.4 w139.2 h0.0)]
              Text (TMP) [txt=00:00 godot(x913.7 y587.4 w0.0 h0.0)]
        Daily Mission Container (1) [godot(x1271.3 y565.5 w0.0 h172.5)]
          title [inactive txt=Deal 500 damage to enemy units godot(x1428.5 y580.1 w-156.8 h71.6)]
          description [txt=Deal 500 damage to enemy units godot(x1428.5 y580.1 w-156.8 h71.6)]
          timer [txt=Available in 64h godot(x1428.5 y580.1 w-307.2 h71.6)]
          Separator Line [godot(x1409.8 y567.3 w1.9 h169.0)]
          Rewards [godot(x1271.3 y565.5 w145.3 h172.5)]
            Reward Display Mission Vertical Variant [godot(x1271.3 y565.5 w145.3 h172.5)]
              drawerHolder [godot(x1291.8 y565.5 w104.3 h123.7)]
                Icon Campaign Points Drawer Variant [godot(x1291.8 y689.2 w0.0 h0.0)]
                  Content [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Campaign Glow [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Image [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x1291.8 y689.2 w0.0 h0.0)]
                      Price Display [godot(x1291.8 y689.2 w0.0 h0.0)]
                        icon [godot(x1291.8 y689.2 w0.0 h0.0)]
                        text [txt=2000 godot(x1291.8 y689.2 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x1291.8 y689.2 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x1291.8 y689.2 w0.0 h0.0)]
                      Price Display [godot(x1291.8 y689.2 w0.0 h0.0)]
                        icon [godot(x1291.8 y689.2 w0.0 h0.0)]
                        text [txt=24 hours godot(x1291.8 y689.2 w0.0 h0.0)]
              count [txt=100 godot(x1271.3 y679.1 w145.3 h58.9)]
          Mission Milestones Progress Bar [godot(x1428.5 y655.3 w-88.9 h59.6)]
            Progress Bar [godot(x1434.8 y701.6 w-95.2 h13.3)]
              Background [godot(x1434.8 y701.6 w-95.2 h13.3)]
              Fill [godot(x1434.8 y714.9 w0.0 h0.0)]
              Handle Slide Area [inactive godot(x1434.8 y701.6 w-106.7 h13.3)]
                Handle [godot(x1428.1 y702.0 w13.4 h25.8)]
            progress [txt=52/500 godot(x1428.5 y651.8 w-88.9 h46.9)]
          Generic UI Button [godot(x957.8 y658.7 w292.8 h64.9)]
            Button Text [txt=Collect godot(x965.9 y658.7 w276.7 h64.9)]
          Trash mission [godot(x889.5 y662.8 w56.5 h56.7)]
            Button Text [inactive txt=X godot(x898.7 y662.8 w38.1 h56.7)]
            Image [godot(x889.5 y663.9 w54.2 h54.5)]
          Mission Debug Buttons [godot(x983.3 y548.6 w906.1 h38.8)]
            Reset [godot(x923.9 y587.4 w118.7 h0.0)]
              Button Text [txt=Reset godot(x938.8 y587.4 w88.9 h0.0)]
            Re-Roll [godot(x923.9 y587.4 w118.7 h0.0)]
              Button Text [txt=Re-Roll godot(x938.8 y587.4 w88.9 h0.0)]
            GameObject [godot(x923.9 y587.4 w118.7 h0.0)]
              Increase one [godot(x923.9 y587.4 w0.0 h0.0)]
                Button Text [txt=+1 godot(x938.8 y587.4 w-29.9 h0.0)]
              Increase half [godot(x923.9 y587.4 w0.0 h0.0)]
                Button Text [txt=+5 godot(x938.8 y587.4 w-29.9 h0.0)]
            Complete [godot(x897.6 y587.4 w171.3 h0.0)]
              Button Text [txt=Complete godot(x912.6 y587.4 w141.4 h0.0)]
            GameObject (1) [godot(x913.7 y587.4 w139.2 h0.0)]
              Text (TMP) [txt=00:00 godot(x913.7 y587.4 w0.0 h0.0)]
        Daily Mission Container (2) [godot(x1271.3 y565.5 w0.0 h172.5)]
          title [inactive txt=Deal 500 damage to enemy units godot(x1428.5 y580.1 w-156.8 h71.6)]
          description [txt=Deal 500 damage to enemy units godot(x1428.5 y580.1 w-156.8 h71.6)]
          timer [txt=Available in 64h godot(x1428.5 y580.1 w-307.2 h71.6)]
          Separator Line [godot(x1409.8 y567.3 w1.9 h169.0)]
          Rewards [godot(x1271.3 y565.5 w145.3 h172.5)]
            Reward Display Mission Vertical Variant [godot(x1271.3 y565.5 w145.3 h172.5)]
              drawerHolder [godot(x1291.8 y565.5 w104.3 h123.7)]
                Icon Campaign Points Drawer Variant [godot(x1291.8 y689.2 w0.0 h0.0)]
                  Content [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Campaign Glow [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Image [godot(x1291.8 y689.2 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x1291.8 y689.2 w0.0 h0.0)]
                      Price Display [godot(x1291.8 y689.2 w0.0 h0.0)]
                        icon [godot(x1291.8 y689.2 w0.0 h0.0)]
                        text [txt=2000 godot(x1291.8 y689.2 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x1291.8 y689.2 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x1291.8 y689.2 w0.0 h0.0)]
                      Price Display [godot(x1291.8 y689.2 w0.0 h0.0)]
                        icon [godot(x1291.8 y689.2 w0.0 h0.0)]
                        text [txt=24 hours godot(x1291.8 y689.2 w0.0 h0.0)]
              count [txt=100 godot(x1271.3 y679.1 w145.3 h58.9)]
          Mission Milestones Progress Bar [godot(x1428.5 y655.3 w-88.9 h59.6)]
            Progress Bar [godot(x1434.8 y701.6 w-95.2 h13.3)]
              Background [godot(x1434.8 y701.6 w-95.2 h13.3)]
              Fill [godot(x1434.8 y714.9 w0.0 h0.0)]
              Handle Slide Area [inactive godot(x1434.8 y701.6 w-106.7 h13.3)]
                Handle [godot(x1428.1 y702.0 w13.4 h25.8)]
            progress [txt=52/500 godot(x1428.5 y651.8 w-88.9 h46.9)]
          Generic UI Button [godot(x957.8 y658.7 w292.8 h64.9)]
            Button Text [txt=Collect godot(x965.9 y658.7 w276.7 h64.9)]
          Trash mission [godot(x889.5 y662.8 w56.5 h56.7)]
            Button Text [inactive txt=X godot(x898.7 y662.8 w38.1 h56.7)]
            Image [godot(x889.5 y663.9 w54.2 h54.5)]
          Mission Debug Buttons [godot(x983.3 y548.6 w906.1 h38.8)]
            Reset [godot(x923.9 y587.4 w118.7 h0.0)]
              Button Text [txt=Reset godot(x938.8 y587.4 w88.9 h0.0)]
            Re-Roll [godot(x923.9 y587.4 w118.7 h0.0)]
              Button Text [txt=Re-Roll godot(x938.8 y587.4 w88.9 h0.0)]
            GameObject [godot(x923.9 y587.4 w118.7 h0.0)]
              Increase one [godot(x923.9 y587.4 w0.0 h0.0)]
                Button Text [txt=+1 godot(x938.8 y587.4 w-29.9 h0.0)]
              Increase half [godot(x923.9 y587.4 w0.0 h0.0)]
                Button Text [txt=+5 godot(x938.8 y587.4 w-29.9 h0.0)]
            Complete [godot(x897.6 y587.4 w171.3 h0.0)]
              Button Text [txt=Complete godot(x912.6 y587.4 w141.4 h0.0)]
            GameObject (1) [godot(x913.7 y587.4 w139.2 h0.0)]
              Text (TMP) [txt=00:00 godot(x913.7 y587.4 w0.0 h0.0)]
      Mission Header [godot(x1274.4 y15.0 w617.0 h60.7)]
        info [godot(x1844.2 y21.8 w47.2 h47.2)]
        name [txt=Daily Missions godot(x1292.9 y16.6 w499.8 h57.5)]
        Refill Counter [txt=0 Disponible godot(x1274.4 y16.6 w555.0 h57.5)]
  Weekly Mission Holder [godot(x372.4 y759.8 w1519.0 h227.5)]
    Weekly Mission [godot(x372.4 y759.8 w1519.0 h227.5)]
      raycast target [inactive godot(x372.4 y759.8 w1519.0 h227.5)]
      background [godot(x372.4 y759.8 w1519.0 h227.5)]
        header [godot(x372.4 y759.8 w379.7 h55.0)]
          name [txt=Weekly Challenge godot(x383.8 y762.3 w307.6 h50.0)]
          info [godot(x701.1 y766.8 w41.0 h41.0)]
        body [inactive godot(x1539.4 y765.6 w325.0 h94.2)]
          description [godot(x1539.4 y765.6 w325.0 h94.2)]
          image [godot(x1539.4 y765.6 w325.0 h94.2)]
        progress [godot(x412.5 y794.2 w1068.4 h158.6)]
          Mission Progress Bar [godot(x442.5 y871.8 w1008.4 h22.7)]
            Background [godot(x442.5 y871.8 w1008.4 h22.7)]
            Fill [godot(x442.5 y894.5 w0.0 h0.0)]
            Handle Slide Area [godot(x442.5 y871.8 w1008.4 h22.7)]
              Handle [godot(x439.4 y853.1 w4.2 h50.6)]
                counter [txt=13/15 godot(x414.4 y898.0 w62.6 h35.1)]
          Mission Milestones Progress [godot(x412.5 y850.4 w1068.4 h158.6)]
            steps [godot(x412.5 y803.4 w1068.4 h158.6)]
              Weekly Mission Milestones Step (3) [godot(x377.5 y927.0 w70.0 h70.0)]
                holder [godot(x377.5 y927.0 w70.0 h70.0)]
                  Image [godot(x377.5 y927.0 w70.0 h70.0)]
                  CheckMark [godot(x341.0 y897.4 w142.9 h129.1)]
                  text [txt=5 godot(x341.0 y970.5 w142.9 h56.0)]
              Weekly Mission Milestones Step (3) [godot(x377.5 y927.0 w70.0 h70.0)]
                holder [godot(x377.5 y927.0 w70.0 h70.0)]
                  Image [godot(x377.5 y927.0 w70.0 h70.0)]
                  CheckMark [godot(x341.0 y897.4 w142.9 h129.1)]
                  text [txt=5 godot(x341.0 y970.5 w142.9 h56.0)]
              Weekly Mission Milestones Step (3) [godot(x377.5 y927.0 w70.0 h70.0)]
                holder [godot(x377.5 y927.0 w70.0 h70.0)]
                  Image [godot(x377.5 y927.0 w70.0 h70.0)]
                  CheckMark [godot(x341.0 y897.4 w142.9 h129.1)]
                  text [txt=5 godot(x341.0 y970.5 w142.9 h56.0)]
              Weekly Mission Milestones Step (3) [godot(x377.5 y927.0 w70.0 h70.0)]
                holder [godot(x377.5 y927.0 w70.0 h70.0)]
                  Image [godot(x377.5 y927.0 w70.0 h70.0)]
                  CheckMark [godot(x341.0 y897.4 w142.9 h129.1)]
                  text [txt=5 godot(x341.0 y970.5 w142.9 h56.0)]
        footer [godot(x1563.7 y851.8 w300.7 h102.1)]
          Rewards [inactive godot(x485.6 y926.0 w1000.0 h113.1)]
            Reward Display Mission [godot(x485.6 y926.0 w250.0 h113.1)]
              drawerHolder [godot(x485.6 y1039.1 w0.0 h0.0)]
                Icon Campaign Points Drawer Variant [godot(x485.6 y1039.1 w0.0 h0.0)]
                  Content [godot(x485.6 y1039.1 w0.0 h0.0)]
                    Campaign Glow [godot(x485.6 y1039.1 w0.0 h0.0)]
                    Image [godot(x485.6 y1039.1 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x485.6 y1039.1 w0.0 h0.0)]
                      Price Display [godot(x485.6 y1039.1 w0.0 h0.0)]
                        icon [godot(x485.6 y1039.1 w0.0 h0.0)]
                        text [txt=2000 godot(x485.6 y1039.1 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x485.6 y1039.1 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x485.6 y1039.1 w0.0 h0.0)]
                      Price Display [godot(x485.6 y1039.1 w0.0 h0.0)]
                        icon [godot(x485.6 y1039.1 w0.0 h0.0)]
                        text [txt=24 hours godot(x485.6 y1039.1 w0.0 h0.0)]
              count [txt=200 godot(x485.6 y1039.1 w0.0 h0.0)]
            Reward Display Mission [godot(x735.6 y926.0 w250.0 h113.1)]
              drawerHolder [godot(x735.6 y1039.1 w0.0 h0.0)]
                Icon Campaign Points Drawer Variant [godot(x735.6 y1039.1 w0.0 h0.0)]
                  Content [godot(x735.6 y1039.1 w0.0 h0.0)]
                    Campaign Glow [godot(x735.6 y1039.1 w0.0 h0.0)]
                    Image [godot(x735.6 y1039.1 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x735.6 y1039.1 w0.0 h0.0)]
                      Price Display [godot(x735.6 y1039.1 w0.0 h0.0)]
                        icon [godot(x735.6 y1039.1 w0.0 h0.0)]
                        text [txt=2000 godot(x735.6 y1039.1 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x735.6 y1039.1 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x735.6 y1039.1 w0.0 h0.0)]
                      Price Display [godot(x735.6 y1039.1 w0.0 h0.0)]
                        icon [godot(x735.6 y1039.1 w0.0 h0.0)]
                        text [txt=24 hours godot(x735.6 y1039.1 w0.0 h0.0)]
              count [txt=100 godot(x735.6 y1039.1 w0.0 h0.0)]
            Reward Display Mission (1) [godot(x985.6 y926.0 w250.0 h113.1)]
              drawerHolder [godot(x985.6 y1039.1 w0.0 h0.0)]
                Icon Campaign Points Drawer Variant [godot(x985.6 y1039.1 w0.0 h0.0)]
                  Content [godot(x985.6 y1039.1 w0.0 h0.0)]
                    Campaign Glow [godot(x985.6 y1039.1 w0.0 h0.0)]
                    Image [godot(x985.6 y1039.1 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x985.6 y1039.1 w0.0 h0.0)]
                      Price Display [godot(x985.6 y1039.1 w0.0 h0.0)]
                        icon [godot(x985.6 y1039.1 w0.0 h0.0)]
                        text [txt=2000 godot(x985.6 y1039.1 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x985.6 y1039.1 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x985.6 y1039.1 w0.0 h0.0)]
                      Price Display [godot(x985.6 y1039.1 w0.0 h0.0)]
                        icon [godot(x985.6 y1039.1 w0.0 h0.0)]
                        text [txt=24 hours godot(x985.6 y1039.1 w0.0 h0.0)]
              count [txt=100 godot(x985.6 y1039.1 w0.0 h0.0)]
            Reward Display Mission (2) [godot(x1235.6 y926.0 w250.0 h113.1)]
              drawerHolder [godot(x1235.6 y1039.1 w0.0 h0.0)]
                Icon Campaign Points Drawer Variant [godot(x1235.6 y1039.1 w0.0 h0.0)]
                  Content [godot(x1235.6 y1039.1 w0.0 h0.0)]
                    Campaign Glow [godot(x1235.6 y1039.1 w0.0 h0.0)]
                    Image [godot(x1235.6 y1039.1 w0.0 h0.0)]
                    Converted Drawer [inactive godot(x1235.6 y1039.1 w0.0 h0.0)]
                      Price Display [godot(x1235.6 y1039.1 w0.0 h0.0)]
                        icon [godot(x1235.6 y1039.1 w0.0 h0.0)]
                        text [txt=2000 godot(x1235.6 y1039.1 w0.0 h0.0)]
                      AlreadyOwned [txt=Already Owned godot(x1235.6 y1039.1 w0.0 h0.0)]
                    Ephemeral Drawer [inactive godot(x1235.6 y1039.1 w0.0 h0.0)]
                      Price Display [godot(x1235.6 y1039.1 w0.0 h0.0)]
                        icon [godot(x1235.6 y1039.1 w0.0 h0.0)]
                        text [txt=24 hours godot(x1235.6 y1039.1 w0.0 h0.0)]
              count [txt=100 godot(x1235.6 y1039.1 w0.0 h0.0)]
          Generic UI Button [godot(x1570.1 y865.5 w294.3 h74.7)]
            Button Text [txt=Collect godot(x1577.1 y865.5 w280.3 h74.7)]
          TimerHolder [godot(x1563.7 y964.2 w300.7 h57.1)]
            Timer [txt=Ends in 12h 34 m godot(x1513.7 y932.9 w400.7 h57.2)]
        debug_buttons [inactive godot(x1574.9 y834.8 w261.7 h145.0)]
          Reset [godot(x1574.9 y979.8 w0.0 h0.0)]
            Button Text [txt=Reset godot(x1587.9 y979.8 w-26.0 h0.0)]
          Re-Roll [godot(x1574.9 y979.8 w0.0 h0.0)]
            Button Text [txt=Re-Roll godot(x1587.9 y979.8 w-26.0 h0.0)]
          GameObject [godot(x1574.9 y979.8 w0.0 h0.0)]
            Increase one [godot(x1574.9 y979.8 w0.0 h0.0)]
              Button Text [txt=+1 godot(x1587.9 y979.8 w-26.0 h0.0)]
            Increase half [godot(x1574.9 y979.8 w0.0 h0.0)]
              Button Text [txt=+5 godot(x1587.9 y979.8 w-26.0 h0.0)]
          Complete [godot(x1574.9 y979.8 w0.0 h0.0)]
            Button Text [txt=Complete godot(x1587.9 y979.8 w-26.0 h0.0)]
          GameObject (1) [godot(x1574.9 y979.8 w0.0 h0.0)]
            Text (TMP) [txt=00:00 godot(x1574.9 y979.8 w0.0 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Missions Tab | ✅ `scripts\rewards.gd:198 # 横向滚动 (7 天条目, 原版 Missions Tab 内容区 x[165,1920] y[153,965])` |
| Normal Missions | ✅ `scripts\quests.gd:215 # y 95.8 = 说明书 Rewards Base Submenu Variant Normal Missions 起点, 消除与周常条 (y691) 的 54px 重叠 — 2026-08-21` |
| Special Missions | ⚠️ 未命中 |
| Daily Login Container | ⚠️ 未命中 |
| raycast target | ⚠️ 未命中 |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| header | ✅ `scripts\campaign.gd:128 _build_header(); scripts\campaign.gd:180 func _build_header() -> void:` |
| name | ✅ `scripts\achievements.gd:82 for card_name in tiers:; scripts\achievements.gd:83 var lvl := int(tiers[card_name])` |
| info | ✅ `scripts\base_event_popup.gd:56 img.texture = load(SPR + "40k_shop_popup_info_bg.png"); scripts\battle.gd:1453 var info := _make_la` |
| body | ✅ `scripts\quests.gd:378 # body (原版: 图标 + counter); scripts\rule_core.gd:171 # 替身 (bodyguard, Vargard Obyron): desc "Any attack again` |
| description | ✅ `scripts\achievements.gd:229 # 描述 (原版 description); scripts\battle.gd:468 # 名字/描述层 (原版 Name and description (0,-0.77) 1.3×0.68; 名字 ` |
| image | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| progress | ✅ `scripts\achievements.gd:43 var _progress: Dictionary = {}; scripts\achievements.gd:49 _compute_progress()` |
| Mission Milestones Progress Bar | ⚠️ 未命中 |
| Progress Bar | ✅ `scripts\quests.gd:227 ## 周常挑战条 (说明书 Weekly Mission Container: header + Mission Progress Bar 1008x23 + 4 里程碑 70x70 + Reward; script` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| progress | ✅ `scripts\achievements.gd:43 var _progress: Dictionary = {}; scripts\achievements.gd:49 _compute_progress()` |
| footer | ✅ `scripts\deck_builder.gd:466 var footer := Control.new(); scripts\deck_builder.gd:467 footer.custom_minimum_size = Vector2(0, 70)` |
| Rewards | ✅ `scripts\battle.gd:3141 # 统计 (原版 AllRewardsHolder: 骷髅 + 奖励); scripts\battle.gd:3161 # 底部奖励条 (原版 EndBattlePanel → AllRewardsHolder, ` |
| Reward Display Mission | ✅ `scripts\quests.gd:315 # 里程碑奖励 (原版 Reward Display Mission 250x113 之一, 缩小版)` |
| drawerHolder | ⚠️ 未命中 |
| Currency | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Reward Display Mission | ✅ `scripts\quests.gd:315 # 里程碑奖励 (原版 Reward Display Mission 250x113 之一, 缩小版)` |
| drawerHolder | ⚠️ 未命中 |
| Campaign Points  | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| TimerHolder | ✅ `scripts\quests.gd:63 # 每日任务重置倒计时 (原版 TimerHolder 'Resets in 12h 34 m' — 到午夜); scripts\quests.gd:464 # 重置时间 (原版 TimerHolder "Resets` |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| debug_buttons | ⚠️ 未命中 |
| Reset | ✅ `scripts\daily_streak_popup.gd:3 ##   Streak Failed: 'STREAK BROKEN' + 'Streak lost: 10' + 'Reset Streak' 按钮; scripts\daily_streak_` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Re-Roll | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject | ✅ `scenes\unity_arena_battlearena1.gd:2227 n_680.name = 'GameObject'` |
| Increase one | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Increase half | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Complete | ✅ `scripts\achievements.gd:29 ["collect_all", "Complete Collection", "Collect all 1193 cards", "collect", 1193, 500],; scripts\achiev` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject (1) | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Daily Skulls Mission Container | ✅ `scripts\quests.gd:2 ## 任务界面 (原版 Mission Header + Daily Skulls Mission Container 说明书); scripts\quests.gd:214 # 3 个任务容器 (原版 Daily Sk` |
| raycast target | ⚠️ 未命中 |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| header | ✅ `scripts\campaign.gd:128 _build_header(); scripts\campaign.gd:180 func _build_header() -> void:` |
| name | ✅ `scripts\achievements.gd:82 for card_name in tiers:; scripts\achievements.gd:83 var lvl := int(tiers[card_name])` |
| info | ✅ `scripts\base_event_popup.gd:56 img.texture = load(SPR + "40k_shop_popup_info_bg.png"); scripts\battle.gd:1453 var info := _make_la` |
| body | ✅ `scripts\quests.gd:378 # body (原版: 图标 + counter); scripts\rule_core.gd:171 # 替身 (bodyguard, Vargard Obyron): desc "Any attack again` |
| description | ✅ `scripts\achievements.gd:229 # 描述 (原版 description); scripts\battle.gd:468 # 名字/描述层 (原版 Name and description (0,-0.77) 1.3×0.68; 名字 ` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| image | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| progress | ✅ `scripts\achievements.gd:43 var _progress: Dictionary = {}; scripts\achievements.gd:49 _compute_progress()` |
| milestones | ✅ `scripts\quests.gd:43 "milestones": [; scripts\quests.gd:265 var last_need := int((WEEKLY["milestones"][3] as Array)[0])` |
| steps | ✅ `scripts\battle.gd:2290 var steps: Array = _tutorial_data.get(stage_key, {}).get("steps", []); scripts\battle.gd:2290 var steps: Ar` |
| Mission Milestones Step | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Mission Milestones Step (1) | ⚠️ 未命中 |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Mission Milestones Step (2) | ⚠️ 未命中 |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Mission Milestones Step (3) | ⚠️ 未命中 |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Mission Milestones Step (4) | ⚠️ 未命中 |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| footer | ✅ `scripts\deck_builder.gd:466 var footer := Control.new(); scripts\deck_builder.gd:467 footer.custom_minimum_size = Vector2(0, 70)` |
| Rewards | ✅ `scripts\battle.gd:3141 # 统计 (原版 AllRewardsHolder: 骷髅 + 奖励); scripts\battle.gd:3161 # 底部奖励条 (原版 EndBattlePanel → AllRewardsHolder, ` |
| Reward Display Mission | ✅ `scripts\quests.gd:315 # 里程碑奖励 (原版 Reward Display Mission 250x113 之一, 缩小版)` |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Reward Display Mission | ✅ `scripts\quests.gd:315 # 里程碑奖励 (原版 Reward Display Mission 250x113 之一, 缩小版)` |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| TimerHolder | ✅ `scripts\quests.gd:63 # 每日任务重置倒计时 (原版 TimerHolder 'Resets in 12h 34 m' — 到午夜); scripts\quests.gd:464 # 重置时间 (原版 TimerHolder "Resets` |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| debug_buttons | ⚠️ 未命中 |
| Reset | ✅ `scripts\daily_streak_popup.gd:3 ##   Streak Failed: 'STREAK BROKEN' + 'Streak lost: 10' + 'Reset Streak' 按钮; scripts\daily_streak_` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Re-Roll | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject | ✅ `scenes\unity_arena_battlearena1.gd:2227 n_680.name = 'GameObject'` |
| Increase one | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Increase half | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Complete | ✅ `scripts\achievements.gd:29 ["collect_all", "Complete Collection", "Collect all 1193 cards", "collect", 1193, 500],; scripts\achiev` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject (1) | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Daily Missions | ✅ `scripts\quests.gd:212 _make_label(self, "Daily Missions · reset daily · progress from real matches", Vector2(240, 60), Vec` |
| Daily Missions Holder | ⚠️ 未命中 |
| Daily Mission Container | ⚠️ 未命中 |
| title | ✅ `scripts\achievements.gd:189 var title := str(a[1]); scripts\achievements.gd:226 # 标题 (原版 title)` |
| description | ✅ `scripts\achievements.gd:229 # 描述 (原版 description); scripts\battle.gd:468 # 名字/描述层 (原版 Name and description (0,-0.77) 1.3×0.68; 名字 ` |
| timer | ✅ `scripts\battle.gd:331 await get_tree().create_timer(_ai_delay()).timeout; scripts\battle.gd:334 await get_tree().create_timer(_ai_` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Rewards | ✅ `scripts\battle.gd:3141 # 统计 (原版 AllRewardsHolder: 骷髅 + 奖励); scripts\battle.gd:3161 # 底部奖励条 (原版 EndBattlePanel → AllRewardsHolder, ` |
| Reward Display Mission Vertical Variant | ⚠️ 未命中 |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Mission Milestones Progress Bar | ⚠️ 未命中 |
| Progress Bar | ✅ `scripts\quests.gd:227 ## 周常挑战条 (说明书 Weekly Mission Container: header + Mission Progress Bar 1008x23 + 4 里程碑 70x70 + Reward; script` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| progress | ✅ `scripts\achievements.gd:43 var _progress: Dictionary = {}; scripts\achievements.gd:49 _compute_progress()` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Trash mission | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Mission Debug Buttons | ⚠️ 未命中 |
| Reset | ✅ `scripts\daily_streak_popup.gd:3 ##   Streak Failed: 'STREAK BROKEN' + 'Streak lost: 10' + 'Reset Streak' 按钮; scripts\daily_streak_` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Re-Roll | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject | ✅ `scenes\unity_arena_battlearena1.gd:2227 n_680.name = 'GameObject'` |
| Increase one | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Increase half | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Complete | ✅ `scripts\achievements.gd:29 ["collect_all", "Complete Collection", "Collect all 1193 cards", "collect", 1193, 500],; scripts\achiev` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject (1) | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Daily Mission Container (1) | ⚠️ 未命中 |
| title | ✅ `scripts\achievements.gd:189 var title := str(a[1]); scripts\achievements.gd:226 # 标题 (原版 title)` |
| description | ✅ `scripts\achievements.gd:229 # 描述 (原版 description); scripts\battle.gd:468 # 名字/描述层 (原版 Name and description (0,-0.77) 1.3×0.68; 名字 ` |
| timer | ✅ `scripts\battle.gd:331 await get_tree().create_timer(_ai_delay()).timeout; scripts\battle.gd:334 await get_tree().create_timer(_ai_` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Rewards | ✅ `scripts\battle.gd:3141 # 统计 (原版 AllRewardsHolder: 骷髅 + 奖励); scripts\battle.gd:3161 # 底部奖励条 (原版 EndBattlePanel → AllRewardsHolder, ` |
| Reward Display Mission Vertical Variant | ⚠️ 未命中 |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Mission Milestones Progress Bar | ⚠️ 未命中 |
| Progress Bar | ✅ `scripts\quests.gd:227 ## 周常挑战条 (说明书 Weekly Mission Container: header + Mission Progress Bar 1008x23 + 4 里程碑 70x70 + Reward; script` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| progress | ✅ `scripts\achievements.gd:43 var _progress: Dictionary = {}; scripts\achievements.gd:49 _compute_progress()` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Trash mission | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Mission Debug Buttons | ⚠️ 未命中 |
| Reset | ✅ `scripts\daily_streak_popup.gd:3 ##   Streak Failed: 'STREAK BROKEN' + 'Streak lost: 10' + 'Reset Streak' 按钮; scripts\daily_streak_` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Re-Roll | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject | ✅ `scenes\unity_arena_battlearena1.gd:2227 n_680.name = 'GameObject'` |
| Increase one | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Increase half | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Complete | ✅ `scripts\achievements.gd:29 ["collect_all", "Complete Collection", "Collect all 1193 cards", "collect", 1193, 500],; scripts\achiev` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject (1) | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Daily Mission Container (2) | ⚠️ 未命中 |
| title | ✅ `scripts\achievements.gd:189 var title := str(a[1]); scripts\achievements.gd:226 # 标题 (原版 title)` |
| description | ✅ `scripts\achievements.gd:229 # 描述 (原版 description); scripts\battle.gd:468 # 名字/描述层 (原版 Name and description (0,-0.77) 1.3×0.68; 名字 ` |
| timer | ✅ `scripts\battle.gd:331 await get_tree().create_timer(_ai_delay()).timeout; scripts\battle.gd:334 await get_tree().create_timer(_ai_` |
| Separator Line | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Rewards | ✅ `scripts\battle.gd:3141 # 统计 (原版 AllRewardsHolder: 骷髅 + 奖励); scripts\battle.gd:3161 # 底部奖励条 (原版 EndBattlePanel → AllRewardsHolder, ` |
| Reward Display Mission Vertical Variant | ⚠️ 未命中 |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Mission Milestones Progress Bar | ⚠️ 未命中 |
| Progress Bar | ✅ `scripts\quests.gd:227 ## 周常挑战条 (说明书 Weekly Mission Container: header + Mission Progress Bar 1008x23 + 4 里程碑 70x70 + Reward; script` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| progress | ✅ `scripts\achievements.gd:43 var _progress: Dictionary = {}; scripts\achievements.gd:49 _compute_progress()` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Trash mission | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Mission Debug Buttons | ⚠️ 未命中 |
| Reset | ✅ `scripts\daily_streak_popup.gd:3 ##   Streak Failed: 'STREAK BROKEN' + 'Streak lost: 10' + 'Reset Streak' 按钮; scripts\daily_streak_` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Re-Roll | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject | ✅ `scenes\unity_arena_battlearena1.gd:2227 n_680.name = 'GameObject'` |
| Increase one | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Increase half | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Complete | ✅ `scripts\achievements.gd:29 ["collect_all", "Complete Collection", "Collect all 1193 cards", "collect", 1193, 500],; scripts\achiev` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GameObject (1) | ⚠️ 未命中 |
| Text (TMP) | ⚠️ 未命中 |
| Mission Header | ✅ `scripts\quests.gd:2 ## 任务界面 (原版 Mission Header + Daily Skulls Mission Container 说明书); scripts\quests.gd:160 # 任务标题区 (原版 Mission He` |
| info | ✅ `scripts\base_event_popup.gd:56 img.texture = load(SPR + "40k_shop_popup_info_bg.png"); scripts\battle.gd:1453 var info := _make_la` |
| name | ✅ `scripts\achievements.gd:82 for card_name in tiers:; scripts\achievements.gd:83 var lvl := int(tiers[card_name])` |
| Refill Counter | ⚠️ 未命中 |
| Weekly Mission Holder | ✅ `scripts\quests.gd:39 # 周常挑战 (原版 Weekly Mission Holder: 'Weekly Challenge' + 进度条 + 4 里程碑 + 4 奖励); scripts\quests.gd:223 # 周常挑战条 (原版` |
| Weekly Mission | ✅ `scripts\quests.gd:39 # 周常挑战 (原版 Weekly Mission Holder: 'Weekly Challenge' + 进度条 + 4 里程碑 + 4 奖励); scripts\quests.gd:223 # 周常挑战条 (原版` |
| raycast target | ⚠️ 未命中 |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| header | ✅ `scripts\campaign.gd:128 _build_header(); scripts\campaign.gd:180 func _build_header() -> void:` |
| name | ✅ `scripts\achievements.gd:82 for card_name in tiers:; scripts\achievements.gd:83 var lvl := int(tiers[card_name])` |
| info | ✅ `scripts\base_event_popup.gd:56 img.texture = load(SPR + "40k_shop_popup_info_bg.png"); scripts\battle.gd:1453 var info := _make_la` |
| body | ✅ `scripts\quests.gd:378 # body (原版: 图标 + counter); scripts\rule_core.gd:171 # 替身 (bodyguard, Vargard Obyron): desc "Any attack again` |
| description | ✅ `scripts\achievements.gd:229 # 描述 (原版 description); scripts\battle.gd:468 # 名字/描述层 (原版 Name and description (0,-0.77) 1.3×0.68; 名字 ` |
| image | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| progress | ✅ `scripts\achievements.gd:43 var _progress: Dictionary = {}; scripts\achievements.gd:49 _compute_progress()` |
| Mission Progress Bar | ✅ `scripts\quests.gd:227 ## 周常挑战条 (说明书 Weekly Mission Container: header + Mission Progress Bar 1008x23 + 4 里程碑 70x70 + Reward; script` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| Mission Milestones Progress | ⚠️ 未命中 |
| steps | ✅ `scripts\battle.gd:2290 var steps: Array = _tutorial_data.get(stage_key, {}).get("steps", []); scripts\battle.gd:2290 var steps: Ar` |
| Weekly Mission Milestones Step (3) | ⚠️ 未命中 |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Weekly Mission Milestones Step (3) | ⚠️ 未命中 |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Weekly Mission Milestones Step (3) | ⚠️ 未命中 |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Weekly Mission Milestones Step (3) | ⚠️ 未命中 |
| holder | ✅ `scripts\battle.gd:404 var holder := Node3D.new(); scripts\battle.gd:405 holder.name = "Card3D_%d_%d" % [p, slot]` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| footer | ✅ `scripts\deck_builder.gd:466 var footer := Control.new(); scripts\deck_builder.gd:467 footer.custom_minimum_size = Vector2(0, 70)` |
| Rewards | ✅ `scripts\battle.gd:3141 # 统计 (原版 AllRewardsHolder: 骷髅 + 奖励); scripts\battle.gd:3161 # 底部奖励条 (原版 EndBattlePanel → AllRewardsHolder, ` |
| Reward Display Mission | ✅ `scripts\quests.gd:315 # 里程碑奖励 (原版 Reward Display Mission 250x113 之一, 缩小版)` |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Reward Display Mission | ✅ `scripts\quests.gd:315 # 里程碑奖励 (原版 Reward Display Mission 250x113 之一, 缩小版)` |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Reward Display Mission (1) | ⚠️ 未命中 |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Reward Display Mission (2) | ⚠️ 未命中 |
| drawerHolder | ⚠️ 未命中 |
| Icon Campaign Points Drawer Variant | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Campaign Glow | ✅ `scripts\quests.gd:181 # 战役入口辉光 (原版 Campaign Glow 活动辉光 sprite:-7870341820918878983, 脉动)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Converted Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| AlreadyOwned | ⚠️ 未命中 |
| Ephemeral Drawer | ⚠️ 未命中 |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| count | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\achievements.gd:103 "deck_5": GameData.de` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |

## 摘要

- 规格元素: 417
- 代码命中: 285
- ⚠️未命中: 115 (以下需人工判断)

- `Special Missions`
- `Daily Login Container`
- `raycast target`
- `Mission Milestones Progress Bar`
- `Handle Slide Area`
- `drawerHolder`
- `Currency`
- `drawerHolder`
- `Campaign Points `
- `debug_buttons`
- `Re-Roll`
- `Increase one`
- `Increase half`
- `GameObject (1)`
- `Text (TMP)`
- `raycast target`
- `Mission Milestones Step (1)`
- `Mission Milestones Step (2)`
- `Mission Milestones Step (3)`
- `Mission Milestones Step (4)`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `debug_buttons`
- `Re-Roll`
- `Increase one`
- `Increase half`
- `GameObject (1)`
- `Text (TMP)`
- `Daily Missions Holder`
- `Daily Mission Container`
- `Reward Display Mission Vertical Variant`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Mission Milestones Progress Bar`
- `Handle Slide Area`
- `Trash mission`
- `Mission Debug Buttons`
- `Re-Roll`
- `Increase one`
- `Increase half`
- `GameObject (1)`
- `Text (TMP)`
- `Daily Mission Container (1)`
- `Reward Display Mission Vertical Variant`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Mission Milestones Progress Bar`
- `Handle Slide Area`
- `Trash mission`
- `Mission Debug Buttons`
- `Re-Roll`
- `Increase one`
- `Increase half`
- `GameObject (1)`
- `Text (TMP)`
- `Daily Mission Container (2)`
- `Reward Display Mission Vertical Variant`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Mission Milestones Progress Bar`
- `Handle Slide Area`
- `Trash mission`
- `Mission Debug Buttons`
- `Re-Roll`
- `Increase one`
- `Increase half`
- `GameObject (1)`
- `Text (TMP)`
- `Refill Counter`
- `raycast target`
- `Handle Slide Area`
- `Mission Milestones Progress`
- `Weekly Mission Milestones Step (3)`
- `Weekly Mission Milestones Step (3)`
- `Weekly Mission Milestones Step (3)`
- `Weekly Mission Milestones Step (3)`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Reward Display Mission (1)`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`
- `Reward Display Mission (2)`
- `drawerHolder`
- `Icon Campaign Points Drawer Variant`
- `Converted Drawer`
- `AlreadyOwned`
- `Ephemeral Drawer`