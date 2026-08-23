# 子代理报告：campaign（战役）与 achievements（成就）界面权威规格

> 生成 2026-08-23 · 子代理完全深读（说明书 04_界面UI 索引/全树/要点 1-4 块 + 原始 Unity JSON 逐元素 dump + chain_rect.py v2 绝对坐标复核 + 项目代码 campaign.gd/achievements.gd/player_profile.gd 逐行对比）
> 坐标一律为 Godot 1920×1080 y向下 绝对坐标 = chain_rect.py v2（含 m_LocalScale，rt_scale_map.json）。所有数值均直接来自原始 JSON（`d:/2/解包整理/03_界面UI/菜单/`），整理文档仅作定位。
> 原始 JSON 行号引用："全树" = `解包整理/说明书/04_界面UI/菜单全树.md` 行号。

---

## 0. 关键结论（先看这个）

1. **原版战役页（Campaign Tab）不是独立场景，是 `Rewards Base Submenu Variant`（奖励子菜单）内的一个 Tab**（全树 12171 起，Campaign Tab 在 12676，**inactive**），左侧配 **4-Tab 竖栏：Missions / Campaign / Forge / Booster Packs**。项目把 campaign 做成独立场景 + 全局导航层（NavBuilder），**没有 4-Tab 竖栏**（仅 rewards.gd 有一个 5 键残缺版）。
2. **原版成就页（Achievements Tab，全树 4949）没有任何类型筛选钮**——只有 Scroll→ContainerHolder→Achievement Container（20 个元素）+ 1 个模板容器。**Achievement Type Toggle 只存在于 Player Profile Window→Trophies Tab**（全树 16148-16167，5 个竖排，284.1x100）。→ projects 的 achievements.gd 自创 6 个筛选钮应删除。
3. 成就条目容器原版 = **520x150**，双列，列距 530（即间隙 10），行距 160（间隙 10）。项目用 580x160、间隔 12 —— 尺寸/间隔均错。
4. 进度条原版 = **40k_campaign_bar_bg/fill/outline/end 四件套**（底色 tint 0.3,0.29,0.69 / 填充 1,0.51,0 / 描边 1,0.84,0 / 端头 29.4x31.9 白 α0.7），条体 **221x26**（容器内 x152）。项目用 40k_bt_underbutton + 40k_generial_bar_fill（金色）—— 全错。
5. campaign 头部原版底纹 = **WF_Campaign_Info_Background**（非项目用的 40K_tab_button_overwindow）；Points 行原版**带 Point Icon（50x33 本体 ×m_LocalScale=2.0 → 显示 100x66，x828.1,135.2）双层贴图**（40K_genearl_icon_Campaign points + 阵营图标 40k_DeckSelection_icon_FactionBlackLegion），项目纯文字无图标。
6. campaign 节点原版 = **Campaign Node 100x100 圆钮**（WF_Campaign_Levelspot 107x106 圆片 + Premium 节点盖 WF_Campaign_Levelspot-Premium 256 方 + Collectable Highlight = Border Thick Circle FX 178.9 + Item Holder 100x100 + 节点连线 Node Line 290.6x10 = 40k_Generic Smooth line）。项目用 40k_missions_milestone_on/off 方块 + 阵营小图标 + 勾 —— 贴图不符、尺寸 68 偏小、无连线。

---

## 1. campaign 原版元素全表

### 1.1 父容器：Rewards Base Submenu Variant（全树 12171 `[0,0 1920x1080]`）

JSON：`GameObject\Rewards Base Submenu Variant_-8343312282719283457.json`（RT 507527829764970239，dump 见 `_tmp_rewards_submenu.txt`）

| 元素 | 类型 | 父 | Godot 绝对 (x,y,w,h) | 锚点/pivot | 贴图/说明 | 来源 |
|---|---|---|---|---|---|---|
| Content Area | 容器 | Submenu | (167.2, 0) 1752.8x1009.1 | anchor(0,0,1,1) pivot(0.5,0.5)，offset 左167.2 下70.9 | 页面区 | 全树 12172 |
| Tab Buttons | 容器+Image | Content Area | (167.2,71) 165x1009.1 | anchor(0,0,0,1) pivot(0,0.5) | Image→**40k_main_tab_background**（185x4 拉伸） | 全树 12174 |
| Tab Buttons · Shadow | Image | Tab Buttons | (167,71) 48x1009 | — | sprite -8666545702653119048（竖阴影条） | 全树 12203 |

**4-Tab 竖栏按键**（全部 Button，尺寸 **0x180**=165x180，anchor(0,0,0,0) pivot(0.5,0.5)，**原始 pos(0,0)=布局组运行时排版**；所在布局组：spacing 0 / alignment 1(UpperCenter) / padding top 120 → 运行时按钮顶从 y≈71+120=191 起每 180 一个；4 键占 720）。每键结构（以 Campaign 键为例，全树 12182-12188）：

