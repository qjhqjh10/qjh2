# -*- coding: utf-8 -*-
"""批量替换剩余界面中文 UI -> 英文 (引号内替换, 长串优先)"""
import io
import re

# 长字符串优先映射 (跨文件通用 UI 词)
MAP = [
 # 组合/句子级
 ('每日奖励', 'Daily Rewards'),
 ('连续 7 天', '7-day streak'),
 ('每日刷新', 'Resets daily'),
 ('查看任务', 'Missions'),
 ('查看奖励', 'Rewards'),
 ('开始对战', 'Start Battle'),
 ('返回主菜单', 'Main Menu'),
 ('选择阵营', 'Choose Faction'),
 ('我的卡组', 'My Deck'),
 ('选择督军', 'Choose Warlord'),
 ('请先选择督军', 'Choose a warlord first'),
 ('单机复刻版', 'single-player build'),
 ('卡组为空', 'Deck is empty'),
 ('卡组内容', 'Deck Contents'),
 ('卡组已满', 'Deck is full'),
 ('卡组已保存', 'Deck saved'),
 ('保存失败', 'Save failed'),
 ('未选择督军', 'No warlord chosen'),
 ('卡组需 30 张', 'Deck needs 30 cards'),
 ('没有卡组', 'No decks yet'),
 ('创建你的第一个卡组', 'build your first deck'),
 ('卡牌详情', 'card details'),
 ('成员列表', 'Member List'),
 ('联盟分数', 'Alliance Score'),
 ('创建联盟', 'Create Alliance'),
 ('联盟频道', 'Alliance'),
 ('全球频道', 'Global'),
 ('输入消息', 'Type a message'),
 ('发送', 'Send'),
 ('点击改名', 'Rename'),
 ('收件箱', 'Inbox'),
 # 单词级
 ('关闭', 'Close'),
 ('取消', 'Cancel'),
 ('删除', 'Delete'),
 ('保存', 'Save'),
 ('设置', 'Settings'),
 ('搜索', 'Search'),
 ('确认', 'Confirm'),
 ('继续', 'Continue'),
 ('开始', 'Start'),
 ('返回', 'Back'),
 ('卡包', 'Pack'),
 ('商店', 'Shop'),
 ('战役', 'Campaign'),
 ('任务', 'Missions'),
 ('奖励', 'Rewards'),
 ('成就', 'Achievements'),
 ('排位', 'Ranked'),
 ('宝库', 'Vault'),
 ('熔炉', 'Forge'),
 ('联盟', 'Alliance'),
 ('好友', 'Friends'),
 ('成员', 'Members'),
 ('卡组', 'Deck'),
 ('卡牌', 'Card'),
 ('卡片', 'Card'),
 ('督军', 'Warlord'),
 ('阵营', 'Faction'),
 ('金币', 'Gold'),
 ('能量', 'Energy'),
 ('费用', 'Cost'),
 ('近战', 'Melee'),
 ('远程', 'Ranged'),
 ('生命', 'Health'),
 ('护甲', 'Armour'),
 ('关键词', 'Keywords'),
 ('效果', 'Effect'),
 ('稀有度', 'Rarity'),
 ('传说', 'Legendary'),
 ('史诗', 'Epic'),
 ('稀有', 'Rare'),
 ('普通', 'Common'),
 ('特殊', 'Special'),
 ('胜利', 'Victory'),
 ('失败', 'Defeat'),
 ('再来一局', 'Play Again'),
 ('跳过', 'Skip'),
 ('兑换', 'Claim'),
 ('收集', 'Collected'),
 ('解锁', 'Unlock'),
 ('查看', 'View'),
 ('选择', 'Select'),
 ('显示', 'Show'),
 ('隐藏', 'Hide'),
 ('最大', 'Max'),
 ('最小', 'Min'),
 ('退出', 'Quit'),
 ('暂停', 'Pause'),
 ('播放', 'Play'),
 ('停止', 'Stop'),
 ('已收集', 'Collected'),
 ('保底', 'Pity'),
 ('开包', 'Open Pack'),
 ('宝箱', 'Crate'),
 ('门票', 'Ticket'),
 ('物品', 'Item'),
 ('制作', 'Craft'),
 ('复制', 'Duplicate'),
 ('分享', 'Share'),
 ('导入', 'Import'),
 ('导出', 'Export'),
 ('编辑', 'Edit'),
 ('名称', 'Name'),
 ('标题', 'Title'),
 ('提示', 'Hint'),
 ('信息', 'Info'),
 ('错误', 'Error'),
 ('欢迎', 'Welcome'),
 ('帮助', 'Help'),
 ('关于', 'About'),
 ('版本', 'Version'),
 ('声音', 'Sound'),
 ('音量', 'Volume'),
 ('画质', 'Quality'),
 ('语言', 'Language'),
 ('账号', 'Account'),
 ('资料', 'Profile'),
 ('头像', 'Avatar'),
 ('名字', 'Name'),
 ('等级', 'Level'),
 ('段位', 'Rank'),
 ('胜场', 'Wins'),
 ('败场', 'Losses'),
 ('回合', 'Turn'),
 ('手牌', 'Hand'),
 ('牌库', 'Deck'),
 ('墓地', 'Graveyard'),
 ('坟场', 'Cemetery'),
 ('骷髅', 'Skulls'),
 ('行动', 'Action'),
 ('攻击', 'Attack'),
 ('防御', 'Defence'),
 ('部署', 'Deploy'),
 ('战术', 'Tactic'),
 ('单位', 'Unit'),
 ('玩家', 'Player'),
 ('敌方', 'Enemy'),
 ('我方', 'Your'),
 ('系统', 'System'),
 ('聊天', 'Chat'),
 ('活动', 'Event'),
 ('连胜', 'Streak'),
 ('邀请', 'Invite'),
 ('接受', 'Accept'),
 ('拒绝', 'Decline'),
 ('加入', 'Join'),
 ('离开', 'Leave'),
 ('刷新', 'Refresh'),
 ('加载', 'Loading'),
 ('完成', 'Done'),
 ('成功', 'Success'),
 ('失败', 'Failed'),
 ('在线', 'Online'),
 ('离线', 'Offline'),
 ('好友请求', 'Friend Request'),
 ('添加好友', 'Add Friend'),
 ('删除好友', 'Remove Friend'),
]

