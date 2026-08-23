# 子代理报告：Rewards（任务中心）原版规格权威表 — 0823

> 任务：完整读取 rewards（任务中心）界面说明书 + 原始 Unity JSON + 项目现状，输出重构唯一依据。
> 来源：④ `d:/2/解包整理/说明书/04_界面UI/`（界面索引 239 行 / 菜单全树 12171-12732 / 要点第3块 #61 / 要点第4块 #0）
> 原始 JSON：`d:/2/解包整理/03_界面UI/菜单/`（dump_go_tree.py 全树 562 行 → `d:/2/_dump_rewards_tree.txt`，下文"dump 行 N"指向它）
> 权威坐标：chain_rect.py v2 链式换算（1920×1080，y 翻转/pivot/锚点中心/父链/scale），与 `d:/2/audit_D_rewards.md` 一致。
> ⚠️ 关键语义修正：dump_go_tree.py 行尾 "active" 标记是**反义**（脚本 `' active' if not m_IsActive`），即标 active 的实为**inactive**。已用原始 GO JSON 逐一复核（Daily Login Container=False、description=False、Raycast target=False 等）。菜单全树 "(inactive)" 为准。

---

## 0. 一句话结论（重构核心）

原版 = **Rewards Base Submenu Variant**：全屏任务中心，左侧竖排 **4 键**（Missions / Campaign / Forge / Booster Packs），**同屏切换** 3 个内容 Tab（Missions Tab / Forge Tab / Campaign Tab），Booster Packs 键并非 Tab（TabGroup 脚本只注册 3 个 Toggle，它是独立的 Menu Navigation Panel Button 跳转商店卡包页）。
每日 7 天签到在**原版是另一个全屏界面 Daily Reward Popup**（说明书第1块 #22，行 810），任务页里只有一个 **inactive 的 Daily Login Container 卡片**（40K_missions_display_Daily vertical 底，'Daily Login Bonus' 卡）。

项目现状：rewards.tscn = Daily Reward Popup 内容（7 天横向滚动）做成了独立场景，且其**滚动区/标题/时钟 x231-240 压在 x167.2-332.2 的 Tab 栏上拦截点击**；Tab 栏是 5 键（多 The Vault/Menu，缺 Booster Packs）且**点击跳子场景**（quests.tscn/campaign.tscn/forge.tscn）而非同屏切换。

---

## 1. 原版元素全表（Rewards Base Submenu Variant 整树）

根 GO：`GameObject/Rewards Base Submenu Variant_-8343312282719283457.json`（RT PathID 507527829764970239，GameObject reprint 见菜单全树 12171 行）
全屏 1920×1080，m_IsActive=true。

### 1.1 根 → Content Area → Tab Buttons / Tabs（菜单全树 12172-12204 | dump 1-34）

| GO 名 | 类型/组件 | 原始 RT | Godot 绝对 (x,y,w,h) | 贴图(PathID→Sprite 名) | 文字/字号/颜色 | 备注 |
|---|---|---|---|---|---|---|
| Content Area | RectTransform | anchor(0,0,1,1) offsets(167.2,0,0,-70.9) pivot(0.5,0.5) | **(167.2, 70.9) 1752.8×1009.1** | — | — | 内容区左缘 167.2，顶 70.9（导航条+金币条下方） |
| Background | Image | anchor(0,0,1,1) pivot(0,0.5) | 同 Content Area | m_Sprite=**0 无贴图**，color(1,1,1,1) | — | 纯色透出场景底 |
| Tab Buttons | Image + **VerticalLayoutGroup** + **TabGroup 脚本** + ToggleGroup + Gradient | anchor(0,0,0,1) pivot(0,0.5) size(165,-0) | **(167.2, 70.9) 165×1009.1** | -2833714758900102314 → **40k_main_tab_background**（`03_界面UI/图集/0_mainmenu/Sprite/40k_main_tab_background.json`） | — | ① **VerticalLayoutGroup：Padding Top=120，spacing=0，ChildAlignment=1(UpperCenter)，ChildControlWidth=1，ChildControlHeight=0，ForceExpandWidth=1，ForceExpandHeight=0** → **运行期 4 键竖排：y 190.9-370.9 / 370.9-550.9 / 550.9-730.9 / 730.9-910.9（各高 180、宽 165）**（静态 RT 只给 w0 h180，audit/chain_rect 的 y990 是未排布假值！）② **TabGroup 脚本 options 仅 3 条**：tab:-6485706199792675073+toggle:-4134137194770196737 / tab:6512207849649477375+toggle:1881031983073597183 / tab:3903199890974775039+toggle:2894314079170729727 + group:-934655292178491649（ToggleGroup, AllowSwitchOff=0）；tabButtonPrefab 5159086895759431423 |
| Tabs | RectTransform | anchor(0,0,1,1) | (167.2, 70.9) 1752.8×1009.1 | — | — | 内容 Tab 容器 |
| Shadow (Tab Buttons 内) | Image | anchor(0,0,1,1) pos(-58.7,0) size(-117.4,0) | 绝对 x167.2 起 w47.6（audit：Shadow (167.2,70.9) 47.6×1009.1） | -8666545702653119048 → **40k_main_tab_shadow** | color(0,0,0,0.47) | 栏右缘阴影 |
| Shadow (1)（Tabs 内, inactive） | Image | — | 绝对 x330.4 w49.4 | 同 40k_main_tab_shadow | color(0,0,0,0.47) | Forge/Campaign 页左缘阴影（默认隐藏） |

