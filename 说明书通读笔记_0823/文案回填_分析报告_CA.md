# 文案回填分析报告 — CA（4 界面：Draft / Draft Expiring / Rate / Daily Streak）

> 生成 2026-08-23。分析方式：从原始 Unity JSON（d:/2/解包整理/03_界面UI/菜单/）根 GO 走树取**完整 m_text**（自写树遍历脚本 `Warpforge_tools/scripts/_tmp_ca_fulltext.py`，直接读原始 JSON，非 audit 表截断预览），与项目 gd 现状字符串逐项对比。关键长文本另用 grep/JSON 加载复核字节级一致（含 U+2014 破折号等）。
> 结论速览：**需替换 24 处**（Draft 20 + Rate 1 + Daily Streak 2 + 1 处成功态缺失需补）；**保留 24 处**（原文一致或原版为西语/俄语残留）；**标注疑点/缺失 16 处**（原版为占位符/运行期变量、inactive 元素、单机无内购未实现的按钮等）。

---

## 1) Draft 界面（原版根 GO "Draft Mode Menu Demo"；项目 `d:/warpforge/scripts/draft.gd`）

### 1.1 需替换（20 处）

| 元素 | 项目文件:行 | 项目当前字符串 | 原文完整 m_text | 动作 |
|---|---|---|---|---|
| Header Window Title | draft.gd:152 | `"Draft"` | `Game mode` | **替换** → `"Game mode"`（说明书 Window Title 原文；原版各模式头统一 'Game mode'） |
| Intro Game Mode Title | draft.gd:181 | `"Welcome to Draft!"` | `WELCOME TO THE DRAFT MODE!` | **替换** → `"WELCOME TO THE DRAFT MODE!"` |
| Intro Game mode instructions | draft.gd:183 | `"Select your Warlord, build a Deck, and win as many battles as you can!"` | `Select your warlord, build your deck from the draft options available, and face other players with it!` | **替换**（全句整串替换） |
| Intro Description 1 | draft.gd:184 | `"12 wins or 3 losses to settle Rewards - every match can continue"` | `Try to win as many battles as possible! If you are defeated 3 times, your run will end.` | **替换** |
| Intro Event locked | draft.gd:188 | `"Hint: complete one battle to enter"` | `Locked. Win one battle to enter.` | **替换** |
| Pay Game Mode Title | draft.gd:208 | `"Welcome to Draft!"` | `WELCOME TO THE DRAFT MODE!` | **替换**（同 Intro） |
| Pay Game mode instructions | draft.gd:219 | `"Select your Warlord, build a Deck, and win as many battles as you can!"` | `Select your warlord, build your deck from the draft options available, and face other players with it!` | **替换**（同 Intro） |
| Pay Free Button | draft.gd:221 | `"Free Entry"` | `Free` | **替换** → `"Free"` |
| Pay FreeTimeText | draft.gd:224 | `"Playable now"` | `Available in` | **替换**（原文为片段 "Available in"，运行期大概率拼接剩余时间；单机可 `"Available in"` + 计时，或仅显示原文片段） |
| Warlord State Title | draft.gd:235 | `"Choose Warlord"` | `Select Warlord` | **替换** → `"Select Warlord"` |
| DEBUG_REROLL_BUTTON | draft.gd:249 | `"Reroll"` | `REROLL` | **替换** → `"REROLL"` |
| Packs SubTitle | draft.gd:384 | `"Select cards to join your Deck"` | `Choose cards to add to your deck` | **替换** |
| Packs Reroll Text（标签） | draft.gd:391 | `"Reroll Pack:"` | `Reroll packs:` | **替换** → `"Reroll packs:"` |
| Ongoing Game Mode Title | draft.gd:481 | `"Draft"` | `Draft Mode` | **替换** → `"Draft Mode"` |
| Ongoing Victories text | draft.gd:492 | `"Wins:"` | `Victories:` | **替换** → `"Victories:"` |
| Ongoing Defeat Marks | draft.gd:525 | `"Losses:"` | `Defeats:` | **替换** → `"Defeats:"` |
| Ongoing To Battle Button | draft.gd:553 | `"Start Battle!"` | `Battle!` | **替换** → `"Battle!"` |
| Ongoing Collect Button | draft.gd:575 / 860 | `"Claim Rewards"` | `Collect reward` | **替换** → `"Collect reward"`（两处都改：575 建钮 + 860 `_refresh_ongoing` 复位） |
| Deck Info Alliance 空态 | draft.gd:721 | `"Join an Alliance for extra Rewards"` | `Join an alliance to gain additional rewards` | **替换** |
| Header 副信息 | — | — | — | （无；Header 无其他文字） |

### 1.2 保留（原文一致 / 原版残留）

