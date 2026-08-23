# Base Submenu / 弹窗外壳 复刻质量研究（2026-08-23）

> 研究任务（只读）：原版 Warpforge "Base Submenu" 弹窗框架 vs 项目 Godot 弹窗实现对比。
> 权威依据：`dump_go_tree.py` 输出的原始 Unity JSON（`D:/2/解包整理/03_界面UI/菜单/` 下 GameObject/RectTransform/MonoBehaviour/Sprite 原始文件），非整理文档二手数值。
> 项目侧：`D:/warpforge/scripts/` 9 个弹窗脚本 + `D:/warpforge/assets/` 资源。

---

## §0 关键澄清：Base Submenu ≠ 弹窗框架

**`Base Submenu`（菜单全树.md 行 9013-9029）不是模态弹窗**，它是原版**侧栏子菜单基类**（主菜单内 Contents 页的通用骨架：左侧 Tab 栏 + 右侧内容区），共 17 行，无遮罩/关闭钮/标题条。原版的**弹窗框架另有其物**，分三个外壳族（见 §2）。用户观感"弹窗简陋模仿"对应的是这三族的外壳复刻问题。

- Base Submenu 对应项目里各子菜单页（rewards/quests/campaign 等侧栏结构，要点文档标记"已实现"）——**它本身已经按 JSON 复刻**（Tab Buttons 40k_main_tab_background/40k_main_bt_selected BW/40K_shop_bt_boosters/40k_main_bt_nametag/40K_notification_number/40k_main_tab_shadow/40k_main_line 这些贴图项目 assets 全有），问题不在它。
- 真正的弹窗族：
  - **A 族 "40k_popup 九宫格窗"**：Give Feedback / Import Deck / ReRollPopup / Deck info(部分) / MessagePopupWindowDuel / Searching Oponent
  - **B 族 "红窗"（Generic Window Red Background Big = UI_Deck_Information_Back）**：Base Offer / Booster Info / Base Event / Draft Expiring / WhereToGetCards / Ranked Leaderboard
  - **C 族 "全屏奖励页"**：Daily Reward / Daily Streak（无中央窗，整屏条带 + 侧栏/顶栏）

---

## §1 原版 Base Submenu 权威元素表（原始 JSON）

| 元素 | 锚点/尺寸(屏幕) | 贴图 | 颜色/文字/字号 | 备注 |
|---|---|---|---|---|
| Base Submenu 根 | 全屏拉伸 (0,0,1,1) | — | — | Offset 全 0 |
| Content Area | (0,0,1,1) offsets(167.2,0,0,-70.9) → 屏幕 [167.2..1920]×[70.9..1080] | — | — | 1753×1009 |
| Background | 拉伸填满 Content Area | **Image->?（无贴图，运行时脚本铺图）** | color(1,1,1,1) | 内容页底纹运行时给 |
| Tab Buttons | anchor(0,0,0,1) 左缘宽 165 | **40k_main_tab_background** | white | 左侧竖 Tab 底 |
| ├ Menu Navigation Panel Button | 高 180（Button） | — | — | Tab 按钮（预制体） |
| │ ├ Highlight | 拉伸 | **40k_main_bt_selected BW** | **color(1,0,0,1) 红 tint** | 选中态 |
| │ ├ Icon | 拉伸 pivot(0.5,0.7) | **40K_shop_bt_boosters** | white | 图标 |
| │ ├ Label | 155×37.9 | **40k_main_bt_nametag** | white | 名牌底 |
| │ │ └ TabButtonLabel | 155×填充 | — | text 'Booster Packs' **25.65pt** 白 | 文字 |
| │ └ Badge Highlight | 35×35 | **40K_notification_number** | color(0.74,0.74,0.74,1) | 角标(OneText '' 34pt 白) |
| └ Shadow | 拉伸，左缘 -117.4 宽 | **40k_main_tab_shadow** | color(0,0,0,0.47) | Tab 栏右侧阴影 |
| Tabs | 拉伸 | — | — | 内容 Tab 容器 |
| └ Sample Tab | 拉伸 | — | — | 模板页 |
| │ └ Header | (0,1,1,1) 高 85 | — | — | 顶栏 |
| │ │ └ Separator Line | 距左 163.5 高 10 | **40k_main_line** | white | 分隔线 |
| └ Shadow (1) | active，offsets(163.2,-1540.2) | 40k_main_tab_shadow | (0,0,0,0.47) | 内容右侧阴影 |

