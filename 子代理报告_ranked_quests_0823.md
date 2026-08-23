# 子代理报告: ranked & quests 界面权威规格表 (2026-08-23)

> 依据: 原始 Unity JSON (d:/2/解包整理/03_界面UI/菜单/) 完整子树 dump + chain_rect.py v2 (py312) 权威换算 (1920×1080, y 翻转)
> 坐标格式: (x1, y1) = Godot 屏幕左上角; 尺寸 w×h; 全部经 chain_rect 复核, 与 audit_B_ranked.md / audit_D_quests.md 一致
> 整理文档 (菜单全树.md / 要点块) 仅作定位索引, 与本报告冲突时以本报告 (原始 JSON + chain_rect) 为准

---

## 0. 结论速览 (主代理快速阅读)

### ranked — 原版其实有 3 个相关 prefab, 任务文件数值横跨其中 (已逐一复核):

| 任务文件数值 | chain_rect 复核结果 | 出处 |
|---|---|---|
| Back[143,904] | **(142.5, 903.7) 73.2×72.0** ✅ 字面吻合 | RankedEventWindow v1 (旧版全屏排位窗口) |
| Ranked-Unranked[832,913] | **(832.4, 913.2) 255.1×53.8** ✅ | 同上 (ChangeRankedToggle)。**注意: V2 的 toggle 在 (191.4, 868.1), 不是这个** |
| Play[1697,893] | **(1697.0, 893.1) 90×90** ✅ | 同上 (Ranked Play Mode Button, 40k_UI_bt_play) |
| No Deck + 'Create deck'[789,866 342x103] | **(789.0, 865.7) 342.0×103.0** ✅ | RankedEventWindowV2 (新版) 的 Ranked Deck Selection 内 |
| Warlord Darkening[530,418 940x558] | **(530.0, 418.2) 940.1×557.6** ✅ | RankedEventWindowV2 |
| DivisionText 'Division V' 36px | ✅ 两版都是 'Division V'; v1/standalone=36px, **V2=42px** | 任一 |
| Timer icon 33² + 'Ends in: 23d 5h' 32px | ✅ v1/standalone; **V2: icon 43.9² + 'Termina en: 23d 5h' 38px (西语)** | 任一 |
| RankImage 78² | ✅ 名义 78.2×78.2 (锚点 0.4-0.6×0.6-0.7 拉伸), 祖先累计 scale 1.08 → **画面上约 84.4** | 任一 |
| footer '4879'/'32'/'16' 全 40px | **仅 standalone (562×864) 有此组合**: '4879'40px / '32'40px / counter'16'40px。v1 面板(434×694) 的 footer 是 '4879'**90px**/'5000'**76px**/'2500'40px | 见 1.3 |
| RankedSealStep 5×100 | 名义 100×100 ("5"=运行时 5 级印章数), prefab 内静态实例 1~2 个 | standalone/V2 |

**关键决策点**: 项目 ranked.gd 当前 = "standalone 段位面板 (562×864) + V2 卡组选择器" 的混合。任务文件的 chrome (Back/Toggle/Play) 来自 v1 全屏窗口, 卡组部分 (Create deck/Warlord Darkening) 来自 V2。**建议**: 面板内部按 standalone 规格 (562×864, 含 '4879'/'32'/'16' 40px footer + RankedSealStep), chrome 按 v1 规格 (Back 143,904 / Toggle 832,913 / Play 1697,893 / Battle 条 1403,913), 卡组区按 V2 规格 (Create deck 789,866 / Warlord Darkening 530,418)。三套全表均在 1.2/1.3/1.4, 由主代理选择。

### quests — 原版结构 (已全部复核):

- 原版 = **Rewards Base Submenu Variant → Tabs → Missions Tab** (项目 quests.gd 对应它)。
- **左列** = Special Missions (Daily Login Bonus 容器 [inactive] + Daily Skulls 容器 336×555), **容器中心 (372.4, 652.1)** → 名义占位 x[204.4,540.4] y[374.6,929.6] ✅ 与任务文件"底对齐 y[374.6,929.6]"一致。
- **右列** = Daily Missions 面板: **(1271.3, 12.5) 620.1×639.3** ✅ "620 宽" — 3 条任务行 (Daily Mission Container ×3, 每行 172.5 高) + Trash mission ('X' 黄钮) + 'Available in 64h' 40px + 进度条 '52/500' 40px。
- Mission Header (标题) 在**右上**: (1274.4, 15.0) 617×60.7 — name 'Daily Missions' 36px + info 47² + Refill Counter '0 Disponible' 36px。
- Weekly Mission Holder: **(372.4, 759.8) 1519×227.5** — 项目现状 (206,691) 差 **x166 / y69** ✅。
- **重要**: Special Missions 与 Daily Missions 两个父节点均有 **m_LocalScale = 1.15** (rt_scale_map.json 证实) — 原版此区域整体放大 15%, 审计表数值已含 (子元素 373.8 宽=325×1.15)。实现时子元素直接按审计绝对坐标摆放即可。

---

## 1. ranked 原版规格

### 1.1 三个相关 prefab 的关系

| prefab | 索引行 | 尺寸 | 用途 |
|---|---|---|---|
| **RankedEventWindow** (v1) | 10169 | 0,0 1920×1080 | 排位全屏窗口(旧): Back 底左 + 段位面板 (434×694) + 右侧 Deck info 卡组详情 + Battle 条 + Ranking/Unranked toggle + 搜索弹窗 |
| **Ranked Division Info** (root) | 4920 | 105,43 562×864 | 段位信息面板独立 prefab (竖排高版, footer 含 4879/32/16 40px) — **任务文件竖排数值出处**, projected.gd 面板大小来源 |
| **RankedEventWindowV2** (V2) | 13884 | 0,0 1920×1080 | 排位全屏窗口(新): Game Mode Header + 左侧 Ranked Deck Selection (526~1394) + 中央段位面板 638×812 + 右侧 Ranked Army Selector + To Battle 'Battle!' + 搜索弹窗 |

三者的 DivisionText/Timer/RankImage/ChangeRankedToggle 文案字号略有差异 (V2 全部放大且部分西语化), 以 v1/standalone (英文版) 为复刻基准, V2 仅取"卡组选择器新增功能" (Create deck / Warlord Darkening / No Deck Text)。

### 1.2 RankedEventWindow v1 全表 (chain_rect 绝对坐标)

根: `GameObject\RankedEventWindow_-3438541305642376491.json` / `RectTransform\RectTransform_340272506660692693.json` (anchor 全拉伸)

#### 1.2.1 背景
| GO (PathID) | 绝对坐标 | 尺寸 | 内容 | 源 JSON |
|---|---|---|---|---|
| Menu Dark Background _5201405823689073365 | (0,0) | 4574.6×2572.4 | Image->? color(0,0,0,0.77) | GameObject/Menu Dark Background_5201405823689073365.json |

#### 1.2.2 Back 按钮 (任务文件 Back[143,904] ✅)
| GO | 绝对坐标 | 尺寸 | 锚点/pivot | 内容 | 父链 |
|---|---|---|---|---|---|
| Back button 1740526766187324117 | **(142.5, 903.7)** | 73.2×72.0 | (0.5,0.5)/(1.0,0.0) | Image->**40k_UI_bt_back** (PathID 218399751571532351→`12_主程序资源/Sprite/40k_UI_bt_back.json`); Button | RankedEventWindow |
| Text 9110766738230256341 | (227.1, 903.7) | 314.3×72.0 | 拉伸 (0,0,1,1) | **Text:'Back' fontsize=40** color(1,1,1,1) | (子) |

#### 1.2.3 Ranked Division Info 面板 (v1 版, 434×694 — audit_B 即此面板)
GO `Ranked Division Info_-2472178969530752299.json` / `RectTransform_8669472690379465429.json`
→ 绝对 **(251.9, 213.1) 434.3×694.4**, anchor(0.5,0.5) pivot(0.5,0.5)

