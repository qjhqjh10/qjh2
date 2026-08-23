# -*- coding: utf-8 -*-
"""混合串英文化第四批: two_sides_event/base_event_popup/give_feedback/rate_popup/draft_expiring"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

MAP = {
    r'd:\warpforge\scripts\two_sides_event.gd': {
        '"Blue Team 蓝色小队"': '"Blue Team"',
        '"Red Team 红色小队"': '"Red Team"',
        '"Select你的Faction。在Event期间赢得对战CollectedSkulls，为你的Faction贡献分数，\\n达到里程碑即可领取CrateRewards！"':
            '"Select your Faction. Win battles during the Event to collect Skulls and score points for your Faction,\\nclaim Crate Rewards at milestones!"',
        '"Select Select此Faction"': '"Select this Faction"',
        '"Game mode 双边事件"': '"Game mode: Two Sides Event"',
        '"Progression Event进度"': '"Progression Event"',
        '"在对战中CollectedSkulls为Faction贡献分数\\n达到里程碑领取CrateRewards"':
            '"Collect Skulls in battles to score points for your Faction\\nclaim Crate Rewards at milestones"',
        '"Collect 领取"': '"Collect"',
        '"已领取Crate %d: Gold +%d · %s 通配符 x%d"':
            '"Claimed Crate %d: Gold +%d · %s Wildcard x%d"',
        '"尚未达到下一个Crate里程碑 (Skulls %d)"':
            '"Next Crate milestone not reached yet (Skulls %d)"',
    },
    r'd:\warpforge\scripts\base_event_popup.gd': {
        '"Welcome来到战锤 40K Warpforge 的single-player build！\\n\\nCollectedCard、组建Deck、DoneCampaign、参与Event。\\n\\n点击ContinueStart你的征程！"':
            '"Welcome to the single-player build of Warhammer 40K Warpforge!\\n\\nCollect cards, build Decks, finish the Campaign, join Events.\\n\\nClick Continue to start your journey!"',
        '"Clique para continuar 点击Continue"': '"Click to continue"',
    },
    r'd:\warpforge\scripts\give_feedback_popup.gd': {
        '"年龄组"': '"Age Group"',
        '"18 岁以下"': '"Under 18"',
        '"18-25 岁"': '"18-25"',
        '"26-35 岁"': '"26-35"',
        '"35 岁以上"': '"35+"',
        '"游戏偏好"': '"Game Preferences"',
        '"Card对战"': '"Card Battles"',
        '"策略Collected"': '"Strategy & Collection"',
        '"剧情Campaign"': '"Story Campaign"',
        '"Ranked竞技"': '"Ranked Competition"',
        '"体验评价"': '"Overall Experience"',
        '"非常好"': '"Excellent"',
        '"还不错"': '"Good"',
        '"一般"': '"Average"',
        '"有待改进"': '"Needs Work"',
        '"最想增加"': '"Most Wanted"',
        '"更多Faction"': '"More Factions"',
        '"Online对战"': '"Online Battles"',
        '"更丰富Event"': '"More Events"',
        '"更多Card"': '"More Cards"',
        '"Done这份问卷只需不到两分钟，Help我们做得更好！"':
            '"This survey takes under two minutes and helps us improve!"',
        '"自由反馈 (280/500 字)"': '"Free feedback (280/500 chars)"',
        '"Submit 提交反馈"': '"Submit Feedback"',
        '"感谢你的反馈，已提交！"': '"Thanks for your feedback - submitted!"',
    },
    r'd:\warpforge\scripts\rate_popup.gd': {
        '"请Share你对这款游戏的看法。\\n\\n你的评分会Help我们做得更好！\\n\\n\\n★ 1-4 星：遇到问题或建议\\n★ 5 星：支持我们Continue开发"':
            '"Please share your thoughts on the game.\\n\\nYour rating helps us improve!\\n\\n\\n★ 1-4 stars: issues or suggestions\\n★ 5 stars: support us to keep developing"',
        '"感谢你的反馈！我们会Continue改进"': '"Thanks for your feedback! We will keep improving"',
        '"感谢你的五星好评！为了帝皇！"': '"Thanks for the five stars! For the Emperor!"',
    },
    r'd:\warpforge\scripts\draft_expiring_popup.gd': {
        '"选秀模式Event已结束！"': '"The Draft Event has ended!"',
        '"Alliance: 无 (单机版)"': '"Alliance: none (offline build)"',
        '"Leaderboard 排行榜"': '"Leaderboard"',
        '"单机版无选秀排行榜"': '"No Draft leaderboard in this offline build"',
        '"Tap to continue 点击Continue"': '"Tap to continue"',
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
