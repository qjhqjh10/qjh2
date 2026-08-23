# 子代理报告：Settings 设置界面 完整说明书读取 + 权威规格表（2026-08-23）

> 本报告为批次 4 第 0 项（settings 0.9 scale 容器）实施的唯一依据。
> 数据来源：原始 Unity JSON（`解包整理/03_界面UI/菜单/`，dump_go_tree.py 全树 324 行）+ chain_rect.py v2 权威换算 + 布局组 MonoBehaviour 参数 + Warpforge_code 反编译。
> 所有"视觉坐标"= Godot 绝对屏幕坐标 1920×1080（y 翻转、pivot 修正、锚点中心、父链累加、**含全树唯一 0.9 缩放**），与 `d:/2/audit_A_settings.md` 中 chain_rect 权威值逐一一致。
> 权威判定规则：**布局组（VGroup/HGroup）子元素以布局组公式为准**（prefab 快照坐标是未布局状态）；无布局组元素以 chain_rect 快照链为准。

---

## 0. 核心结论（任务验证）

**任务文件要点全部证实：**

| 项 | 任务文件 | 本报告证实 |
|---|---|---|
| settings 根 RT 真实 m_LocalScale=0.9 | ✓ | `RectTransform_-7066813013973172314.json` 的 `m_LocalScale = {x:0.9, y:0.9, z:0.9}`（bundle 序列化字段直接可见）；rt_scale_map.json 亦记 0.9 |
| Menu Area 视觉 (391.3,164.8) 1146.9×758.8 | ✓ | chain_rect GO 6980647852167364518 | 累计 scale=0.90 |
| 项目现 1274×843 大 11% 且左偏 63/上偏 42 | ✓ | 328 vs 391.3 → 偏 63.3；123 vs 164.8 → 偏 41.8；1274/1146.9 = 1.111 → 大 11.1% |
| Tab 列 160.6 宽 | ✓ | chain_rect GO -301262919896891482：x[391.3,164.8] 宽 160.6 高 758.8 |
| 键 148.5×151.76 | ◑ | 键 148.5×**141.9**（=165×0.9 / 157.7×0.9）；151.76=列高 758.8/5（均分 slot，含间距的近似）—— 精确布局=键 141.93 高 + 间距 8.03（见 §2.3） |
| 图标 127.2×96.1 | ✓ | 141.4×106.8 未缩放 ×0.9 = 127.26×96.12 |
| PAGE_POS (551.9,164.8) 929×758.8 | ✓ | chain_rect Tab Content GO -1958548370395332698 |
| Close 按钮 (1499.1,136.4) 67.5² | ✓ | chain_rect GO -5975704140969246810 |

**缩放机制（铁证）**：缩放发生在 **Main Menu Settings Window 根 RectTransform**（anchor 全屏 0,0,1,1 + pivot 0.5,0.5 + offsets 0）。全树 157 个 RectTransform 中**仅此一个非 1 缩放**。以屏幕中心 (960,540) 为轴：视觉覆盖 = 1920×1080×0.9 = **1728×972，位于 [96,54]..[1824,1026]**（audit 表根行 godot(x96.0 y54.0 w1728.0 h972.0) ✓）。
验证等式（GENERAL 键示例）：prefab 键局部 165×157.7 → 链 ×0.9 = 148.5×141.93；Menu Area prefab (328,123,1274×843) → ×0.9 以 (960,540) 为轴 = (960-568.8, 540-375.3)=(391.2,164.7)≈(391.3,164.8) ✓。

---

## 1. 缩放容器结构（原版）

```
Main Menu Settings Window  ★缩放节点: RT m_LocalScale=0.9, anchor(0,0,1,1) pivot(0.5,0.5) offsets=0
│        → 视觉覆盖 [96,54] 1728×972；子元素以屏幕中心 (960,540) 缩放 0.9
├─ Menu Dark Background   (0,0) 4574.6×2572.4 → 视觉 [-1098.6,-617.6] 4117.2×2315.2；Image->? color(0,0,0,0.77)
├─ Debug Buttons           [402.0,65.7] 1116.0×99.1（未缩放 [340,13] 1240×110）调试按钮组（开发用，17 键+border+标题）
├─ old menu        (inactive) [96,54] 1728×972（旧版 Steam 按钮残留）
└─ Menu Area               [391.3,164.8] 1146.9×758.8（未缩放 [328,123] 1274.4×843.1, anchor 0.5,0.5 pivot 0.5,0.5）
   ├─ Generic Popup Background  [391.3,164.8] 1146.9×758.8  Image->40k_popup（主底）
   │  └─ Mask                  [400.6,173.3] 1128.8×741.4  Image->40k_popup（次级底）
   │     └─ Background fill    [555.6,173.3] 973.8×741.4   Image->40k_popup_texture rect(0,0,128,128)（中央内衬 9-slice）
   ├─ Popup BG          (inactive) [391.3,164.8] 1146.9×758.8  Image->40k_popup
   ├─ Generic Close Button    [1499.1,136.4] 67.5×67.5（未缩放 [1559,92] 75×75 = Menu Area 右上角外侧 -6,-6）
   │  └─ Icon                [1507.5,145.7] 50.7×49.0  Image->40k_bt_close
   ├─ Mask Tabs buttons       [400.4,173.3] 1129.0×741.4  Image->40k_popup
   │  └─ Tab Buttons          [391.3,164.8] 160.6×758.8（anchor(0,0,0.14,1)）★含 VerticalLayoutGroup
   │     ├─ Separators        [550.6,146.8] 2.6×794.8  Image->40k_Separator Fade Sides Vertical color(0.02,0.32,0.21,1)
   │     └─ [General/Media/Account/Graphics/Support] 5 键（★键=Toggle 组件, 布局组排位, 见 §2.3）
   └─ Tab Content             [551.9,164.8] 929.0×758.8（anchor(0.14,0,0.95,1)）
      ├─ General Tab  (active)   ★页（无布局组, 快照=视觉）
      ├─ Media Tab    (active)
      ├─ Account Tab  (inactive) ← 默认快照隐藏, 运行时脚本切换
      ├─ Support Tab  (inactive)
      └─ Graphics Tab (inactive)
```

→ **Godot 实现即：全树包进一个 scale=(0.9,0.9)、pivot_offset=(960,540) 的根容器，内部坐标直接用菜单全树/dump_go_tree 的未缩放 prefab 坐标**（现有 settings.gd 数值体系 328,123/1274×843/1559,92/75×75/507,123/1032×843 全部保留即得精确复刻——渲染后 = 权威值，误差 <0.2px）。见 §5。

---

## 2. 原版元素全表（权威视觉坐标）

> 每行：GO名 | 类型 | 视觉 (x,y,w,h) | 锚点/pivot | 贴图(PathID→Sprite名) | 文字/字号/颜色 | m_IsActive | 原始 JSON
> 未缩放 prefab 值可直接从 dump_go_tree 输出（本报告 §2 表内用"视觉"值；括号内"未缩放"供参考）。

