# UI 规格审计: Give Feedback Popup menu

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 09:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Give Feedback Popup menu [godot(x0.5 y-31.8 w1919.0 h1079.0)]
  Menu Dark Background [godot(x-1327.3 y-778.5 w4574.6 h2572.3)]
  Window [godot(x-155.5 y38.6 w2231.0 h937.1)]
    Generic Popup Background [godot(x38.0 y38.6 w1825.0 h996.9)]
      Mask [godot(x48.4 y48.0 w1804.7 h977.7)]
        Background fill [sprite=40k_popup_texture godot(x48.4 y48.0 w1804.7 h977.7)]
    Title [txt=Give us your feedback! godot(x105.1 y75.2 w1605.8 h77.9)]
    Subtitle [txt=It takes less than two minutes to help u godot(x105.1 y153.1 w1605.8 h40.2)]
    Submit button [godot(x720.6 y909.2 w478.3 h75.0)]
      Button Text [txt=Submit godot(x733.3 y908.6 w452.3 h75.0)]
    Generic Close Button [godot(x1816.5 y10.7 w75.0 h75.0)]
      Icon [godot(x1825.8 y21.0 w56.4 h54.5)]
    Free feedback [inactive godot(x293.8 y640.6 w1332.4 h230.0)]
      Input field [godot(x400.5 y640.6 w1119.0 h252.7)]
        Text Area [godot(x410.5 y647.6 w1099.0 h239.7)]
          Placeholder [txt=Enter text... godot(x410.5 y647.6 w1099.0 h239.7)]
          Text [txt=​ godot(x410.5 y647.6 w1099.0 h239.7)]
        Input Field title [txt=Let us know your comments and feedback godot(x400.5 y579.7 w1119.0 h60.9)]
        Character Counter [txt=280/500 godot(x1407.9 y603.2 w111.6 h37.4)]
    Scroll Rect [godot(x70.9 y211.6 w1765.5 h673.7)]
      Questions container [godot(x86.4 y211.6 w1745.0 h0.0)]
        Section 1 [godot(x86.4 y211.6 w0.0 h0.0)]
          S1Q1 [godot(x86.4 y-55.7 w0.0 h534.6)]
            Header [godot(x86.4 y478.9 w0.0 h0.0)]
              Title (1) [txt=Your age group: godot(x86.4 y478.9 w0.0 h0.0)]
              Subtitle [godot(x86.4 y478.9 w0.0 h0.0)]
            Questions List [godot(x86.4 y478.9 w0.0 h0.0)]
              Checkbox [godot(x86.4 y441.1 w0.0 h75.6)]
                Toggle [godot(x86.4 y516.7 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y516.7 w0.0 h0.0)]
                Label [txt=CCG (e.g. Marvel Snap, Hearthstone, ...) godot(x86.4 y516.7 w0.0 h0.0)]
              Checkbox (1) [godot(x86.4 y441.1 w0.0 h75.6)]
                Toggle [godot(x86.4 y516.7 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y516.7 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y516.7 w0.0 h0.0)]
              Checkbox (2) [godot(x86.4 y441.1 w0.0 h75.6)]
                Toggle [godot(x86.4 y516.7 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y516.7 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y516.7 w0.0 h0.0)]
              Checkbox (3) [godot(x86.4 y441.1 w0.0 h75.6)]
                Toggle [godot(x86.4 y516.7 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y516.7 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y516.7 w0.0 h0.0)]
              Checkbox (4) [godot(x86.4 y441.1 w0.0 h75.6)]
                Toggle [godot(x86.4 y516.7 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y516.7 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y516.7 w0.0 h0.0)]
        Section 2 [godot(x86.4 y211.6 w0.0 h0.0)]
          S2Q1 Header [godot(x86.4 y176.6 w0.0 h70.0)]
            Question [txt=How easy was it to get into Warpforge wh godot(x86.4 y246.6 w0.0 h0.0)]
            Subtitle [txt=(1 = Very easy, 5 = Very difficult) godot(x86.4 y246.6 w0.0 h0.0)]
          S2Q1 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [inactive txt=...a sense of relatedness \n(spending tim godot(x86.4 y180.5 w644.5 h62.3)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S2Q2 Header [godot(x86.4 y163.6 w0.0 h96.0)]
            Title (1) [txt=How familiar are you with Warhammer 40,0 godot(x-476.5 y259.6 w1125.7 h0.0)]
            Subtitle [txt=(1 = Not familiar at all, 5 = Extremely  godot(x-157.7 y259.6 w488.2 h0.0)]
          S2Q2 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [inactive txt=...a sense of excitement \n(adrenaline ru godot(x86.4 y180.5 w495.7 h62.3)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S2Q3 [godot(x86.4 y-311.8 w0.0 h1046.8)]
            Header [godot(x86.4 y735.0 w0.0 h0.0)]
              Title (1) [txt=What games genre are you currently playi godot(x86.4 y735.0 w0.0 h0.0)]
              Subtitle [godot(x86.4 y735.0 w0.0 h0.0)]
            Questions List [godot(x86.4 y735.0 w0.0 h0.0)]
              Checkbox [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (1) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (2) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (3) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (4) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (5) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (6) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (7) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (8) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (9) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
              Checkbox (10) [godot(x86.4 y697.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y772.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y772.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y772.8 w0.0 h0.0)]
          S2Q4 [godot(x86.4 y48.0 w0.0 h327.2)]
            Header [godot(x86.4 y375.2 w0.0 h0.0)]
              Title (1) [txt=What do you like and dislike about Warpf godot(x86.4 y375.2 w0.0 h0.0)]
              Subtitle [godot(x86.4 y375.2 w0.0 h0.0)]
            Text Area [godot(x86.4 y375.2 w0.0 h0.0)]
              Text Area [godot(x96.4 y382.2 w-20.0 h-13.0)]
                Placeholder [inactive txt=Enter text... godot(x96.4 y382.2 w-20.0 h-13.0)]
                description text [txt=\n​ godot(x96.4 y382.2 w-20.0 h-13.0)]
        Section 3 [godot(x86.4 y211.6 w0.0 h0.0)]
          S3 Header [godot(x86.4 y176.6 w0.0 h70.0)]
            Title (1) [txt=When I am playing Warpforge, I'm looking godot(x86.4 y246.6 w0.0 h0.0)]
            Subtitle [txt=(1 = Strongly disagree, 5 = Strongly agr godot(x86.4 y246.6 w0.0 h0.0)]
          S3Q1 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of relatedness (spending time godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q2 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of excitement (adrenaline rus godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q3 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of competition (climbing the  godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q4 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of achievement (getting all c godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q5 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of progression (optimizing th godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q6 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of mastery (seeking difficult godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q7 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of escapism (relaxing while p godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q8 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of immersion (learning about  godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q9 [godot(x86.4 y180.5 w0.0 h62.3)]
            Question title [txt=...a sense of freedom (choosing what and godot(x86.4 y242.8 w0.0 h0.0)]
            Button Container [godot(x86.4 y242.8 w0.0 h0.0)]
          S3Q10 [godot(x86.4 y-22.8 w0.0 h468.8)]
            Header [godot(x86.4 y446.0 w0.0 h0.0)]
              Title (1) [txt=Do you consider Warpforge more of a: godot(x86.4 y446.0 w0.0 h0.0)]
              Subtitle [godot(x86.4 y446.0 w0.0 h0.0)]
            Questions List [godot(x86.4 y446.0 w0.0 h0.0)]
              Checkbox [godot(x86.4 y408.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y483.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y483.8 w0.0 h0.0)]
                Label [txt=CCG (e.g. Marvel Snap, Hearthstone, ...) godot(x86.4 y483.8 w0.0 h0.0)]
              Checkbox (1) [godot(x86.4 y408.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y483.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y483.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y483.8 w0.0 h0.0)]
              Checkbox (2) [godot(x86.4 y408.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y483.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y483.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y483.8 w0.0 h0.0)]
              Checkbox (3) [godot(x86.4 y408.2 w0.0 h75.6)]
                Toggle [godot(x86.4 y483.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y483.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y483.8 w0.0 h0.0)]
        Section 4 [godot(x86.4 y211.6 w0.0 h0.0)]
          S4Q1 [godot(x86.4 y77.6 w0.0 h268.1)]
            Header [godot(x86.4 y345.7 w0.0 h0.0)]
              Title (1) [txt=Have you ever stopped playing Warpforge  godot(x86.4 y345.7 w0.0 h0.0)]
              Subtitle [godot(x86.4 y345.7 w0.0 h0.0)]
            Questions List [godot(x86.4 y345.7 w0.0 h0.0)]
              Checkbox [godot(x86.4 y307.9 w0.0 h75.6)]
                Toggle [godot(x86.4 y383.5 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y383.5 w0.0 h0.0)]
                Label [txt=CCG (e.g. Marvel Snap, Hearthstone, ...) godot(x86.4 y383.5 w0.0 h0.0)]
              Checkbox (1) [godot(x86.4 y307.9 w0.0 h75.6)]
                Toggle [godot(x86.4 y383.5 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y383.5 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y383.5 w0.0 h0.0)]
          S4Q2 [godot(x86.4 y-89.0 w0.0 h601.2)]
            Header [godot(x86.4 y512.2 w0.0 h0.0)]
              Title (1) [txt=What made you stop playing? (Select all  godot(x86.4 y512.2 w0.0 h0.0)]
              Subtitle [godot(x86.4 y512.2 w0.0 h0.0)]
            Questions List [godot(x86.4 y512.2 w0.0 h0.0)]
              Checkbox [godot(x86.4 y474.4 w0.0 h75.7)]
                Toggle [godot(x86.4 y550.1 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y550.1 w0.0 h0.0)]
                Label [txt=CCG (e.g. Marvel Snap, Hearthstone, ...) godot(x86.4 y550.1 w0.0 h0.0)]
              Checkbox (1) [godot(x86.4 y474.4 w0.0 h75.7)]
                Toggle [godot(x86.4 y550.1 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y550.1 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y550.1 w0.0 h0.0)]
              Checkbox (2) [godot(x86.4 y474.4 w0.0 h75.7)]
                Toggle [godot(x86.4 y550.1 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y550.1 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y550.1 w0.0 h0.0)]
              Checkbox (3) [godot(x86.4 y474.4 w0.0 h75.7)]
                Toggle [godot(x86.4 y550.1 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y550.1 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y550.1 w0.0 h0.0)]
              Checkbox (4) [godot(x86.4 y474.4 w0.0 h75.7)]
                Toggle [godot(x86.4 y550.1 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y550.1 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y550.1 w0.0 h0.0)]
              Checkbox (5) [godot(x86.4 y474.4 w0.0 h75.7)]
                Toggle [godot(x86.4 y550.1 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y550.1 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y550.1 w0.0 h0.0)]
          S4Q2_Extra [godot(x86.4 y48.0 w0.0 h327.2)]
            Header [godot(x86.4 y375.2 w0.0 h0.0)]
              Title (1) [txt=Other godot(x86.4 y375.2 w0.0 h0.0)]
              Subtitle [godot(x86.4 y375.2 w0.0 h0.0)]
            Text Area [godot(x86.4 y375.2 w0.0 h0.0)]
              Text Area [godot(x96.4 y382.2 w-20.0 h-13.0)]
                Placeholder [inactive txt=Enter text... godot(x96.4 y382.2 w-20.0 h-13.0)]
                description text [txt=\n​ godot(x96.4 y382.2 w-20.0 h-13.0)]
          S4Q3 [godot(x86.4 y-95.4 w0.0 h614.1)]
            Header [godot(x86.4 y518.7 w0.0 h0.0)]
              Title (1) [txt=What made you return? (Select all that a godot(x86.4 y518.7 w0.0 h0.0)]
              Subtitle [godot(x86.4 y518.7 w0.0 h0.0)]
            Questions List [godot(x86.4 y518.7 w0.0 h0.0)]
              Checkbox [godot(x86.4 y480.8 w0.0 h75.7)]
                Toggle [godot(x86.4 y556.5 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y556.5 w0.0 h0.0)]
                Label [txt=CCG (e.g. Marvel Snap, Hearthstone, ...) godot(x86.4 y556.5 w0.0 h0.0)]
              Checkbox (1) [godot(x86.4 y480.8 w0.0 h75.7)]
                Toggle [godot(x86.4 y556.5 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y556.5 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y556.5 w0.0 h0.0)]
              Checkbox (2) [godot(x86.4 y480.8 w0.0 h75.7)]
                Toggle [godot(x86.4 y556.5 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y556.5 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y556.5 w0.0 h0.0)]
              Checkbox (3) [godot(x86.4 y480.8 w0.0 h75.7)]
                Toggle [godot(x86.4 y556.5 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y556.5 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y556.5 w0.0 h0.0)]
              Checkbox (4) [godot(x86.4 y480.8 w0.0 h75.7)]
                Toggle [godot(x86.4 y556.5 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y556.5 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y556.5 w0.0 h0.0)]
              Checkbox (5) [godot(x86.4 y480.8 w0.0 h75.7)]
                Toggle [godot(x86.4 y556.5 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y556.5 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y556.5 w0.0 h0.0)]
          S4Q3_Extra [godot(x86.4 y48.0 w0.0 h327.2)]
            Header [godot(x86.4 y375.2 w0.0 h0.0)]
              Title (1) [txt=Other godot(x86.4 y375.2 w0.0 h0.0)]
              Subtitle [godot(x86.4 y375.2 w0.0 h0.0)]
            Text Area [godot(x86.4 y375.2 w0.0 h0.0)]
              Text Area [godot(x96.4 y382.2 w-20.0 h-13.0)]
                Placeholder [inactive txt=Enter text... godot(x96.4 y382.2 w-20.0 h-13.0)]
                description text [txt=\n​ godot(x96.4 y382.2 w-20.0 h-13.0)]
          S4Q4 [godot(x86.4 y-155.7 w0.0 h734.7)]
            Header [godot(x86.4 y579.0 w0.0 h0.0)]
              Title (1) [txt=What would you like to receive when retu godot(x86.4 y579.0 w0.0 h0.0)]
              Subtitle [godot(x86.4 y579.0 w0.0 h0.0)]
            Questions List [godot(x86.4 y579.0 w0.0 h0.0)]
              Checkbox [godot(x86.4 y541.1 w0.0 h75.7)]
                Toggle [godot(x86.4 y616.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y616.8 w0.0 h0.0)]
                Label [txt=CCG (e.g. Marvel Snap, Hearthstone, ...) godot(x86.4 y616.8 w0.0 h0.0)]
              Checkbox (1) [godot(x86.4 y541.1 w0.0 h75.7)]
                Toggle [godot(x86.4 y616.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y616.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y616.8 w0.0 h0.0)]
              Checkbox (2) [godot(x86.4 y541.1 w0.0 h75.7)]
                Toggle [godot(x86.4 y616.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y616.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y616.8 w0.0 h0.0)]
              Checkbox (3) [godot(x86.4 y541.1 w0.0 h75.7)]
                Toggle [godot(x86.4 y616.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y616.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y616.8 w0.0 h0.0)]
              Checkbox (4) [godot(x86.4 y541.1 w0.0 h75.7)]
                Toggle [godot(x86.4 y616.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y616.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y616.8 w0.0 h0.0)]
              Checkbox (5) [godot(x86.4 y541.1 w0.0 h75.7)]
                Toggle [godot(x86.4 y616.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y616.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y616.8 w0.0 h0.0)]
              Checkbox (6) [godot(x86.4 y541.1 w0.0 h75.7)]
                Toggle [godot(x86.4 y616.8 w0.0 h0.0)]
                  CheckMark [godot(x86.4 y616.8 w0.0 h0.0)]
                Label [txt=Select Language godot(x86.4 y616.8 w0.0 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Give Feedback Popup menu | ✅ `scripts\give_feedback_popup.gd:2 ## 反馈问卷弹窗 (原版 Give Feedback Popup menu [8609] 说明书):` |
| Menu Dark Background | ✅ `scripts\achievements.gd:110 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\campaign.gd:94 # 背景 (原版 Menu Dark` |
| Window | ✅ `scripts\base_event_popup.gd:3 ##   Generic Window Red Background Big [443,146 1053x733] +; scripts\base_event_popup.gd:40 # 红窗 (原版` |
| Generic Popup Background | ✅ `scripts\choose_name.gd:7 const TEX_POPUP := SPR + "40k_popup.png"                    # Generic Popup Background; scripts\give_feed` |
| Mask | ✅ `scripts\draft.gd:360 # Packs Mask 红窗底 (先建, 避免盖住标题; 说明书 5230836453799319039); scripts\gacha.gd:146 ## 左区 Chest panel (说明书 [57,0 108` |
| Background fill | ⚠️ 未命中 |
| Title | ✅ `scripts\base_event_popup.gd:4 ##   Event image [282,34 859x859] + Texts [1005,190 450x580] (Title/Description/'Clique para continu` |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Submit button | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:405 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Generic Close Button | ✅ `scripts\booster_info_popup.gd:146 # 关闭按钮 (原版 Generic Close Button Orange); scripts\deck_info_popup.gd:212 # 关闭按钮 (原版 Generic Close` |
| Icon | ✅ `scripts\achievements.gd:15 const TEX_GOLD := SPR + "40K_Icon_Discount_Gold.png"; scripts\battle.gd:1848 # 敌方能量 (holder 顶部): Card F` |
| Free feedback | ✅ `scripts\give_feedback_popup.gd:5 ##   Free feedback 输入框 [294,641 1332x230] + Submit [721,909 478x75] + 关闭` |
| Input field | ⚠️ 未命中 |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| Text | ✅ `scripts\achievements.gd:131 b.flat = false   # flat=true 时 StyleBoxTexture override 不渲染 (2026-08-20 实测); scripts\achievements.gd:1` |
| Input Field title | ⚠️ 未命中 |
| Character Counter | ⚠️ 未命中 |
| Scroll Rect | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\give_feedback_popup.gd:70 # ` |
| Questions container | ⚠️ 未命中 |
| Section 1 | ⚠️ 未命中 |
| S1Q1 | ✅ `scripts\give_feedback_popup.gd:11 # 问卷定义: [节标题, 选项数组] — 2026-08-21 换原版问卷题面 (S1Q1 单选; S2Q1/Q2 1-5 量表;` |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Questions List | ⚠️ 未命中 |
| Checkbox | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\settings.gd:197 # 3 个开关 (原版 ` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (1) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (2) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (3) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (4) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Section 2 | ⚠️ 未命中 |
| S2Q1 Header | ⚠️ 未命中 |
| Question | ✅ `scripts\settings.gd:407 _make_label(page, "Questions about the game? View the FAQ", Vector2(90, 149), Vector2(942, 85), 18, ` |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| S2Q1 | ✅ `scripts\give_feedback_popup.gd:11 # 问卷定义: [节标题, 选项数组] — 2026-08-21 换原版问卷题面 (S1Q1 单选; S2Q1/Q2 1-5 量表;` |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S2Q2 Header | ⚠️ 未命中 |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| S2Q2 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S2Q3 | ✅ `scripts\give_feedback_popup.gd:12 # S2Q3 原版多选(选最多3), 现有 CheckButton 单选结构 → 按节适配; S4Q1 自由文本 = 下方输入框)` |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Questions List | ⚠️ 未命中 |
| Checkbox | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\settings.gd:197 # 3 个开关 (原版 ` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (1) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (2) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (3) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (4) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (5) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (6) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (7) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (8) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (9) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (10) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| S2Q4 | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| description text | ⚠️ 未命中 |
| Section 3 | ⚠️ 未命中 |
| S3 Header | ⚠️ 未命中 |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| S3Q1 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q2 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q3 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q4 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q5 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q6 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q7 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q8 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q9 | ⚠️ 未命中 |
| Question title | ⚠️ 未命中 |
| Button Container | ⚠️ 未命中 |
| S3Q10 | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Questions List | ⚠️ 未命中 |
| Checkbox | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\settings.gd:197 # 3 个开关 (原版 ` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (1) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (2) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (3) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Section 4 | ⚠️ 未命中 |
| S4Q1 | ✅ `scripts\give_feedback_popup.gd:12 # S2Q3 原版多选(选最多3), 现有 CheckButton 单选结构 → 按节适配; S4Q1 自由文本 = 下方输入框); scripts\give_feedback_popup.g` |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Questions List | ⚠️ 未命中 |
| Checkbox | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\settings.gd:197 # 3 个开关 (原版 ` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (1) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| S4Q2 | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Questions List | ⚠️ 未命中 |
| Checkbox | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\settings.gd:197 # 3 个开关 (原版 ` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (1) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (2) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (3) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (4) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (5) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| S4Q2_Extra | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| description text | ⚠️ 未命中 |
| S4Q3 | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Questions List | ⚠️ 未命中 |
| Checkbox | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\settings.gd:197 # 3 个开关 (原版 ` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (1) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (2) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (3) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (4) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (5) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| S4Q3_Extra | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Text Area | ✅ `scripts\deck_builder.gd:418 # 文字右边距留图标空间 (原版 Text Area x[10,w-10] + 图标 x[w-40,w-5] 重叠 30px — 留边避免 placeholder 被图标盖)` |
| Placeholder | ✅ `scripts\deck_builder.gd:407 # 原始 JSON RectTransform_-7700575496447594716 / Placeholder RectTransform_-764554671449313500); scripts` |
| description text | ⚠️ 未命中 |
| S4Q4 | ⚠️ 未命中 |
| Header | ✅ `scripts\battle.gd:1448 # 名字 (原版 Header Text); scripts\campaign.gd:2 ## 战役界面 (原版 Campaign Tab 说明书: Campaign Army Selector + Campaig` |
| Title (1) | ⚠️ 未命中 |
| Subtitle | ✅ `scripts\card_displayer.gd:325 lines.append("Subtitle: %s" % str(subtitle)); scripts\give_feedback_popup.gd:3 ##   Window 大窗 + Titl` |
| Questions List | ⚠️ 未命中 |
| Checkbox | ✅ `scripts\give_feedback_popup.gd:4 ##   Scroll Rect 问卷区 [71,212 1766x674] (4 节 Checkbox 选择题) +; scripts\settings.gd:197 # 3 个开关 (原版 ` |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (1) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (2) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (3) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (4) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (5) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |
| Checkbox (6) | ⚠️ 未命中 |
| Toggle | ✅ `scripts\achievements.gd:116 # 类型筛选 (原版 Achievement Type Toggle, 单机横排放顶部); scripts\achievements.gd:135 # 底图样式 (原版 Achievement Type ` |
| CheckMark | ✅ `scripts\quests.gd:280 # 4 个里程碑 (原版 Weekly Mission Milestones Step 70x70 + CheckMark + text); scripts\quests.gd:389 # 4 个里程碑 (原版 Mi` |
| Label | ✅ `scripts\achievements.gd:260 font_size: int, color: Color) -> Label:; scripts\achievements.gd:261 var lb := Label.new()` |

## 摘要

- 规格元素: 290
- 代码命中: 182
- ⚠️未命中: 108 (以下需人工判断)

- `Background fill`
- `Submit button`
- `Input field`
- `Input Field title`
- `Character Counter`
- `Questions container`
- `Section 1`
- `Title (1)`
- `Questions List`
- `Checkbox (1)`
- `Checkbox (2)`
- `Checkbox (3)`
- `Checkbox (4)`
- `Section 2`
- `S2Q1 Header`
- `Question title`
- `Button Container`
- `S2Q2 Header`
- `Title (1)`
- `S2Q2`
- `Question title`
- `Button Container`
- `Title (1)`
- `Questions List`
- `Checkbox (1)`
- `Checkbox (2)`
- `Checkbox (3)`
- `Checkbox (4)`
- `Checkbox (5)`
- `Checkbox (6)`
- `Checkbox (7)`
- `Checkbox (8)`
- `Checkbox (9)`
- `Checkbox (10)`
- `S2Q4`
- `Title (1)`
- `description text`
- `Section 3`
- `S3 Header`
- `Title (1)`
- `S3Q1`
- `Question title`
- `Button Container`
- `S3Q2`
- `Question title`
- `Button Container`
- `S3Q3`
- `Question title`
- `Button Container`
- `S3Q4`
- `Question title`
- `Button Container`
- `S3Q5`
- `Question title`
- `Button Container`
- `S3Q6`
- `Question title`
- `Button Container`
- `S3Q7`
- `Question title`
- `Button Container`
- `S3Q8`
- `Question title`
- `Button Container`
- `S3Q9`
- `Question title`
- `Button Container`
- `S3Q10`
- `Title (1)`
- `Questions List`
- `Checkbox (1)`
- `Checkbox (2)`
- `Checkbox (3)`
- `Section 4`
- `Title (1)`
- `Questions List`
- `Checkbox (1)`
- `S4Q2`
- `Title (1)`
- `Questions List`
- `Checkbox (1)`
- `Checkbox (2)`
- `Checkbox (3)`
- `Checkbox (4)`
- `Checkbox (5)`
- `S4Q2_Extra`
- `Title (1)`
- `description text`
- `S4Q3`
- `Title (1)`
- `Questions List`
- `Checkbox (1)`
- `Checkbox (2)`
- `Checkbox (3)`
- `Checkbox (4)`
- `Checkbox (5)`
- `S4Q3_Extra`
- `Title (1)`
- `description text`
- `S4Q4`
- `Title (1)`
- `Questions List`
- `Checkbox (1)`
- `Checkbox (2)`
- `Checkbox (3)`
- `Checkbox (4)`
- `Checkbox (5)`
- `Checkbox (6)`