### 1.2 Tab Buttons 下 4 键（菜单全树 12175-12202 | dump 5-33）

共性（4 键相同）：RT anchor(0,0,0,0) pivot(0.5,0.5) offsets(0,0,-90,90)（= 高 180 居中，静态值）
- **Highlight**（子）：Image m_Type=**1(Tiled)**，m_Sprite 503137736542995528 → **40k_main_bt_selected BW**（`0_mainmenu/Sprite/40k_main_bt_selected BW.json`），**color(1,0,0,1) 纯红**；由 Toggle 控制显隐（Toggle.graphic=Highlight、toggleTransition=1 ColorTint、onColor=白/offColor=0.75 灰）
- **Icon**（子）：Image m_Type=0(Simple) pivot(0.5,0.7) 填满键区（RT anchor 全拉伸）；纹理 126×126；另带 TabButton id 脚本（见下）
- **Label**（子）：Image 1838051009033412331 → **40k_main_bt_nametag**（名牌底 155×37.9）anchor(0.5,0.5) pivot(0.5,0) pos(0,-72.2) → 键底部；含 **TabButtonLabel**：Text 36px（Booster 25.65px）白
- **Badge Highlight**（子）：Image m_Type=0(Simple) **40K_notification_number**（35×35）color(0.736,0.736,0.736)；带 notificationDefinitions/showCounter/counterText 角标计数脚本 + **OneText** 空文本 34px 白

| 键 | GO (PathID) | Id | Icon 贴图 | 名牌文字/字号 | Badge 相对 pos | 运行期绝对区（VerticalLayoutGroup 推导） |
|---|---|---|---|---|---|---|
| MissionsRewardsButton | 6509742238143682303（Toggle: -4134137194770196737, id 脚本: -1040296725195778305） | RewardsMenu_MissionsButton | 6056325442236481915 → **40K_rewards_bt_missions**（`03_界面UI/菜单/Sprite/`） | **Missions** 36px | (51.7,-27.2) | **(167.2,190.9) 165×180** |
| CampaignRewardsButton | -309639361232693505（Toggle: 1881031983073597183） | RewardsMenu_CampaignButton | -7386844692906402995 → **40k_main_bt_campaign**（0_mainmenu 图集） | **Campaign** 36px | (51.7,-27.2) | **(167.2,370.9) 165×180** |
| Forge Button | -406639554272618753（Toggle: 2894314079170729727） | RewardsMenu_ForgeButton | -3881622862070525641 → **40K_rewards_bt_forge** | **Forge** 36px | (51.7,-27.2) | **(167.2,550.9) 165×180** |
| Menu Navigation Panel Button | 4168857396300748543（仅 Button，**非 Toggle**） | — | 9037460324982195104 → **40K_shop_bt_boosters**（`03_界面UI/运营图标/Sprite/`） | **Booster Packs** 25.65px | (51.7,**47.9**)（+47.9=中心下方，贴底） | **(167.2,730.9) 165×180** |

- 键间距离 180 精确相邻（spacing=0），Top padding 120（板块下方余 169.1）。
- 名牌 TabButtonLabel 基准：Label 底=键中心下方 72.2，名牌 37.9 高 → 名牌绝对 y = 键中心+34.3 ~ +72.2，**名牌 x[172.2,327.2]**（155 居中于键）。角标 badge 35×35 中心 = 键中心+(-27.2→y 转正)27.2 → Missions 角标中心 (301.4, 308.1)；Booster 角标中心 (301.4, 868.8)。
- **点击行为**：Missions/Campaign/Forge 是 Toggle 组内同屏切 Tab（TabGroup.persistent）；Booster Packs 是 Button → 跳 Booster Packs（商店卡包页）。

### 1.3 Missions Tab（active，默认页）（菜单全树 12205-12621 | dump 35-451）

Missions Tab GO -3261567823877957889：anchor(0,0,1,1) pos(-0.2,0.9) → 绝对 **(166.7,69.2) 1753.3×1010.8**。内容：