### 2.1 框架层（含调试区/背景）

| 元素 | 视觉 (x,y,w,h) | 锚点 | 贴图/颜色 | 文字 | active | 原始 JSON（菜单目录） |
|---|---|---|---|---|---|---|
| Main Menu Settings Window | 根 | anchor(0,0,1,1) pivot(0.5,0.5) **scale 0.9** | — | — | 1 | GameObject\Main Menu Settings Window_-9019961019057471578.json / RectTransform\RectTransform_-7066813013973172314.json |
| Menu Dark Background | (-1098.6,-617.6) 4117.2×2315.2 | (0.5,0.5) | Image->? 黑 (0,0,0,0.77) | | 1 | GameObject\Menu Dark Background_3213153224911519654.json |
| Debug Buttons | (402.0,65.7) 1116.0×99.1 | (0.5,0.5) | 组容器 | | 1 | GameObject\Debug Buttons_7652293982013390758.json |
| Debug button text | (870.0,74.8) 180×21.6 | (0.5,0) | | 'Debug Buttons' 36px 白 | 1 | GameObject\Debug button text_-4356163549120725082.json |
| Border ×3 | (402.0,100.9) 1116×2.7 等 | Stretch | White Square (0.7,0.7,0.7,0.7) | | | GameObject\Border_-980899085839990874.json 等 |
| old menu | (96,54) 1728×972 | full | — | | **0** | GameObject\old menu_4609093541619924902.json |
| Steam Button | (483.0,672.7) 972×86.7 | anchor(0,0.5,1,0.5) | 40K_button (0.37,0.89,0.59,**α=0**) | 'Добавить в Список Желаемого' 42px | 1 | GameObject\Steam Button_-2524240625835999322.json |
| steamImage | (506.8,671.0) 69.9×88.4 | (0,0.5) | Steam_icon_logo.svg | | | GameObject\steamImage_-7124133411501080666.json |

调试 17 键（Console/Unlink/ResetTutorial/AddCoins(inactive)/Season Check(inactive)/Reset GameModes/Reset Feedback/Reset Events/AddWildcards(inactive)/RateButton/ResetDLC/Enviromental Debug/GetRewards/Score On Leaderboard/Time Offset/Clean Cache/Toggle  Debug）：全部 Image->**40K_button (0.94,0.16,0.82,1.0)** 紫粉 Debug 色，文字 12~24px 白；可活跃键视觉位置 ≈ (402..1518, 115.2) 三个：(594,68,72×43)→视觉≈(630.8,115.2,65×38.6) AddCoins / (759,68,93×43)→(778.8,115.2,83.5×38.6) SeasonCheck / (964,68,113×43)→(963.8,115.2,102×38.6) AddWildcards（未缩放取 dump 树行 11-22：AddCoins pos(282.8,-21.4) 72.2×42.8 等）。项目当前**完全没有**该调试区 —— 开发调试功能，建议跳过（用户可见性：无）。

### 2.2 Menu Area 主窗口层

| 元素 | 视觉 (x,y,w,h) | 锚点/pivot | 贴图 | 文字 | active | 原始 JSON |
|---|---|---|---|---|---|---|
| Menu Area | (391.3,164.8) 1146.9×758.8 | (0.5,0.5) | — | | 1 | GameObject\Menu Area_6980647852167364518.json |
| Generic Popup Background | (391.3,164.8) 1146.9×758.8 | full | 40k_popup（Sprite rect 359×336） | | 1 | GameObject\Generic Popup Background_2152500398337654694.json |
| Mask | (400.6,173.3) 1128.8×741.4 | full offset(10.4,-9.9,9.8,-9.4) | 40k_popup | | 1 | GameObject\Mask_-7710459438390476890.json |
| Background fill | (555.6,173.3) 973.8×741.4 | full | **40k_popup_texture** rect(0,0,128,128) 中央内衬 | | 1 | GameObject\Background fill_-1691446943306711130.json |
| Popup BG | (391.3,164.8) 1146.9×758.8 | full | 40k_popup | | **0** | GameObject\Popup BG_5613162753722515366.json |
| Generic Close Button | (1499.1,136.4) 67.5×67.5 | (1,1) pos(-6,-6) pivot(0.5) | **UI_Button_Round_background**（237×237 圆底）Button | | 1 | GameObject\Generic Close Button_-5975704140969246810.json |
| Icon (Close) | (1507.5,145.7) 50.7×49.0 | (0.127,0.137,0.873,0.863) | **40k_bt_close**（175×174） | | 1 | GameObject\Icon_-5525257267418464346.json |
| Mask Tabs buttons | (400.4,173.3) 1129.0×741.4 | full offset(10.2,-9.9,9.8,-9.4) | 40k_popup | | 1 | GameObject\Mask Tabs buttons_3867140593184898982.json |
| Tab Buttons | (391.3,164.8) 160.6×758.8 | (0,0,0.14,1) | — | | 1 | GameObject\Tab Buttons_-301262919896891482.json |
| Separators | (550.6,146.8) 2.6×794.8 | (1,0,1,1) offset(-1.5,1.4,-20,20) | 40k_Separator Fade Sides Vertical (0.02,0.32,0.21,1) | | 1 | GameObject\Separators_4450700267126161318.json |
| Tab Content | (551.9,164.8) 929.0×758.8 | (0.14,0,0.95,1) pivot(0,0.5) | — | | 1 | GameObject\Tab Content_-1958548370395332698.json |

### 2.3 Tab 键列（★布局组公式，prefab 快照 y=852.6 不可用）

**Tab Buttons VGroup 参数**（MonoBehaviour\..._-8185144684232147034.json）：`m_Enabled=1, padding Top=13/Bottom=0, spacing=8.92, alignment=5(MiddleRight), ChildControlW=0/H=0, ChildForceExpandW=1/H=0, ChildScaleHeight=1`。
另：Tab Buttons 上有 **ToggleGroup**（AllowSwitchOff=0，Mono \..._378544895857295270）+ 自定义 Tab 脚本（Mono \..._-6549404459375099994，`options:[{tab,toggle}...]` 引用 5 键）。

**5 键运行时布局（视觉）**：键宽 148.5 = 165×0.9；键高 141.93 = 157.7×0.9；间距 8.03 = 8.92×0.9；padding top 11.7；MiddleRight → 键右缘=列右 551.9，键 x = **403.4**；竖直排 top = 179.2 + i×149.96（i=0..4）。

