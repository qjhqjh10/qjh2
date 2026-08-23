# UI 问题清单（说明书对照核查，2026-08-19 建立）

> 依据：复刻一致性准则（用户 2026-08-18）——任何界面元素（按钮/图标/容器/纹理/文字）必须与解包说明书（菜单全树.md / 卡组界面说明书.md / 原始 Unity JSON）一致。
> 状态：✅ 已修复 | ⬜ 待修 | ❌ 不做（有依据）
> 核查范围：先收藏/卡组（用户指定重点），其余界面滚动核查。

---

## 十八、战斗画面复刻差距（2026-08-21 用户 F5 实测否定："现在的战斗不是原版，画面复刻也不行"，新会话 P0 待办）

> 依据：07_场景/battlearena1 原始 Unity JSON（GO 1224 个）。用户逐项质疑 + 定位结论见任务文件续32h 交接。

| # | 差距（项目 vs 原版说明书） | 状态 |
|---|---|---|
| T1 | **3D 战场**：原版=烘焙场景 Mesh（Scenario Battle Arena 1 Baked 地板/建筑/背景一体）+ Barrel/Bridge/Cannon/Fences 等场景物；项目=贴图平面近似（floor.png 立幕 30.34×7.46 + 天空 pano + 40×40 地面 + OBJ 装饰） | ⬜ 新会话评估还原 |
| T2 | **相机**：原版 BoardCamera (100,2.22,-13.57) FOV 46.4 **无旋转**（Transform_1318 权威，父链 1301/1300 均无旋转；场景根 -90°X 补偿），项目 rotY180 近似 | ⬜ 对照验证 |
| T3 | **3D 卡牌 = 2DCard 组合**：原版 卡框 CardFrame+卡图 CardImage+血/甲/攻/费统计+关键词+Card Highlight And Shadow（battlearena1 2DCard 结构）；项目仅 PlaneMesh 卡面贴图立牌（"部分卡牌就是一个贴图"） | ⬜ 新会话按 2DCard 组合实现 |
| T4 | **HUD 全对照**：TurnBtn/能量框(302×481@1622)/骷髅(161,929)/坟场/换牌/攻击选择器/手牌数条 等位置文字 active 逐项复核；文字溢出需用户整屏截图 | ⬜ 新会话 |
| T5 | **ReplayButtons**：原版屏外（LeftArea 相对 [-550,1117 294x57]，观战模式滑入），项目此前误放屏内 (410,37) | ✅ 2026-08-21 已修（移屏外） |
| T6 | **SceneTransition 遮罩 bug**（战场黑+无法出牌/进攻/拖拽总根因）：淡入遮罩永不释放+叠第二遮罩 | ✅ 2026-08-21 已修（复用遮罩淡出；主流程截图暗占比 93.8%→11.3%） |
| T7 | **督军天赋**：机制已实现（desc "Talent: X"→回合开始生成天赋卡，84 张带 Talent，rule_test 过）；用户"天赋没效果"待提供督军名排查 | ⬜ 待用户信息 |
| T8 | **防御卡入口**：续32f 已实现（防御槽点击弹选择器/拖防御卡入槽，test_deck_builder2 过）；用户实测"还是不能加入"——**模板卡组无防御卡数据，需自组卡组验证** | ⬜ 待用户复验 |
| T9 | **验证工具**：shot_battle_flow.gd（完整主流程截图，须设 current_scene）/test_scene_transition.gd（遮罩断言）——--script 直接加载场景会绕过 change_scene 无法发现过渡 bug（坑 34 教训） | ✅ 已建 |

---

## 十七、deck_builder 第二轮审查修复（2026-08-21，用户实测反馈：排版混乱/相互重叠/防御卡无法放入/无法拖动/卡牌展示形式）

> 依据：原始 Unity JSON 权威（m_IsActive 逐文件核实，**推翻 dump "active" 标记**——见使用地图坑 33）。专项测试 test_deck_builder2 31 项全过 + e2e/auto_test/popups 回归绿。

| # | 问题（用户反馈 → 根因） | 修复 |
|---|---|---|
| K1 | **左边卡组卡片列表被重叠** → 费用曲线抽屉常显（dump 误标 active，原始 JSON m_IsActive=false）覆盖卡行区 | ✅ 默认隐藏，Deck info 视图切换显示（原版 DeckEditingStateController 语义） |
| K2 | **排版混乱** → Troops/Stratagems 抽屉常显 + 'Edit your deck' 标题 + Instructions 常显（均 m_IsActive=false） | ✅ 全部移除/隐藏（标题/提示删除；抽屉绝对定位+默认隐藏） |
| K3 | **无法放入防御卡（后手补偿）** → 防御槽被 disabled 锁死 | ✅ 功能槽：点击弹选择器（当前阵营 rarity=defence 卡）/ 拖防御卡入槽 / 空槽虚线底 '-- Defensive --' / 有卡显示费用+名+x1 / 保存加载 defensive 字段 / deck_info_popup 列表补防御卡行 |
| K4 | **无法拖动卡片** → 无拖拽实现（原版 CardDraggingController） | ✅ 池卡 _get_drag_data（卡面预览+拖拽音效）→ 卡组列表/防御槽 _can_drop_data/_drop_data（防御槽只收 defence 卡）；点击加卡保留（原版 CardCollider 点击+拖拽并存） |
| K5 | **卡牌展示形式有问题** → 自绘 250x405 方块（卡图裁剪+金框+名字条） | ✅ 改原版 Collection Card prefab 形式：完整 PnP 卡面 397.45x576 居中铺格 + Counter 'xN/M' 角标 + 达上限灰显 + DEFENSIVE 角标 |
| K6 | 区域划分重叠 → 卡池网格 3 列右空 400px | ✅ 原版 _segments 4 间距 0 → 4 列铺满 1590 视口 |
| K7 | 卡行费用数字 38px vs 原版 50px | ✅ 50px |
| K8 | Header 缺 Filler 黑块（x[-202,241] y[71,156] 纯黑盖导航带） | ✅ 补（Back 按钮之下） |
| K9 | 'Filters' 字号 42 vs 原版 40 | ✅ 40 |
| K10 | 空卡组提示 'Click a card to add it' 常显（原版 Empty Warning m_IsActive=false） | ✅ 移除；卡池空态警告（筛选无结果时）按原版文案 |

**战斗侧配套（同轮）**：① **能量修正**——规则书 "Each player's Energy starts at 1 and increases by 1 every turn" → 经典第 N 回合 = N+1（第一回合 2，用户新指示；推翻 8.21 早前"首回合 1 能"记录），Skirmish 1+2N + 后手 +1；rule_test 273/0 ② **先手随机**（"Roll off or flip a coin to decide who plays first"）→ 换牌界面 "You go second" 仅后手显示（此前常显）③ **后手防御卡入手**（"Player acting second starts with their Defence card"）+ AI 先行动（_run_ai_first_turn 提取复用）④ test_battle_defence 新建全过 ⑤ 战场"黑色"核查：当前构建 3D 战场渲染正常（shot_battle2 整屏 + PIL 像素验证），反馈为旧版遗留。

