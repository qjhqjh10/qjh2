# 文案回填分析报告 CB — Gacha / Forge / Tutorial

> 分析日期: 2026-08-23 | 分析代理: 文案子代理 CB | 只读分析（未改任何文件）
> 方法: audit_E_{gacha,forge,tutorial}.md 规格树 txt= 元素 → 原始 Unity JSON（d:/2/解包整理/03_界面UI/菜单/ GameObjects+MonoBehaviour，dump_go_tree.py 全树）取完整 m_text → 与 d:/warpforge/scripts/{gacha,forge,tutorial}.gd 逐项对比
> 权威依据: 原始 Unity JSON m_text（说明书摘要/audit 表 txt= 仅预览，截断处以原始 JSON 为准）

---

## 一、Gacha（The Vault 宝库）— d:/warpforge/scripts/gacha.gd

规格树 63 元素，文本元素 12 个。**需替换 4，保留 8**。

### 替换清单

| 界面 | 元素 | 项目文件:行 | 项目当前字符串 | 原文完整m_text（原始JSON） | 动作 |
|---|---|---|---|---|---|
| Gacha | Generic Simplified UI Button(1) > Button Text | gacha.gd:232 | `"Card Sources"` | `Where get cards`（MonoBehaviour_7113569655039036191.json，55px） | **替换**：按钮文字改 `"Where get cards"`（注意原版无 "to"、无 "Cards" 大写 C 二词差异——原文就是 'Where get cards' 三词） |
| Gacha | Gacha Reward Claimed > Claimed Tex（已集齐飘带） | gacha.gd:438 | `"Collected"` | `Claimed`（Claimed Tex，40.55px；gacha 抽屉 41.95px） | **替换**：`"Collected"` → `"Claimed"`（飘带通常印在 40k_OfferBadge 上，文字层按原文） |
| Gacha | Player doesn't have all items > Footer Text（保底说明） | gacha.gd:307 | `"You'll receive at least one Special Item after 10 opens"` | `You’ll receive at least one Special Item after <color=#E0DC2DFF>10</color> crates.`（MonoBehaviour_6185239214392530561.json，38px） | **替换**（两处注意）：① 撇号是 U+2019 `’` 不是 ASCII `'`；② 数字 10 带 TMP rich text 金色标签 `<color=#E0DC2DFF>` — Godot Label 需 `bbcode_enabled = true` 才渲染 `<color>`；或剥离标签为纯文本 `You’ll receive at least one Special Item after 10 crates.`（文字仍为原文案）。词尾是 "crates." 不是 "opens" |
| Gacha | Completed > Complete Tex Info | gacha.gd:368 | `"You collected all Special Items - you can keep opening for rewards;\na new round starts with the next event"`（自创合并文案） | `You have collected all the available Special Items`（Complete Tex Info，53.2px，MonoBehaviour_490919429230679681.json） | **替换**：整段换为原文；对应字号约 53（项目现在 22）。原版另有一条 footer 文案在 "Player has all items"（隐藏态 Footer Text，56px）：`You've collected all the Special Items, but you can keep opening crates to earn even more rewards.`（MonoBehaviour_5091751188706154113.json）——若复刻原版"集齐后 footer 文案切换"设计，可把"keep opening"信息放 footer 而非 Complete 层 |

### 保留（已与原文一致）

| 界面 | 元素 | 项目文件:行 | 项目字符串 | 原文 m_text | 动作 |
|---|---|---|---|---|---|
| Gacha | Header > Title | gacha.gd:203 | `"The Vault"` | `The Vault`（90px） | 保留 |
| Gacha | Time Remaining | gacha.gd:213, 285 | `"Ends in:"` | `Ends in:`（40px） | 保留 |
| Gacha | Time | gacha.gd:214, 286 | `"19d 15h"` | `19d 15h`（40px） | 保留（运行期动态由服务器下发，格式照抄） |
| Gacha | Price Display > text | gacha.gd:219 | `"1"` | `1`（62.77px） | 保留 |
| Gacha | Rewards Panel > Header Title | gacha.gd:276 | `"Special Items"` | `Special Items`（90px） | 保留 |
| Gacha | Footer > Reward count | gacha.gd:563 | `"%d/%d"` → `0/5` | `2/5`（56px） | 保留（动态格式一致；原版 2/5=已集齐 2 / 共 5） |
| Gacha | ProgressBar > counter | gacha.gd:580 | `"%d/%d"` → `0/10` | `5/10`（49.8px） | 保留（动态格式一致） |
| Gacha | Completed > Complete Text Title | gacha.gd:357 | `"Complete!"` | `Complete!`（131.9px） | 保留 |