| 键 | 视觉 (x,y,w,h) | 键底图(button_bg) | 图标 Sprite | 标题文字 35px 白 | m_IsOn | Toggle JSON |
|---|---|---|---|---|---|---|
| General | (403.4,179.2) 148.5×141.9 | **40K_settings_button_hover**（on 态！） | 40K_settings_button_general | 'General' | **1** | GameObject\General_4781754479190835110.json（Toggle Mono \..._2348637581993934758） |
| Media | (403.4,329.1) 148.5×141.9 | 40K_settings_button | 40K_settings_button_quality | 'Multimedia' | 0 | GameObject\Media_6879991055787392934.json |
| Account | (403.4,479.1) 148.5×141.9 | 40K_settings_button | 40K_settings_button_account | 'Cuenta' | 0 | GameObject\Account_599645953609269158.json |
| Graphics | (403.4,629.0) 148.5×141.9 | 40K_settings_button | 40K_settings_button_graphics | 'Gráficos' | 0 | GameObject\Graphics_-5168413219369943130.json |
| Support | (403.4,779.0) 148.5×141.9 | 40K_settings_button | 40K_settings_button_support | 'Soporte' | 0 | GameObject\Support_3446293880883281830.json |

**键内子元素**（相对键，未缩放 → 视觉换算）：
- `button_bg`：拉伸全键。**Toggle 组件字段：onSprite=40K_settings_button_hover(-2307655919992762574)、offSprite=40K_settings_button(1956647257489494794)、spriteToChange=button_bg Image、changeSpriteOnValueChange=1、m_IsOn General=1 其他=0**（切换选中态换底图！项目现有实现已做此逻辑但底图名用 `40K_settings_button_selected.png` —— **原版无 selected 资产，选中=hover 变体**）。颜色 (0,1,0.64,0.71) 绿。
- `Icon`：pos(0,12.6) 相对键中心（Unity y 上 → 视觉中心 y = 键中心y - 11.34），141.4×106.8 → 视觉 127.3×96.1，color (1,1,1,0.86)。JSON：GameObject\Icon_-6455666725173624922.json 等（每键一个 Icon PathID）。
- `Label(pivot 0.5,0)` → `Tab Toggle Title`：pos(0,-67.2) → 视觉顶部=键底上方 60.5(=67.2×0.9)；155×40 → 139.5×36；**35px 白 (1,1,1,1)**。JSON：GameObject\Label_-7814110490308477018.json / Tab Toggle Title_289300845483753382.json。
- **Badge Highlight**（仅 Support 键）：pos(64.3,51.7) 相对键中心 35×35 → 视觉 (519.8,787.8) 31.5×31.5，**40K_notification_number**（65×65）color(0.74,0.74,0.74,1)；OneText：'' **34px** 白。JSON：Badge Highlight_-6067555852508495962.json。

### 2.4 General Tab（active，默认页；无布局组 → 快照=视觉）

| 元素 | 视觉 (x,y,w,h) | 贴图 | 文字/字号/颜色 | active | 原始 JSON |
|---|---|---|---|---|---|
| General Tab | (551.9,164.8) 929.0×758.8 | — | | 1 | GameObject\General Tab_4625536937723592614.json（脚本 Mono\..._5160047533284622246 字段: languageSelector/disableBotsToggle/disableNotificationsToggle/touchInputToggle/versionText/ExitButton/RedeemCodeButton） |
| Tab Title | (632.9,224.3) 848×63 | — | **'General' 55px 白** | 1 | Tab Title_-5322248279465623642.json |
| VersionText | (1200.4,182.8) 245.7×36.7 | — | **'v0.15.5PREPROD-0' 28px 白** | 1 | VersionText_3719459358269472678.json |
| Language Selector | (632.9,359.1) 751.3×53.4 | — | | 1 | Language Selector_-1133165519560081498.json |
| LanguagesDropdown | (632.9,359.1) 360.6×53.5 | **40K_dropdown_field_closed** (0.29,0.96,0.69) Button | 内 Label '' 18px | 1 | LanguagesDropdown_-2216660945872584794.json |
| Arrow | (971.0,376.8) 18×18 | **40K_dropdown_arrow_closed** (0.09,0.35,0.25) | | 1 | Arrow_7074655610719731622.json |
| Template(下拉列表) | (632.9,405.6) 356.1×516.5 | 40K_dropdown_bg | | **0** | Template_-5311206632940994650.json |
| └ Viewport | (632.9,405.6) 340.8×516.5 | 透明(0.37,0.89,0.59) | | 0 | Viewport_-8877427368193720410.json |
| └ Content→Item | 行 41.7 高 → 视觉 37.5 | — | | 0 | Content_4671579718064373670.json |
| └ Item Background | 拉伸 | **40K_dropdown_item** (0.29,0.96,0.69) | | 0 | Item Background_-4239332898157920346.json |
| └ Item Checkmark | (642.9,365.4?) 20×20→18×18 | 40K_dropdown_item 勾 | | 0 | Item Checkmark_3214230085477826470.json |
| └ Item Label | (650.9,407.8) 313.8×34.0 | — | 'Option A' **30px** 白 | 0 | Item Label_-6937712486711722074.json |
| └ Scrollbar/Handle | (971.0,441.8) 18×480.3 | (1660267235368898380/5837791642106728268) | | 0 | Scrollbar_3486205763533045670.json |
| SelectLanguageText | (1017.5,359.0) 366.7×53.5 | — | **'Select Language' 42px 白** | 1 | SelectLanguageText_-7734231700157202522.json |
| Checkboxes | (632.9,455.5) 751.3×263.0 | — | | 1 | Checkboxes_-2531723942980386906.json |
| Disable Bots | 行1 (632.9,455.5) 751.3×68.0 | — | | 1 | Disable Bots_5390210448176742310.json |
| Disable Notifications | 行2 (632.9,528.0) 751.3×68.0 | | | 1 | Disable Notifications_3020289508228104102.json |
| Touch Input | 行3 (632.9,600.6) 751.3×68.0 | | | 1 | Touch Input_7778645706359472038.json |
| └ Toggle(每行) | (632.9,行y) 107.1×68.0 | **40K_dropdown_bg** (1,1,1,1) | | 1 | Toggle_2661784937123315622.json |
| └ CheckMark | 拉伸 Toggle | **40K_settings_icon_checkmark** (66×51) | | 1 | CheckMark_5120618986433380262.json |
| └ Label(每行) | (740.0,行y) 644.2×68.0 | — | **'Disable Bots/Disable Notifications/Touch input' 42px 白** | 1 | Label_1222800531428966310.json |
| Bottom Buttons | (632.9,755.6) 848×81 | — | | 1 | Bottom Buttons_-4281752605896245338.json |
| Redeem Code | (632.9,755.6) 270×81 | **40K_button (0.37,0.89,0.59)** Button | 'Redeem Code' **40px** 白 | 1 | Redeem Code_-5279191389464330330.json |
| Close Game Button | (942.9,755.6) 270×81 | 40K_button (0.37,0.89,0.59) | 'Exit Game' **38px** 白 | 1 | Close Game Button_5721816160092848038.json |
| Button Text | 均拉伸按钮 | — | (居中) | 1 | Button Text_-7437928960549290074.json |