---

## 十六、3D/2D 使用核查（2026-08-20 用户指定新增，新会话最高优先待办）

> 任务：检查项目 3D/2D 使用是否符合说明文件、是否复刻原版。原版是 3D 的地方项目是否 3D，原版是 2D 的地方是否 2D。

| # | 界面/元素 | 原版形式（JSON 依据） | 项目现状 | 判定/待核 |
|---|---|---|---|---|
| D1 | 手牌卡 | 3D 世界空间 2DCard（Cards←Card Display←相机投影；HandArea scale 108；BoxCollider2D 碰撞） | 2D UI Button（95×150 弧形） | ⬜ 待定是否 3D 化 |
| D2 | 场上单位 | 3D 世界卡牌立牌（MinionArea 槽位世界坐标 x=-9..9 z=-7.255/0.443） | 3D PlaneMesh 卡牌 ✓ | ✅ |
| D3 | 战场背景 | 3D（Floor plane/Background 世界 Transform+相机 FOV 46.4） | 3D ✓ | ✅ |
| D4 | 攻击/召唤特效 | 3D 世界粒子（battlearena1 ParticleSystem+08_预制体 3D） | 2D HUD 层 GPUParticles2D（_slot_center 投影定位） | ⬜ 待核（效果位置=屏幕投影≈世界位置，观感是否一致） |
| D5 | 手牌数条/敌方手牌区 | 3D 世界空间 TMP（CardsInHandText scale 108 投影） | 2D Label | ⬜ 低 |
| D6 | 能量/回合 HUD | 2D UI ✓ | 2D ✓ | ✅ |
| D7 | 主菜单背景视频 | 2D（Background Render Texture Holder） | 2D SubViewport ✓ | ✅ |
| D8 | 卡组/收藏/商店界面 | 2D UI ✓ | 2D ✓ | ✅ |
| D9 | 阵营环境装饰 | 3D 模型+粒子（06_模型/场景 ParticleSystem） | 3D OBJ+GPUParticles3D ✓ | ✅ |
| D10 | 开包动画 | 2D UI 动画（Booster Pack Open Window） | 2D ✓ | ✅ |

**核查方法**：07_场景/battlearena1 相机/Transform 逐项对照；输出差异表+修复建议；修复前与用户确认范围。

---

## 十五、三项自检 + A/B/C 修复（2026-08-20，用户"战斗是否与原版一致/修改是否按 JSON/走一遍卡组流程"）

### 战斗 JSON 对照（battlearena1 原始 JSON 代理换算 + 亲自验证）

| # | 元素 | JSON 事实 | 项目 | 判定 |
|---|---|---|---|---|
| S1 | 手牌区 y | PlayerCardAreaSizeHelper To Use y[830.1,1080] | y830 | ✅ |
| S2 | 手牌弧形 | CardsHorizontalLayout 间距1.45×宽/弧高0.7×高/12卡/verticalOffset-330/useRotation/z序 | 全套 | ✅ |
| S3 | END TURN | TurnBtn x[1716,1846.7] y[415.3,495.8] 130.7×80.4 | (1716,415) 131×80 | ✅ 完全吻合 |
| S4 | 牌库文字 | fontSize=42 @x[1599.5,1819] 中心y800 | 30px→**42px** @y775 | ✅ 已修 |
| S5 | Mulligan 副标题 | fontSize=55 y[129.4,183.6] | 22px→**55px** @(295,129) | ✅ 已修 |
| S6 | Mulligan 标题区 | y[66.8,146.2] 高79.4 | 高50→**79** | ✅ 已修 |
| S7 | 攻击选择器钮 | 三钮 x[590,708.3] y[541.7,660.5] 118.37×118.81；m_Spacing=37 | (590,542) 118×119；37px | ✅ 完全吻合 |
| S8 | 准星三色 | melee(0.953,0.082,0.004)/ranged(0.827,0.306,0.922)/skill金(0.914,0.776,0.204) | ATK_COLORS 同值 | ✅ |
| S9 | 骷髅 | MatchSkulls Icon (160.7,929.5) 65.4×54.1；'xN' 35px @(225.4,936.1) | (161,929) 65×54；35px | ✅ 完全吻合 |
| S10 | Mulligan Continue | x[1062.9,1895.8] y[921.5,1039] 833×117.5 | (1063,922) 833×117 | ✅ 完全吻合 |
| S11 | HideMulliganButton | (101.5,908.5) 83×79.6 | (102,908) 83×80 | ✅ |
| S12 | Cemetery | x[-1200,-405.9] y[223.9,877.7] 794×653.8 | (-1200,224) 794×654 | ✅ 完全吻合 |
| S13 | 出牌交互 | CardCollider 同时实现 IPointerClickHandler+IDragHandler（反编译） | 拖拽+点击并存 | ✅ 架构一致 |
| S14 | 能量框 | RT3342 302.08×480.82（GO 名 Background，尺寸=代码 302×481） | (1622,186) | ⚠️ 尺寸吻合；位置双算法（8.13 x[1621.7,1923.8] vs 锚点公式 x[1778,2081]）待复核 |
| S15 | 手牌绝对尺寸 | 2DCard 比例 0.628（有）；95×150 无直接 JSON | 95×150 | ⚠️ 比例有据，绝对尺寸估算 |

### 卡组组建流程断点（走查+交叉验证）

| # | 断点 | 修复 | 状态 |
|---|---|---|---|
| F1 | PLAY 导航直连 battle 跳过选卡组 | PLAY→mode_select（原版语义） | ✅ |
| F2 | 主菜单无卡组入口+孤儿函数 | _on_practice 接 PLAY；孤儿全删 | ✅ |
| F3 | 卡组仅 1 槽（Unlock 占位） | **DeckStore 多卡组**（decks.json 列表/迁移/双写/3 槽→Debug Unlock 12 槽） | ✅ |
| F4 | 导入/删除后网格不刷新 | parent meta 回调 _refresh_grid | ✅ |
| F5 | Select Deck ≡ Practice Deck | Select=仅选中，Practice=开战 | ✅ |
| F6 | Duplicate 只 Toast | 实际复制（净化字段+Copy 后缀） | ✅ |
| F7 | Done=保存+立即开战 | Done=保存+返回列表 | ✅ |
| F8 | 死代码（阵营弹窗/门帘/详情面板/孤儿） | 全部删除 | ✅ |

---

## 十四、战斗"找不同"审计修复（2026-08-20 凌晨，用户"找不同不是找相同"）

> 4 代理对照 battlearena1/03_界面UI 原始 JSON + 自核；详见 项目任务文件.md 8.13。