| 元素 | GO PathID | 绝对坐标 | 尺寸 | 贴图/文字 (Sprite 名→解包路径) | 字号/颜色 | active |
|---|---|---|---|---|---|---|
| info | -7801220088682405163 | (259.9, 144.5) | 55.2² | 40K_generic_bt_info→`12_主程序资源/Sprite/40K_generic_bt_info.json` | — | **True** |
| LeaderboardButton | 7489668598122717909 | (323.5, 145.5) | 290.9×53.2 | UI_Button_Mulligan→`12_主程序资源/Sprite/UI_Button_Mulligan.json`; Button | — | True |
| Button Text 'Leaderboard' | 8437202167328514773 | (336.9, 150.7) | 263.3×42.8 | text 'Leaderboard' | **36px** | True |
| Generic Window Red Background Small | -5815480447584460075 | 满面板 | 0×0 拉伸 | **UI_Deck_Selection_Back**→`03_界面UI/图集/0_mainmenu/Sprite/UI_Deck_Selection_Back.json` (-2186414362693705441) | — | True |
| Content | -8121363345024769323 | (280.2, 230.0) | 377.6×622.8 | (容器) | — | True |
| ├ RankTitleBG | -296707730790964523 | (51.6, 852.8) | 457.2×0 | **40K_main_rank_display**→`12_主程序资源/Sprite/40K_main_rank_display.json` (3837025018791853890), color(1,1,1,**0.92**) | — | True |
| │ └ DivisionText | -8549781889952668971 | **(102.5, 822.8)** | 355.4×60.0 | **'Division V'** | **36px** | True |
| ├ Timer (容器) | 2535971565271425749 | — | 361.0×0 | — | — | True |
| │ ├ Timer Icon | 5646783119286248149 | **(83.2, 836.3)** | **33.0²** | **WF_icon_clock**→`03_界面UI/图集/0_mainmenu/Sprite/WF_icon_clock.json` (8552223381227235564) | — | True |
| │ └ Timer | 3327478336848306901 | **(215.8, 857.8)** | 167.6×55.9 | **'Ends in: 23d 5h'** | **32px** | True |
| ├ DivisionImage | 7799205547868332757 | (69.1, 852.8) | 422.2×0 | Image->? (容器, 运行高度由 layout 驱动) | — | True |
| │ └ **RankImage** | 1726301961322865365 | **(238.0, 861.4)** | 84.4×-8.6 | Image->**'Roman V'** 名义 78.2² (锚点 (0.4,0.6)-(0.6,0.7) 拉伸, 祖先 scale 1.08→84.4) → `03_界面UI/排位图标/Sprite/Roman V.json` (-5716310642658349672) | — | True |
| └ footer | 2888436240925827797 | (75.2, 852.8) | 410.0×0 | (容器) | — | True |
| 　 ├ Highest Faction Rating | 3136191220218962645 | (-102.5, 832.9) | 355.4×39.8 | 40K_main_rank_display | — | **False** |
| 　 │ └ Rating Text: '4879' | 8527834769690239701 | (0-size 动画态) | 0×0 | '4879' + Secondary 40k_DeckSelection_icon_FactionUM + Main 40k_UI_icon_ranked_Skirmish | **40px** | False |
| 　 ├ **FactionScoreSmall** | 266174006045418197 | (-102.5, 794.0) | 355.4×117.7 | 底 Image->? color(0.01,0,0,0.1) | — | **True** (v1 面板 footer 唯一显示块) |
| 　 │ ├ icon | 4221326266672587477 | — | 180×117.7 | 40k_DeckSelection_icon_FactionUM→`12_主程序资源/Sprite/40k_DeckSelection_icon_FactionUM.json` | — | True |
| 　 │ ├ Alliance Rating Display | -3334051620933623083 | (56.5, 806.2) | 196.4×55.8 | '4879' (**90px**, 7053613965656629973) + Secondary 40k_UI_icon_ranked_Skirmish(inactive) | 90px | True |
| 　 │ └ Alliance Rating Display (1) | 7922721881411855061 | (56.5, 862.4) | 196.4×36.4 | '5000' (**76.35px**) + Menu_Icon_Galon | 76.35px | True |
| 　 ├ MainRating | -1056601395968630059 | (87.0, 981.7) | 386.4×60.3 | 40K_main_rank_display | — | **False** |
| 　 │ ├ Mission Milestones Progress | 3374040072716985045 | (87.0, 968.6) | 355.4×86.5 | (容器) | — | False |
| 　 │ │ ├ counter | 7893891539152511701 | (91.3, 741.2) | 80.0×52.2 | **'16'** | **40px** | False |
| 　 │ │ └ steps → RankedSealStep | 3278375838598603477 | (87.0, 938.5) | 71.1×60.3 | Image->**'Rank Skull'** color(1,1,1,**0.0**)+Empty('Rank Skull Empty')+Fill('Rank Skull') → `12_主程序资源/Sprite/Rank Skull.json` (-300467167438017286)/Rank Skull Empty.json (-7214020762604782334) | — | True |
| 　 │ └ Global Rating | 6925097370890183381 | (186.0, 983.2) | 256.5×57.4 | '2500' (**40px**, -1518701518990302507) + Secondary Menu_Icon_Galon 40×57.4 + Main 40k_UI_icon_ranked_Skirmish 60×57.4 | 40px | False |

> ⚠️ 注意 v1 面板 footer 三个块 (HighestFactionRating/FactionScoreSmall/MainRating) 默认锚定在 (0,0)/(0,1) 角, 静态坐标大量为负/超界 — 这是 prefab 的**入场动画状态** (运行时动画会移到最终位置)。静态可见 footer = FactionScoreSmall 块 ('4879' 90px + '5000' 76px)。'16'/'2500' 默认隐藏。
> 若面板按 standalone 版实现 (1.3), 则 footer 为 '4879'40px + '32'40px + 里程碑'16'40px + RankedSealStep(100 名义) — 与任务文件一致。

#### 1.2.4 ChangeRankedToggle (任务文件 Ranked-Unranked[832,913] ✅)
GO `ChangeRankedToggle_8609311580852429525.json` / `RectTransform_7398693236135600853.json`
→ **(832.4, 913.2) 255.1×53.8**

| 元素 | GO | 绝对坐标 | 尺寸 | 内容 |
|---|---|---|---|---|
| ChangeRankedToggle | 8609311580852429525 | (832.4, 913.2) | 255.1×53.8 | Image->40k_menu_bt color(1,1,1,**0**) (透明底) |
| RankedText | 475005726799733461 | (1014.8, 917.6) | 256.4×48.0 | **'Ranked' 40px** |
| UnrankedText | 7019901393897169621 | (648.8, 917.6) | 256.4×48.0 | **'Unranked' 40px** |
| Image (toggle 滑块) | -2669182009714433323 | (915.5, 920.1) | 89.0×40.0 | **40_main_bt_toggle_on**→`03_界面UI/图集/0_mainmenu/Sprite/40_main_bt_toggle_on.json` |
| ChangeRankedButton | -4349729935627345195 | 满 toggle | 255.1×53.8 | 同 40k_menu_bt 透明 + Button |

