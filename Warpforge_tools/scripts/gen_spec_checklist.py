# -*- coding: utf-8 -*-
"""重新生成说明文件完成清单 (已实现界面标 ✅)"""
import re

with open(r'd:/2/Warpforge_tools/data/ui_layout/菜单全树.md', encoding='utf-8') as f:
    lines = f.readlines()
roots = []
for i, ln in enumerate(lines):
    if ln.startswith('- '):
        roots.append((i + 1, ln.strip()[2:]))

DONE = [
    'Deck Editing Menu', 'Collection Menu Variant', 'Deck info Popup', 'Import Deck Popup',
    'Practice Mode Menu', 'Game mode deck selector', 'Deck Selector Menu Item',
    'Collection Card', 'Collection Cosmetic', 'Profile Cosmetic Tab', 'Achievements Tab',
    'Achievement Container', 'Achievement Type Toggle', 'Item Display Window', 'Card Alternate Art Drawer',
    'Shop Menu Variant', 'Generic Shop Tab', 'Item Shop Tab', 'Daily Shop Tab', 'Gold Tab',
    'Card Shop Tab', 'InApp Shop Container', 'Shop Item Container', 'Cosmetic Item Shop Container',
    'Catalog Item Shop Container', 'Price Display Button',
    'Packs Tab', 'Booster Pack Open Window', 'Prebuilt Pack UI', 'Booster Info Popup',
    'Gacha Tab', 'Gacha Drawer Holder', 'Gacha Reward Claimed',
    'Daily Reward Popup', 'Daily Streak Popup', 'Daily Login Bonus Container',
    'Daily Skulls Mission Container', 'Daily Mission Container', 'Weekly Mission Container',
    'Mission Header', 'Mission Milestones Progress', 'Mission Milestones Step',
    'Weekly Mission Milestone', 'Campaign Tab', 'Campaign Army Selector', 'Campaign Node',
    'Campaign Reward Window', 'Campaign Points Drawer', 'Node Line', 'Mission Progress Bar',
    'Reward Window', 'Reward Display Mission', 'Reward Event Container', 'Base Event Popup',
    'Forge Tab', 'Forge Army Selector', 'Forge Army Item Button', 'Forge Menu Reward Button',
    'Social Submenu Variant', 'Friend Info Item', 'Invitation List Entry', 'Alliance List Entry',
    'AllianceRankingRow', 'Alliance Badge Drawer', 'Alliance Event Score Info',
    'Alliance Event Score Panel', 'Alliance Score Bar Line', 'Alliance Member Entry',
    'Member Options Panel', 'Generic Options Panel', 'Inbox Menu', 'InboxBtn',
    'Ranked Deck Selection', 'SearchingOpponentWindow', 'Ranked Division Info',
    'Ranked Division Change Window', 'Ranked Army Selector', 'RankedSealStep',
    'Ranked Leaderboard Display', 'Rank Points',
    'Main Menu Settings Window', 'Settings Menu Tab Toggle', 'GenericDropdown', 'Checkbox',
    'Orange Tab Toggle', 'ChooseNameWindow', 'GenericPromptWindow', 'LoadingMenu',
    'MessagePopupWindowDuel', 'Give Feedback Popup menu', 'Purchase Premium Window',
    'Player Profile Window', 'Avatar Menu Item', 'Avatar Item Small', 'Player Level',
    'PlayerRankingRow', 'TrophyDisplay', 'Profile Player Info',
    'ChatPanel', 'ChatPreview', 'Main Menu Navigation Button', 'Menu Navigation Panel Button',
    'Battle Log Popup', 'Match Log', 'Base Submenu', 'Rewards Base Submenu Variant',
    'Wildcard Drawer', 'Icon Wildcard Drawer Variant', 'Currency Drawer', 'Icon Currency Drawer Variant',
    'Forge Points Drawer', 'Icon Forge Points Drawer Variant', 'Icon Campaign Points Drawer Variant',
    'Cardback Drawer', 'Avatar Drawer', 'Icon Avatar Drawer Variant', 'Avatar Border Drawer',
    'Icon Avatar Border Drawer Variant', 'Title Drawer', 'Title Drawer Horizontal Variant',
    'Container Drawer', 'Base Drawer', 'Premium Drawer', 'Premium Drawer No Glow',
    'Random Card Drawer', 'Icon Random Card Drawer Variant', 'Card Drawer',
    'Generic Army Item Drawer', 'Generic Multi Card Display', 'Generic Multi Card Display Combat',
    'Card in deck container', 'Draft Mode Card in deck container Variant',
    'Alliance Trophy Info Popup', 'Icon VIP Premium Campaign Drawer Variant',
    'Icon Premium Campaign Drawer Variant', 'RankedClassicLeaderboardPopup Variant',
    'RankedSkirmishLeaderboardPopup', 'Daily Reward Popup Item Drawer', 'Icon Expansion Pass Points Drawer Variant',
]
NOT_DONE = [
    'Tutorial Mode Menu', 'Tutorial Message Window PopUp', 'Tutorial Army Select Button',
    'Choose Army Deck FTUE Window', 'WelcomeScreen Alpha', 'Base Expiration Popup',
    'Liveop Event Help Variant', 'Event Help Popup Variant', 'Event Help Popup Small Image Variant',
    'Full Screen Event Announcement Variant', 'Two Sides Event Window', 'Two Side Event Select Team',
    'Parent Event Window', 'Sunset Popup', 'Draft Mode Menu Demo', 'Draft Mode Ongoing Content',
    'Draft Mode Ongoing State', 'Draft Mode Expiring Popup', 'Draft Mode Timed Mode Window',
    'Draft Mode Deck Info Panel', 'DraftLeaderboardPopup', 'Expansion Pass Tab',
    'Expansion Pass Missions Tab', 'Expansion Pass Progress Bar', 'Expansion Pass Reward Container',
    'Expansion Pass Points Drawer', 'Expansion Pass Premium Drawer', 'Raid Progress Tab',
    'Raid Progress Bar', 'Raid Reward Container', 'EnergySinglePlayerOnlyEventWindow',
    'InApp Shop Container Disabled', 'Webshop Offer Container', 'XSolla Offer Drawer',
    'Referral Container', 'Daily Bonus Shop Container', 'Booster Offer Container', 'Offer Container',
    'Main Menu Offer Container', 'Base Game Mode Container', 'Draft Game Mode Container',
    'Ranked Game Mode Container', 'Skirmish Ranked Game Mode Container',
    'Reward Event Faction Bonus Container', 'Daily Reward Popup Entry', 'Daily Streak Reward Popup Entry',
    'Mission Container Vertical', 'Mission Debug Buttons', 'Placeholder Generic Leaderboard Display',
    'FactionScoreSmall', 'FactionScoreBig', '2Armies Progress Bar',
    'Event Navigation Button', 'Feedback Scoring Button', 'Simple Army Icon',
    'Boosterpack Open Card Rarity', 'RewardAppearParticle', 'Timer',
    'Deck Selector Card Info button', 'Deck Selector Hero Card Info button',
    'Deck Selector Defensive Card Slot', 'Deck CostQuantity Row Drawer', 'Deck Drawer',
    'Card Info Draft Mode button', 'Ranked Boost Reward Event Window', 'Ranked New Season WIndow',
    'Ranked Season Ended Window', 'RankedEventWindow', 'RankedEventWindowV2',
    'SkirmishModeEventWindow', 'AllianceRankingRow Variant', 'Player RankingRow For Army',
    'RankedSealStep Division Change Variant', 'RankedSealStep Animation Disabled',
    'Tooltip trigger', 'Node Line', 'Timer With Time Description', 'Daily Bonus Shop Container',
]

