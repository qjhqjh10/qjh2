# -*- coding: utf-8 -*-
"""混合串英文化: settings.gd / quests.gd (引号内用户可见中文 → 英文)"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

MAP = {
    r'd:\warpforge\scripts\settings.gd': {
        '"禁用机器人"': '"Disable Bots"',
        '"禁用通知"': '"Disable Notifications"',
        '"触屏输入"': '"Touch Input"',
        '"单机版无Claim码System"': '"No claim code system in this offline build"',
        '"音乐Volume"': '"Music Volume"',
        '"音效Volume"': '"SFX Volume"',
        '"语音Volume"': '"Voice Volume"',
        '"窗口模式"': '"Window Mode"',
        '"全屏"': '"Fullscreen"',
        '"窗口"': '"Windowed"',
        '"Max化"': '"Maximized"',
        '"指挥官"': '"Commander"',
        '"Player名: %s"': '"Player name: %s"',
        '"单机版无需AccountSystem\\n原版Account功能 (登录/绑定/Shop云同步) 在此Version中由本地存档代替"':
            '"Offline build: no Account System\\n(login/linking/shop sync) replaced by local save"',
        '"本地存档: user://profile.json (Gold/通配符/Avatar/称号/Settings)"':
            '"Local save: user://profile.json (Gold/Wildcards/Avatar/Title/Settings)"',
        '"无限"': '"Unlimited"',
        '"Quality档位"': '"Quality Preset"',
        '"低"': '"Low"',
        '"中"': '"Medium"',
        '"高"': '"High"',
        '"极高"': '"Ultra"',
        '"Hand文字大小"': '"Hand Text Size"',
        '"小"': '"Small"',
        '"中"': '"Medium"',
        '"大"': '"Large"',
        '"About游戏的问题? 请View常见问题解答"': '"Questions about the game? View the FAQ"',
        '"FAQ: 请参阅文档目录"': '"FAQ: see the docs folder"',
        '"需要Help? 请联系我们"': '"Need help? Contact us"',
        '"单机版无Online客服"': '"Offline build: no online support"',
        '"单机版支持: 见项目文档"': '"Offline build support: see project docs"',
        '"游戏体验反馈?"': '"Game feedback?"',
        '"Give Feedback 反馈问卷"': '"Give Feedback survey"',
        '"Rate 评分"': '"Rate the game"',
        '"原版游戏由 Everguild 开发 · 本复刻仅供学习研究使用"':
            '"Original game by Everguild · this recreation is for study only"',
    },
    r'd:\warpforge\scripts\quests.gd': {
        '"每日Skulls"': '"Daily Skulls"',
        '"累计击杀Skulls (每日重置)"': '"Kill Skulls (daily reset)"',
        '"Common通配符"': '"Common Wildcard"',
        '"Rare通配符"': '"Rare Wildcard"',
        '"Epic通配符"': '"Epic Wildcard"',
        '"Legendary通配符"': '"Legendary Wildcard"',
        '"Victory之路"': '"Path of Victory"',
        '"赢得对战 (累计)"': '"Wins (cumulative)"',
        '"收藏家"': '"Collector"',
        '"CollectedCard (图鉴总数)"': '"Cards collected (collection total)"',
        '"赢得对战 (周常挑战)"': '"Wins (weekly challenge)"',
        '"每日Missions · 每日重置 · 进度来自真实对战记录"':
            '"Daily Missions · reset daily · progress from real matches"',
        '"Weekly Challenge 周常挑战"': '"Weekly Challenge"',
    },
}

for fp, pairs in MAP.items():
    txt = open(fp, encoding='utf-8').read()
    n = 0
    for old, new in pairs.items():
        if old in txt:
            txt = txt.replace(old, new)
            n += 1
        else:
            print(f'  !! 未找到: {fp} :: {old}')
    open(fp, 'w', encoding='utf-8').write(txt)
    print(f'{fp}: 替换 {n}/{len(pairs)}')