#### 1.2.5 Deck info 面板 (右侧卡组详情, v1)
根: `Deck info_-3478449537383750955.json` → 中心校准后 **x[600.6,1919.5] y[43.4,907.5]** (1318.9×864.1, 锚点(0.5,0.5), pos(300.0,64.6))
- Generic Window Red Background Big 1760368540345606869: **UI_Deck_Information_Back**→`03_界面UI/图集/0_mainmenu/Sprite/UI_Deck_Information_Back.json` (5230836453799319039), 1106.3×704.1
- Character Image -1411729509011381547: 830.1² (立绘, animator 填充)
- Background Info -1157960105772735787: **UI_Deck_Information_submenu_Back**, 548.8×497.0
- Warlord Name 792665819750114005: 'Warlord name' **28px**
- Deck Name 3362278212882965205: 'DECK NAME' **30px**
- Army Image 8509479324797608661: 40k_DeckSelection_icon_FactionOrks 105.3²
- General container → Cardback 6259286289908015829 209.6×302.3; 'Card / Energy cost' **26px**; Deck Information cost drawer (158.1×199.1, 卡片数量行 Slider 40k_CardAmount_bar_bg/fill); Show Deck Content Button -5739716176579222827 64.2×63.2 (40k_UI_bt_deck)
- Deck List Drawer -6599136539171380523 569.8×619.5 (卡列表)
- ChangeDeckButton 7709122281682936533: (390.0,-308.8) rel → 'Change Deck' **36px** UI_Button_Mulligan
- ViewDeckButton 7518380733848855253: 'View Deck' **36px**

#### 1.2.6 Battle 底部条 (DeckSelectionContinueButton)
| 元素 | GO | 绝对坐标 | 尺寸 | 内容 |
|---|---|---|---|---|
| DeckSelectionContinueButton | -1452711708135873835 | (1081.1, 913.2) | 832.9×49.8 | 容器, pivot(1.0,0.0) |
| Continue Button | 6181622978244027093 | (1403.1, 913.2) | 453.1×49.8 | Image->**40k_bt_underbutton** color(**0.37,0.89,0.59**,1) + Button |
| Text 'Battle' | -132013370205166891 | (1403.3, 918.1) | 287.3×44.9 | **'Battle' 38px** |
| **Ranked Play Mode Button** | -6371155886875893035 | **(1697.0, 893.1)** | **90.0²** | Image->**40k_UI_bt_play**→`12_主程序资源/Sprite/40k_UI_bt_play.json`; Button (任务文件 Play[1697,893] ✅) |
| GameModeText | 7566555942870885077 | (1243.2, 975.1) | 445.0×50.0 | **'Game mode: Multiplayer' 35px** |

#### 1.2.7 Searching Oponent Popup (v1, 默认 **inactive**, 1919×1079)
GO `Searching Oponent Popup_-8824811068708969771.json`
- Menu Dark Background: 黑 0.77
- Window -3538592503406746923: 中心 (960, 620.0) → x[560,1360] y[394.1,845.9] 800×451.9; Generic Popup Background 40k_popup + Mask + Background fill 40k_popup_texture
- Skull -5142459746218499371: 567.3² **40K_icon_searching_skull** color(1,1,1,0.18); Cog -2751295059240115499: 40K_icon_searching_cog 0.18
- Main Search message -8141792790364052779: 'Searching' **50px**
- Generic UI Button -1200403617932336427: 'Cancel' **45px** 40K_button color(0.37,0.89,0.59,1) 478.3×75.0
- Few players online message 2616824377766290133: 'There are few players online at the moment...' **30px**

> (项目 ranked.gd 的搜索覆盖层按另一个 prefab "SearchingOpponentWindow" (索引 72) 实现: 双督军立绘 1138² 出血 + 'Searching opponent' 36px + Cancel — 本次不涉及, 保持现状。)

### 1.3 Ranked Division Info 独立 prefab (562×864 — 任务文件 竖排/32/16/4879 出处)

根: `GameObject\Ranked Division Info_-3383320362765802140.json` (m_Father=0 根) / `RectTransform_-7004980321802476188.json` → **(105.2, 43.4) 561.7×864.1** ✅ 与文档"105,43 562x864"一致

| 元素 | GO PathID | 绝对坐标 | 尺寸 | 贴图/文字 | 字号 | active |
|---|---|---|---|---|---|---|
| LeaderboardButton | 9092481377619977572 | (240.6, 72.5) | 290.9×53.2 | UI_Button_Mulligan + 'Leaderboard' | 36px | True |
| (Button Text) | 1585184718299112804 | (254.0, 78.0) | 263.3×42.8 | 'Leaderboard' | 36px | True |
| Generic Window Red Background Small | 7238771847651370340 | 满面板 | UI_Deck_Selection_Back | — | — | True |
| Content | 2927076519117694308 | (197.3, 164.1) | 377.6×622.8 | 容器 (平移 105+280.85-188.8=197.25, 43.4+432.05-292.5+18.9=164.1; 中心 = 面板中心 (386.05, 475.45) + (0,18.9)) | — | True |
| ├ RankTitleBG | -4588441716283693724 | (39.6, 748.1)* | 457.2×0 | 40K_main_rank_display color(1,1,1,0.92) — *底左锚 (Content 左下) | — | True |
| │ └ DivisionText | 3613652542100055396 | **(19.6, 738.0)** | 355.4×60.0 | **'Division V'** | **36px** | True |
| ├ Timer 容器 | 5925588763801068900 | — | 361.0×0 | — | — | True |
| │ ├ Timer Icon | -3360943639321991836 | **(0.3, 751.5)** | **33.0²** | WF_icon_clock | — | True |
| │ └ Timer | -6014156590293670556 | **(132.9, 773.0)** | 167.6×55.9 | **'Ends in: 23d 5h'** | **32px** | True |
| ├ DivisionImage | -3465093660578699932 | (17.8, 748.1)* | 390.9×0 | — | — | True |
| │ └ **RankImage** | -4317093779380591260 | **(155.1, 776.6)** | **84.4×-8.6 (名义 78², ×1.08)** | **'Roman V'** | — | True |
| └ footer | 1068302024091411812 | (-7.7, 768.0) | 410.0×0 | — | — | True |
| 　 ├ Highest Faction Rating | -8392164862930279068 | (19.6, 768.0) | 355.4×39.8 | 40K_main_rank_display | — | **False** |
| 　 │ └ '4879' (Rating Text) | 868348800040543588 | (216.0, 768.9) | 67.1×37.9 | **'4879'** (+FactionUM 60×59.2 + ranked_Skirmish 44.4×59.2) | **40px** | False |
| 　 ├ MainRating | -5837361147004803740 | (-200.9, 737.8) | 386.4×60.3 | 40K_main_rank_display | — | **True** |
| 　 │ ├ Mission Milestones Progress | -2382991840473537180 | (-200.9, 754.9) | 0×86.5 | — | — | True |
| 　 │ │ ├ counter | -5581338801583512220 | (-196.6, 527.4) | 80.0×52.2 | **'16'** | **40px** | **False** |
| 　 │ │ └ steps → RankedSealStep | 8461653276811765092 | (-200.9, 791.4) | **0×100 (名义 100²)** | Rank Skull(a0.0)/Rank Skull Empty/Rank Skull | — | True |
| 　 │ └ Global Rating | -8265965392563100316 | (-62.1, 739.3) | 216.7×57.4 | '32' | **40px** | **False** |
| 　 │ 　 └ '32' (Individual rating value) | 5952452059420927332 | (51.6, 749.0) | 33.5×37.9 | **'32'** (+ranked_Skirmish 44.4×57.4) | **40px** | False |

> 该 prefab 的静态 prefab 默认状态: HighestFactionRating(4879)/counter(16)/Global(32) 都是 inactive (动画时切入), MainRating 本体 active。任务文件的 "'4879'/'32'/'16' 全 40px" 描述即此表。

### 1.4 RankedEventWindowV2 关键元素全表 (任务文件卡组区数值出处)

根: `RankedEventWindowV2_-5324570929900320848.json` / `RectTransform_6837807522738505648.json`