**A. Normal Missions（372.4, 95.8）1519×723.8**（Menu树 12206 | dump 36）：anchor(0,1,0,1) pivot(0,0.5) pos(205.7,-388.5)——绝对 x372.4（=167.2+165+40.2 阴影后），顶部 95.8。
- **Special Missions（372.4, 12.4? 视顶）896.1 宽**（audit (372.4,12.4) 896.1×639.7 | dump 37）：anchor(0,1,0,1) pivot(0,1) size(779.2,556.2)。含两块：
  - **Daily Login Container**（GO -3916738376757274881，**m_IsActive=false** | dump 38-87）：动态激活的"每日登录奖励"卡。卡底 **40K_missions_display_Daily vertical**（6122037746554878635）；header: name '**Daily Login Bonus**' 35.15px + info 40K_generic_bt_info 41×41；body: description(inactive, 空) + image **40K_missions_icon_login bonus**（4018610588019826553, 拉伸 325×261 + Button）；progress(默认 inactive): **Mission Milestones Progress Bar** 302.6×61.5（Progress Bar=40k_generial_bar_empty tint(1,0.59,0) + Fill 40k_generial_bar_fill tint(1,0.77,0.33) + Handle(11.6 宽暗金) + progress text '**52/500**' 32.45px）+ Handle Slide Area(inactive)；footer: Rewards×2（Reward Display Mission：① Currency(40k_topmarquee_currency_crystal)+count '**100**' 40px ② Campaign Points(40K_genearl_icon_Campaign points_big + 阵营图)+count '**?**'）+ **Generic UI Button** '**Collect**'（40K_button 256×74.6 tint(1,0.47,0.1) 44px）+ **TimerHolder** '**Resets in 12h 34 m**' 38px；debug_buttons（Reset/Re-Roll/+1/+5/Complete/00:00，40K_button 品红，仅开发）
  - **Daily Skulls Mission Container**（GO 7706541736523601663，**active** | dump 88-178）：同卡底；header: name '**Daily Skulls**' 36px + info；body: Image '**40K_missions_icon_Daily skulls**' 66.2×64.6 + counter '**x160000**' 30px + image（同 skull 纹 221.7×229）；progress: milestones→steps→**5× Mission Milestones Step 40×40**（holder=Image 黑(0,0,0) + CheckMark **40K_settings_icon_checkmark** + text '1' 42.2px）；footer：Rewards×2（Icon Campaign Points Drawer Variant：Content 1080×1080（过屏裁剪）+ Campaign Glow 40K_genearl_icon_Campaign points_big + Converted Drawer(inactive: Price Display 2000 金 + AlreadyOwned 'Already Owned' 75px) + Ephemeral Drawer(inactive: WF_icon_clock '24 hours' 65px)）+ count '200'/'100' 40px + Collect（Button Text 44px）+ Timer 'Resets in 12h 34 m'；debug_buttons（同上）
- **Daily Missions（1271.3, 12.5）620.1×639.3（含 scale 1.15 累积）**（dump 179-324）：anchor(0,1) pivot(0,1) pos(898.9,0) size(539.2,555.9)（绝对 x1271.3）。含：
  - **Daily Missions Holder**（content 容器）
  - **Daily Mission Container ×3**（x3 同构 | dump 181-324）：Image **40K_missions_display_Daily horizontal**（8657822044864735361）**0×150**（运行期由脚本排布成 3 行）；每行：title(inactive 'Deal 500 damage to enemy units' 30px) + description（同文 40px）+ timer '**Available in 64h**' 40px + Separator Line（color(0.25,0.25,0.41,0.59) 1.6 宽）+ Rewards（Reward Display Mission **Vertical Variant** 126.3×150 + drawerHolder + Icon Campaign Points Drawer 1080² + count '100' 40px）+ **Mission Milestones Progress Bar**（'52/500' + bar 填充）+ **Generic UI Button** 'Collect'（254.6×56.5 tint(1,0.53,0)）+ **Trash mission**（40k_general_bt_yellow 49.1×49.4 + 40k_general_bt_yellow_delete 图标 + 'X' 30px inactive）+ **Mission Debug Buttons**（Reset/Re-Roll/Complete +1/+5/00:00，开发用）
  - **Mission Header**（dump 325-328）：name '**Daily Missions**' 36px（anchor(0.03,0.5,0.84,0.5)）+ info **40K_generic_bt_info** 41×41 + **Refill Counter** '**0 Disponible**' 36px（右端）
- **Weekly Mission Holder（372.4, 759.8）1519×227.5**（dump 329-451）：GO 7218257402582079231。Weekly Mission 内：
  - background **40K_missions_display_Weekly**（-1583576307776439273，整条横纹理）1519×227.5
  - header: name '**Weekly Challenge**' 36px + info 41×41
  - body（inactive）：description + image 40K_missions_icon_Daily skulls 325×94.2
  - progress→**Mission Progress Bar**（'13/15' 33.15px + 40k_generial_bar_empty/fill 1008×22.8 + Handle 4.1×50.6 带 counter）+ **Mission Milestones Progress** 1068.4×158.6：steps → **4× Weekly Mission Milestones Step（*GM 名字重复 '(3)'*）70×70**（Image **40k_missions_milestone_off** + **CheckMark=40k_Crate_Tier1_Iron** 72.9×59.1（宝箱=里程碑奖励按钮！）+ text '5' 50px）
  - footer（1564,852 301×102）：Rewards（inactive，4× Reward Display Mission 250×113 横排 x486/736/986/1236 —— 绝对 footer 内偏移 -728.5, count 200/100/100/100 30px）+ **Generic UI Button** 'Collect' 294.3×74.6 + TimerHolder '**Ends in 12h 34 m**' 38px
  - debug_buttons（inactive）

### 1.4 Forge Tab（inactive 默认）（菜单全树 12622-12675 | dump 452-505）

Forge Tab GO 3399233590492468991：绝对 **(330.7, 71.1) 1589.3×1008.7**（=Tab 栏 165 + Shadow 后内容起始 x330.7！）