### 标注疑点 / 无原文（数据驱动，原版菜单无 m_text 可比对）

- **物品池名称/数量**（gacha.gd:41-47 ITEMS）：原版 Gacha Drawer Holder 的 Name/Quantity 为运行期设置，菜单 JSON 无 m_text；可查证原文仅 `Legendary Wildcard`（75px，Forge 奖励 Name 元素用词一致）→ 项目 `"Legendary Wildcard"` 用词吻合，其余 `Epic Wildcard/Rare Wildcard/Gold/Pack` 无菜单原文，**保留**并待数据源核实。
- **数量行**（gacha.gd:418 `"× %d"`）：无原文（原版 Quantity 元素样例为 `2` 纯数字 75px，如 Forge Points Drawer）→ 标注疑点：原版数量无 `×` 前缀、字号约 75；建议改纯数字。
- **自创运行时文案（原版无对应，保留待议）**：gacha.gd:460 `"Not enough Tickets - come back tomorrow (+1 per day)"`、:502 `"Pity Rewards: Legendary Wildcard x1"`、:515 `"Reward: %s x%d"`、:562 `"Ticket %d"`（右上门票条为项目自加 UI，原版 Gacha Tab 无此顶部货币条）。
- 打开弹窗按钮 `_open_where_cards()` 引用的 where_cards_popup.gd:59 标题 `"Where to get cards"` 与按钮原文 `Where get cards` 不同——弹窗应为独立界面（不在本次 3 界面范围），仅提示。

---

## 二、Forge（熔炉）— d:/warpforge/scripts/forge.gd

规格树 53 元素，文本元素 10 个 + 奖励行内文本（Forge Menu Reward Button）。**需替换 3，保留 5，缺失补建 2，标注疑点 3**。

### 替换 / 格式修正清单

| 界面 | 元素 | 项目文件:行 | 项目当前字符串 | 原文完整m_text | 动作 |
|---|---|---|---|---|---|
| Forge | Selected Army Info > TotalXp Points | forge.gd:426 | `"%d / %d" % [pts, req]` → `0 / 0` | `154748`（TotalXp Points，32.7px，纯总 XP 数字；奖励行 PointsLabel 样例 `20505/1546778` 33.7px 亦无空格） | **替换（格式）**：原版为**单一累计总数**（无 "/"）且**无空格**。建议：`_points_label.text = "%d" % total`（累计点数）；若保留 "当前/需求" 语义则至少去空格 `"%d/%d"`（与 PointsLabel 无空格格式一致）。原版 32.7px（项目 33） |
| Forge | 奖励行 > 等级徽章 | forge.gd:316 | `"Lv.%d"` → `Lv.5` | LevelLabel `99`（45px，纯数字） | **替换（格式）**：原版只显示纯数字等级，无 "Lv." 前缀；建议 `"%d" % (offset+1)` |
| Forge | 奖励行 > 奖励名 | forge.gd:481-487 | `"Common Wildcard ×5"` / `"Gold ×200"` / `"Rare Wildcard ×2"` / `"Epic Wildcard ×1"` | 原版为**两个独立元素**：Name `Legendary Wildcard`（75px，Forge Menu Reward Button RewardTransform 内）+ Quantity `2`（75px，Forge Points Drawer） | **替换（结构）**：名称与数量分开显示——名称纯名（无 `×`），数量单独元素纯数字；`"Legendary Wildcard"` 用词有原文可证（75px） |