| # | 问题（项目 vs 原版 JSON） | 修复 |
|---|---|---|
| Z1 | **棋盘 9 格 vs 原版每侧 4 位（3 小兵+督军）**（MinionArea slotsPerSide=4，x=-9/-6/-3/0/+3/+6/+9） | ✅ BOARD_SIZE 9→7 / WARLORD_SLOT 4→3；rule_test 槽位引用同步 |
| Z2 | **3D 卡牌从不上场**（2D 格投影到地板：格中心在屏幕中线以上+相机水平→射线向上永远打不到地板，返回 ZERO） | ✅ 3D 卡站原版坐标（玩家行 z=-7.255/敌方 0.443、督军 -7.12/0.22）；卡面朝相机；PnP 卡面优先 |
| Z3 | **拖拽出牌整条失效**（set_drag_forwarding get-data 回调只传 1 参，lambda 声明 2 参→运行时错误）——"手牌无法打出"根因 | ✅ 改 1 参捕获按钮 |
| Z4 | **无拖拽攻击**（原版 Drag Attack Selector：拖动单位→选择器→目标；3 钮 37px 间距 HorizontalLayoutGroup + Attack Target Reticle 准星拖线 红/紫/金） | ✅ 实现拖拽攻击（选择器跟随/准星自绘十字/拖线/释放命中攻击；点击流程保留兜底）；ActiveSkill 走 activate_alt |
| Z5 | **自创阵营选择弹窗+开场门帘动画**（原版 battlearena1 无 army selector；BattleDoors 实为结算层 m_IsActive=false） | ✅ 删除；开局直接换牌 |
| Z6 | **手牌直排 vs 原版弧形**（CardsInHand：间距 1.45×卡宽/弧高 0.7×卡高/旋转/z 序） | ✅ 弧形布局（换牌同布局） |
| Z7 | **背景过大/只显局部**（原版 Floor plane 世界 (100.2,0,6.93) scale (30.34,7.46,17.69) + Background (99.3,15.7,-3.34) rotX90） | ✅ 背景幕 30.34×7.46 @(0,0,6.93) + 天空全景（高度≤可见切片→整幅可见；CULL_DISABLED）+ 地面 40×40 阵营地面图 |
| Z8 | **场上 2D 色块角标**（费用/攻/血彩色 StyleBoxFlat 块——原版单位=完整卡面站场） | ✅ 删除；保留已行动暗化遮罩 |
| Z9 | 能量框 UI_Energy_Holder_big x 1778 vs 原版 1622（RT3342 x[1621.7,1923.8]） | ✅ x 1622 |
| Z10 | 牌库文字 'Your deck N' vs 原版 'Cards left: X/Y' @y800；手牌数条 'Hand N|Deck M' vs 'Cards left: XX' | ✅ 按原版 m_text |
| Z11 | Mulligan 文字缺 'in first hand'/'You go second'；自加黑遮罩 | ✅ 原版文字；删遮罩 |
| Z12 | 教程提示条 1320×110 顶部色块 vs 原版 TutorialTip 430×150 @(749,466) | ✅ 按原版位置/尺寸 |
| Z13 | **Filter Toggle 默认展开盖 Tab 栏**（原版 m_IsOn=0）——"无法进入卡组"根因 | ✅ 默认收起（collection/deck_collection 两页）+ 面板 visible=false |
| Z14 | **池复用信号重连漏判**（is_connected 裸 Callable vs bind 连接）→滚动后叠弹窗 | ✅ get_connections 全断重连（collection/deck_collection） |
| Z15 | 收藏页自创 NavBuilder 导航条（原版 Collection Menu 无）| ✅ 删除 |

**遗留（见项目任务文件 8.13 末尾）**：卡牌效果引擎 P1（16 占位关键词/单位 desc 解析/112 未匹配战术/35 种无特效事件）；战斗音乐；battlearena1 基础 60 粒子；攻击类其余 VFX；玩家资料 Ranking/Avatar；开包动画全屏重做。

---

## 〇、问题类别总览（用户问"还有什么问题"——除图标/按钮位置外的系统性类别）

| # | 类别 | 说明 | 检查方式 |
|---|---|---|---|
| 1 | 布局类 | 按钮/图标位置、容器尺寸与说明书坐标不符 | 坐标逐一比对 |
| 2 | 排版类 | 文本溢出/截断、对齐混乱、双语混排、字体大小不符 | 截图 + 文本对比 |
| 3 | 纹理缺失类 | 该有原版贴图的地方用纯色块/StyleBoxFlat 代替、贴图拉伸变形 | 检查 StyleBoxFlat 出现处 |
| 4 | 容器类 | PanelContainer 尺寸/锚点/边距与说明书 RectTransform 不符 | 锚点/尺寸比对 |
| 5 | 交互类 | 按钮作用与说明书（反编译 C#）不符、占位弹窗 | 对照按钮作用表 |
| 6 | 层级类 | 元素父子关系/遮挡/叠放顺序与说明书不符 | 场景树比对 |
| 7 | 资源未用类 | 解包资源存在但项目未接线（任务 3 详查） | 资源清单核查 |
| 8 | 缺失类 | 说明书有元素但项目完全没有实现 | 全树要点未实现清单 |
| 9 | 音效类 | 按钮应有音效（CardMove/CardPlay 等）未接 | 反编译音效引用 |
| 10 | 状态类 | 选中/悬停/禁用态缺失或与说明书不符（三态贴图） | 贴图三态检查 |

---

## 一、收藏-卡组列表（deck_collection.gd vs Collection Menu Variant 说明书 9606/10810 行）

| # | 问题 | 说明书依据 | 状态 |
|---|---|---|---|
| C1 | **右侧自制详情面板(320px)多余**——说明书无此栏，Deck Scroll View [331,156 1589x924] 直达右缘；点卡组应弹 Deck info Popup(全屏，已有) | Collection Menu Variant: Deck Scroll View 1589x924 | ✅ 2026-08-19 修复: 右侧详情面板移除, 网格直达右缘; 详情走 DeckInfoPopup 全屏弹窗; 死代码清理 |
| C2 | **Cosmetics/Styles Tab 点击弹"单机复刻版占位"AcceptDialog**——原版切到卡背收藏/异画页 | Tab: CardBacks(40k_collection_bt_cosmetics)/Alternate Art(40k_collection_bt_style) | ✅ 2026-08-19 修复: Cosmetics/Styles Tab → cosmetics.tscn |
| C3 | **卡组方块 Frame 全幅拉伸**——原版 40K_bt_deck 框内缩 [2,17 246x368] | Collection Deck prefab: Frame [2,17 246x368] | ✅ 2026-08-19 修复: Frame 内缩 [2,17 246x368] |
| C4 | **卡组名位置差**——项目底部锚点 (y357-397)，原版 [20,344 210x40] | Collection Deck prefab: Deck Name [20,344 210x40] | ✅ 2026-08-19 修复: Deck Name 绝对位置 [20,344 210x40] |
| C5 | **选中高亮用 StyleBoxFlat 金框**——原版 Highlight Rounded Square 贴图 | Collection Deck prefab: Highlight [-20,-11 290x427] Highlight Rounded Square | ✅ 2026-08-19 修复: 选中高亮换 Highlight Rounded Square 贴图 (toggled 显示) |
| C6 | **右下显示"30 卡"文字**——原版 Game Mode Icon（经典/练习模式图标 40k_gamemode_icon_classic） | Collection Deck prefab: Game Mode Icon [171,274 84x86] | ✅ 2026-08-19 修复: 右下改 Game Mode Icon (40k_gamemode_icon_classic; 玩家自建=经典) |
| C7 | 通配符条 340x56 比说明书 400x85 小 | WIldcard Display [1470,71 400x85] | ✅ 2026-08-19 修复: 通配符条 400 宽 |
| C8 | Tab 按钮宽 160 微差（说明书 165）；tab 面板 170 | Tab Buttons 165x921 | ✅ 2026-08-19 修复: Tab 宽 165 |
| C9 | 筛选栏 220 宽 vs 说明书 335 | Deck Filters [0,156 335x924] | ✅ 2026-08-19 修复: 筛选栏 335 |