坐标结论：与项目 NavBuilder 侧栏结构一致；本项目各子菜单页也用了同批贴图（40k_main_tab_background.png 等已在 `assets/ui/mainmenu/`），**Base Submenu 本体无"简陋"问题**。

---

## §2 原版弹窗外壳权威元素表（三族）

### A 族：40k_popup 九宫格窗（Give Feedback / Import Deck / ReRoll 等）

| 层 | 元素（原版层级） | 尺寸/锚 | 贴图 | 颜色 | 说明 |
|---|---|---|---|---|---|
| 1 | **Menu Dark Background** | 4574.6×2572.4 中心锚 | Image->**?（无贴图，纯色 Image）** | **color(0,0,0,0.77)** | 全屏变暗层（比屏幕大 2 倍防边缘漏光） |
| 2 | Window（内容定位用） | 如 Give Feedback 2231×937 @中心(0,+0.5) | — | — | Import Deck: 800×451.9 @中心(0,80)；ReRoll: 850×430 @中心(0,80) |
| 3 | **Generic Popup Background** | 拉伸填 Window | **`40k_popup`（359×336，m_Border=(169,160,169,160)）** | color(1,1,1,1) | 九宫格边框层（Unity Image Type=Sliced，圆角+边框保持） |
| 4 | Mask（同贴图再垫一层） | 内缩 ~10px（offsets 10.4,-9.9,9.8,-9.4） | 40k_popup | white | 二次嵌套形成内框 |
| 5 | **Background fill** | 拉伸填 Mask | **`40k_popup_texture`（128×128，border 0）** | white | 中心平铺底纹（细密纹理） |
| 6 | 标题 | 如 'Give us your feedback!' | — | **50pt 白** | Import Deck 'Paste your deck' 50pt 白 |
| 7 | 主按钮 | 478.3×75 | **40K_button tint (0.37,0.89,0.59,1.0) 绿** | 文字 45pt 白 | Confirm/Submit |
| 8 | 输入框 | 700×141.1 | **40K_dropdown_bg tint (0.29,0.95,0.68,1.0)** | placeholder 32pt | Import Deck |
| 9 | 关闭钮（绿/白灰族） | 75×75 | **UI_Button_Round_background**（237×237 圆盘）+ **Icon 40k_bt_close**（175×174 X，锚 0.127~0.873 内缩 10%） | white | 两层；位置=窗右上角 |
| 10 | 关闭钮（橙族，B/C 族大窗用） | 74.4×75.6 | **UI_Button_Round_background + 40k_general_bt_yellow + 40k_general_bt_yellow_close** 三层 | white | 黄盘+黄 X |

### B 族：红窗（Base Offer / Booster Info / Base Event / Draft Expiring / WhereToGetCards / Ranked）

| 层 | 元素 | 尺寸/位置 | 贴图 | 说明 |
|---|---|---|---|---|
| 1 | Menu Dark Background | 4574.6×2572.4 | 无贴图 | **(0,0,0,0.77)** |
| 2 | window | 1128.6×663.3 @中心(0,+20)（Offer/BoosterInfo） | — | Base Event: 1052.7×733.3 @中心(+9,+27) |
| 3 | **Generic Window Red Background Big** | 1151.6×717.4（比窗大一圈，中心低 17.1 → 上下突出） | **UI_Deck_Information_Back** | 大窗底带描边/浮雕 |
| 4 | Generic Close Button Orange | 74.4×75.6 锚(1,1) 右上 | 三层（见 A 族 10） | Offer/BoosterInfo/WhereToGetCards；Base Event/Draft 无关闭钮（全屏点击） |
| 5 | 文本族 | Title 40 / Category 39 / Desc 35（Offer）；Title 34 / Desc **28** / Tap 30（Event）；Title 41（Draft）；Title **72**（Where） | — | **全部 m_text 白色** |
| 6 | 按钮族 | 40K_button tint（金 0.9,0.64,0.18,1 / 绿 0.33,0.88,0.34,1 / 绿 0.37,0.89,0.59,1）；UI_Button_Mulligan（Leaderboard 白） | — | 按钮文字 34-45pt 白 |
| 7 | Offer Badge | Image->?（**color(0.65,0,0,1) 红底**） | 文字 '+60% value' 38pt 白 | 非金色底 |
| 8 | Event image（Base Event） | 858.8×858.8 @(-249,+76.5) | **Image->? 运行时图** color(0.8,0.8,0.8,1) | 动态事件图（无法静态复刻，需替代） |