Checkboxes VGroup：`Enabled=1, padding 0, spacing 5.0, align 0(UpperLeft), CtrlW=1 CtrlH=0, ForceW=1` → 3 行每行 68.04 高、间距 4.5、从 (632.9,455.5) 顶部排。行内 HGroup（Disable Bots 上 Mono\..._-6087336142770307162）：`spacing 0, align 0, CtrlW=1 CtrlH=1, ForceW=0 ForceH=1` → Toggle 视觉宽 107.1(=40K_dropdown_bg 纹理 119×0.9)、高 68.0；Label 起 x=740.0。
Bottom Buttons HGroup：`Enabled=1, padding 0, spacing 40, align 0(UpperLeft), CtrlW=0 CtrlH=0, ForceW=0 ForceH=1` → Redeem (632.9,755.6)、Exit (632.9+270+36=**942.9**,755.6)，均 270×81。

### 2.5 Media Tab（active）

| 元素 | 视觉 (x,y,w,h) | 贴图 | 文字/字号 | 原始 JSON |
|---|---|---|---|---|
| Media Tab | (551.9,164.8) 929.0×758.8 | | | Media Tab_-4141130078537547866.json |
| Tab Title | (632.9,224.3) 848×63 | | 'Multimedia' 55px 白 | Tab Title_-3737757086216847450.json |
| Audio Settings | (632.9,306.1) 615.8×315.7 | — | | Audio Settings_4102939723637817254.json |
| Music Container | (632.9,306.1) 615.8×94.5 | Image->?(0.24,0.24,0.24,1) 快照垫 | | Music Container_-6002086298825621594.json |
| └ Music Slider | (632.9,357.5) 615.8×11.7 Button | 轨 | | Music Slider_-2677944884821327962.json |
| └ Background | 轨拉伸 | **Volume_bar_inactive** | | Background_-3122758164611301466.json |
| └ Fill | 轨拉伸 | **Volume_bar_active** | | Fill_9211155765658419110.json |
| └ Handle Slide Area→Handle | (622.6,368.6) 42.1×20.2 | **Volume_button** | | Handle_4755845432359026598.json |
| └ Label | (632.9,294.0) 307.9×55.8 | | 'Música' **42px** 白 | Label_-3320084143067136090.json |
| FX Container | (632.9,400.6) 615.8×95.4 | 同上 | | FX Container_-978140520457601114.json |
| └ Sound effects Slider | (632.9,452.0) 615.8×11.7 | | | Sound effects Slider_2830778641409081254.json |
| └ Label | (632.9,388.9) 307.9×56.7 | | 'Efectos de Sonido' 42px 白 | Label_7387045382514573222.json |
| Voiceovers Container | (632.9,496.0) 615.8×95.4 | | | Voiceovers Container_7812398949032624038.json |
| └ Voice Over Slider | (632.9,547.4) 615.8×11.7 | | | Voice Over Slider_-5332939918518419546.json |
| └ Label | (632.9,484.3) 307.9×56.7 | | 'Narraciones' 42px 白 | Label_-7819588473204867162.json |
| Visual Settings | (632.9,621.9) 800.1×268.7 | | | Visual Settings_8001456313638354854.json |
| WindowMode Selector | (632.9,621.9) 751.3×53.5 | | | WindowMode Selector_-3862718586440220762.json |
| └ Dropdown | (632.8,621.9) 360.6×53.5 | 40K_dropdown_field_closed (0.29,0.96,0.69) | Label ''18px | Dropdown_-7288258913784791130.json |
| └ Arrow | (970.9,639.6) 18×18 | 40K_dropdown_arrow_closed (0.09,0.35,0.25) | | Arrow_-3319543017719562330.json |
| └ Template/Item/Scrollbar | | 同 General 下拉（30px item） | | Template_6987110399555174310.json 等 |
| Label | (641.8,675.3) 366.7×53.5 | | 'Modo Ventana' **42px** 白 | Label_7928232658061000614.json |

Audio Settings VGroup：`Enabled=1, padding 0, spacing 0, align 0, CtrlW=1 CtrlH=0, ForceW=1 ForceH=1` → 3 个 Container 每行自身高 94.5/95.4/95.4、宽拉满 615.8，从 306.1 顶部排。行内：Slider 中心=行中心+9.99 向下（pos y=-11.1）；Label 中心=行中心-31.5 向上（pos y=+35），Label 顶略溢出行顶（-12.2px）属原版设计（无裁剪）。
⚠️ **Visual Settings VGroup 疑点**：`Enabled=1, spacing 0, align 0, CtrlW=0 CtrlH=0, ForceW=1 ForceH=1`。按 Unity 手册（Force Expand 仅 Child Control 开启时生效）→ 运行时 Selector/Label 保持自身 59.4×2 高、从容器顶 621.9 排（上表即此方案）；**prefab 快照坐标（audit 表）为 Selector (257.2,863.8)**。两者相差 242px。若整屏截图对比发现窗口模式应贴页底，改用快照方案 (257.2,863.8)+(641.8,863.8)。实施后请以原版整屏观感终判（Media 页底部）。

### 2.6 Graphics Tab（inactive 默认；快照=视觉）