| 元素 | 项目文件:行 | 项目字符串 | 原文 |
|---|---|---|---|
| Intro Start Button | draft.gd:185 | `"Start"` | `Start` ✅ |
| Warlord Select Button | draft.gd:319 | `"Select"` | `Select` ✅ |
| Warlord Continue Button | draft.gd:253 | `"Continue"` | `Continue` ✅ |
| Pay Timer | draft.gd:218 | `"Ends in: 23d 5h"` | `Ends in: 23d 5h` ✅ |
| Ongoing Timer | draft.gd:491 | `"Ends in: 23d 5h"` | `Ends in: 23d 5h` ✅ |
| Ongoing Reset Event Button | draft.gd:549 | `"Abandon"` | `Abandonar`（**西语残留**→按用户已裁决先例保留项目英文 "Abandon"）✅ |
| Deck Info Title | draft.gd:642 | `"Deck info"` | `Deck info` ✅ |
| Deck Info CardCounter | draft.gd:646 | `"Cards: 30/30"` | `Cards: 30/30` ✅ |
| Deck Info Energy balance | draft.gd:697 | `"Energy balance"` | `Energy balance` ✅ |
| Deck info 费用行数字 | draft.gd:668/683 | `str(cost)` / `"0"` | `0`（动态）✅ |
| Packs Stage Counter | draft.gd:385 | `"Pack 1/10"` | 原文为两元素：`Pack` + `1/10`（原版 Pack 标签与 Stage Counter 上下叠放）——内容一致，合并单行可接受（或按原版拆两元素）✅ |

### 1.3 标注疑点 / 缺失（16 处）

| 元素 | 项目:行 | 现状 | 原文 | 说明 |
|---|---|---|---|---|
| Pay Description 1 | — | **缺失** | `Try to win as many battles as possible! If you are defeated 3 times, your run will end.` | 原版 Pay State 有 Description 1（同 Intro），项目 Pay 层未放 → **建议补**（用原文全句） |
| Pay Premium Button + PremiumText | — | 未实现（单机全免费） | `Premium Rewards!` | 原版有 Premium（价格 0）+ Premium10x（`10x Premium Rewards!`）。单机无内购→**保留不补**（注释已声明单机全免费） |
| Reroll 按钮 Button Text | draft.gd:387 | `"Reroll Pack"` | 原版 **空串** + 价格显示 `3000`（Price Display 图标+3000） | 原版重摇入口=价格按钮（文字空、显示 3000 价格）；项目自创 "Reroll Pack" 文字。单机免费无法显示 3000 → **建议按钮文字改 `"Reroll"`（与 `Reroll packs:` 标签配对）**，标注供裁决 |
| CardUI New Card Badge Text | —（card_displayer 未实现） | 未实现 | `New!` | 选督军/选卡界面原版卡面挂 New! 徽章；项目卡面组件未铺 → 缺失，后续铺卡组件时用 `New!` |
| CardUI Banned Text | — | 未实现 | `Banned` | 同上（选卡容器 Ban Icon）；俄语残留版本 `Запрещено`（CardUI-Warlord/Generic Multi Card Display）→ 若实现一律用英文 `Banned` |
| CardUI CreatedByText | — | 未实现 | `Created by someone fancy` | 原版 [INACTIVE]（隐藏）→ 不改 |
| Ongoing Quote End | — | 未实现 | `"Battles like this are what I was made for." —Marneus Calgar`（U+2014 破折号；含首尾引号） | 原版 [INACTIVE]（隐藏）→ 可不实现；若实现务必含引号+破折号 |
| Debug Win / Debug Battle | — | 未实现 | `Change Deck` / `Battle!` | 调试元素 → 可不补 |
| Deck Info Warlord Name | draft.gd:700 | `"Warlord: " + 名字` | 占位符 `Warlord Name`（运行期被真实督军名整体替换） | 项目加了 `"Warlord: "` 前缀——原版占位符会被整体替换（显示=仅名字）；建议去掉前缀或保留（低优先，标注） |
| Deck info 卡行 Count | draft.gd:885 | `"×%d"`（乘号 ×） | 卡行模板 `x2`（小写字母 x） | 建议统一 `"x%d"` 与原版一致（deck_builder.gd 已用 x？核对时一并统一） |
| Cards in deck 卡行 Card Name/Cost | — | 运行期填充 | 占位符 `Card Name` / `5` | 模拟模板 → 无需改 |
| Alliance 两个按钮 | — | 仅文字无按钮 | `Search`（Join Alliances Button）/ `Leaderboard`（Leaderboard Button） | 功能缺失（非文案）；social.gd 已有实现可参考 |
| 卡组列表视图 Warlord Name / Card counter | draft.gd:704 | `"30/30"` | `30/30` | ✅ 保留（一致） |
| Generic Multi Card Display（inactive） | — | 未实现 | `Header Text` / `Back` | 原版隐藏模板 → 不实现 |
| Intro Event Title / Event Description（均 inactive） | — | 未实现 | `Duel at Saint's Haven` / `During the War of Beasts Marneus Calgar openly challenged the Warmaster. Urged to humiliate the Chapter Master, Abaddon and his elite teleported before Calgar and his retinue on Saint's Haven, where battle immediately broke.` | 原版 [INACTIVE]（事件模式文案）→ 项目无事件系统，**不补**（保留原文备查） |

