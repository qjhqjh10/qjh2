# -*- coding: utf-8 -*-
"""混合串英文化第三批: gacha/packs/social/tutorial/card_displayer/loading/offer_popup/choose_name/daily_streak/booster_info"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

MAP = {
    r'd:\warpforge\scripts\gacha.gd': {
        '"结束于:"': '"Ends in:"',
        '"19天 15小时"': '"19d 15h"',
        '"获得: %s ×%d"': '"Reward: %s x%d"',
    },
    r'd:\warpforge\scripts\packs.gd': {
        '"500 Gold一包 · 5 张随机卡"': '"500 Gold per pack · 5 random cards"',
        '"5 张随机卡"': '"5 random cards"',
        '"Gold不足!"': '"Not enough Gold!"',
    },
    r'd:\warpforge\scripts\social.gd': {
        '"No Alliance\\nCreate or join an Alliance to earn Event得分"':
            '"No Alliance\\nCreate or join an Alliance to earn Event points"',
        '"已添加Friends: "': '"Friends added: "',
        '"ViewProfile (单机占位)"': '"View Profile (offline placeholder)"',
        '"升职"': '"Promote"',
        '"已提升职级"': '"Promoted"',
        '"降职"': '"Demote"',
        '"已降低职级"': '"Demoted"',
        '"踢出Alliance"': '"Kick from Alliance"',
        '"已踢出 (单机演示)"': '"Kicked (offline demo)"',
        '"输入AllianceName..."': '"Enter alliance name..."',
        '"创建"': '"Create"',
        '"请输入AllianceName"': '"Enter an alliance name"',
        '"Gold不足 (需要 1000)"': '"Not enough Gold (need 1000)"',
        '"指挥官"': '"Commander"',
        '"Alliance之主"': '"Alliance Leader"',
        '"AI 副官"': '"AI Officer"',
        '"副盟主"': '"Vice Leader"',
        '"AI 战士"': '"AI Warrior"',
        '"Alliance创建Success!"': '"Alliance created successfully!"',
        '"单机版Friends为本地记录 · 原版为OnlineFriendsSystem"':
            '"Friends are local records in this offline build · original uses an online friends system"',
        '"输入FriendsName..."': '"Enter friend name..."',
        '"添加Friends"': '"Add Friend"',
        '"暂无Friends\\n添加Friends后Show在这里"': '"No friends yet\\nfriends added will show here"',
        '"Join于 %s"': '"Joined %s"',
        '"挑战"': '"Challenge"',
    },
    r'd:\warpforge\scripts\tutorial.gd': {
        '"Start学习！与你的连长进行演练。DeployUnit、Attack敌人、赢得战斗。"':
            '"Start learning! Train with your Captain. Deploy units, attack enemies, win battles."',
        '"了解Energy、Cost与Card类型。掌握出牌的节奏。"':
            '"Learn about Energy, Cost and card types. Master the rhythm of play."',
        '"Melee与RangedAttack的区别，以及Armour与Keywords。"':
            '"The difference between Melee and Ranged attacks, plus Armour and Keywords."',
        '"使用Tactic卡扭转战局。Deploy、增益、伤害一应俱全。"':
            '"Turn the tide with Tactic cards - deploy, buff and damage in one."',
        '"Warlord是你的主将。保护他，同时用他的天赋卡发起进攻。"':
            '"The Warlord is your champion. Protect him while striking with his Talent cards."',
        '"集齐Skulls、击败EnemyWarlord、赢得Victory！"':
            '"Gather Skulls, defeat the enemy Warlord, claim Victory!"',
        '"第 %d 关  %s"': '"Stage %d  %s"',
    },
    r'd:\warpforge\scripts\card_displayer.gd': {
        '"语音"': '"Voice"',
        '"卡面文字"': '"Card text"',
        '"费用 %s    近战 %s    远程 %s    生命 %s"':
            '"Cost %s    Melee %s    Ranged %s    Health %s"',
        '"关键词: %s"': '"Keywords: %s"',
        '"副标题: %s"': '"Subtitle: %s"',
        '"类型:%s · %s"': '"Type: %s · %s"',
        '"制作副本"': '"Craft Copy"',
        '"升级"': '"Upgrade"',
        '"替换样式"': '"Swap Style"',
        '"当前样式: 原版完整卡面"': '"Current style: original full card art"',
        '"上一个样式"': '"Previous style"',
        '"下一个样式"': '"Next style"',
        '"原版样式已拥有"': '"Original style owned"',
        '"制作副本 · 需要 %d 张%s通配符"': '"Craft copy · needs %d %s Wildcard(s)"',
        '"该卡已达最高等级"': '"Card is at max level"',
        '"升级到等级 %d"': '"Upgrade to level %d"',
        '"当前等级 %d · 升级后解锁更高稀有度卡框"': '"Level %d · upgrade unlocks higher-rarity frame"',
        '"稀有"': '"Rare"',
        '"史诗"': '"Epic"',
        '"传说"': '"Legendary"',
        '"普通"': '"Common"',
        '"通配符不足: 需要 1 张%s通配符"': '"Not enough Wildcards: need 1 %s Wildcard"',
        '"制作成功! 副本数 %d"': '"Crafted! Copies: %d"',
        '"已达最高等级"': '"Already at max level"',
        '"该卡暂无语音"': '"No voice for this card"',
        '"语音文件缺失"': '"Voice file missing"',
    },
    r'd:\warpforge\scripts\loading.gd': {
        '"Loading中..."': '"Loading..."',
    },
    r'd:\warpforge\scripts\offer_popup.gd': {
        '"购买"': '"Buy"',
    },
    r'd:\warpforge\scripts\choose_name.gd': {
        '"Welcome来到 WARHAMMER 40,000: WARPFORGE!"': '"Welcome to WARHAMMER 40,000: WARPFORGE!"',
        '"Select你的PlayerName"': '"Select your Player Name"',
        '"输入PlayerName"': '"Enter Player Name"',
        '"single-player build · 无需登录"': '"single-player build · no login required"',
        '"指挥官"': '"Commander"',
    },
    r'd:\warpforge\scripts\daily_streak_popup.gd': {
        '"Daily Streak 每日Streak"': '"Daily Streak"',
        '"每天登录保持Streak，获得更多Rewards"':
            '"Log in daily to keep your streak and earn more rewards"',
        '"未Unlock"': '"Locked"',
    },
    r'd:\warpforge\scripts\booster_info_popup.gd': {
        '"每开启 1 包，「距上次Legendary卡」计数 +1。\\n\\n最多 200 包必出Legendary（Pity）。\\n\\n开出Legendary卡后计数重置为 0，重新累计。\\n\\nRarity权重：Common 60% / Rare 25% / Epic 10% / Legendary 5%。"':
            '"Each pack opened adds +1 to the \\"packs since last Legendary\\" counter.\\n\\nA Legendary is guaranteed within 200 packs (pity).\\n\\nDrawing a Legendary resets the counter to 0.\\n\\nRarity weights: Common 60% / Rare 25% / Epic 10% / Legendary 5%."',
        '"自上次LegendaryPack已开启 %d 包"': '"Packs opened since last Legendary: %d"',
        '"Open Pack累计 200 次未出Legendary时, 下一次必出Legendary"':
            '"After 200 packs without a Legendary, the next pack is guaranteed Legendary"',
    },
}

total = 0
for fp, pairs in MAP.items():
    txt = open(fp, encoding='utf-8').read()
    n = 0
    for old, new in pairs.items():
        if old in txt:
            txt = txt.replace(old, new)
            n += 1
        else:
            print(f'  !! 未找到: {fp} :: {old[:50]}')
    open(fp, 'w', encoding='utf-8').write(txt)
    total += n
    print(f'{fp.split(chr(92))[-1]}: 替换 {n}/{len(pairs)}')
print('共', total)