### 缺失（原版存在，项目完全没有）

| 界面 | 元素 | 项目文件:行 | 原文完整m_text | 动作 |
|---|---|---|---|---|
| Forge | Debug Add points > Text (TMP) | forge.gd:（无，audit ⚠️未命中） | `Debug add points`（24px） | **缺失**：原版 GO active 存在（Button 40K_button 玫红底）。项目无任何调试 UI。若复刻原版调试功能按原文案补建；不做调试则标注缺失可忽略 |
| Forge | Debug Add points > InputField > Placeholder / Text | 同上 | `Enter text...`（51.4px）/ `5`（51.4px，原文含 U+200B 零宽空格 `5\u200b`——编辑器痕迹，回填用纯 `5`） | **缺失**同上。注意原版默认值即 `5`，Placeholder 与可见 Text 双元素 |
| Forge | Debug Set Forge > Text (TMP) | 同上 | `Set Forge Level`（24px） | **缺失**同上 |
| Forge | Debug Set Forge > InputField > Placeholder / Text | 同上 | `Enter text...` / `5\u200b` | **缺失**同上 |

> 备注：原版 **Forge Tab 根节点本身 [inactive]**（Debug 子元素 active 但在整体禁用的 Tab 内），项目 forge.gd 以 rewards.gd 内嵌方式使用——调试元素按复刻准则可不入成品，是否补建由实现方定。

### 保留（已与原文一致）

| 界面 | 元素 | 项目文件:行 | 项目字符串 | 原文 m_text | 动作 |
|---|---|---|---|---|---|
| Forge | ArmyText | forge.gd:179, 424 | `_capitalize_first(_cur_army)` → `Ultramarines` | `Ultramarines`（41.3px） | 保留（Title Case 一致） |
| Forge | LevelText | forge.gd:180, 425 | `"Level %d/%d"` → `Level 1/50` | `Level 1/50`（32.38px） | 保留 |
| Forge | 奖励行 > Claim 按钮 | forge.gd:395, 468 | `"Claim"` | `Claim`（36.8px，Forge Menu Reward Button Button Text） | 保留 |
| Forge | 奖励行 > 已领取态 | forge.gd:463 | `"Claimed"` | `Claimed`（72px，Forge Points Drawer Collected Badge Text (TMP)） | 保留（原版"已领取"徽章亦用词 `Claimed`）；原版另有 Converted Drawer `Already Owned`（75px）属点数兑换抽屉 | 
| Forge | 奖励行 > 进度数字 | forge.gd:458 | `"%d/%d"` → `0/100` | `20505/1546778`（PointsLabel，33.7px，无空格） | 保留（无空格格式一致） |

### 标注疑点

- **Locked 态**（forge.gd:473 `"Locked"`）：全菜单 m_text 检索无 `Locked` 原文 → 原版可能无锁定态按钮文案（未解锁行或不显示按钮）。**保留/待原版数据核**。
- **阵营显示名**：factions.json 键为紧凑名（SaimHann/TauEmpire/BlackLegion/…），原版 ArmyText 为带空格显示名（样例 `Ultramarines`；推测 `Black Legion`/`Tau Empire`/`Astra Militarum` 等）。项目显示紧凑键 → 建议加 display 名映射（不为文案回填，属数据命名）。
- **自创 toast**（forge.gd:514 `"Claimed Lv.%d Rewards: %s"`）：原版无对应 → 保留/标注。

---

## 三、Tutorial（教程模式）— d:/warpforge/scripts/tutorial.gd

规格树 21 元素。**需替换 3，保留 5，无原文待定（STAGES 2-6）**。

### 替换清单

