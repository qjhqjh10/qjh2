# Card Displayer 三面板核查+实现报告 (2026-08-23)

**任务**：核实并补全原版 Card Displayer 三面板（Crafting / Upgrade / Alternate Art）+ Wildcard Segment + Card Display。
**结论先行**：三面板原版真实存在且项目已有完整实现骨架；本次核查发现 **续11"删除自创 Upgrade 按钮"的结论依据有误（原版确有 Upgrade 按钮）**，已在项目按原版权威恢复；并修正三面板多处与原始 Unity JSON 不符的"自创"元素。

---

## 一、核查方法（原始 Unity JSON 权威）

- 场景：`D:/2/解包整理/07_场景/mainmenuwarpforge/`（主菜单场景，GameObject/RectTransform/MonoBehaviour 全量 JSON）
- 根：`Card Displayer Menu For Menu`（GO PathID 479，m_IsActive=false，位于主菜单 Game UI→Main Canvas→**3 - PopUp Holder** 挂点）
- 工具：`dump_go_tree.py`（210 行全树）、脚本实例字段（MonoBehaviour）、`UpgradePanel.cs`/`CraftingPanel.cs`/`AlternateArtPanel.cs`/`WildcardDisplay.cs`/`CardDisplayWindow.cs`/`CardDisplayOptions.cs`（decompiled 存根,字段权威）
- 注意：**dump_go_tree 有 PathID 文件名碰撞缺陷**（见"坑 59"），本次多处以原始 GO/RT JSON 直接复核。

## 二、续11 删除核实结论 ★

**结论：半错。删"自创按钮"对（自创按钮=黄底 40K_button @(160,160) 130x62，与原版不符）；但"原版 Upgrade 面板无 Upgrade 按钮"的结论错（误删），原版确有 upgradeButton。**

证据链：
1. `Upgrade Panel`（GO 205）上挂 `UpgradePanel` 脚本实例（MB 2117，脚本类 = UpgradePanel.cs），字段 **`upgradeButton`（EverguildButton）= PathID 2247**，另有 neededCards/cost/rewardText/titleText/forgeIcon/costIcon。
2. GO **`Upgrade`（PathID 311）**= 升级按钮：RT 1341（父=Content RT 1357，锚(0.2,0.33535)-(0.80162,0.56678)，pivot(0.5,0)，尺寸≈270.4x60.3，与 Craft 按钮同为拉伸锚模式）+ Image 2215（sprite=UI_Button_Mulligan）+ Button 2247 + LayoutGroupContentFixer 2620 + 子"Button Text"（GO 316, m_text='Change Deck' 占位 40px，运行时本地化）。
3. 续11/2026-08-23 审查用 dump_go_tree 树漏打了该子树——因为 `Glow_311.json` 与 `Upgrade_311.json` **共享文件名后缀 PathID 311**，工具索引首见优先（Glow 赢），误判"Upgrade 不存在"。同批漏掉的还有 Wildcard 计数段的 **Rare**（`Rare_315.json` vs `Lightning_315.json` 碰撞）与两个 **quantity** GO（'12'/'12342' 数量占位）。
4. 修复恢复位置：**Upgrade 按钮 @ Content 局部 (90.0, 83.6) 尺寸 270.4x60.3**（chain 演算，与 Craft 按钮 x[90,360.4] 同列交叉验证一致），UI_Button_Mulligan 底、文字 "Upgrade" 40px 白。

## 三、原版权威表（三面板 + 通配符条 + Card Display 新核对项）

### 布局总框
- OptionPanel（Card Options Panel→Panel）: x[1294,1744] y[146,903]，450x757（锚(0.5,0.5) pos(559,15.1)）
- Crafting Panel y1-264.7 / Upgrade Panel y264.7-526.4 / Alternate Art Panel y527-756.6（三面板各 450 宽，底图均 UI_Deck_Information_Back）

### 1) Crafting Panel（GO 362，CraftingPanel 脚本 MB 2397）
| 元素 | 原版 | 项目（修复后） |
|---|---|---|
| 底图 | UI_Deck_Information_Back 450x263.7 | ✓ |
| title（TMP 1772/GO 328） | **'Create a copy of this card' 42px 白** | 新增（此前自创=卡名 26px 金）|
| craftButton（GO 531） | UI_Button_Mulligan，锚(0.2,0.4,0.8,0.6)→270x60.7 @(90,97.9)；Button Text '1' 40px 白 | ✓ 修正（此前 'Craft Copy' +40K_button 已被上轮改对；本轮补 '1' 左对齐）|
| 按钮内 wildcardIcon（GO 235, MB 2427） | 稀有度对应小通配符图标（wildcardSprites[4]） | 新增 48x48 @按钮内(198,6) |
| description（TMP 1830/GO 122） | **'This will consume a wildcard' 40px 白** 锚(0.03,0.12,0.96,0.36)→Godot y[168.8,232.1] | 修正（此前自创 "Craft copy · needs X Wildcard(s)" 18px 行）|
| Info Icon | 40K_generic_bt_info 41.4x41.4 @(446.6,15.5) | ✓ 保留 |
| craftVFXs（4 稀有度粒子） | 制作特效（按钮+卡粒子） | PENDING（无粒子预制体接入）|