### C 族：全屏奖励页（Daily Reward / Daily Streak）

| 元素 | 尺寸 | 贴图/文字 | 说明 |
|---|---|---|---|
| Menu Dark Background | 4574.6×2572.4 | **(0,0,0,0.77)** | Daily Reward 内还有子 Image 1920×1080 white 0.65 |
| bg 条带 | 全宽 812.1 高 @中心 | Image->?（无贴图白 1,1,1,1，运行时） | 上下 40k_main_line 分隔线 14.9 高 |
| Daily Reward 关闭 | **Generic Round Button Variant 124×124** | **40k_UI_bt_back** + Text 'X' 30pt + **40k_general_bt_yellow_delete** | 在 Tracks Side Bar 内 anchor(0.5,0) |
| Tracks Side Bar | 290.7×824.7 | **UI_Login_Tracker** | Free/Premium 双轨 |
| Daily Streak 顶栏 | 550×109.5 | **Header With Back Button：WF_Campaign_Info_Background** + Window Title 'Daily Streak' **67.55pt 白** + Header Back Button **UI_Button_Menu_Back** 167.9×111.3 | — |
| Streak 文案 | 'STREAK BROKEN' **128.1pt** / 'Current streak:' 70pt / 数值 80pt | 全白 | Reset Streak 钮 UI_Button_Mulligan 464.6×103 55pt |

---

## §3 项目各弹窗外壳实现对照表

> 状态：✓=精确复刻  ≈=近似（有可接受小差） ✗=偏差（可见差异大） ✖=缺失/贴图用错/结构错