| 界面 | 元素 | 项目文件:行 | 项目当前字符串 | 原文完整m_text | 动作 |
|---|---|---|---|---|---|
| Tutorial | TutorialDescription（第 1 关描述） | tutorial.gd:15 | `"Start learning! Train with your Captain. Deploy units, attack enemies, win battles."`（自创） | `Start here! Spar with your Chapter Master to learn the teachings of the Codex before heading out into battle.`（MonoBehaviour_2909133765077550966.json，40px，autosize 10-40） | **替换**（任务记载"第 1 关文案自创"→ 用回原文） |
| Tutorial | TutorialWarlordTitle | tutorial.gd:106, 197 | `"Warlord: %s" % STAGES[i]["warlord"]` → `Warlord: Uriel Ventris` | `Warlord: <color=orange>Uriel Ventris</color>`（TutorialWarlordTitle，54.3px，TMP rich text） | **替换（格式）**：原文含 `<color=orange>` 内联标记（名字橙色）。Godot 用 bbcode：`bbcode_enabled=true` + `Warlord: [color=orange]Uriel Ventris[/color]`；或剥离标记按项目现有全局色（e8c76a 近似 orange）→ 标注疑点 |
| Tutorial | Army Selector > 关卡选择按钮文字 | tutorial.gd:131 | `("✓ " if done else "") + "Stage %d  %s" % [i + 1, STAGES[i]["sub"]]` → `Stage 1  The Basics` | 原版选择按钮（Tutorial Army Select Button）两个文本元素：TutorialTitle `Tutorial 1`（36px）+ TutorialSubTitle `The Basics`（36px）+ 完成态 TutorialComplete `Complete!`（36px） | **替换（格式）**：按钮主文本改 `"Tutorial %d"`（原版 'Tutorial 1' 格式，无 "Stage"）；副标题独立行；完成态徽章用 `Complete!`（原版有 "✓ " 类勾选？原样为 TutorialComplete 覆盖层 'Complete!') |

### 保留（已与原文一致）

| 界面 | 元素 | 项目文件:行 | 项目字符串 | 原文 m_text | 动作 |
|---|---|---|---|---|---|
| Tutorial | Window Title | tutorial.gd:64 | `"Game mode"` | `Game mode`（67.55px） | 保留 |
| Tutorial | PlayTutorialButton > Button Text | tutorial.gd:174 | `"Play Tutorial"` | `Play Tutorial`（74.25px） | 保留 |
| Tutorial | TutorialTitle（第 1 关） | tutorial.gd:15 | `"TUTORIAL 01"` | `TUTORIAL 01`（74.25px） | 保留 |
| Tutorial | TutorialSubTitle（第 1 关） | tutorial.gd:15 | `"The Basics"` | `The Basics`（54.3px） | 保留 |
| Tutorial | Completed Text | tutorial.gd:120 | `"Completed: %d/6"` | `Completed: 1/6`（54px） | 保留（动态格式一致） |

### 标注疑点：STAGES 2-6（原包无 2-6 关菜单原文，且项目内容与原版事实不符）

全解包检索（03_界面UI 全部 m_text）：Tutorial 相关仅 4 条——`Play Tutorial` / `Reset tutorial`（设置页）/ `TUTORIAL 01` / `Tutorial 1`。**原包未解出第 2-6 关的关名/副题/描述 m_text**（原版应为服务端/运行时数据填充，客户端只带第 1 关实例）。

但按原始 Warpforge_TutorialStage{1-6}.json（09_游戏数据/教程/）的事实核查，**项目 STAGES 2-6 的子题/关主与原版不符**：

