# UI 规格审计: Draft Mode Menu Demo

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Draft Mode Menu Demo [godot(x0.0 y0.0 w1920.0 h1080.0)]
  General Red Background [godot(x960.0 y635.3 w0.0 h-190.6)]
    Menu Dark Background [godot(x-1327.3 y-773.6 w4574.6 h2572.3)]
    Reward Background Get Reward [godot(x-0.0 y94.6 w1920.0 h890.8)]
    Noise [sprite=UI Dirt And Noise skratches godot(x-0.0 y94.6 w1920.0 h890.8)]
    Menu Vignette [godot(x-0.0 y-27.2 w1920.0 h1079.5)]
  Draft Mode Intro State [inactive godot(x0.0 y0.0 w1920.0 h1080.0)]
    Game Mode Title [txt=WELCOME TO THE DRAFT MODE! godot(x869.6 y233.3 w567.3 h45.7)]
    Event image [godot(x-102.1 y-8.4 w1072.5 h1072.5)]
    Event Title [inactive txt=Duel at Saint's Haven godot(x400.8 y430.9 w1118.4 h74.2)]
    Event Description [inactive txt=During the War of Beasts Marneus Calgar  godot(x503.4 y342.0 w913.2 h198.0)]
    Game mode instructions [txt=Select your warlord, build your deck fro godot(x869.6 y321.3 w567.3 h130.4)]
    Description 1 [txt=Try to win as many battles as possible!  godot(x869.6 y467.9 w567.3 h135.2)]
    Start Button [godot(x1033.3 y646.3 w218.5 h61.6)]
      Button Text [txt=Start godot(x1044.0 y651.5 w196.3 h51.2)]
    Event locked [txt=Locked. Win one battle to enter. godot(x863.6 y720.5 w567.5 h73.0)]
  Draft Mode Pay State [inactive godot(x0.0 y0.0 w1920.0 h1080.0)]
    Event image [godot(x-102.1 y-8.4 w1072.5 h1072.5)]
    Scale menu [godot(x272.0 y-34.0 w1920.0 h1082.0)]
      ButtonsLayout [godot(x958.4 y653.8 w567.2 h168.4)]
        Free Button [godot(x967.9 y707.2 w170.0 h61.6)]
          Button Text [txt=Free godot(x976.9 y718.3 w151.4 h39.4)]
          FreeTimeText [txt=Available in godot(x967.9 y778.0 w170.0 h70.0)]
        Premium Button [godot(x1157.0 y707.2 w170.0 h61.6)]
          layout [godot(x1167.2 y707.2 w149.0 h61.6)]
            icon [godot(x1173.0 y718.0 w60.0 h40.0)]
            text [txt=0 godot(x1244.8 y718.0 w65.5 h40.0)]
          PremiumText [txt=Premium Rewards! godot(x1157.0 y778.0 w170.0 h70.0)]
        Premium Ten Button [godot(x1346.1 y707.2 w170.0 h61.6)]
          layout [godot(x1356.3 y707.2 w149.0 h61.6)]
            icon [godot(x1362.1 y718.0 w60.0 h40.0)]
            text [txt=0 godot(x1433.9 y718.0 w65.5 h40.0)]
          Premium10xText [txt=10x Premium Rewards! godot(x1346.1 y778.0 w170.0 h70.0)]
      Game Mode Title [txt=WELCOME TO THE DRAFT MODE! godot(x958.4 y275.8 w567.2 h45.7)]
      Game mode instructions [txt=Select your warlord, build your deck fro godot(x967.0 y380.1 w550.0 h130.4)]
      Description 1 [txt=Try to win as many battles as possible!  godot(x967.0 y526.7 w550.0 h135.2)]
      Timer [godot(x964.9 y322.4 w554.2 h43.6)]
        Timer Icon [godot(x1123.0 y330.2 w33.0 h33.0)]
        Timer [txt=Ends in: 23d 5h godot(x1161.9 y318.7 w199.1 h56.0)]
  Draft Mode Select Warlord State [inactive godot(x0.0 y0.0 w1920.0 h1080.0)]
    Title [txt=Select Warlord godot(x53.6 y148.6 w1812.8 h76.8)]
    Generic Card Selector Menu [godot(x0.0 y101.9 w1920.0 h905.0)]
      Viewport [godot(x0.0 y101.9 w1920.0 h905.0)]
        Content [godot(x703.7 y101.9 w512.6 h905.0)]
          Generic Select Card Container [godot(x658.1 y177.3 w504.0 h754.2)]
            Content [godot(x658.1 y177.3 w504.0 h754.2)]
              CardUI [godot(x675.1 y222.5 w469.9 h622.3)]
                CreatedByText [inactive txt=Created by someone fancy godot(x679.2 y193.7 w461.8 h70.2)]
                2DCard [godot(x716.8 y225.9 w386.6 h615.4)]
                  UI Collider [godot(x735.3 y270.3 w349.6 h534.1)]
                  Front [godot(x716.8 y196.4 w386.6 h644.9)]
                    Card Highlight And Shadow [godot(x501.1 y112.2 w818.0 h818.0)]
                    CardImage [godot(x656.2 y273.1 w507.8 h507.7)]
                    CardFrame [godot(x702.7 y223.5 w414.8 h601.8)]
                  Cardback Container [inactive godot(x817.7 y441.3 w184.8 h184.7)]
                    Cardback Shadow SDF [godot(x640.3 y181.5 w539.6 h704.3)]
                    Cardback [godot(x709.3 y243.9 w401.6 h579.4)]
                Card Ready for level up [inactive godot(x745.4 y277.6 w329.4 h505.8)]
                New Card Badge [godot(x733.7 y286.5 w223.5 h72.4)]
                  Text [txt=New! godot(x733.7 y302.9 w212.7 h39.6)]
                Ban Icon [godot(x722.1 y327.6 w376.0 h412.0)]
                  Banned Text [txt=Banned godot(x759.7 y492.4 w300.8 h82.4)]
              Select Button [godot(x805.1 y831.0 w210.0 h81.7)]
                Button Text [txt=Select godot(x816.2 y847.5 w187.1 h48.7)]
          Spacing [godot(x1136.8 y504.4 w80.0 h100.0)]
    DEBUG_REROLL_BUTTON [godot(x813.5 y985.8 w213.0 h54.4)]
      Button Text [txt=REROLL godot(x824.1 y988.1 w191.1 h49.8)]
    Generic Simplified UI Button_updated [godot(x1526.5 y932.7 w339.9 h93.8)]
      Button Text [txt=Continue godot(x1541.6 y939.4 w308.6 h80.4)]
  Draft Mode Select Packs State [godot(x0.0 y0.0 w1920.0 h1080.0)]
    Warlord Image [godot(x-258.2 y-17.7 w1072.4 h1072.5)]
    Content [godot(x118.7 y156.6 w1381.6 h723.9)]
      SubTitle [txt=Choose cards to add to your deck godot(x498.1 y263.2 w974.6 h63.4)]
      Packs [godot(x754.6 y353.6 w446.9 h47.9)]
        Pack [txt=Pack godot(x754.6 y377.6 w0.0 h47.9)]
        Stage Counter [txt=1/10 godot(x754.6 y382.6 w0.0 h37.9)]
      Packs Mask [godot(x395.0 y178.3 w1077.7 h658.8)]
        Packs Container [godot(x510.5 y272.6 w945.7 h665.6)]
    Reroll [godot(x698.2 y802.7 w639.6 h128.6)]
      Reroll Text [txt=Reroll packs: godot(x686.2 y878.5 w331.8 h61.9)]
      Price Display Button 2 Variant [godot(x1033.9 y878.5 w313.6 h61.9)]
        Generic UI Button [godot(x1033.9 y878.5 w313.6 h61.9)]
          Button Text [inactive godot(x1046.9 y904.7 w287.6 h9.5)]
          Price Display [godot(x1049.9 y885.8 w279.8 h47.2)]
            icon [godot(x1015.5 y933.0 w68.8 h0.0)]
            text [txt=3000 godot(x1178.9 y885.8 w90.5 h57.3)]
  Draft Mode Ongoing State [inactive godot(x0.0 y0.0 w1920.0 h1080.0)]
    MainContent [godot(x77.1 y134.9 w1470.4 h767.3)]
      Warlord Image [godot(x-290.4 y-49.9 w1136.8 h1136.9)]
      Scaled Content [godot(x1030.7 y498.4 w106.0 h106.0)]
        Game Mode Title [txt=Draft Mode godot(x673.8 y191.5 w821.8 h63.6)]
        Timer [godot(x673.8 y245.0 w821.8 h46.3)]
          Timer Icon [godot(x958.6 y253.3 w35.0 h35.0)]
          Timer [txt=Ends in: 23d 5h godot(x999.8 y241.2 w211.0 h59.2)]
        Victories text [txt=Victories: godot(x909.2 y327.8 w231.8 h46.0)]
          Victories text Number [txt=0 godot(x1148.4 y303.4 w149.2 h94.7)]
        Win Marks [godot(x697.9 y373.8 w773.7 h335.0)]
          Background Back [godot(x722.7 y373.8 w734.0 h345.4)]
            Background [godot(x732.6 y393.1 w714.5 h306.1)]
          Stages Container [godot(x746.6 y408.8 w678.5 h274.7)]
            Stage Info UI_ref [godot(x1043.5 y503.8 w84.8 h84.8)]
              Glow [inactive godot(x1035.3 y495.7 w101.2 h100.9)]
              Completed [godot(x1042.3 y491.1 w87.1 h113.6)]
        Defeat Marks [txt=Defeats: godot(x697.9 y742.5 w127.5 h55.5)]
          Losses container [godot(x825.4 y728.1 w247.1 h84.3)]
            Losses Info UI_ref [godot(x825.4 y734.3 w71.8 h71.8)]
              Fail [godot(x827.4 y736.3 w67.8 h67.9)]
        Quote End [inactive txt="Battles like this are what I was made f godot(x489.3 y245.0 w1012.3 h60.5)]
        Glows [godot(x-57.9 y-31.1 w2238.7 h1144.8)]
          Border Glow Up [godot(x686.0 y374.5 w816.2 h78.2)]
            Glow [godot(x686.0 y350.9 w816.2 h62.7)]
          Border Glow Down [godot(x686.0 y640.1 w816.2 h78.2)]
            Glow [godot(x686.0 y679.9 w816.2 h62.7)]
        Reset Event Button [godot(x1230.7 y748.1 w186.6 h56.1)]
          Button Text [txt=Abandonar godot(x1240.5 y754.5 w166.4 h43.3)]
    Reward Info Panel [inactive godot(x1505.9 y168.3 w390.2 h712.2)]
      Reward Info [godot(x1505.9 y168.3 w390.2 h712.2)]
        Highlight Crate [sprite=Crate Border Highlight godot(x1444.5 y245.9 w513.0 h457.0)]
        Crate [godot(x1505.9 y311.9 w390.2 h325.0)]
        Collect Button [godot(x1537.6 y627.7 w326.8 h78.4)]
          Button Text [txt=Collect reward godot(x1552.2 y628.3 w296.6 h77.2)]
    Debug Win [godot(x1262.0 y218.0 w150.0 h50.0)]
      Button Text [txt=Change Deck godot(x1270.3 y225.7 w132.9 h34.6)]
    Debug Battle Button Button [godot(x738.2 y1007.1 w577.6 h49.8)]
      CircleButton [godot(x1211.4 y1000.0 w-64.7 h64.0)]
      Text [txt=Battle! godot(x862.0 y1007.1 w263.8 h49.8)]
    To Battle Button [godot(x1455.7 y927.7 w440.4 h120.6)]
      Button Text [txt=Battle! godot(x1471.2 y934.7 w408.8 h106.5)]
  Draft Mode Deck Info Panel [godot(x1504.9 y204.4 w390.2 h712.1)]
    Buttons [godot(x1504.9 y147.7 w383.6 h63.2)]
      Deck Info Toggle [godot(x1463.9 y171.6 w82.1 h78.5)]
        button_bg [godot(x1463.9 y171.6 w82.1 h78.5)]
        Icon [godot(x1472.9 y178.9 w64.0 h64.0)]
      Card List Toggle [godot(x1463.9 y171.6 w82.1 h78.5)]
        button_bg [godot(x1463.9 y171.6 w82.1 h78.5)]
        Icon [godot(x1472.9 y178.9 w64.0 h64.0)]
      Alliance Info Toggle [godot(x1463.9 y171.6 w82.1 h78.5)]
        button_bg [godot(x1463.9 y171.6 w82.1 h78.5)]
        Icon [godot(x1469.7 y175.7 w70.4 h70.4)]
      Separator line [sprite=40k_Generic Smooth line godot(x1488.3 y212.9 w401.8 h4.6)]
    content [godot(x1498.1 y204.4 w403.8 h702.6)]
      Generic Window Red Background Small [inactive godot(x1500.0 y210.5 w400.0 h696.5)]
      Energy View panel [godot(x1502.3 y178.0 w390.1 h712.2)]
        Title [txt=Deck info godot(x1539.7 y250.2 w315.2 h50.0)]
        CardCounter [txt=Cards: 30/30 godot(x1562.7 y814.1 w269.3 h50.0)]
        Deck Information cost drawer [godot(x1607.8 y586.8 w179.1 h225.5)]
          Background [godot(x1607.8 y586.8 w179.1 h225.5)]
          Content [godot(x1570.7 y586.8 w253.3 h225.5)]
            Deck CostQuanityt Row Drawer [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
            Deck CostQuanityt Row Drawer (1) [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
            Deck CostQuanityt Row Drawer (2) [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
            Deck CostQuanityt Row Drawer (3) [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
            Deck CostQuanityt Row Drawer (4) [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
            Deck CostQuanityt Row Drawer (5) [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
            Deck CostQuanityt Row Drawer (6) [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
            Deck CostQuanityt Row Drawer (7) [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
            Deck CostQuanityt Row Drawer (8) [godot(x1444.1 y801.6 w253.2 h21.4)]
              Card Cost [txt=0 godot(x1447.9 y801.0 w29.0 h22.5)]
              Cards in deck [txt=0 godot(x1664.1 y800.9 w29.0 h22.7)]
              Slider [godot(x1485.0 y800.9 w171.4 h22.7)]
                Background [godot(x1485.0 y803.2 w171.4 h18.8)]
                Fill [godot(x1485.0 y826.3 w0.0 h-5.4)]
        Energy balance [txt=Energy Balance godot(x1535.3 y534.4 w324.1 h50.0)]
        CardUI-Warlord [inactive godot(x1601.1 y292.9 w192.5 h254.9)]
          CreatedByText [inactive txt=Created by someone fancy godot(x1602.8 y281.1 w189.1 h28.7)]
          2DCard [godot(x1618.2 y294.3 w158.3 h252.1)]
            UI Collider [godot(x1625.7 y312.4 w143.3 h218.8)]
            Front [godot(x1618.2 y282.2 w158.3 h264.2)]
              Card Highlight And Shadow [godot(x1529.8 y247.7 w335.1 h335.0)]
              CardImage [godot(x1593.4 y313.6 w207.9 h208.0)]
              CardFrame [godot(x1612.4 y293.3 w169.9 h246.5)]
            Cardback Container [inactive godot(x1659.5 y382.5 w75.7 h75.6)]
              Cardback Shadow SDF [godot(x1586.8 y276.1 w221.1 h288.4)]
              Cardback [godot(x1615.1 y301.7 w164.5 h237.3)]
          Card Ready for level up [inactive godot(x1629.9 y315.5 w134.9 h207.1)]
          New Card Badge [godot(x1625.1 y319.1 w91.6 h29.6)]
            Text [txt=Новинка! godot(x1625.1 y325.8 w87.1 h16.2)]
          Ban Icon [godot(x1620.4 y335.9 w153.9 h168.8)]
            Banned Text [txt=Запрещено godot(x1635.8 y403.4 w123.1 h33.8)]
        Separator [godot(x1539.7 y293.2 w315.2 h2.9)]
        Cardback [godot(x1614.5 y306.9 w156.7 h226.1)]
          Cardback Front [godot(x1625.9 y301.8 w156.3 h226.4)]
      Cards in deck panel [inactive godot(x1489.6 y141.3 w415.5 h785.7)]
        Scroll View [godot(x1530.0 y269.8 w330.9 h588.8)]
          Viewport [godot(x1530.0 y269.8 w330.9 h588.8)]
            Content [godot(x1530.0 y269.8 w330.9 h45.0)]
              Deck Selector Card Info button [godot(x1530.0 y269.8 w330.9 h45.0)]
                Content [godot(x1530.0 y269.8 w330.9 h45.0)]
                  Background [godot(x1548.4 y269.8 w312.5 h45.0)]
                    Rarity Gradient [godot(x1737.3 y269.8 w123.6 h44.9)]
                    Background Border [godot(x1549.5 y269.8 w311.4 h45.0)]
                    Cost Image [godot(x1532.1 y266.8 w51.0 h51.0)]
                      Cost [txt=5 godot(x1533.2 y272.5 w48.8 h39.6)]
                    banned Icon [godot(x1529.2 y263.7 w51.0 h51.0)]
                    Text fill [godot(x1589.1 y272.9 w263.7 h38.7)]
                      Card Name [txt=Card Name godot(x1589.1 y272.9 w193.6 h38.7)]
                      Count [txt=x2 godot(x1782.7 y272.9 w70.1 h38.7)]
        Warlord Name [txt=Warlord Name godot(x1536.4 y227.9 w261.8 h41.5)]
        Card counter [txt=30/30 godot(x1776.6 y227.9 w78.9 h41.5)]
        Separator [godot(x1528.1 y266.9 w338.4 h2.9)]
      Alliance Detail View [inactive godot(x1489.6 y141.3 w415.5 h785.7)]
        2Armies Progress Bar [godot(x1513.7 y227.1 w367.3 h129.5)]
          Background [godot(x1598.4 y304.1 w198.0 h15.5)]
            Fill Area [godot(x1598.4 y304.1 w198.0 h15.5)]
              Fill [godot(x1598.4 y304.1 w135.0 h15.5)]
                end [inactive godot(x1709.7 y296.9 w29.4 h31.9)]
          counter [inactive txt=100/200 godot(x1587.2 y266.0 w220.3 h64.7)]
          Outline [godot(x1513.7 y199.5 w367.3 h183.1)]
          leftArmyIcon [godot(x1524.0 y277.8 w73.7 h74.0)]
          rightArmyIcon [godot(x1798.5 y276.8 w74.0 h74.2)]
        Alliance Event Score Panel [godot(x1514.0 y369.6 w366.7 h488.9)]
          In Alliance [godot(x1514.0 y360.0 w366.7 h488.9)]
            Alliance Name [txt=Alliance Name godot(x1513.8 y360.0 w367.1 h47.8)]
            View Leaderboard Button [godot(x1580.3 y421.0 w234.1 h64.6)]
              Button Text [txt=Leaderboard godot(x1591.4 y425.8 w211.1 h55.0)]
            Alliance Event Score Info [godot(x1560.4 y498.9 w273.9 h357.8)]
              Progress Bar [godot(x1665.8 y505.7 w63.1 h344.6)]
                Fill Area [godot(x1686.1 y523.9 w22.0 h306.2)]
                  Fill [godot(x1686.1 y825.9 w22.0 h4.2)]
                Background [godot(x1681.6 y505.7 w31.5 h344.6)]
              Score Levels [godot(x1649.6 y486.6 w95.5 h309.5)]
                Alliance Score Bar Line Level 1 [godot(x1556.1 y736.2 w282.5 h57.8)]
                  Chest [godot(x1726.6 y731.4 w75.7 h67.5)]
                  Skull [godot(x1628.7 y743.4 w48.6 h43.4)]
                    Score [txt=1256 godot(x1526.9 y744.4 w96.5 h41.5)]
                Alliance Score Bar Line Level 2 [godot(x1556.1 y674.3 w282.5 h57.8)]
                  Chest [godot(x1726.6 y669.5 w75.7 h67.5)]
                  Skull [godot(x1628.7 y681.5 w48.6 h43.4)]
                    Score [txt=1256 godot(x1526.9 y682.5 w96.5 h41.5)]
                Alliance Score Bar Line Level 3 [godot(x1556.1 y612.4 w282.5 h57.8)]
                  Chest [godot(x1726.6 y607.6 w75.7 h67.5)]
                  Skull [godot(x1628.7 y619.6 w48.6 h43.5)]
                    Score [txt=1256 godot(x1526.9 y620.6 w96.5 h41.5)]
                Alliance Score Bar Line Level 4 [godot(x1556.1 y550.5 w282.5 h57.8)]
                  Chest [godot(x1726.6 y545.7 w75.7 h67.5)]
                  Skull [godot(x1628.7 y557.7 w48.6 h43.5)]
                    Score [txt=1256 godot(x1526.9 y558.7 w96.5 h41.5)]
                Alliance Score Bar Line Level 5 [godot(x1556.1 y488.6 w282.5 h57.9)]
                  Chest [godot(x1726.6 y483.8 w75.7 h67.5)]
                  Skull [godot(x1628.7 y495.8 w48.6 h43.5)]
                    Score [txt=1256 godot(x1526.9 y496.8 w96.5 h41.5)]
          No Alliance [inactive godot(x1514.0 y369.6 w366.7 h488.9)]
            Background [godot(x1531.1 y369.6 w332.5 h488.9)]
            Join Alliance text [txt=Join an alliance to gain additional rewa godot(x1514.0 y369.6 w367.1 h230.7)]
            Join Alliances Button [godot(x1580.3 y610.6 w234.1 h64.6)]
              Button Text [txt=Search godot(x1591.4 y615.4 w211.1 h55.0)]
            Leaderboard Button [godot(x1580.5 y682.3 w234.1 h64.6)]
              Button Text [txt=Leaderboard godot(x1591.6 y688.6 w211.1 h52.0)]
  Select Pack Anim Anchor (It must be out of Select Pack State) [godot(x910.0 y490.0 w100.0 h100.0)]
  Generic Multi Card Display [inactive godot(x0.0 y151.5 w1920.0 h818.0)]
    Menu Dark Background [godot(x-1327.3 y-725.7 w4574.6 h2572.4)]
    Header Text [txt=Header Text godot(x363.8 y151.5 w1192.4 h63.2)]
    Viewport [godot(x0.0 y151.5 w1920.0 h818.0)]
      Content [godot(x951.0 y151.5 w2.0 h818.0)]
        CardUI Reference [godot(x668.5 y184.6 w567.6 h751.7)]
          CreatedByText [inactive txt=Created by someone fancy godot(x673.3 y149.9 w557.9 h84.8)]
          2DCard [godot(x718.8 y188.8 w467.0 h743.3)]
            UI Collider [godot(x741.1 y242.4 w422.3 h645.1)]
            Front [godot(x718.8 y153.1 w467.0 h779.0)]
              Card Highlight And Shadow [godot(x458.2 y51.4 w988.1 h988.1)]
              CardImage [godot(x645.6 y245.8 w613.3 h613.3)]
              CardFrame [godot(x701.8 y185.9 w501.0 h726.8)]
            Cardback Container [inactive godot(x840.7 y448.9 w223.1 h223.1)]
              Cardback Shadow SDF [godot(x626.4 y135.1 w651.8 h850.7)]
              Cardback [godot(x709.7 y210.5 w485.1 h699.9)]
          Card Ready for level up [inactive godot(x753.3 y251.3 w397.9 h610.9)]
          New Card Badge [godot(x739.2 y261.9 w270.0 h87.5)]
            Text [txt=Новинка! godot(x739.2 y281.7 w256.9 h47.9)]
          Ban Icon [godot(x725.2 y311.7 w454.1 h497.6)]
            Banned Text [txt=Запрещено godot(x770.6 y510.7 w363.3 h99.5)]
    Close button [godot(x185.8 y976.8 w64.2 h63.2)]
      Text [txt=Back godot(x259.1 y976.8 w305.3 h63.2)]
  Game Mode Header With Back Button [godot(x0.0 y14.0 w550.0 h109.5)]
    Header Background [godot(x0.0 y14.0 w0.0 h115.4)]
      Window Title [txt=Game mode godot(x155.0 y30.4 w369.4 h82.6)]
      Game Mode Icon [godot(x0.0 y79.4 w100.0 h100.0)]
    Header Background (1) [godot(x-462.1 y14.0 w550.0 h115.4)]
    Header Back Button [godot(x-24.4 y16.0 w167.9 h111.3)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Draft Mode Menu Demo | ✅ `scripts\draft.gd:3 ## 选秀模式 (原版 Draft Mode Menu Demo 说明书 [0,0 1920x1080] 状态机: Intro → Pay → Select Warlord → Select Pack` |
| General Red Background | ✅ `scripts\draft.gd:123 # 背景 (原版 General Red Background: Reward Background 红底 + Noise 划痕 + 晕影)` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Reward Background Get Reward | ⚠️ 未命中 |
| Noise | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Menu Vignette | ✅ `scripts\menu_bg.gd:4 ## 还原依据: 菜单全树.md — 各二级界面根下均挂 Menu Dark Background [-1327,-746 4575x2572] + 专属背景 + Noise + Menu Vigne` |
| Draft Mode Intro State | ⚠️ 未命中 |
| Game Mode Title | ✅ `scripts\draft_expiring_popup.gd:4 ##   Game Mode Title 'The Space Marine event has finished!' +; scripts\draft_expiring_popup.gd:6` |
| Event image | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Event Title | ✅ `scripts\main_menu.gd:397 ##   TextDarkening(底条 529.9x105.9 黑 0.61 @卡内 y[740.4,846.3]) → Event Title(58.8px 白 513.7x55.7); scripts\` |
| Event Description | ⚠️ 未命中 |
| Game mode instructions | ⚠️ 未命中 |
| Description 1 | ⚠️ 未命中 |
| Start Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Event locked | ⚠️ 未命中 |
| Draft Mode Pay State | ⚠️ 未命中 |
| Event image | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Scale menu | ⚠️ 未命中 |
| ButtonsLayout | ⚠️ 未命中 |
| Free Button | ✅ `scripts\draft.gd:218 # 免费入场 (原版 Free Button; 单机全免费)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| FreeTimeText | ⚠️ 未命中 |
| Premium Button | ⚠️ 未命中 |
| layout | ✅ `scripts\battle.gd:155 var _hand_box: Control   # 手牌容器 (原版 CardsInHand 弧形布局, 位置由 _layout_hand 计算); scripts\battle.gd:1153 _layout_h` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| PremiumText | ⚠️ 未命中 |
| Premium Ten Button | ⚠️ 未命中 |
| layout | ✅ `scripts\battle.gd:155 var _hand_box: Control   # 手牌容器 (原版 CardsInHand 弧形布局, 位置由 _layout_hand 计算); scripts\battle.gd:1153 _layout_h` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Premium10xText | ⚠️ 未命中 |
| Game Mode Title | ✅ `scripts\draft_expiring_popup.gd:4 ##   Game Mode Title 'The Space Marine event has finished!' +; scripts\draft_expiring_popup.gd:6` |
| Game mode instructions | ⚠️ 未命中 |
| Description 1 | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Timer Icon | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Draft Mode Select Warlord State | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Generic Card Selector Menu | ⚠️ 未命中 |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Generic Select Card Container | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| CardUI | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
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
| Select Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Spacing | ✅ `scripts\battle.gd:1711 # MonoBehaviour_5271: m_useRotation=1 / m_betweenElementsSpacing=1.45×卡宽 / m_maxHeight=0.7×卡高 /; scripts\ba` |
| DEBUG_REROLL_BUTTON | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Simplified UI Button_updated | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Draft Mode Select Packs State | ⚠️ 未命中 |
| Warlord Image | ✅ `scripts\deck_info_popup.gd:79 # 督军立绘 (原版 Warlord Image 1108x1108, pivot(0.5,0) 原始 JSON RectTransform_8411164374367242664:; scripts` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| SubTitle | ⚠️ 未命中 |
| Packs | ✅ `scripts\booster_info_popup.gd:96 cc.text = "Packs opened since last Legendary: %d" % since; scripts\draft.gd:3 ## 选秀模式 (原版 Draft M` |
| Pack | ✅ `scripts\battle.gd:3757 _drag_line.points = PackedVector2Array([atk_pos, pos]); scripts\booster_info_popup.gd:67 title.text = "%s P` |
| Stage Counter | ⚠️ 未命中 |
| Packs Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039)` |
| Packs Container | ⚠️ 未命中 |
| Reroll | ✅ `scripts\draft.gd:247 var reroll := _mk_btn(layer, Vector2(814, 986), Vector2(213, 54), "Reroll", func():; scripts\draft.gd:250 rer` |
| Reroll Text | ⚠️ 未命中 |
| Price Display Button 2 Variant | ⚠️ 未命中 |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Draft Mode Ongoing State | ⚠️ 未命中 |
| MainContent | ⚠️ 未命中 |
| Warlord Image | ✅ `scripts\deck_info_popup.gd:79 # 督军立绘 (原版 Warlord Image 1108x1108, pivot(0.5,0) 原始 JSON RectTransform_8411164374367242664:; scripts` |
| Scaled Content | ⚠️ 未命中 |
| Game Mode Title | ✅ `scripts\draft_expiring_popup.gd:4 ##   Game Mode Title 'The Space Marine event has finished!' +; scripts\draft_expiring_popup.gd:6` |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Timer Icon | ⚠️ 未命中 |
| Timer | ✅ `scripts\battle.gd:4569 var _clock_timer: Timer = null; scripts\battle.gd:4588 _clock_timer = Timer.new()` |
| Victories text | ⚠️ 未命中 |
| Victories text Number | ⚠️ 未命中 |
| Win Marks | ✅ `scripts\draft.gd:492 # Win Marks 12 格 (说明书 Stages Container [750,415 640x259] + Stage 80²)` |
| Background Back | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Stages Container | ✅ `scripts\draft.gd:492 # Win Marks 12 格 (说明书 Stages Container [750,415 640x259] + Stage 80²)` |
| Stage Info UI_ref | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| Completed | ✅ `scripts\battle.gd:2987 # 教程胜利 → 记录完成关卡 (tutorial.gd 'Completed: N/6' 数据源; 2026-08-21); scripts\battle.gd:3245 ## tutorial.gd 读取显示 ` |
| Defeat Marks | ✅ `scripts\draft.gd:522 # Defeat Marks (说明书 [704,730] 'Defeats:' + Losses 68²)` |
| Losses container | ⚠️ 未命中 |
| Losses Info UI_ref | ⚠️ 未命中 |
| Fail | ✅ `scripts\battle.gd:3364 _log("Failed to play tactic: " + ERR_MSGS.get(err, str(err))); scripts\battle.gd:3603 _log("Failed to play ` |
| Quote End | ⚠️ 未命中 |
| Glows | ⚠️ 未命中 |
| Border Glow Up | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| Border Glow Down | ⚠️ 未命中 |
| Glow | ✅ `scripts\battle.gd:502 ## Energy Accumulation VFX On / Glow Acummulated (原版 layer5 UI 粒子, 能量区光效); scripts\battle.gd:507 ["Glow Acum` |
| Reset Event Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Reward Info Panel | ✅ `scripts\draft.gd:554 # Reward Info Panel (说明书 [1506,168 390x712]: Crate + Collect reward)` |
| Reward Info | ✅ `scripts\draft.gd:554 # Reward Info Panel (说明书 [1506,168 390x712]: Crate + Collect reward)` |
| Highlight Crate | ✅ `scripts\gacha.gd:180 # 宝箱高亮光晕 (说明书 Highlight Crate [177,163 846x754])` |
| Crate | ✅ `scripts\battle.gd:617 # 装饰扩展: 箱堆两侧 (说明书 Crates 4/Crates 18 左侧近场, 镜像右侧); scripts\battle.gd:617 # 装饰扩展: 箱堆两侧 (说明书 Crates 4/Crates 18` |
| Collect Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Debug Win | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Debug Battle Button Button | ⚠️ 未命中 |
| CircleButton | ✅ `scripts\mode_select.gd:708 # 右侧 CircleButton [1679,886 90x90] 40k_UI_bt_play — 2026-08-21 审查修正染色/字号); scripts\mode_select.gd:723 #` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| To Battle Button | ✅ `scripts\draft.gd:550 # Battle! 按钮 (说明书 To Battle Button [1456,928 440x121])` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Draft Mode Deck Info Panel | ✅ `scripts\draft.gd:582 ## Deck Info Panel (说明书 Draft Mode Deck Info Panel): Deck Info/Card List/Alliance Info 三切换; scripts\draft.gd:` |
| Buttons | ✅ `scripts\battle.gd:2048 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Deck Info Toggle | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Card List Toggle | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Alliance Info Toggle | ⚠️ 未命中 |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Separator line | ⚠️ 未命中 |
| content | ✅ `scripts\achievements.gd:138 sb.content_margin_left = 16; scripts\achievements.gd:139 sb.content_margin_right = 16` |
| Generic Window Red Background Small | ⚠️ 未命中 |
| Energy View panel | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| CardCounter | ⚠️ 未命中 |
| Deck Information cost drawer | ✅ `scripts\deck_builder.gd:460 # 费用曲线 (原版 Deck Information cost drawer [88.8,411 158.1x199.1]: 9 行 18.9 高,; scripts\deck_builder.gd:4` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Deck CostQuanityt Row Drawer | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (1) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (2) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (3) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (4) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (5) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (6) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (7) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Deck CostQuanityt Row Drawer (8) | ⚠️ 未命中 |
| Card Cost | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —` |
| Cards in deck | ✅ `scripts\deck_builder.gd:461 # Card Cost 25px + 40k_CardAmount_bar_bg/fill 金(1,0.82,0.49) + Cards in deck 25px —; scripts\draft.gd:` |
| Slider | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\battle.gd:1249 ## 内容 40k_battlelog_display_neu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Energy balance | ✅ `scripts\draft.gd:685 # Deck info 页签督军卡槽 (原版 Cardback x[1614.5,1771.2] y[306.9,533.0] 156.7×226.1) + Energy balance; scripts\draft.` |
| CardUI-Warlord | ⚠️ 未命中 |
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
| Separator | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Cardback | ✅ `scripts\battle.gd:425 if f.begins_with("Cardback_UM") and f.ends_with(".png"):; scripts\cosmetics.gd:102 b.tooltip_text = file.get` |
| Cardback Front | ⚠️ 未命中 |
| Cards in deck panel | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Deck Selector Card Info button | ✅ `scripts\deck_builder.gd:1420 ## 原版卡行 (Deck Selector Card Info button, 86px 行高): PnP 卡面缩略+渐变条+费用图标+卡名+数量; scripts\deck_builder.gd:1` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Rarity Gradient | ✅ `scripts\deck_builder.gd:1481 # 稀有度渐变条 (原版 Rarity Gradient anchor(0.606,0,1,1) 右 40% 区域稀有度着色); scripts\deck_builder.gd:1657 # 稀有度渐变` |
| Background Border | ✅ `scripts\deck_builder.gd:1471 # 卡行边框 (原版 Background Border 40k_deck_cardlist_border 11x11 m_Border=(5,5,5,5) 四边线 9-slice); scripts\` |
| Cost Image | ✅ `scripts\deck_builder.gd:1496 # 费用图标 (原版 Cost Image: Card Frame Cost Icon 左竖条 + 数字 50px); scripts\deck_builder.gd:1684 # 费用图标 (原版 C` |
| Cost | ✅ `scripts\battle.gd:435 # 实时数值层 (原版 2DCard Card Info: Cost/Health/Melee/Armour 文字实时更新 —; scripts\battle.gd:438 ["Cost", Vector3(0.28` |
| banned Icon | ✅ `scripts\deck_info_popup.gd:473 # banned Icon: 原版卡行模板 banned Icon [343,514 0x62] (行内 x+23/y-6, 62 高挂出贴底,; scripts\deck_info_popup.g` |
| Text fill | ⚠️ 未命中 |
| Card Name | ✅ `scripts\deck_builder.gd:1518 # 卡名 + 类型/稀有度 (锚定左 112 右 70, 原版 Card Name 34px); scripts\deck_builder.gd:1717 # 卡名 (原版 Card Name 34px` |
| Count | ✅ `scripts\battle.gd:4454 # 伤害数字 (原版 DamageCounter y+1.71 头顶; 解析 'dealt N damage to <目标>'); scripts\battle.gd:4492 # 攻击伤害数字 (原版 Damag` |
| Warlord Name | ✅ `scripts\deck_info_popup.gd:148 # 督军名可点 (原版 Warlord Name GO 挂 Button — 2026-08-21 审查补); scripts\draft.gd:696 # Cards in deck 视图: 列表` |
| Card counter | ✅ `scripts\draft.gd:697 # Card counter 28px / Scroll View y[269.8,858.6] — 2026-08-20 下偏 72px 修复)` |
| Separator | ✅ `scripts\collection.gd:140 # 分隔线 (原版 Separator Line [167.2,150.9 1752.8x10] 40k_main_line — RectTransform_7677886368797760811); scr` |
| Alliance Detail View | ⚠️ 未命中 |
| 2Armies Progress Bar | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| end | ✅ `scripts\achievements.gd:1 extends Control; scripts\achievements.gd:32 ["upgrade_legendary", "Legendary Forger", "Upgrade 3 Legenda` |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| Outline | ⚠️ 未命中 |
| leftArmyIcon | ⚠️ 未命中 |
| rightArmyIcon | ⚠️ 未命中 |
| Alliance Event Score Panel | ✅ `scripts\social.gd:198 # 右: Alliance Event Score Panel (原版 x[1505.6,1889.1] y[358.3,869.8] 384x512)` |
| In Alliance | ✅ `scripts\social.gd:221 # In Alliance 内容` |
| Alliance Name | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| View Leaderboard Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Alliance Event Score Info | ⚠️ 未命中 |
| Progress Bar | ✅ `scripts\quests.gd:227 ## 周常挑战条 (说明书 Weekly Mission Container: header + Mission Progress Bar 1008x23 + 4 里程碑 70x70 + Reward; script` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Score Levels | ⚠️ 未命中 |
| Alliance Score Bar Line Level 1 | ✅ `scripts\social.gd:228 # 竖进度条 (MiniBar_01) + 5 级宝箱 (说明书 Alliance Score Bar Line Level 1-5)` |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Alliance Score Bar Line Level 2 | ⚠️ 未命中 |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Alliance Score Bar Line Level 3 | ⚠️ 未命中 |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Alliance Score Bar Line Level 4 | ⚠️ 未命中 |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| Alliance Score Bar Line Level 5 | ⚠️ 未命中 |
| Chest | ✅ `scripts\gacha.gd:2 ## 宝库抽奖界面 (原版 Gacha Tab 说明书 [164,0 1756x1080]: 左 Chest panel 宝箱开箱 + 右 Rewards Panel 特殊物品池+保底进度); scripts\gacha.` |
| Skull | ✅ `scripts\achievements.gd:26 ["skull_100", "Killing Machine", "Kill 100 Skulls total", "battle", 100, 150],; scripts\achievements.gd` |
| Score | ✅ `scripts\player_profile.gd:347 _make_label(tab, "Highest Score: 0", Vector2(376, 470), Vector2(361, 40), 18, Color("b0b5bd")); scri` |
| No Alliance | ✅ `scripts\draft.gd:718 # Alliance 视图 (单机无联盟 → No Alliance 空态); scripts\social.gd:215 var no_desc := _make_label(_no_ally, "No Allian` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Join Alliance text | ⚠️ 未命中 |
| Join Alliances Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Leaderboard Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Select Pack Anim Anchor (It must be out of Select Pack State) | ⚠️ 未命中 |
| Generic Multi Card Display | ⚠️ 未命中 |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Header Text | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text)` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| CardUI Reference | ⚠️ 未命中 |
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
| Close button | ⚠️ 未命中 |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Game Mode Header With Back Button | ✅ `scripts\draft.gd:141 # Header (说明书 Game Mode Header With Back Button [0,14 550x110])` |
| Header Background | ⚠️ 未命中 |
| Window Title | ✅ `scripts\tutorial.gd:4 ## Window Title 'Game mode' + Back) + Warlod Image [411,-9 1098x1098] (督军立绘+Darkening) +` |
| Game Mode Icon | ✅ `scripts\deck_collection.gd:791 # 5) 模式图标 (右下, 原版 Game Mode Icon [171,274 84x86]; 玩家自建卡组=经典模式; 网格 0.9 倍 → offsets(153.45,229.5)); s` |
| Header Background (1) | ⚠️ 未命中 |
| Header Back Button | ✅ `scripts\tutorial.gd:64 # 返回按钮 (原版 Header Back Button 168x111)` |

## 摘要

- 规格元素: 318
- 代码命中: 206
- ⚠️未命中: 112 (以下需人工判断)

- `Reward Background Get Reward`
- `Draft Mode Intro State`
- `Event Description`
- `Game mode instructions`
- `Description 1`
- `Start Button`
- `Event locked`
- `Draft Mode Pay State`
- `Scale menu`
- `ButtonsLayout`
- `FreeTimeText`
- `Premium Button`
- `PremiumText`
- `Premium Ten Button`
- `Premium10xText`
- `Game mode instructions`
- `Description 1`
- `Timer Icon`
- `Draft Mode Select Warlord State`
- `Generic Card Selector Menu`
- `Generic Select Card Container`
- `CreatedByText`
- `UI Collider`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `Select Button`
- `DEBUG_REROLL_BUTTON`
- `Generic Simplified UI Button_updated`
- `Draft Mode Select Packs State`
- `SubTitle`
- `Stage Counter`
- `Packs Container`
- `Reroll Text`
- `Price Display Button 2 Variant`
- `Draft Mode Ongoing State`
- `MainContent`
- `Scaled Content`
- `Timer Icon`
- `Victories text`
- `Victories text Number`
- `Background Back`
- `Stage Info UI_ref`
- `Losses container`
- `Losses Info UI_ref`
- `Quote End`
- `Glows`
- `Border Glow Up`
- `Border Glow Down`
- `Reset Event Button`
- `Collect Button`
- `Debug Win`
- `Debug Battle Button Button`
- `Deck Info Toggle`
- `Card List Toggle`
- `Alliance Info Toggle`
- `Separator line`
- `Generic Window Red Background Small`
- `Energy View panel`
- `CardCounter`
- `Deck CostQuanityt Row Drawer`
- `Deck CostQuanityt Row Drawer (1)`
- `Deck CostQuanityt Row Drawer (2)`
- `Deck CostQuanityt Row Drawer (3)`
- `Deck CostQuanityt Row Drawer (4)`
- `Deck CostQuanityt Row Drawer (5)`
- `Deck CostQuanityt Row Drawer (6)`
- `Deck CostQuanityt Row Drawer (7)`
- `Deck CostQuanityt Row Drawer (8)`
- `CardUI-Warlord`
- `CreatedByText`
- `UI Collider`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `Cardback Front`
- `Cards in deck panel`
- `Text fill`
- `Alliance Detail View`
- `2Armies Progress Bar`
- `Fill Area`
- `Outline`
- `leftArmyIcon`
- `rightArmyIcon`
- `View Leaderboard Button`
- `Alliance Event Score Info`
- `Fill Area`
- `Score Levels`
- `Alliance Score Bar Line Level 2`
- `Alliance Score Bar Line Level 3`
- `Alliance Score Bar Line Level 4`
- `Alliance Score Bar Line Level 5`
- `Join Alliance text`
- `Join Alliances Button`
- `Leaderboard Button`
- `Select Pack Anim Anchor (It must be out of Select Pack State)`
- `Generic Multi Card Display`
- `CardUI Reference`
- `CreatedByText`
- `UI Collider`
- `CardFrame`
- `Cardback Container`
- `Cardback Shadow SDF`
- `Card Ready for level up`
- `Banned Text`
- `Close button`
- `Header Background`
- `Header Background (1)`