| 项目脚本 | 遮罩 | 窗底 | 关闭钮 | 标题/文字 | 主按钮 | 与 §2 差异评定 |
|---|---|---|---|---|---|---|
| **offer_popup.gd**（B族·Offer） | ✗ ColorRect 暗红 (0.11,0.045,0.055,0.82)（原版**纯黑 0.77**） | ≈ UI_Deck_Information_Back ✓；但窗 1129×663 **背景 717.4 高被 STRETCH_SCALE 压扁 7.6%**（原版背景独立层、比窗大一圈） | ✓ 三层橙族（Round+yellow+yellow_close）结构/贴图全对；坐标 ≈（项目 1487.1,159.8 vs 原版 1487.1,181.3，差 21px） | ≈ 40/39/35 字号对 ✓；✗ 颜色金/灰（原版**全白**） | ✗ 40K_button **缺金 tint** (0.9,0.64,0.18,1)；✗ Offer Badge 用 40k_bt_underbutton 金底+32pt（原版**红底 0.65,0,0,1**+38pt 白）；✗ Save More 用 UI_Button_Mulligan 0.5 透明+黄 Octagon 0.55（原版 **40K_button 绿 0.33,0.88,0.34,1**+白 Octagon 0.8）；✗ **Artwork 底用 UI_Deck_Information_submenu_Back_opaque（原版 40k_shop_popup_info_bg）**；✗ Available Counter 24pt（原版 30pt） | **7 处偏差——但骨架/坐标是大体按说明书的** |
| **base_event_popup.gd**（B族·Event） | ✗ 暗红 0.78 **合并进 Collider StyleBoxFlat**（原版独立 Menu Dark Background 黑 0.77 + 透明 Collider 两层） | ✓ UI_Deck_Information_Back 1052.7×733.3 ✓ 坐标(443,146) 对 | ➖ 原版无关闭钮（全屏点击）✓ | ✗ Title 34 ✓ 但金色（原版白）；✗ Desc **20pt（原版 28pt）**；✓ Tap 30pt；文字 'Click to continue'（原版 m_text 西语，英文为文档化替身可） | — | 窗底/坐标好，**遮罩色+字号差** |
| **give_feedback_popup.gd**（A族） | ✗ 暗红 (0.11,0.045,0.055,0.78) | ✖ **只用 40k_popup_texture(128×128 平铺纹) 单层 STRETCH_SCALE 当整窗底**——**缺 40k_popup 九宫格边框层 + Mask 层**，纹理被拉成糊面（40k_popup.png 资产已在项目中却未用） | ✖ **缺 UI_Button_Round_background 圆底，只有 40k_bt_close X** | ✗ Title **36pt 金（原版 50pt 白）**；✗ Subtitle **20pt 灰（原版 42.45pt 白）** | ✗ 40K_button **无绿 tint**，文字 **30pt 金（原版 45pt 白）** | **7 处——本次"简陋"观感的主要来源**（坐标 105,75/70.9,211.6/720.6,909.2/1816.5,10.7 按说明书 ✓） |
| **import_deck_popup.gd**（A族） | ✗ 暗红 0.65（原版 Import Deck Background **黑 0.4**） | ≈ 40k_popup_texture + 40k_popup 两层都有 ✓（**顺序对**）；✗ 但用 **TextureRect.STRETCH_SCALE 而非 NinePatchRect**（40k_popup border 169/160/169/160，800/359=2.23x 与 452/336=1.35x 不同轴 → **九宫格圆角被拉伸变形**） | ✓ **两层齐全**（Round+X）位置 [1317,202.1]（chain_rect 修正过 ✓） | ✗ Title 50pt ✓ 但金色（原版白） | ✓ 40K_button 绿 tint ✓ 45pt ✓（margins 12/6 需复核原版） | **9 个弹窗中复刻度最高的**；差距在遮罩色/九宫格方式/文字色 |
| **booster_info_popup.gd**（B族·Booster） | ✗ 暗红 0.78 | ✓ UI_Deck_Information_Back **全尺寸 1151.6×717.4 @(395.7,178.4)** ✓（无压缩问题） | ≈ 需看文件 120 行后（未逐项核对，疑似同 offer 橙族） | ≈ 40/39/35 字号对（2026-08-23 修过）✓ 颜色金/灰（原版白） | 原版购包区 = 金 tint 40K_button + WebShop 绿 + 保底条 40k_campaign_bar_bg/outline（项目有 40k_campaign_bar_bg ✓） | 外壳是 B 族较好者 |
| **daily_reward_popup.gd**（C族） | ✓ **黑 (0,0,0,0.77)**（唯一遮罩颜色正确的弹窗） | ≈ 无中央窗（全屏族人） | ✗ **74×76 仅 40k_bt_close X @(1786,33)**；原版 = **124×124 40k_UI_bt_back 大圆钮 + 'X' 30pt + 40k_general_bt_yellow_delete，位于 Tracks Side Bar 内** | — | — | 遮罩对，**关闭钮样式/贴图/位置全错位** |
| **daily_streak_popup.gd**（C族） | ✗ 暗红 0.78 | ✗ bg 用 **ColorRect 暗红纯色 0.92**（原版 bg 为运行时 Image 白框 + 上下 40k_main_line ✓ 项目也有分隔线 ✓） | ✗ Back 按钮 flat 无贴图（原版 **UI_Button_Menu_Back** 167.9×111.3） | ✗ Window Title **36pt 金（原版 67.55pt 白）**；STREAK BROKEN 需核（原版 128.1pt） | ✗ 'Tap to continue' 18pt（draft）；Streak 行 'More Rewards In' 50pt→? | 顶栏贴图 WF_Campaign_Info_Background ✓ 用了；字号/遮罩/Back 贴图差 |
| **draft_expiring_popup.gd**（B族·Draft） | ✗ 暗红 0.8 合并进 Collider | ✓ UI_Deck_Information_Back (328.8,199.5,1262.4,723.9) ✓ | ➖ 原版也无关闭钮（Tap To Continue 全屏）✓ | ✗ Title **40pt（原版 41）**金/白；✗ Leaderboard 文字 22pt（原版 36pt）；✗ 'Tap to continue' **18pt（原版 50pt）**；✗ x10 40pt 金（原版 34.05pt 白） | ✓ UI_Button_Mulligan ✓（原版同款） | 外壳本体对，**文字字号普遍缩水 + 遮罩色错** |
| **where_cards_popup.gd**（B族·Where） | ✗ 暗红 0.78 | ✓ UI_Deck_Information_Back (204.7,16.3,1510.6,990.6) ✓ | ✖ **仅 40k_bt_close X**（原版**橙族 3 层** 74.4×75.6 @(1656.8,9.2)——坐标对但缺圆底/黄盘） | ✓ Title **72pt ✓ 尺寸坐标全对**；✗ 金色（原版白） | — | 坐标忠实，关闭钮缺层 |