### 2) Upgrade Panel（GO 205，UpgradePanel 脚本 MB 2117）
| 元素 | 原版 | 项目（修复后） |
|---|---|---|
| 底图 | UI_Deck_Information_Back 450x261.6 | ✓ |
| content / noUpgradeContent | SetContentGroups(canUpgrade) 切换 | ✓ 实现（_up_content / _up_warning 切换）|
| titleText（TMP 1883/GO 221） | **'Upgrade this card\nto level {0}' 41.4px 白** 锚(0.03,0.6,0.96,0.9)→Godot y[26.2,104.7] | ✓ 修复（此前自创 "Upgrade to level %d" 22px 金）|
| rewardText（TMP 1887/GO 401） | **'Will get: +350' 40px 白** @Explanation(420x64.8 居中@(225,215.8))→(108.6,1.4) | ✓ 新增（此前无）|
| forgeIcon（GO 372 ForgePointIconDrawer） | 40K_general_icon_Forge points 42.7x64.4 @(268.6,0.2)；内含 Converted Drawer('2000' 65px+AlreadyOwned 75px)/Ephemeral Drawer(clock+'24 hours' 65px) 状态抽屉 | 图标 ✓；状态抽屉简化（单机无数据源，报告标注）|
| **upgradeButton（GO 311）** | **UI_Button_Mulligan 270.4x60.3 @(90,83.6)**，文字 40px（JSON 占位 'Change Deck'→运行时本地化 'Upgrade'）| **恢复**（续11 误删，本任务重构）|
| No Upgrade Warning（GO 471） | 'Maximum card tier reached' 40px 白 锚(0.044,0.106,0.956,0.925) | ✓ 新增（此前为 _up_label 局部替代）|
| Info Icon | 40K_generic_bt_info 41.4x41.4 @(446.6,15.5) | ✓ 保留 |
| levelUpAnimationController（MB 2522）+ 相机震动 | 升级动画+震动（Cinemachine impulse, amp 20）| 保留原实现 Octagon 光环（简化，无相机震动）|
| cost（'12342'/数量 '12' 占位） | 原版运行时填真实费用 | 按模拟数据（见四）|

### 3) Alternate Art Panel（GO 358，AlternateArtPanel 脚本 MB 2476）
| 元素 | 原版 | 项目（修复后） |
|---|---|---|
| Background | UI_Deck_Information_Back 450x229.6（面板自带）| ✓（上轮已补）|
| Title（GO 153，TMP 31.7px 白） | **m_text='Upgrade this card\nto level {0}'**（原版素材即此占位拷贝文本，脚本无 title 字段不覆盖 → 原样保留）| ✓ 新增（此前自创 'Swap Style' 20px 金）|
| styleImageContainer（Current Style GO 52） | 406x101.5 锚(0.5,0.5) pos(0,-26.8)→@(22,90.9)，运行时加载异画 | ✓ 修正（此前自创 120x130 缩略图）；单机显示当前卡面 |
| leftButton/rightButton（GO 393/402） | 74.4x75.6 @(10.7,12)/(359.7,12)：UI_Button_Round_background 圆底 + 黄底 56.4x57.7（锚0.114-0.873）+ 40k_general_bt_arrow | ✓ 重构（此前仅圆底单层箭头）；单机禁用（原版 ToggleButtons(false) 同）|
| lockIcon（GO 553=Lock Background） | UI_Deck_Information_Tab 65.8x124.9 @(422.6,48.7) + WF Lock Icon Simple 28.1x42.2 @(445.5,90) | ✓ 修正（此前仅锁图标无 Tab 底）|
| priceDisplayButton（GO 374 Buy Original Card Button） | 328.7x73.4 @(60.7,104.9)，Mulligan 底；PriceDisplay：金币图标 60x60 @(70.5,0) + **'300,00' 54px 白**（欧元逗号格式）| ✓ 修正（此前文字 '300' 无图标）|