| 元素 | 视觉 (x,y,w,h) | 贴图 | 文字/字号 | 原始 JSON |
|---|---|---|---|---|
| Graphics Tab | (551.9,164.8) 929.0×758.8 | | | Graphics Tab_-7383123982260273242.json |
| Tab Title | (632.9,224.3) 848×63 | | 'Gráficos' 55px 白 | Tab Title_7487528459173592998.json |
| Content | (551.9,294.9) 929.1×628.6 | | ★含 HGroup: spacing 23, align 0, Ctrl=0, Force=0 | Content_-7767295202069676122.json |
| Quality Selector | (592.4,294.9) 751.3×53.4 | | | Quality  Selector_-4997617895784284250.json |
| └ Quality DropDown | (592.4,294.9) 360.6×53.5 | 40K_dropdown_field_closed (0.29,0.96,0.69) | Label '' 18px | Quality DropDown_-1629605811713507418.json |
| └ Arrow | (930.5,312.7) 18×18 | 40K_dropdown_arrow_closed (0.09,0.35,0.25) | | Arrow_-6840201424618160218.json |
| └ Quality selector text | (977.0,294.9) 366.7×53.5 | | 'Seleccionar Calidad' **42px** 白 | Quality selector text_-3454495057096769626.json |
| Text In Hand Selector | (592.4,369.1) 751.3×53.4 | | | Text In Hand  Selector_1307906736316252070.json |
| └ Text in Hand DropDown | (592.4,369.1) 360.6×53.5 | 40K_dropdown_field_closed | | Text in Hand DropDown_-2614653520048980058.json |
| └ Quality selector text | (977.0,369.1) 366.7×53.4 | | 'Texto para cartas en mano' **42px** 白 | Quality selector text_-2439088495673835610.json |
| Scroll View | (593.0,443.2) 888.7×469.4 | | | Scroll View_3899934504175894438.json |
| └ Viewport | (603.2,443.2) 867.0×469.4 | | | Viewport_-4567078880021348442.json |
| └ Content | (603.2,443.2) 409.7×270.0 | | | Content_2185962370154463142.json |
| └ Small Screen Size Toggle | (603.2,443.2) 409.7×68.0 | Toggle=40K_dropdown_bg + CheckMark=40K_settings_icon_checkmark | 'Aumentar tamaño de UI' **42px** 白 | Small Screen Size Toggle_5777285256249507750.json |
| └ Auto Zoom Toggle | (603.2,515.8) 409.7×68.0 | | 'Auto zoom' 42px 白 | Auto Zoom Toggle_-7726404914777063514.json |
| └ Hi FPS toggl | (603.2,588.4) 409.7×68.0 | | 'Alta tasa de refresco' 42px 白 | Hi FPS toggl_9025102222751006630.json |
| └ Android extra compatibility | (603.2,661.0) 409.7×68.0 | | 'Compatibilidad extendida' 42px 白 | Android extra compatibility_-1890495269183979610.json **inactive** |
| └ └ Tooltip - Extended compaibility | (1046.7,661.0) 68.3×68.0 | **40K_generic_bt_info** | | Tooltip - Extended compaibility_7981327631678472102.json |
| └ Use super sampling | (603.2,661.0) 409.7×68.0 | | 'Sobremuestreo' 42px 白 | Use super sampling_-1080153348310990938.json |
| └ Vsync | (603.2,733.6) 409.7×68.0 | | 'VSync' 42px 白 | Vsync_-4931308610596929626.json |
| └ FPS Limit | (603.2,806.1) 409.7×94.5 | | | FPS Limit_3725205647961587622.json |
| └ └ Title | (617.6,793.5) 278.6×55.8 | | 'Límite de FPS' **42px** 白 | Title_6372010424437473190.json |
| └ └ FPS Slider | (842.6,881.9) 442.1×11.7 | Volume_bar_inactive/active + Volume_button | | FPS Slider_-3749264034945400922.json |
| └ └ 30 FPS / 60 FPS / Unlimited | (749.9,830.5)/(966.7,830.5)/(1179.2,826.1) 各 205.2×55.8 | | '30'/'60'/'Ilimitado' **42px** 白 | 30 FPS_162192926652530598.json 等 |

⚠️ **Content 上 HGroup（spacing 23）存疑**：若生效，Quality/TextInHand/ScrollView 三块水平排（总宽 2433 >> 929 溢出页外）——与快照竖排及常理矛盾。候选结论：a) 该 HGroup 实际使三项横排（不合理）；b) 布局组对"未激活页"不排且在激活时……仍横排。**建议按快照竖排复刻**（项目现状已与快照一致：Quality y294.9 → 项目 (90,268) 相对页 ≈ (641.9,432.8)? 下差异表细述），并以原版整屏截图观感终判。

Toggle 行内布局（Scroll Content 无布局组 → 快照=视觉）：Toggle (603.2,行y) 107.1×68.0（pos 59.5 相对行中心 → 行宽 409.7）；Label 起 x=710.3, 宽=行宽-107.1。行距 72.6（=118.5-37.8 未缩放 ×0.9）。
FPS Limit 行：pos(227.6,-455.7) 相对 Content 顶 → 视觉 (603.2,806.1) 409.7×94.5；FPS Slider (842.6,881.9) 442.1×11.7；30/60/Ilimitado 均 228×62 → 205.2×55.8, 42px。

### 2.7 Account Tab（inactive 默认；全套表单，快照=视觉关键值）

| 元素 | 视觉 (x,y,w,h) | 贴图 | 文字/字号 | 原始 JSON |
|---|---|---|---|---|
| Account Tab | (551.9,164.8) 929.0×758.8 | | | Account Tab_6977187114249977766.json |
| Tab Title | (632.9,224.3) 848×63 | | 'Account' 55px 白 | Tab Title_3773921610551361446.json |
| Player Id | (1129.5,202.9) 330.4×35.1 | | 'Player ID: 325161617' **40px** 白 | Player Id_7471851218865455014.json |
| Player Id Text | (1072.4,194.7) 387.5×47.4 | | | Player Id Text_7513478670087651238.json |
| External Link Icon | (1063.9,190.8) 51.2×51.3 | **Copy@3x** rect(0,0,48,48) | | External Link Icon_-4769325090132688986.json |
| Account Form | (632.9,299.8) 828.0×370.8 | | | Account Form_2458092180012236710.json |
| EmailText | (632.9,289.3) 414×54 | | 'E-mail' **37px** 白 | EmailText_-2832386156305350746.json |
| InputEmail | (632.9,342.6) 828×54 | 40K_dropdown_bg (0.29,0.95,0.68) | Placeholder ''18px/Text 40px | InputEmail_9217059814301990822.json |
| PasswordText | (632.9,405.6) 414×54 | | 'Password' 37px 白 | PasswordText_309385981998301094.json |
| InputPassword | (632.9,459.7) 828×54 | 40K_dropdown_bg | | InputPassword_4884970622036705190.json |
| Reset Password | (1046.9,417.1) 414×39.9 | | 'Reset Password' **32px** 白 Button | Reset Password_8178967897677594534.json |
| Forgot Password | (1046.9,417.1) 414×39.9 | | 'Forgot Password' 32px 白 Button | Forgot Password_-2103729280699039834.json |
| Error Message | (632.9,526.1) 828×42.4 | | '* Invalid Password' **37px** 白 | Error Message_-318271249664737370.json |
| Subscribe Newsletter | (632.9,551.7) 539.5×69 | | 'Subscribe to the Newsletter?' **40px** 白 Button | Subscribe Newsletter_8947213454270627750.json |
| Social Media Links | (622.4,654.1) 573.5×72.8 | | | Social Media Links_-6415323874570567770.json |
| Discord Button | (622.4,647.7) 114.7×85.5 | **Discord-Logo-Color** | | Discord Button_-7876065212153364570.json |
| IG Button | (737.1,656.7) 114.7×67.5 | **Instagram_icon** | | IG Button_7684066536174747558.json |
| Facebook Button | (851.8,656.7) 114.7×67.5 | **fb-icon** | | Facebook Button_8612904505745833894.json |
| Twitter Button | (966.5,656.7) 114.7×67.5 | **Twitter_Social_Icon_Rounded_Square_Color** | | Twitter Button_-7641732877469581402.json |
| Youtube Button | (1081.2,654.5) 114.7×72.0 | **YouTube_full-color_icon_(2017).svg** | | Youtube Button_4453274433351876518.json |
| Buttons (容器) | (971.4,675.4) 90×90 | platforms 组件 | | Buttons_5573572599672438694.json |
| Unregistered Buttons | (898.1,544.7) 559.8×81 | | | Unregistered Buttons_-181356464059809882.json |
| Register Button | (1187.9,544.7) 270×81 | 40K_button (0.37,0.89,0.59) | 'Register' **40px** | Register Button_-5583086498785427546.json |
| Login Button | (1178.0,544.7) 270×81 **inactive** | 40K_button | 'Log in' 40px | Login Button_6914329876671004582.json |
| Twitch Button | (914.4,778.8) 267.6×81 **inactive** | **40K_button (1,0,0.89,1) 粉** | 'Link Twitch' 38px | Twitch Button_1652937718928670630.json |
| Delete Button | (1190.9,779.5) 270×81 | **40K_button (1,0.03,0,1) 红** | 'Delete account' 40px | Delete Button_2530498445530660774.json |
| Registered Buttons | (632.9,778.8) 594×81 | | | Registered Buttons_-5081667507277234266.json |
| Switch Account Button | (632.9,778.8) 270×81 | 40K_button (0.37,0.89,0.59) | 'Switch Account' 40px | Switch Account Button_4691308697010012070.json |
| Logout Button | (929.9,778.8) 270×81 **inactive** | 40K_button | 'Выйти из системы' **33.75px** | Logout Button_-1026035652693688410.json |
| Login Window | (420.3,292.2) 1087.7×360 **inactive** | | | Login Window_3053592964502880166.json |
| └ Generic Popup Background | 同框架 | 40k_popup + 40k_popup_texture | | Generic Popup Background_2109661778368429990.json |
| └ EmailText/InputEmail/PasswordText/InputPassword | (458.3,331.6)/(458.3,384.9)/(458.3,447.9)/(458.3,502.0) | 40K_dropdown_bg | 37px/40px | EmailText_-6384130909698883674.json 等 |
| └ Forgot Password | (795.3,460.6) 393.8×39.9 | | 'Forgot Password' 32px | Forgot Password_4982768266054959014.json |
| └ ErrorMensajeContainer | (458.3,573.1) 730.8×33.1 | | | ErrorMensajeContainer_-4597319549924376666.json |
| └ Animated Loading Image/Cog | (458.3,572.6) 34.1×34.1 | **40K_icon_searching_skull / 40K_icon_searching_cog** | | Animated Loading Image_6483071373931347878.json |
| └ Error Message | (503.2,573.1) 696.7×33.1 | | '* Invalid Password' 37px | Error Message_5481181439886065574.json |
| └ Login Button | (1210.5,500.5) 278.3×54 | 40K_button | 'Log in' 40px | Login Button_-2873166905862488154.json |
| └ Generic Close Button Green | (1469.5,262.9) 67.5×67.5 | UI_Button_Round_background + 40k_bt_close | | Generic Close Button Green_2789484781694320550.json |

