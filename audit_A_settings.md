# UI 规格审计: Main Menu Settings Window

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:48
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Main Menu Settings Window [godot(x96.0 y54.0 w1728.0 h972.0)]
  Menu Dark Background [godot(x-1098.6 y-617.6 w4117.2 h2315.2)]
  Debug Buttons [godot(x402.0 y65.7 w1116.0 h99.1)]
    Buttons container [godot(x408.8 y115.2 w1101.1 h38.6)]
      Console [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Console godot(x408.8 y153.8 w0.0 h0.0)]
      Unlink [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Unlink account godot(x408.8 y153.8 w0.0 h0.0)]
      ResetTutorial [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Reset tutorial godot(x408.8 y153.8 w0.0 h0.0)]
      AddCoins [inactive godot(x630.8 y115.2 w65.0 h38.6)]
        Button Text [txt=Add coins godot(x630.8 y128.2 w65.0 h12.6)]
      Season Check [inactive godot(x778.8 y115.2 w83.5 h38.6)]
        Button Text [txt=Season Check godot(x778.8 y126.4 w83.5 h16.2)]
      Reset GameModes [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Reset GameModes\n godot(x408.8 y153.8 w0.0 h0.0)]
      Reset Feedback [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=RESET SURVEY godot(x408.8 y153.8 w0.0 h0.0)]
      Reset Events [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Manage Events godot(x422.3 y153.8 w-27.0 h0.0)]
      AddWildcards [inactive godot(x963.8 y115.2 w102.0 h38.6)]
        Button Text [txt=Wildcards godot(x963.8 y124.6 w102.0 h19.8)]
      RateButton [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Rate godot(x408.8 y153.8 w0.0 h0.0)]
      ResetDLC [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Reset DLC godot(x408.8 y153.8 w0.0 h0.0)]
      Enviromental Debug [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Offence godot(x408.8 y153.8 w0.0 h0.0)]
      GetRewards [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Get Rewards godot(x408.8 y153.8 w0.0 h0.0)]
      Score On Leaderboard [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Score on Leaderboard godot(x408.8 y153.8 w0.0 h0.0)]
      Time Offset [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Time Offset\n godot(x408.8 y153.8 w0.0 h0.0)]
      Clean Cache [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Clean Cache godot(x408.8 y153.8 w0.0 h0.0)]
      Toggle  Debug [godot(x408.8 y153.8 w0.0 h0.0)]
        Button Text [txt=Toggle  Debug godot(x408.8 y153.8 w0.0 h0.0)]
    Debug button text [txt=Debug Buttons godot(x870.0 y74.8 w180.0 h21.6)]
    Border [godot(x402.0 y100.9 w1116.0 h2.7)]
    Border 2 [godot(x400.9 y103.6 w2.2 h30.4)]
    Border 3 [godot(x1516.9 y103.6 w2.2 h30.4)]
  old menu [inactive godot(x96.0 y54.0 w1728.0 h972.0)]
    Steam Button [godot(x483.0 y672.7 w972.0 h86.7)]
      Button Text [txt=Добавить в Список Желаемого godot(x1182.3 y689.5 w272.7 h53.1)]
      steamImage [godot(x506.8 y671.0 w69.9 h88.4)]
  Menu Area [godot(x391.3 y164.8 w1146.9 h758.8)]
    Generic Popup Background [godot(x391.3 y164.8 w1146.9 h758.8)]
      Mask [godot(x400.6 y173.3 w1128.8 h741.4)]
        Background fill [sprite=40k_popup_texture godot(x555.6 y173.3 w973.8 h741.4)]
    Popup BG [inactive godot(x391.3 y164.8 w1146.9 h758.8)]
    Generic Close Button [godot(x1499.1 y136.4 w67.5 h67.5)]
      Icon [godot(x1507.5 y145.7 w50.7 h49.0)]
    Mask Tabs buttons [godot(x400.4 y173.3 w1129.0 h741.4)]
      Tab Buttons [godot(x391.3 y164.8 w160.6 h758.8)]
        Separators [godot(x550.6 y146.8 w2.6 h794.8)]
        General [godot(x317.0 y852.6 w148.5 h141.9)]
          button_bg [godot(x317.0 y852.6 w148.5 h141.9)]
          Icon [godot(x327.7 y864.2 w127.2 h96.1)]
          Label [godot(x321.5 y948.1 w139.5 h36.0)]
            Tab Toggle Title [txt=General godot(x321.5 y948.1 w139.5 h36.0)]
        Media [godot(x317.0 y852.6 w148.5 h141.9)]
          button_bg [godot(x317.0 y853.3 w148.5 h141.9)]
          Icon [godot(x327.7 y861.6 w127.2 h96.1)]
          Label [godot(x321.5 y950.7 w139.5 h36.0)]
            Tab Toggle Title [txt=Multimedia godot(x321.5 y950.7 w139.5 h36.0)]
        Account [godot(x317.0 y852.6 w148.5 h141.9)]
          button_bg [godot(x317.0 y853.3 w148.5 h141.9)]
          Icon [godot(x327.7 y861.6 w127.2 h96.1)]
          Label [godot(x321.5 y950.7 w139.5 h36.0)]
            Tab Toggle Title [txt=Cuenta godot(x321.5 y950.7 w139.5 h36.0)]
        Graphics [godot(x317.0 y852.6 w148.5 h141.9)]
          button_bg [godot(x317.0 y853.3 w148.5 h141.9)]
          Icon [godot(x327.7 y861.6 w127.2 h96.1)]
          Label [godot(x321.5 y950.7 w139.5 h36.0)]
            Tab Toggle Title [txt=Gráficos godot(x321.5 y950.7 w139.5 h36.0)]
        Support [godot(x317.0 y852.6 w148.5 h141.9)]
          button_bg [godot(x317.0 y853.3 w148.5 h141.9)]
          Icon [godot(x327.7 y861.6 w127.2 h96.1)]
          Label [godot(x321.5 y950.7 w139.5 h36.0)]
            Tab Toggle Title [txt=Soporte godot(x321.5 y950.7 w139.5 h36.0)]
          Badge Highlight [godot(x433.4 y861.3 w31.5 h31.5)]
            OneText [godot(x433.4 y862.1 w31.5 h31.5)]
    Tab Content [godot(x551.9 y164.8 w929.0 h758.8)]
      General Tab [godot(x551.9 y164.8 w929.0 h758.8)]
        Tab Title [txt=General godot(x632.9 y224.3 w848.0 h63.0)]
        VersionText [txt=v0.15.5PREPROD-0 godot(x1200.4 y182.8 w245.7 h36.7)]
        Language Selector [godot(x632.9 y359.1 w751.3 h53.4)]
          LanguagesDropdown [godot(x632.9 y359.1 w360.6 h53.4)]
            Label [godot(x641.9 y365.4 w342.6 h41.7)]
            Arrow [godot(x971.0 y376.8 w18.0 h18.0)]
            Template [inactive godot(x632.9 y405.6 w356.1 h516.5)]
              Viewport [godot(x632.9 y405.6 w340.8 h516.5)]
                Content [godot(x632.9 y405.6 w340.8 h37.5)]
                  Item [godot(x632.9 y406.0 w340.8 h36.7)]
                    Item Background [godot(x632.9 y406.0 w340.8 h36.7)]
                    Item Checkmark [godot(x632.9 y415.4 w18.0 h18.0)]
                    Item Label [txt=Option A godot(x650.9 y407.8 w313.8 h34.0)]
              Scrollbar [godot(x971.0 y405.6 w18.0 h516.5)]
                Sliding Area [godot(x980.0 y414.6 w0.0 h498.5)]
                  Handle [godot(x971.0 y441.8 w18.0 h480.3)]
          SelectLanguageText [txt=Select Language godot(x1017.5 y359.0 w366.7 h53.5)]
        Checkboxes [godot(x632.9 y455.5 w751.3 h263.0)]
          Disable Bots [godot(x632.9 y684.4 w0.0 h68.1)]
            Toggle [godot(x632.9 y752.5 w0.0 h0.0)]
              CheckMark [godot(x632.9 y752.5 w0.0 h0.0)]
            Label [txt=Disable Bots godot(x632.9 y752.5 w0.0 h0.0)]
          Disable Notifications [godot(x632.9 y684.4 w0.0 h68.1)]
            Toggle [godot(x632.9 y752.5 w0.0 h0.0)]
              CheckMark [godot(x632.9 y752.5 w0.0 h0.0)]
            Label [txt=Disable Notifications godot(x632.9 y752.5 w0.0 h0.0)]
          Touch Input [godot(x632.9 y684.4 w0.0 h68.1)]
            Toggle [godot(x632.9 y752.5 w0.0 h0.0)]
              CheckMark [godot(x632.9 y752.5 w0.0 h0.0)]
            Label [txt=Touch input godot(x632.9 y752.5 w0.0 h0.0)]
        Bottom Buttons [godot(x632.9 y755.6 w848.0 h81.0)]
          Redeem Code [godot(x632.9 y796.1 w270.0 h81.0)]
            Button Text [txt=Redeem Code godot(x644.3 y795.6 w246.6 h81.0)]
          Close Game Button [godot(x632.9 y796.1 w270.0 h81.0)]
            Button Text [txt=Exit Game godot(x644.3 y795.6 w246.6 h81.0)]
      Media Tab [godot(x551.9 y164.8 w929.0 h758.8)]
        Tab Title [txt=Multimedia godot(x632.9 y224.3 w848.0 h63.0)]
        Audio Settings [godot(x632.9 y306.1 w615.7 h315.8)]
          Music Container [godot(x632.9 y574.6 w0.0 h94.5)]
            Music Slider [godot(x632.9 y626.0 w0.0 h11.7)]
              Background [godot(x632.9 y626.0 w0.0 h11.7)]
              Fill [godot(x632.9 y637.7 w0.0 h0.0)]
              Handle Slide Area [godot(x632.9 y626.0 w-9.0 h11.7)]
                Handle [godot(x622.6 y627.6 w42.1 h20.2)]
            Label [txt=Música godot(x632.9 y562.5 w0.0 h55.8)]
          FX Container [godot(x632.9 y574.2 w0.0 h95.4)]
            Sound effects Slider [godot(x632.9 y626.0 w0.0 h11.7)]
              Background [godot(x632.9 y626.0 w0.0 h11.7)]
              Fill [godot(x632.9 y637.7 w0.0 h0.0)]
              Handle Slide Area [godot(x632.9 y626.0 w-9.0 h11.7)]
                Handle [godot(x622.6 y627.6 w42.1 h20.2)]
            Label [txt=Efectos de Sonido godot(x632.9 y562.0 w0.0 h56.7)]
          Voiceovers Container [godot(x632.9 y574.2 w0.0 h95.4)]
            Voice Over Slider [godot(x632.9 y626.0 w0.0 h11.7)]
              Background [godot(x632.9 y626.0 w0.0 h11.7)]
              Fill [godot(x632.9 y637.7 w0.0 h0.0)]
              Handle Slide Area [godot(x632.9 y626.0 w-9.0 h11.7)]
                Handle [godot(x622.6 y627.6 w42.1 h20.2)]
            Label [txt=Narraciones godot(x632.9 y562.0 w0.0 h56.7)]
        Visual Settings [godot(x632.9 y621.9 w800.1 h268.7)]
          WindowMode Selector [godot(x257.2 y863.8 w751.3 h53.5)]
            Dropdown [godot(x257.2 y863.8 w360.6 h53.5)]
              Label [godot(x266.2 y870.1 w342.6 h41.8)]
              Arrow [godot(x595.3 y881.6 w18.0 h18.0)]
              Template [inactive godot(x257.2 y910.4 w356.1 h516.5)]
                Viewport [godot(x257.2 y910.4 w340.8 h516.5)]
                  Content [godot(x257.2 y910.4 w340.8 h37.5)]
                    Item [godot(x257.2 y910.7 w340.8 h36.8)]
                      Item Background [godot(x257.2 y910.7 w340.8 h36.8)]
                      Item Checkmark [godot(x257.2 y920.1 w18.0 h18.0)]
                      Item Label [txt=Option A godot(x275.2 y912.5 w313.8 h34.1)]
                Scrollbar [godot(x595.3 y910.4 w18.0 h516.5)]
                  Sliding Area [godot(x604.3 y919.4 w0.0 h498.5)]
                    Handle [godot(x595.3 y910.4 w18.0 h516.5)]
            Label [txt=Modo Ventana godot(x641.8 y863.8 w366.7 h53.5)]
      Account Tab [inactive godot(x551.9 y164.8 w929.0 h758.8)]
        Tab Title [txt=Account godot(x632.9 y224.3 w848.0 h63.0)]
        Player Id [inactive txt=Player ID: 325161617 godot(x1129.5 y202.9 w330.4 h35.1)]
          Player Id Text [godot(x1072.4 y194.7 w387.5 h47.4)]
          External Link Icon [sprite=Copy@3x godot(x1063.9 y190.8 w51.2 h51.3)]
        Account Form [godot(x632.9 y299.8 w828.0 h370.8)]
          EmailText [txt=E-mail godot(x632.9 y289.3 w414.0 h54.0)]
          InputEmail [godot(x632.9 y342.6 w828.0 h54.0)]
            Text Area [godot(x650.9 y355.7 w810.0 h27.9)]
              Placeholder [godot(x650.9 y355.7 w810.0 h27.9)]
              Text [txt=​ godot(x650.9 y355.7 w810.0 h27.9)]
          PasswordText [txt=Password godot(x632.9 y405.6 w414.0 h54.0)]
          InputPassword [godot(x632.9 y459.7 w828.0 h54.0)]
            Text Area [godot(x650.9 y472.7 w810.0 h27.9)]
              Placeholder [godot(x650.9 y472.7 w810.0 h27.9)]
              Text [txt=​ godot(x650.9 y472.7 w810.0 h27.9)]
          Reset Password [txt=Reset Password godot(x1046.9 y417.1 w414.0 h39.9)]
          Forgot Password [txt=Forgot Password godot(x1046.9 y417.1 w414.0 h39.9)]
          Error Message [txt=* Invalid Password godot(x632.9 y526.1 w828.0 h42.4)]
        Subscribe Newsletter [txt=Subscribe to the Newsletter? godot(x632.9 y551.7 w539.5 h69.0)]
        Social Media Links [godot(x622.4 y654.1 w573.5 h72.8)]
          Discord Button [godot(x622.4 y647.7 w114.7 h85.5)]
            Button Text [inactive godot(x633.9 y674.8 w91.3 h30.2)]
          IG Button [godot(x737.1 y656.7 w114.7 h67.5)]
            Button Text [inactive godot(x748.6 y683.8 w91.3 h12.2)]
          Facebook Button [godot(x851.8 y656.7 w114.7 h67.5)]
            Button Text [inactive godot(x863.3 y683.8 w91.3 h12.2)]
          Twitter Button [godot(x966.5 y656.7 w114.7 h67.5)]
            Button Text [inactive godot(x978.0 y683.8 w91.3 h12.2)]
          Youtube Button [godot(x1081.2 y654.5 w114.7 h72.0)]
            Button Text [inactive godot(x1092.7 y681.6 w91.3 h16.7)]
        Buttons [godot(x971.4 y675.4 w90.0 h90.0)]
          Unregistered Buttons [godot(x898.1 y544.7 w559.8 h81.0)]
            Register Button [godot(x1187.9 y544.7 w270.0 h81.0)]
              Button Text [txt=Register godot(x1197.8 y560.4 w249.9 h48.6)]
            Login Button  [inactive godot(x1178.0 y544.7 w270.0 h81.0)]
              Button Text [txt=Log in godot(x1189.4 y561.9 w246.6 h45.6)]
          Twitch Button [inactive godot(x914.4 y778.8 w267.6 h81.0)]
            Button Text [txt=Link Twitch godot(x925.8 y796.2 w244.2 h45.1)]
          Delete Button [godot(x1190.9 y779.5 w270.0 h81.0)]
            Button Text [txt=Delete account godot(x1202.3 y795.4 w246.6 h48.0)]
          Registered Buttons [godot(x632.9 y778.8 w594.0 h81.0)]
            Switch Account Button [godot(x632.9 y778.8 w270.0 h81.0)]
              Button Text [txt=Switch Account godot(x644.3 y794.8 w246.6 h48.0)]
            Logout Button [inactive godot(x929.9 y778.8 w270.0 h81.0)]
              Button Text [txt=Выйти из системы godot(x941.3 y796.0 w246.6 h45.5)]
        Login Window [inactive godot(x420.3 y292.2 w1087.7 h360.0)]
          Backgroun filler [inactive godot(x431.0 y300.8 w1065.7 h338.6)]
          Generic Popup Background [godot(x420.3 y292.2 w1087.7 h360.0)]
            Mask [godot(x429.7 y300.7 w1069.5 h342.7)]
              Background fill [sprite=40k_popup_texture godot(x429.7 y300.7 w1069.5 h342.7)]
          EmailText [txt=E-mail godot(x458.3 y331.6 w393.7 h54.0)]
          InputEmail [godot(x458.3 y384.9 w730.8 h54.0)]
            Text Area [godot(x476.3 y398.0 w712.8 h27.9)]
              Placeholder [godot(x476.3 y398.0 w712.8 h27.9)]
              Text [txt=​ godot(x476.3 y398.0 w712.8 h27.9)]
          PasswordText [txt=Password godot(x458.3 y447.9 w393.7 h54.0)]
          InputPassword [godot(x458.3 y502.0 w730.8 h54.0)]
            Text Area [godot(x476.3 y515.0 w712.8 h27.9)]
              Placeholder [godot(x476.3 y515.0 w712.8 h27.9)]
              Text [txt=​ godot(x476.3 y515.0 w712.8 h27.9)]
          Forgot Password [txt=Forgot Password godot(x795.3 y460.6 w393.8 h39.9)]
          ErrorMensajeContainer [godot(x458.3 y573.1 w730.8 h33.1)]
            Animated Loading Image [godot(x458.3 y572.6 w34.1 h34.1)]
              Cog [godot(x458.3 y572.6 w34.1 h34.1)]
            Error Message [txt=* Invalid Password godot(x503.2 y573.1 w696.7 h33.1)]
          Login Button  [godot(x1210.5 y500.5 w278.3 h54.0)]
            Button Text [txt=Log in godot(x1221.9 y503.4 w254.9 h47.1)]
          Generic Close Button Green [godot(x1469.5 y262.9 w67.5 h67.5)]
            Icon [godot(x1477.9 y272.2 w50.7 h49.0)]
      Support Tab [inactive godot(x551.9 y164.8 w929.0 h758.8)]
        Tab Title [txt=Support godot(x632.9 y224.3 w848.0 h63.0)]
        Faq Text [txt=Questions about the game? Visit the Freq godot(x632.9 y299.0 w848.0 h76.5)]
        Faq Button [godot(x632.9 y389.8 w324.0 h54.0)]
          Button Text [txt=FAQ godot(x687.9 y391.9 w256.0 h49.8)]
          External Link Icon [godot(x641.8 y402.6 w36.1 h28.4)]
        Contact Text [txt=Do you need help from us? godot(x632.9 y461.4 w848.0 h56.6)]
        Contact Button [godot(x632.9 y530.9 w324.0 h54.0)]
          Button Text [txt=Contact godot(x687.9 y533.0 w256.0 h49.8)]
          External Link Icon [godot(x641.8 y543.7 w36.1 h28.4)]
        Support Button [godot(x632.9 y389.1 w324.0 h54.0)]
          Button Text [txt=Support godot(x658.3 y388.3 w285.6 h55.6)]
        Email Text [txt=You can also contact us at support@everg godot(x632.9 y611.8 w848.0 h124.2)]
        bottom links [godot(x632.9 y776.8 w848.0 h53.1)]
          Terms of Service [godot(x632.9 y776.8 w424.0 h53.1)]
            External Link Icon [godot(x632.9 y789.2 w36.0 h28.4)]
            Terms of Service Text [txt=Terms of Service godot(x677.9 y776.8 w378.9 h53.1)]
          Privacy Policy [godot(x1056.9 y776.8 w424.0 h53.1)]
            External Link Icon [godot(x1056.9 y789.2 w36.0 h28.4)]
            Privacy Policy Button [godot(x1101.9 y776.8 w378.9 h53.1)]
              Button Text [txt=Privacy Policy godot(x1106.4 y766.4 w374.4 h72.8)]
        Faq Text Mobile [txt=Questions about the game? Check out the  godot(x632.9 y299.0 w848.0 h82.8)]
        Email Text Mobile [txt=You can also contact us at support@everg godot(x632.9 y463.7 w848.0 h124.2)]
      Graphics Tab [inactive godot(x551.9 y164.8 w929.0 h758.8)]
        Tab Title [txt=Gráficos godot(x632.9 y224.3 w848.0 h63.0)]
        Content [godot(x551.9 y294.9 w929.1 h628.7)]
          Quality  Selector [godot(x592.4 y294.9 w751.3 h53.5)]
            Quality DropDown [godot(x592.4 y294.9 w360.6 h53.5)]
              Label [godot(x601.4 y301.2 w342.6 h41.8)]
              Arrow [godot(x930.5 y312.7 w18.0 h18.0)]
              Template [inactive godot(x592.4 y341.5 w356.1 h516.5)]
                Viewport [godot(x592.4 y341.5 w340.8 h516.5)]
                  Content [godot(x592.4 y341.5 w340.8 h37.5)]
                    Item [godot(x592.4 y341.8 w340.8 h36.8)]
                      Item Background [godot(x592.4 y341.8 w340.8 h36.8)]
                      Item Checkmark [godot(x592.4 y351.2 w18.0 h18.0)]
                      Item Label [txt=Option A godot(x610.4 y343.6 w313.8 h34.1)]
                Scrollbar [godot(x930.5 y341.5 w18.0 h516.5)]
                  Sliding Area [godot(x939.5 y350.5 w0.0 h498.5)]
                    Handle [godot(x930.5 y377.7 w18.0 h480.3)]
            Quality selector text [txt=Seleccionar Calidad godot(x977.0 y294.9 w366.7 h53.5)]
          Text In Hand  Selector [godot(x592.4 y369.1 w751.3 h53.4)]
            Text in Hand DropDown [godot(x592.4 y369.1 w360.6 h53.4)]
              Label [godot(x601.4 y375.4 w342.6 h41.7)]
              Arrow [godot(x930.5 y386.8 w18.0 h18.0)]
              Template [inactive godot(x592.4 y415.6 w356.1 h516.6)]
                Viewport [godot(x592.4 y415.6 w340.8 h516.6)]
                  Content [godot(x592.4 y415.6 w340.8 h37.6)]
                    Item [godot(x592.4 y416.0 w340.8 h36.8)]
                      Item Background [godot(x592.4 y416.0 w340.8 h36.8)]
                      Item Checkmark [godot(x592.4 y425.4 w18.0 h18.0)]
                      Item Label [txt=Option A godot(x610.4 y417.8 w313.8 h34.1)]
                Scrollbar [godot(x930.5 y415.6 w18.0 h516.6)]
                  Sliding Area [godot(x939.5 y424.6 w0.0 h498.6)]
                    Handle [godot(x930.5 y451.9 w18.0 h480.3)]
            Quality selector text [txt=Texto para cartas en mano godot(x977.0 y369.1 w366.7 h53.4)]
          Scroll View [godot(x592.4 y443.2 w888.6 h469.4)]
            Viewport [godot(x603.2 y443.2 w867.0 h469.4)]
              Content [godot(x603.2 y443.2 w409.7 h270.0)]
                Small Screen Size Toggle [godot(x603.2 y443.2 w409.7 h68.1)]
                  Toggle [godot(x603.2 y443.2 w107.1 h68.1)]
                    CheckMark [godot(x603.2 y443.2 w107.1 h68.1)]
                  Label [txt=Aumentar tamaño de UI godot(x710.3 y443.2 w302.6 h68.1)]
                Auto Zoom Toggle [godot(x603.2 y515.8 w409.7 h68.1)]
                  Toggle [godot(x603.2 y515.8 w107.1 h68.1)]
                    CheckMark [godot(x603.2 y515.8 w107.1 h68.1)]
                  Label [txt=Auto zoom godot(x710.3 y515.8 w136.2 h68.1)]
                Hi FPS toggl [godot(x603.2 y588.4 w409.7 h68.1)]
                  Toggle [godot(x603.2 y588.4 w107.1 h68.1)]
                    CheckMark [godot(x603.2 y588.4 w107.1 h68.1)]
                  Label [txt=Alta tasa de refresco godot(x710.3 y588.4 w261.3 h68.1)]
                Android extra compatibility [inactive godot(x603.2 y661.0 w426.9 h68.1)]
                  Toggle [godot(x603.2 y661.0 w107.1 h68.1)]
                    CheckMark [godot(x603.2 y661.0 w107.1 h68.1)]
                  Label [txt=Compatibilidad extendida godot(x710.3 y661.0 w319.8 h68.1)]
                    Tooltip - Extended compaibility [godot(x1046.7 y661.0 w68.3 h68.1)]
                Use super sampling [godot(x603.2 y661.0 w409.7 h68.1)]
                  Toggle [godot(x603.2 y661.0 w107.1 h68.1)]
                    CheckMark [godot(x603.2 y661.0 w107.1 h68.1)]
                  Label [txt=Sobremuestreo godot(x710.3 y661.0 w194.7 h68.1)]
                Vsync [godot(x603.2 y733.6 w409.7 h68.0)]
                  Toggle [godot(x603.2 y733.6 w107.1 h68.0)]
                    CheckMark [godot(x603.2 y733.6 w107.1 h68.0)]
                  Label [txt=VSync godot(x710.3 y733.6 w82.3 h68.0)]
                FPS Limit [godot(x603.2 y806.1 w409.7 h94.5)]
                  Title [txt=Límite de FPS godot(x617.6 y793.5 w278.6 h55.8)]
                  FPS Slider [godot(x842.6 y881.9 w442.0 h11.7)]
                    Background [godot(x842.6 y881.9 w442.0 h11.7)]
                    Fill [godot(x842.6 y881.9 w0.0 h11.7)]
                    Handle Slide Area [godot(x842.6 y881.9 w433.0 h11.7)]
                      Handle [godot(x832.3 y871.8 w42.1 h31.9)]
                    30 FPS [txt=30 godot(x749.9 y830.5 w205.2 h55.8)]
                    60 FPS [txt=60 godot(x966.7 y830.5 w205.2 h55.8)]
                    Unlimited [txt=Ilimitado godot(x1179.2 y826.1 w205.2 h55.8)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Main Menu Settings Window | ✅ `scripts\main_menu.gd:948 ## 设置按钮: 打开设置窗口 (原版 Main Menu Settings Window 5 页: 常规/画质/质量/账号/支持); scripts\settings.gd:2 ## 设置界面 (原版 Mai` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Debug Buttons | ⚠️ 未命中 |
| Buttons container | ⚠️ 未命中 |
| Console | ✅ `scripts\battle.gd:717 # 装饰扩展: 坠毁坦克右后/地堡右后/控制台前场 (说明书 Crashed tank/Bunker 1/Console Front Left/Right); scripts\battle.gd:720 ["tauv` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Unlink | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| ResetTutorial | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| AddCoins | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Season Check | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Reset GameModes | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Reset Feedback | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Reset Events | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| AddWildcards | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| RateButton | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| ResetDLC | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Enviromental Debug | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GetRewards | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Score On Leaderboard | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Time Offset | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Clean Cache | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Toggle  Debug | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Debug button text | ⚠️ 未命中 |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Border 2 | ⚠️ 未命中 |
| Border 3 | ⚠️ 未命中 |
| old menu | ⚠️ 未命中 |
| Steam Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| steamImage | ⚠️ 未命中 |
| Menu Area | ✅ `scripts\settings.gd:3 ## 权威结构 (菜单全树.md): Menu Area [328,123] 1274x843 (40k_popup 底) / Generic Close Button [1559,92] 75x75; script` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ⚠️ 未命中 |
| Popup BG | ⚠️ 未命中 |
| Generic Close Button | ✅ `scripts\booster_info_popup.gd:146 # 关闭按钮 (原版 Generic Close Button Orange); scripts\deck_info_popup.gd:212 # 关闭按钮 (原版 Generic Close` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Mask Tabs buttons | ⚠️ 未命中 |
| Tab Buttons | ✅ `scripts\collection.gd:150 # ---- Tab Buttons (原版 [167.2,158.6 165x921.4] 左竖排 4 tab — RectTransform_-1995773233925987627) ----; scr` |
| Separators | ✅ `scripts\main_menu.gd:230 ##   Separators Left/Right(40k_Separator 2.8 宽, x[-2.5,0.3]&x[164,166.8] y[-0.1,1009]); scripts\main_menu` |
| General | ✅ `scripts\draft.gd:123 # 背景 (原版 General Red Background: Reward Background 红底 + Noise 划痕 + 晕影); scripts\main_menu.gd:737 # 左侧 Tab 列 (` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Media | ✅ `scripts\settings.gd:4 ## Tab Buttons [328,123] 178x843 5 键均分: General(40K_settings_button_general) / Media(40K_settings_bu; script` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Account | ✅ `scripts\choose_name.gd:98 # 底部说明 (原版 Link Accounts message 位置); scripts\player_profile.gd:952 var cats := ["All", "Battle", "Colle` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Graphics | ✅ `scripts\settings.gd:5 ## ——原版 Media 页图标文件就是 quality) / Account / Graphics / Support; scripts\settings.gd:7 ## Graphics=质量档位+手牌文字下拉` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Support | ✅ `scripts\main_menu.gd:941 ## 反馈按钮: 打开反馈问卷 (原版 Support Tab → Feedback); scripts\settings.gd:5 ## ——原版 Media 页图标文件就是 quality) / Accou` |
| button_bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\player_profile.gd:1038 # 分类按钮` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tab Toggle Title | ✅ `scripts\player_profile.gd:228 # 文字 (原版 Tab Toggle Title 35px 白, 按钮底部 y[10,50] from bottom); scripts\settings.gd:139 # 文字 (原版 Tab T` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Tab Content | ✅ `scripts\player_profile.gd:182 # 6 个标签内容 (场景 Tab Content x351-119 1396x843 → 内容区 x351-1747 y119-963); scripts\settings.gd:151 # 5 页` |
| General Tab | ⚠️ 未命中 |
| Tab Title | ⚠️ 未命中 |
| VersionText | ✅ `scripts\settings.gd:185 # 版本 (说明书 VersionText [1227,143] 273x41 → 相对内容区)` |
| Language Selector | ⚠️ 未命中 |
| LanguagesDropdown | ✅ `scripts\settings.gd:187 # 语言选择 (说明书 LanguagesDropdown [597,339] 401x59 → 相对内容区 (90,216); 标签右移对齐)` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Arrow | ✅ `scripts\where_cards_popup.gd:142 arrow.name = "Arrow"` |
| Template | ✅ `scripts\deck_info_popup.gd:572 _Toast("Template decks cannot be edited; create your own"); scripts\deck_info_popup.gd:582 _Toast("` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Item | ✅ `scripts\battle.gd:1727 # Avatar Item Small x[-19,136] y[12,149] 156×137; ShowCemeteryBtn 64² x[52,116] y[136,200]; scripts\battle.` |
| Item Background | ⚠️ 未命中 |
| Item Checkmark | ⚠️ 未命中 |
| Item Label | ⚠️ 未命中 |
| Scrollbar | ✅ `scripts\collection.gd:637 # 原版 m_VerticalScrollbar=0 无滚动条 — 2026-08-21 审查: 去除金色滚动条, 仅透明面板` |
| Sliding Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| SelectLanguageText | ⚠️ 未命中 |
| Checkboxes | ✅ `scripts\settings.gd:197 # 3 个开关 (原版 Checkboxes: Disable Bots / Disable Notifications / Touch input — 75.6 高间距 108.25)` |
| Disable Bots | ✅ `scripts\settings.gd:197 # 3 个开关 (原版 Checkboxes: Disable Bots / Disable Notifications / Touch input — 75.6 高间距 108.25); scripts\set` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Disable Notifications | ✅ `scripts\settings.gd:197 # 3 个开关 (原版 Checkboxes: Disable Bots / Disable Notifications / Touch input — 75.6 高间距 108.25); scripts\set` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Touch Input | ✅ `scripts\settings.gd:201 ["Touch Input", "touch"],` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Bottom Buttons | ✅ `scripts\settings.gd:217 # 底部按钮 (原版 Bottom Buttons: Redeem Code 300x90 + Exit Game 300x90, 屏幕 y 780..870)` |
| Redeem Code | ✅ `scripts\settings.gd:217 # 底部按钮 (原版 Bottom Buttons: Redeem Code 300x90 + Exit Game 300x90, 屏幕 y 780..870); scripts\settings.gd:221 ` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Close Game Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Media Tab | ⚠️ 未命中 |
| Tab Title | ⚠️ 未命中 |
| Audio Settings | ✅ `scripts\settings.gd:243 # 音频 (说明书 Audio Settings [597,280]: Music 'Música' / Sound FX 'Efectos de Sonido' / Voice 'Narracion` |
| Music Container | ⚠️ 未命中 |
| Music Slider | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| FX Container | ⚠️ 未命中 |
| Sound effects Slider | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Voiceovers Container | ⚠️ 未命中 |
| Voice Over Slider | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Visual Settings | ✅ `scripts\settings.gd:250 # 窗口模式 (说明书 Visual Settings WindowMode Selector [597,631] → 相对内容区 (90,508))` |
| WindowMode Selector | ✅ `scripts\settings.gd:250 # 窗口模式 (说明书 Visual Settings WindowMode Selector [597,631] → 相对内容区 (90,508))` |
| Dropdown | ✅ `scripts\settings.gd:187 # 语言选择 (说明书 LanguagesDropdown [597,339] 401x59 → 相对内容区 (90,216); 标签右移对齐)` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Arrow | ✅ `scripts\where_cards_popup.gd:142 arrow.name = "Arrow"` |
| Template | ✅ `scripts\deck_info_popup.gd:572 _Toast("Template decks cannot be edited; create your own"); scripts\deck_info_popup.gd:582 _Toast("` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Item | ✅ `scripts\battle.gd:1727 # Avatar Item Small x[-19,136] y[12,149] 156×137; ShowCemeteryBtn 64² x[52,116] y[136,200]; scripts\battle.` |
| Item Background | ⚠️ 未命中 |
| Item Checkmark | ⚠️ 未命中 |
| Item Label | ⚠️ 未命中 |
| Scrollbar | ✅ `scripts\collection.gd:637 # 原版 m_VerticalScrollbar=0 无滚动条 — 2026-08-21 审查: 去除金色滚动条, 仅透明面板` |
| Sliding Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Account Tab | ⚠️ 未命中 |
| Tab Title | ⚠️ 未命中 |
| Player Id | ⚠️ 未命中 |
| Player Id Text | ⚠️ 未命中 |
| External Link Icon | ⚠️ 未命中 |
| Account Form | ⚠️ 未命中 |
| EmailText | ⚠️ 未命中 |
| InputEmail | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| PasswordText | ⚠️ 未命中 |
| InputPassword | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Reset Password | ⚠️ 未命中 |
| Forgot Password | ⚠️ 未命中 |
| Error Message | ⚠️ 未命中 |
| Subscribe Newsletter | ⚠️ 未命中 |
| Social Media Links | ⚠️ 未命中 |
| Discord Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| IG Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Facebook Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Twitter Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Youtube Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Buttons | ✅ `scripts\battle.gd:2048 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Unregistered Buttons | ⚠️ 未命中 |
| Register Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Login Button  | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Twitch Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Delete Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Registered Buttons | ⚠️ 未命中 |
| Switch Account Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Logout Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Login Window | ⚠️ 未命中 |
| Backgroun filler | ⚠️ 未命中 |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ⚠️ 未命中 |
| EmailText | ⚠️ 未命中 |
| InputEmail | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| PasswordText | ⚠️ 未命中 |
| InputPassword | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Forgot Password | ⚠️ 未命中 |
| ErrorMensajeContainer | ⚠️ 未命中 |
| Animated Loading Image | ✅ `scripts\loading.gd:3 ## 2026-08-18 重做: 按主菜单全树.md Loading Controller 结构 — Animated Loading Image 270x270; scripts\loading.gd:21 # 骷` |
| Cog | ✅ `scripts\loading.gd:4 ## (40K_icon_searching_skull) + Cog 270x270 (40K_icon_searching_cog) 同心覆盖旋转; scripts\loading.gd:30 # 齿轮 (原版 C` |
| Error Message | ⚠️ 未命中 |
| Login Button  | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Close Button Green | ✅ `scripts\import_deck_popup.gd:120 # 关闭 (原版 Generic Close Button Green: Window 中心 (960,620), anchor(0.5,0.5) ap(394.8,220.4) 75x75` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Support Tab | ✅ `scripts\main_menu.gd:941 ## 反馈按钮: 打开反馈问卷 (原版 Support Tab → Feedback)` |
| Tab Title | ⚠️ 未命中 |
| Faq Text | ✅ `scripts\settings.gd:405 # 说明书: Faq Text [597,272] 942x85 / Faq Button [597,373] 360x60 / Contact [597,530]` |
| Faq Button | ✅ `scripts\settings.gd:405 # 说明书: Faq Text [597,272] 942x85 / Faq Button [597,373] 360x60 / Contact [597,530]` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| External Link Icon | ⚠️ 未命中 |
| Contact Text | ⚠️ 未命中 |
| Contact Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| External Link Icon | ⚠️ 未命中 |
| Support Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Email Text | ✅ `scripts\settings.gd:413 # 邮箱 (原版 Email Text 'You can also contact us at support@everguild.com')` |
| bottom links | ⚠️ 未命中 |
| Terms of Service | ⚠️ 未命中 |
| External Link Icon | ⚠️ 未命中 |
| Terms of Service Text | ⚠️ 未命中 |
| Privacy Policy | ⚠️ 未命中 |
| External Link Icon | ⚠️ 未命中 |
| Privacy Policy Button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Faq Text Mobile | ⚠️ 未命中 |
| Email Text Mobile | ⚠️ 未命中 |
| Graphics Tab | ⚠️ 未命中 |
| Tab Title | ⚠️ 未命中 |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Quality  Selector | ⚠️ 未命中 |
| Quality DropDown | ⚠️ 未命中 |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Arrow | ✅ `scripts\where_cards_popup.gd:142 arrow.name = "Arrow"` |
| Template | ✅ `scripts\deck_info_popup.gd:572 _Toast("Template decks cannot be edited; create your own"); scripts\deck_info_popup.gd:582 _Toast("` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Item | ✅ `scripts\battle.gd:1727 # Avatar Item Small x[-19,136] y[12,149] 156×137; ShowCemeteryBtn 64² x[52,116] y[136,200]; scripts\battle.` |
| Item Background | ⚠️ 未命中 |
| Item Checkmark | ⚠️ 未命中 |
| Item Label | ⚠️ 未命中 |
| Scrollbar | ✅ `scripts\collection.gd:637 # 原版 m_VerticalScrollbar=0 无滚动条 — 2026-08-21 审查: 去除金色滚动条, 仅透明面板` |
| Sliding Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Quality selector text | ⚠️ 未命中 |
| Text In Hand  Selector | ⚠️ 未命中 |
| Text in Hand DropDown | ⚠️ 未命中 |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Arrow | ✅ `scripts\where_cards_popup.gd:142 arrow.name = "Arrow"` |
| Template | ✅ `scripts\deck_info_popup.gd:572 _Toast("Template decks cannot be edited; create your own"); scripts\deck_info_popup.gd:582 _Toast("` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Item | ✅ `scripts\battle.gd:1727 # Avatar Item Small x[-19,136] y[12,149] 156×137; ShowCemeteryBtn 64² x[52,116] y[136,200]; scripts\battle.` |
| Item Background | ⚠️ 未命中 |
| Item Checkmark | ⚠️ 未命中 |
| Item Label | ⚠️ 未命中 |
| Scrollbar | ✅ `scripts\collection.gd:637 # 原版 m_VerticalScrollbar=0 无滚动条 — 2026-08-21 审查: 去除金色滚动条, 仅透明面板` |
| Sliding Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| Quality selector text | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Small Screen Size Toggle | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Auto Zoom Toggle | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Hi FPS toggl | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Android extra compatibility | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Tooltip - Extended compaibility | ⚠️ 未命中 |
| Use super sampling | ✅ `scripts\settings.gd:365 ["Use super sampling", "superSampling"],` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Vsync | ✅ `scripts\settings.gd:366 ["Vsync", "vsync"],` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| FPS Limit | ✅ `scripts\settings.gd:382 # FPS Limit 滑块 (滚动区底部); scripts\settings.gd:383 _make_label(page, "FPS Limit", Vector2(90, ty + 10), Vecto` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| FPS Slider | ⚠️ 未命中 |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| Handle Slide Area | ⚠️ 未命中 |
| Handle | ✅ `scripts\deck_builder.gd:37 # ---- 拖拽/放置内部类 (原版 CardDraggingController: IBeginDragHandler+IDragHandler+IEndDragHandler;; scripts\de` |
| 30 FPS | ✅ `scripts\settings.gd:387 fps_opt.add_item("30 FPS")` |
| 60 FPS | ✅ `scripts\settings.gd:388 fps_opt.add_item("60 FPS")` |
| Unlimited | ✅ `scripts\settings.gd:389 fps_opt.add_item("Unlimited")` |

## 摘要

- 规格元素: 324
- 代码命中: 195
- ⚠️未命中: 129 (以下需人工判断)

- `Debug Buttons`
- `Buttons container`
- `Unlink`
- `ResetTutorial`
- `AddCoins`
- `Season Check`
- `Reset GameModes`
- `Reset Feedback`
- `Reset Events`
- `AddWildcards`
- `RateButton`
- `ResetDLC`
- `Enviromental Debug`
- `GetRewards`
- `Score On Leaderboard`
- `Time Offset`
- `Clean Cache`
- `Toggle  Debug`
- `Debug button text`
- `Border 2`
- `Border 3`
- `old menu`
- `Steam Button`
- `steamImage`
- `Background fill`
- `Popup BG`
- `Mask Tabs buttons`
- `OneText`
- `General Tab`
- `Tab Title`
- `Language Selector`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `SelectLanguageText`
- `Close Game Button`
- `Media Tab`
- `Tab Title`
- `Music Container`
- `Music Slider`
- `Handle Slide Area`
- `FX Container`
- `Sound effects Slider`
- `Handle Slide Area`
- `Voiceovers Container`
- `Voice Over Slider`
- `Handle Slide Area`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `Account Tab`
- `Tab Title`
- `Player Id`
- `Player Id Text`
- `External Link Icon`
- `Account Form`
- `EmailText`
- `InputEmail`
- `PasswordText`
- `InputPassword`
- `Reset Password`
- `Forgot Password`
- `Error Message`
- `Subscribe Newsletter`
- `Social Media Links`
- `Discord Button`
- `IG Button`
- `Facebook Button`
- `Twitter Button`
- `Youtube Button`
- `Unregistered Buttons`
- `Register Button`
- `Login Button `
- `Twitch Button`
- `Delete Button`
- `Registered Buttons`
- `Switch Account Button`
- `Logout Button`
- `Login Window`
- `Backgroun filler`
- `Background fill`
- `EmailText`
- `InputEmail`
- `PasswordText`
- `InputPassword`
- `Forgot Password`
- `ErrorMensajeContainer`
- `Error Message`
- `Login Button `
- `Tab Title`
- `External Link Icon`
- `Contact Text`
- `Contact Button`
- `External Link Icon`
- `Support Button`
- `bottom links`
- `Terms of Service`
- `External Link Icon`
- `Terms of Service Text`
- `Privacy Policy`
- `External Link Icon`
- `Privacy Policy Button`
- `Faq Text Mobile`
- `Email Text Mobile`
- `Graphics Tab`
- `Tab Title`
- `Quality  Selector`
- `Quality DropDown`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `Quality selector text`
- `Text In Hand  Selector`
- `Text in Hand DropDown`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `Quality selector text`
- `Small Screen Size Toggle`
- `Auto Zoom Toggle`
- `Hi FPS toggl`
- `Android extra compatibility`
- `Tooltip - Extended compaibility`
- `FPS Slider`
- `Handle Slide Area`