| 子元素 | 尺寸 | 贴图/文字 | 备注 |
|---|---|---|---|
| Highlight | 满 180 | 40k_main_bt_selected BW，color(1,0,0,1)（红染选中高亮） | 选中页用 |
| Icon | 满 165x180 | pivot(0.5,0.7)：Missions=**40K_rewards_bt_missions**(126x126)、Campaign=**40k_main_bt_campaign**(126x126)、Forge=**40K_rewards_bt_forge**(126x126)、Booster Packs=**40K_shop_bt_boosters**(126x126) | 全树 12177/12184/12191/12198 |
| Label | 155x37.9 | Image→40k_main_bt_nametag(109x41)，pivot(0.5,0)，位于键底 | 全树 12178 等 |
| Label→TabButtonLabel | 155x37.9 | 'Missions'/'Campaign'/'Forge'/**'Booster Packs'**；字号 36（Booster Packs 25.65），**style 16=全大写**，白 | 全树 12179/12186/12193/12200 |
| Badge Highlight | 35x35 | 40K_notification_number(65x65)，color(0.74,0.74,0.74) | 通知角标，键右上 |
| Badge→OneText | 35x35 | '' 字号34 | 数字未显示 |

### 1.2 Campaign Tab 本体（全树 12676 `[331,71 1589x1009]`，实例 **inactive**；独立根版本 全树 282 `[164,0 1756x1080]` active，同一预制体两实例，结构完全一致）

JSON：`GameObject\Campaign Tab_-880831270227011841.json`（RT -7627375673320990977，子菜单实例）/ `Campaign Tab_5958516118268259725.json`（独立实例）。以下坐标为**子菜单实例**（项目 campaign.gd 以 x331 布局 = 此实例基准；audit_D_campaign.md 同源）。

| 元素 | 类型 | 父 | Godot 绝对 (x,y,w,h) | 锚点/pivot/其他 | 贴图/文字/字号/颜色 | active | 来源(全树/JSON) |
|---|---|---|---|---|---|---|---|
| Campaign Tab | 容器 | Rewards Submenu→Tabs | (330.7,70.9) 1589.3x1009.1 | anchor(0,0,1,1) | — | 子菜单内 inactive | 12676 |
| Campaign Background | Image | Tab | (330.3,70.9) 1589.7x1009.1 | anchor 满 pivot(0,0.5) | m_Sprite=0 纯黑 (0,0,0,1) | — | 12677 |
| ├ Background Image | Image | Background | (330.3,-45.2) 1589.7x1589.7 | anchor 满 pivot(0,0.8) sizeΔ(0,580.6) | 无贴图白 | **inactive** | 12678 |
| Campaign Army Selector | 容器 | Tab | (745.9,70.9) 1174.4x137.0 | anchor(0,1,1,1) pivot(0.5,1) | — | — | 12679 |
| ├ Background | Image | Selector | (643.2,71.4) 1277.1x136.0 | anchor(0,0.5,1,0.5) pivot(0,1) | 无贴图 黑 α0.35 | — | 12680 |
| ├ Viewport | — | Selector | (745.9,70.9) 1174.4x137.0 | anchor 满 | 透明 | — | 12681 |
| │ └ Army Content | 容器 | Viewport | (916.1,70.9) 0x137 | anchor(0.5,0,0.5,1) | 运行时放 **Campaign Army Item Button**（见1.3） | — | 12682 |
| Campaign Header | Image | Tab | (330.7,60.9) 460.2x165.0 | anchor(0,1,0,1) pivot(0,1) | **WF_Campaign_Info_Background**(740x167) | — | 12683 |
| ├ Debug Point Button | Button | Header | (1146.2,91.6) 245x67.7 | — | UI_Button_Mulligan；Text 'Change Deck' 36 | **inactive** | 12684-85 |
| ├ Army Icon | Image | Header | (345.7,60.9) 135x165 | pivot(1,0.5) pos(-80.1,0) | 40k_DeckSelection_icon_FactionBlackLegion（阵营图标） | — | 12686 |
| ├ Title | Text | Header | (480.7,60.9) 225x74.3 | anchor(0.2,0.55,0.5,1) pivot(0.5,0.5) | 'ULTRAMARINES' TMP auto 25-35（现 31.75） 白 | — | 12687 |
| ├ Premium Button Container | 容器 | Header | (743.2,60.9) 262.5x82.5 | anchor(0.55,0.5,0.9,1) | — | **inactive** | 12688 |
| │ ├ Premium Button | Button | Container | (743.2,143.4) 0x0（折叠） | — | UI_Button_Mulligan 'Premium' 36.6 | — | 12689-90 |
| │ ├ Premium pruchased | Image | Container | (811.2,92.5) 54.1x54.1 | — | **40k_campaign_Premium-icon**(301x305)；旁 Text 'Premium' 29.7 | — | 12691-92 |
| ├ Points | Text | Header | (480.7,151.7) 368.2x33.0 | anchor(0.25,0.25,1,0.45) pivot(0,1) | 'Points: 69' TMP auto 18-40（现 34.8） 白 | — | 12693 |
| │ └ Point Icon | 容器 | Points | **(828.1,135.2) 100x66**（本体 50x33，**m_LocalScale=2.0**，rt_scale_map 实锤） | anchor(1,0,1,1) pivot(0,0.5) | 双层满铺：(1) Campaign Point Background=**40K_genearl_icon_Campaign points**；(2) Army Icon=40k_DeckSelection_icon_FactionBlackLegion | — | 12694-96 |
| ├ Info Button | Button | Header | (719.8,94.0) 41.2x41.2 | — | **40K_generic_bt_info** | — | 12697 |
| Campaign Track | ScrollRect | Tab | (330.7,335.5) 1589.6x709.1 | anchor(0,0.5,1,0.5) pivot(0,0.5) | ScrollRect（横向滚动，运行时布节点） | — | 12698 |
| ├ Viewport | Image | Track | (330.7,285.5) 1589.6x759.0 | anchor 满 pivot(0,1) | 无贴图 (1,1,1,0) | — | 12699 |
| │ └ Content | 容器 | Viewport | (330.7,335.5) 200x659.1 | anchor(0,0,0,1) pivot(0,0.5) | **初始 200 宽，659 高**（运行时脚本调宽/布节点+连线） | — | 12700 |
| Premium Panel | 容器 | Tab | (344.3,1080) 376.1x0 | anchor(0,0,0,0) pivot(0,0) | **折叠在屏幕下缘外**（动画弹出；当前 h=0） | inactive 态 | 12701 |
| ├ Background | Image | Panel | 满 | — | WF_UI_Ranked_Background_Gold | — | 12702 |
| ├ Title | Text | Panel | (166.4,1058.8) 355.8x42.4 | — | 'Premium Campaign daily bonus' 33.3 | — | 12703 |
| ├ Points(Quantity) | Text | Panel | (270.4,1051) 77x58 | — | '200' 61.2 | — | 12704-05 |
| ├ Points(icon) | 容器 | Panel | (141.6,1074.1) 65x69.7 | pivot(1,0.5) | Icon Campaign Points Drawer（1080 Content: Campaign Glow=40K_genearl_icon_Campaign points_big + Converted/Ephemeral 价格抽屉） | — | 12706-19 |
| ├ Generic Simplified UI Button | Button | Panel | (216.3,1052.3) 256x55.5 | — | UI_Button_Mulligan 'Continue' 49.3 | — | 12720-21 |
| ├ Timer | — | Panel | (344.3,1080) 348.4x39.3 | pivot(0,1) | 时钟 WF_icon_clock + 'Siguiente: 5d 20h 15m' 37.9（西语残留） | — | 12722-24 |
| ├ Timer Icon | Image | Timer | (344.3,1100) 38.5x38.6 | — | WF_icon_clock color(0.76,0.76,0.76) | — | 12723 |
| Tutorial Message | 容器 | Tab | (1184.1,220.4) 567.1x120.2（骨架拉伸） | anchor(0,1,1,1) | 40k_popup 底 + 40k_popup_texture + 'Choose your favourite faction. You can l…' 35 + Highlight Down/Up=Border Line Only Horizontal FX(128x64) | **inactive** | 12725-31 |

### 1.3 阵营选择条目 Campaign Army Item Button（运行时置于 Army Content；全树 4214 `[-60,1080 120x0]`）

JSON：`GameObject\Campaign Army Item Button_6426011274901591754.json`（RT -6148399272832133430）

| 元素 | 尺寸 | 贴图/文字 | 说明 |
|---|---|---|---|
| 根 | 120x0（运行时高≈110-130，脚本调） | Button | 每个阵营一个 |
| HighlightBG | 120x110（锚顶） | 40K_settings_button_hover color(1,0.63,0.28) | 悬停/选中橙色 |
| Icon | 120x100（锚顶，-5 偏移） | 运行时阵营图标 | |
| Badge Highlight | 35x35 右上 | 40K_notification_number color(0.74,0.74,0.74) + OneText 34 | 通知角标 |
| Slider（**阵营战役进度条**） | pos(0,-110) size(-10,20) | Background=**40k_campaign_bar_bg** color(0.3,0.29,0.69)；Fill Area→Fill=40k_campaign_bar_fill color(1,0.51,0)；Outline=40k_campaign_bar_outline color(1,0.84,0) | 每阵营进度条，条底+填充+描边三件套 |

### 1.4 Campaign Node（战役地图节点，全树 13872 `[-215,14 100x100]`）

JSON：`GameObject\Campaign Node_666348682854551431.json`（RT 6791446287889289095）

| 元素 | 尺寸 | 贴图 | active | 说明 |
|---|---|---|---|---|
| Campaign Node | 100x100 | — | — | pos(-215,476) anchor(0,0.5) pivot(0,0.5)（模板锚点），运行时排位 |
| Premium Mark | 100x100 | **WF_Campaign_Levelspot-Premium**（256x256 Premium 角标片） | — | Premium 节点覆盖层 |
| Generic Round Button Variant | 100x100 | **WF_Campaign_Levelspot**（107x106 圆盘），Button | — | 主节点钮 |
| ├ Button Text | 满 | 'X' 30 | **inactive** | 编辑器删除钮（隐藏） |
| ├ Image | 满 | 40k_general_bt_yellow_delete sizeΔ(-2,-2) | — | 隐藏 |
| Collectable Highlight | 178.9x178.9 | **Border Thick Circle FX** | **inactive**（可领取时点亮） | 光圈 |
| Item Holder | 满 100x100 | — | — | 运行时节点内图标（阵营图标等） |

### 1.5 Node Line（节点连线，全树 11479 `[960,535 291x10]`）

JSON：`GameObject\Node Line_8711542813501762573.json`：290.6x10，anchor(0.5,0.5) pivot(0,0.5)，Image→**40k_Generic Smooth line**（113x32）。→ 相邻节点中心距 ≈ 290.6px。

### 1.6 Campaign Reward Window（节点奖励弹窗，全树 9108 `[0,0 1920x1080]`）

JSON：`GameObject\Campaign Reward Window_-3992165112361214842.json`（dump `_tmp_campaign_reward.txt` 54 行，chain_rect 已复核）

| 元素 | Godot 绝对 (x1,y1)-(x2,y2) | 尺寸 | 贴图/文字/字号/颜色 | active | 全树 |
|---|---|---|---|---|---|
| Campaign Reward Window（根） | 全屏 | 1920x1080 | — | — | 9108 |
| Menu Dark Background | 全屏（拉伸 4574x2572） | — | 纯黑 α0.77 | — | 9109 |
| Content | (0,165)-(1920,965) | 1920x800 | — | — | 9110 |
| ├ Reward Background Get Reward | 满 Content | — | 40k_general_popup_simple red（21x81 平铺红底） | **inactive**（领取态） | 9111 |
| ├ Reward Background Preview Reward | 满 Content | — | 40k_general_popup_simple greyscale | active（预览态） | 9112 |
| ├ Scroll View | (0,285)-(1920,935) | 1920x650 | ScrollRect | — | 9113 |
| │ └ Viewport→Content→**Base Rewards** | (0,285)-(960,935) | 960x650 | anchor(0,0,0.5,1) | — | 9116 |
| │ │ └ Rewards | (895,295)-(895,910)（右贴 0 宽拉伸） | 0x615 | **UI_Deck_Information_submenu_Back** | — | 9117 |
| │ │ │ ├ Unlock Button | (772.5,850)-(1017.5,895) | **245x45** | UI_Button_Mulligan + Button（child 无文字；另带 Claimed Text 'Change Deck' 35 size(0,0)、Point Count '100' 32.3 inactive） | — | 9118 |
| │ │ │ │ └ Icon Campaign Points Drawer Variant | 左半区 (0,0,0.5,1) 宽77.5 | Content 1080：Campaign Glow=**40K_genearl_icon_Campaign points_big** + Converted/Ephemeral 价格抽屉（2000/24 hours） | inactive 折叠 | 9119-31 |
| │ │ │ └（无） | | | | |
| │ └ **Premium Rewards** | (960,285)-(1920,935) | 960x650 | 同 Base 结构（Rewards 右贴 x1025 0x615；Unlock (902,850) 245x45；Badge 100x100=40k_campaign_Premium-icon @(1025,295)；Warning (1010,850) 30x45 'Warning or Tip' 47.5 inactive） | — | 9134-53 |
| ├ Title | (660,193.3)-(1260,268.3) | 600x75 | anchor(0.5,1) | — | 9154 |
| │ ├ Glow Get reward | (660,187.4) 600x75 | 40k_bt_underbutton color(**0.8,0.08,0.08**) + 'Campaign Rewards' 50 | inactive（领取态） | 9155-56 |
| │ └ Glow Preview reward | 同上 | color(**0.53,0.36,0.36**) + 'Available rewards' 50 | active（预览态） | 9157-58 |
| Tap To Continue | (576,965)-(1344,1045) | 768x80 | 'Click to continue' 55 | inactive | 9159 |
| Reward Claim | 无 RT | — | 动画（Wave/Wave Shine/Trails 粒子） | inactive | 9160-66 |
| Menu Vignette | 全屏 | — | 纯黑 α0.58 | — | 9167 |

### 1.7 其它 campaign 相关（佐证/周边）

- **Campaign Profile Container Variant**（全树 1574 `[-278,992 555x175]`）：玩家资料小容器（Profile 页 'Current campaign' 徽章）：Background=-2338345087259041511、Title 'Current campaign'、Badge、ArmyName 'Ultramarines'、Level 'Level: 0'。已实现于 player_profile.gd（项目有 Campaign Profile 容器）。
- **Campaign Points Drawer**（全树 13329-13353）：奖励抽屉 712x1080（Content x604）：Background 4317389718814432617 + Campaign Glow 40K_genearl_icon_Campaign points_big + Label 条（'Campaign Points' '500'）+ Converted/Ephemeral + Claimed + Army 'Leviathan'。项目 achievements.gd TEX_CAMPAIGN 已用它做点数图标（TEX_CAMPAIGN = 40K_genearl_icon_Campaign points_big ✓ 与抽屉 Glow 一致）。
- **40K_ArmyTrack_bg**（轨道底纹，pathid 2374284676670985858）：**JSON 中无任何 Image 引用**（运行时脚本赋给轨道），项目 campaign.gd 已用 (331,335) 1590x709 —— 保持现状，无冲突证据。

---

## 2. achievements 原版元素全表

### 2.1 Achievements Tab（全树 4949 `[-0,-2 1920x1082]`，是**独立根界面**，活动）

JSON：`GameObject\Achievements Tab_7942391680202248253.json`（RT -7048126750119620547；dump `_tmp_achievements_tab.txt` 18 行）

**全表只有以下 18 个元素，无标题文字、无筛选钮、无 Tab 栏。**

| 元素 | 类型 | 父 | Godot 绝对 (x,y,w,h) | 锚点/pivot | 贴图/文字/字号/颜色 | 全树 | JSON pid |
|---|---|---|---|---|---|---|---|
| Achievements Tab | 根 | — | (0,0) 1920x1082 | anchor(0,0,1,1) | — | 4949 | GO 7942391680202248253 |
| Scroll | ScrollRect | Tab | **(199.0,129.1) 1523.6x928.0** | (0.5,0.5) sizeΔ(-396.9,-153.7) | 无贴图 (1,1,1,0) | 4950 | GO -7823392288012169155 |
| ├ Viewport | Image | Scroll | (199.0,129.1) 1523.6x911.0 | pivot(0,1) sizeΔ(0,-17) | 无贴图 | 4951 | GO -1111312797949882307 |
│ └ ContainerHolder | 容器 | Viewport | (199.0,129.1) 1523.6x0 | anchor(0,1,1,1) | 运行时布容器（脚本，自定义容器器：maxAmount=-1） | 4952 | GO 5619714873142022205 |
│ │ └ **Achievement Container**（模板） | 容器 | Holder | (199,54.1) **0x150**（宽由脚本拉伸） | anchor(0,0,0,0) pivot(0.5,0.5) sizeΔ(0,150) | Image→**UI_Deck_Information_submenu_Back** | 4953 | GO -3625966182550532035 |

> 注：容器模板宽=0，运行时由自动排版脚本按 **520x150**（与 Trophies Tab 烘焙值一致，见 2.3）设置。Grid 双列 530 步进/160 步进（Trophies Tab 烘焙：x 290.9→820.9，y -107→-267…，即每格 520x150、格距 10）。

### 2.2 Achievement Container 内容（容器内相对坐标 = 原版布局基准，520x150 容器上）

JSON：`GameObject\Achievement Container_8365984317912611378.json`（Trophies Tab 实例=预制体基准，同容器用在 Achievements Tab）。**Trophies Tab 首格 abs 坐标**（container 在 (666.1,232.3)）：标题 (818.1,253.2)、描述 (818.1,285.9)、Image (681.1,242.3)、rewards (1068.8,334.3)、rewardIcon (1040.2,329.5)。

| 元素 | 容器内相对 (x,y,w,h) | 锚点/pivot | 贴图/文字/字号/颜色 | 全树(520 版) | 说明 |
|---|---|---|---|---|---|
| 背景框 | 满 | anchor(0,0,1,1) | **UI_Deck_Information_submenu_Back** | 16171 | 容器自身 Image |
| Image（成就图标） | (15,10) 130x130 | anchor(0,0.5) pivot(0,0.5) → 若拉伸容器宽 520 不变 | 无贴图（运行时资源）；颜色白 | 16184 | |
| title | (152,20.9) 359x32.7 | anchor(0.3,0.5,1.0,0.5) pivot(0,0.5) pos(-4,37.7) sizeΔ(-5,32.7) | 'Victorious 1/5' TMP **auto 12-35 (base 36, style 1=Bold)** | 16172 | |
| description | (152,53.6) 359x48.4 | 同上 pos(-4,-2.9) sizeΔ(-5,48.4) | 'Upgrade Ultramarines cards to tier 2' auto 12-35（实例 12/29.55/35 不等） | 16173 | |
| rewards（文字） | (402.7,102) 108.3x29.5 | anchor(0.3,0.5,1,0.5) pos(246.7,-41.8) sizeΔ(-255.7,29.5) | '2 points' auto 12-35 | 16174 | |
| └ rewardIcon | (374.1,97.2) **28.5x39.1** | anchor(0,0.5) pivot(1,0.5)（文字左贴） | **40k_Achievements_icon_seal points**（54x74） | 16175 | **项目缺失** |
| Progress | (152,102) 220.7x29.5 | 同 rewards 系 | — | 16176 | |
| └ Slider | (152,93.8) 220.7x43.6 | anchor(0,0,1,1) pivot(0.5,1) pos(0,8.3) sizeΔ(0,14.2) | Button | 16177 | 超出 Progress 上下各约 7px |
| │ ├ Background | (152,102.5) 220.7x26.2 | anchor(0,0.2,1,0.8) | **40k_campaign_bar_bg** color(**0.3,0.29,0.69**) | 16178 | 条底 |
| │ │ └ Fill Area | (152,104.5) 220.7x22.3 | 同 | — | 16179 | |
| │ │ │ └ Fill | (152,104.5) 220.7x22.3（模板满格） | — | **40k_campaign_bar_fill** color(**1,0.51,0**) | 16180 | 进度填充 |
| │ │ │ │ └ end | (348.9,100.7) 29.4x31.9 | anchor(1,0.5) pivot(1,0.5) | **40k_campaign_bar_end** color(1,1,1,**0.7**) | 16181 | 端头帽 |
| │ ├ counter | (196.1,106.9) 132.4x21.8 | anchor(0.2,0.2,0.8,0.7) pivot(0,0.5) | '100/200' auto 12-35 | 16182 | 进度数字 |
| │ └ Outline | (152,102.5) 220.7x26.2 | anchor(0,0.2,1,0.8) | **40k_campaign_bar_outline** color(**1,0.84,0**) | 16183 | 黄色描边（叠最上层） |

### 2.3 Player Profile Window → Trophies Tab（Achievement Type Toggle 权威位置；全树 15854 起，Trophies Tab 16145）

JSON：`GameObject\Player Profile Window_-2413820956890924494.json` → `Trophies Tab_-1698997230529643982.json`（dump `_tmp_trophies_tab.txt` 197 行）

| 元素 | Godot 绝对 (x,y,w,h) | 锚点/pivot | 贴图/文字 | 全树 |
|---|---|---|---|---|
| Trophies Tab | (351,118.9) 1395.9x843.1 | anchor 满 Tab Content | — | 16145 |
| bg | (635.1,213.2) 1111.8x678.5 | — | **UI_Deck_Information_submenu_Back** | 16146 |
| buttons（分类列） | (351,230.6) 284.1x697.6 | — | — | 16147 |
| **Achievement Type Toggle ×5** | (351,230.6) (351,350.6) (351,470.6) (351,590.6) (351,710.6) 各 **284.1x100** | anchor(0,1,0,1) pivot(0.5,0.5)，pos(142.1,-50/-170/-290/-410/-530) | Button | 16148-16167 |
| ├ button_bg | 满 | — | **40K_settings_button**（168x156） color(**1,0.57,0,0.71**) | |
| ├ Label | 155x40（键中心） | anchor(0.5,0.5) | — | |
| │ └ Tab Toggle Title | 满 Label | — | 'Secret'（占位，运行时设分类名）TMP 35 白 | |
| Scroll | (635.1,213.2) 1111.8x678.5 | — | — | 16168 |
| └ Viewport→ContainerHolder | (635.1,200.3) 1111.8x1014 | — | — | 16169-70 |
| │ └ **Achievement Container ×12** | (666.1,232.3) 起，**x步 530（520+10）、y步 160（150+10）**，各 520x150 | anchor(0,1,0,1) pivot(0.5,0.5) | UI_Deck_Information_submenu_Back | 16171-16325 |
| Counter（成就点数） | (1568.9,161.1) 135.1x41.1 | — | **Feedback Scoring Button**(96x60) color(0.65,0.07,0.07) | 16145 区 |
| ├ EverguildTextMeshPro | (1580.5,165.1) 111.8x33.1 | — | '300' 34.85 白 | |
| └ Image（seal） | (1521.2,145.0) 65.3x79.0 | — | **40k_Achievements_icon_seal points** | |

**结论（task 第 3 项佐证完成）：原版 Achievement Type Toggle = Player Profile→Trophies Tab 左侧 5 个 284.1x100 竖排（步进 120），button_bg=40K_settings_button 橙染 (1,0.57,0,0.71)、文字 35px 白居中。成就专用界面（Achievements Tab）内没有此组件。**

---

## 3. 项目现有实现差异清单（逐元素 原版 vs campaign.gd / achievements.gd）

### 3.1 campaign.gd（`D:/warpforge/scripts/campaign.gd`，626 行，场景只挂脚本）

| # | 原版 | 项目现状 campaign.gd | 判定 |
|---|---|---|---|
| C1 | 战役页属于 Rewards 子菜单，左侧 4-Tab 竖栏（Missions/Campaign/Forge/Booster Packs）165x180 带图标/nametag | 独立场景，无 4-Tab 栏（只有 NavBuilder 全局导航 x0-166）；页面内容起点 x331（原版 Tab 区右缘位置），x166-331 空 165px 无内容 | **缺失**（批次4共享项，见 §5.3） |
| C2 | Campaign Header 底 = **WF_Campaign_Info_Background**（460x165，(330.7,60.9)） | 用 `40K_tab_button_overwindow.png`（加标签高亮底）@(331,61) 460x165 —— **贴图错** | 错（换贴图即可） |
| C3 | 阵营图标 135x165 @(345.7,60.9) | 120x150 @(331,66) | 尺寸/位置偏差 |
| C4 | Title 'ULTRAMARINES' @ (480.7,60.9) 225x74.3，白，auto 25-35 | Label @(470,80) 320x40 字号24 金色 | 位置/字号/颜色均不符 |
| C5 | Points 'Points: 69' @ (480.7,151.7) 368x33，白 auto 18-40 | Label @(470,130) 320x36 字号18 灰 b0b5bd | 位置/字号/颜色不符 |
| C6 | **Point Icon**（100x66 @ 828.1,135.2：Campaign points 底+阵营图标双层） | **无**（纯文字） | **缺失** |
| C7 | **Info Button** 41.2x41.2 @(719.8,94.0) 40K_generic_bt_info | **无** | **缺失** |
| C8 | Premium Button Container（inactive：Premium Button 262.5x82.5 + Premium pruchased 54.1 40k_campaign_Premium-icon + 'Premium' 29.7） | **无**（单机无 Premium） | 缺失（可选项，按原版为 inactive） |
| C9 | Campaign Army Selector：黑 α0.35 底条 (643.2,71.4) 1277.1x136 + 每阵营 Campaign Army Item Button（120 宽，40K_settings_button_hover 橙高亮 + 120x100 图标 + **阵营进度条 40k_campaign_bar_三件套** + 角标 35） | 自建按钮流：84x84 每键 @(746+89i,95)（第一步 95，键距 89），选中用金色 StyleBoxFlat 描边，无进度条、无角标、无 hover 底 | 结构风格偏 —— 键尺寸/间距/进度条/高亮贴图不符 |
| C10 | Campaign Track = ScrollRect 1589.6x709 Viewport (330.7,285.5) + Content 200x659（运行时布 15 节点），节点 = **Campaign Node 100x100**（WF_Campaign_Levelspot 圆盘 + Premium Mark 覆盖 + Border Thick Circle FX 光圈178.9 + Item Holder）+ **Node Line 290.6x10 连线**（40k_Generic Smooth line，节点距≈290.6） | 无 ScrollRect；节点 68x68（x=331+gap*i，y=430，gap=1590/14≈113.6）—— 节点距 113.6（原 290.6）、尺寸 68（原 100）、无连线、无光圈、无 Premium 标记；节点内容=40k_missions_milestone_on/off 方块+阵营 68 图标+Text 'Start'/'名字' + 已领勾 40K_settings_icon_checkmark；终点用 Legions gold crate | **节点贴图/结构不符**（core 修复项） |
| C11 | 节点轨道底纹 40K_ArmyTrack_bg（JSON 无引用，运行时赋）→ 项目 (331,335) 1590x709 使用中 | 一致 | OK |
| C12 | **自创** Claim 按钮 "Claim node rewards" 200x56 @(1450,610) + "Current node" desc 标签 @(480,615) + tooltip | 原版**无**此按钮（点节点→弹 Campaign Reward Window；进度注入 Campaign Army Item Button 的 Slider） | **多余**（可保留为便捷但非原版） |
| C13 | 弹窗：Campaign Reward Window —— Menu Dark 0.77 + 40k_general_popup_simple red（领取）/greyscale（预览）底 1920x800 @(0,165) + Base/Premium 两栏 960x650 @(0,285)/(960,285)，栏底 UI_Deck_Information_submenu_Back + 标题 'Campaign Rewards'/'Available rewards' 50px @(660,187.4) 600x75（40k_bt_underbutton 红 0.8,0.08,0.08 / 灰红 0.53,0.36,0.36）+ Unlock 245x45 @(772.5,850) / (902,850) + Badge Premium 100x100 @(1025,295) + 'Click to continue' 768x80 @(576,965) | 自建：通用窗 UI_Deck_Information_Back @(0,60) 1920x960 + 标题 @(660,95) 字号40 + 副标题 @(560,170) + 两栏 @(0,285)/(960,285) 960x650（栏底 submenu_Back ✓）+ 自建 "Claim Rewards" 大按钮 450x68 @(pos+255,pos+480) 40K_button + Locked 文案 + 关闭钮 40k_bt_close @(1816.5,70.7) | 结构近似但**贴图/文字/按钮规格不符**（原版无 'Available rewards' 副标题于母窗？——注意：'Available rewards' 是 Glow Preview reward 的标题文字；原版无 Locked 大按钮/无副标题行；关闭按钮原版弹窗内无（点击遮罩或 Tap To Continue 关闭）；Unlock 按钮原版 @ 栏底 245x45） |
| C14 | 数据模型：原版=通行证轨道+每阵营进度条+Premium 每日奖金面板（Premium Panel 376 宽 折叠）+ Campaign Points 点数（'Points: 69'） | 单机模型 progress 0-14 / claimed / faction，点数=_progress*10+胜场*2 | 玩法简化合理（单机），UI 规格仍按原版 |
| C15 | Tutorial Message（inactive 教学提示） | 无 | 可选（inactive） |
| C16 | Campaign 页面无金币条（原版头部有 Points 行+Info 钮；金币条是全局 top bar 的一部分？—— 原版 Campaign Header 内无金币显示） | 项目加了金币条 @(1530,14) 300x44 | 多余项（非原版 Campaign Tab 元素；若场景共享 topbar 可保留，否则删） |

### 3.2 achievements.gd（272 行）

| # | 原版 | 项目现状 | 判定 |
|---|---|---|---|
| A1 | Achievements Tab 无任何筛选钮 | **自创 6 个筛选钮**（All/Battle/Collected/Upgrade/Campaign/Economy）@(500+i*110,84) 100x44 + _filter/_on_filter 逻辑 | **删除**（原版 Toggle 在 Player Profile→Trophies，player_profile.gd 已实现 284.1x100 ×5） |
| A2 | 无标题/副标题 | 自创 'Achievements' @(240,40) 28px + 'All progress from real game data' @(240,80) | **自创**（原版 Tab 内无标题；若判为场景框架标题需挂在父场景 —— 建议删或移出滚动区顶层判断） |
| A3 | Scroll @(199,129) 1524x928 | ✓ (199,129) 1524x928（MenuBg.style_scroll） | OK |
| A4 | 容器 **520x150**，格 530/160（间隙 10/10），双列 | 容器 **580x160**，h/v separation **12** | **尺寸/间隔错** → 520x150、10/10 |
| A5 | 背景 UI_Deck_Information_submenu_Back | ✓ TEX_CONTAINER | OK |
| A6 | 图标 Image **130x130 @容器(15,10)** | icon (12,10) 130x130 —— x 应为 15 | 位置差 3px |
| A7 | 图标内容：原版 = 运行时成就资源（无贴图） | 项目用自选 medal1-5 徽章按类型 | 可接受替代（原版图标运行时分发） |
| A8 | title @(152,20.9) 359x32.7 **Bold auto 12-35** | @(150,12) 400x34 字号20；文案附加 "✓"（原版无勾） | 位置/字号/样式不符，勾是自创 |
| A9 | description @(152,53.6) 359x48.4 auto | @(150,46) 400x44 字号15 | 位置/字号不符 |
| A10 | 进度条：**40k_campaign_bar_bg**(0.3,0.29,0.69) 条底 @(152,102.5) **220.7x26.2** + **Fill 40k_campaign_bar_fill**(1,0.51,0) + **Outline 40k_campaign_bar_outline**(1,0.84,0) 同尺寸叠顶 + **end 40k_campaign_bar_end** 29.4x31.9 + counter '100/200' @(196.1,106.9) 132.4x21.8 | **40k_bt_underbutton** @(150,96) **360x26** + fill 40k_generial_bar_fill 金色(0.969,0.914,0.714) @(152,98) + counter @(452,96) | **贴图/颜色/尺寸全错**（core 修复项） |
| A11 | rewardIcon **40k_Achievements_icon_seal points 28.5x39.1 @(374.1,97.2)**（rewards '2 points' 内嵌） | **无** —— 奖励只有文字 "+X pts" @(330,130) | **缺失**（seal 贴图项目已有：scenes_sprites/40k_Achievements_icon_seal points.png ✓） |
| A12 | rewards 文字 '2 points' @(402.7,102) 108.3x29.5 | '+%d pts' 金色文字 @(330,130) 字号14 颜色金/灰 | 文字格式/位置/颜色不符（原版 '2 points' 白） |

### 3.3 player_profile.gd（对照，非本批次主改但佐证）

- Trophies Tab 已有 5 分类钮 284.1x100 @(351,230.6+i*120)（与 raw 一致 ✓）、Counter/Seal @(1568.9,161.1)/(1521.2,145.1) ✓、Scroll (635.2,213.2) 1111.8x678.5 ✓、格 10/10 ✓。
- 差异（小）：未选中 button_bg alpha 用 0.5（原版 0.71）；分类名用 'All/Battle/Collection/Victories/Account'（原版占位 'Secret'，实为运行时类型名，任自定义合理）。
- 该文件的成就条目构建是否也用了 520x150 需复核（若复用 achievements.gd 的函数则随 A4 一并修正）。

---

## 4. 实施建议

### 4.1 campaign（按优先级）

1. **节点贴图替换（core）**：`_build_track()` 的节点改用——底座 = `WF_Campaign_Levelspot.png`（100x100，KEEP_ASPECT 或直接铺 100x100）；Premium 节点叠 `WF_Campaign_Levelspot-Premium.png` 100x100；可领取节点显示 `Border Thick Circle FX.png`（178.9x178.9 居中，α 或 modulate 控制）；节点 100x100；节点间连线 `40k_Generic Smooth line.png`（290.6x10，旋转使首尾相连）或直接按原版 290.6 节点距水平排布；节点下阵营图标放 Item Holder。
2. **弹窗按 Campaign Reward Window 改造**：底 `40k_general_popup_simple red.png`（领取态）/`greyscale`（预览态）1920x800 @(0,165)；标题 600x75 @(660,187.4) 用 `40k_bt_underbutton.png` modulate (0.8,0.08,0.08)/(0.53,0.36,0.36) + 50px 'Campaign Rewards'/'Available rewards'；栏底 UI_Deck_Information_submenu_Back 两栏 (0,285)/(960,285) 960x650；Unlock 按钮 245x45 UI_Button_Mulligan @(772.5,850)/(902,850)；Premium 栏 Badge 100x100 40k_campaign_Premium-icon @(1025,295)；'Click to continue' 768x80 @(576,965)（点击关闭）。删自建 "Claim Rewards" 大按钮/Locked 图标/副标题。
3. **头部修正**：底纹换 WF_Campaign_Info_Background；阵营图标 135x165 @(345.7,60.9)；Title 31.75px 白 @(480.7,60.9)；Points @(480.7,151.7) 白 auto→34.8px；**Point Icon 100x66 @(828.1,135.2)** = 40K_genearl_icon_Campaign points 底 + 阵营图标两层（项目两者贴图已存在）；补 **Info Button 41.2 @(719.8,94)** 40K_generic_bt_info。
4. **阵营选择条**：黑 α0.35 底 @(643.2,71.4) 1277.1x136（现有 84px 键偏小）；每键按 Campaign Army Item Button 重建（120 宽、40K_settings_button_hover 橙高亮、120x100 图标、35 角标、**每阵营 20px 高 40k_campaign_bar 三件套进度条**）。
5. **4-Tab 竖栏**（与 rewards.gd 共享，见 5.3 统一改）——campaign/quests/forge 三页都补左栏后，内容 x331 起才成立。

### 4.2 achievements

1. **删自创筛选钮**（filters 数组 + `_on_filter` + `_filter_btns` + `_filter` 相关，行 116-148/167-173/179-182）。
2. **容器改 520x150**（custom_minimum_size 改 580x160→520x150；grid h/v separation 12→10）。
3. **进度条按原版四件套**：条底 40k_campaign_bar_bg (modulate 0.3,0.29,0.69) 220.7x26.2 @容器(152,102.5)；Fill 40k_campaign_bar_fill (1,0.51,0) 同位置按比例宽；端头 end 40k_campaign_bar_end 29.4x31.9 贴右侧；Outline 40k_campaign_bar_outline (1,0.84,0) 同条底叠顶（金色描边）；counter '100/200' @(196.1,106.9)。删 40k_bt_underbutton/40k_generial_bar_fill 用法。
4. **奖励行**：rewards 文字 '2 points' 白 @(402.7,102)（或 'x points' 用实际点数）+ **rewardIcon 40k_Achievements_icon_seal points 28.5x39.1 @(374.1,97.2)**（贴图已在 scenes_sprites ✓）。
5. 文字：title Bold（autosize 12-35 → Godot 约 22-24 加粗），desc 15→约 20；标题去掉 "✓" 附加符号（原版 title 无勾）。
6. 图标 Image @(15,10)；删 'Achievements'/'All progress…' 自创标题（如保留须有父场景框架理由）。

### 4.3 4-Tab 竖栏共享（rewards/campaign/quests/forge 统一）

原版（§1.1）：Tab Buttons (167.2,71) 165x1009 40k_main_tab_background；4 键 165x180（布局组 padding top 120、间距 0 → 首键 y191）；每键 = 选中红高亮 40k_main_bt_selected BW(1,0,0,1) + Icon 126x126（Missions=40K_rewards_bt_missions / Campaign=40k_main_bt_campaign / Forge=40K_rewards_bt_forge / **Booster Packs=40K_shop_bt_boosters**——项目缺此贴图，需从 `d:/2/Warpforge_tools/data/ui_extract/menus_assets_all/Sprite/40K_shop_bt_boosters.png` 补入）+ Label 155x37.9 nametag + 文字 36px 全大写（Booster Packs 25.65）+ 角标 35。
现有 rewards.gd 差异：5 键（第4键 'The Vault'→应为 'Booster Packs'；多 'Menu'）、无图标/nametag/角标、键位 y=71+ti*180（应为布局后 191 起？——原版布局组 padding top 120，无图标与 nametag 是主要差距）。

### 4.4 一行传阅要点（主代理实施时注意）

- 全部所需贴图**项目内已有**（scenes_sprites：WF_Campaign_Levelspot(.png/-Premium)、Border Thick Circle FX、40k_campaign_bar_bg/fill/outline/end、40k_Achievements_icon_seal points、40K_genearl_icon_Campaign points、WF_Campaign_Info_Background、40K_generic_bt_info、40k_campaign_Premium-icon、40k_general_popup_simple red/greyscale、40k_bt_underbutton、40k_Generic Smooth line、40K_settings_button_hover、40k_main_bt_campaign、40K_rewards_bt_missions/forge/achievements、40K_notification_number；仅 **40K_shop_bt_boosters** 缺）。
- Point Icon 的 100x66 是因 m_LocalScale=2.0（rt_scale_map.json 实锤 RT -3407274137851521281 {'x':2.0,'y':2.0}），直接布 100x66 即可（不用再乘 2）。
- 原始 JSON 中 'Unlock Button' 无按钮文字（Point Count '100' 与 Claimed Text 'Change Deck' 均 size≈0/inactive）——按钮视觉即 Mulligan 底，可加 'Change Deck' 35px 或保持无文字。
- achievements 描述/标题字号均为 TMP autosize(min12 max35 base36)，不同实例 dump 值不同（12/29.55/35）——实现按 20-24px 视觉近似即可，精确值以容器矩形 359 宽为约束。
- 依据 `audit_D_campaign.md`（56 规格元素，35 命中 21 未命中）与 `audit_D_achievements.md`（18 元素 14 命中 4 未命中 ContainerHolder/rewardIcon/Fill Area/Outline）。未命中项与本报告 3.1/3.2 逐条对应（ContainerHolder 为运行时容器器可用 GridContainer 替代；Fill Area/Outline/O container 在本报告 2.2 给出精确坐标与贴图）。

---

## 5. 原始 JSON 关键文件索引（供主代理直接引用）

| 界面 | 根 GO 文件（解包整理/03_界面UI/菜单/GameObject/） | 根 RT |
|---|---|---|
| Rewards Base Submenu Variant | Rewards Base Submenu Variant_-8343312282719283457.json | 507527829764970239 |
| MissionsRewardsButton/CampaignRewardsButton/Forge Button/Menu Navigation Panel Button | …6509742238143682303 / -309639361232693505 / -406639554272618753 / 4168857396300748543 | 6051947520314382079 等 |
| Campaign Tab（子菜单实例/inactive） | Campaign Tab_-880831270227011841.json | -7627375673320990977 |
| Campaign Tab（独立实例/active） | Campaign Tab_5958516118268259725.json | -1280772513942098547 |
| Campaign Header（子菜单实例） | Campaign Header_-7857794479342151937.json | 5567135349741328127 |
| Point Icon（子菜单实例，scale2） | Point Icon_-6352502784788588801.json | -3407274137851521281 |
| Campaign Track（子菜单实例） | Campaign Track_-5801902842250848513.json | -738854002306640129 |
| Campaign Node | Campaign Node_666348682854551431.json | 6791446287889289095 |
| Node Line | Node Line_8711542813501762573.json | 4183496315837885453 |
| Campaign Reward Window | Campaign Reward Window_-3992165112361214842.json | 2439992069526822022 |
| Achievements Tab | Achievements Tab_7942391680202248253.json | -7048126750119620547 |
| Achievement Container（模板/0x150） | Achievement Container_-3625966182550532035.json | -6857241059549441987 |
| Achievement Container（520x150 基准） | Achievement Container_8365984317912611378.json | 2146878903578950194 |
| Achievement Type Toggle（Trophies Tab 键） | Achievement Type Toggle_1330132040127904306.json | 860611429324913202 |
| Trophies Tab | Trophies Tab_-1698997230529643982.json | 8482975979751504434 |
| Campaign Army Item Button | Campaign Army Item Button_6426011274901591754.json | -6148399272832133430 |

（dump 文件副本供复核：`d:/2/_tmp_rewards_submenu.txt`（562 行）、`_tmp_campaign_tab_a/b.txt`、`_tmp_campaign_reward.txt`、`_tmp_campaign_node.txt`、`_tmp_achievements_tab.txt`、`_tmp_trophies_tab.txt`、`_tmp_achv_toggle_profile/root.txt`）