### 2.8 Support Tab（inactive 默认）

| 元素 | 视觉 (x,y,w,h) | 贴图 | 文字/字号 | 原始 JSON |
|---|---|---|---|---|
| Support Tab | (551.9,164.8) 929.0×758.8 | | | Support Tab_-2614690941459267674.json（脚本引用 privacyPolicyButton/termsOfServiceButton/faqButton/contactButton/supportButton） |
| Tab Title | (632.9,224.3) 848×63 | | 'Support' 55px 白 | Tab Title_2944597960171224998.json |
| Faq Text | (632.9,299.0) 848×76.5 | | 'Questions about the game? Visit the Frequent Asked Questions' **35px** 白 | Faq Text_9202905503072166.json |
| Faq Button | (632.9,389.8) 324×54 | 40K_button (0.37,0.89,0.59) | 'FAQ' **35px** | Faq Button_1095624222620483494.json |
| └ External Link Icon | (641.8,402.6) 36.1×28.4 | **Button_External_Link** | | External Link Icon_1052163399318929318.json |
| Contact Text | (632.9,461.4) 848×56.6 | | 'Do you need help from us?' 35px 白 | Contact Text_-423170690666496090.json |
| Contact Button | (632.9,530.9) 324×54 | 40K_button | 'Contact' 35px + 外链图标 | Contact Button_3857688997120081830.json |
| Support Button | (632.9,389.1) 324×54 | 40K_button | 'Support' 35px（与 Faq 同位置=旧版副本） | Support Button_-1007316107269603418.json |
| Email Text | (632.9,611.8) 848×124.2 | | "You can also contact us at support@everguild.com\nWe'll do our best to answer as soon as possible." 35px 白 | Email Text_-1623544072920268890.json |
| bottom links | (632.9,776.8) 848×53.1 | | | bottom links_8610941976387157926.json |
| Terms of Service | (632.9,776.8) 424×53.1 | Button + External Link Icon (632.9,789.2) 36×28.4 | 'Terms of Service' **35px** | Terms of Service_3665878762108256166.json |
| Privacy Policy | (1056.9,776.8) 424×53.1 | External Link Icon (1056.9,789.2) | 'Privacy Policy' 35px | Privacy Policy_-2675816412195422298.json |
| Faq Text Mobile / Email Text Mobile | (632.9,299.0)/(632.9,463.7) | | 35px（移动端副本，桌面忽略） | Faq Text Mobile_662520627710099366.json |

---

## 3. 字体汇总（原版 m_fontSize，全部白 (1,1,1,1)）

| 元素 | 原版字号 | 元素 | 原版字号 |
|---|---|---|---|
| Tab Toggle Title（键标题） | **35** | Checkbox Label（General 页） | **42** |
| Tab Title（页标题） | **55** | Music/FX/Voice Label | **42** |
| VersionText | **28** | 'Modo Ventana' / 'Select Language' | **42** |
| Redeem Code | **40** | Exit Game | **38** |
| Quality/Text-in-hand selector text | **42** | Graphics 页 toggle Label | **42** |
| FPS Title / 30 / 60 / Ilimitado | **42** | 下拉 field Label / item Label | **18** / **30** |
| FAQ/Contact/Support 按钮 & 文案 | **35** | Terms/Privacy | **35** |
| Player Id | **40** | EmailText/PasswordText | **37** |
| 输入框 Text | **40** | 输入框 Placeholder | **18** |
| Reset/Forgot Password | **32** | Error Message | **37** |
| Subscribe Newsletter | **40** | Register/Login/Delete/Switch | **40** |
| Twitch | **38** | Logout | **33.75** |
| Badge OneText | **34** | Debug 按钮组 | 12~24 / 标题 36 |

---

## 4. 项目现有实现差异清单（D:\warpforge\scripts\settings.gd，530 行）

### 4.1 结构性（必须）