| 关 | 原版内容（TurnScriptedData 证据） | 玩家方 Warlord（Chat 发言者） | 项目当前 | 建议 |
|---|---|---|---|---|
| 1 | UM vs Orks，战术基础（攻击/远程/部署） | **Uriel Ventris**（Ventris1 等 PlayerChat） | TUTORIAL 01 / The Basics / Uriel Ventris ✓ | 关1 回填原文（见上） |
| 2 | Orks 教程（Makari 光环、Tide/Mob/Vanguard 特性、Stratagem） | **Ghazghkull**（Ghazghkull1-2 PlayerChat，Radio 为 Makari） | "Card Mechanics" / Uriel Ventris ✗ | Warlord 应为 Ghazghkull Thraka；"Card Mechanics" 为自创子题，无原文可回填 → 标注：子题保留自创英文或待游戏数据（各关仅首条 SmallTip 可概括，如 Stage2 首条 "Most units have special abilities. Makari gives adjacent units a Melee Attack bonus."） |
| 3 | Necron 教程（Remnant 特性） | **Zahndrekh**（Zahndrekh1-4 PlayerChat，Orikan AiChat） | "Combat" / Uriel Ventris ✗ | 同上 |
| 4 | Chaos/帝国？（Sylar vs Varro） | **Sylar**（Sylar1-6 PlayerChat，Varro AiChat） | "Tactics" / Uriel Ventris ✗ | 同上 |
| 5 | Aeldari 教程（Shuriken 特性，Craftworld） | **Ghaelyn**（Ghaelyn1-3 PlayerChat，Imotekh AiChat） | "Warlords" / Uriel Ventris ✗ | 同上 |
| 6 | Tyranid 教程 | **Tervigon**（Tervigon PlayerChat，Uriel AiChat） | "Victory" / Uriel Ventris ✗ | 同上 |

> 结论：STAGES 2-6 的 "warlord: Uriel Ventris" 全部与原文不符（原版 6 关 = 阵营引导链：UM→Orks→Necrons→Sylar→Aeldari→Tyranid），属**数据事实错误**；关名格式建议与第 1 关一致 `TUTORIAL 0N`；子题/描述无原文可回填（原包缺失）——保持现英文或后续从各关 SmallTip 内容提炼（需用户裁决，不属"回填"）。

### 相关观察（不在替换范围）

- **局内引导提示**（battle.gd:2261 读 res://data/tutorial_stages.json）：Stage1 提示已镜像原版 SmallTip（`<br>`→`\n`）；但原版 `<link=...><nobr><sprite name=Atlas_trait_icon_xxx><b>特性</b></nobr></link>` 富文本在项目数据中被剥离（如 Stage2 Tide/Mob/Vanguard、Stage3 Remnant、Stage5 Shuriken 的内联特性图标/链接），文字在但**特性图标标记丢失** → 标注：如需还原图标需保留 link/sprite 标记并在 Godot 侧实现。
- 原版 Tutorial Mode Menu 有**两套变体**：主面板大字版（TUTORIAL 01 74.25 / The Basics 54.3 / Warlord 54.3 / desc 40 = 本次规格树）与栏目按钮小字版（Tutorial 1 / The Basics / Complete! 均 36px = Tutorial Army Select Button）——项目已把"6 关列表"自制成按钮列表，文本格式按小字版回填。

---

## 四、汇总

| 界面 | 文本元素 | 需替换 | 保留 | 缺失/疑点 |
|---|---|---|---|---|
| Gacha | 12 | 4 | 8 | 物品名/数量/自创 toast 4 处无原文 |
| Forge | 10 + 行内 | 3（格式） | 5 | Debug 双按钮×2 文本缺失（原版 active 原样 5 条 m_text 已录）、Locked/阵营显示名无原文 |
| Tutorial | 9 | 3 | 5 | STAGES 2-6 子题/描述无原文 + Warlord 6 关中 5 关与原文事实不符 |

**特殊发现**：
1. Gacha 保底 footer 原文撇号是 **U+2019**（`You’ll`），且含 TMP 金色 `<color=#E0DC2DFF>10</color>` 内联标签。
2. Forge Debug 输入框原文默认值 `5` 尾随 **U+200B 零宽空格**（拆包痕迹，回填剔掉）。
3. 原版 Gacha "Where get cards" 按钮字号 55px、Header 时间字号 40px、Complete info 53.2px——项目当前 22/20/22px，文字回填时字号可不改（另一批），但回填后建议顺带校准。
4. Tutorial 主面板 Warlord 行原文带 `<color=orange>` 标记 → 项目用整行 e8c76a，等价效果但非原文串。
5. 原版 Tutorial 6 关 = 阵营引导（UM/Orks/Necrons/Sylar/Aeldari/Tyranid），非项目自创的"Card Mechanics/Combat/Tactics"主题式关卡；Stage1 卡组即 Ultramarines（playerDeck pid 7422324008993234997）。