---

## 2) Draft Mode Expiring Popup（项目 `d:/warpforge/scripts/draft_expiring_popup.gd`）

**需替换 0 处。** 逐项：

| 元素 | 项目:行 | 项目字符串 | 原文 | 动作 |
|---|---|---|---|---|
| Game Mode Title | :68 | `"The Space Marine event has finished!"` | `The Space Marine event has finished!` | 保留 ✅（已是 JSON 原文） |
| subtitle | :81 | `"Alliance: none (offline build)"` | 占位符 `Alliance Name`（运行期=真实联盟名） | **标注疑点**——原版为占位符被整体替换（显示=仅联盟名）；单机无联盟，项目自创说明可保留，或改用 `"Alliance Name"` 占位+运行期（无数据则留占位） |
| Alliance Name（联盟名标签） | — | **缺失** | `Alliance Name:`（带冒号！与 subtitle 占位符不同文本，位于 [917,371.5]） | 原版另有独立 `Alliance Name:` 标签（冒号结尾）→ 项目缺失；建议补 `"Alliance Name:"` + 联盟名（单机=空/无） |
| Individual rating value | :98 | `"%d" % _skulls` | `3400`（示例值） | 保留 ✅（动态，格式一致） |
| Victories text + Number | — | **缺失** | `Victories:` / `9\n`（数字带尾随换行符 \n） | 原版 [INACTIVE]（隐藏）→ 可不补；若补数字注意原文带 `\n` |
| x10 text | :117 | `"x10"` | `x10` | 保留 ✅ |
| Leaderboard 按钮 | :127 | `"Leaderboard"` | `Leaderboard` | 保留 ✅ |
| Tap To Continue | :145 | `"Tap to continue"` | `Tap to continue` | 保留 ✅ |

---

## 3) Rate Popup（项目 `d:/warpforge/scripts/rate_popup.gd`）

**需替换 1 处。**

| 元素 | 项目:行 | 项目当前字符串 | 原文完整 m_text | 动作 |
|---|---|---|---|---|
| TitleText | :66 | `"Welcome to Warpforge!"` | `Welcome to Warpforge!` | **保留** ✅（文案一致）——**特殊发现**：原版 TitleText 为 **[INACTIVE]（隐藏）**，原版只显示 DescriptionText；项目显示了标题。是否照原版隐藏由主代理裁决（文案本身一致） |
| DescriptionText | :78 | 自创多行：`"Please share your thoughts on the game.\n\nYour rating helps us improve!\n\n\n★ 1-4 stars: issues or suggestions\n★ 5 stars: support us to keep developing"` | `Please share your thoughts before entering the battlefield.<br>How would you rate the game so far? ` | **替换** → 原文（`<br>` 转真实换行 `\n`；**注意原文句尾有空格** `so far? `；两行文本） |
| Button 1-4 stars | :87 | `"1-4 stars"` | `1-4 stars` | 保留 ✅ |
| Button 5 stars | :89 | `"5 stars"` | `5 stars` | 保留 ✅ |
| 点击后 _flash 提示 | :116 / :126 | `"Thanks for your feedback! We will keep improving"` / `"Thanks for the five stars! For the Emperor!"` | （原版无此文案——点按后原版跳转 App Store/商店页） | **标注疑点**——项目自创运行期反馈提示，非原版元素；可保留（离线单机无商店可跳），也可删 |

---

## 4) Daily Streak Popup（项目 `d:/warpforge/scripts/daily_streak_popup.gd`）

**需替换 2 处（其中 1 处为成功态缺失需补）。**