out = []
out.append('# 说明文件完成清单（说明书资源安放核查跟踪）\n')
out.append('> 用户第 4 项指示（2026-08-18）：检查阅读全部说明文件，按里面要求把解包资源逐个安放到位，完成一个打勾。\n')
out.append('> 状态标记：✅=已按说明书实现并验收 | ⏳=已实现但待完善/待核查 | ❌=未实现（运营/教程/特效内容或可选）\n')
out.append('> 说明书来源：`Warpforge_tools/data/ui_layout/菜单全树.md`（313 根界面）等\n')
out.append('\n---\n\n## 一、主菜单场景说明书（主菜单全树.md）\n')
out.append('| 说明书根元素 | 状态 | 实现位置 | 备注 |\n|---|---|---|---|\n')
mainmenu_items = [
    ('Navigation Panel（左侧竖排 5 键）', '✅', 'main_menu.gd _build_navigation / nav_builder.gd', '点击变白已修复 (2026-08-18 半透明高亮)'),
    ('Upper bar（顶栏）', '✅', 'main_menu.gd _build_topbar', '货币 4 项+头像+设置'),
    ('GameModes（中央模式容器区）', '✅', 'main_menu.gd _build_game_modes', '6 卡 1x2 竖卡横排 (2026-08-18 重做)'),
    ('ChatPreview + ChatPanel', '✅', 'main_menu.gd _build_chat_preview', '双频道+消息底纹'),
    ('3-PopUp Holder → Card Displayer', '✅', 'card_displayer', '制作/升级/语音/卡面文字'),
    ('Player Profile Window', '✅', 'player_profile', '6 标签'),
    ('LoadingMenu', '✅', 'loading.gd', ''),
    ('Toast Notification Controller', '✅', 'toast.gd', ''),
    ('TooltipManager', '⏳', '—', '细节提示低优先'),
    ('Campaign Glow', '⏳', '—', '活动辉光'),
    ('UI Error Message Controller', '❌', '—', 'inactive'),
    ('Tutorial highlight', '❌', '—', '随教程'),
]
for row in mainmenu_items:
    out.append('| %s | %s | %s | %s |\n' % row)