---

## §4 结论：是"简陋模仿"吗？

**部分成立。** 坐标层面普遍按说明书（多数弹窗坐标/字号经 2026-08-20~23 多轮审查修正，无乱排）；**但"外壳质感三件套"（窗底贴图层级 / 关闭钮样式 / 遮罩颜色）系统性不统一，加上文字色金化、字号缩水、按钮 tint 缺失**，造成"界面不好看/图标混乱"的观感。具体 Top 差距（按观感权重）：

1. **give_feedback 窗底用错贴图（最扎眼）**：原版 40k_popup 九宫格边框（359×336，border 169/160）+ Mask + 40k_popup_texture 三层；项目把 128×128 平铺填充纹**单层拉伸**当窗底 → 无圆角/茶色浮雕边框，纹理糊化。**40k_popup.png 资产在 `assets/ui/battle/` 与 `scenes_sprites/` 都有，纯粹没用**。A 族其他窗（import_deck 用了两层 ✓）对比更显其简陋。
2. **九宫格全部用 TextureRect.STRETCH_SCALE 而非 NinePatchRect**：40k_popup border=169/160/169/160（原版 Image.Type.Sliced），拉伸后圆角/描边变形（import_deck 800×452、give_feedback 1825×997 变形程度不同）。
3. **关闭钮三套样式不统一且多处缺层**：橙族 3 层仅 offer_popup 有；give_feedback/where_cards/daily_reward 只有 X 图标（缺 UI_Button_Round_background 圆底）；daily_reward 的关闭钮与原版 124×124 大圆钮（40k_UI_bt_back）完全不同。
4. **遮罩色系统性错误**：全部弹窗用暗红 `Color(0.11,0.045,0.055,0.78~0.82)`，原版权威为**纯黑 `(0,0,0,0.77)`**（Menu Dark Background；仅 daily_reward_popup.gd 恰好用对）。暗红遮罩改变整体氛围/色调 → "界面不好看"的第一印象来源。
5. **文字全用金色/灰色**（`0.969,0.914,0.714`/`f7e9b6`/`b0b5bd`），**原版弹窗文字一律白色**（m_fontColor 1,1,1,1）；Gold 是主菜单导航字色，非弹窗字色——全局给弹窗文字套金色是最大的"非原版"感觉来源。
6. **标题/正文字号系统性缩水**：Give Feedback Title 50→36、Subtitle 42.45→20、Submit 45→30；Streak 标题 67.55→36、Streak Broken 128→(需核)；Where Section 42 vs 原版 42 ✓（部分过关）。
7. **按钮 tint 缺失/错误**: Offer 购买钮缺金 tint、Save More 用错材质组合（原版绿钮+白 Octagon）、Import/Feedback Submit 有绿 tint ✓。
8. **Offer 弹窗细节错位**：Artwork 底用错贴图（应 40k_shop_popup_info_bg）、Offer Badge 应红底（0.65,0,0,1）非金底。
9. **红窗背景被压缩**：offer_popup 窗 1129×663 内直接铺 717.4 高的 UI_Deck_Information_Back（STRETCH_SCALE 压 7.6%）→ 边框浮雕变形（booster_info 用全尺寸 1151.6×717.4 是正确的做法）。
10. **遮蔽方式**：base_event/draft 把暗色合并进全屏 Button（StyleBoxFlat），原版是 独立 Menu Dark Background 层 + 透明 Collider 层——功能等价，但 0.8 暗红 vs 0.77 纯黑的色差仍在。

**非问题项（澄清）**：import_deck 坐标/关闭钮/绿钮/字号全部正确（2026-08-23 已修到位）；booster_info/draft_expiring/where_cards 的窗底尺寸坐标正确；Base Submenu 侧栏本身无问题。

---

