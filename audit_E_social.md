# UI 规格审计: Social Submenu Variant

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:46
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Social Submenu Variant [godot(x0.0 y0.0 w1920.0 h1080.0)]
  Content Area [godot(x167.2 y70.9 w1752.8 h1009.1)]
    Background [godot(x167.2 y70.9 w1752.8 h1009.1)]
    Tab Buttons [godot(x167.2 y70.9 w165.0 h1009.1)]
      Alliances Tab Button [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Alliances godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1014.6 w35.0 h35.0)]
          OneText [godot(x201.4 y1015.5 w35.0 h35.0)]
      Friends Tab Button [godot(x167.2 y990.0 w0.0 h180.0)]
        Highlight [godot(x167.2 y990.0 w0.0 h180.0)]
        Icon [godot(x167.2 y990.0 w0.0 h180.0)]
        Label [godot(x89.7 y1114.3 w155.0 h37.9)]
          TabButtonLabel [txt=Friends godot(x89.7 y1114.3 w155.0 h37.9)]
        Badge Highlight [godot(x201.4 y1014.6 w35.0 h35.0)]
          OneText [godot(x201.4 y1015.5 w35.0 h35.0)]
      Shadow [godot(x167.2 y70.9 w47.6 h1009.1)]
    Tabs [godot(x167.2 y70.9 w1752.8 h1009.1)]
      Alliances Tab [godot(x167.2 y70.9 w1752.8 h1009.1)]
        AllianceNotMemberVariant [godot(x332.2 y70.9 w1587.3 h1009.1)]
          Alliance Header Buttons [godot(x331.7 y89.9 w1588.3 h72.1)]
            Divisor line [godot(x331.2 y158.4 w1589.3 h3.6)]
            Tab buttons [godot(x360.5 y89.9 w1057.3 h68.5)]
              Generic Tab UI Button Search [godot(x230.5 y124.5 w260.0 h67.7)]
                Button Text [txt=Join godot(x240.1 y129.2 w240.7 h67.7)]
              Generic Tab UI Button Create [godot(x230.5 y124.5 w260.0 h67.7)]
                Button Text [txt=Create godot(x240.1 y129.2 w240.7 h67.7)]
          List View [godot(x361.0 y162.0 w1541.6 h918.0)]
            Search Field [godot(x1402.0 y172.9 w396.6 h57.0)]
              Text Area [godot(x1406.6 y172.9 w352.0 h57.0)]
                Placeholder [txt=Search godot(x1406.6 y172.9 w352.0 h57.0)]
                Text [txt=​ godot(x1406.6 y172.9 w352.0 h57.0)]
              Generic Round Button Variant [godot(x1800.8 y171.4 w60.0 h60.0)]
                Button Text [inactive txt=X godot(x1808.8 y171.4 w44.0 h60.0)]
                Image [godot(x1812.4 y183.0 w36.7 h36.7)]
            List Area [godot(x361.0 y252.3 w1513.9 h827.5)]
              Invitations [godot(x-396.0 y1079.8 w1513.9 h0.0)]
                Title [txt=Alliances invitations: godot(x-1148.5 y1079.8 w1505.0 h0.0)]
                List [godot(x-1148.5 y1079.8 w1505.0 h0.0)]
                  Invitation List Entry [godot(x-1148.5 y1024.8 w0.0 h110.0)]
                    background [godot(x-1148.5 y1024.8 w0.0 h110.0)]
                    BadgeDrawer [godot(x-1882.2 y1034.8 w90.0 h90.0)]
                      Frame [godot(x-1882.2 y1034.8 w90.0 h90.0)]
                      Badge [godot(x-1882.2 y1034.8 w90.0 h90.0)]
                    Title [txt=Alliance Name Bla Bla godot(x-1014.9 y1029.3 w505.5 h53.0)]
                    Region [txt=Global godot(x-1014.9 y1083.1 w505.5 h44.6)]
                    Members Header [txt=Members: godot(x-509.4 y1037.6 w177.1 h36.4)]
                    Member Count [txt=17/20 godot(x-509.4 y1080.1 w177.1 h52.4)]
                    Ranking Header [txt=Ranking: godot(x-301.0 y1037.6 w177.1 h36.4)]
                    Ranking Score [godot(x-1072.2 y1077.8 w202.5 h52.4)]
                      Icon [godot(x-1099.9 y1102.5 w55.4 h55.4)]
                      Ranking Value [txt=-------- godot(x-943.3 y1079.6 w0.0 h48.7)]
                    raycastTarget [godot(x-1148.5 y1024.8 w0.0 h110.0)]
                    Join [godot(x-854.7 y1049.2 w200.0 h57.0)]
                      Button Text [txt=Join godot(x-841.7 y1049.2 w174.0 h57.0)]
                    Reject [godot(x-644.7 y1048.5 w200.0 h57.0)]
                      Button Text [txt=Dismiss godot(x-631.7 y1048.5 w174.0 h57.0)]
                  Invitation List Entry (1) [godot(x-1148.5 y1024.8 w0.0 h110.0)]
                    background [godot(x-1148.5 y1024.8 w0.0 h110.0)]
                    BadgeDrawer [godot(x-1882.2 y1034.8 w90.0 h90.0)]
                      Frame [godot(x-1882.2 y1034.8 w90.0 h90.0)]
                      Badge [godot(x-1882.2 y1034.8 w90.0 h90.0)]
                    Title [txt=Alliance Name Bla Bla godot(x-1014.9 y1029.3 w505.5 h53.0)]
                    Region [txt=Global godot(x-1014.9 y1083.1 w505.5 h44.6)]
                    Members Header [txt=Members: godot(x-509.4 y1037.6 w177.1 h36.4)]
                    Member Count [txt=17/20 godot(x-509.4 y1080.1 w177.1 h52.4)]
                    Ranking Header [txt=Ranking: godot(x-301.0 y1037.6 w177.1 h36.4)]
                    Ranking Score [godot(x-1072.2 y1077.8 w202.5 h52.4)]
                      Icon [godot(x-1099.9 y1102.5 w55.4 h55.4)]
                      Ranking Value [txt=-------- godot(x-943.3 y1079.6 w0.0 h48.7)]
                    raycastTarget [godot(x-1148.5 y1024.8 w0.0 h110.0)]
                    Join [godot(x-854.7 y1049.2 w200.0 h57.0)]
                      Button Text [txt=Join godot(x-841.7 y1049.2 w174.0 h57.0)]
                    Reject [godot(x-644.7 y1048.5 w200.0 h57.0)]
                      Button Text [txt=Dismiss godot(x-631.7 y1048.5 w174.0 h57.0)]
              Open Alliances [godot(x-396.0 y1079.8 w1513.9 h0.0)]
                Title [txt=Open alliances: godot(x-396.0 y1079.8 w1513.9 h45.0)]
                Viewport [godot(x-396.0 y1139.8 w1513.9 h-60.0)]
                  List [godot(x-396.0 y1139.8 w1505.0 h110.0)]
                    Entry [godot(x-396.0 y1139.8 w1505.0 h110.0)]
                      background [godot(x-396.0 y1139.8 w1505.0 h110.0)]
                      BadgeDrawer [godot(x-377.2 y1149.8 w90.0 h90.0)]
                        Frame [godot(x-377.2 y1149.8 w90.0 h90.0)]
                        Badge [godot(x-377.2 y1149.8 w90.0 h90.0)]
                      Title [txt=Alliance Name Bla Bla godot(x-262.4 y1144.3 w505.5 h53.0)]
                      Region [txt=Global godot(x-262.4 y1198.1 w505.5 h44.6)]
                      Members Header [txt=Members: godot(x243.1 y1156.6 w177.1 h36.4)]
                      Member Count [txt=17/20 godot(x243.1 y1199.1 w177.1 h48.7)]
                      Ranking Header [txt=Ranking: godot(x451.5 y1156.6 w177.1 h36.4)]
                      Ranking [godot(x436.9 y1194.8 w206.3 h53.0)]
                        Icon [godot(x410.1 y1220.9 w53.6 h53.7)]
                        Ranking Value [txt=45 godot(x566.9 y1193.3 w0.0 h56.0)]
                      raycastTarget [godot(x-396.0 y1139.8 w1505.0 h110.0)]
                      Generic UI Button [godot(x792.0 y1161.0 w245.0 h67.6)]
                        Button Text [txt=Join godot(x805.0 y1161.0 w219.0 h67.6)]
          Create Alliance View [inactive godot(x368.5 y165.1 w1513.9 h914.9)]
            TopAnchor [godot(x368.5 y165.1 w1513.9 h61.9)]
              Name input title [txt=Alliance Name godot(x432.5 y257.7 w692.9 h50.0)]
                Name Input [godot(x432.5 y308.0 w900.0 h59.3)]
                  Text Area [godot(x442.5 y315.0 w880.0 h46.3)]
                    Placeholder [inactive txt=TESTE godot(x442.5 y315.0 w880.0 h46.3)]
                    Text [txt=​ godot(x442.5 y315.0 w880.0 h46.3)]
              Desc input title [txt=Alliance Description godot(x432.5 y403.0 w692.9 h50.0)]
                Desc Input [godot(x432.5 y454.5 w900.0 h204.5)]
                  Text Area [godot(x442.5 y461.5 w880.0 h191.5)]
                    Placeholder [inactive txt=TESTE godot(x442.5 y461.5 w880.0 h191.5)]
                    Text [txt=​ godot(x442.5 y461.5 w880.0 h191.5)]
              Create Alliance Text [txt=Create alliance godot(x428.1 y666.8 w250.0 h56.8)]
                Price Display Button [godot(x428.1 y714.2 w250.0 h78.8)]
                  Generic UI Button [godot(x428.1 y714.2 w250.0 h78.8)]
                    Button Text [inactive txt=Continue godot(x441.1 y740.4 w224.0 h26.4)]
                    Price Display [godot(x437.6 y730.7 w229.1 h46.9)]
                      icon [godot(x490.5 y726.0 w56.3 h56.3)]
                      text [txt=1000 godot(x546.8 y730.7 w67.0 h46.9)]
              Select Language [txt=Select language godot(x1440.4 y250.9 w250.0 h56.8)]
                LanguagesDropdown [godot(x1440.4 y307.6 w250.0 h59.4)]
                  Label [godot(x1450.4 y314.6 w230.0 h46.4)]
                  Arrow [godot(x1665.4 y327.3 w20.0 h20.0)]
                  Template [inactive godot(x1440.4 y359.3 w245.0 h574.0)]
                    Viewport [godot(x1440.4 y359.3 w228.0 h574.0)]
                      Content [godot(x1440.4 y359.3 w228.0 h41.8)]
                        Item [godot(x1440.4 y359.8 w228.0 h40.8)]
                          Item Background [godot(x1440.4 y359.8 w228.0 h40.8)]
                          Item Checkmark [godot(x1440.4 y370.2 w20.0 h20.0)]
                          Item Label [txt=Option A godot(x1460.4 y361.8 w198.0 h37.8)]
                    Scrollbar [godot(x1665.4 y359.3 w20.0 h574.0)]
                      Sliding Area [godot(x1675.4 y369.3 w0.0 h554.0)]
                        Handle [godot(x1665.4 y399.6 w20.0 h533.7)]
              Select Privacy [txt=Select privacy godot(x1440.4 y397.5 w250.0 h56.8)]
                Privacy Dropdown [godot(x1440.4 y454.3 w250.0 h59.4)]
                  Label [godot(x1450.4 y461.3 w230.0 h46.4)]
                  Arrow [godot(x1665.4 y474.0 w20.0 h20.0)]
                  Template [inactive godot(x1440.4 y506.0 w245.0 h573.9)]
                    Viewport [godot(x1440.4 y506.0 w228.0 h573.9)]
                      Content [godot(x1440.4 y506.0 w228.0 h41.7)]
                        Item [godot(x1440.4 y506.4 w228.0 h40.9)]
                          Item Background [godot(x1440.4 y506.4 w228.0 h40.9)]
                          Item Checkmark [godot(x1440.4 y516.8 w20.0 h20.0)]
                          Item Label [txt=Option A godot(x1460.4 y508.4 w198.0 h37.9)]
                    Scrollbar [godot(x1665.4 y506.0 w20.0 h573.9)]
                      Sliding Area [godot(x1675.4 y516.0 w0.0 h553.9)]
                        Handle [godot(x1665.4 y546.2 w20.0 h533.7)]
          GeneralDetails [inactive godot(x332.7 y162.0 w1586.3 h918.0)]
            Content [godot(x332.7 y162.0 w1586.3 h918.0)]
              DEBUG_TEXTS [txt=Season: 10\n10/30/200 29:00\n godot(x955.0 y75.5 w499.4 h71.1)]
              BadgeDrawer [godot(x360.4 y170.5 w250.5 h235.1)]
                Frame [godot(x360.4 y170.5 w250.5 h235.1)]
                Badge [godot(x360.4 y170.5 w250.5 h235.1)]
              Alliance name text [txt=Alliance Name bla bla godot(x614.9 y177.5 w499.3 h71.1)]
              Alliance Rating Display [godot(x614.9 y237.4 w486.6 h80.8)]
                Secondary Icon [inactive godot(x614.9 y237.4 w94.7 h80.8)]
                Main Icon [godot(x614.9 y318.2 w0.0 h0.0)]
                Individual rating value [txt=------- godot(x614.9 y318.2 w0.0 h0.0)]
              Draft Rating Display [godot(x614.9 y318.2 w486.6 h80.8)]
                Secondary Icon [inactive godot(x614.9 y318.2 w94.7 h80.8)]
                Main Icon [godot(x614.9 y399.0 w0.0 h0.0)]
                Individual rating value [txt=------- godot(x614.9 y399.0 w0.0 h0.0)]
              Config fields [godot(x1079.5 y183.0 w782.8 h60.0)]
                extra_info [txt=English / Private godot(x1408.7 y183.0 w453.6 h60.0)]
                LanguagesDropdown [inactive godot(x1129.9 y183.6 w250.0 h59.4)]
                  Label [godot(x1139.9 y190.6 w230.0 h46.4)]
                  Arrow [godot(x1354.9 y203.3 w20.0 h20.0)]
                  Template [inactive godot(x1129.9 y235.3 w245.0 h574.0)]
                    Viewport [godot(x1129.9 y235.3 w228.0 h574.0)]
                      Content [godot(x1129.9 y235.3 w228.0 h41.7)]
                        Item [godot(x1129.9 y235.7 w228.0 h40.9)]
                          Item Background [godot(x1129.9 y235.7 w228.0 h40.9)]
                          Item Checkmark [godot(x1129.9 y246.2 w20.0 h20.0)]
                          Item Label [txt=Option A godot(x1149.9 y237.7 w198.0 h37.9)]
                    Scrollbar [godot(x1354.9 y235.3 w20.0 h574.0)]
                      Sliding Area [godot(x1364.9 y245.3 w0.0 h554.0)]
                        Handle [godot(x1354.9 y275.6 w20.0 h533.7)]
                Privacy Dropdown [inactive godot(x1394.4 y183.6 w250.0 h59.4)]
                  Label [godot(x1404.4 y190.6 w230.0 h46.4)]
                  Arrow [godot(x1619.4 y203.3 w20.0 h20.0)]
                  Template [inactive godot(x1394.4 y235.3 w245.0 h574.0)]
                    Viewport [godot(x1394.4 y235.3 w228.0 h574.0)]
                      Content [godot(x1394.4 y235.3 w228.0 h41.7)]
                        Item [godot(x1394.4 y235.7 w228.0 h40.9)]
                          Item Background [godot(x1394.4 y235.7 w228.0 h40.9)]
                          Item Checkmark [godot(x1394.4 y246.2 w20.0 h20.0)]
                          Item Label [txt=Option A godot(x1414.4 y237.7 w198.0 h37.9)]
                    Scrollbar [godot(x1619.4 y235.3 w20.0 h574.0)]
                      Sliding Area [godot(x1629.4 y245.3 w0.0 h554.0)]
                        Handle [godot(x1619.4 y275.6 w20.0 h533.7)]
                Edit button [inactive godot(x1658.9 y183.0 w58.1 h60.0)]
                  Button Text [inactive txt=X godot(x1666.9 y183.0 w42.1 h60.0)]
                  Image [godot(x1661.0 y185.7 w50.1 h54.6)]
                Confirm button [inactive godot(x1731.5 y183.0 w58.2 h60.0)]
                  Button Text [inactive txt=X godot(x1739.5 y183.0 w42.2 h60.0)]
                  Image [godot(x1733.2 y188.4 w53.0 h46.8)]
                Cancel button [inactive godot(x1804.2 y183.0 w58.1 h60.0)]
                  Button Text [inactive txt=X godot(x1812.2 y183.0 w42.1 h60.0)]
                  Image [godot(x1859.9 y181.5 w-56.1 h58.0)]
              Description input text [godot(x1129.4 y262.1 w748.8 h193.2)]
                Text Area [godot(x1139.4 y269.1 w728.8 h180.2)]
                  Placeholder [inactive txt=Enter text... godot(x1139.4 y269.1 w728.8 h180.2)]
                  description text [txt=Aliance Description Aliance Description  godot(x1145.3 y264.9 w717.0 h190.0)]
              Divisor line members [godot(x332.2 y463.1 w1587.3 h3.6)]
              MemberList [godot(x370.9 y419.8 w1511.5 h660.2)]
                members label [txt=Members: --/20 godot(x370.9 y420.2 w594.9 h41.5)]
                Scroll View [godot(x371.2 y466.8 w1511.0 h613.2)]
                  Viewport [godot(x371.2 y466.8 w1511.0 h613.2)]
                    Content [godot(x371.2 y466.8 w1511.0 h76.8)]
                      Alliance Member Entry [godot(x371.2 y543.6 w0.0 h0.0)]
                        background [godot(x371.2 y543.6 w0.0 h0.0)]
                          Image [godot(x-1.6 y496.1 w45.3 h95.1)]
                        member index [txt=5 godot(x-1.3 y496.2 w44.5 h94.8)]
                        Avatar Item Small [godot(x421.7 y505.5 w98.9 h103.1)]
                          Raycast Target [inactive godot(x381.7 y440.7 w178.9 h214.4)]
                          Image Container [godot(x421.7 y505.5 w98.9 h65.7)]
                            Highlight [godot(x375.7 y471.6 w194.2 h128.3)]
                            Border [godot(x409.4 y503.9 w123.6 h82.1)]
                            Image [godot(x372.3 y469.9 w197.8 h131.4)]
                          Avatar Name [inactive txt=Avatar name godot(x421.7 y608.6 w98.9 h41.3)]
                        connection status [godot(x424.1 y562.0 w22.5 h29.0)]
                        member name [txt=Pepito el de siempr godot(x145.6 y505.5 w545.3 h47.4)]
                        member role [txt=Alliance Master godot(x145.6 y552.9 w346.1 h39.3)]
                        Ratings [godot(x520.6 y497.0 w215.8 h94.0)]
                          Draft Rating [godot(x520.6 y567.7 w0.0 h46.5)]
                            Secondary Icon [inactive godot(x520.6 y567.7 w44.4 h59.2)]
                            Main Icon [godot(x520.6 y614.2 w0.0 h0.0)]
                            Individual rating value [txt=32 godot(x520.6 y614.2 w0.0 h0.0)]
                          Ranked Rating [godot(x520.6 y591.0 w0.0 h0.0)]
                            Secondary Icon [inactive godot(x520.6 y591.0 w44.4 h59.1)]
                            Main Icon [godot(x520.6 y591.0 w0.0 h0.0)]
                            Individual rating value [txt=555 godot(x520.6 y591.0 w0.0 h0.0)]
        AllianceMemberVariant [inactive godot(x330.7 y70.9 w1589.8 h1009.1)]
          Alliance Header Buttons (1) [godot(x331.2 y116.6 w1588.8 h72.2)]
            Divisor line [godot(x330.7 y185.1 w1589.8 h3.7)]
            Tab buttons [godot(x360.0 y116.7 w1057.3 h68.4)]
              Generic Tab UI Button Info [godot(x360.0 y117.1 w260.0 h67.6)]
                Button Text [txt=General godot(x369.6 y132.2 w240.7 h46.8)]
              Generic Tab UI Button Trophies [godot(x632.4 y117.1 w260.0 h67.6)]
                Button Text [txt=Trophies godot(x642.1 y132.2 w240.7 h46.8)]
          GeneralDetails [godot(x331.2 y188.8 w1588.8 h891.2)]
            Content [godot(x331.2 y188.8 w1588.8 h891.2)]
              DEBUG_TEXTS [txt=Season: 10\n10/30/200 29:00\n godot(x953.5 y102.3 w499.4 h71.1)]
              BadgeDrawer [godot(x358.9 y197.3 w250.5 h235.1)]
                Frame [godot(x358.9 y197.3 w250.5 h235.1)]
                Badge [godot(x358.9 y197.3 w250.5 h235.1)]
              Alliance name text [txt=Alliance Name bla bla godot(x613.4 y204.3 w499.3 h71.0)]
              Alliance Rating Display [godot(x613.4 y264.2 w486.6 h80.8)]
                Secondary Icon [inactive godot(x613.4 y264.2 w94.7 h80.8)]
                Main Icon [godot(x613.4 y264.2 w60.0 h80.8)]
                Individual rating value [txt=------- godot(x673.4 y264.2 w426.6 h80.8)]
              Draft Rating Display [godot(x613.4 y345.0 w486.6 h80.8)]
                Secondary Icon [inactive godot(x613.4 y345.0 w94.7 h80.8)]
                Main Icon [godot(x613.4 y345.0 w60.0 h80.8)]
                Individual rating value [txt=------- godot(x673.4 y345.0 w426.6 h80.8)]
              Config fields [godot(x1080.5 y209.8 w782.8 h60.0)]
                extra_info [inactive txt=English / Private godot(x1080.5 y209.8 w453.7 h60.0)]
                LanguagesDropdown [godot(x1130.9 y210.4 w250.0 h59.4)]
                  Label [godot(x1140.9 y217.4 w230.0 h46.4)]
                  Arrow [godot(x1355.9 y230.1 w20.0 h20.0)]
                  Template [inactive godot(x1130.9 y262.1 w245.0 h574.0)]
                    Viewport [godot(x1130.9 y262.1 w228.0 h574.0)]
                      Content [godot(x1130.9 y262.1 w228.0 h41.7)]
                        Item [godot(x1130.9 y262.5 w228.0 h40.9)]
                          Item Background [godot(x1130.9 y262.5 w228.0 h40.9)]
                          Item Checkmark [godot(x1130.9 y273.0 w20.0 h20.0)]
                          Item Label [txt=Option A godot(x1150.9 y264.5 w198.0 h37.9)]
                    Scrollbar [godot(x1355.9 y262.1 w20.0 h574.0)]
                      Sliding Area [godot(x1365.9 y272.1 w0.0 h554.0)]
                        Handle [godot(x1355.9 y302.4 w20.0 h533.7)]
                Privacy Dropdown [godot(x1395.4 y210.4 w250.0 h59.4)]
                  Label [godot(x1405.4 y217.4 w230.0 h46.4)]
                  Arrow [godot(x1620.4 y230.1 w20.0 h20.0)]
                  Template [inactive godot(x1395.4 y262.1 w245.0 h574.0)]
                    Viewport [godot(x1395.4 y262.1 w228.0 h574.0)]
                      Content [godot(x1395.4 y262.1 w228.0 h41.7)]
                        Item [godot(x1395.4 y262.5 w228.0 h40.9)]
                          Item Background [godot(x1395.4 y262.5 w228.0 h40.9)]
                          Item Checkmark [godot(x1395.4 y273.0 w20.0 h20.0)]
                          Item Label [txt=Option A godot(x1415.4 y264.5 w198.0 h37.9)]
                    Scrollbar [godot(x1620.4 y262.1 w20.0 h574.0)]
                      Sliding Area [godot(x1630.4 y272.1 w0.0 h554.0)]
                        Handle [godot(x1620.4 y302.4 w20.0 h533.7)]
                Edit button [godot(x1659.9 y209.8 w58.1 h60.0)]
                  Button Text [inactive txt=X godot(x1667.9 y209.8 w42.1 h60.0)]
                  Image [godot(x1662.0 y212.5 w50.1 h54.6)]
                Confirm button [godot(x1732.5 y209.8 w58.2 h60.0)]
                  Button Text [inactive txt=X godot(x1740.5 y209.8 w42.2 h60.0)]
                  Image [godot(x1734.2 y215.2 w53.0 h46.7)]
                Cancel button [godot(x1805.2 y209.8 w58.1 h60.0)]
                  Button Text [inactive txt=X godot(x1813.2 y209.8 w42.1 h60.0)]
                  Image [godot(x1860.9 y208.3 w-56.1 h58.0)]
              Description input text [godot(x1130.4 y288.8 w748.8 h193.3)]
                Text Area [godot(x1140.4 y295.8 w728.8 h180.3)]
                  Placeholder [inactive txt=Enter text... godot(x1140.4 y295.8 w728.8 h180.3)]
                  description text [txt=Aliance Description Aliance Description  godot(x1146.3 y291.6 w717.0 h190.1)]
              Divisor line members [godot(x330.7 y489.8 w1589.8 h3.7)]
              MemberList [godot(x369.4 y446.5 w1511.5 h633.5)]
                members label [txt=Members: --/20 godot(x369.4 y447.0 w594.9 h41.4)]
                Scroll View [godot(x369.7 y493.6 w1511.0 h586.4)]
                  Viewport [godot(x369.7 y493.6 w1511.0 h586.4)]
                    Content [godot(x369.7 y493.6 w1511.0 h184.0)]
                      Alliance Member Entry [godot(x369.7 y502.6 w750.0 h100.0)]
                        background [godot(x369.7 y502.6 w750.0 h100.0)]
                          Image [godot(x371.9 y505.2 w45.3 h95.0)]
                        member index [txt=5 godot(x372.2 y505.2 w44.5 h94.8)]
                        Avatar Item Small [godot(x420.2 y514.5 w98.9 h103.1)]
                          Raycast Target [inactive godot(x380.2 y449.7 w178.9 h214.4)]
                          Image Container [godot(x420.2 y514.5 w98.9 h65.7)]
                            Highlight [godot(x374.2 y480.6 w194.2 h128.3)]
                            Border [godot(x407.9 y512.9 w123.6 h82.1)]
                            Image [godot(x370.8 y479.0 w197.8 h131.3)]
                          Avatar Name [inactive txt=Avatar name godot(x420.2 y617.6 w98.9 h41.3)]
                        connection status [godot(x422.6 y571.0 w22.5 h29.0)]
                        member name [txt=Pepito el de siempr godot(x519.1 y514.5 w545.3 h47.4)]
                        member role [txt=Alliance Master godot(x519.1 y561.9 w346.1 h39.3)]
                        Ratings [godot(x894.1 y506.0 w215.8 h94.0)]
                          Draft Rating [godot(x894.1 y506.0 w215.8 h46.5)]
                            Secondary Icon [inactive godot(x894.1 y506.0 w44.4 h59.2)]
                            Main Icon [godot(x1009.6 y506.0 w65.0 h46.5)]
                            Individual rating value [txt=32 godot(x1074.6 y506.0 w35.3 h46.5)]
                          Ranked Rating [godot(x894.1 y552.5 w215.8 h46.5)]
                            Secondary Icon [inactive godot(x894.1 y552.5 w44.4 h59.2)]
                            Main Icon [godot(x988.3 y552.5 w65.0 h46.5)]
                            Individual rating value [txt=555 godot(x1053.3 y552.5 w56.6 h46.5)]
          TrophiesWindow [inactive godot(x367.0 y189.0 w1554.0 h890.8)]
            CurrentActiveBadge Name [txt=Featured: Trophy Name godot(x598.4 y217.4 w895.1 h49.8)]
              CurrentActiveBadge Count [txt=45 Trophies Achieved! godot(x597.9 y267.6 w906.5 h51.1)]
            CurrentActiveBadge [godot(x414.0 y204.9 w166.0 h155.7)]
              Frame [godot(x414.0 y204.9 w166.0 h155.7)]
              Badge [godot(x414.0 y204.9 w166.0 h155.7)]
            Divisor line Trophies [godot(x331.1 y376.7 w1589.0 h3.7)]
            Scroll Rect [godot(x367.0 y378.5 w1554.0 h701.3)]
              Item Drawer [godot(x367.0 y378.5 w1554.0 h377.0)]
                TrophyDisplay [godot(x377.0 y401.5 w298.0 h354.0)]
                  Collectable Highlight [inactive godot(x345.9 y360.1 w360.5 h426.8)]
                  bg [godot(x377.0 y401.5 w298.0 h354.0)]
                  BadgeDrawer [godot(x411.0 y408.5 w230.0 h230.0)]
                    Frame [godot(x411.0 y408.5 w230.0 h230.0)]
                    Badge [godot(x411.0 y408.5 w230.0 h230.0)]
                  title [txt=Trophy Name  godot(x400.9 y638.5 w249.1 h40.8)]
                  Progress [godot(x402.0 y700.6 w248.0 h25.4)]
                    ProgressBar [godot(x400.7 y684.4 w249.3 h47.6)]
                      Background [godot(x400.7 y693.9 w249.3 h28.6)]
                        Fill Area [godot(x400.7 y696.4 w249.3 h23.6)]
                          Fill [godot(x400.7 y696.4 w0.0 h23.6)]
                            end [godot(x377.0 y693.3 w29.4 h31.8)]
                      Outline [godot(x400.7 y693.9 w249.3 h28.6)]
                      counter [txt=100/200 godot(x414.6 y696.4 w224.0 h25.5)]
          ChatPreview [godot(x1479.8 y109.8 w400.0 h60.0)]
            Container [godot(x1479.5 y109.8 w372.3 h60.0)]
              Message Preview [godot(x1494.5 y112.8 w357.3 h27.0)]
                text [txt=<color=#00FF20>Player Name:</color> Mess godot(x1494.5 y112.8 w327.3 h27.0)]
              Message Preview (1) [godot(x1494.5 y139.8 w357.3 h27.0)]
                text [txt=<color=#00FF20>Player Name:</color> Mess godot(x1494.5 y139.8 w327.3 h27.0)]
            Button [godot(x1815.8 y106.5 w68.0 h66.5)]
      Friends Tab [inactive godot(x167.2 y70.9 w1752.8 h1009.1)]
        Header [godot(x332.2 y70.9 w1752.8 h229.6)]
          Find players panel [godot(x357.4 y147.1 w743.5 h109.4)]
            Search Field [godot(x398.8 y173.4 w526.6 h56.9)]
              Text Area [godot(x403.3 y173.4 w482.1 h56.9)]
                Placeholder [txt=Enter player name godot(x403.3 y173.4 w482.1 h56.9)]
                Text [txt=​ godot(x403.3 y173.4 w482.1 h56.9)]
            Add Friend Button [godot(x953.1 y167.6 w80.0 h68.4)]
              Icon [godot(x966.5 y169.4 w53.3 h64.9)]
            Instant duel Button [godot(x1045.7 y167.6 w80.0 h68.4)]
              Icon [godot(x1062.6 y170.3 w46.2 h63.1)]
            Search Player [txt=Search player godot(x382.4 y125.6 w695.4 h53.4)]
        Friends List [godot(x332.2 y254.3 w1587.8 h825.8)]
          Friends Title [txt=Your friends: godot(x383.4 y261.3 w695.5 h53.5)]
          Divisor line [godot(x343.1 y311.1 w1555.8 h3.7)]
          Friends Container [godot(x332.2 y314.8 w1543.6 h765.3)]
            Viewport [godot(x332.2 y314.8 w1543.6 h765.3)]
              Content [godot(x332.2 y314.8 w1543.6 h7.3)]
    Shadow (1) [inactive godot(x330.4 y70.9 w49.4 h1009.1)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Social Submenu Variant | ✅ `scripts\main_menu.gd:985 ## 社交按钮: 好友界面 (原版 Social Submenu Variant, 本地好友); scripts\social.gd:2 ## 社交界面 (原版 Social Submenu Variant 说` |
| Content Area | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\rewards.gd:145` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Tab Buttons | ✅ `scripts\collection.gd:150 # ---- Tab Buttons (原版 [167.2,158.6 165x921.4] 左竖排 4 tab — RectTransform_-1995773233925987627) ----; scr` |
| Alliances Tab Button | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Friends Tab Button | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| TabButtonLabel | ✅ `scripts\collection.gd:280 lb.add_theme_color_override("font_color", Color(1, 1, 1))   # 原版 TabButtonLabel 白; scripts\deck_collecti` |
| Badge Highlight | ✅ `scripts\collection.gd:285 # 角标 (原版 Badge Highlight 40K_notification_number 35x35 右上:; scripts\deck_collection.gd:293 # 角标 (原版 Badg` |
| OneText | ⚠️ 未命中 |
| Shadow | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:2759 # 悬浮` |
| Tabs | ✅ `scripts\shop.gd:163 # 3 个标签页 (Tabs 区 x330-1920)` |
| Alliances Tab | ✅ `scripts\social.gd:154 # ---------------- 联盟页 (说明书 Social Submenu Alliances Tab) ----------------` |
| AllianceNotMemberVariant | ⚠️ 未命中 |
| Alliance Header Buttons | ⚠️ 未命中 |
| Divisor line | ⚠️ 未命中 |
| Tab buttons | ⚠️ 未命中 |
| Generic Tab UI Button Search | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Tab UI Button Create | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| List View | ⚠️ 未命中 |
| Search Field | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Generic Round Button Variant | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| List Area | ⚠️ 未命中 |
| Invitations | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| List | ✅ `scripts\deck_builder.gd:433 # 卡组列表 (原版 Deck List drawer [0,366 325x644] Scroll View; 存引用供视图切换显隐); scripts\deck_builder.gd:923 ## 视` |
| Invitation List Entry | ⚠️ 未命中 |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| BadgeDrawer | ✅ `scripts\social.gd:169 # 徽章 (BadgeDrawer 251x235)` |
| Frame | ✅ `scripts\battle.gd:70 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:71 co` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Region | ⚠️ 未命中 |
| Members Header | ⚠️ 未命中 |
| Member Count | ⚠️ 未命中 |
| Ranking Header | ⚠️ 未命中 |
| Ranking Score | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Ranking Value | ⚠️ 未命中 |
| raycastTarget | ⚠️ 未命中 |
| Join | ✅ `scripts\draft.gd:719 var no_ally := _mk(layer, "Join an Alliance for extra Rewards", Vector2(1536, 420), Vector2(340, 241; scripts` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Reject | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Invitation List Entry (1) | ⚠️ 未命中 |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| BadgeDrawer | ✅ `scripts\social.gd:169 # 徽章 (BadgeDrawer 251x235)` |
| Frame | ✅ `scripts\battle.gd:70 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:71 co` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Region | ⚠️ 未命中 |
| Members Header | ⚠️ 未命中 |
| Member Count | ⚠️ 未命中 |
| Ranking Header | ⚠️ 未命中 |
| Ranking Score | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Ranking Value | ⚠️ 未命中 |
| raycastTarget | ⚠️ 未命中 |
| Join | ✅ `scripts\draft.gd:719 var no_ally := _mk(layer, "Join an Alliance for extra Rewards", Vector2(1536, 420), Vector2(340, 241; scripts` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Reject | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Open Alliances | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| List | ✅ `scripts\deck_builder.gd:433 # 卡组列表 (原版 Deck List drawer [0,366 325x644] Scroll View; 存引用供视图切换显隐); scripts\deck_builder.gd:923 ## 视` |
| Entry | ✅ `scripts\draft.gd:219 var free := _mk_btn(layer, Vector2(968, 707), Vector2(170, 62), "Free Entry", func():; scripts\rewards.gd:3 #` |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| BadgeDrawer | ✅ `scripts\social.gd:169 # 徽章 (BadgeDrawer 251x235)` |
| Frame | ✅ `scripts\battle.gd:70 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:71 co` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Region | ⚠️ 未命中 |
| Members Header | ⚠️ 未命中 |
| Member Count | ⚠️ 未命中 |
| Ranking Header | ⚠️ 未命中 |
| Ranking | ✅ `scripts\player_profile.gd:37 const TEX_ADMIRAL := "res://assets/ui/ranked/04-Admiral.png"        # Ranking 中央段位图; scripts\player_p` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Ranking Value | ⚠️ 未命中 |
| raycastTarget | ⚠️ 未命中 |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Create Alliance View | ⚠️ 未命中 |
| TopAnchor | ⚠️ 未命中 |
| Name input title | ⚠️ 未命中 |
| Name Input | ✅ `scripts\choose_name.gd:8 const TEX_INPUT := SPR + "40K_dropdown_bg.png"              # Choose Name Input Field 底; scripts\choose_n` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Desc input title | ⚠️ 未命中 |
| Desc Input | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Create Alliance Text | ⚠️ 未命中 |
| Price Display Button | ✅ `scripts\gacha.gd:216 # 开箱价格按钮 (说明书 Price Display Button [385,794 429x110]: Open Chest Button + 门票 icon + '1'); scripts\packs.gd:23` |
| Generic UI Button | ✅ `scripts\quests.gd:433 # Collect 按钮 (原版 Generic UI Button 256x75)` |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Price Display | ✅ `scripts\card_displayer.gd:601 ## 购买原版样式: 扣金币 (原版 Price Display 54px '300,00' — 2026-08-21 实现购买流); scripts\gacha.gd:216 # 开箱价格按钮 (说` |
| icon | ✅ `scripts\achievements.gd:16 const TEX_CAMPAIGN := SPR + "40K_genearl_icon_Campaign points_big.png"; scripts\achievements.gd:135 # 底` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Select Language | ✅ `scripts\battle.gd:2350 ## Music/Sound Effects/Voice-overs 三滑杆 + Mute opponent 开关 + Select Language 下拉 + Resign 300×90` |
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
| Select Privacy | ⚠️ 未命中 |
| Privacy Dropdown | ⚠️ 未命中 |
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
| GeneralDetails | ✅ `scripts\social.gd:157 # 左: 联盟详情卡 (原版 GeneralDetails x[331.2,1920] y[188.8,1080] 1589x891)` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| DEBUG_TEXTS | ⚠️ 未命中 |
| BadgeDrawer | ✅ `scripts\social.gd:169 # 徽章 (BadgeDrawer 251x235)` |
| Frame | ✅ `scripts\battle.gd:70 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:71 co` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Alliance name text | ⚠️ 未命中 |
| Alliance Rating Display | ✅ `scripts\player_profile.gd:1227 # Alliance Rating Display 行 (rank 图标 + 40px 数字); scripts\player_profile.gd:1362 # Alliance Rating D` |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Draft Rating Display | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Config fields | ⚠️ 未命中 |
| extra_info | ⚠️ 未命中 |
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
| Privacy Dropdown | ⚠️ 未命中 |
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
| Edit button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Confirm button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Cancel button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Description input text | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| description text | ⚠️ 未命中 |
| Divisor line members | ⚠️ 未命中 |
| MemberList | ⚠️ 未命中 |
| members label | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Alliance Member Entry | ✅ `scripts\social.gd:181 # 成员列表 (原版 Alliance Member Entry 行); scripts\social.gd:308 ## 成员行 (说明书 Alliance Member Entry: 序号+头像+在线状态+名字+` |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| member index | ⚠️ 未命中 |
| Avatar Item Small | ✅ `scripts\battle.gd:1727 # Avatar Item Small x[-19,136] y[12,149] 156×137; ShowCemeteryBtn 64² x[52,116] y[136,200]; scripts\battle.` |
| Raycast Target | ⚠️ 未命中 |
| Image Container | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Avatar Name | ⚠️ 未命中 |
| connection status | ⚠️ 未命中 |
| member name | ⚠️ 未命中 |
| member role | ⚠️ 未命中 |
| Ratings | ⚠️ 未命中 |
| Draft Rating | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Ranked Rating | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| AllianceMemberVariant | ⚠️ 未命中 |
| Alliance Header Buttons (1) | ⚠️ 未命中 |
| Divisor line | ⚠️ 未命中 |
| Tab buttons | ⚠️ 未命中 |
| Generic Tab UI Button Info | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Tab UI Button Trophies | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| GeneralDetails | ✅ `scripts\social.gd:157 # 左: 联盟详情卡 (原版 GeneralDetails x[331.2,1920] y[188.8,1080] 1589x891)` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| DEBUG_TEXTS | ⚠️ 未命中 |
| BadgeDrawer | ✅ `scripts\social.gd:169 # 徽章 (BadgeDrawer 251x235)` |
| Frame | ✅ `scripts\battle.gd:70 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:71 co` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Alliance name text | ⚠️ 未命中 |
| Alliance Rating Display | ✅ `scripts\player_profile.gd:1227 # Alliance Rating Display 行 (rank 图标 + 40px 数字); scripts\player_profile.gd:1362 # Alliance Rating D` |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Draft Rating Display | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Config fields | ⚠️ 未命中 |
| extra_info | ⚠️ 未命中 |
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
| Privacy Dropdown | ⚠️ 未命中 |
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
| Edit button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Confirm button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Cancel button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Description input text | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| description text | ⚠️ 未命中 |
| Divisor line members | ⚠️ 未命中 |
| MemberList | ⚠️ 未命中 |
| members label | ⚠️ 未命中 |
| Scroll View | ✅ `scripts\collection.gd:156 # ---- 网格 (原版 CardsTab Scroll View [330.2,155.9 1589.8x924.1] 直达右缘 — RectTransform_30349758856354782; sc` |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Alliance Member Entry | ✅ `scripts\social.gd:181 # 成员列表 (原版 Alliance Member Entry 行); scripts\social.gd:308 ## 成员行 (说明书 Alliance Member Entry: 序号+头像+在线状态+名字+` |
| background | ✅ `scripts\battle.gd:83 const TEX_AVATAR_RING := BATTLE_UI + "UI_Button_Round_background.png"  # 头像金属圆环 237² (中心透明); scripts\card_dis` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| member index | ⚠️ 未命中 |
| Avatar Item Small | ✅ `scripts\battle.gd:1727 # Avatar Item Small x[-19,136] y[12,149] 156×137; ShowCemeteryBtn 64² x[52,116] y[136,200]; scripts\battle.` |
| Raycast Target | ⚠️ 未命中 |
| Image Container | ⚠️ 未命中 |
| Highlight | ✅ `scripts\battle.gd:42 const CARD_HL_W := 4.0 * CARD2D_KX   # Card Highlight And Shadow 4x4 (canvas 单位); scripts\battle.gd:465 var h` |
| Border | ✅ `scripts\deck_builder.gd:1454 # 卡行底 9-slice (原版 40k_deck_cardlist_bg 318x54 m_Border=(150,0,150,0) — 2026-08-23 修正:; scripts\deck_b` |
| Image | ✅ `scripts\achievements.gd:186 ## 成就容器 (原版 Achievement Container 520x150: Image 130 + 标题/描述 + 进度条 + 奖励); scripts\achievements.gd:205 ` |
| Avatar Name | ⚠️ 未命中 |
| connection status | ⚠️ 未命中 |
| member name | ⚠️ 未命中 |
| member role | ⚠️ 未命中 |
| Ratings | ⚠️ 未命中 |
| Draft Rating | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| Ranked Rating | ⚠️ 未命中 |
| Secondary Icon | ⚠️ 未命中 |
| Main Icon | ✅ `scripts\draft_expiring_popup.gd:5 ##   Alliance Name + Alliance Skull Count (Main Icon) + Crate Image 'x10' +; scripts\draft_expir` |
| Individual rating value | ⚠️ 未命中 |
| TrophiesWindow | ⚠️ 未命中 |
| CurrentActiveBadge Name | ⚠️ 未命中 |
| CurrentActiveBadge Count | ⚠️ 未命中 |
| CurrentActiveBadge | ⚠️ 未命中 |
| Frame | ✅ `scripts\battle.gd:70 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:71 co` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| Divisor line Trophies | ⚠️ 未命中 |
| Scroll Rect | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\give_feedback_popup.gd:70 # ` |
| Item Drawer | ✅ `scripts\player_profile.gd:533 # 原版 Item Drawer: GridLayoutGroup cellSize 180x180 spacing(25,50) padding(left 13, top 40)` |
| TrophyDisplay | ⚠️ 未命中 |
| Collectable Highlight | ⚠️ 未命中 |
| bg | ✅ `scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type Toggle: button_bg 底 + 文字, 无独立 icon); scripts\achievements.gd:198 var bg :=` |
| BadgeDrawer | ✅ `scripts\social.gd:169 # 徽章 (BadgeDrawer 251x235)` |
| Frame | ✅ `scripts\battle.gd:70 const TEX_PLAYER_FRAME := BATTLE_UI + "UI_Player_Frame.png"            # 玩家框 442×146; scripts\battle.gd:71 co` |
| Badge | ✅ `scripts\card_displayer.gd:149 # CardUI 覆盖层 (原版 CardUI 组合: Card Ready For Level Up / New Card Badge / Ban Icon —; scripts\card_disp` |
| title | ✅ `scripts\achievements.gd:189 var title := str(a[1]); scripts\achievements.gd:226 # 标题 (原版 title)` |
| Progress | ✅ `scripts\deck_builder.gd:523 var bar := TextureProgressBar.new(); scripts\deck_builder.gd:565 (_cost_bars[i] as TextureProgressBar)` |
| ProgressBar | ✅ `scripts\deck_builder.gd:523 var bar := TextureProgressBar.new(); scripts\deck_builder.gd:565 (_cost_bars[i] as TextureProgressBar)` |
| Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\achievements.gd:110 # 背景 (原版 Menu` |
| Fill Area | ⚠️ 未命中 |
| Fill | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\card_displayer.gd:26 const TEX_OCTAGON := UI_D` |
| end | ✅ `scripts\achievements.gd:1 extends Control; scripts\achievements.gd:32 ["upgrade_legendary", "Legendary Forger", "Upgrade 3 Legenda` |
| Outline | ⚠️ 未命中 |
| counter | ✅ `scripts\achievements.gd:231 # 进度条 (原版 Slider: Background + Fill + counter); scripts\achievements.gd:249 # 进度数字 + 奖励点数 (原版 counter ` |
| ChatPreview | ✅ `scripts\main_menu.gd:6 ##   ③ Safe area Only Horizontal: Navigation Panel / ChatPreview / Upper bar(顶栏)/ 3 个 Holder / 弹窗层; scripts` |
| Container | ✅ `scripts\achievements.gd:2 ## 成就界面 (原版 Achievements Tab 说明书: 类型筛选按钮 + Achievement Container 520x150 网格); scripts\achievements.gd:41` |
| Message Preview | ✅ `scripts\main_menu.gd:673 ##   Container 372.3x60(条底 Closed-Chat_background)+ Message Preview + Button 68x66.5(聊天图标); scripts\main_` |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Message Preview (1) | ⚠️ 未命中 |
| text | ✅ `scripts\achievements.gd:132 b.text = str(f[1]); scripts\achievements.gd:137 sb.texture = load(TEX_TAB_BG)` |
| Button | ✅ `scripts\achievements.gd:11 const TEX_BTN := SPR + "UI_Button_Mulligan.png"; scripts\achievements.gd:127 var b := Button.new()` |
| Friends Tab | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Find players panel | ⚠️ 未命中 |
| Search Field | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Add Friend Button | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Instant duel Button | ⚠️ 未命中 |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Search Player | ⚠️ 未命中 |
| Friends List | ⚠️ 未命中 |
| Friends Title | ⚠️ 未命中 |
| Divisor line | ⚠️ 未命中 |
| Friends Container | ⚠️ 未命中 |
| Viewport | ✅ `scripts\deck_builder.gd:230 # 原版 Scroll View Viewport 透明 (2026-08-21 专项审查: 此前右偏 3.8px + 多余半透明底); scripts\gacha.gd:288 # 物品池 (原版 Re` |
| Content | ✅ `scripts\deck_builder.gd:96 # 背景: 原版 Deck Editing Menu Background m_Sprite=0 无贴图 (纯色, Content Area 透出场景底) —; scripts\deck_info_popu` |
| Shadow (1) | ✅ `scripts\collection.gd:219 # 右缘阴影 (原版 Shadow (1) [330.4,70.9 49.4x1009.1] 黑 0.47 — 2026-08-21 审查修正 0.31)` |

## 摘要

- 规格元素: 372
- 代码命中: 210
- ⚠️未命中: 162 (以下需人工判断)

- `Alliances Tab Button`
- `OneText`
- `Friends Tab Button`
- `OneText`
- `AllianceNotMemberVariant`
- `Alliance Header Buttons`
- `Divisor line`
- `Tab buttons`
- `Generic Tab UI Button Search`
- `Generic Tab UI Button Create`
- `List View`
- `Search Field`
- `Generic Round Button Variant`
- `List Area`
- `Invitations`
- `Invitation List Entry`
- `Region`
- `Members Header`
- `Member Count`
- `Ranking Header`
- `Ranking Score`
- `Ranking Value`
- `raycastTarget`
- `Reject`
- `Invitation List Entry (1)`
- `Region`
- `Members Header`
- `Member Count`
- `Ranking Header`
- `Ranking Score`
- `Ranking Value`
- `raycastTarget`
- `Reject`
- `Open Alliances`
- `Region`
- `Members Header`
- `Member Count`
- `Ranking Header`
- `Ranking Value`
- `raycastTarget`
- `Create Alliance View`
- `TopAnchor`
- `Name input title`
- `Desc input title`
- `Desc Input`
- `Create Alliance Text`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `Select Privacy`
- `Privacy Dropdown`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `DEBUG_TEXTS`
- `Alliance name text`
- `Secondary Icon`
- `Individual rating value`
- `Draft Rating Display`
- `Secondary Icon`
- `Individual rating value`
- `Config fields`
- `extra_info`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `Privacy Dropdown`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `Edit button`
- `Confirm button`
- `Cancel button`
- `Description input text`
- `description text`
- `Divisor line members`
- `MemberList`
- `members label`
- `member index`
- `Raycast Target`
- `Image Container`
- `Avatar Name`
- `connection status`
- `member name`
- `member role`
- `Ratings`
- `Draft Rating`
- `Secondary Icon`
- `Individual rating value`
- `Ranked Rating`
- `Secondary Icon`
- `Individual rating value`
- `AllianceMemberVariant`
- `Alliance Header Buttons (1)`
- `Divisor line`
- `Tab buttons`
- `Generic Tab UI Button Info`
- `Generic Tab UI Button Trophies`
- `DEBUG_TEXTS`
- `Alliance name text`
- `Secondary Icon`
- `Individual rating value`
- `Draft Rating Display`
- `Secondary Icon`
- `Individual rating value`
- `Config fields`
- `extra_info`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `Privacy Dropdown`
- `Item Background`
- `Item Checkmark`
- `Item Label`
- `Sliding Area`
- `Edit button`
- `Confirm button`
- `Cancel button`
- `Description input text`
- `description text`
- `Divisor line members`
- `MemberList`
- `members label`
- `member index`
- `Raycast Target`
- `Image Container`
- `Avatar Name`
- `connection status`
- `member name`
- `member role`
- `Ratings`
- `Draft Rating`
- `Secondary Icon`
- `Individual rating value`
- `Ranked Rating`
- `Secondary Icon`
- `Individual rating value`
- `TrophiesWindow`
- `CurrentActiveBadge Name`
- `CurrentActiveBadge Count`
- `CurrentActiveBadge`
- `Divisor line Trophies`
- `TrophyDisplay`
- `Collectable Highlight`
- `Fill Area`
- `Outline`
- `Message Preview (1)`
- `Friends Tab`
- `Find players panel`
- `Search Field`
- `Add Friend Button`
- `Instant duel Button`
- `Search Player`
- `Friends List`
- `Friends Title`
- `Divisor line`
- `Friends Container`