| # | 项 | 原版（权威） | 项目现状 (settings.gd) | 差异 |
|---|---|---|---|---|
| S1 | **0.9 缩放层** | 根 RT m_LocalScale=0.9，全树以 (960,540) 缩放，视觉 1728×972 | 无任何缩放；所有元素用未缩放坐标且不平移 | **根本差异：所有元素大 11.1%、左偏 63.3、上偏 41.8（L74-75 win 328,123 1274×843 实测视觉 (328,123) vs 权威 (391.3,164.8) 1146.9×758.8）** |
| S2 | Menu Area 底结构 | 3 层：40k_popup（窗口底）+ Mask 40k_popup + Background fill **40k_popup_texture**（中央 973.8×741.4 内衬）；+ Popup BG(inactive) | 单层 TextureRect 40k_popup 拉伸 1274×843（L72-80） | 缺中央内衬层 Background fill；无 Mask 层 |
| S3 | Close 按钮 | (1499.1,136.4) 67.5×67.5；圆底 **UI_Button_Round_background** + 40k_bt_close 图标 50.7×49（锚 0.127..0.873） | (1559,92) 75×75 flatten Button + 满铺 40k_bt_close keep-aspect（L83-97） | 位置偏差 (59.9,44.4)、尺寸 75→67.5、缺圆底纹理按钮态 |
| S4 | Tab 列 | 列 (391.3,164.8) 160.6×758.8 + Separators 竖线 (550.6,146.8) 2.6×794.8 | 无 Separators；列按 178 宽 x=328（L18 TAB_W=178、L114 b.position=(328,123+i×168.6)） | 键宽 178→**148.5**、键高 168.6→**141.93**（间距 8.03）、x 328→**403.4**、y 123+i×168.6→**179.2+i×149.96**；缺竖线 Separators |
| S5 | Tab 键底图（选中态） | Toggle on=**40K_settings_button_hover**、off=**40K_settings_button**（changeSpriteOnValueChange） | on 用 `40K_settings_button_selected.png`（L172） | 原版无 "selected" 资产（虽项目 assets 存在该文件，需确认是否等同 hover）；**建议改用 40K_settings_button_hover** |
| S6 | Tab 键图标 | 127.3×96.1，中心偏上 11.3（pos 0,+12.6），α=0.86 | 141×107@ (TAB_W-141)/2, TAB_H×0.16（L131-138） | 图标 141→127.3、96.1；位置换算；α 0.86 未设 |
| S7 | Tab 键标题 | 139.5×36 @ 键底上方 60.5，**35px 白 (1,1,1)** | 155×40 @ (TAB_W-155)/2, TAB_H×0.74，35px **e8e6e0**（L140-149） | 颜色应白；位置随键重排 |
| S8 | Badge Highlight（Support 键角标） | (519.8,787.8) 31.5×31.5 40K_notification_number + OneText '' 34px | **缺失** | 缺（notification 角标，内容为空串） |
| S9 | 页容器 | Tab Content (551.9,164.8) 929×758.8；页标题 (632.9,224.3) 848×63 **55px 白** | PAGE_POS=(507,123) PAGE_SIZE=(1032,843)（L20-21）；页标题 (90,66) 55px **金色 0.969,0.914,0.714**（L184 等） | 页定位随缩放层修正；标题色应白（或按项目统一金色 = 用户决策点） |
| S10 | 背景 | Menu Dark Background (0,0,0,**0.77**) 覆盖 4117×2315 中心 (960,540) | MenuBg.build + `dark.color=(0.11,0.045,0.055,0.77)` 红棕（L66-70） | 原版纯黑 0.77；项目偏红棕 |
| S11 | Debug Buttons / old menu | 有（调试区 17 键；old menu inactive） | 无 | 忽略（开发调试用；old menu inactive） |

### 4.2 General 页

| 元素 | 原版 | 项目 | 差异 |
|---|---|---|---|
| VersionText | 'v0.15.5PREPROD-0' **28px** 白 @(1200.4,182.8) | 'Godot single-player build v0.9' 16px 灰 8a8f98 @(720,20)（L186） | 文字/字号/颜色/位置全部不同（复刻准则标注：信息性替换文案） |
| 语言选择 | 'Select Language' **42px** 白 @(1017.5,359.0)；下拉 360.6×53.5 @(632.9,359.1) | 'Language' 24px @(90,210)；OptionButton 401×59 @(90,216)（L188-196） | 文字 24→42+右侧 42px 标签；下拉 401×59→**360.6×53.5**；定位 (81,194.3) |
| checkbox | 行 @(632.9,455.5/528.0/600.6) 68.0 高、Toggle 107.1 宽 40K_dropdown_bg+checkmark、Label 'Disable Bots/Disable Notifications/Touch input' **42px** 白 x=740 | CheckButton @(90,300+i×108) 420×76、24px e8e6e0（L198-216） | 行位/行距 (455.5 vs 300; 72.5 vs 108)、Toggle 视觉、字号 24→42、文字 'Touch Input'→'Touch input'（原版小写 i） |
| Bottom 按钮 | Redeem (632.9,755.6) 270×81 40px；Exit (942.9,755.6) 270×81 38px | (90,640)/(440,640) 300×90、24px（L218-234） | 尺寸 300×90→**270×81**；位置 (81,590.8)/(391,590.8) 相对页；字号 24→40/38 |

### 4.3 Media 页

| 元素 | 原版 | 项目 | 差异 |
|---|---|---|---|
| 音量 3 行 | 行 (632.9,306.1/400.6/496.0) 高 94.5/95.4/95.4；滑轨 615.8×11.7 + Label 'Música/Efectos de Sonido/Narraciones' **42px** 白在上 | Label (0,315/438/561) 24px + HSlider (90,337/460/583) **684×13**（L244-249） | 行距 123→**94.5**；滑轨 684×13→**615.8×11.7**；Label 42px；位置 (81,相对页 y306.1+…) |
| 窗口模式 | WindowMode Selector (632.9,621.9)（VGroup 方案）含 Dropdown 360.6×53.5 + Arrow + 'Modo Ventana' 42px | Label (0,508) 24px + OptionButton (90,514) 401×59（L251-261） | 位置 (81,457.1)；尺寸 401×59→360.6×53.5；文字 42px；页底（快照 (257.2,863.8) 备选方案见 §2.5） |
| 滑轨样式 | Volume_bar_inactive/active + Volume_button Handle 42.1×20.2 | 已有 _style_slider（同贴图）✓ | 样式 OK，尺寸/位置随上 |

### 4.4 Graphics 页

| 元素 | 原版 | 项目 | 差异 |
|---|---|---|---|
| 两个下拉 | (592.4,294.9)/(592.4,369.1) 360.6×53.5 + 右侧 42px 西语标签 | Label (90,246/328) 24px 'Quality Preset'/'Hand Text Size' + OptionButton (90,268/350) **684×59** 24px 文本（L332-358） | 下拉 684×59→**360.6×53.5**；标签 42px 白；位置 (40.5,130.1)/(40.5,204.3) 相对页 |
| 6 开关 | 行 (603.2,443.2/515.8/588.4/661.0×2/733.6) 68.0 高 行距 72.6、Toggle 107.1 宽 + Label 42px 白 x=710.3；Android 行含 Tooltip 40K_generic_bt_info（inactive） | CheckButton (90,432+i×80) 500×60、24px、含 "Android compatibility" 行（L360-381） | 行距 80→**72.6**、Toggle 107.1 宽、Label 42px；Tooltip 图标缺失；'androidCompat' 行原版 inactive |
| FPS Limit | (603.2,806.1) 409.7×94.5：Title 42px + **FPS Slider 442.1×11.7**（Volume 样式）+ 30/60/Ilimitado 42px | Label 24px + OptionButton (90,ty+56) 684×59 '30 FPS/60 FPS/Unlimited'（L383-396） | 原版是 **Slider**（非下拉）！+ 3 个文字档位；标题 42px |
| Scroll View | 有 Scroll View+Viewport+Content（可滚动 4 行+FPS 行在 806 可见区） | 无滚动容器（直接铺页上） | 页内仍可见（高度内容相同），可不做滚动容器——列差异待验收 |