## 二、收藏-图鉴（collection.gd vs CardsTab 说明书 10888 行）

| # | 问题 | 说明书依据 | 状态 |
|---|---|---|---|
| L1 | Tab 按钮高 230(921/4) 与说明书 4 键分占 921 一致 ✅ | Tab Buttons [167,159 165x921] | ✅ 2026-08-19 核查 |
| L2 | **右侧详情面板移除**（说明书 CardsTab 无详情栏, Scroll View 1590 直达右缘; 点卡改弹 CardDisplayer 全屏弹窗）| CardsTab: Scroll View [330,156 1590x924] | ✅ 2026-08-19 修复 |
| L3 | 图鉴网格卡 148x190 vs 原版卡 350x512(Collection Card [0,0 350x512] 大图版?)——图鉴网格是缩略网格，原版 CardsTab 卡格尺寸待查 | Collection Card 350x512 | ⬜ 待核 |

## 三、卡组编辑（deck_builder.gd vs Deck Editing Menu 说明书 8165 行）

| # | 问题 | 说明书依据 | 状态 |
|---|---|---|---|
| B1 | 底部改为 保存/对战 + 卡数图标 + 30/30 计数（原版 Footer 元素补齐） | Deck Editing Footer [0,1010 335x70] | ✅ 2026-08-19 修复 |
| B2 | 卡行行高 86px?（说明书 0x56=86px ✓） | Deck Selector Card Info button 86px | ✅ |
| B3 | 卡组名输入框保留流式布局（sidebar 内 VBox） | Deck Name [10,311 308x50] | ✅ 核查: 位置在 sidebar 顶部合理 |
| B4 | 筛选栏独立布局确认；补 Owned/Upgradable Toggle | Card Filters: Owned/Upgradable Toggle | ✅ 2026-08-19 修复 |

## 四、卡组详情弹窗（deck_info_popup.gd vs Deck info Popup 说明书 13842 行）

| # | 问题 | 说明书依据 | 状态 |
|---|---|---|---|
| D1 | 三键绝对坐标 [345/699/1053,926 324x80] ✓ | Buttons [669,886 1101x80] | ✅ |
| D2 | Info Panel [659,218 1140x650] UI_Deck_Information_submenu_Back ✓ | Info Panel [659,218 1140x650] | ✅ |
| D3 | 卡行 86px+PnP 缩略+费用+卡名+xN ✓ | Deck Selector Card Info button | ✅ |
| D4 | Deck Options 5 圆钮——项目是否齐全(duplicate/share/delete)? | Deck Options [1264,93 520x150] 5 圆钮 | ⬜ 待核 |

## 五、导入卡组（import_deck_popup.gd vs 说明书 646 行）

| # | 问题 | 说明书依据 | 状态 |
|---|---|---|---|
| I1 | Window [560,234 800x452] 40k_popup+texture ✓ | Window [560,234 800x452] | ✅ |
| I2 | Input [610,370 700x141] / Confirm [354,615 478x75] / Close [1317,202 75x75] ✓ | 同上 | ✅ |

## 六、全局核查发现（其他界面滚动核查，待修）

| # | 界面 | 问题 | 状态 |
|---|---|---|---|
| G1 | 全部二级界面 | NavBuilder 5 键导航——检查每界面导航高亮/位置一致 | ⬜ 待核 |
| G2 | mode_select | 与说明书三节对比（Deck Selector 534x693/Continue 453x50/CircleButton 90x90） | ✅ 2026-08-19 核查: mode_select 全元素按说明书 (Back 216,893 64x63/CircleButton 1679,886 90x90/Change Deck 1398,681/Show Deck Content 1729,238/cost drawer/Cardback/Army Selector) |
| G3 | 全局按钮三态 | 检查主要按钮 hover/pressed 贴图是否接齐（UI_Button_Mulligan 三态等） | ⬜ 待核 |
| G4 | 全局音效 | 按钮点击音效（CardMove/CardPlay）覆盖率 | ⬜ 待核 |

## 七、任务 3 交叉引用：解包资源未用项（详见资源清单）

- 11_着色器 524 个：VFX Shader 手写替代（不重写，记录在案）
- 12_主程序资源 剩余 Sprite：按需反查
- 04_音频 剩余音效：按需接线
- community_cards 26 个 index 缺失卡（P3）
- Aura_2 共享资源（备用）
- 08_预制体特效剩余 AnimFX/3D 动画

## 八、deck_builder 原始树核查修复（2026-08-19，菜单全树 9249-9470 行 + 原始 RectTransform 锚点）

| # | 问题 | 修复 |
|---|---|---|
| D5 | 底部 Footer 缺 Done/30-30/卡数图标（原为"保存卡组/对战"） | ✅ 补 保存+对战按钮 + 卡数图标(40k_general_icon_card amount) + 30/30 计数(金色) |
| D6 | Window Options 3 键纯文字（原版图标+nametag 底） | ✅ 补图标(40k_collection_bt_cards/decks/cosmetics) + 40k_main_bt_nametag 名字牌 |
| D7 | 缺 Clear filters 按钮 | ✅ Header 补 [1150,88 250x60] Mulligan 底 |
| D8 | 筛选缺 Owned/Upgradable | ✅ 补 CheckButton + 过滤逻辑 + 清除重置 |
| D9 | 卡牌库标题"卡牌库(点击加入)" | ✅ 改"卡牌库" |
| D10 | 分隔线 z 顺序错误盖住网格 | ✅ sep 移到底层（先于内容 add_child） |
| D11 | 卡面缩略模糊 | ⚠️ PnP 卡面压缩至 56x78 的固有现象（原版行缩略同为小图） |

## 九、deck_builder 第二轮原始 JSON 审查修复（2026-08-19 晚，亲自逐个读原始 Unity JSON + unity_rect_to_godot.py 换算）