## §5 复刻方案建议（统一原版外壳）

### 5.1 新建共享外壳模板（加到 ui 工具库，如 `ui_kit.gd` 静态函数）

1. **`make_dark_bg(alpha=0.77)`** — ColorRect 纯黑 0.77 全屏（替代散落各处的暗红 0.78/0.8/0.82/0.65）。一键替换 9 个弹窗。
2. **`make_popup_window_a(parent, rect, use_mask=true)`** — A 族 40k_popup 窗：
   - 40k_popup → **`NinePatchRect`**（texture_margin l=169 t=160 r=169 b=160，对应 m_Border）
   - 40k_popup_texture → 内缩 10px 的填充层（NinePatchRect patch_margin 0 或 shader 平铺；拉伸可接受且与原版视觉接近）
   - 可选第三层 Mask 边框再垫（原版两层 40k_popup；视觉增益小，先一层+fill 也可）
3. **`make_popup_window_b(parent, rect)`** — B 族红窗：**背景与窗口分离**——背景 NinePatchRect（UI_Deck_Information_Back，margin 按 x 差值≈11.5/17.1）尺寸 1151.6×717.4 中心差 (11.5,-17.1)，窗口容器 1128.6×663.3 只做定位→ 消除压缩变形。
4. **`make_close_button(parent, pos, style)`** — 三种关闭钮：
   - `"green"`：75×75 UI_Button_Round_background + 40k_bt_close（锚 0.127-0.873 内缩 10%）
   - `"orange"`：74.4×75.6 UI_Button_Round_background + 40k_general_bt_yellow + 40k_general_bt_yellow_close
   - `"round124"`：124×124 40k_UI_bt_back + 'X' 30pt + 40k_general_bt_yellow_delete（Daily Reward）
5. **`make_primary_button(parent, rect, tint, label, size=45)`** — 40K_button StyleBoxTexture + modulate tint（绿 0.37,0.89,0.59,1 / 金 0.9,0.64,0.18,1 / 绿 0.33,0.88,0.34,1），白字。
6. **统一弹窗文字规范**：弹窗内文字一律白（外层标题可留金色？不——原版弹窗（含 Where 72pt、Streak 67.55pt、STREAK BROKEN 128pt）全部 m_text 白色；主菜单页级标题金色是另一套。逐弹窗按 §2 表核对字号。

### 5.2 各弹窗接入拆解（工作量，按优先级）

| 优先级 | 弹窗 | 改动 |
|---|---|---|
| P0 | give_feedback_popup.gd | 窗底换 40k_popup NinePatchRect+fill；Title 50pt 白、Subtitle 42.45pt 白；Submit 绿 tint+45pt 白；关闭钮加圆底；遮罩黑 0.77 |
| P0 | offer_popup.gd | 背景独立全尺寸层；Artwork 底→40k_shop_popup_info_bg；购买钮金 tint；Offer Badge 红底+38pt；Save More 绿钮+白 Octagon；Available Counter 30pt 白；遮罩黑 |
| P0 | 遮罩统一 | 9 个弹窗暗红→黑 0.77（daily_reward 已是） |
| P1 | import_deck_popup.gd | 40k_popup 两层改 NinePatchRect；遮罩 0.4 黑（原版）或与全局统一 0.77（推荐统一 0.77 并记载差异）；Title 白 |
| P1 | daily_reward_popup.gd | 关闭钮→124×124 round124 族（40k_UI_bt_back+X+delete，位置=窗口右上/ Tracks 侧栏内 按原版） |
| P1 | where_cards_popup.gd | 关闭钮→橙族 3 层；Section/文字色白 |
| P1 | base_event_popup.gd | 遮罩独立黑层+透明 Collider；Desc 28pt；文字白 |
| P1 | daily_streak_popup.gd | Title 67.55pt 白；Back→UI_Button_Menu_Back；STREAK BROKEN 128.1pt；'Streak lost' 66.9pt 等按 §2 表 |
| P2 | draft_expiring_popup.gd | 'Tap to continue' 50pt、Leaderboard 36pt、x10 34.05pt 白、Game Mode Title 41pt 白；遮罩黑 |
| P2 | booster_info_popup.gd | 遮罩黑、文字白、购包区（金 tint+WebShop 绿+保底条 outline 40k_campaign_bar_outline tint 1,0.63,0,1）核对 |