### 4.5 Account 页（原版全套表单+社交按钮；项目=自制文字说明）

| 元素 | 原版 | 项目 | 差异 |
|---|---|---|---|
| Player 信息 | 'Player ID: 325161617' 40px + Copy@3x 复制图标 51.2×51.3 | 'Player name: %s' 20px + 'Player ID: single-player build' 18px + 说明文字 16/15px（L314-322） | 自制文案替换缺口（离线版无账号系统）。实施建议：保留自制说明或按原版贴图/文字复刻骨架（决策点） |
| 表单/社交/按钮 | 完整（Email/Password 输入、Reset/Forgot、Subscribe Newsletter、5 社交按钮、Register/Login/Twitch/Delete/Switch/Logout、Login Window inactive） | 全部缺失 | 4.2 节全套缺失（批次 4 若只做 scale 容器可暂缓，报告在案） |

### 4.6 Support 页

| 元素 | 原版 | 项目 | 差异 |
|---|---|---|---|
| FAQ/Contact | Faq Text 35px @(632.9,299.0) + 按钮 324×54 35px + 外链图标 Button_External_Link 36.1×28.4 | 18px 文案 (90,149/330)、_make_button (90,250/407) **360×60**、按钮文字未设字号（Button 默认 ~16px!）（L407-416） | 字号 18→**35**、按钮 360×60→**324×54**、按钮字 16→**35**、缺外链图标 |
| Email | 'You can also contact us at support@everguild.com...' 35px 白 | 18px 灰（L414） | 字号/颜色 |
| 底部链接 | Terms of Service / Privacy Policy + 外链图标 @(632.9/1056.9,776.8) 424×53.1 | **缺失**（项目在 Support 页放自制"Give Feedback survey/Rate the game"按钮（L418-426，非原版元素=自制扩展，属新增内容） | 底部链接缺失；自制按钮=非原版（保留与否决策点） |

---

## 5. 实施建议：Godot 侧 0.9 缩放容器（核心方案）

**方案（与原版完全同构，改动最小）：**

```gdscript
# settings.gd _build_ui() 开头（MenuBg/暗色层之后）：
var _scale_root := Control.new()
_scale_root.set_anchors_preset(Control.PRESET_FULL_RECT)   # 1920×1080
_scale_root.pivot_offset = Vector2(960, 540)               # 缩放轴=屏幕中心
_scale_root.scale = Vector2(0.9, 0.9)
_scale_root.mouse_filter = Control.MOUSE_FILTER_IGNORE
add_child(_scale_root)
```

然后：`win`、`close_btn`、5 个 Tab 按钮、5 个 page 全部 `add_child(_scale_root)` 而非 `add_child(self)`；**现有全部坐标数值保持不变**（328,123/1274×843/1559,92/75×75/507,123/1032×843/178 宽……即菜单全树=prefab 未缩放局部链坐标，缩放后自动=权威值 391.3,164.8 1146.9×758.8 等，验证: (328-960)×0.9+960=391.2, (123-540)×0.9+540=164.7）。

**理由**：原版正是如此——根 RT 全屏 + scale 0.9 + pivot(0.5,0.5)，子元素保持 prefab 坐标。Godot 对等物 = full-rect Control + pivot_offset(960,540) + scale 0.9。菜单全树坐标（328,123 1274×843 等）= 该坐标系下的子坐标，可 1:1 使用。

**注意**：
1. MenuBg.build(self) 与 dark 全屏层**不放**进 _scale_root（原版 Dark Background 语义=窗口外场景背景；放根层即可——原版本应也乘 0.9，但 dark 覆盖 4117×2315 远超屏幕，无视觉差异）。dark 颜色建议由 (0.11,0.045,0.055,0.77) 改回原版 (0,0,0,0.77)。
2. NavBuilder.build(self, "")（L40）保持 self 根层不动。
3. 缩放后页内坐标链：page.position=507,123 → 视觉 551.9,164.8 ✓（§4 差异表中"相对页"坐标=原版 prefab 相对 Tab Content 的 pos（如 Redeem 相对页 (81,590.8)），主代理定位时注意页内元素用视觉绝对坐标而非（页顶+ 90 之类）。

**后续（可选）修正清单**（按 §4 差异表逐项；批次 4 若聚焦缩放容器，S1-S3 必做，S4-S8/S9 次之，4.2-4.6 页内细节排后）。

关键原始 JSON 行号速查（dump_go_tree 输出 tmp_settings_tree.txt 行号 / 文件）：
- 根缩放：RectTransform\RectTransform_-7066813013973172314.json（m_LocalScale 0.9）
- Tab 键 Toggle on/off sprite：GameObject\General_4781754479190835110.json → MonoBehaviour\..._2348637581993934758.json
- 5 布局组：MonoBehaviour 中 `m_Padding/m_Spacing` 字段（Tab Buttons -8185144684232147034 / Checkboxes -8816793191438516314 / Bottom Buttons 561881817965166502 / Audio Settings -897860312560992346 / Visual Settings 5428376091839725478 / Content HGroup 4427977381967855526 / Disable Bots HGroup -6087336142770307162），全部 m_Enabled=1
- 全部 m_IsActive：GameObject\*_<PathID>.json 的 m_IsActive 字段（General Tab/Media Tab=1，Account/Support/Graphics Tab=0，old menu/Popup BG=0，AddCoins/Season Check/AddWildcards=0，Android extra compatibility=0）
- Sprite 文件：`解包整理/12_主程序资源/Sprite/`（40k_popup 359×336、40k_popup_texture 128×128、40K_dropdown_bg 119×102、40K_dropdown_field_closed 727×102、40K_dropdown_arrow_closed 46×19、40K_dropdown_item 717×92、40K_button 489×107、40K_settings_button(+hover) 168×156、Volume_bar_inactive 400×31、Volume_bar_active 64×31、Volume_button 110×110、40K_settings_icon_checkmark 66×51）；`解包整理/03_界面UI/图集/0_mainmenu/Sprite/`（5 个 40K_settings_button_* 图标）；`03_界面UI/图集/Sprite/`（Button_External_Link、Discord-Logo-Color、Instagram_icon 等）；`03_界面UI/菜单/Sprite/Copy@3x.json`+Texture2D\Copy@3x.png