> 方法：新工具 `Warpforge_tools/scripts/unity_rect_to_godot.py`（Unity 锚点/offset → Godot 屏幕坐标 y 翻转换算，1920x1080 直接等价）；Deck Editing Menu 全树 248 元素逐个换算后与 deck_builder.gd 逐项比对。

| # | 问题（项目 vs 原版 JSON 屏幕坐标） | 修复 |
|---|---|---|
| D12 | **Clear filters 按钮严重错位**：项目 @(392,200)（Header 中央）vs 原版 x[1488.6,1738.6] y[83.5,143.5]（Header 右上 Filters 容器右缘，RectTransform_-707558480957542620） | ✅ 移至 (1488,83)，字号 22→42 |
| D13 | **筛选栏整栏错位**：项目 x[165,497] vs 原版 x[2.2,333.9]（RectTransform_-719853638878302428 覆盖 Sidebar，不遮卡牌库） | ✅ 移至 x[2,334] |
| D14 | **卡牌库区右移**：项目 x[497,1920] vs 原版 Scroll View x[330.2,1920]（RectTransform_8276914638760963876）→ 损失 167px 宽度 | ✅ 移至 x[334,1920] 宽 1586；删自设"卡牌库"标题（原版无） |
| D15 | **Filters 按钮右移 25px**：项目 @(392,88) vs 原版 x[367.2,417.2]（RectTransform_3548632173616295716）；'Filters' 文字同错位且字号 24 vs 40 | ✅ 按钮 (367,88)、文字 (437,88) 字号 40 |
| D16 | **'Edit your deck' 错位+字号**：项目 @(1370,86) 26px vs 原版 x[1320,1820] y[81,141] 38px（RectTransform_-623581803696558300） | ✅ (1320,81) 38px |
| D17 | **Back 按钮贴图错误**：项目 40k_bt_underbutton+返回20px vs 原版 UI_Button_Mulligan+'Back' 40px（RectTransform_8928128143323754276） | ✅ 换 Mulligan 三态 + 'Back' 40px |
| D18 | **缺费用曲线**：原版 Deck Information cost drawer [88.8,411 158.1x199.1] 9 行 18.9 高（Card Cost 25px + 40k_CardAmount_bar_bg/fill 金条 + Cards in deck 25px，RectTransform_7431712229497630500）项目完全没有 | ✅ 新增 CostDrawer（9 行 TextureProgressBar + 实时更新 _update_cost_drawer） |
| D19 | **字号全面缩水**（原版 JSON m_fontSize 直接值）：Window Options 34/31.5/28.15（项目15）、Deck Name placeholder 28（17）、通配符计数 32.6（16）、卡行 Card Name 34（15）/Count 36（13）/Cost 50（13）、-- Warlord -- 34（16）、-- Defensive -- 34（15）、30/30 36（20）、Done 40（22） | ✅ 全部恢复原版字号 |
| D20 | **筛选栏内容缺失**：原版有 Rarity FIlter 280 高（4_40k_cardframe_rarity_* 50x50 + 名 23.2px）、Type Filter 150 高（40k_menu_search_icon_warlord + 'Warlord' 23.2px）；项目只有阵营+费用。且搜索框 placeholder 中文 15px vs 'Search' 26px；Owned/Upgradable 无 toggle 贴图 32px vs 项目 30px CheckButton 无贴图；Army 标题 15 vs 32 | ✅ 补 Rarity/Type 筛选 + 全部按原版字号/贴图（40_main_bt_toggle_on/off、cost icon 底、稀有度框） |
| D21 | Window Options 选中态：项目金色文字 vs 原版 40k_main_bt_selected BW 红色 Highlight | ✅ 选中红 (1,0.35,0.3) |
| D22 | 防御卡槽/督军行文字字号恢复 | ✅ 34px |

**遗留**：筛选栏运行时位置为序列化快照（覆盖 Sidebar）——原版运行时抽屉动画未知（反编译空壳），维持"筛选栏覆盖 Sidebar 右半"的可见性决策（打开时遮 Sidebar 中部，与 8.10 收藏决策同理）；deck_collection 三栏布局维持用户已确认的方案。

## 十、战斗代码运行性检查（2026-08-19 晚）

| 测试 | 结果 |
|---|---|
| test_battle_hand（手牌 95x150 贴底/拖拽） | ✅ PASS |
| test_battle_hud（门动画/拖拽校验） | ✅ PASS |
| test_arena_props（12 阵营装饰 OBJ+粒子） | ✅ PASS |
| test_tutorial（教程逐条引导） | ✅ PASS |
| test_card_vfx（卡牌动画 VFX 数据） | ✅ PASS |
| battle_sim（随机对局） | ✅ 16 回合正常推进至胜利 |
| e2e_deck（组建→选卡→战斗全链） | ✅ 全部通过 |
| auto_test（图鉴滚动内存监控） | ✅ 内存稳定 119MB |

**结论：战斗代码可正常运行**，无功能性问题。test_battle_hand 的 `set_drag_preview` ERROR 为测试环境直接调用拖拽回调所致（非真实拖拽状态，引擎断言），非代码缺陷。

## 十一、收藏/卡组界面全面按 JSON 重构（2026-08-19 深夜，用户"一切以 Unity JSON 为准，不要近似"）

> 依据：Collection Menu Variant / Deck Selection Popup 全树 Godot 屏幕坐标（unity_rect_to_godot.py）。

