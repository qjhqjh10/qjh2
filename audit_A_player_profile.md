# UI 规格审计: Player Profile Window

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Player Profile Window [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Menu Dark Background [godot(x-1327.3 y-746.2 w4574.6 h2572.4)]
  Menu Area [godot(x0.0 y0.0 w1920.0 h1080.0)]
    Tab Buttons [godot(x95.5 y180.2 w178.0 h705.6)]
      Profile Button [godot(x13.0 y885.8 w165.0 h0.0)]
        button_bg [godot(x13.0 y885.8 w165.0 h0.0)]
        Icon [godot(x24.8 y826.1 w141.4 h94.1)]
        Label [godot(x18.0 y897.5 w155.0 h40.0)]
          Tab Toggle Title [txt=Profile godot(x18.0 y897.5 w155.0 h40.0)]
      Avatar Button [godot(x13.0 y885.8 w165.0 h0.0)]
        button_bg [godot(x13.0 y886.6 w165.0 h0.0)]
        Icon [godot(x18.0 y825.1 w155.0 h96.1)]
        Label [godot(x18.0 y895.8 w155.0 h40.0)]
          Tab Toggle Title [txt=Avatar godot(x18.0 y895.8 w155.0 h40.0)]
      Title Button [godot(x13.0 y885.8 w165.0 h0.0)]
        button_bg [godot(x13.0 y886.6 w165.0 h0.0)]
        Icon [godot(x25.3 y820.0 w140.3 h85.4)]
        Label [godot(x18.0 y905.4 w155.0 h32.0)]
          Tab Toggle Title [txt=Title godot(x18.0 y905.4 w155.0 h32.0)]
      Battle Log Button [godot(x13.0 y885.8 w165.0 h0.0)]
        button_bg [godot(x13.0 y886.6 w165.0 h0.0)]
        Icon [godot(x24.8 y826.0 w141.4 h93.3)]
        Label [godot(x18.0 y895.8 w155.0 h40.0)]
          Tab Toggle Title [txt=Battle Log godot(x18.0 y895.8 w155.0 h40.0)]
      Trophies [godot(x13.0 y885.8 w165.0 h0.0)]
        button_bg [godot(x13.0 y886.6 w165.0 h0.0)]
        Icon [godot(x24.8 y827.3 w141.4 h93.3)]
        Label [godot(x18.0 y895.8 w155.0 h40.0)]
          Tab Toggle Title [txt=Achievements godot(x18.0 y895.8 w155.0 h40.0)]
      Ranked [godot(x13.0 y885.8 w165.0 h0.0)]
        button_bg [godot(x13.0 y886.6 w165.0 h0.0)]
        Icon [godot(x24.8 y831.9 w141.4 h87.1)]
        Label [godot(x18.0 y895.8 w155.0 h40.0)]
          Tab Toggle Title [txt=Ranking godot(x18.0 y895.8 w155.0 h40.0)]
    Tab  Area [godot(x273.5 y118.0 w1551.0 h844.0)]
      Generic Window Red Background Big [godot(x273.5 y118.9 w1551.0 h843.1)]
      Generic Close Button Orange [godot(x1760.8 y118.9 w74.4 h75.6)]
        Background [godot(x1769.0 y126.9 w56.8 h58.1)]
        Icon [godot(x1769.0 y126.9 w56.8 h58.1)]
      Tab Content [godot(x351.0 y118.9 w1396.0 h843.1)]
        Profile Tab [inactive godot(x351.0 y118.9 w1396.0 h843.1)]
          Invite to alliance [godot(x1532.4 y865.9 w214.6 h45.1)]
            Button Outline [godot(x1532.9 y865.9 w213.6 h45.1)]
            Text [txt=Invite to Alliance godot(x1544.5 y874.5 w190.4 h27.9)]
          PlayerId [godot(x351.0 y867.4 w562.4 h40.0)]
            Image [godot(x350.7 y867.9 w27.2 h39.0)]
            playerIdText [txt=Player id: gdajhahjaihj godot(x387.0 y867.4 w519.1 h40.0)]
          Consecutive login days [inactive godot(x1258.0 y867.4 w490.0 h34.9)]
            playerIdText [txt=Consecutive login days: 312 days godot(x1258.0 y867.4 w490.0 h34.9)]
          Player Info [godot(x351.0 y168.2 w836.0 h152.3)]
            Avatar Item Small [godot(x351.0 y168.2 w159.2 h152.3)]
              Raycast Target [godot(x341.2 y128.0 w178.9 h214.4)]
              Image Container [godot(x351.0 y168.2 w159.2 h115.0)]
                Highlight [godot(x277.9 y112.0 w308.7 h222.1)]
                Border [godot(x331.1 y165.3 w199.0 h143.8)]
                Image [godot(x271.5 y108.0 w318.3 h230.0)]
              Avatar Name [inactive txt=Avatar name godot(x351.0 y320.5 w159.2 h41.4)]
            Info Section with Alliance [inactive godot(x510.2 y168.2 w895.7 h152.3)]
              Name and Title Holder [godot(x510.2 y168.2 w864.3 h49.8)]
                Edit Name Button [godot(x510.2 y168.2 w53.1 h49.8)]
                  Button Outline [godot(x510.7 y168.2 w52.1 h49.8)]
                  Icon [godot(x510.2 y168.2 w53.1 h49.8)]
                Player Name [txt=Player Name godot(x568.3 y168.2 w241.7 h49.8)]
                Player Title [txt=Player Title godot(x815.0 y168.2 w559.5 h49.8)]
              Alliance Info [godot(x510.2 y220.5 w878.6 h66.0)]
                Alliance Name [txt=Alliance Name godot(x510.2 y212.1 w878.6 h39.0)]
                Alliance Rating Display [godot(x510.2 y251.1 w263.9 h35.4)]
                  Secondary Icon [inactive godot(x510.2 y251.1 w44.4 h59.1)]
                  Main Icon [godot(x510.2 y246.9 w49.3 h43.7)]
                  Individual rating value [txt=------ godot(x559.5 y251.1 w214.6 h35.4)]
            Info Section without Alliance [godot(x510.2 y168.2 w895.7 h152.3)]
              Name and Title Holder [godot(x510.2 y168.2 w864.3 h49.8)]
                NameHolder [godot(x510.2 y168.2 w616.9 h49.8)]
                  Edit Name Button [godot(x510.2 y168.2 w53.1 h49.8)]
                    Button Outline [godot(x510.7 y168.2 w52.1 h49.8)]
                    Icon [godot(x510.2 y168.2 w53.1 h49.8)]
                  Player Name [txt=Player Name godot(x563.3 y170.7 w242.4 h47.3)]
                Player Title [txt=Warrior of the raging winds godot(x510.2 y218.0 w616.9 h49.8)]
            Player Level [godot(x453.1 y259.2 w53.2 h53.1)]
              Player Level Text [txt=- godot(x460.0 y266.1 w39.4 h39.4)]
          Ranking [godot(x351.0 y327.7 w786.1 h529.5)]
            Current Rank [godot(x351.0 y327.7 w425.3 h529.5)]
              LeaderboardButton [inactive godot(x418.2 y189.6 w290.9 h53.2)]
                Button Text [txt=Leaderboard godot(x431.5 y194.8 w263.4 h42.8)]
              Generic Window Red Background Small [godot(x351.0 y327.7 w425.3 h529.5)]
              Content [godot(x375.7 y339.7 w372.6 h489.4)]
                Title [txt=Current Rank godot(x381.6 y339.7 w360.9 h48.9)]
                RankTitleBG [godot(x374.4 y388.6 w375.3 h60.0)]
                  DivisionText [txt=Division V godot(x384.3 y388.6 w355.4 h60.0)]
                Timer [inactive godot(x195.2 y829.1 w361.0 h0.0)]
                  Timer Icon [godot(x178.7 y812.6 w33.0 h33.0)]
                  Timer [txt=Ends in: 23d 5h godot(x311.3 y834.1 w167.7 h55.9)]
                spacing [godot(x424.9 y448.6 w274.2 h10.0)]
                DivisionImage [godot(x317.7 y458.6 w488.7 h0.0)]
                  RankImage [godot(x513.2 y463.6 w97.7 h-10.0)]
                footer [godot(x357.0 y458.6 w410.0 h180.0)]
                  Highest Faction Rating [inactive godot(x179.3 y618.7 w355.5 h39.8)]
                    Rating Text [godot(x179.3 y628.9 w0.0 h59.2)]
                      Secondary Icon [godot(x179.3 y688.1 w0.0 h0.0)]
                      Main Icon [godot(x179.3 y688.1 w0.0 h0.0)]
                      Individual rating value [txt=4879 godot(x179.3 y688.1 w0.0 h0.0)]
                  MainRating [inactive godot(x368.9 y458.6 w386.3 h60.3)]
                    Mission Milestones Progress [godot(x368.9 y445.5 w146.4 h86.5)]
                      counter [inactive txt=16 godot(x373.2 y218.1 w80.0 h52.2)]
                      steps [godot(x368.9 y445.5 w146.4 h86.5)]
                        RankedSealStep [godot(x363.4 y449.5 w47.6 h78.5)]
                          Empty [godot(x363.4 y449.5 w47.6 h78.5)]
                          Fill [godot(x363.4 y449.5 w47.6 h78.5)]
                        RankedSealStep (2) [godot(x400.0 y449.5 w47.6 h78.5)]
                          Empty [godot(x400.0 y449.5 w47.6 h78.5)]
                          Fill [godot(x400.0 y449.5 w47.6 h78.5)]
                        RankedSealStep (3) [godot(x436.6 y449.5 w47.6 h78.5)]
                          Empty [godot(x436.6 y449.5 w47.6 h78.5)]
                          Fill [godot(x436.6 y449.5 w47.6 h78.5)]
                        RankedSealStep (4) [godot(x473.2 y449.5 w47.6 h78.5)]
                          Empty [godot(x473.2 y449.5 w47.6 h78.5)]
                          Fill [godot(x473.2 y449.5 w47.6 h78.5)]
                    Global Rating [godot(x515.3 y460.1 w239.9 h57.3)]
                      Secondary Icon [inactive godot(x515.3 y517.4 w0.0 h0.0)]
                      Main Icon [godot(x588.5 y460.1 w60.0 h57.3)]
                      Individual rating value [txt=32 godot(x648.5 y469.8 w33.5 h37.9)]
            Highest Rank [godot(x777.7 y327.7 w359.4 h529.5)]
              LeaderboardButton [inactive godot(x811.9 y189.6 w291.0 h53.2)]
                Button Text [txt=Leaderboard godot(x825.3 y194.8 w263.3 h42.8)]
              Generic Window Red Background Small [godot(x777.7 y327.7 w359.4 h529.5)]
              Content [godot(x798.3 y340.5 w315.1 h466.2)]
                Title [txt=Highest Rank godot(x805.8 y340.5 w300.0 h48.9)]
                RankTitleBG [godot(x727.2 y389.4 w457.2 h60.0)]
                  DivisionText [txt=Division V godot(x778.1 y400.2 w355.4 h38.4)]
                Timer [inactive godot(x617.8 y806.7 w361.0 h0.0)]
                  Timer Icon [godot(x601.3 y790.2 w33.0 h33.0)]
                  Timer [txt=Ends in: 23d 5h godot(x733.9 y811.7 w167.6 h55.9)]
                DivisionImage [godot(x721.3 y449.4 w469.1 h0.0)]
                  RankImage [godot(x908.9 y459.0 w93.8 h-9.6)]
                footer [godot(x750.8 y449.4 w410.0 h140.9)]
                  Highest Faction Rating [inactive godot(x778.1 y465.7 w355.5 h0.0)]
                    Rating Text [godot(x879.3 y447.8 w153.1 h35.9)]
                      Secondary Icon [godot(x879.3 y447.8 w43.0 h35.9)]
                      Main Icon [godot(x900.8 y447.8 w43.0 h35.9)]
                      Individual rating value [txt=4879 godot(x965.3 y447.8 w67.1 h35.9)]
                  MainRating [godot(x762.6 y498.3 w386.4 h43.1)]
                    Mission Milestones Progress [inactive godot(x762.6 y476.6 w355.5 h86.5)]
                      counter [inactive txt=16 godot(x766.9 y249.2 w80.0 h52.2)]
                      steps [inactive godot(x762.6 y476.6 w355.5 h86.5)]
                        RankedSealStep [godot(x762.6 y454.4 w71.1 h44.4)]
                          Empty [godot(x762.6 y454.4 w71.1 h44.4)]
                          Fill [godot(x762.6 y454.4 w71.1 h44.4)]
                    Global Rating [godot(x762.6 y502.7 w386.4 h34.4)]
                      Secondary Icon [inactive godot(x762.6 y537.1 w0.0 h0.0)]
                      Main Icon [godot(x909.1 y497.4 w60.0 h45.0)]
                      Individual rating value [txt=32 godot(x969.1 y502.7 w33.5 h34.4)]
                legendary title [txt=Legendary Points godot(x818.7 y590.3 w274.2 h34.3)]
                Legendarey Counter [godot(x789.4 y624.6 w332.8 h159.8)]
                  Rating Text [godot(x790.5 y686.4 w330.7 h36.2)]
                    Secondary Icon [inactive godot(x790.5 y722.6 w0.0 h0.0)]
                    Main Icon [godot(x912.4 y682.0 w60.0 h45.0)]
                    Individual rating value [txt=32 godot(x972.4 y689.3 w26.9 h30.4)]
                spacing [godot(x818.7 y784.4 w274.2 h22.3)]
            Legendary Display Profile [godot(x777.7 y327.7 w359.4 h529.5)]
              Generic Window Red Background Small [godot(x777.7 y327.7 w359.4 h529.5)]
              Content [godot(x798.3 y340.5 w315.1 h466.2)]
                DivisionImage [godot(x721.3 y374.2 w469.1 h397.2)]
                  RankImage [inactive godot(x908.9 y503.0 w93.8 h30.1)]
                legendary title [txt=Legendary Points godot(x818.7 y340.5 w274.2 h34.3)]
                Legendary Counter [godot(x789.4 y386.3 w332.8 h42.9)]
                  Rating Text [godot(x790.5 y389.6 w330.7 h36.3)]
                    Secondary Icon [inactive godot(x790.5 y425.9 w0.0 h0.0)]
                    Main Icon [godot(x912.4 y385.2 w60.0 h45.0)]
                    Individual rating value [txt=32 godot(x972.4 y392.6 w26.9 h30.3)]
                Player Profile Ranked Trophies Gold [godot(x799.3 y440.7 w313.0 h106.9)]
                  Background [godot(x824.7 y441.2 w281.4 h106.9)]
                  Icon [sprite=WF_UI_Trophy_Gold godot(x767.4 y437.7 w113.8 h113.9)]
                  Victories number [txt=0 godot(x861.9 y456.3 w219.3 h45.5)]
                  Victories text [txt=Trophies godot(x861.9 y490.3 w219.3 h50.0)]
                Player Profile Ranked Trophies Silver [godot(x799.3 y559.2 w313.0 h106.9)]
                  Background [godot(x824.7 y559.6 w281.4 h106.9)]
                  Icon [sprite=WF_UI_Trophy_Gold godot(x767.4 y556.2 w113.8 h113.8)]
                  Victories number [txt=0 godot(x861.9 y574.7 w219.3 h45.5)]
                  Victories text [txt=Trophies godot(x861.9 y608.8 w219.3 h50.0)]
                Player Profile Ranked Trophies Bronze [godot(x799.3 y677.6 w313.0 h106.9)]
                  Background [godot(x824.7 y678.1 w281.4 h106.8)]
                  Icon [sprite=WF_UI_Trophy_Gold godot(x767.4 y674.6 w113.8 h113.8)]
                  Victories number [txt=0 godot(x861.9 y693.1 w219.3 h45.6)]
                  Victories text [txt=Trophies godot(x861.9 y727.2 w219.3 h50.0)]
          Events [godot(x1047.9 y327.7 w682.2 h529.5)]
            Warlord  Mastery Container [godot(x1175.1 y327.7 w555.0 h175.0)]
              Player Profile Container Base [godot(x1175.1 y327.7 w555.0 h175.0)]
              Title [txt=Highest Warlod Mastery godot(x1195.1 y340.8 w280.4 h60.9)]
              Badge [godot(x1397.1 y94.4 w440.0 h440.0)]
              ArmyName [txt=Ultramarines godot(x1195.1 y401.7 w289.5 h45.5)]
              Level [txt=Level: 0 godot(x1195.1 y444.1 w312.3 h32.0)]
            Forge Profile Container [godot(x1175.1 y507.7 w555.0 h175.0)]
              Player Profile Container Base [godot(x1175.1 y507.7 w555.0 h175.0)]
              Title [txt=Current campaign godot(x1194.4 y509.5 w483.0 h60.0)]
              Badge [godot(x1198.6 y560.7 w123.1 h104.3)]
              ArmyName [txt=Ultramarines godot(x1330.9 y565.6 w240.4 h61.6)]
              Level [txt=Level: 0 godot(x1330.9 y624.1 w312.2 h32.0)]
            Campaign Profile Container [godot(x1175.1 y687.7 w555.0 h175.0)]
              Player Profile Container Base [godot(x1175.1 y687.7 w555.0 h175.0)]
              Title [txt=Current campaign godot(x1194.4 y689.5 w483.0 h60.0)]
              Badge [godot(x1198.6 y740.7 w123.1 h104.3)]
              ArmyName [txt=Ultramarines godot(x1330.9 y745.6 w240.4 h61.6)]
              Level [txt=Level: 0 godot(x1330.9 y804.1 w312.2 h32.0)]
          ChooseNameWindow [inactive godot(x-0.1 y0.0 w1920.2 h1080.0)]
            Dark Background [godot(x-620.6 y-213.7 w3161.2 h1777.4)]
            Generic Popup Background [godot(x519.5 y395.0 w881.0 h301.0)]
              Mask [godot(x529.9 y404.4 w860.7 h281.8)]
                Background fill [sprite=40k_popup_texture godot(x529.9 y404.4 w860.7 h281.8)]
            Choose Name Input Field [godot(x540.1 y496.0 w836.2 h60.0)]
              Text Area [godot(x550.1 y503.0 w816.2 h47.0)]
                Placeholder [godot(x550.1 y503.0 w816.2 h47.0)]
                Text [txt=​ godot(x550.1 y503.0 w816.2 h47.0)]
            MessageText [txt=Choose your player name godot(x540.1 y426.9 w836.2 h74.2)]
            Change Name Button [godot(x822.8 y578.2 w274.4 h67.6)]
              Generic UI Button [godot(x822.8 y578.2 w274.4 h67.6)]
                Button Text [txt=Free godot(x835.8 y587.8 w248.4 h48.4)]
                Price Display [inactive godot(x833.2 y586.8 w251.4 h51.4)]
                  icon [godot(x881.9 y581.6 w61.8 h61.8)]
                  text [txt=300,00 godot(x943.7 y586.8 w92.2 h51.4)]
            Generic Close Button Green [godot(x1358.3 y362.5 w75.0 h75.0)]
              Icon [godot(x1367.6 y372.8 w56.4 h54.4)]
        Avatar Tab [inactive godot(x318.4 y118.9 w1428.6 h843.1)]
          Selected Item Panel [godot(x318.4 y292.0 w268.9 h466.9)]
            Avatar Menu Item [godot(x318.4 y360.2 w267.1 h273.5)]
              Raycast Target [godot(x362.5 y380.6 w178.9 h214.4)]
              Image Container [godot(x318.4 y360.2 w267.1 h213.5)]
                Highlight [inactive godot(x196.7 y258.7 w513.8 h409.3)]
                Border [godot(x285.0 y354.8 w333.8 h267.0)]
                Image [godot(x184.8 y250.7 w534.2 h427.1)]
              Avatar Name [txt=TEST NAME godot(x303.4 y253.1 w297.1 h67.9)]
            Select Avatar Button [godot(x343.5 y670.4 w218.7 h66.1)]
              Button Text [txt=Selecionar godot(x354.3 y677.9 w196.4 h51.1)]
            Toggle borde [godot(x343.5 y771.4 w218.7 h66.1)]
              Button Text [txt=Toggle Border godot(x354.3 y778.9 w196.4 h51.1)]
          Item Display Panel [godot(x632.8 y210.7 w1068.7 h657.9)]
            Select Item [txt=Select your avatar godot(x654.2 y147.5 w512.4 h63.2)]
            Background [godot(x632.8 y210.7 w1068.7 h657.9)]
            Scroll Rect [godot(x654.2 y210.7 w1025.9 h644.8)]
              Item Drawer [godot(x654.2 y210.7 w1044.6 h220.0)]
                Avatar Item Small_Ref [godot(x667.2 y250.7 w180.0 h180.0)]
                  Raycast Target [godot(x667.7 y224.4 w178.9 h214.4)]
                  Image Container [godot(x667.2 y250.7 w180.0 h142.6)]
                    Highlight [godot(x584.7 y182.1 w348.3 h274.6)]
                    Border [godot(x644.7 y247.1 w225.0 h178.3)]
                    Image [godot(x577.2 y176.7 w360.0 h285.2)]
                  Avatar Name [inactive txt=Avatar name godot(x667.2 y430.7 w180.0 h41.3)]
        Title Tab [godot(x318.4 y118.9 w1428.6 h843.1)]
          Selected Item Panel [godot(x318.4 y292.0 w268.9 h466.9)]
            Avatar Name [txt=Warrior of the Raging Winds godot(x322.5 y516.4 w264.8 h115.1)]
            Select Avatar Button [godot(x343.5 y670.4 w218.7 h66.1)]
              Button Text [txt=Selecionar godot(x354.3 y676.9 w196.4 h53.1)]
            Toggle borde [inactive godot(x343.5 y771.4 w218.7 h66.1)]
              Button Text [txt=Toggle Border godot(x354.3 y778.9 w196.4 h51.1)]
            Image [godot(x344.3 y295.2 w221.2 h221.2)]
          Item Display Panel [godot(x632.8 y210.7 w1068.7 h657.9)]
            Select Item [txt=Select your title godot(x654.2 y147.5 w512.4 h63.2)]
            Background [godot(x632.8 y210.7 w1068.7 h657.9)]
            Scroll Rect [godot(x654.2 y210.7 w1025.9 h644.8)]
              Item Drawer [godot(x654.2 y210.7 w1044.6 h0.0)]
        Battle Log Tab [inactive godot(x351.0 y118.9 w1396.0 h843.1)]
          Matches [godot(x326.0 y162.8 w1446.0 h741.7)]
            Viewport [godot(x326.0 y162.8 w1446.0 h724.7)]
              Content [godot(x326.0 y162.8 w1446.0 h203.2)]
                Match Log [godot(x326.0 y162.8 w1446.0 h203.2)]
                  Result [txt=Victory godot(x924.0 y178.8 w250.0 h80.0)]
                  Mode [txt=Ranked mode godot(x346.0 y187.8 w210.0 h76.6)]
                  ReplayButton [godot(x1675.5 y188.9 w65.0 h65.0)]
                    replayicon [godot(x1675.5 y188.9 w65.0 h65.0)]
                  PinButton [godot(x1597.6 y188.9 w65.0 h65.0)]
                    pinicon [godot(x1597.6 y188.9 w65.0 h65.0)]
                  Player Info [godot(x326.0 y162.8 w723.0 h203.2)]
                    Hero Name [txt=Gazkull Thraka godot(x561.0 y194.4 w340.0 h50.0)]
                    Player Name [txt=Player's name godot(x594.0 y279.4 w305.0 h50.0)]
                    Alliance Name [godot(x636.0 y316.4 w250.0 h50.0)]
                    Score [txt=Gold IV godot(x454.5 y279.4 w116.5 h50.0)]
                    Score Icon [godot(x389.5 y271.9 w65.0 h65.0)]
                    Score Icon (1) [godot(x335.7 y277.5 w53.8 h53.9)]
                    Skulls [godot(x887.5 y254.4 w100.0 h100.0)]
                    skullCounter [txt=x3 godot(x872.4 y325.8 w61.6 h28.6)]
                  Enemy Info [godot(x1049.0 y162.8 w723.0 h203.2)]
                    Hero Name [txt=Gazkull Thraka godot(x1197.0 y194.4 w360.0 h50.0)]
                    Player Name [txt=Marneus Calgar godot(x1214.0 y279.4 w276.4 h50.0)]
                    Alliance Name [godot(x1214.0 y316.4 w338.0 h50.0)]
                    Score [txt=987 (+12) godot(x1513.4 y279.4 w116.5 h50.0)]
                    Score Icon [godot(x1635.9 y271.9 w65.0 h65.0)]
                    Score Icon (1) [godot(x1700.9 y277.5 w53.8 h53.9)]
                    Skulls [godot(x1110.5 y254.4 w100.0 h100.0)]
                    skullCounter [txt=x3 godot(x1162.4 y325.8 w61.6 h28.6)]
                    GameObject [godot(x1225.5 y264.4 w343.5 h72.5)]
                  Details [godot(x326.0 y162.8 w1446.0 h203.2)]
                    Sword [godot(x999.0 y254.4 w100.0 h100.0)]
        Trophies Tab [inactive godot(x351.0 y118.9 w1396.0 h843.1)]
          bg [godot(x635.2 y213.2 w1111.8 h678.5)]
          buttons [godot(x351.0 y230.6 w284.1 h697.7)]
            Achievement Type Toggle [godot(x351.0 y230.6 w284.1 h100.0)]
              button_bg [godot(x351.0 y231.4 w284.1 h100.0)]
              Label [godot(x415.6 y260.6 w155.0 h40.0)]
                Tab Toggle Title [txt=Secret godot(x420.6 y260.6 w145.0 h40.0)]
            Achievement Type Toggle (1) [godot(x351.0 y350.6 w284.1 h100.0)]
              button_bg [godot(x351.0 y351.4 w284.1 h100.0)]
              Label [godot(x415.6 y380.6 w155.0 h40.0)]
                Tab Toggle Title [txt=Secret godot(x420.6 y380.6 w145.0 h40.0)]
            Achievement Type Toggle (4) [godot(x351.0 y470.6 w284.1 h100.0)]
              button_bg [godot(x351.0 y471.4 w284.1 h100.0)]
              Label [godot(x415.6 y500.6 w155.0 h40.0)]
                Tab Toggle Title [txt=Secret godot(x420.6 y500.6 w145.0 h40.0)]
            Achievement Type Toggle (2) [godot(x351.0 y590.6 w284.1 h100.0)]
              button_bg [godot(x351.0 y591.4 w284.1 h100.0)]
              Label [godot(x415.6 y620.6 w155.0 h40.0)]
                Tab Toggle Title [txt=Secret godot(x420.6 y620.6 w145.0 h40.0)]
            Achievement Type Toggle (3) [godot(x351.0 y710.6 w284.1 h100.0)]
              button_bg [godot(x351.0 y711.4 w284.1 h100.0)]
              Label [godot(x415.6 y740.6 w155.0 h40.0)]
                Tab Toggle Title [txt=Secret godot(x420.6 y740.6 w145.0 h40.0)]
          Scroll [godot(x635.1 y213.2 w1111.9 h678.5)]
            Viewport [godot(x635.1 y216.1 w1111.9 h675.6)]
              ContainerHolder [godot(x635.1 y200.3 w1111.9 h1014.0)]
                Achievement Container [godot(x666.1 y232.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x818.1 y253.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x818.1 y285.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1068.8 y334.3 w108.2 h29.5)]
                    rewardIcon [godot(x1040.2 y329.5 w28.6 h39.1)]
                  Progress [godot(x818.1 y334.3 w220.6 h29.5)]
                    Slider [godot(x818.1 y326.1 w220.6 h43.6)]
                      Background [godot(x818.1 y334.8 w220.6 h26.2)]
                        Fill Area [godot(x818.1 y336.8 w220.6 h22.2)]
                          Fill [godot(x818.1 y336.8 w220.6 h22.2)]
                            end [godot(x1015.0 y333.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x862.2 y339.2 w132.4 h21.8)]
                      Outline [godot(x818.1 y334.8 w220.6 h26.2)]
                  Image [godot(x681.1 y242.3 w130.0 h130.0)]
                Achievement Container (1) [godot(x1196.1 y232.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x1348.1 y253.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x1348.1 y285.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1598.8 y334.3 w108.2 h29.5)]
                    rewardIcon [godot(x1570.2 y329.5 w28.6 h39.1)]
                  Progress [godot(x1348.1 y334.3 w220.6 h29.5)]
                    Slider [godot(x1348.1 y326.1 w220.6 h43.6)]
                      Background [godot(x1348.1 y334.8 w220.6 h26.2)]
                        Fill Area [godot(x1348.1 y336.8 w220.6 h22.2)]
                          Fill [godot(x1348.1 y336.8 w220.6 h22.2)]
                            end [godot(x1545.0 y333.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x1392.2 y339.2 w132.4 h21.8)]
                      Outline [godot(x1348.1 y334.8 w220.6 h26.2)]
                  Image [godot(x1211.1 y242.3 w130.0 h130.0)]
                Achievement Container (2) [godot(x666.1 y392.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x818.1 y413.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x818.1 y445.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1068.8 y494.3 w108.2 h29.5)]
                    rewardIcon [godot(x1040.2 y489.5 w28.6 h39.1)]
                  Progress [godot(x818.1 y494.3 w220.6 h29.5)]
                    Slider [godot(x818.1 y486.1 w220.6 h43.6)]
                      Background [godot(x818.1 y494.8 w220.6 h26.2)]
                        Fill Area [godot(x818.1 y496.8 w220.6 h22.2)]
                          Fill [godot(x818.1 y496.8 w220.6 h22.2)]
                            end [godot(x1015.0 y493.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x862.2 y499.2 w132.4 h21.8)]
                      Outline [godot(x818.1 y494.8 w220.6 h26.2)]
                  Image [godot(x681.1 y402.3 w130.0 h130.0)]
                Achievement Container (3) [godot(x1196.1 y392.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x1348.1 y413.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x1348.1 y445.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1598.8 y494.3 w108.2 h29.5)]
                    rewardIcon [godot(x1570.2 y489.5 w28.6 h39.1)]
                  Progress [godot(x1348.1 y494.3 w220.6 h29.5)]
                    Slider [godot(x1348.1 y486.1 w220.6 h43.6)]
                      Background [godot(x1348.1 y494.8 w220.6 h26.2)]
                        Fill Area [godot(x1348.1 y496.8 w220.6 h22.2)]
                          Fill [godot(x1348.1 y496.8 w220.6 h22.2)]
                            end [godot(x1545.0 y493.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x1392.2 y499.2 w132.4 h21.8)]
                      Outline [godot(x1348.1 y494.8 w220.6 h26.2)]
                  Image [godot(x1211.1 y402.3 w130.0 h130.0)]
                Achievement Container (4) [godot(x666.1 y552.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x818.1 y573.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x818.1 y605.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1068.8 y654.3 w108.2 h29.5)]
                    rewardIcon [godot(x1040.2 y649.5 w28.6 h39.1)]
                  Progress [godot(x818.1 y654.3 w220.6 h29.5)]
                    Slider [godot(x818.1 y646.1 w220.6 h43.6)]
                      Background [godot(x818.1 y654.8 w220.6 h26.2)]
                        Fill Area [godot(x818.1 y656.8 w220.6 h22.2)]
                          Fill [godot(x818.1 y656.8 w220.6 h22.2)]
                            end [godot(x1015.0 y653.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x862.2 y659.2 w132.4 h21.8)]
                      Outline [godot(x818.1 y654.8 w220.6 h26.2)]
                  Image [godot(x681.1 y562.3 w130.0 h130.0)]
                Achievement Container (5) [godot(x1196.1 y552.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x1348.1 y573.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x1348.1 y605.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1598.8 y654.3 w108.2 h29.5)]
                    rewardIcon [godot(x1570.2 y649.5 w28.6 h39.1)]
                  Progress [godot(x1348.1 y654.3 w220.6 h29.5)]
                    Slider [godot(x1348.1 y646.1 w220.6 h43.6)]
                      Background [godot(x1348.1 y654.8 w220.6 h26.2)]
                        Fill Area [godot(x1348.1 y656.8 w220.6 h22.2)]
                          Fill [godot(x1348.1 y656.8 w220.6 h22.2)]
                            end [godot(x1545.0 y653.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x1392.2 y659.2 w132.4 h21.8)]
                      Outline [godot(x1348.1 y654.8 w220.6 h26.2)]
                  Image [godot(x1211.1 y562.3 w130.0 h130.0)]
                Achievement Container (6) [godot(x666.1 y712.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x818.1 y733.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x818.1 y765.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1068.8 y814.3 w108.2 h29.5)]
                    rewardIcon [godot(x1040.2 y809.5 w28.6 h39.1)]
                  Progress [godot(x818.1 y814.3 w220.6 h29.5)]
                    Slider [godot(x818.1 y806.1 w220.6 h43.6)]
                      Background [godot(x818.1 y814.8 w220.6 h26.2)]
                        Fill Area [godot(x818.1 y816.8 w220.6 h22.2)]
                          Fill [godot(x818.1 y816.8 w220.6 h22.2)]
                            end [godot(x1015.0 y813.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x862.2 y819.2 w132.4 h21.8)]
                      Outline [godot(x818.1 y814.8 w220.6 h26.2)]
                  Image [godot(x681.1 y722.3 w130.0 h130.0)]
                Achievement Container (7) [godot(x1196.1 y712.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x1348.1 y733.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x1348.1 y765.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1598.8 y814.3 w108.2 h29.5)]
                    rewardIcon [godot(x1570.2 y809.5 w28.6 h39.1)]
                  Progress [godot(x1348.1 y814.3 w220.6 h29.5)]
                    Slider [godot(x1348.1 y806.1 w220.6 h43.6)]
                      Background [godot(x1348.1 y814.8 w220.6 h26.2)]
                        Fill Area [godot(x1348.1 y816.8 w220.6 h22.2)]
                          Fill [godot(x1348.1 y816.8 w220.6 h22.2)]
                            end [godot(x1545.0 y813.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x1392.2 y819.2 w132.4 h21.8)]
                      Outline [godot(x1348.1 y814.8 w220.6 h26.2)]
                  Image [godot(x1211.1 y722.3 w130.0 h130.0)]
                Achievement Container (8) [godot(x666.1 y872.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x818.1 y893.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x818.1 y925.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1068.8 y974.3 w108.2 h29.5)]
                    rewardIcon [godot(x1040.2 y969.5 w28.6 h39.1)]
                  Progress [godot(x818.1 y974.3 w220.6 h29.5)]
                    Slider [godot(x818.1 y966.1 w220.6 h43.6)]
                      Background [godot(x818.1 y974.8 w220.6 h26.2)]
                        Fill Area [godot(x818.1 y976.8 w220.6 h22.2)]
                          Fill [godot(x818.1 y976.8 w220.6 h22.2)]
                            end [godot(x1015.0 y973.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x862.2 y979.2 w132.4 h21.8)]
                      Outline [godot(x818.1 y974.8 w220.6 h26.2)]
                  Image [godot(x681.1 y882.3 w130.0 h130.0)]
                Achievement Container (9) [godot(x1196.1 y872.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x1348.1 y893.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x1348.1 y925.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1598.8 y974.3 w108.2 h29.5)]
                    rewardIcon [godot(x1570.2 y969.5 w28.6 h39.1)]
                  Progress [godot(x1348.1 y974.3 w220.6 h29.5)]
                    Slider [godot(x1348.1 y966.1 w220.6 h43.6)]
                      Background [godot(x1348.1 y974.8 w220.6 h26.2)]
                        Fill Area [godot(x1348.1 y976.8 w220.6 h22.2)]
                          Fill [godot(x1348.1 y976.8 w220.6 h22.2)]
                            end [godot(x1545.0 y973.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x1392.2 y979.2 w132.4 h21.8)]
                      Outline [godot(x1348.1 y974.8 w220.6 h26.2)]
                  Image [godot(x1211.1 y882.3 w130.0 h130.0)]
                Achievement Container (10) [godot(x666.1 y1032.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x818.1 y1053.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x818.1 y1085.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1068.8 y1134.3 w108.2 h29.5)]
                    rewardIcon [godot(x1040.2 y1129.5 w28.6 h39.1)]
                  Progress [godot(x818.1 y1134.3 w220.6 h29.5)]
                    Slider [godot(x818.1 y1126.1 w220.6 h43.6)]
                      Background [godot(x818.1 y1134.8 w220.6 h26.2)]
                        Fill Area [godot(x818.1 y1136.8 w220.6 h22.2)]
                          Fill [godot(x818.1 y1136.8 w220.6 h22.2)]
                            end [godot(x1015.0 y1133.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x862.2 y1139.2 w132.4 h21.8)]
                      Outline [godot(x818.1 y1134.8 w220.6 h26.2)]
                  Image [godot(x681.1 y1042.3 w130.0 h130.0)]
                Achievement Container (11) [godot(x1196.1 y1032.3 w520.0 h150.0)]
                  title [txt=Victorious 1/5 godot(x1348.1 y1053.2 w358.9 h32.7)]
                  description [txt=Upgrade Ultramarines cards to tier 2 godot(x1348.1 y1085.9 w358.9 h48.4)]
                  rewards [txt=2 points godot(x1598.8 y1134.3 w108.2 h29.5)]
                    rewardIcon [godot(x1570.2 y1129.5 w28.6 h39.1)]
                  Progress [godot(x1348.1 y1134.3 w220.6 h29.5)]
                    Slider [godot(x1348.1 y1126.1 w220.6 h43.6)]
                      Background [godot(x1348.1 y1134.8 w220.6 h26.2)]
                        Fill Area [godot(x1348.1 y1136.8 w220.6 h22.2)]
                          Fill [godot(x1348.1 y1136.8 w220.6 h22.2)]
                            end [godot(x1545.0 y1133.0 w29.4 h31.8)]
                      counter [txt=100/200 godot(x1392.2 y1139.2 w132.4 h21.8)]
                      Outline [godot(x1348.1 y1134.8 w220.6 h26.2)]
                  Image [godot(x1211.1 y1042.3 w130.0 h130.0)]
          Counter [godot(x1568.9 y161.1 w135.1 h41.1)]
            EverguildTextMeshPro [txt=300 godot(x1580.5 y165.1 w111.8 h33.1)]
            Image [godot(x1521.2 y145.0 w65.3 h79.1)]
        Ranking Tab [inactive godot(x351.0 y118.9 w1396.0 h843.1)]
          Profile Player Info [godot(x351.0 y168.2 w836.0 h152.3)]
            Avatar Item Small [godot(x351.0 y168.2 w159.2 h152.3)]
              Raycast Target [godot(x341.2 y128.0 w178.9 h214.4)]
              Image Container [godot(x351.0 y168.2 w159.2 h115.0)]
                Highlight [godot(x277.9 y112.0 w308.7 h222.1)]
                Border [godot(x331.1 y165.3 w199.0 h143.8)]
                Image [godot(x271.5 y108.0 w318.3 h230.0)]
              Avatar Name [inactive txt=Avatar name godot(x351.0 y320.5 w159.2 h41.4)]
            Info Section with Alliance [inactive godot(x510.2 y168.2 w895.7 h152.3)]
              Name and Title Holder [godot(x510.2 y168.2 w864.3 h49.8)]
                Edit Name Button [inactive godot(x536.7 y193.1 w0.0 h0.0)]
                  Button Outline [godot(x536.7 y193.1 w0.0 h0.0)]
                  Icon [godot(x536.7 y193.1 w0.0 h0.0)]
                Player Name [txt=Player Name godot(x510.2 y168.2 w241.7 h49.8)]
                Player Title [txt=Player Title godot(x756.9 y168.2 w617.6 h49.8)]
              Alliance Info [godot(x510.2 y220.5 w878.6 h66.0)]
                Alliance Name [txt=Alliance Name godot(x510.2 y212.1 w878.6 h39.0)]
                Alliance Rating Display [godot(x510.2 y251.1 w263.9 h35.4)]
                  Secondary Icon [inactive godot(x510.2 y251.1 w44.4 h59.1)]
                  Main Icon [godot(x510.2 y246.3 w60.0 h45.0)]
                  Individual rating value [txt=------ godot(x570.2 y251.1 w203.9 h35.4)]
            Info Section without Alliance [godot(x510.2 y168.2 w895.7 h152.3)]
              Name and Title Holder [godot(x510.2 y168.2 w864.3 h49.8)]
                NameHolder [godot(x510.2 y168.2 w616.9 h49.8)]
                  Edit Name Button [inactive godot(x536.7 y193.1 w0.0 h0.0)]
                    Button Outline [godot(x536.7 y193.1 w0.0 h0.0)]
                    Icon [godot(x536.7 y193.1 w0.0 h0.0)]
                  Player Name [txt=Player Name godot(x510.2 y169.5 w242.4 h47.2)]
                Player Title [txt=Warrior of the raging winds godot(x510.2 y218.0 w616.9 h49.8)]
            Player Level [godot(x453.1 y259.2 w53.2 h53.1)]
              Player Level Text [txt=- godot(x460.0 y266.1 w39.4 h39.4)]
          Top4 [godot(x351.0 y334.0 w836.0 h553.0)]
            bg [godot(x351.0 y334.0 w836.0 h553.0)]
            content [godot(x367.8 y345.0 w802.5 h530.9)]
              left-side [godot(x374.4 y345.0 w210.0 h530.9)]
                #1 FactionScoreBig [godot(x384.4 y355.0 w190.0 h230.5)]
                  icon [godot(x397.4 y363.5 w164.0 h145.8)]
                  Alliance Rating Display [godot(x397.4 y509.3 w164.0 h41.0)]
                    Secondary Icon [inactive godot(x397.4 y509.3 w44.4 h59.1)]
                    Main Icon [godot(x425.8 y509.3 w40.0 h41.0)]
                    Individual rating value [txt=3000 godot(x465.8 y509.3 w67.1 h41.0)]
                  MaxRating [godot(x397.4 y550.3 w164.0 h26.7)]
                    Secondary Icon [inactive godot(x397.4 y550.3 w44.4 h59.1)]
                    Main Icon [godot(x425.8 y550.3 w40.0 h26.7)]
                    Individual rating value [txt=3000 godot(x465.8 y550.3 w67.1 h26.7)]
                #2 FactionScoreBig [godot(x384.4 y635.5 w190.0 h230.4)]
                  icon [godot(x397.4 y643.9 w164.0 h145.8)]
                  Alliance Rating Display [godot(x397.4 y789.7 w164.0 h41.0)]
                    Secondary Icon [inactive godot(x397.4 y789.7 w44.4 h59.2)]
                    Main Icon [godot(x425.8 y789.7 w40.0 h41.0)]
                    Individual rating value [txt=3000 godot(x465.8 y789.7 w67.1 h41.0)]
                  MaxRating [godot(x397.4 y830.7 w164.0 h26.8)]
                    Secondary Icon [inactive godot(x397.4 y830.7 w44.4 h59.2)]
                    Main Icon [godot(x425.8 y830.7 w40.0 h26.8)]
                    Individual rating value [txt=3000 godot(x465.8 y830.7 w67.1 h26.8)]
              center [godot(x584.4 y345.0 w369.3 h530.9)]
                DivisionText [txt=Global Rating godot(x584.4 y355.0 w369.3 h66.7)]
                DivisionImage [godot(x547.4 y383.3 w443.2 h460.7)]
                  RankImage [godot(x724.7 y521.5 w88.6 h46.0)]
                footer [godot(x584.4 y805.6 w369.3 h60.3)]
                  MainRating [godot(x591.3 y805.6 w355.4 h60.3)]
                    Global Rating [godot(x591.3 y807.1 w355.4 h57.3)]
                      Secondary Icon [inactive godot(x591.3 y864.4 w0.0 h0.0)]
                      Main Icon [godot(x722.9 y807.1 w58.6 h57.3)]
                      Individual rating value [txt=32 godot(x781.5 y816.8 w33.6 h37.9)]
              right-side [godot(x953.7 y345.0 w210.0 h530.9)]
                #3 FactionScoreBig [godot(x963.7 y355.0 w190.0 h230.5)]
                  icon [godot(x976.7 y363.5 w164.0 h145.8)]
                  Alliance Rating Display [godot(x976.7 y509.3 w164.0 h41.0)]
                    Secondary Icon [inactive godot(x976.7 y509.3 w44.4 h59.1)]
                    Main Icon [godot(x1008.5 y509.3 w40.0 h41.0)]
                    Individual rating value [txt=------ godot(x1048.5 y509.3 w60.3 h41.0)]
                  MaxRating [godot(x976.7 y550.3 w164.0 h26.7)]
                    Secondary Icon [inactive godot(x976.7 y550.3 w44.4 h59.1)]
                    Main Icon [godot(x1005.1 y550.3 w40.0 h26.7)]
                    Individual rating value [txt=3000 godot(x1045.1 y550.3 w67.1 h26.7)]
                #4 FactionScoreBig [godot(x963.7 y635.5 w190.0 h230.4)]
                  icon [godot(x976.7 y643.9 w164.0 h145.8)]
                  Alliance Rating Display [godot(x976.7 y789.7 w164.0 h41.0)]
                    Secondary Icon [inactive godot(x976.7 y789.7 w44.4 h59.2)]
                    Main Icon [godot(x1005.1 y789.7 w40.0 h41.0)]
                    Individual rating value [txt=3000 godot(x1045.1 y789.7 w67.1 h41.0)]
                  MaxRating [godot(x976.7 y830.7 w164.0 h26.8)]
                    Secondary Icon [inactive godot(x976.7 y830.7 w44.4 h59.2)]
                    Main Icon [godot(x1005.1 y830.7 w40.0 h26.8)]
                    Individual rating value [txt=3000 godot(x1045.1 y830.7 w67.1 h26.8)]
          AllFactions [godot(x1302.8 y264.8 w444.2 h622.2)]
            Faction Ranking Points [txt=Faction Rating godot(x1302.8 y200.1 w369.3 h60.0)]
            info [godot(x1686.9 y205.9 w51.0 h48.5)]
            bg [godot(x1302.8 y264.8 w444.2 h622.2)]
            scroll rect [godot(x1305.3 y288.6 w441.7 h575.8)]
              viewport [godot(x1305.3 y288.6 w441.7 h575.8)]
                content [godot(x1305.3 y288.6 w430.3 h470.9)]
                  FactionScoreSmall [godot(x1305.3 y288.6 w438.7 h117.7)]
                    icon [godot(x1305.3 y277.8 w143.1 h128.5)]
                    Alliance Rating Display [godot(x1517.9 y300.8 w226.1 h55.9)]
                      Secondary Icon [inactive godot(x1517.9 y300.8 w22.4 h29.8)]
                      Main Icon [godot(x1517.9 y300.8 w76.5 h55.9)]
                      Individual rating value [txt=4879 godot(x1594.4 y300.8 w149.6 h55.9)]
                    Alliance Rating Display (1) [godot(x1517.9 y357.1 w226.1 h36.4)]
                      Secondary Icon [inactive godot(x1517.9 y357.1 w22.4 h29.8)]
                      Main Icon [godot(x1517.9 y357.1 w76.5 h36.4)]
                      Individual rating value [txt=5000 godot(x1594.4 y357.1 w149.6 h36.4)]
                  FactionScoreSmall (1) [godot(x1305.3 y406.3 w438.7 h117.7)]
                    icon [godot(x1305.3 y395.5 w143.1 h128.5)]
                    Alliance Rating Display [godot(x1517.9 y418.6 w226.1 h55.8)]
                      Secondary Icon [inactive godot(x1517.9 y418.6 w22.4 h29.8)]
                      Main Icon [godot(x1517.9 y418.6 w76.5 h55.8)]
                      Individual rating value [txt=4879 godot(x1594.4 y418.6 w149.6 h55.8)]
                    Alliance Rating Display (1) [godot(x1517.9 y474.8 w226.1 h36.4)]
                      Secondary Icon [inactive godot(x1517.9 y474.8 w22.4 h29.8)]
                      Main Icon [godot(x1517.9 y474.8 w76.5 h36.4)]
                      Individual rating value [txt=5000 godot(x1594.4 y474.8 w149.6 h36.4)]
                  FactionScoreSmall (2) [godot(x1305.3 y524.0 w438.7 h117.8)]
                    icon [godot(x1305.3 y513.3 w143.1 h128.5)]
                    Alliance Rating Display [godot(x1517.9 y536.3 w226.1 h55.8)]
                      Secondary Icon [inactive godot(x1517.9 y536.3 w22.4 h29.8)]
                      Main Icon [godot(x1517.9 y536.3 w76.5 h55.8)]
                      Individual rating value [txt=4879 godot(x1594.4 y536.3 w149.6 h55.8)]
                    Alliance Rating Display (1) [godot(x1517.9 y592.5 w226.1 h36.4)]
                      Secondary Icon [inactive godot(x1517.9 y592.5 w22.4 h29.8)]
                      Main Icon [godot(x1517.9 y592.5 w76.5 h36.4)]
                      Individual rating value [txt=5000 godot(x1594.4 y592.5 w149.6 h36.4)]
                  FactionScoreSmall (3) [godot(x1305.3 y641.8 w438.7 h117.7)]
                    icon [godot(x1305.3 y631.0 w143.1 h128.5)]
                    Alliance Rating Display [godot(x1517.9 y654.0 w226.1 h55.8)]
                      Secondary Icon [inactive godot(x1517.9 y654.0 w22.4 h29.8)]
                      Main Icon [godot(x1517.9 y654.0 w76.5 h55.8)]
                      Individual rating value [txt=4879 godot(x1594.4 y654.0 w149.6 h55.8)]
                    Alliance Rating Display (1) [godot(x1517.9 y710.2 w226.1 h36.4)]
                      Secondary Icon [inactive godot(x1517.9 y710.2 w22.4 h29.8)]
                      Main Icon [godot(x1517.9 y710.2 w76.5 h36.4)]
                      Individual rating value [txt=5000 godot(x1594.4 y710.2 w149.6 h36.4)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Player Profile Window | ✅ `scripts\main_menu.gd:861 # ---------------- 玩家资料 (原版 Player Profile Window, 点头像弹出) ----------------; scripts\player_profile.gd:2 #` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Menu Area | ✅ `scripts\settings.gd:3 ## 权威结构 (菜单全树.md): Menu Area [328,123] 1274x843 (40k_popup 底) / Generic Close Button [1559,92] 75x75; script` |
| Tab Buttons | ✅ `scripts\collection.gd:150 # ---- Tab Buttons (原版 [167.2,158.6 165x921.4] 左竖排 4 tab — RectTransform_-1995773233925987627) ----; scr` |
| Profile Button | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Avatar Button | ✅ `scripts\player_profile.gd:509 # 原版 Select Avatar Button / Toggle borde 218.7x66.1 @(25,378)/(25,479) (Selected Item Panel 底部)` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Title Button | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Battle Log Button | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Trophies | ✅ `scripts\player_profile.gd:38 const TEX_FEEDBACK_SCORE := "res://assets/ui/mainmenu/Feedback Scoring Button.png"  # Trophies 点数 Co;` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Ranked | ✅ `scripts\main_menu.gd:66 # 小冲突(Skirmish Ranked 1x2 带 Rating)/ 经典(Ranked 1x2 带 Rating)/ 选秀(Draft Game Mode Container 1x2); scripts\m` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Tab  Area | ⚠️ 未命中 |
| Generic Window Red Background Big | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Generic Close Button Orange | ✅ `scripts\booster_info_popup.gd:146 # 关闭按钮 (原版 Generic Close Button Orange); scripts\deck_info_popup.gd:212 # 关闭按钮 (原版 Generic Close` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Tab Content | ✅ `scripts\player_profile.gd:182 # 6 个标签内容 (场景 Tab Content x351-119 1396x843 → 内容区 x351-1747 y119-963); scripts\settings.gd:151 # 5 页` |
| Profile Tab | ⚠️ 未命中 |
| Invite to alliance | ⚠️ 未命中 |
| Button Outline | ⚠️ 未命中 |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| PlayerId | ✅ `scripts\player_profile.gd:324 # 玩家 ID (场景 PlayerId x351-913 y867-907; 左侧 copy 图标 40k_profile_icon_copy 27x39)` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| playerIdText | ⚠️ 未命中 |
| Consecutive login days | ⚠️ 未命中 |
| playerIdText | ⚠️ 未命中 |
| Player Info | ✅ `scripts\player_profile.gd:869 # 玩家侧 (Player Info 左半 x[0,700]; 锚点基准 = 父宽 700); scripts\player_profile.gd:1165 # 玩家信息 (Profile Playe` |
| Avatar Item Small | ✅ `scripts\battle.gd:1727 # Avatar Item Small x[-19,136] y[12,149] 156×137; ShowCemeteryBtn 64² x[52,116] y[136,200]; scripts\battle.` |
| Raycast Target | ⚠️ 未命中 |
| Image Container | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Avatar Name | ⚠️ 未命中 |
| Info Section with Alliance | ⚠️ 未命中 |
| Name and Title Holder | ✅ `scripts\player_profile.gd:283 # 名字 + 称号 (场景 Name and Title Holder x510-1127; Edit Name Button 53x50 在名字左缘)` |
| Edit Name Button | ✅ `scripts\player_profile.gd:283 # 名字 + 称号 (场景 Name and Title Holder x510-1127; Edit Name Button 53x50 在名字左缘)` |
| Button Outline | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Player Name | ✅ `scripts\choose_name.gd:78 _input.placeholder_text = "Enter Player Name"; scripts\main_menu.gd:685 # 消息预览文字 (原版 Message Preview: '<` |
| Player Title | ⚠️ 未命中 |
| Alliance Info | ✅ `scripts\draft.gd:582 ## Deck Info Panel (说明书 Draft Mode Deck Info Panel): Deck Info/Card List/Alliance Info 三切换` |
| Alliance Name | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Alliance Rating Display | ✅ `scripts\player_profile.gd:1227 # Alliance Rating Display 行 (rank 图标 + 40px 数字); scripts\player_profile.gd:1362 # Alliance Rating D` |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Info Section without Alliance | ⚠️ 未命中 |
| Name and Title Holder | ✅ `scripts\player_profile.gd:283 # 名字 + 称号 (场景 Name and Title Holder x510-1127; Edit Name Button 53x50 在名字左缘)` |
| NameHolder | ⚠️ 未命中 |
| Edit Name Button | ✅ `scripts\player_profile.gd:283 # 名字 + 称号 (场景 Name and Title Holder x510-1127; Edit Name Button 53x50 在名字左缘)` |
| Button Outline | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Player Name | ✅ `scripts\choose_name.gd:78 _input.placeholder_text = "Enter Player Name"; scripts\main_menu.gd:685 # 消息预览文字 (原版 Message Preview: '<` |
| Player Title | ⚠️ 未命中 |
| Player Level | ✅ `scripts\player_profile.gd:311 # 玩家等级 (场景 Player Level x453-506 y259-312); scripts\player_profile.gd:1170 # 玩家等级 (Ranking 页补 Player` |
| Player Level Text | ⚠️ 未命中 |
| Ranking | ✅ `scripts\player_profile.gd:37 const TEX_ADMIRAL := "res://assets/ui/ranked/04-Admiral.png"        # Ranking 中央段位图; scripts\player_p` |
| Current Rank | ✅ `scripts\player_profile.gd:335 # 当前段位 (场景 Current Rank x351-776 y328-858); scripts\player_profile.gd:337 _make_label(tab, "Current ` |
| LeaderboardButton | ✅ `scripts\ranked.gd:81 # 排行榜按钮 (原版 LeaderboardButton [241,73 291x53], +62 → [303,73])` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Window Red Background Small | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| RankTitleBG | ⚠️ 未命中 |
| DivisionText | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Timer Icon | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| spacing | ✅ `scripts\battle.gd:2856 var spacing := HAND_SPACING_F * HAND_W; scripts\battle.gd:2857 var total := (n - 1) * spacing` |
| DivisionImage | ✅ `scripts\ranked.gd:115 # 段位图标 (原版 DivisionImage [2,768] RankImage 78²: Roman I-V 原版贴图); scripts\ranked.gd:468 var _division_icon: T` |
| RankImage | ✅ `scripts\ranked.gd:115 # 段位图标 (原版 DivisionImage [2,768] RankImage 78²: Roman I-V 原版贴图); scripts\ranked.gd:468 var _division_icon: T` |
| footer | ✅ `scripts\deck_builder.gd:466 var footer := Control.new(); scripts\deck_builder.gd:467 footer.custom_minimum_size = Vector2(0, 70)` |
| Highest Faction Rating | ⚠️ 未命中 |
| Rating Text | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| MainRating | ⚠️ 未命中 |
| Mission Milestones Progress | ⚠️ 未命中 |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| steps | ✅ `scripts\battle.gd:2290 var steps: Array = _tutorial_data.get(stage_key, {}).get("steps", []); scripts\battle.gd:2290 var steps: Ar` |
| RankedSealStep | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2511 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:426 var csb2 := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| RankedSealStep (2) | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2511 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:426 var csb2 := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| RankedSealStep (3) | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2511 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:426 var csb2 := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| RankedSealStep (4) | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2511 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:426 var csb2 := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Global Rating | ✅ `scripts\player_profile.gd:1184 # 中央列 (584.4-953.7): 'Global Rating' 标题 + 段位图 04-Admiral + 主段位条; scripts\player_profile.gd:1185 var` |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Highest Rank | ✅ `scripts\player_profile.gd:350 # 最高段位 (场景 Highest Rank x778-1137 y328-858); scripts\player_profile.gd:352 _make_label(tab, "Highest` |
| LeaderboardButton | ✅ `scripts\ranked.gd:81 # 排行榜按钮 (原版 LeaderboardButton [241,73 291x53], +62 → [303,73])` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Window Red Background Small | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| RankTitleBG | ⚠️ 未命中 |
| DivisionText | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Timer Icon | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| DivisionImage | ✅ `scripts\ranked.gd:115 # 段位图标 (原版 DivisionImage [2,768] RankImage 78²: Roman I-V 原版贴图); scripts\ranked.gd:468 var _division_icon: T` |
| RankImage | ✅ `scripts\ranked.gd:115 # 段位图标 (原版 DivisionImage [2,768] RankImage 78²: Roman I-V 原版贴图); scripts\ranked.gd:468 var _division_icon: T` |
| footer | ✅ `scripts\deck_builder.gd:466 var footer := Control.new(); scripts\deck_builder.gd:467 footer.custom_minimum_size = Vector2(0, 70)` |
| Highest Faction Rating | ⚠️ 未命中 |
| Rating Text | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| MainRating | ⚠️ 未命中 |
| Mission Milestones Progress | ⚠️ 未命中 |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| steps | ✅ `scripts\battle.gd:2290 var steps: Array = _tutorial_data.get(stage_key, {}).get("steps", []); scripts\battle.gd:2290 var steps: Ar` |
| RankedSealStep | ⚠️ 未命中 |
| Empty | ✅ `scripts\battle.gd:2511 var sb := StyleBoxEmpty.new(); scripts\campaign.gd:426 var csb2 := StyleBoxEmpty.new()` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Global Rating | ✅ `scripts\player_profile.gd:1184 # 中央列 (584.4-953.7): 'Global Rating' 标题 + 段位图 04-Admiral + 主段位条; scripts\player_profile.gd:1185 var` |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| legendary title | ⚠️ 未命中 |
| Legendarey Counter | ⚠️ 未命中 |
| Rating Text | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| spacing | ✅ `scripts\battle.gd:2856 var spacing := HAND_SPACING_F * HAND_W; scripts\battle.gd:2857 var total := (n - 1) * spacing` |
| Legendary Display Profile | ⚠️ 未命中 |
| Generic Window Red Background Small | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| DivisionImage | ✅ `scripts\ranked.gd:115 # 段位图标 (原版 DivisionImage [2,768] RankImage 78²: Roman I-V 原版贴图); scripts\ranked.gd:468 var _division_icon: T` |
| RankImage | ✅ `scripts\ranked.gd:115 # 段位图标 (原版 DivisionImage [2,768] RankImage 78²: Roman I-V 原版贴图); scripts\ranked.gd:468 var _division_icon: T` |
| legendary title | ⚠️ 未命中 |
| Legendary Counter | ⚠️ 未命中 |
| Rating Text | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Player Profile Ranked Trophies Gold | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Victories number | ⚠️ 未命中 |
| Victories text | ⚠️ 未命中 |
| Player Profile Ranked Trophies Silver | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Victories number | ⚠️ 未命中 |
| Victories text | ⚠️ 未命中 |
| Player Profile Ranked Trophies Bronze | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Victories number | ⚠️ 未命中 |
| Victories text | ⚠️ 未命中 |
| Events | ✅ `scripts\base_event_popup.gd:11 var _desc_text := "Welcome to the single-player build of Warhammer 40K Warpforge!\n\nCollect cards,` |
| Warlord  Mastery Container | ⚠️ 未命中 |
| Player Profile Container Base | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| ArmyName | ⚠️ 未命中 |
| Level | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Forge Profile Container | ✅ `scripts\player_profile.gd:416 # 当前铸造 (Forge Profile Container x1175-508)` |
| Player Profile Container Base | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| ArmyName | ⚠️ 未命中 |
| Level | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Campaign Profile Container | ✅ `scripts\player_profile.gd:420 # 当前战役 (Campaign Profile Container x1175-688)` |
| Player Profile Container Base | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| ArmyName | ⚠️ 未命中 |
| Level | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| ChooseNameWindow | ✅ `scripts\choose_name.gd:2 ## 选名窗口 (原版 ChooseNameWindow 说明书: Choose name Window 1209x400 + 输入框 + OK); scripts\main_menu.gd:512 # 点击名` |
| Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ⚠️ 未命中 |
| Choose Name Input Field | ✅ `scripts\choose_name.gd:8 const TEX_INPUT := SPR + "40K_dropdown_bg.png"              # Choose Name Input Field 底; scripts\choose_n` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| MessageText | ✅ `scripts\choose_name.gd:61 # 提示 (原版 MessageText "Choose your player name")` |
| Change Name Button | ⚠️ 未命中 |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Generic Close Button Green | ✅ `scripts\import_deck_popup.gd:120 # 关闭 (原版 Generic Close Button Green: Window 中心 (960,620), anchor(0.5,0.5) ap(394.8,220.4) 75x75` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Avatar Tab | ⚠️ 未命中 |
| Selected Item Panel | ✅ `scripts\player_profile.gd:500 # 选中预览 (场景 Selected Item Panel x318-587 y292-759; Avatar Menu Item 267.1x273.6 @(0,68)); scripts\pla` |
| Avatar Menu Item | ✅ `scripts\player_profile.gd:500 # 选中预览 (场景 Selected Item Panel x318-587 y292-759; Avatar Menu Item 267.1x273.6 @(0,68))` |
| Raycast Target | ⚠️ 未命中 |
| Image Container | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Avatar Name | ⚠️ 未命中 |
| Select Avatar Button | ✅ `scripts\player_profile.gd:509 # 原版 Select Avatar Button / Toggle borde 218.7x66.1 @(25,378)/(25,479) (Selected Item Panel 底部)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Toggle borde | ✅ `scripts\player_profile.gd:509 # 原版 Select Avatar Button / Toggle borde 218.7x66.1 @(25,378)/(25,479) (Selected Item Panel 底部)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Item Display Panel | ✅ `scripts\player_profile.gd:513 # 头像网格区 (场景 Item Display Panel x633-1702 y211-869); scripts\player_profile.gd:715 # 称号列表 (场景 Item Di` |
| Select Item | ✅ `scripts\player_profile.gd:522 # 标题 'Select your avatar' 35px 白 (原版 Select Item @(654,148))` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Scroll Rect | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\give_feedback_popup.gd:70 # ` |
| Item Drawer | ✅ `scripts\player_profile.gd:533 # 原版 Item Drawer: GridLayoutGroup cellSize 180x180 spacing(25,50) padding(left 13, top 40)` |
| Avatar Item Small_Ref | ⚠️ 未命中 |
| Raycast Target | ⚠️ 未命中 |
| Image Container | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Avatar Name | ⚠️ 未命中 |
| Title Tab | ⚠️ 未命中 |
| Selected Item Panel | ✅ `scripts\player_profile.gd:500 # 选中预览 (场景 Selected Item Panel x318-587 y292-759; Avatar Menu Item 267.1x273.6 @(0,68)); scripts\pla` |
| Avatar Name | ⚠️ 未命中 |
| Select Avatar Button | ✅ `scripts\player_profile.gd:509 # 原版 Select Avatar Button / Toggle borde 218.7x66.1 @(25,378)/(25,479) (Selected Item Panel 底部)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Toggle borde | ✅ `scripts\player_profile.gd:509 # 原版 Select Avatar Button / Toggle borde 218.7x66.1 @(25,378)/(25,479) (Selected Item Panel 底部)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Item Display Panel | ✅ `scripts\player_profile.gd:513 # 头像网格区 (场景 Item Display Panel x633-1702 y211-869); scripts\player_profile.gd:715 # 称号列表 (场景 Item Di` |
| Select Item | ✅ `scripts\player_profile.gd:522 # 标题 'Select your avatar' 35px 白 (原版 Select Item @(654,148))` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Scroll Rect | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\give_feedback_popup.gd:70 # ` |
| Item Drawer | ✅ `scripts\player_profile.gd:533 # 原版 Item Drawer: GridLayoutGroup cellSize 180x180 spacing(25,50) padding(left 13, top 40)` |
| Battle Log Tab | ⚠️ 未命中 |
| Matches | ✅ `scripts\player_profile.gd:799 # 记录列表区 (场景 Matches x326-1772 y163-905; 原版 Viewport y[162.8,887.5])` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Match Log | ✅ `scripts\player_profile.gd:28 const TEX_BTN_YELLOW := SPR + "40k_general_bt_yellow.png"           # Match Log Replay/Pin 按钮底; scrip` |
| Result | ✅ `scripts\battle.gd:3087 panel.name = "ResultPanel"; scripts\packs.gd:197 _result_area.name = "ResultArea"` |
| Mode | ✅ `scripts\battle.gd:2247 "AttackFreeMode": "Attack an enemy unit (click your unit, choose attack type, click target)",; scripts\deck` |
| ReplayButton | ✅ `scripts\battle.gd:2048 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| replayicon | ⚠️ 未命中 |
| PinButton | ✅ `scripts\player_profile.gd:887 # 回放/置顶按钮 (原版 ReplayButton x[1303.5,1368.5] / PinButton x[1225.6,1290.6], 65x65 并排 y[26,91])` |
| pinicon | ⚠️ 未命中 |
| Player Info | ✅ `scripts\player_profile.gd:869 # 玩家侧 (Player Info 左半 x[0,700]; 锚点基准 = 父宽 700); scripts\player_profile.gd:1165 # 玩家信息 (Profile Playe` |
| Hero Name | ⚠️ 未命中 |
| Player Name | ✅ `scripts\choose_name.gd:78 _input.placeholder_text = "Enter Player Name"; scripts\main_menu.gd:685 # 消息预览文字 (原版 Message Preview: '<` |
| Alliance Name | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Score Icon | ⚠️ 未命中 |
| Score Icon (1) | ⚠️ 未命中 |
| Skulls | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| skullCounter | ⚠️ 未命中 |
| Enemy Info | ✅ `scripts\player_profile.gd:878 # 敌方侧 (Enemy Info 右半 x[700,1400], 坐标镜像; 锚点基准 = 0.5*1400=700)` |
| Hero Name | ⚠️ 未命中 |
| Player Name | ✅ `scripts\choose_name.gd:78 _input.placeholder_text = "Enter Player Name"; scripts\main_menu.gd:685 # 消息预览文字 (原版 Message Preview: '<` |
| Alliance Name | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Score Icon | ⚠️ 未命中 |
| Score Icon (1) | ⚠️ 未命中 |
| Skulls | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| skullCounter | ⚠️ 未命中 |
| GameObject | ✅ `scenes\unity_arena_battlearena1.gd:2227 n_680.name = 'GameObject'` |
| Details | ✅ `scripts\deck_info_popup.gd:4 ## 布局: 大窗口(UI_Deck_Information_Back) + 督军立绘 + Deck Details(卡组名/阵营图标/督军名); scripts\deck_info_popup.gd:` |
| Sword | ✅ `scripts\battle.gd:4319 "AstraMilitarum": "Sword Slash",` |
| Trophies Tab | ⚠️ 未命中 |
| bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\achievements.gd:198 var bg :=` |
| buttons | ✅ `scripts\collection.gd:52 _build_faction_buttons(); scripts\collection.gd:53 _build_type_buttons()` |
| Achievement Type Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Achievement Type Toggle (1) | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Achievement Type Toggle (4) | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Achievement Type Toggle (2) | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Achievement Type Toggle (3) | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
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
| Achievement Container (1) | ⚠️ 未命中 |
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
| Achievement Container (2) | ⚠️ 未命中 |
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
| Achievement Container (3) | ⚠️ 未命中 |
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
| Achievement Container (4) | ⚠️ 未命中 |
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
| Achievement Container (5) | ⚠️ 未命中 |
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

## 摘要

- 规格元素: 622
- 代码命中: 268
- ⚠️未命中: 132 (以下需人工判断)

- `Profile Button`
- `Title Button`
- `Battle Log Button`
- `Tab  Area`
- `Profile Tab`
- `Invite to alliance`
- `Button Outline`
- `playerIdText`
- `Consecutive login days`
- `playerIdText`
- `Raycast Target`
- `Image Container`
- `Avatar Name`
- `Info Section with Alliance`
- `Button Outline`
- `Player Title`
- `Secondary Icon`
- `Individual rating value`
- `Info Section without Alliance`
- `NameHolder`
- `Button Outline`
- `Player Title`
- `Player Level Text`
- `Generic Window Red Background Small`
- `RankTitleBG`
- `DivisionText`
- `Timer Icon`
- `Highest Faction Rating`
- `Rating Text`
- `Secondary Icon`
- `Individual rating value`
- `MainRating`
- `Mission Milestones Progress`
- `RankedSealStep`
- `RankedSealStep (2)`
- `RankedSealStep (3)`
- `RankedSealStep (4)`
- `Secondary Icon`
- `Individual rating value`
- `Generic Window Red Background Small`
- `RankTitleBG`
- `DivisionText`
- `Timer Icon`
- `Highest Faction Rating`
- `Rating Text`
- `Secondary Icon`
- `Individual rating value`
- `MainRating`
- `Mission Milestones Progress`
- `RankedSealStep`
- `Secondary Icon`
- `Individual rating value`
- `legendary title`
- `Legendarey Counter`
- `Rating Text`
- `Secondary Icon`
- `Individual rating value`
- `Legendary Display Profile`
- `Generic Window Red Background Small`
- `legendary title`
- `Legendary Counter`
- `Rating Text`
- `Secondary Icon`
- `Individual rating value`
- `Player Profile Ranked Trophies Gold`
- `Victories number`
- `Victories text`
- `Player Profile Ranked Trophies Silver`
- `Victories number`
- `Victories text`
- `Player Profile Ranked Trophies Bronze`
- `Victories number`
- `Victories text`
- `Warlord  Mastery Container`
- `Player Profile Container Base`
- `ArmyName`
- `Player Profile Container Base`
- `ArmyName`
- `Player Profile Container Base`
- `ArmyName`
- `Background fill`
- `Change Name Button`
- `Avatar Tab`
- `Raycast Target`
- `Image Container`
- `Avatar Name`
- `Avatar Item Small_Ref`
- `Raycast Target`
- `Image Container`
- `Avatar Name`
- `Title Tab`
- `Avatar Name`
- `Battle Log Tab`
- `replayicon`
- `pinicon`
- `Hero Name`
- `Score Icon`
- `Score Icon (1)`
- `skullCounter`
- `Hero Name`
- `Score Icon`
- `Score Icon (1)`
- `skullCounter`
- `Trophies Tab`
- `Achievement Type Toggle (1)`
- `Achievement Type Toggle (4)`
- `Achievement Type Toggle (2)`
- `Achievement Type Toggle (3)`
- `ContainerHolder`
- `rewardIcon`
- `Fill Area`
- `Outline`
- `Achievement Container (1)`
- `rewardIcon`
- `Fill Area`
- `Outline`
- `Achievement Container (2)`
- `rewardIcon`
- `Fill Area`
- `Outline`
- `Achievement Container (3)`
- `rewardIcon`
- `Fill Area`
- `Outline`
- `Achievement Container (4)`
- `rewardIcon`
- `Fill Area`
- `Outline`
- `Achievement Container (5)`
- `rewardIcon`
- `Fill Area`
- `Outline`