| 元素 | GO PathID | 绝对坐标 | 尺寸 | 内容 |
|---|---|---|---|---|
| Reward Background Get Reward | 4908504744533395376 | 满屏 | 1920×1081.5 | **40k_general_popup_simple red** (1928446884932611385) |
| Noise | -2540193944841320528 | 满屏 | — | UI Dirt And Noise skratches color(0.31,0.13,0,0.72) |
| Menu Vignette | 2009128930916599728 | (0,27.5) | 1920×1270.2 | 黑 0.58 |
| **Ranked Deck Selection** | -5807527989194618960 | (525.3, -0.1) | **869.4×1080.2** | 中央卡组选择区 ✅ 与项目 ranked.gd 现有 [525,0] 一致 |
| ├ Warlod Image | -2390114862854010960 | (450.9, -95.1) | 1098.1² | 督军立绘 ✅ 项目 (451,-95) 一致 |
| │ └ **Warlord Darkening** | 7900782381865469872 | **(530.0, 418.2)** | **940.1×557.6** | Image->**'Smooth background square'** (1485029260898738437→`03_界面UI/去重资源/Sprite/Smooth background square.json`) color(**0,0,0,0.82**) — 任务文件 [530,418] ✅ |
| ├ Faction Icon Image | -9037412523571509328 | (972.3, 685.2 中心) | 522.6² | 阵营图标 ✅ 项目 (711,134) |
| ├ Deck Buttons ×4 | (Previous 4477837128968996784 / Change 2716152103905888176 / View -910385673344743504 / Next -765736443442985040) | **(640.85, 816.05) 起, 4 连排间距 160.9** | 160.9×128.0 ×4 | **UI_Button_Round_background** + Icon (40k_UI_bt_back / 40k_UI_bt_deck_change / 40k_bt_eye / 40k_UI_bt_back 翻转) — 项目 (641,816) 起, 间距 158, 宽 148 (应 160.9) |
| ├ Deck Name | -5390955259115239504 | — | 522.0×76.9 | 'DECK NAME HERE' **62.85px** |
| ├ Deck Warlord | -8852530313292380240 | — | 522.0×54.7 | 'WARLORD NAME' **44.65px** |
| ├ No Deck Text | 5923129373692954544 | (617.2, 685.0) | 685.7×166.5 | "'Tienes <color=#E98A00FF>{0} {1} Comandante(s)</color>, ¡comi…'" **(西语) 45px** |
| ├ **Create deck 按钮** | 2978782831094433712 | **(789.0, 865.7)** | **342.0×103.0** | Image->**UI_Button_Mulligan** + Button + 'Create deck' **55px** (8127068332485216176) — 任务文件 [789,866 342x103] ✅ |
| └ Numer Of Army Decks + Deck Quantity Icon | 1044301838075856816 / 5672268556177213360 | — | 88.8×76.9 / 67² | '1/20' **60.5px** + 40k_UI_icon_deck |
| Ranked Army Selector | -3676644275251017808 | (636.7 center→ x[323.1,950.4]... 实: anchor(1,0.5) → x1 = 960-323.3-313.65=323.1? chain 需单独 — 文档 [1283,128 627x790] 即 (1283,128) 627.3×789.7 | 627.3×789.7 | Factions Title 'Factions' **45.87px** + Army Selector Viewport 547.1×663.1 |
| Game Mode Header With Back Button | 6954516072760969136 | (0, 40.9) 顶左 | 550×109.5 | Header Background **WF_Campaign_Info_Background** (6473405944757030420); Window Title 'Game mode' **67.55px**; **Header Back Button** -6873468868321769552 167.9×111.3 **UI_Button_Menu_Back** (218399751571532351) |
| **Ranked Division Info (V2)** | 2414930959176796080 | **(0.0, 146.9)** | **638.0×812.1** | 大号段位面板 (V2 变体) |
| ├ Rank Title | -3543011042255796304 | (58.0, 161.3) | 522.0×54.7 | **'Rank' 57.7px** |
| ├ info | 5484638253501876144 | (605.6, 397.6 中心) | 55.2² | 40K_generic_bt_info | **inactive** |
| ├ LeaderboardButton | -438005176617171024 | (140.5, 966.0) | 357.1×74.8 | 'Leaderboard' 36px |
| ├ Content | -3369813056631634000 | — | 507.9×663.8 | — |
| │ ├ DivisionText | 7570943522211792816 | — | 355.4×68.0 | 'Division V' **42px** |
| │ ├ DivisionImage → RankImage | 3509417057607255984 → 3746912248135190448 | — | 539.8×572.6 → 78² | 'Roman V' |
| │ └ footer → MainRating | -1511393920980777040 | — | 410.0×67.8 | 40K_main_rank_display, **active**; MMP: Background 40K_main_rank_display a0.65, counter '16' 40px inactive, steps 2× RankedSealStep 100 名义, Legendary Ratings: Position '#' 66.6px + '2' 45px (inactive), Global '152' 45px + **WF_UI_Trophy_Gold** 55×57.4 (inactive); HighestFactionRating('4879' 45px, inactive) + FactionScoreSmall('4879' 90px+'5000' 76.35px, inactive) |
| ├ Timer Icon / Timer | 2198739989953677232 / -1616443368984377424 | — | 43.9² / 248.4×55.9 | WF_icon_clock / **'Termina en: 23d 5h' 38px (西语)** |
| ├ ChangeRankedToggle | -502879902723766352 | **(191.4, 868.1)** | 255.1×53.8 | RankedText 'Ranked' 45px (415.1,868.1), UnrankedText 'Unranked' 45px (12.3,868.1), Image 40_main_bt_toggle_on 89×40 |
| **To Battle Button** | 522930913867433904 | **(1376.8, 917.8)** | **440.3×120.6** | UI_Button_Mulligan + **'Battle!' 74.25px** + ShieldIcon UI_icon_shield 100² + TrophyIcon 40k_ranking_icon_trophy Plus 100² |
| Searching Oponent Popup (1) | 5686493648261187504 | — | 1919×1079 | 同 1.2.7 (inactive) |
| Help Button | -6094820477392287824 | (1827.9, 35.4) | 65.1² (scale 0.74) | 40K_generic_bt_info + Button (V2 右上帮助) |

### 1.5 排位罗马图标资源
`解包整理/03_界面UI/排位图标/Sprite/Roman I.json ... Roman VI.json` + `Texture2D/Roman I.png ... Roman VI.png` (Division V → Roman V; 06-Galactic Threat/07-Legend 是 Legendary 图标)
项目已用 `res://assets/ui/ranked/Roman %s.png` (ranked.gd:480) ✅

---

## 2. quests 原版规格 (Rewards Base Submenu Variant → Missions Tab)

根: `GameObject\Rewards Base Submenu Variant_-8343312282719283457.json` (1920×1080 全屏), 内含左侧 Tab Buttons (Missions/Campaign/Forge/Booster Packs 竖排导航 — 项目由 NavBuilder "REWARDS" 承担) 与 Tabs → Missions Tab。

### 2.1 外层结构 (chain_rect 绝对)

| 元素 | GO PathID | 绝对坐标 | 尺寸 | scale | 备注 |
|---|---|---|---|---|---|
| **Missions Tab** | -3261567823877957889 | (166.7, 69.2) | 1753.3×1010.8 | 1 | 内容区 (导航条 0-166.7 之外) |
| ├ **Normal Missions** | -1180275796818061569 | (372.4, 95.8) | **1519.0×723.8** | 1 | 左+右两列总区 |
| │ ├ **Special Missions** | 8671611484050626303 | (372.4, 12.4) | 896.1×639.7 | **1.15** | 左列 (Daily Login + Daily Skulls) |
| │ │ ├ Daily Login Container | -3916738376757274881 | (372.4, 652.1) | 0×0 (layout) | 1.15 | **m_IsActive=False** (默认隐藏; 背景 40K_missions_display_Daily vertical) |
| │ │ └ **Daily Skulls Mission Container** | 7706541736523601663 | 中心 **(372.4, 652.1)** | 名义 **336×555** → 含 scale 约 386.4×638.3 | 1.15 | ⭐主容器 (细节 2.2) |
| │ └ **Daily Missions** (右列) | 5064257774696273663 | **(1271.3, 12.5)** | **620.1×639.3** | **1.15** | ⭐右侧任务面板 (细节 2.3) |
| │ 　 ├ Daily Missions Holder | 3523712292682602239 | (1271.3, 75.1) | 620.1×576.7 | 1.15 | 3 行任务容器 |
| │ 　 └ Mission Header | -2637473773048293633 | **(1274.4, 15.0)** | 617.0×60.7 | 1.15 | 面板标题条 (细节 2.4) |
| └ **Weekly Mission Holder** | 7218257402582079231 | **(372.4, 759.8)** | **1519.0×227.5** | 1 | ⭐周常条 (细节 2.5) |

> **1.15 scale 证实**: rt_scale_map.json: `-3954402248558504193` (Special Missions) = {x:1.15,y:1.15}, `4921620045776164607` (Daily Missions) = {x:1.15,y:1.15}。原版此两区整体 ×1.15 放大 — 审计/下表所有子元素尺寸均已含。

### 2.2 Daily Skulls Mission Container 全表 (左列主容器; GO 7706541736523601663)

名义占位: 中心 (372.4, 652.1) → **x[204.4,540.4] y[374.6,929.6]** (336×555, 任务文件 ✅ "左 Daily Skulls 容器 336x555 底对齐 y[374.6,929.6]")。
绘制尺寸含 scale: 约 386.4×638.3 → x[179.2,565.6] y[333.0,971.2]。
以下子元素为 chain_rect 绝对 (已含 1.15; 审计表一致):

| 元素 | GO PathID | 绝对坐标 | 尺寸 | 贴图/文字 | 字号 | active | 父链 |
|---|---|---|---|---|---|---|---|
| background | 5778909478831855359 | 满容器 | 306.7×0 (layout) | **40K_missions_display_Daily vertical**→`03_界面UI/图集/Sprite/40K_missions_display_Daily vertical.json` | — | True | container |
| header | 9196678919644452607 | — | — | — | — | True | background |
| ├ name | 3977510389831440127 | (375.4, 656.2) | (layout) | **'Daily Skulls'** | **36px** | True | header |
| └ info | 4563713717731006207 | (313.7, 661.4) | 47.2² | 40K_generic_bt_info | — | True | header |
| body | -1084580059607001345 | (185.5, 404.4) | 373.7×263.3 | 图标区 | — | True | background |
| ├ description | 794261466947131135 | — | — | Text:'' 30px | 30px | True | body |
| ├ Image (小骷髅图标) | 4936055337281132287 | (185.5, 397.2) | 76.1×74.4 | **40K_missions_icon_Daily skulls**→`03_界面UI/图集/Sprite/40K_missions_icon_Daily skulls.json` | — | True | body |
| ├ counter | 1448179826786244351 | (243.3, 428.9) | 78.1×36.6 | **'x160000'** | **30px** | True | body |
| └ image (大骷髅) | -787083600429836545 | (261.6, 422.0) | 255.0×263.3 | 40K_missions_icon_Daily skulls | — | True | body |
| progress | 3561008042681505535 | (185.5, 637.9) | 373.7×84.7 | 里程碑带 | — | True | background |
| └ milestones → steps → **Mission Milestones Step ×5** | 8606354798897141503 → -7057516715192936705 → -885246227177007361 等 | (162.5, 699.6) 起 | **46.0² (名义 40×40 ×1.15)** | holder 黑底 + CheckMark **40K_settings_icon_checkmark** + text '1' **42.2px** | 42.2px | True | progress |
| footer | -4419199459216582913 | (183.7, 724.4) | 373.8×209.2 | 奖励+Collect | — | True | background |
| ├ Rewards ×2 | 6309506554898355967 | (183.7, 724.4) | — | Reward Display Mission: Icon Campaign Points Drawer Variant (40K_genearl_icon_Campaign points_big + Drawer 2000/24 hours) + count **'200'/'100' 40px** | 40px | True | footer |
| ├ **Generic UI Button (Collect)** | 261096784261945087 | **(227.1, 813.7)** | **294.4×85.8 (名义 256×74.6 ×1.15)** | Image->**40K_button** color(**1.0,0.47,0.1**,1) + Button + **'Collect' 44px** | **44px** | True | footer |
| └ TimerHolder → Timer | 5001287283522868991 / 3431862689130157823 | (183.7, 899.5) | 373.8×65.7 | **'Resets in 12h 34 m'** | **38px** | True | footer |
| (debug_buttons) | -8830901318168471809 | — | — | Reset/Re-Roll/+1/+5/Complete/00:00 — **DEBUG 专用, 不实现** | — | True | background |

### 2.3 Daily Missions 右侧面板 (3 条任务行) 全表

Daily Missions (1271.3, 12.5) 620.1×639.3 → 右缘 **1891.4**; Daily Missions Holder (1271.3, 75.1) 620.1×576.7。
**3 行 Daily Mission Container** (`-1689853150408665345` / `4933302183333467903` / `-7898691639256960327` 等): 每行名义 150×... ×1.15 → **172.5 高**, 由 VerticalLayoutGroup 在 Holder 内顶起排布。行内 (rel 到行, 距行左缘/右缘; 行宽取 Holder 620.1):

| 元素 | GO | 行内布局 (raw→×1.15) | 内容 |
|---|---|---|---|
| 行底 | -1689853150408665345 | 620.1×172.5 (运行时) | Image->**40K_missions_display_Daily horizontal**→`03_界面UI/图集/Sprite/40K_missions_display_Daily horizontal.json` color(**0.49,0.57,0.92**,1) |
| Rewards (左) | 7360476496196736767 | 左起 0..145.3 (126.3×150 ×1.15) | Reward Display Mission Vertical Variant: Campaign Glow(40K_genearl_icon_Campaign points_big) + Converted Drawer(2000,65px)/Ephemeral(24 hours,65px)/AlreadyOwned(75px) + count **'100' 40px** |
| Separator Line | 8136099825001961215 | 绝对 (1409.8, 567.3) 1.8×169.0 | 竖分隔线 color(0.25,0.25,0.41,0.59), 行左缘 +138.5 处 |
| title (inactive) | 1825327262567569151 | 文本区 | 'Deal 500 damage to enemy units' **30px** | **m_IsActive=False** |
| description | -2588369643904231681 | 文本区 | 'Deal 500 damage to enemy units' **40px** |
| timer | -226965837893593345 | 文本区 | **'Available in 64h' 40px** |
| Mission Milestones Progress Bar | 7745735966228158207 | 文本区下方 | Progress Bar: Background 40k_generial_bar_empty color(1,0.59,0) + Fill 40k_generial_bar_fill color(1,0.77,0.33) + progress **'52/500' 40px** |
| **Generic UI Button (Collect)** | -3800356798300678401 | 右底: 右缘 -313.5 处 (绝对 (957.8,658.7)→运行时右对齐 ≈(1577.9 中心)) | 254.6×56.5 ×1.15=292.8×64.9, 40K_button color(**1.0,0.53,0.0**,1), **'Collect' 44px** |
| **Trash mission** | 703899705255204607 | 右底: 右缘 -353.5 处 (≈Trash 在 Collect 左侧 40px) | **49.1×49.4 ×1.15=56.5×56.8**, Image->**40k_general_bt_yellow** color(1,0.77,0.33,1) + 'X' **30px**(inactive) + **40k_general_bt_yellow_delete**; Button |
| Mission Debug Buttons | -4665265858557831425 | — | 调试按钮, 不实现 |

**行内文本区域绝对值** (layout 态参考): name/description/timer 位于 x≈1428.5 起 (即行左缘+157)。'Available in 64h' 于左上 (1428.5, 580.1) 附近, 与实际布局"行上缘"一致 (行1 顶 ≈ y75.1)。**实现建议: 行内右侧按钮对 (Trash+Collect) 底右对齐, 行右缘 1891.4; Rewards 块 145.3 宽居左; 其余文本区 157..380; 分隔线 x1409.8。** (行间实际 y 排布以 Holder 顶为基准, 每行 172.5 高, 任务文件"3 条任务行+Trash+Available in 64h"吻合。)

### 2.4 Mission Header (右上标题条)

| 元素 | GO | 绝对坐标 | 尺寸 | 内容 |
|---|---|---|---|---|
| Mission Header | -2637473773048293633 | (1274.4, 15.0) | 617.0×60.7 | 标题条 (Image->? 白 1,1,1) |
| ├ name | 1489701787785893631 | (1292.9, 16.6) | 499.8×57.5 | **'Daily Missions' 36px** |
| ├ info | -1632138551327058177 | (1844.2, 21.8) | 47.1² | 40K_generic_bt_info |
| └ Refill Counter | 2315493933018060543 | (1274.4, 16.6) | 555.1×57.5 | **'0 Disponible' 36px** (西语原文; 无英文实例, 按 m_text 保留或本地化)**

### 2.5 Weekly Mission Holder 全表

| 元素 | GO | 绝对坐标 | 尺寸 | 内容 |
|---|---|---|---|---|
| Weekly Mission Holder | 7218257402582079231 | **(372.4, 759.8)** | **1519.0×227.5** | 周常条 (与 Normal Missions 同 x 起) |
| background | -5938319942889433345 | 满 holder | — | **40K_missions_display_Weekly**→`03_界面UI/图集/Sprite/40K_missions_display_Weekly.json` |
| ├ name | 3987398106967840511 | (383.8, 762.3) | 307.6×50.0 | **'Weekly Challenge' 36px** |
| ├ info | 6618834839397996287 | (701.1, 766.8) | 41.0² (×1.0) | 40K_generic_bt_info — 注意: 周常条**无 1.15 scale** (41² 不放大) |
| ├ body (inactive) | 5370696486117250815 | (1539.4, 765.6) | 325.0×94.2 | Image->40K_missions_icon_Daily skulls + desc (隐藏) |
| ├ progress | 8282266981546137343 | (412.5, 794.2) | 1068.4×158.6 | 进度区 |
| │ ├ Mission Progress Bar | — | (442.5, 871.8) | 1008.4×22.7 | 40k_generial_bar_empty/fill + Handle + counter **'13/15'** (Handle 容器内, 40px?) — 审计: counter (414.4,898.0) 62.6×35.1 |
| │ └ steps → **Weekly Mission Milestones Step (3) ×4** | 7700881246602401535 等 | (377.5, 927.0) 起, 4 连排 | **70.0²** | 石(镜像 40k_missions_milestone_off) + **CheckMark 节点=40k_Crate_Tier1_Iron 72.9×59.1 (奖励箱图标, Button)** + text **'5' 50px** |
| └ footer | — | (1563.7, 851.8) | 300.7×102.1 | 奖励+Collect |
| 　 ├ Rewards ×4 (inactive) | — | (485.6, 926.0) 起 每 250 宽 | 250.0×113.1 | Reward Display Mission (Campaign 图标 + count 200/100) |
| 　 ├ **Generic UI Button (Collect)** | — | (1570.1, 865.5) | 294.3×74.7 | 'Collect' **44px** 40K_button — color 未标注 (同面板为 (1,0.47,0.1)) |
| 　 └ TimerHolder | — | (1563.7, 964.2) | 300.7×57.1 | **'Ends in 12h 34 m' 38px** |

> 周常条完整子树在 dump 行 329-425 (`Rewards Base Submenu Variant` 内), 里程碑石图标 GO 为 Weekly Mission Milestones Step (3) — 步骤 5/10/15/20 对应文本 '5'(42px 级)。审计表有 Steps (3) 四份 (audit 命名 Bug, 实为 4 个不同 PathID)。

---

## 3. 项目现有实现差异清单

### 3.1 ranked.gd (742 行) — 逐元素 原版 vs 现状

| 原版元素 | 原版规格 | ranked.gd 现状 | 判定 |
|---|---|---|---|
| 面板底 UI_Deck_Selection_Back 562×864 @(105,43) | (105.2,43.4) 562×864 | panel @(167,43) 562×864 (+62 人为右移) | ⚠️ 位置自创 (+62 无原版依据; 原版面板本体在 105,43, v1 面板是 434×694@(251.9,213.1)) |
| **Current Rank 标题** | **原版无此元素** (原版面板顶部=LeaderboardButton) | `_make_label "Current Rank" (167,60) 26px` (ranked.gd:106) | ❌ **自创, 删** |
| **40K_main_rank_display 横幅 (460×64 @217,120)** | 原版 40K_main_rank_display 只用于 RankTitleBG (段位名下底, 457×0 layout) & footer 块, 不在顶部横放 | `rank_disp (217,120) 460×64` (ranked.gd:107-114) | ❌ **自创摆放, 删** (保留贴图但按原版用途) |
| LeaderboardButton | 独立 prefab: (240.6,72.5) 291×53 @面板顶 / v1 面板: (323.5,145.5) | (303,73) 291×53 (+62) | ⚠️ 位置 +62; 若按 standalone 则回 (240.6,72.5) |
| _division_icon (Roman) | DivisionImage→RankImage 78²(84.4 含 1.08) @ (155.1,776.6) standalone / (238.0,861.4) v1 | (317,128) 60×60 | ❌ 位置尺寸错误 (60² vs 78², y 差 650px——原版在图下方 776 处) |
| _division_label 'Division V' | (19.6,738.0) 355×60 **36px** / v1 (102.5,822.8) | (372,120) 260×64 36px | ❌ 错位 (y 差 618) |
| **Ranked score 标签** | **原版无** (footer '4879'/'32' 40px + '16' 40px 里程碑 + RankedSealStep) | `_rating_label "Ranked score: %d" (167,200) 22px` (ranked.gd:126) | ❌ **自创, 删** → 换原版 footer |
| Timer icon 33² + 32px | (0.3,751.5) 33² / (132.9,773.0) 167.6×55.9 32px | (277,258) 33² / (320,246) 300×56 32px | ⚠️ 文字/字号对, 位置差 ~745px y; 需放回 footer 上方原位置 |
| tooltip info 钮 | 原版面板有 info (55.2² 40K_generic_bt_info; v1 active @(259.9,144.5)) | tip_btn (532,258) 48² | ⚠️ 自创 Tooltip 文案 + 位置; 原版有 info 钮但位 (259.9,144.5) 且为 Tooltip 挂点 (V2 的 Rank Title 旁) — 保留功能, 移位置 |
| **Start Ranked 按钮 (450×68 @222,700)** | **原版无** → 原版 = DeckSelectionContinueButton: Continue 'Battle' 38px @(1403.1,913.2) 453.1×49.8 (40k_bt_underbutton 绿 0.37,0.89,0.59) + **Play 圆钮 90² 40k_UI_bt_play @(1697.0,893.1)** | `_rank_btn "Start Ranked" (222,700) 450×68` (ranked.gd:159-175) | ❌ **自创, 删** → 按原版 Battle 条 |
| Back 按钮 | (142.5,903.7) 73.2×72 40k_UI_bt_back + 'Back' 40px | **无** | ❌ **缺, 加** |
| ChangeRankedToggle | (832.4,913.2) 255.1×53.8 (Ranked/Unranked 40px + 40_main_bt_toggle_on 89×40) | **无** | ❌ **缺, 加** |
| Footer (4879/32/16 40px + RankedSealStep) | 见 1.3 | **无** (只有一个 22px 'Ranked score') | ❌ **缺, 加** (含 inactive 动画态可先静态显示或按 prefab 默认) |
| Deck 区 (V2) | Faction Icon 523²@(711,134)/Warlord 1098²@(451,-95)/4 钮/名 34px/计数 | 已按 V2 实现 (525,0 869×1080) | ✅ 结构在; 差异: ①无 Warlord Darkening (530,418 940×558 黑 0.82) ②无 No Deck Text + Create deck 按钮 (789,866 342×103, 'Create deck' 55px) ③4 圆钮宽 148/间距 158 vs 原版 160.9×128/间距 160.9 (起点 (640.85,816.05) vs 项目 (641,816) ✅基本对) ④文案 'NO DECK' vs 原版 'Tienes...Comandante' (西语) |
| GameModeText | 'Game mode: Multiplayer' 35px @(1243.2,975.1) | **无** | ❌ 缺 (Battle 条下) |
| 搜索弹窗 | RankedEventWindow 自带 Searching Oponent Popup (Skull/Cog/'Searching'/'Cancel'/'There are few players online'); 项目实现的是另一个 prefab (双立绘) | 已有 (SearchingOpponentWindow 版) | ⚠️ 保持现状可 (不同 prefab, 功能等价); 若要完全复刻此窗口则换 v1 版 |

### 3.2 quests.gd (642 行) — 逐元素 原版 vs 现状

| 原版元素 | 原版规格 | quests.gd 现状 | 判定 |
|---|---|---|---|
| Daily Skulls 容器 | **1 个**, 中心 (372.4,652.1), 336×555, y[374.6,929.6] | **3 个并排** x=206+i*400, y=95.8, 336×555 (顶部对齐) | ❌ **结构错误** — 原版左列只有 1 个容器 (另 2 个 "Path of Victory"/"Collector" 是自创); 应 1 容器放 (204.4,374.6), 另两条变"Daily Missions 右列 3 行" |
| Daily Login Bonus 容器 | 有 (Special Missions 第 1 项, inactive); body 325×261/图标 40K_missions_icon_login bonus/进度 52/500/Collect(1,0.47,0.1) | **无** | ⚠️ 可选实现 (默认 inactive, 可跳过; 若做则作左列第 2 容器) |
| Daily Missions 右列面板 | (1271.3,12.5) 620.1×639.3, 3 行 (172.5 高) + Trash + 'Available in 64h' 40px + '52/500' 40px | **无** (3 容器横排代替) | ❌ **缺, 加** |
| Mission Header 右上 | (1274.4,15.0): name 'Daily Missions' 36px + info 41² + Refill '0 Disponible' 36px | "Missions" (1274,98) 400×53 **44px 金色** | ❌ 文字/字号/位置错 (原 'Daily Missions' 36px @y15) |
| **自创 Campaign 按钮** | 原版 = 左侧 Tab Buttons (NavBuilder REWARDS 负责); 任务界面内**无** Campaign 按钮 | camp_btn (1274,152) 200×44 | ❌ **自创入口** (若 NavBuilder 已含 Campaign Tab 则删) |
| **自创 Achievements 按钮** | 原版任务界面内无 | ach_btn (1484,152) 200×44 | ❌ **自创入口** (同理) |
| **自创辉光** | 无 (原版辉光属活动容器) | glow (1452,74) 256×88 脉动 | ❌ 自创 (依附 campaign 入口, 随其删) |
| **自创小字副标题** | 无 | "Daily Missions · reset daily · progress from real matches" (240,60) 16px | ❌ 自创, 删 |
| 金币显示 (1530,14) | 原版 Rewards Base Submenu 顶部是否有? — 原版此界面未见金币栏 (金币在全局 topbar 由主菜单提供) | 自建 gold_bg+icon+label | ⚠️ 自创; 核对主菜单是否已全局有金币显示, 若有则删 |
| 周常条 | (372.4,759.8) 1519×227.5 (与 Normal Missions 同 x 起) | box (206,691) 1519×228 | ❌ 差 x166 / y69 (任务文件 ✅ 指出) |
| 周常 header | 'Weekly Challenge' **36px** @(383.8,762.3) + info 41²@(701.1,766.8) | 'Weekly Challenge' 22px @(226,703) 相对 + info 34²@(654,709) | ❌ 字号/位置 (36px; 绝对 383.8,762.3) |
| 周常进度条 | (442.5,871.8) 1008.4×22.7 + counter '13/15' + 4×里程碑 **70²** | bar (406,841) 1008×23 相对 | ⚠️ 位置 y 差; 里程碑 70² 已用 ✅; counter '13/15' vs 实际 "wins/20" 暂自定 |
| 周常锚点 Collect | (1570.1,865.5) 294.3×74.7 'Collect' 44px | (1446,773) 160×60 20px | ❌ 尺寸/字号差异 |
| 周常 TimerHolder | 'Ends in 12h 34 m' 38px @(1563.7,964.2) | **无** | ❌ 缺 |
| 每日容器 header | name **36px** + info 41² (绝对容器 y 顶 -0; x..) | name 20px (12,10) + info 34² (282,12) | ❌ 字号/位置 |
| body | 原版: Image 76.1×74.4 (小骷髅) + counter 'x160000' 30px + 大骷髅 255×263 | icon 60² (14,60) + desc 15px (14,118) | ❌ 结构/字号; 原版无 desc 文字行, 有 x160000 计数 |
| 里程碑 | 5× 46² (40×40×1.15) + CheckMark 40K_settings_icon_checkmark + text '1' 42.2px | 4× 40² + 自绘 stone (TEX_MILESTONE_ON/OFF) + num 22px | ❌ **5 个** vs **4 个**; 原版底色黑 Image(0,0,0,1) + check; text 42.2px |
| Rewards | Reward Display Mission (Campaign 图标 1080 内容 + count 40px) | _make_reward_display 140×78 图标 64² + 'x' 18px | ⚠️ 尺寸/字号差异; 原版 count 40px |
| Collect | (227.1,813.7) 294.4×85.8 (256×74.6×1.15) 40K_button (1,0.47,0.1) 'Collect' 44px | (40,370) 256×75 40K_button 橙 ✅ 'Collect' 22px | ⚠️ 颜色已修 ✅; 字号 44px; 位置按容器内 |
| TimerHolder | 'Resets in 12h 34 m' 38px | reset_lbl 15px (16,460) | ❌ 字号 38px |
| 进度条 | 40k_generial_bar_empty/fill; 原版在 progress 区 373.8×84.7 (含 5 里程碑), 无独立大进度条在底部 | bar_bg (16,505) 304×14 + fill | ⚠️ 自创位置 (原版无 505 底部条; 原版进度表现=里程碑带) |

> quests.gd 的 "wins"/"collect" 两任务内容原版没有对应容器 — 原版左列 = Daily Login (隐藏) + Daily Skulls, 右列 = 3 条 Daily Mission 行 (内容为动态生成的任务描述+Trash+Available in 64h)。项目可保留自己的任务内容 (wins/collect 等自定任务), 只是**容器形态/位置按原版**: 每日骷髅放左单容器, 其余任务进右列 3 行。

---

## 4. 实施建议

### 4.1 ranked 重排

1. **删** (ranked.gd): ① "Current Rank" 标签 (106-106) ② rank_disp 40K_main_rank_display 横幅 (107-114) ③ "Ranked score" 标签 (126-127) ④ "Start Ranked" 按钮 (158-175)。
2. **面板**: 保持 562×864 独立 prefab 结构 (推荐, 因 footer 32/16/4879 在此版), 位置按原版 (105.2, 43.4) — 但注意 2026-08-21 曾因导航条 x[0,166] 覆盖而 +62 → 处理: 面板放 (105,43) 或维持 +62 但作为已知偏差; 若按 v1 全屏窗口方案则面板=434×694 @(251.9,213.1) 且 footer 用 90px 版。**二选一, 推荐独立 prefab 方案** (任务文件数值全部出自该版)。
3. **面板内部按 1.3 表重构**: LeaderboardButton (240.6,72.5) 291×53 'Leaderboard' 36px 置顶; 竖排 RankTitleBG(457×0, 40K_main_rank_display a0.92) + DivisionText 'Division V' 36px; Timer icon WF_icon_clock 33² + 'Ends in: 23d 5h' 32px; DivisionImage → RankImage 78² Roman (ranked.gd:480 已接 Roman I-V PNG ✅); footer 三块 (4879 40px + 32 40px + 16 40px + RankedSealStep 100² 用 `12_主程序资源/Sprite/Rank Skull.json`(-300467167438017286 描边? 实际该 sprite=满印) + Rank Skull Empty 空印, 用 modulate alpha 或切换 Empty/Fill 显示达标/未达)。
4. **加 chrome (v1)**: Back 按钮 (142.5,903.7) 73×72 贴图 40k_UI_bt_back + 'Back' 40px; ChangeRankedToggle (832.4,913.2) 255×54 (40k_menu_bt 透明底 + Ranked/Unranked 40px + 40_main_bt_toggle_on 89×40 滑块); Battle 条 = Continue (1403.1,913.2) 453×50 40k_bt_underbutton 绿 (0.37,0.89,0.59) 'Battle' 38px + Ranked Play Mode Button (1697,893) 90² 40k_UI_bt_play + GameModeText 'Game mode: Multiplayer' 35px (1243.2,975.1)。
5. **卡组区 (V2 补齐)**: ① Warlord Darkening: TextureRect (530,418) 940×558, 贴图 `03_界面UI/去重资源/.../Smooth background square.png` (08_预制体特效/战斗预制体/Texture2D/Smooth background square.png), color 黑 alpha 0.82 (可用 modulate=(1,1,1,0.82) 或黑 ColorRect) — 叠在督军立绘上 (项目立绘区 (451,-95) 1098² 中心 (1000,626) 恰与 V2 一致 (1000,626)!) ② 无卡组时: No Deck Text (617.2,685.0) 685.7×166.5 45px —— 建议用英文换行文案 (原版西语 'Tienes <color=#E98A00FF>{0} {1} Comandante(s)</color>, ¡comienza...' → 可用 "You have X Y Commanders, start..." 或按 JSON 西语 — 按 UI 英文规则改英) + **Create deck 按钮** (789.0,865.7) 342×103 UI_Button_Mulligan 'Create deck' **55px** (现有 "NO DECK/Create a deck in Collection" 逻辑保留, 按钮样式换成原版) ③ Deck 4 圆钮对位: 原版 (640.85,816.05) 起 4×160.9 宽 → 微调间距 (现 641+i*158)。
6. **工具**: ranked.gd:480 `_division_icon` 已用 `res://assets/ui/ranked/Roman %s.png` — 资源存在 (解包 03_界面UI/排位图标/Texture2D/Roman I..VI.png) ✅ 无需改。

### 4.2 quests 改造

1. **容器结构改单容器+右列**:
   - 左列 = 1 个 Daily Skulls 容器: 容器 Control (204.4, 374.6) 336×555 (或按含 scale 绘制: (179.2,333.0) 386.4×638.3 并把内部所有元素按审计表的 x1.15 绝对坐标摆放 — 推荐后者, 像素级一致)。
   - 内部 (以 1.15 缩放绝对坐标, 直接对照 audit_D 表): header name 'Daily Skulls' 36px + info 41²; body: 小骷髅 76.1×74.4 @(185.5,397.2) + 'x160000' 30px @(243.3,428.9) + 大骷髅 255×263 @(261.6,422.0); progress: **5** 个 Mission Milestones Step 46² @(162.5,699.6) 起 ×1.15 间隔 (原版 5 个, 现 4 个 → 加 1) + text 42.2px + CheckMark 40K_settings_icon_checkmark; footer: Rewards (Campaign 图标) ×2 + count 40px + Collect (227.1,813.7) 294.4×85.8 40K_button (1,0.47,0.1) 'Collect' 44px + Timer 'Resets in 12h 34 m' 38px。
   - wins/collect 自定任务内容 → 改放右侧 Daily Missions 3 行。若只保留 daily skulls 单列, 右列 3 行= 任务行 (wins/collect/每日骷髅综合… 由主代理决定数据源; UI 按原版行模板)。
2. **右列 Daily Missions 面板** (1271.3,12.5) 620.1×639.3: Mission Header (1274.4,15.0) 'Daily Missions' 36px + info 41² + Refill Counter '0 Disponible' 36px; 3 行 Daily Mission Container 每行 172.5 高、行底 40K_missions_display_Daily horizontal (0.49,0.57,0.92,1)、Rewards 块 145.3 宽左 (Campaign 图标+'100' 40px)、竖分隔线 x1409.8 (1.8×169 color(0.25,0.25,0.41,0.59))、文本区 'Deal 500 damage to enemy units' **40px** + 'Available in 64h' **40px**、进度 '52/500' **40px** (40k_generial_bar_empty (1,0.59,0)/fill (1,0.77,0.33))、右下角对: Trash mission 49.1²(56.5) **40k_general_bt_yellow** (1,0.77,0.33) + 40k_general_bt_yellow_delete + Collect (1,0.53,0) 254.6×56.5 'Collect' 44px。
3. **周常条**: 移到 (372.4, 759.8) (现 (206,691) → x+166, y+69); header 'Weekly Challenge' 36px @(383.8,762.3) + info 41²; 进度条 (442.5,871.8) 1008.4×22.7; 4×里程碑 70² @(377.5,927.0 起); Rewards 4× 250×113 @(485.6,926.0); Collect (1570.1,865.5) 294.3×74.7 44px; TimerHolder 'Ends in 12h 34 m' 38px @(1563.7,964.2)。
4. **删自创**: Campaign 按钮 + Achievements 按钮 + 辉光 + 副标题 "Daily Missions · reset daily…" (若 NavBuilder REWARDS 已含左列 Tab 导航含 Campaign/Forge — 需核对 nav_builder; D 组审查结论"自创三入口"即指此)。"Missions" 44px 标题改 "Daily Missions" 36px, 位 (1292.9,16.6)。金币显示 (1530,14): 核对主菜单全局 topbar, 若已有则删。
5. **保留**: Collect 橙 (1,0.47,0.1) ✅ 已修; 领取逻辑/进度数据不动。

---

## 附录: 关键原始 JSON 位置速查 (03_界面UI/菜单/)

| 内容 | 文件 |
|---|---|
| ranked v1 根 | GameObject/RankedEventWindow_-3438541305642376491.json (+ RectTransform_340272506660692693.json) |
| ranked v2 根 | GameObject/RankedEventWindowV2_-5324570929900320848.json (RectTransform_6837807522738505648.json) |
| Ranked Division Info standalone | GameObject/Ranked Division Info_-3383320362765802140.json (RectTransform_-7004980321802476188.json) |
| Ranked Division Change Window (PROMOTED!) | GameObject/Ranked Division Change Window_-3030737852390665906.json |
| quests 根 (Rewards Base Submenu) | GameObject/Rewards Base Submenu Variant_-8343312282719283457.json |
| Missions Tab | GameObject/Missions Tab_-3261567823877957889.json |
| Daily Skulls 容器 | GameObject/Daily Skulls Mission Container_7706541736523601663.json |
| Daily Missions 面板 | GameObject/Daily Missions_5064257774696273663.json + Daily Missions Holder_3523712292682602239.json |
| Daily Mission Container ×3 | _-1689853150408665345 / 4933302183333467903 / -7898691639256960327.json |
| Mission Header | GameObject/Mission Header_-2637473773048293633.json |
| Weekly Mission Holder | GameObject/Weekly Mission Holder_7218257402582079231.json |

scale 映射: `Warpforge_tools/data/ui_layout/rt_scale_map.json` (Special Missions -3954402248558504193 / Daily Missions 4921620045776164607 = 1.15; RankImage 链 1.08; V2 Help Button 0.74)