### collection.gd（图鉴页 = CardsTab）
| # | 修改 |
|---|---|
| E1 | **布局框架**：HSplitContainer 流式布局 → 绝对定位（原版 Header y[70.9,155.9] + Tab x[167.2,332.2] + 筛选 x[0.3,335.6] 覆盖 Tab + 网格 x[330.2,1920]） |
| E2 | **Header 按原版**：Back @(192,83) 150x60 'Back' 40px / Filter Toggle 50x50 @(367,88)（原 130x44 带字）/'Filters' 40px @(437,88) / Clear filters @(612,83) 250x60 42px / 通配符条 @(1470,71) 400x85（Army 80 + 4 组 65 宽计数 32.6px）/ Separator @y151 |
| E3 | **删自设元素**：'卡牌图鉴'标题、'获取途径'按钮、卡数计数 Label（原版 Header 均无） |
| E4 | **Tab 栏**：x[167,332]（原 x0 起差 167）+ 右缘阴影 40k_main_tab_shadow；英文 Deck/Cards/CardBacks/Alternate Art 36px（原中文 22px）；键 y[188,908] padding-top 30 |
| E5 | **筛选栏内容按原版**：Search 26px（原中文 15px）/ Owned+Upgradable 40_main_bt_toggle_on/off 贴图 32px（原 CheckButton 无贴图 30px）/ Army 100x100 图标块（原文字按钮）/ Rarity 2 列 100x100 块（50x50 稀有度框+23.2px 名，原文字按钮）/ Cost 62x62 费用水晶+45px 数字（原 56x40）/ Type 80x100 图标块（40k_menu_search_icon_warlord/tactic） |
### deck_collection.gd（卡组页 = Select Deck Tab）
| # | 修改 |
|---|---|
| F1 | 布局改绝对（同 E1 框架；网格 x[330.9,1920]） |
| F2 | Header 按原版：Back/Filters 50x50/'Filters'/Clear filters @(612,83) + **Control Buttons：Unlock @(1180,81) 186x60(40k_bt_outline) + Import @(1391,81) + Create @(1661,81) 245x60 40px**；删通配符条（Select Deck Tab Header 无） |
| F3 | Tab：Deck 高亮（当前页）+ 英文文字 36px @ x[167,332] |
| F4 | 筛选栏 x[0,336] 覆盖 Tab：仅 Search 26px + Army 100x100 图标块（原版 Deck Filters 无 Rarity/Cost/Type/Owned） |
| F5 | 删"你的卡组列表"标题/计数/通配符（原版无） |
### import_deck_popup.gd
| # | 修改 |
|---|---|
| G1 | 弹窗 800x452 @ x[560,1360] y[234,686]（原 840 宽错位）；PanelContainer→Control（content margin 重排绝对子节点 bug） |
| G2 | 'Paste your deck' 50px @ 弹窗内 y[46,106]（原 26px VBox 顶部） |
| G3 | 输入框 700x141 @ y[136,277] 32px 'Enter text...'（原 130 高 13px）+ 40K_dropdown_bg 绿底 |
| G4 | Confirm 478x75 @ (161,110) 40K_button 绿(0.37,0.89,0.59) 'Confirm' 45px（原 220x48 18px）；删 Cancel 按钮+说明文字（原版无） |
| G5 | Error msg 28px @ y[293,329]；Close 绿钮 75x75 @ x[1317,1392] y[202,277]（原 x 偏 22px） |
### 测试
- test_collection_filters 更新（旧 ContentArea/中文 Tab 名依赖）→ PASS
- e2e_deck 全过 / test_battle_hand / test_battle_hud / test_popups 全 PASS

---

## 十、战斗界面 + 主菜单 + 弹窗审计修复（2026-08-19 下午，用户"按计划执行+以原始 JSON 为准"）

> 依据：全部为 battlearena1 / mainmenuwarpforge / 03_界面UI 菜单 原始 Unity JSON 链式换算（chain_rect.py 工具：沿 m_Father 累加 anchors/anchoredPosition/sizeDelta/pivot，y 翻转，根 Canvas 全屏处理）。
> 工具：d:/2/Warpforge_tools/scripts/chain_rect.py（新增，修复了 dump_go_tree 的 y 符号/offsets 顺序问题）。

### 战斗界面（battle.gd，阶段 A+B）
| # | 修改 | 原版 JSON 依据 |
|---|---|---|
| H1 | **摄像机 FOV 73→46.4**（Godot fov 为垂直角，原 73 是水平等效 → 取景放大 1.57 倍） | Camera_1461.json 'field of view' 46.397 |
| H2 | 敌方信息区：NameBackground 436×126 @ (-38,16)（左侧出屏为原版设计）/ TitleBackground 311×42 @ (54,93) / 名字 35px / 头像 @ (-19,12) | EnemyInfo 链式 (RectTransform_2687) |
| H3 | 坟场按钮 44→**64²** @ (52,136) | ShowCemeteryBtn (RectTransform_2586) |
| H4 | **删自创"回合指示"**（原版无此元素） | battlearena1 全树无 |
| H5 | 我方信息区：NameBackground @ (-38,951) / 名字 35px / 头像 @ (-19,972)；**骷髅 Milestones 移到 PlayerInfo 上方 Icon 65×54 @ (161,929) + xN 35px @ (225,935)**（原 (36,850) 错位） | PlayerInfo(1174) 链式 |
| H6 | **右侧能量区重建**：UI_Energy_Holder_big 302×481 @ (1778,186)（右侧出屏 160px 原版设计）+ EnemyMana 图标 75×77+40px @ (1826,250) + **TurnBtn 131×80 @ (1716,415)**（原 110×68 @ (1738,440) 偏上 200px）+ PlayerMana 76×77+40px @ (1828,517) | Energy And turn holder 链式 (RectTransform_3359) |
| H7 | 牌库：EnemyDeck 200² @ (1602,-200) 滑入动画 / PlayerDeck 230² @ (1615,850)（原 120×160 错位） | PlayerDeck (RectTransform_3292) / EnemyDeck (RectTransform_2964) |
| H8 | 语音按钮 85²@(480,40/908) → **64×62 @ (51,880)**（原版仅我方有 ChatButton；敌方隐藏） | ChatButton (RectTransform_2984) |
| H9 | **新增左侧按钮组**：OffensiveButton 109×107 @ (0,447) + CenterCameraButton 64×62 @ (18,568)（原缺失） | OffensiveButton / CenterCameraButton 链式 |
| H10 | **新增设置按钮** 64² @ (1808,9)（战斗设置弹窗） | SettingsBtn (RectTransform_2585) |
| H11 | **新增回放条** 4 钮 79.8×48.6 @ (410,37)（Replay/Play/Pause/StepPlay） | ReplayButtons (RectTransform_3355) |
| H12 | **删 2D 棋盘行标签**"敌方战场/我方战场"（原版纯 3D 无行标）；日志条移出棋盘区 → 底部中央 (730,690)（原版 HUD 无常驻日志） | battlearena1 全树 |
| H13 | **攻击选择器改单钮轮换**：Select Attack Background 780×285 @ (570,497) + 单钮 118×119 @ (590,542)（近战优先/仅远程显远程钮，原版三钮重叠单显）+ highlight 176² hover | Drag Attack Selector 链式 |
| H14 | **坟场弹层改左侧滑入**：CemeteryLogPanel x[-1200,794] y[224,878] 滑入 + 40k_battlelog_frame 边框 + 竖排 40k_battlelog_display_neutral 条目（原居中 860×620 横排） | CemeteryLogPanel (RectTransform_2936) |
| H15 | 卡详情弹窗 320×420 → **752×868 @ (584,106)** | Card Display 链式 |
| H16 | 手牌数条 (816,983) 288×90 / 换牌 Continue (1063,922) / 跳过 (102,908) / 门帘 — 原本已正确，未动 | — |