FILES = [
 'draft.gd', 'ranked.gd', 'campaign.gd', 'shop.gd', 'gacha.gd', 'packs.gd',
 'forge.gd', 'settings.gd', 'player_profile.gd', 'quests.gd', 'rewards.gd',
 'social.gd', 'achievements.gd', 'tutorial.gd', 'cosmetics.gd', 'inbox.gd',
 'two_sides_event.gd', 'booster_info_popup.gd', 'choose_name.gd',
 'give_feedback_popup.gd', 'rate_popup.gd', 'base_event_popup.gd',
 'daily_streak_popup.gd', 'offer_popup.gd', 'draft_expiring_popup.gd',
 'loading.gd', 'toast.gd', 'menu_bg.gd', 'nav_builder.gd',
]

def replace_in_strings(text):
    """只替换双引号字符串内的中文"""
    def repl(m):
        s = m.group(0)
        inner = m.group(1)
        for zh, en in MAP:
            if zh in inner:
                inner = inner.replace(zh, en)
        return '"%s"' % inner
    # 双引号字符串
    text = re.sub(r'"([^"\\]*(?:\\.[^"\\]*)*)"', repl, text)
    return text

total = 0
for f in FILES:
    path = 'd:/warpforge/scripts/' + f
    try:
        s = io.open(path, encoding='utf-8').read()
    except Exception as e:
        print('skip %s: %s' % (f, e))
        continue
    lines = s.split('\n')
    out = []
    n = 0
    for ln in lines:
        st = ln.lstrip()
        if st.startswith('#'):
            out.append(ln)  # 注释不动
            continue
        new = replace_in_strings(ln)
        if new != ln:
            n += 1
        out.append(new)
    io.open(path, 'w', encoding='utf-8', newline='').write('\n'.join(out))
    total += n
    print('%s: %d 行' % (f, n))
print('total %d 行' % total)
