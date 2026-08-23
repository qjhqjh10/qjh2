# -*- coding: utf-8 -*-
"""混合串英文化第二批: rewards/campaign/achievements/where_cards_popup/inbox/cosmetics"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

MAP = {
    r'd:\warpforge\scripts\rewards.gd': {
        '"第 1 天"': '"Day 1"', '"第 2 天"': '"Day 2"', '"第 3 天"': '"Day 3"',
        '"第 4 天"': '"Day 4"', '"第 5 天"': '"Day 5"', '"第 6 天"': '"Day 6"',
        '"第 7 天"': '"Day 7"',
        '"Resets daily · 今天第 %d 天"': '"Resets daily · Day %d"',
        '"高级: "': '"Premium: "',
        '"✓ 已领取"': '"✓ Claimed"',
        '"领取"': '"Claim"',
        '"未Unlock"': '"Locked"',
        '"已领取: %s"': '"Claimed: %s"',
    },
    r'd:\warpforge\scripts\campaign.gd': {
        '"起点"': '"Start"', '"终点"': '"Finish"', '"起"': '"Start"',
        '"领取节点Rewards"': '"Claim node rewards"',
        '"终点: Legendary通配符 x2 + Gold 1000"': '"Finish: Legendary Wildcard x2 + Gold 1000"',
        '"已领取终点Rewards: Legendary通配符 x2 + 1000 Gold!"':
            '"Claimed finish rewards: Legendary Wildcard x2 + 1000 Gold!"',
        '"该节点已领取"': '"Node already claimed"',
        '"已领取 %s 节点Rewards!"': '"Claimed %s node rewards!"',
        '"领取终点Rewards"': '"Claim finish rewards"',
        '"终点已领取"': '"Finish claimed"',
        '"节点已领取"': '"Node claimed"',
        '"当前节点: %s"': '"Current node: %s"',
    },
    r'd:\warpforge\scripts\achievements.gd': {
        '"初战告捷"': '"First Victory"',
        '"赢得第一场对战"': '"Win your first battle"',
        '"赢得 5 场对战"': '"Win 5 battles"',
        '"赢得 50 场对战"': '"Win 50 battles"',
        '"杀戮机器"': '"Killing Machine"',
        '"累计击杀 100 Skulls"': '"Kill 100 Skulls total"',
        '"战功赫赫"': '"War Hero"',
        '"累计击杀 500 Skulls"': '"Kill 500 Skulls total"',
        '"收藏家"': '"Collector"',
        '"Collected 500 张Card"': '"Collect 500 cards"',
        '"图鉴全开"': '"Complete Collection"',
        '"Collected全部 1193 张Card"': '"Collect all 1193 cards"',
        '"通配符猎人"': '"Wildcard Hunter"',
        '"累计持有 50 张通配符"': '"Hold 50 Wildcards"',
        '"升级达人"': '"Upgrade Master"',
        '"升级Card 10 次"': '"Upgrade cards 10 times"',
        '"Legendary铸造师"': '"Legendary Forger"',
        '"升级 3 张Legendary卡"': '"Upgrade 3 Legendary cards"',
        '"Campaign先锋"': '"Campaign Pioneer"',
        '"Campaign推进 5 节点"': '"Advance 5 Campaign nodes"',
        '"Campaign征服者"': '"Campaign Conqueror"',
        '"Done全部Campaign轨道"': '"Complete all Campaign tracks"',
        '"财富积累"': '"Fortune Builder"',
        '"累计持有 10000 Gold"': '"Hold 10000 Gold"',
        '"Deck大师"': '"Deck Master"',
        '"组建 5 套Deck"': '"Build 5 Decks"',
        '"全部进度来自真实游戏数据"': '"All progress from real game data"',
        '"全部"': '"All"', '"战斗"': '"Battle"', '"升级"': '"Upgrade"', '"经济"': '"Economy"',
        '"+%d 点"': '"+%d pts"',
    },
    r'd:\warpforge\scripts\where_cards_popup.gd': {
        '"Booster packs 卡包开包"': '"Booster Packs"',
        '"在「开包」界面花费 500 金币开启阵营卡包，每包随机 5 张卡。\\n稀有度权重：普通 60% / 稀有 25% / 史诗 10% / 传说 5%，每 200 包保底传说。"':
            '"Open faction packs in the Packs screen for 500 Gold, 5 random cards each.\\nRarity weights: Common 60% / Rare 25% / Epic 10% / Legendary 5%, pity Legendary every 200 packs."',
        '"Campaign 战役奖励"': '"Campaign Rewards"',
        '"在「战役」界面推进轨道节点：每赢一场对战前进 1 节点，\\n节点可领取通配符/金币奖励，终点可领传说通配符。"':
            '"Advance along the Campaign track: win a battle to move 1 node,\\nclaim Wildcard/Gold rewards at nodes, Legendary Wildcard at the finish."',
        '"Shop 商店购买"': '"Shop Purchases"',
        '"在「商店」购买阵营卡包（150 金币/包）或资源包，\\n通配符包直接入库存，可用于制作卡牌副本。"':
            '"Buy faction packs (150 Gold) or resource packs in the Shop;\\nWildcard packs go straight to inventory for crafting copies."',
        '"Crafting 制作系统"': '"Crafting"',
        '"在卡牌详情弹窗中使用通配符制作副本：\\n普通 x1 / 稀有 x3 / 史诗 x5 / 传说 x10（各阵营通配符通用）。"':
            '"Craft copies in the card detail popup using Wildcards:\\nCommon x1 / Rare x3 / Epic x5 / Legendary x10 (any faction Wildcard works)."',
        '"Daily Rewards 每日奖励"': '"Daily Rewards"',
        '"在「奖励」界面每日登录领取连续 7 天奖励，\\n包含金币与各稀有度通配符，断签后从第 1 天重新累计。"':
            '"Log in daily on the Rewards screen for a 7-day streak,\\nGold and Wildcards of each rarity; streak resets after a missed day."',
        '"关闭"': '"Close"',
    },
    r'd:\warpforge\scripts\inbox.gd': {
        '"原版公告横幅：%s\\n单机版展示解包资源，点击View详情。"':
            '"Original announcement banner: %s\\noffline build shows unpacked resources, click to view details."',
    },
    r'd:\warpforge\scripts\cosmetics.gd': {
        '"美容品 · 卡背"': '"Cosmetics · Card Backs"',
        '"Select卡背 · 对战中Hand/棋盘卡背生效 · %d 款"':
            '"Select a card back · applied to your hand/board in battle · %d styles"',
        '"当前卡背"': '"Current Card Back"',
        '"使用此卡背"': '"Use This Card Back"',
        '"卡背已应用!"': '"Card back applied!"',
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
            print(f'  !! 未找到: {fp} :: {old[:40]}')
    open(fp, 'w', encoding='utf-8').write(txt)
    total += n
    print(f'{fp.split(chr(92))[-1]}: 替换 {n}/{len(pairs)}')
print('共', total)