### 主菜单（main_menu.gd，阶段 C）
| # | 修改 | 原版 JSON 依据 |
|---|---|---|
| M1 | **导航 hover：半透明灰面板 → 图标染淡蓝 (0.722,0.815,1.0) 0.1s**（ColorTint 作用于图标 m_TargetGraphic） | MonoBehaviour_2098 m_Colors |
| M2 | **导航按下：图标染灰 (0.784)**（原无反馈） | 同上 |
| M3 | **导航选中态：PLAY 默认常驻红色 Selected highlight (1,0.08,0)**（原版 ToggleGroup 单选 m_IsOn=1；点击切换跟随） | MonoBehaviour_2098 + Selected highlight Image 颜色 |
| M4 | 导航文字 19px 白+描边 → **金色 (0.996,0.929,0.710) 33px 无描边** | MonoBehaviour_1082 等 |
| M5 | 面板背景平灰 → 深红棕 (0.13,0.05,0.02)（UICornersGradient 四角渐变近似，无渐变贴图标注） | MonoBehaviour_1941 |
| M6 | 分隔线 x[1,4]&[163,166] 无 tint → **x[-2.5,0.3]&[164,166.8] tint (0.65,0.38,0.26)** | RectTransform_1099/1108 |
| M7 | **REWARDS 徽章 y 高 84px 修正 → 按钮内 y[91.7,126.7]** | Badge Highlight (RectTransform_1508) |
| M8 | **删 GameModesDim 68% 深蓝暗化层（自造）** — 原版无此层 | mainmenuwarpforge 全树 |
| M9 | **模式区 6 卡单排 HBox → 4 卡 2 行网格**（小冲突/经典 1x2 @ (205,48)/(760,48) 535×849；选秀/教程 1x1 @ (1315,48)/(1315,482) 535×414；间距 20、左内边距 38；删旧版残留多人/练习卡） | FlexibleGridLayout (MonoBehaviour_1961) |
| M10 | 卡内标题：金 38px → **白 58.8px 暗条底部 y[790.55,846.25]**；Timer 行 24px → **42.95/40px @ y[805.55,846.25]**；Border 0.72 → **0.34 深灰** | Event Title/Timer prefab JSON |

### 卡组弹窗（子代理审计后修复）
| # | 修改 | 原版 JSON 依据 |
|---|---|---|
| D5 | **deck_info_popup 督军立绘 548px 出屏 → y[-34,1074]**（pivot(0.5,0) 误算为 (0.5,0.5)） | RectTransform_8411164374367242664 |
| D6 | **Deck Name → y[334,389] 44.5px / Warlord Name → y[387,437] 40px**（漏算 VerticalLayoutGroup 重排，y 差 220px）；补 Game Mode Icon @ (659,106) 100×110 + Army Icon @ (659,327) | RectTransform_-3726127451252815448 等 |
| D7 | 底部三键右对齐 Practice @ (725,886)；**Deck Options 圆钮 5 钮重叠分布 x[1611.65+24.4i] y[130,206]**（原 x[1264,1784] 差 347px）；关闭按钮 → (1783,63) | Buttons/Deck Options/Close 布局组计算 |
| D8 | **import_deck_popup Confirm → 弹窗内 y[336,411]**（原 y[110,185] 差 226px） | RectTransform_-6281951505085497198 |
| D9 | **where_cards_popup 整体修正**：窗口 y[16.3,1006.9] / 标题 72px @ (283,37) + TopBar 分隔线 / 滚动区 (304.5,159.3) 1277×804 / 关闭 (1656.8,9.2) | RectTransform_2081512770263934257 等 |
| D10 | deck_builder 筛选按钮：阵营 52→**100×100**、稀有度 74→**100×100**、费用 30×34→**65×65**（45px 数字不再溢出）+4 列网格、类型 80×74→**80×100** | Toggle/RectTransform_155474855032054485 等 |
| D11 | Tab 文字 'CardBacks'/'Alternate Art' → **'Cosmetics'/'Styles'**；Header 按钮 'Unlock/Import/Create' → 'Debug Unlock/Import Deck/Create Deck'；搜索框 26→35px 高 40 | TabButtonLabel 原始 JSON |

### 待办
- ⬜ battle.gd 敌方手牌区（EnemyArea 图标形态与数量显示细节）、Clock 倒计时条、能量块 Lights 发光
- ⬜ deck_info_popup Deck Options 圆钮精确重叠参数复核（当前按子代理链式值）
- ⬜ main_menu 背景视频从不切换（BG_VIDEO_MULTI 定义未用）；视频映射 JSON 无序列化依据（demo 版 stub）
- ⬜ collection.gd/deck_collection.gd nametag y 差 17.8px、Filters 字号 40 vs 42px 微差

### 测试
- auto_test / e2e_deck / battle_sim（14 回合胜利）/ test_battle_hand / test_battle_hud / test_popups / test_collection_filters 全 PASS

---

## 十一、全项目其余界面核查修复（2026-08-19 晚，用户"还有按钮/图标位置错误+排版混乱"）

> 三代理并行核查 14 个界面 + chain_rect.py 修复（根元素 anchoredPosition/sizeDelta 仍有效——Gacha/Forge/Packs Tab 等根元素 x 偏移 163.8 此前被丢弃；已修并验证战斗场景回归无损）。

### chain_rect.py 修复
- **根元素处理**：m_Father=0 的元素（Gacha Tab/Forge Tab/Packs Tab 等）的 anchoredPosition/sizeDelta 仍相对全屏 Canvas 有效 → x[163.8,1920] 正确输出（原被当全屏丢弃偏移）；场景根 Canvas 特判保留

### 对战入口类（代理1）
| # | 界面 | 修复 |
|---|---|---|
| N1 | mode_select | 搜索弹窗 Window (560,234)/骷髅 567² @(668,176)/'Searching' 50号 x[610,1310] y[293,441]/Cancel (721,570) 478×75/补 'Few players online' 30号；**Show Deck Content (1444,192)→(1729,238)**；**Change Deck (1113,635)→(1398,681)**；阵营列竖排 x[75,240]→底部横向条带 x[336,814] y[814,880] |
| N2 | draft | 费用曲线序反+上移 210px（待修）、督军卡槽偏移（待修）、Deck Info 面板位置（待修） |
| N3 | ranked | 搜索覆盖层整体不符（待修）、Leaderboard tabs/Last Season/Timer/行高（待修） |
| N4 | campaign | 轨道区高度（低优先） |

### 商店类（代理2）
| # | 界面 | 修复 |
|---|---|---|
| N5 | **packs** | 滚动区 (200,190) 1520×420 → **x[164,1920] y[0,1080] 全高**（原屏下半 460px 空区——"排版混乱"主要来源）+ Header 条 y[0,85]+分隔线 y[80,90]；开包动画卡槽居中屏心 (960,540)（原低 260px） |
| N6 | **gacha** | 物品卡 156.8→**300 宽**（5×300 横向滚动，Claimed 徽章 226 不再溢出）；The Vault 字号 44→**90** 中心 x600；Special Items 40→**90**；左区倒计时簇时钟 (550,162)/'结束于'右缘 600；右区时钟 (1430,162)/时间 (1532,162)；阴影2 754→**622 宽**；保底进度条 (1224,920) 37 高→**(1224,905) 62 高**（fill/outline/counter 同步） |
| N7 | shop | 卡包页滚动区 y166→127.6、商品卡内部结构（待修）；TimeCounter 微偏（低） |
| N8 | forge | 石柱中下段多画（原版屏外，待删）；阵营按钮 100×108 vs 136×122（低） |