| 元素 | 绝对坐标 | 贴图/文字 | 备注 |
|---|---|---|---|
| Background | 同 Tab | 无贴图 color(0,0,0,1) | 黑底 |
| ⤷ Warp | **(741.8, 88.5) 767×974** | 2374284676670985858 → **40K_ArmyTrack_bg** | 中央涡旋，中心=Tab 中心 (1125.35,575.45) |
| ⤷ War ParticleSystemUI | 中心同 Tab，1483.6² | ParticleSystem nebula | 星云粒子 |
| Ready for level up | **(1028.1, 424.1) 194.5×302.8** | Glow: '**Glow UI W40K**' 700² tint(1,0.17,0.88) + 上下粒子(Up y191.5/Down y949.5 绝对) | 升级就绪光 |
| Rewards Scroll View | **(331.0, 318.6) 1588.7×761.4**（vision center 575.4-123.8±380.7） | Viewport -426171492875694260 + Rewards Content 122×761.4 | 等级奖励列表（行=Forge Reward，未在树内=动态生成）|
| Forge Army Selector | **(588.2, 71.6) 1074.3×125.1** | Separator Line '**40k_main_line purple**' (491.4,191.4) 1267.9×6 + Viewport + Army Content 0×126（动态） | 阵营切换行 |
| Background Elements | 同 Tab | — | — |
| ⤷ Decoration Top | **(444.7, 185.1) 273×210** | 7817997903597179370 → **40k_rewards_forge_decoration 2** | |
| ⤷ Column Left | **(330.7, 71.1) 358.6×1396.9** | Culumn Top **40k_rewards_forge_decoration_Column_top** 319×460 / Candle '40k_rewards_forge_decoration 1_candle' 40×59 / Culumn Mid _Column_mid 206×461 / Culumn Down _Column_down 213×474 / Light Candle '...1_candle_light' 142.6×175.5 | 左柱（顶对齐，上边=71.1-223.5） |
| ⤷ Column Right | **(1920.0, 71.1) 358.6×1396.9**（anchor(1,1) 镜像） | 同左柱贴图镜像排列 | 右柱 |
| Selected Army Info | **(619.4, 195.8) 621.3×122.7** | ArmyText '**Ultramarines**' 41.3px / LevelText '**Level 1/50**' 32.38px / **Army Icon 40k_DeckSelection_icon_FactionUM** 125.3² / Xp Points Icon(inactive) '**40K_general_icon_Forge points**' 53² + TotalXp '**154748**' 32.7px | 中心信息块 |
| Debug Add points (inactive) | (947.4,214.2) 203.6×53.9 | 40K_button tint(1,0,0.95) + InputField | 开发 |
| Debug Set Forge (inactive) | (1278.5,215.9) 同结构 | 'Set Forge Level' | 开发 |
| Help Icon | **(1685.2, 215.9) 52.2²** | 40K_generic_bt_info | |

### 1.5 Campaign Tab（inactive 默认）（菜单全树 12676-12731 | dump 506-561）

Campaign Tab GO -880831270227011841：绝对 **(330.7, 70.9) 1589.3×1009.1**

