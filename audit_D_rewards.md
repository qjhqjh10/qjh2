# UI 规格审计: Rewards Base Submenu Variant

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Rewards Base Submenu Variant [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Content Area [godot(x167.2 y70.9 w1752.8 h1009.1)]
    Background [godot(x167.2 y70.9 w1752.8 h1009.1)]
    Tab Buttons [godot(x167.2 y70.9 w165.0 h1009.1)]
      MissionsRewardsButton [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [sprite=40K_rewards_bt_missions godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Missions godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1089.7 w35.0 h35.0)]
          OneText [godot(x201.4 y1090.6 w35.0 h35.0)]
      CampaignRewardsButton [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Campaign godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1089.7 w35.0 h35.0)]
          OneText [godot(x201.4 y1090.6 w35.0 h35.0)]
      Forge Button [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Forge godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1089.7 w35.0 h35.0)]
          OneText [godot(x201.4 y1090.6 w35.0 h35.0)]
      Menu Navigation Panel Button [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Booster Packs godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1014.6 w35.0 h35.0)]
          OneText [godot(x201.4 y1015.5 w35.0 h35.0)]
      Shadow [godot(x167.2 y70.9 w47.6 h1009.1)]
    Tabs [godot(x167.2 y70.9 w1752.8 h1009.1)]
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
      Forge Tab [inactive godot(x330.7 y71.1 w1589.3 h1008.7)]
        Background [godot(x330.7 y71.1 w1589.3 h1008.7)]
          Warp [godot(x741.8 y88.5 w767.0 h974.0)]
          War ParticleSystemUI [godot(x1125.3 y575.5 w0.0 h0.0)]
            Warp Particle System [godot(x1125.3 y575.5 w0.0 h0.0)]
        Ready for level up [godot(x1028.1 y424.1 w194.5 h302.8)]
          Glow [godot(x775.3 y225.5 w700.0 h700.0)]
          War ParticleSystemUI Down [godot(x1125.3 y949.5 w0.0 h0.0)]
            Rays [godot(x1125.3 y949.5 w0.0 h0.0)]
              Glow (1) [godot(x1125.3 y949.5 w0.0 h0.0)]
          War ParticleSystem Up [godot(x1125.3 y191.5 w0.0 h0.0)]
            Rays [godot(x1125.3 y191.5 w0.0 h0.0)]
              Glow [godot(x1125.3 y191.5 w0.0 h0.0)]
        Rewards Scroll View [godot(x331.0 y318.6 w1588.7 h761.4)]
          Viewport [godot(x331.0 y318.6 w1588.7 h761.4)]
            Rewards Content [godot(x331.0 y318.6 w122.0 h761.4)]
        Forge Army Selector [godot(x588.2 y71.6 w1074.3 h125.1)]
          Separator Line [godot(x491.4 y191.4 w1267.9 h6.0)]
          Viewport [godot(x588.2 y71.6 w1074.3 h125.1)]
            Army Content [godot(x1125.3 y71.6 w0.0 h126.0)]
        Background Elements [godot(x330.7 y71.1 w1589.3 h1008.7)]
          Decoration Top [godot(x444.7 y185.1 w273.0 h210.0)]
          Column Left [godot(x330.7 y15.2 w373.0 h1452.9)]
            Culumn Top [godot(x330.7 y8.5 w331.8 h478.4)]
              Candle [godot(x458.5 y188.3 w40.0 h59.0)]
              Culumn Mid [godot(x330.7 y486.9 w214.2 h479.4)]
                Culumn Down [godot(x330.7 y966.3 w221.5 h493.0)]
              Light Candle [godot(x358.8 y154.2 w142.6 h175.5)]
          Column Right [godot(x1920.0 y15.2 w-373.0 h1452.9)]
            Culumn Top [godot(x1920.0 y2927.6 w-331.8 h-478.4)]
              Candle (1) [godot(x1753.7 y2747.8 w40.0 h-59.0)]
              Light Candle (1) [godot(x1891.9 y2781.9 w-142.4 h-175.5)]
              Culumn Mid [godot(x1920.0 y2449.2 w-214.2 h-479.4)]
                Culumn Down [godot(x1920.0 y1969.8 w-221.5 h-493.0)]
        Selected Army Info [godot(x619.4 y195.8 w621.3 h122.7)]
          ArmyText [txt=Ultramarines godot(x762.9 y209.4 w320.9 h50.0)]
          LevelText [txt=Level 1/50 godot(x766.1 y252.8 w331.0 h50.0)]
          Army Icon [godot(x621.8 y188.4 w125.2 h125.3)]
          Xp Points Icon [inactive godot(x758.1 y292.5 w53.0 h53.0)]
            TotalXp Points [txt=154748 godot(x811.1 y294.0 w232.3 h50.0)]
        Debug Add points [inactive godot(x947.4 y214.2 w203.7 h53.9)]
          Text (TMP) [txt=Debug add points godot(x947.4 y214.2 w203.7 h53.9)]
          InputField (TMP) [godot(x1161.2 y214.2 w84.5 h53.9)]
            Text Area [godot(x1171.2 y221.2 w64.5 h40.9)]
              Placeholder [txt=Enter text... godot(x1171.2 y221.2 w64.5 h40.9)]
              Text [txt=5​ godot(x1171.2 y221.2 w64.5 h40.9)]
        Debug Set Forge [inactive godot(x1278.5 y215.9 w203.7 h53.9)]
          Text (TMP) [txt=Set Forge Level godot(x1278.5 y215.9 w203.7 h53.9)]
          InputField (TMP) [godot(x1492.3 y215.9 w84.5 h53.9)]
            Text Area [godot(x1502.3 y222.9 w64.5 h40.9)]
              Placeholder [txt=Enter text... godot(x1502.3 y222.9 w64.5 h40.9)]
              Text [txt=5​ godot(x1502.3 y222.9 w64.5 h40.9)]
        Help Icon [godot(x1685.2 y215.9 w52.2 h52.2)]
      Campaign Tab [inactive godot(x330.7 y70.9 w1589.3 h1009.1)]
        Campaign Background [godot(x330.3 y70.9 w1589.7 h1009.1)]
          Background Image [inactive godot(x330.3 y-45.2 w1589.7 h1589.7)]
        Campaign Army Selector [godot(x745.9 y70.9 w1174.4 h137.0)]
          Background [godot(x643.2 y71.4 w1277.1 h136.0)]
          Viewport [godot(x745.9 y70.9 w1174.4 h137.0)]
            Army Content [godot(x916.1 y70.9 w0.0 h137.0)]
        Campaign Header [godot(x330.7 y60.9 w460.2 h165.0)]
          Debug Point Button [inactive godot(x1146.2 y91.6 w245.0 h67.7)]
            Button Text [txt=Change Deck godot(x1157.9 y98.2 w220.8 h54.4)]
          Army Icon [godot(x345.7 y60.9 w135.0 h165.0)]
          Title [txt=ULTRAMARINES godot(x480.7 y60.9 w225.0 h74.3)]
          Premium Button Container [inactive godot(x743.2 y60.9 w262.5 h82.5)]
            Premium Button [godot(x743.2 y143.4 w0.0 h0.0)]
              Button Text [txt=Premium godot(x743.2 y143.4 w0.0 h0.0)]
            Premium pruchased [sprite=40k_campaign_Premium-icon godot(x811.2 y92.5 w54.1 h54.1)]
              Text (TMP) [txt=Premium godot(x865.3 y92.5 w141.9 h54.1)]
          Points [txt=Points: 69 godot(x480.7 y151.7 w368.2 h33.0)]
            Point Icon [godot(x828.1 y135.2 w100.0 h66.0)]
              Campaign Point Background [godot(x818.1 y128.6 w120.0 h79.2)]
              Army Icon [godot(x828.1 y135.2 w100.0 h66.0)]
          Info Button [godot(x719.8 y94.0 w41.2 h41.2)]
        Campaign Track [godot(x330.7 y335.5 w1589.6 h709.0)]
          Viewport [godot(x330.7 y285.5 w1589.6 h759.0)]
            Content [godot(x330.7 y335.5 w200.0 h659.0)]
        Premium Panel [godot(x344.3 y1080.0 w376.0 h0.0)]
          Background [godot(x344.3 y1080.0 w376.0 h0.0)]
          Title [txt=Premium Campaign daily bonus godot(x166.4 y1058.8 w355.8 h42.4)]
          Points [godot(x206.6 y1051.0 w275.4 h58.0)]
            Quantity [txt=200 godot(x270.4 y1051.0 w77.0 h58.0)]
            Points [godot(x141.6 y1074.1 w65.0 h69.7)]
              Icon Campaign Points Drawer Variant [godot(x141.6 y1143.8 w0.0 h0.0)]
                Content [godot(x141.6 y1143.8 w0.0 h0.0)]
                  Campaign Glow [godot(x141.6 y1143.8 w0.0 h0.0)]
                  Image [godot(x141.6 y1143.8 w0.0 h0.0)]
                  Converted Drawer [inactive godot(x141.6 y1143.8 w0.0 h0.0)]
                    Price Display [godot(x141.6 y1143.8 w0.0 h0.0)]
                      icon [godot(x141.6 y1143.8 w0.0 h0.0)]
                      text [txt=2000 godot(x141.6 y1143.8 w0.0 h0.0)]
                    AlreadyOwned [txt=Already Owned godot(x141.6 y1143.8 w0.0 h0.0)]
                  Ephemeral Drawer [inactive godot(x141.6 y1143.8 w0.0 h0.0)]
                    Price Display [godot(x141.6 y1143.8 w0.0 h0.0)]
                      icon [godot(x141.6 y1143.8 w0.0 h0.0)]
                      text [txt=24 hours godot(x141.6 y1143.8 w0.0 h0.0)]
          Generic Simplified UI Button [godot(x216.3 y1052.3 w256.0 h55.4)]
            Button Text [txt=Continue godot(x225.2 y1057.6 w238.1 h46.8)]
          Timer [godot(x344.3 y1080.0 w348.4 h39.3)]
            Icon [godot(x344.3 y1100.0 w38.5 h38.6)]
            Timer Text [txt=Siguiente: 5d 20h 15m godot(x394.8 y1087.4 w285.9 h24.5)]
        Tutorial Message [inactive godot(x1184.1 y220.4 w567.1 h120.2)]
          Background [godot(x1142.1 y250.5 w651.0 h60.1)]
          Mask [godot(x1189.2 y255.1 w557.1 h50.5)]
            Background fill [sprite=40k_popup_texture godot(x1189.2 y255.1 w557.1 h50.5)]
          ChooseArmyText [txt=Choose your favourite faction. You can l godot(x1160.5 y255.3 w618.1 h51.4)]
          Highlight Down [sprite=Border Line Only Horizontal FX godot(x1031.4 y222.2 w898.3 h28.3)]
          Highlight Up [sprite=Border Line Only Horizontal FX godot(x1031.4 y160.0 w898.3 h28.2)]
    Shadow (1) [inactive godot(x330.4 y70.9 w49.4 h1009.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Rewards Base Submenu Variant | ✅ `scripts\quests.gd:215 # y 95.8 = 说明书 Rewards Base Submenu Variant Normal Missions 起点, 消除与周常条 (y691) 的 54px 重叠 — 2026-08-21; script` |
| Content Area | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\rewards.gd:145` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Tab Buttons | ✅ `scripts\collection.gd:150 # ---- Tab Buttons (原版 [167.2,158.6 165x921.4] 左竖排 4 tab — RectTransform_-1995773233925987627) ----; scr` |
| MissionsRewardsButton | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| CampaignRewardsButton | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Forge Button | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Menu Navigation Panel Button | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| Tabs | ✅ `scripts\shop.gd:163 # 3 个标签页 (Tabs 区 x330-1920)` |
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

## 摘要

- 规格元素: 561
- 代码命中: 289
- ⚠️未命中: 111 (以下需人工判断)

- `MissionsRewardsButton`
- `OneText`
- `CampaignRewardsButton`
- `OneText`
- `Forge Button`
- `OneText`
- `Menu Navigation Panel Button`
- `OneText`
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