### 5.3 资源可用性（全部已确认在解包 + 项目 assets 中，复刻无资源障碍）

| 贴图 | 原版 Sprite 数据 | 解包路径 | 项目 assets 路径 |
|---|---|---|---|
| 40k_popup | 359×336 **border (169,160,169,160)** 9-slice，Atlas "0_GeneralUI Atlas" | `解包整理/12_主程序资源/Texture2D/sactx-0-4096x2048-BC7-0_GeneralUI Atlas-7a9721b1.png`（atlas 源）+ `解包整理/03_界面UI/去重资源/Sprite/40k_popup_-7511397500040153103.json` | `assets/ui/battle/40k_popup.png`、`assets/ui/mainmenu/scenes_sprites/40k_popup.png` ✓ |
| 40k_popup_texture | 128×128 border 0（tile fill） | `解包整理/12_主程序资源/Texture2D/40k_popup_texture.png`（多处） | `assets/ui/mainmenu/scenes_sprites/40k_popup_texture.png` 等 ✓ |
| UI_Button_Round_background | 237×237 圆盘（physics shape 圆形） | atlas + `去重资源/Sprite/UI_Button_Round_background_2381704724431365035.json` | `scenes_sprites/UI_Button_Round_background.png` ✓ |
| 40k_bt_close / _hover / _pressed | 175×174 X | atlas + `去重资源/Sprite/40k_bt_close_6553861554683527146.json` | `scenes_sprites/40k_bt_close.png`（三态均齐）✓ |
| UI_Deck_Information_Back | B 族红窗底 | `解包整理/12_主程序资源/`（atlas 提取） | `scenes_sprites/UI_Deck_Information_Back.png` ✓ |
| 40K_button | 通用按钮底（tint 驱动颜色） | atlas | `scenes_sprites/40K_button.png` ✓ |
| 40k_shop_popup_info_bg | Offer Artwork 底 | `解包整理/09_游戏数据/卡包/`（+运营菜单图/） | `scenes_sprites/40k_shop_popup_info_bg.png` ✓ |
| 40k_general_bt_yellow(_close) | 橙族关闭钮 2/3 层 | atlas | `scenes_sprites/` + `assets/ui/battle/` ✓ |
| 40k_UI_bt_back | Daily Reward 关闭（124×124） | atlas | `assets/ui/mainmenu/40k_UI_bt_back.png`（含三态）✓ |
| UI_Button_Menu_Back | Daily Streak 返回钮 | atlas | `assets/ui/mainmenu/atlasindividual_assets_0_mainmenu/UI_Button_Menu_Back.png` ✓ |
| UI_Login_Tracker | Daily Reward 侧栏底 | — | `scenes_sprites/UI_Login_Tracker.png` ✓ |
| WF_Campaign_Info_Background | Streak Header 底 | — | `scenes_sprites/WF_Campaign_Info_Background.png` ✓ |
| 40k_main_line / 40k_main_tab_background / 40k_main_bt_selected BW / 40K_shop_bt_boosters / 40k_main_bt_nametag / 40K_notification_number / 40k_main_tab_shadow | Base Submenu Tab 栏全套 | atlas | `assets/ui/mainmenu/` 全套 ✓ |

**无缺失资源**（唯一"替代品"：Base Event 的 Event image 原版为运行时事件图 Image->?，项目以 40k_shop_popup_info_bg 替代属合理降级，需标注；Daily Reward/Streak 的 bg 原版亦为运行时图，项目用 ColorRect 纯色——建议换用原版同族贴图如 40k_general_popup_simple 系列（`解包整理/03_界面UI/图集/0_mainmenu/Sprite/40k_general_popup_simple red/greyscale.json`，项目已有 `40k_general_popup_simple greyscale.png/red.png`）改善质感）。

---

*调研工具：dump_go_tree.py（原始 JSON 子树）；坐标=原始 RectTransform 链值；菜单树坐标 y 自顶与 Godot 同向（已用 Base Submenu Content Area offsets(167.2,0,0,-70.9)→[167,71 1753x1009] 验证）。弹窗文字/颜色全部引自对应 MonoBehaviour Text/Image m_text/m_fontColor/m_Color。*