| 元素 | 项目:行 | 项目当前字符串 | 原文完整 m_text | 动作 |
|---|---|---|---|---|
| Window Title | :106 | `"Daily Streak"` | `Daily Streak` | 保留 ✅ |
| Daily Streak Broken | :141 | `"STREAK BROKEN"` | `STREAK BROKEN` | 保留 ✅（全大写原文） |
| Current Streak Lost count | :152 | `"Streak lost: %d" % _streak` | `Streak lost: 10`（10=示例值） | 保留 ✅（格式串一致） |
| Info（失败态） | :161 | `"Log in daily to keep your streak and earn more rewards"` | `Log in daily and keep your streak going to unlock bigger rewards. Skip a day, and your streak resets.` | **替换**（全句） |
| Reset Streak | :172 | `"Reset Streak"` | `Reset Streak` | 保留 ✅ |
| Current Streak（成功态） | :214 | `"Current streak:"` | `Current streak:` | 保留 ✅ |
| Current Streak Value | :222 | `"%d" % _streak` | `7`（示例值） | 保留 ✅ |
| **Info（成功态）** | — | **缺失**（`_build_success` 未渲染底部 Info） | `Log in daily and keep your streak going to unlock bigger rewards. Skip a day, and your streak resets.` | **补**（与失败态同文案，原文在 Streak Successful 下 [47.5,830] 有另一份同文本 Info 元素） |
| Next Rewards text | :311 | `"More Rewards In %dh %dm"` | `More Rewards In` + `19h 23m`（原版拆两元素，`19h 23m`=示例值） | 保留 ✅（合并显示内容一致） |
| 奖励卡 Day 标签 | :254 | `"Day %d"` | —（Rewards Content 运行期生成，无静态原文） | 标注疑点——项目自创，可保留 |
| 奖励卡状态标签 | :279 | `"Daily Rewards"` / `"Locked"` | —（同上，运行期生成） | 标注疑点——自创，可保留 |
| main_menu 入口 | main_menu.gd:142-161 | 无 Daily Streak 入口按钮（登录时自动触发弹窗） | — | 无需处理（无入口文案可比对） |

---

## 特殊发现汇总

1. **Rate Popup TitleText 原版为 inactive（隐藏）**——项目显示了标题；文案本身一致。用户此前规则"inactive 元素是否需要文案"：原版隐藏→项目若追求完全复刻应隐藏标题，但文案保留备查（裁决项）。
2. **draft_expiring "Alliance Name" 有两处不同文本**：subtitle 占位符=`Alliance Name`（无冒号，[1017,304]）；Alliance 标签=`Alliance Name:`（**带冒号**，[917,371]）——项目目前只有前者位置的自创文本，后者元素缺失。
3. **Victories text Number 原文带尾随换行**（`9\n`）——若实现数字注意不要截掉 \n（TMP 原文如此，或为样式遗留，按原文）。
4. **Quote End 含 U+2014 EM DASH 与首尾双引号**——原文 `"Battles like this are what I was made for." —Marneus Calgar`（60 字符）。
5. **Rate DescriptionText 句尾有空格**（`so far? `）——替换时按字节保留或自定（TMP 空白视觉无差异，给出原文即可）。
6. **draft Pay 状态 Description 1 缺失**（原版有）；**draft 成功态 Info 缺失**（原版有）——两处"补文案"建议一并列入回填。
7. 俄语残留（`Новинка!`/`Запрещено` 于 CardUI-Warlord 与 Generic Multi Card Display）与西语残留（`Abandonar`）——按用户 Deck info 先例：项目英文保留，不替换。
8. 无 main_menu "Daily Streak 入口文案" 需替换（弹窗自动触发，无入口按钮）。
9. Draft 界面 header 标题项目写了 "Draft"，原版为 `Game mode`——属原版统一头部文案（tutorial.gd 已用 'Game mode' 作参照），应替换。

## 需替换总清单（最终回填 24 处=替换 23 + 补 1）

Draft（20 替换）：`Game mode` / `WELCOME TO THE DRAFT MODE!`（×2）/ `Select your warlord, build your deck from the draft options available, and face other players with it!`（×2）/ `Try to win as many battles as possible! If you are defeated 3 times, your run will end.`（补 Description 1 另计）/ `Locked. Win one battle to enter.` / `Free` / `Available in` / `Select Warlord` / `REROLL` / `Choose cards to add to your deck` / `Reroll packs:` / `Draft Mode` / `Victories:` / `Defeats:` / `Battle!` / `Collect reward` / `Join an alliance to gain additional rewards`
补（Draft Pay Description 1 + Daily Streak 成功态 Info）
Rate（1 替换）：`Please share your thoughts before entering the battlefield.` + `How would you rate the game so far?`（<br>→\n）
Daily Streak（1 替换 1 补）：`Log in daily and keep your streak going to unlock bigger rewards. Skip a day, and your streak resets.`（失败态替换 + 成功态补）
Draft Expiring：无（2 处缺失标注：`Alliance Name:` 标签）。

## 待办辅助信息
- 辅助脚本（临时）：`d:/2/Warpforge_tools/scripts/_tmp_ca_fulltext.py`（根 GO 走树输出完整 m_text；4 界面 4 次调用已覆盖；可复用或删除）。
