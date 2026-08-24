# 04_rule_core现状_笔记（效果引擎 P1 前盘点）

> 全文读依据（子代理 ④ 2026-08-23）：`D:/warpforge/scripts/rule_core.gd`（2531 行逐段全读）、`D:/warpforge/autoload/game_data.gd`（397 行）、`解包资源使用地图.md` 坑 57（L798-810）、`项目任务文件.md` L13/L63、`说明书通读笔记_0823/01`（360 行）、`05`（L49 枚举）、`tools_dev/rule_test.gd`（1992 行）、`test_fx_engine.gd`（339 行）、`battle.gd` L4160-4730。

## ① 摘要（已实现清单 + 缺口 TOP）

1. rule_core.gd=纯逻辑 headless 规则引擎（class_name RuleCore，全 static）；ctx 大字典 + players[2] + board[9]（WARLORD_SLOT=4 督军）；unit 单位字典（kws/fx/temp_buffs/remnant/spirit_stone 状态位）。
2. 关键词驱动：`_parse_keywords`（L234）+`_parse_desc_fx`（L273）双通道；KW_IMPLEMENTED 53 键 / KW_MATCH 前缀表 59 对；**FX_PREFIXES 24 个**（历史"18 前缀"已过时）。
3. 已实现机制：give/gives/deal/deals 部署即结算（P0 52 张）/enemy Warlord 分支（7 张）/**反击同时结算**（Sniper/Long Range 免反）/pending_fx 选目标挂起/Choose one/[Energy]/[Faith] 付费激活/Dark Pact 四契约+广播链/Faith 广播/Pray 广播/Talent 每回合生成（77 名单）/Stimulation/Genomic 选池/常驻降费光环/Skulls 20/10/0/疲劳/Swarm/Tide/Uprising/Teleport/Ambush/Oath/Codex/Agenda/Duty/Ferocity/Synapse(仅伤害)/Mob/Regiment/Cruelty/Ecstasy(攻击计数版)。
4. **与规则书偏差 2 处**：Penitence（规则书=受伤未死触发；实现=替代行动 activate_alt L946-952）；Ecstasy（规则书=生命降至 X 触发；实现=累计攻击 N 次 declare_attack L2236-2239）。
5. 解析全部集中在 `_resolve_text`（L1043 约 440 行）；目标收集 `_collect_tactic_targets`（L1935 约 140 行）。
6. **事件文本=唯一对外表现通道**：57 个 `_log` 调用点 + 20 处直接 `events.append` = **77 个模板**，写进 `ctx["last_events"]`；battle.gd `_append_events`（L4182）→`_fx_from_event`（L4412）文本解析→VFX/音效。
7. **缺口 TOP（P1 挂点）**：WhileInPlay（无持续效果堆）、Survivor/Requiem/Landing/Reanimated/Rage/Growth/Relentless/Mutated/Combo（无触发点）、PlayedThirdCardInTurn（无本回合打牌计数）、AboutToAttack/UnitDamaged*/UnitHealed/UnitStunned（无 hook）、Sacrifice/OtherUnitDeath（仅硬编码广播）、CardReturnedToHand/Deck、ThisUnitSummoned/CardCreatedInHand 通用化、SpentAllMana/TriggeredCodex、UseSpiritStone/OnCollectSpiritStone（只生成不收集）、UnitReceivesMarkerlight/**Sentry/Sabotage/Companion 四关键词完全空转**、QuestTriggered/OnCollectQuestPoints、**Overtime 加时（rule_core 无）**、防御卡（无）。
8. 测试：rule_test 89 函数 295/0；test_fx_engine 15 节 41 断言；缺口机制全无测试。
9. game_data.gd=卡数据管线（card_stats 1106 OCR+noise 过滤 42+6；TALENT_CARD_NAMES 77 硬名单）。
10. **P1 事件总线最安全接入**：rule_core 加 `_emit(ctx, trigger, payload)` 薄层 + `ctx["_emitted"]`，挂 7 个函数（play_card/turn 两端/declare_attack/_damage_unit/_kill/_draw/_check_skulls/_trigger_fx）；last_events 文本冻结不动（battle.gd 现有 _fx_from_event 不受影响可回退），battle.gd 改读 _emitted。

## ② 事件文本模板（77 个）

- `_log` L2529 唯一文本出口（57 处调用 L173/406/419/444/549/559/651/662/665/690/710/715/723/726/815/821/824/835/843/867/901/969/1067/1134/1136/1154/1159/1178/1210/1226/1244/1251/1263/1279/1298/1303/1308/1316/1332/1349/1356/1382/1394/1399/1402/1421/1430/1436/1478/1696/1704/1716/1790/1801/1891/1905/2300/2501/2514）+ 20 处直接 append（declare_attack 7：Shuriken/attacked/counterattacked/lost Long Range/Blast/stunned by/blinded by；_damage_unit 3：shield blocked/invulnerable/flipped on damage；_stomp_splash 1；_kill 6：warlord destroyed/Backlash/died→spirit stone/died→flipped remnant/Hunt Mark/destroyed；_unstable_blast 1）。
- 格式：`ctx["last_events"]: Array[String]`（无结构化字段）；`_log(ctx,fmt,args)`=`append(fmt % args)`；每回合/行动后整体赋值原子提交。
- 类型分组（battle.gd 匹配）：deployed+to slot / played tactic / healed·regenerated / stunned / gained（armour/shield/shuriken/Long Range/兜底）/ dealt+damage / attacked X: N damage（正则）/ counterattacked / 关键词音效（Ambush/Artifice/Rally/Slay/Strike/Duty/Agenda/Backlash/Oath/Tide）/ returned to+hand / fatigue+damage / Skull!
- **局限**：同模板多语义合并（"gained"）、目标名空格硬索引（parts[2]/parts[size-1]）、槽位 rfind("to slot ")、中文前缀依赖英文模板。

## ③ P1 事件总线接入方式（10 个挂接点）

- 原则：rule_core 内薄广播层，last_events 冻结不动；battle.gd 消费新通道 `_emitted`，_fx_from_event 降级 fallback。
- 挂接点：① play_card L748（ThisCardPlayed/OtherCardPlayed/Stimulation/Artifice/Oath/Uprising/Teleport/Tide/Rally/自增益）② begin_turn L589/end_turn L693（TurnStart/TurnEnd/Talent/Ambush/Regeneration/Ephemeral/Remnant）③ declare_attack L2193（AboutToAttack/UnitAttack/被攻击伤害/反击/Blast/Stomp/Slay/Strike/Mob/Regiment/Cruelty/Ecstasy/失去 stealth 等）④ _damage_unit L2374（UnitDamaged/Shield/Invulnerable/UnitDamagedByAbility 区分）⑤ _kill L2421（ThisUnitDeath/OtherUnitDeath/Backlash/Unstable/Waystone/Remnant/Hunt Mark）⑥ _trigger_fx L1701（Rally/Slay/Duty/Pray/Ferocity 统一出口）⑦ _resolve_text L1043（deal/heal/draw/gain/refill/return/lower/deploy 成功分支）⑧ _draw L2506（CardDrawn/疲劳）⑨ _check_skulls L2491（EarnedSkull）⑩ resolve_cost_act L539/resolve_choose_one L1684/resolve_pending_fx L1744（UseFaith/Resolution/结算完成）。
- 不在 _log 单点做总线（77 模板多语义混叠无法还原结构化 trigger）。

## 1. 架构

### 1.1 数据结构
- ctx（new_battle L110-174）：mode/turn/turn_p[2]/active/winner(0/1/2/3 平局 L729-743)/last_events/players[2]/pending_fx/pending_cost_act/pending_choose_one/card_pool/last_created·last_returned。
- player（L150-166）：energy/max_energy/faith/skulls/fatigue/deck/hand/discard/board[8]（9 槽）/warlord/drawn_cards。
- unit（_make_unit L177-231）：card/name/cost/attack/health/max_health/armor/ranged_attack/exhausted/is_warlord/kws/fx/shield/stun/stun_turn/blind/blind_turn/attacks_turn/attacks_total/face_down/remnant/spirit_stone/temp_buffs/cost_aura。
- **持续效果堆不存在**（仅 cost_aura L758-766 + temp_buffs 时长队列 _expire_temp_buffs L1805-1821）→ WhileInPlay 缺口。

### 1.2 回合主循环
| 函数 | 行号 | 要点 |
|---|---|---|
| new_battle | L110 | 洗牌+督军（首 hero）+起手 3（skirmish 4/督军-10 血/后手+1 能） |
| begin_turn | L589 | 清挂起→能量（skirmish 1+2N，L608-613）→temp 过期→attacks 清零→stun/blind 恢复→Talent 生成（L633-654）→Ambush 翻开+触发（L656-663）→抽 1 |
| end_turn | L693 | 清挂起→temp 过期→能量置 0→Regeneration（L703-710）→Ephemeral 移除（L711-718）→Remnant 摧毁（L719-724）→换边 |
| mulligan | L669 | skirmish 禁用 |
| check_winner | L729 | 双督军≤0 平局 3 |
| play_card | L748 | 费用（双降费光环 L758-777）→战术/单位分叉（Stimulation→Artifice→剥离激活→_resolve_tactic→Choose one→付费激活→弃牌→_check_codex；单位：_make_unit→Swarm→Ambush 面朝下→fast/flank→Oath→Uprising 广播→入格→dark pact 广播→Teleport→Tide→Rally→自增益→_check_codex） |
| activate_alt | L925 | Duty L939 / Pray·Penitence L946 / Ferocity L957（触发后洗回） |
| declare_attack | L2193 | Agenda 代替攻击→配额（bloodthirst 2 次）→Pindown/Blind→shuriken 预伤→主伤害→**反击同时结算**（L2276-2288）→失去 Long Range→死亡处理→Blast→Concussion/Blind→Stomp→_check_skulls→Slay/Strike/Mob/Regiment/Cruelty |
| _damage_unit | L2374 | Shield→Invulnerable→Vulnerable→Armour 最低 1→扣血+Ambush 翻开 |
| _kill | L2421 | Unstable→Backlash→Waystone→Remnant→Hunt Mark→入弃 |
| _stomp_splash / _unstable_blast / _check_skulls / _draw | L2400/L2472/L2491/L2506 | |

### 1.4 解析入口
_parse_keywords L234 / _parse_desc_fx L273（正则 `(?i)(prefix)\s*(\d+)?\s*:` 扫 FX_PREFIXES L262-270；ecstasy_n 单独 L293-294）/ _cost_act_of L305 / _strip_cost_act·_energy_act_prep L344·L352 / _choose_one_of·_strip_choose_one L1659·L1675 / _strip_fx_segments L1644 / **__resolve_text L1043**（deal→stun→destroy→heal→draw→return→lower cost→refill→deploy→give/lose/gain；条件伤害 "If target has X deal N instead" L1072-1087；"already had X" L1088-1106/L1391-1400）/ _collect_tactic_targets L1935（your/enemy warlord/highest·lowest/复数/all enemies/all units/random N/with 定语/pick）/ _apply_gain L1560（GIVE_KW 53+8 表 L985-1005；属性 ±N；temp_end 记 temp_buffs）/ _fx_target_type·_auto_fx_target·_cond_unit_matches L1482·L1500·L1534 / _trigger_fx L1701（pick 型挂起 pending_fx/ap）。

## 2. 已实现机制（节选全表见原报告 §2.1，53 键+效果段 24 前缀）

**FX_PREFIXES 24**：rally/slay/strike/backlash/duty/artifice/codex/cruelty/mob/synapse/regiment/destroyer/oath/tide/uprising/teleport/agenda/talent（18，L263-265）+pray/penitence/ecstasy/stimulation（L267）+ambush/ferocity（L269）。

**GIVE_KW 可赋予但无效果实现（空转）**：companion（176）/sentry（205）/markerlight（192）/sabotage（204）——只写 kws 无触发点。

**加时（ot）**：rule_core 无任何加时逻辑；battle.gd `_on_clock_tick` L4670-4671 注明"单机无硬超时归零重置（原版 Overtime 不模拟）"。防御卡机制在 rule_core **不存在**。

## 3. P1 缺口（AbilityTrigger 枚举对照，97 值评估）

✓ 已有（31）：ThisCardPlayed/TurnStart/TurnStartPlayer/TurnEnd/Talent/UnitAttack/ThisUnitDeath/Unstable/Slay/Codex/TurnStarted/Pack/Mob/Regiment/Artifice/Strike/Duty/Pray/Ambush/Uprising/Teleport/Agenda/Stimulation/Ecstasy(偏差)/Cruelty/Ferocity/Oath/EarnedSkull/UnitReceivesMarkOfChaos/UnitDamaged(部分)/ThisCardDrawnAsTrap(无)
△ 部分/硬编码（12）：OtherCardPlayed(仅 stimulation/uprising)/UnitDamaged/OtherUnitDeath(仅 2 desc)/UnitDamagedByAttack/ThisUnitSummoned/CardCreatedInHand(散落)/OtherCardDrawn/UnitReceivesHuntMark/TriggeredSwarm/TriggeredSynapse(仅伤害)/SpentAllMana(≈codex)/UseFaith/TriggeredPray/UnitLoseStealth
**✗ 缺口（~52）**：PlayedThirdCardInTurn/WhileInPlay/TurnBeforeEnd/Courtesy/Resolution/Growth/HeroDefenseBonus/Rage/TurnSetup/UnitDeathByPoison/UnitDeathAttacking/UnitDeathByAbility/UnitDamagedByAbility/UnitHealed/OtherUnitSummoned/TriggerOnceIfBoardCriteria/Sacrifice/OtherCardSacrifice/Relentless/WhileInPlayVariable/ThisCardDrawnAsTrap/TrapResolved/AboutToAttack/UnitPoisoned/UnitStunned/ThisUnitAbilityUsed/FollowUpResolution/Survivor/SurvivorSpent/Requiem/OtherCardRequiem/Landing/OtherCardLanding/OtherCardSpiritStone/Mutated/CardReturnedToHand(hook)/CardReturnedToDeck/QuestTriggered/TriggerEnchantment/UnitReceivesMarkerlight/Support/Reanimated/Combo/UseSpiritStone/OnCollectSpiritStone/TriggeredCodex/TriggeredDuty/OnCollectQuestPoints/OnSecretCreated/OnSabotageCreated/TriggeredFerocity/OtherCardMob/OtherCardRegiment

## 4. 事件文本→battle.gd 联动

- _append_events L4182-4188 → _fx_from_event L4412（~190 行 11 分支，详见 ② 分组）。
- 局限：单位名→位置反向搜索（_find_unit_pos/_find_unit_world_pos L4717-4728 按名遍历 board——**同名牌歧义/已死单位找不到→特效落空**，死亡爆散 P2 即此）；槽位 rfind("to slot ")；heal parts[2] 硬索引。**P1 结构化 payload 可直接消灭全部硬索引**。

## 5. 测试现状

- rule_test.gd 89 测试 295/0：P0 新增 _test_deploy_give_deal(315)/_test_sniper_counter(360)/_test_ranged_no_counter(388)；关键词批次 _test_kw_*(465-2000)；能量/EC/信仰 _test_energy_act_parse(623)/_test_faith_might(769)/_test_ec_mechanics(860)；战术解析 _test_tactic_*(1449-1888)。
- test_fx_engine.gd 15 节 41 断言：Rally pick/Duty/Slay/Strike/条件伤害(If has Armour)/this turn 时长/until your next turn/降费/常驻光环/条件命中/Embers already→destroy/Da Old Ways already→+2/方括号[Shield]+Draw。
- 测试缺口：WhileInPlay/Survivor/Requiem/Landing/Relentless/Combo/Courtesy/Resolution/Growth/Rage/Mutated/Sacrifice/Quest/Secret/Sabotage/Reanimated/Support/SpentAllMana/Markerlight/Overtime/防御卡/同死判定序（被攻击方优先）/Penitence 规则书定义/Ecstasy 规则书定义——均无测试。

## 附：数据管线（game_data.gd 397 行）

- _load_data L114：factions/card_stats（OCR 数值 1106）/decks/decklists/portraits/card_ids(996)/deck_btn_map；noise 过滤 L130-135（42 环境+6 未发行）。
- 查询：faction_by_id/name L164-176 / get_cards L178 / is_talent_card L193-212（TALENT_CARD_NAMES 77 L15-95+desc 正则+后缀）/get_face L291/get_face_hi L304（LRU 64）/get_thumb L244（LRU 256）。
- 接口：ctx["card_pool"]（battle.gd 注入 GameData.cards 无 noise）；rule_core _find_card_in_pool L1835 仅按名找卡。
- game_data **不解析 desc 效果**——解析 100% 在 rule_core（宽正则兜底 OCR 噪声，坑57 P1 遗留 d：15 张乱码人工核对单另列）。