out.append('\n## 二、菜单场景说明书（菜单全树.md，313 根界面）\n')
out.append('| # | 界面（说明书行号） | 状态 | 备注 |\n|---|---|---|---|\n')
for no, name in roots:
    if any(k in name for k in DONE):
        st = '✅'
    elif any(k in name for k in NOT_DONE):
        st = '❌'
    else:
        st = '⏳'
    out.append('| %d | %s | %s | |\n' % (no, name, st))

out.append('\n## 三、对战场景说明书（battlearena1 全树.md）\n')
out.append('| 说明书元素 | 状态 | 实现位置 | 备注 |\n|---|---|---|---|\n')
battle_items = [
    ('Mulligan 换牌界面', '✅', 'battle.gd', '(1063,922) Continue'),
    ('敌方手牌区顶部 (910,50)', '✅', 'battle.gd', ''),
    ('攻击选择器三键', '✅', 'battle.gd', 'Melee/Ranged 贴图'),
    ('EnemyInfo/PlayerInfo 玩家框+圆形督军头像', '✅', 'battle.gd（2026-08-18 补头像）', 'Avatar Item Small 结构: 立绘圆裁+金属圆环'),
    ('ShowCemeteryBtn 坟场按钮 (52,136)', '✅', 'battle.gd（2026-08-18 归位）', '原 (330,178) 错误已修正'),
    ('Energy And turn holder 右侧纵向', '✅', 'battle.gd', ''),
    ('PlayerDeck/EnemyDeck 牌库', '✅', 'battle.gd', ''),
    ('CardsInHandText 手牌数条', '✅', 'battle.gd', '40K_display'),
    ('Card Display 双击详情', '✅', 'battle.gd', ''),
    ('Skull 骷髅', '✅', 'battle.gd', '40k_battle_Win Skull'),
    ('Battle Log Popup', '✅', 'battle.gd', ''),
    ('3D 战场', '✅', 'battle.gd _build_3d_world/_update_3d_cards', ''),
    ('语音按钮 40k_voicelines_bt_L/R', '⏳', '—', '已提取未接线'),
    ('BattleHud 开场动画/牌库滑入', '⏳', '—', ''),
    ('卡牌拖拽交互', '⏳', '—', '当前点击选目标'),
]
for row in battle_items:
    out.append('| %s | %s | %s | %s |\n' % row)

out.append('\n## 四、卡组界面说明书（卡组界面说明书.md）\n')
out.append('| 界面 | 状态 | 备注 |\n|---|---|---|\n')
for row in [
    ('Collection Menu Variant（卡组集合）', '✅', 'deck_collection.gd（2026-08-18 改玩家自建卡组，不展示模板）'),
    ('Deck Editing Menu（卡组组建）', '✅', 'deck_builder.gd'),
    ('Deck info Popup', '✅', 'deck_info_popup.gd'),
    ('Import Deck Popup', '✅', 'import_deck_popup.gd'),
    ('Practice Mode Menu（模式选择）', '✅', 'mode_select.gd'),
    ('Deck Selection Popup with Tabs', '⏳', '可选'),
    ('Deck Selection Popup', '⏳', '可选'),
]:
    out.append('| %s | %s | %s |\n' % row)

with open(r'd:/2/说明文件完成清单.md', 'w', encoding='utf-8') as f:
    f.writelines(out)
done_c = sum(1 for _, n in roots if any(k in n for k in DONE))
not_c = sum(1 for _, n in roots if any(k in n for k in NOT_DONE))
print('DONE', done_c, 'NOT_DONE', not_c, 'TODO', len(roots) - done_c - not_c)