### 4) Wildcard Segment / Card Display（已复核，无改动）
- 4 稀有度计数 Common x10/Rare **x85**/Epic x160/Legendary x235（rel Counters @1555，pitch 75），图标 30x44 + 数字 32.6px 白，'999' 占位；BG 40k_topmarquee_currency_display BW 灰 (0.46)；Army Icon 80 宽 @1470。**Rare 确认存在**（`Rare_315.json`）/ 补树漏。
- 升级入口覆盖层 "Card Ready for level up"（BasicCardUI.cardUpgradeHighlight=GO 444）→ 项目 ReadyForLevelUp 覆盖层已按 `_tier<4 && _duplicates>0`。
- 原版根脚本 CardDisplayWindow：无 craft/upgrade 按钮字段（在 CardDisplayOptions→三面板脚本里），voiceOverButton/showCardTextButton/lore/tutorial 等已实现。

## 四、实现差异清单（本轮改动 card_displayer.gd）

1. **消除自创元素**：Craft 标题卡名/meta 行/WildcardCost 行 → 原版 title+description；Upgrade 自创 _up_label/_up_detail → 原版 titleText+rewardText+按钮；Alt 'Swap Style'/'Current style: ...'/120x130 缩略图 → 原版 Title+Current Style 406x101.5；Buy '300' → '300,00'+金币图标；锁图标 → Tab 底+图标；箭头 → 圆底+黄底+箭头三层。
2. **恢复 Upgrade 按钮**（原版权威几何/贴图/字号），`_on_upgrade` 接线：
   - 数据模拟（单机无服务器）：**升级 = 2000 金币 + 1 对应稀有度通配符 → tier+1（MAX_TIER=4，原版 CardTier 枚举 Tier1..4）**；不足则 flash 提示。
   - 满级 → No Upgrade Warning 层（'Maximum card tier reached' 40px）替代 content（原版 SetContentGroups）。
3. 提示语全部按 m_text（如 'Will get: +350'/'Create a copy of this card'/'300,00'），颜色按 m_fontColor 白（此前金色系为自创）。
4. 常量清理：TEX_BTN/TEX_YELLOW（自创按钮残留）→ TEX_MULLIGAN 共用 + 新增 TEX_ARROW/TEX_YELLOW_BTN/TEX_FORGE/TEX_TAB_BG/TEX_GOLD；MAX_TIER=4；UPGRADE_GOLD=2000。

**未如实数据（报告标注）**：原版升级消耗/奖励为服务器数据（'12342'/'2000'/'+350'/'12' 为占位+典型值）——本实现按 '2000' 金币 + 1 通配符模拟；奖励"+350"为原版占位文本原样显示；异画列表单机无数据 → Current Style 显示当前卡面 + 'No alternate art in offline build' 提示（用户指定）。

## 五、验证输出

1. `--check-only --script`：唯一报错为已知 SFX autoload 误报（任务约定忽略）。
2. **headless 实例化测试** `tools_dev/test_cd_panels.tscn`（新增，参考 test_popups 模式）→ **PASS**：
   - OptionPanel (1294,146) 450x757 ✓；Craft 标题/说明/'1'/通配符图标 ✓；Upgrade 标题 level 2/'Will get: +350'/按钮 'Upgrade' ✓；满级切换 warning 显/content 隐 ✓；Alt 标题/CurrentStyle/箭头x2+Buy/lock Tab 底/'300,00' ✓；升级点击流 tier 1→2、金-2000、通配符-1 ✓；无 SCRIPT ERROR。
3. `auto_test` headless（真实路径主菜单→图鉴 300 帧）→ 0 SCRIPT ERROR。

## 六、PENDING

1. CraftingPanel.craftVFXs（4 稀有度制作粒子：ParticleButton 217/216/213/218 + ParticleCard 215/211/212/214）——需从 06_特效_预制体/08_预制体特效 找对应粒子预制体后接入（本次未做，占位无）。
2. UpgradePanel 状态抽屉（Converted '2000' + AlreadyOwned/'Ephemeral 24 hours'）—— 单机无服务器升级类型数据，保留 Forge 图标+奖励行，抽屉未做。
3. ForgePointIconDrawer 真实按钮文本（原版运行时本地化 'Upgrade'，JSON 'Change Deck' 为占位）——已用 'Upgrade'，如后续接入 i18n 再替换。
4. 相机震动/升级动画完整版（原版 Cinemachine impulse amp 20 / levelUpEffect1/2）——保留现有 Octagon 光环简化版。
5. Alt Art 标题 '{0}' 占位（原版素材即如此）——保持原样，待原版截图/权威确认是否运行时隐藏（脚本无 title 字段，倾向原样）。
6. 验证工具 test_cd_panels.gd/.tscn 已留 tools_dev（可复用，同 test_popups 惯例）。