### 功能类（代理3）
| # | 界面 | 修复 |
|---|---|---|
| N9 | **social** | 积分面板 (1319,160) 384×720 → **x[1505.6,1889.1] y[358.3,869.8] 384×512**（错位 187/198px+高拉伸）；Tab 栏 (167,160)→**x[38.6,210.6] y[104.7,928.5]**；详情卡 980→**1589 全宽** @(331,189)；成员列表 (400,290) 1050×750；创建按钮移 Header 行 (1500,90) |
| N10 | **rewards** | **删右侧 7 个自创快捷按钮列**（原版 Rewards Base Submenu 无此列；遮挡轨道区）→ **加左侧 Tab 栏**（40k_main_tab_background 165 宽全高 + Missions/Campaign/Forge/Menu 4 键 180 高 + 当前页红色高亮）；滚动区 y226→153 812 高 |
| N11 | **quests** | 周常条 (240,766)→**x[205.7,1724.7] y[690.6,918.1] 1519×228**（错位 75px）；标题"任务"移右上 (1274,98) 44 号（原版 Mission Header 右上）；战役/成就按钮下移 (1274,152)/(1484,152)；任务容器 x 起 206 |
| N12 | player_profile | ~~Avatar 页按钮高 108/129px、BattleLog 行内 pin/mode/hero 错位、Trophies 缺 5 分类按钮、Ranking 缺右列~~ ✅ **8.23 全修**（Avatar 5 列 180²/按钮 (25,378)/(25,479)、BattleLog Match Log 行全按 JSON（Replay x1303.5 Pin x1225.6 65² 并排）、Trophies 5 分类+Counter+40k_campaign_bar 条、Ranking Top4 三列+AllFactions FactionScoreSmall 行） |
| N13 | settings/achievements | 合格 ✓（仅 tab 键 20px/无间距微差） |

### 待办（下一轮）
- ⬜ draft.gd 费用曲线/督军卡槽/Deck Info 面板；ranked.gd 搜索覆盖层/Leaderboard；shop.gd 商品卡结构；forge.gd 石柱
- ⬜ player_profile.gd Avatar 页/BattleLog/Trophies/Ranking；settings/player_profile tab 间距 10px
- ⬜ mode_select 阵营条 13 按钮超宽（需横向滚动容器）

### 测试
auto_test 存活 / battle_sim（12 回合胜利）/ e2e_deck 全过 — 全绿

---

## 十二、全项目 UI 英文化 + 战斗格式 bug 修复（2026-08-19 深夜，用户"中文暂时不需要，先按 JSON 英文"）

### UI 文字英文化（约 900 处）
- **battle.gd**：ERR_MSGS 11 条 / 日志与提示 40+ 条 / 按钮（END TURN/Cemetery/Settings 等）/ 换牌 / 坟场弹层 / 卡详情 / 胜利弹窗 / 教程提示 / 语音 tooltip → 全部英文（按 battlearena1 JSON m_text：TurnText 'END TURN' 31px、'Cards left: X/Y' 等）
- **rule_core.gd**：全部 _log/events 事件文本 → 英文（Battle created/Turn N started/Player N deployed X to slot N/dealt damage/counterattacked 等）
- **main_menu.gd**：模式卡标题 Skirmish/Classic/Draft/Tutorial、聊天面板、tooltip、玩家名 Commander
- **卡组系列 82 条**（deck_collection/deck_builder/deck_info_popup/collection/import_deck_popup/mode_select）
- **其余 15 界面 277 行**（draft/ranked/shop/gacha/packs/social/quests/rewards/settings/player_profile/campaign 等）
- 测试工具同步（battle_sim 等 15 个工具的中文引用）
- 残留低优先：achievements/card_displayer/player_profile 等次要界面的半替换混合串（约 200 行，下一轮清理）

### 🔴 英文化引入的 8 个 bug（已全部修复）
| # | 位置 | 问题 | 修复 |
|---|---|---|---|
| 1 | rule_core.gd:535 | 战术伤害 '%s dealt %d damage to %s' % [卡名,目标,伤害] — %d 收到名字 → 运行时报错+日志丢弃 | 参数序 → [卡名,伤害,目标] |
| 2 | rule_core.gd:997 | Shuriken 同错 | [攻击者,伤害,目标] |
| 3 | rule_core.gd:1122 | Stomp 同错 | 同上 |
| 4 | rule_core.gd:1191 | Unstable: dealt %d damage to %s % [名字,伤害] 顺序错 | [伤害,名字] |
| 5 | battle.gd:3371 | _fx_from_event substr(i_tac+4) — 'played tactic' 13 字符 → 战术动画全灭 | +13 |
| 6 | battle.gd:3375 | substr(i_dep+2) — 'deployed' 8 字符 → 部署动画全灭 | +8 |
| 7 | battle.gd:3454 | parts2[2] 英文格式中 [2]=伤害 → 目标位特效不触发 | [5]/size-1 |
| 8 | battle.gd:3384 | 'to slot ' 9 字符 idx+3 碰巧宽容 | +9 |

### 验证
- battle_sim ✓ / rule_test **191 通过 0 失败** / test_battle_hand PASS / test_battle_hud PASS / test_card_vfx PASS / test_collection_filters PASS / e2e_deck 全过 / auto_test 存活
- 战斗核查代理确认：HUD 全部坐标与 battlearena1 JSON 一致 ✓；功能 12 项全 ✓；未做项（Clock 倒计时/Lights 发光/Energy Accumulation/OvertimeIndicator/YourTurnImage/EnemyArea 细节）已记录

---

## 十三、半替换混合串修复（2026-08-20 凌晨续）

- **英文词级替换遗留的混合串修复**：draft/ranked/shop/gacha/social 5 个界面 85 条完整英文句（"Welcome to Draft!"/"Ends in: 23d 5h"/"Claim Rewards"/"Leaderboard"/"Not enough Gold!" 等）
- 修复 deck_builder 筛选栏溢出 P1：**筛选栏内容包进 ScrollContainer**（原版 Card Filters 为 Scroll View——Type 筛选原完全不可见）+ 稀有度 HBox→**2×2 GridContainer**（原 4×100 溢出 80px 到卡池区）+ 类型竖排；同步 `_rarity_box` 变量类型声明
- 验证：e2e_deck 全过 / battle_sim ✓ / test_battle_hand PASS / test_collection_filters PASS
- 剩余待办：player_profile/settings/quests/rewards/campaign/achievements/forge/where_cards 等次要界面约 200 行混合串（下一轮）；战斗未做项（Clock 倒计时/Lights/Energy Accumulation）；卡组 P2（nametag 17.8px/Filters 42px/collection 搜索 30px/where_cards 英文阵营名）