| 元素 | 绝对坐标 | 贴图/文字 | 备注 |
|---|---|---|---|
| Campaign Background | 同 Tab | 无贴图黑底 color(0,0,0,1)；Background Image 无贴图（脚本换图）| |
| Campaign Army Selector | **(745.9, 70.9) 1174.4×137** | Background 黑 0.35 透明度 (643.2,71.4) 1277×136 + Viewport + Army Content（动态 13 阵营） | 顶部右半 |
| Campaign Header | **(330.7, 60.9) 460.2×165** | Image **6473405944757030420 → WF_Campaign_Info_Background**（`0_mainmenu/Sprite/`） | 左上头部底 |
| ⤷ Army Icon | 342? absolute (345.7,60.9) 135×165 | **40k_DeckSelection_icon_FactionBlackLegion**（5519774263930623761）| 注：这是默认阵营图标（BlackLegion? 实际脚本换 UM）|
| ⤷ Title | (480.7,60.9) 225×74.3 | '**ULTRAMARINES**' 31.75px | |
| ⤷ Points | (480.7,151.7) 368.2×33 | '**Points: 69**' 34.8px + Point Icon（40K_genearl_icon_Campaign points 底 + 阵营图标）| |
| ⤷ Info Button | (719.8,94.0) 41.2² | 40K_generic_bt_info | |
| ⤷ Debug Point Button (inactive) | (1146.2,91.6) 245×67.7 | **UI_Button_Mulligan** + 'Change Deck' 36px | |
| ⤷ Premium Button Container (inactive) | (743.2,60.9) 262.5×82.5 | Premium Button UI_Button_Mulligan 'Premium' 36.6px / Premium pruchased **40k_campaign_Premium-icon** 54.1² + 'Premium' 29.7px | |
| Campaign Track | **(330.7, 335.5) 1589.6×709** | Viewport(45.9? 中心 y575.4-114.5=460.9 ±354.55 → y[106.3,815.4]?? audit 给 y285.5-336?——按 audit 表: Viewport (330.7,285.5) 1589.6×759; Content 200 宽×659 | 轨道滚动区（节点动态） |
| Premium Panel | (344.3, **1080**) 376×0（**屏外隐藏**） | WF_UI_Ranked_Background_Gold + Title 'Premium Campaign daily bonus' 33.3px + Points '200' 61.2px + 图标 1080² 抽屉 + Continue (UI_Button_Mulligan 'Continue' 49.35px) + Timer WF_icon_clock '**Siguiente: 5d 20h 15m**' 37.9px | 高级每日奖励下滑面板（默认收起） |
| Tutorial Message (inactive) | 绝对 (1184.1,220.4) 567.1×120.2（RT pos(342.3,-209.5) anchor 拉伸） | 40k_popup 图/40k_popup_texture + 'Choose your favourite faction...' 35px + Border Line Only Horizontal FX 上下光条 | 新手提示（默认隐藏） |

---

## 2. 4 Tab 竖栏权威规格（重构 Tab 栏必须遵守）

1. **栏区**：x[167.2, 332.2]（165 宽），y[70.9, 1080]；底图 40k_main_tab_background；右缘阴影 40k_main_tab_shadow 47.6 宽 x167.2 起（即阴影在栏右侧 x[332.2, 379.8]）。
2. **4 键竖排（运行期）**：Top padding 120 → 键 y = 190.9 / 370.9 / 550.9 / 730.9，各 165×180；顺序 Missions→Campaign→Forge→Booster Packs；底部留 169.1。
3. **键视觉**（从下到上）：Icon 全键区拉伸（纹理 126×126，pivot 0.5/0.7）→ 名牌 Label(40k_main_bt_nametag 155×37.9) 位于键内 y 底 72.2 处（Center+34.3~+72.2），TabButtonLabel 白字 36px（Booster 25.65px）→ Badge Highlight(40K_notification_number 35×35 灰 0.736) 在名牌右上（相对中心 (51.7,-27.2)，Booster (51.7,+47.9)），内含 OneText 空 34px（角标数字由 notification 脚本填）→ Highlight(40k_main_bt_selected BW **Tiled** 纯红 (1,0,0)) 整键，**仅 Toggle 选中键显示**（Toggle.graphic=Highlight，Transition=ColorTint：onColor 白 / offColor 0.75 灰）。
4. **切换机制**：3 个 Toggle（TabGroup options）控制 Tabs 下 3 个子 Tab 显隐（同屏），ToggleGroup 互斥（AllowSwitchOff=0）；**Booster Packs 键无 Toggle**，是普通 Button。
5. **Tab 键文字颜色**：TabButtonLabel 白色 (1,1,1,1)（项目现用金白 (0.996,0.929,0.710)——**不符**；原版名牌文字纯白）。

## 3. 各 Tab 内容面板结构（重构目标）

| Tab | 内容区绝对范围 | 内部布局 |
|---|---|---|
| **Missions** | (372.4, 95.8) 1519×723.8 起（顶部留 95.8 给标题带） | 左 779.2×556.2：Daily Login 卡(inactive) + Daily Skulls 卡 336×555；右 620.1 宽：Mission Header('Daily Missions'+Refill '0 Disponible') + 3× Daily Mission Container 行（各 ~150 高，含 Collect/Trash/奖励/进度 '52/500'）；底部 (372.4,759.8) 1519×227.5：Weekly Challenge 横条（1008 进度条 '13/15' + 4× 70 里程碑含宝箱按钮 + Collect + Timer 'Ends in 12h 34 m'）|
| **Forge** | (330.7, 71.1) 1589.3×1008.7 | Warp 涡旋 (741.8,88.5) 767×974 + 左右双柱蜡烛 + 顶部装饰 (444.7,185.1) + 阵营选择行 (588.2,71.6) 1074.3×125 + Selected Army Info (619.4,195.8) + Rewards 等级列表 Scroll (331,318.6) 1588.7×761.4 + Help (1685.2,215.9) |
| **Campaign** | (330.7, 70.9) 1589.3×1009.1 | 顶右阵营选择 (745.9,70.9) 1174.4×137 + 左上 Header (330.7,60.9) 460.2×165（WF_Campaign_Info_Background）+ 轨道 (330.7,335.5) 1589.6×709 + Premium Panel（屏外隐藏）+ Tutorial Message（inactive）|

> 注意 Missions 内容 x 起点 372.4（不是 330.7！）：Missions Tab 是 1753 全宽页（Tab 阴影被特殊处理），Forge/Campaign Tab 才是 1589.3 宽 x330.7 起。

## 4. 项目现状 vs 原版 差异清单

### 4.1 rewards.gd（现 = Daily Reward Popup 内容，528 行）

| # | 元素 | 原版 | 项目现状（行号） | 判定 |
|---|---|---|---|---|
| 1 | 场景定位 | Rewards Base Submenu Variant=任务中心 | rewards.tscn = 7 天签到横向页（抄自 Daily Reward Popup [行810]） | **整体错位**（错做成另一界面）|
| 2 | 滚动区 | 原版任务中心**无滚动区**；Daily Reward Popup 为 Rewards Scroll View (242,159) 1705×806 | scroll (231,153) 1660×905 (L199-205) | **x231 < 332.2 = 压 Tab 栏 101px → 拦截 Tab 点击**（用户报告的"x231 压 Tab 栏"真相）|
| 3 | 标题 | 无标题 | 'Daily Rewards · 7-day streak' (240,130) (L135) | 多余且压 Tab 栏 |
| 4 | 时钟 | Daily Reward Popup 无硬编码时钟（有 Timer/倒计时在卡片内） | clock (240,186) + 'Resets daily · Day N' (278,184) (L136-144) | 多余且压 Tab 栏 |
| 5 | Tab 键数 | **4 键**：Missions/Campaign/Forge/**Booster Packs** | **5 键**：Missions/Campaign/Forge/**The Vault/Menu** (L157-163) | 缺 Booster Packs；多 2 个自创键 |
| 6 | Tab 键 y | 190.9/370.9/550.9/730.9（layout top pad 120）| 71/251/431/611/791（71+ti*180，L167）| 偏移 +119.9（项目键紧贴顶部，无 120 padding）|
| 7 | Tab 键结构 | Icon(40K_rewards_bt_missions/40k_main_bt_campaign/40K_rewards_bt_forge/40K_shop_bt_boosters，126²) + 名牌(40k_main_bt_nametag+文字36/25.65px) + 角标(40K_notification_number 35²+OneText) + 选中红 Tiled 高亮 | 仅文字 Label 24px + 红色高亮叠加（仅 Missions 有）(L169-189) | **缺图标/名牌/角标**；字号 24 vs 36；高亮调制红 (1,0.08,0) vs 原版 (1,0,0) close |
| 8 | Tab 文字色 | 白 (1,1,1) | (0.996,0.929,0.710) 金白 (L187) | 不符 |
| 9 | 切换方式 | 同屏切换（ToggleGroup 互斥）| `SceneTransition.change_scene(quests/campaign/forge/gacha/main_menu)` (L193-195) | **子场景跳转 ≠ 原版**；Missions 键指 quests.tscn 且"当前页"无法真实表示 |
| 10 | 内容宽度 | Missions 内容 x372.4 起 1519 宽 | 每日卡 327 宽×7=~2400 横向滚动 | 结构无对应（属另一界面）|
| 11 | 金币条/背景 | 原版场景由场景级全局（导航+顶栏）承载——**Content Area 内无金币** | 自建金币条 (1530,14) + MenuBg (L105-132) | 场景级导航 NavBuilder REWARDS 已带左栏；金币位置为通用约定（其他界面同款，接受）|

### 4.2 quests.gd（现 = 任务页，642 行）

| # | 元素 | 原版 | 项目现状 | 判定 |
|---|---|---|---|---|
| 1 | 布局 | Special Missions 左区（Daily Skulls 卡 336×555 竖）+ Daily Missions 右列表（3×150 行）+ Weekly 底条 | 3 个 336×555 容器横排 x206/606/1006 (L216-221) | **布局完全不同**；应为"1 左卡 + 右列表 + 底条" |
| 2 | 任务数 | Daily Skulls + Daily Missions×3 + Weekly | 自定义 3 任务（skulls/wins/collect）+ Weekly | 概念近似但容器结构不同：原版右列表 150 高横条 ≠ 555 高竖卡 |
| 3 | 标题 | Mission Header 'Daily Missions' 36px + Refill Counter '0 Disponible' | 'Missions' 44px (1274,98) (L161) | 文字/字号/位置不符（标题应为 x1290 y99 36px）|
| 4 | 入口按钮 | **无**（Campaign/Forge 是左侧 Tab） | 自创 'Campaign' 按钮 (1274,152) + 'Achievements' 按钮 (1484,152) + 辉光 (1452,74) (L162-211) | **多余（原版无）**；重构后删除（Campaign 变 Tab）|
| 5 | 竖卡里程碑 | Daily Skulls 卡：5× 40×40 里程碑 | 每容器 4× 40×40 (L390-426) | 数量 4 vs 5（卡片语义不同）|
| 6 | Weekly 条 | (372.4,759.8) 1519×227.5，背景 40K_missions_display_Weekly，进度 1008×23，4×70 宝箱按钮 | (206,691) 1519×228（L231），背景用 UI_Deck_Information_submenu_Back 近似 | **坐标 -166.4/-68.8**；背景替代（原版有正版纹理 40K_missions_display_Weekly）；里程碑是 milestone_off 圆石+数字 vs 原版 40k_Crate_Tier1_Iron 宝箱+数字'5' |
| 7 | 任务容器底图 | 正版 40K_missions_display_Daily vertical | 同 (TEX_CONTAINER L8) | ✓ 已用正版 |
| 8 | Collect | 40K_button tint(1,0.47,0.1) 256×75 | (40,370) 256×75 40K_button tint(1,0.47,0.1)（D组已修）| ✓ 一致（位置随容器）|
| 9 | NavBuilder | 场景级导航 | NavBuilder.build(self,"REWARDS") (L71) | 重构为 Tab 内容面板后应移除（或保留独立场景时保留）|

### 4.3 campaign.gd（626 行）

| # | 元素 | 原版 | 项目现状 | 判定 |
|---|---|---|---|---|
| 1 | 场景定位 | Campaign Tab（内容 x330.7 起 1589.3 宽）| 独立场景，NavBuilder REWARDS | 重构后应变为 Tab 面板 |
| 2 | Header 底图 | **WF_Campaign_Info_Background**（0_mainmenu 图集）| **40K_tab_button_overwindow**（借标签高亮纹理，L9）| **错误替代**（违反复刻一致性；原版正版贴图存在！）|
| 3 | Header 位置 | (330.7,60.9) 460.2×165 ✓ | (331,61) 460×165 (L183-184) | ✓ 一致 |
| 4 | 阵营行 | (745.9,70.9) 1174.4×137，y 顶 70.9 | y=95，x746，按钮 84² 且无背景条 (L136-137) | y 差 24.1；尺寸/背景缺失 |
| 5 | 轨道 | (330.7,335.5) 1589.6×709 | (331,335) 1590×709 (L212-213) | ✓ 一致 |
| 6 | Premium Panel | 屏外 (344.3,1080) 376 宽 高级每日奖励面板（Continue + Timer 'Siguiente: 5d 20h 15m'）| 无 | 缺失（单机可视为高级已解锁，降级可接受但需注明）|
| 7 | Tutorial Message | inactive 新手提示 | 无 | 缺失（可接受，引导另有）|
| 8 | Points | 'Points: 69' 34.8px (480.7,151.7) | (470,130) 18px (L204) | 位置略差/字号不符 |
| 9 | Army Icon 默认 | 40k_DeckSelection_icon_FactionBlackLegion 135×165 | GameData.army_icon_path 动态（UI 同尺寸 120×150 @ (331,66)）| 尺寸 120×150 vs 135×165 略差 |

### 4.4 forge.gd（566 行）

| # | 元素 | 原版（Forge Tab，x330.7 体系）| 项目现状 | 判定 |
|---|---|---|---|---|
| 1 | 坐标系 | 内容绝对 x330.7 起 | 注释"原版 [164,0 1756x1080]"（L3）——沿袭错误根（164 是 Tabs 之前的另一版根 or 菜单全 Tree 显示值）→ 所有元素以 x164 为 0 | **整体左移 166.7** |
| 2 | Warp | 绝对 (741.8,88.5) 767×974 | (658,53) (L111-112) | **-83.8/-35.5 错位**（原版 Warp 中心=Tab 中心 (1125.35,575.45)）|
| 3 | Column Left/Right | 绝对 (330.7,71.1)/(1920,71.1) 358.6² | x164 / x1588.4 (L121-122) | -166.7 / +331.6(右柱对齐右缘 1920 应为 1561.4?)——**右柱 x1588.4 vs 原版 1561.4?** 原版 Column Right anchor(1,1) 绝对 x[1561.4,1920]；项目用 1588.4 差 27（2026-08-20 已"核查改"但仍不对：原版右柱左边=-373 宽从右缘 → x1561.4） |
| 4 | Decoration Top | 绝对 (444.7,185.1) | (278,114) (L123-124) | -166.7/-71 错位 |
| 5 | 阵营行 | (588.2,71.6) 1074.3×125.1 | (421,12) 1241×130 + Sep (325,120) (L134-149) | x/y 均差 |
| 6 | Selected Army Info | (619.4,195.8) 621.3×122.7 | (455,117)（L159-160 起）| -164/-79 错位 |
| 7 | 等级列表 | Rewards Scroll View (331,318.6) 1588.7×761.4 | 未在前 160 行出现（后续行有列表，构建于场景坐标系）| 同坐标系错位问题 |
| 8 | 功能 | 熔炉等级奖励列表 ✓ 已有 | 已有 | 功能 OK，坐标系统待改 |

### 4.5 导航/入口

- nav_builder.gd L28：REWARDS 键 → rewards.tscn（会保持）。
- main_menu.gd L983 `_on_rewards` → rewards.tscn（保持）。
- main_menu.gd L142-160：登录弹窗 = daily_streak_popup.tscn（连胜弹窗，非每日奖励）。**每日 7 天奖励页（现 rewards.gd 内容）若保留，需找到新入口：原版是 Daily Reward Popup，从 Daily Login Container 卡点开。**

---

## 5. 重构实施建议（rewards.gd → 4-Tab 同屏任务中心）

### 5.1 架构（推荐）

```
rewards.tscn (RewardsRoot)                    ← rewards.gd = 壳
├─ 场景级固定层: NavBuilder.build(self,"REWARDS") + 场景背景(场景统一)
├─ Content Area (167.2,70.9) 1752.8×1009.1
│  ├─ Background(透明)
│  ├─ Tab Buttons (167.2,70.9) 165×1009.1
│  │  ├─ 底图 40k_main_tab_background + 阴影 40k_main_tab_shadow (右缘)
│  │  └─ 4 键 (165×180): y190.9/370.9/550.9/730.9
│  │     └─ 每键 = Icon(126²贴图) + Label(40k_main_bt_nametag 155×37.9 + TabButtonLabel 36/25.65px 白)
│  │             + Badge(40K_notification_number 35² + OneText) + Highlight(40k_main_bt_selected BW Tiled 纯红,仅选中)
│  ├─ Tabs (167.2,70.9) 1752.8×1009.1
│  │  ├─ MissionsTab (166.7,69.2) 1753.3×1010.8   ← quests 内容（见 5.2）
│  │  ├─ ForgeTab    (330.7,71.1) 1589.3×1008.7    ← forge 内容（坐标系改 330.7）
│  │  └─ CampaignTab (330.7,70.9) 1589.3×1009.1    ← campaign 内容（head 贴图换正版）
```

- Tab 切换 = 3 个 Toggle（ButtonGroup 互斥 / `button_group` + `toggle_mode`），`visible` 切换；Booster Packs = Button → `SceneTransition.change_scene("res://scenes/packs.tscn")`（项目有 packs 场景，已含卡包推荐内容）。
- 4 个现有场景保留为独立场景文件不删（nav_builder/其他入口引用），但 rewards 内**不再跳场景**。

### 5.2 内容并入方式（最小风险路径）

1. **quests.gd → Missions Tab 内容**：把 `_build_ui` 内容改成相对 Missions Tab 的内容面板函数（或新建 `quests_tab.gd extends Control` 复制 quests.gd 数据/逻辑，删 MenuBg/金币/NavBuilder/入口按钮）。
   - 布局改为原版：左区 Special Missions（496 宽）放 **Daily Login 卡**（可做成"每日签到"卡=现 rewards 7 天页入口）与 **Daily Skulls 卡 336×555**；右区 (x1271.3) Daily Missions 标题 'Daily Missions' 36px + Refill Counter '0 Disponible' + 3× 150 高行（沿用现有 3 任务数据，行结构=原版 Daily Mission Container horizontal）；底部 Weekly (372.4,759.8) 1519×227.5。
   - 里程碑奖励用 **40k_Crate_Tier1_Iron** 宝箱按钮（周常里程碑原版是宝箱！）；周常背景换 **40K_missions_display_Weekly**。
2. **campaign.gd → Campaign Tab**：内容类化；Header 底换 **WF_Campaign_Info_Background**（`res://assets/ui/mainmenu/` 下若未拷贝需从 `解包整理/03_界面UI/图集/0_mainmenu/Sprite/WF_Campaign_Info_Background.json`+Texture2D 拷贝入库）；阵营行 y=70.9；点数据已就绪。
3. **forge.gd → Forge Tab**：全部元素按 5.1 坐标表 +166.7 平移（Warp (741.8,88.5)、Column (330.7,71.1)/(1561.4,71.1)、Deco (444.7,185.1)、ArmySelector (588.2,71.6)、Selected info (619.4,195.8)、Scroll (331,318.6)）；注意 forge 现在的 scroll 栏在 x421 是相对 164 → 改 588.2。
4. **每日签到（现 rewards.gd 7 天页）**：独立保留为一个 **Daily Reward Popup 类场景/弹层**（原版 Daily Reward Popup：Rewards Scroll View (242,159) 1705×806 + NormalReward 295×381 + Premium 327×423）；从 Missions Tab 的 **Daily Login Container 卡**（inactive 卡，重构后做成 active 的"Daily Login Bonus"卡，"Collect"按钮→打开该弹层/跳转）。main_menu 登录时不弹它（有 daily_streak_popup 连胜弹窗）。
5. **验证**：重整后整屏截图 → 逐项对照本报告坐标（尤其 x372.4 内容起点、x330.7 Forge/Campaign 起点、Tab 键 190.9 起）；点击四键确认同屏切换；确认无元素越过 x332.2 进入 Tab 栏区域（当前 231 压栏问题应随内容区左缘 372.4 消失）。

### 5.3 已知待办/风险

- quests.gd 的 "Daily Login Container" 现 rewards.gd 的 `daily` profile 字段（day/claimedNormal/claimedPremium）继续用在同一 profile 数据，弹层与卡共用。
- forge.gd 右柱坐标 1588.4 是 2026-08-20 人工"核查"值，与原版 (1920-358.6=1561.4) 仍差 27 —— 一并修正。
- audit_D_rewards 命中表里 111 个 ⚠️ 未命中元素大多为：动态生成项（Reward Display Mission/抽屉/drawerHolder 等组件）、debug_buttons（开发）、Trash/Mission Debug（开发）、Handle Slide Area（Slider 内部）——重构时不必逐一对齐这些调试元素；要覆盖的是：Tab 图标/名牌/角标、Daily Missions 三行、Weekly 宝箱奖励、Forge 页面坐标、Campaign Header 正版贴图。

---

## 6. 跨验记录（chain_rect.py v2 输出摘录）

```
MissionsRewardsButton      x[167.2,167.2] y[990,1170]  w0 h180   （运行期 VerticalLayoutGroup 排布 → y190.9 起）
Menu Navigation Panel Button x[167.2,167.2] y[990,1170] w0 h180 （同上）
Forge Tab   (330.7,71.1) 1589.3×1008.7   Campaign Tab (330.7,70.9) 1589.3×1009.1
Tabs        (167.2,70.9) 1752.8×1009.1   Missions Tab (166.7,69.2) 1753.3×1010.8
Normal Missions (372.4,95.8) 1519×723.8  Daily Missions (1271.3,12.5) 620.1×639.3 (累计 scale=1.15)
Weekly Mission Holder 父链 Missions Tab(1179691781198557881 变体) → x205.2 相对 → 绝对 (372.4,759.8) 1519×227.5
```
与 `d:/2/audit_D_rewards.md` 规格表完全一致；与菜单全树 [x,y w,h] 数值一致（菜单全树 y 已是"屏幕 y 向下"显示值）。

**源 JSON 关键文件（PathID）**：
- 根：`菜单/GameObject/Rewards Base Submenu Variant_-8343312282719283457.json`；RT `RectTransform_507527829764970239.json`
- Tab 栏：`Tab Buttons_8069028602362337023.json` + VerticalLayoutGroup `MonoBehaviour_6895802506940585727.json` + TabGroup `MonoBehaviour_638825230631048959.json` + ToggleGroup `MonoBehaviour_-934655292178491649.json`
- 4 键：`MissionsRewardsButton_6509742238143682303` / `CampaignRewardsButton_-309639361232693505` / `Forge Button_-406639554272618753` / `Menu Navigation Panel Button_4168857396300748543`（Toggle `MonoBehaviour_-4134137194770196737` 等；TabButton id 脚本 `MonoBehaviour_-1040296725195778305`="RewardsMenu_MissionsButton"）
- 贴图：Tab 纹在 `03_界面UI/图集/0_mainmenu/Sprite/`（40k_main_tab_background/40k_main_bt_selected BW/40k_main_bt_nametag/40k_main_bt_campaign/WF_icon_clock/WF_Campaign_Info_Background）；rewards 专用图标在 `03_界面UI/菜单/Sprite/`（40K_rewards_bt_missions/40k_campaign_Premium-icon）；`03_界面UI/运营图标/Sprite/40K_shop_bt_boosters.json`；任务纹在 `03_界面UI/图集/Sprite/`（40K_missions_display_Daily vertical/horizontal/40K_missions_display_Weekly/40K_missions_icon_login bonus/40k_missions_milestone_off）；宝箱 `09_游戏数据/卡包/Sprite/40k_Crate_Tier1_Iron.json`。
