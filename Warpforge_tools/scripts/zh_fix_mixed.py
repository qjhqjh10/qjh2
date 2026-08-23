# -*- coding: utf-8 -*-
"""修复半替换混合串 -> 完整英文 (第二批)"""
import io

MAPS = {
'd:/warpforge/scripts/draft.gd': [
 ('"选秀模式"', '"Draft"'),
 ('"Welcome来到选秀模式!"', '"Welcome to Draft!"'),
 ('"Select你的Warlord，组建Deck，赢下尽可能多的对战！"', '"Select your Warlord, build a Deck, and win as many battles as you can!"'),
 ('"12 胜或 3 败后结算Rewards · 每场对局可Continue"', '"12 wins or 3 losses to settle Rewards - every match can continue"'),
 ('"Hint：Done一局对战即可进入"', '"Hint: complete one battle to enter"'),
 ('"结束于: 23天 5小时"', '"Ends in: 23d 5h"'),
 ('"免费入场"', '"Free Entry"'),
 ('"立即可玩"', '"Playable now"'),
 ('"换一批"', '"Reroll"'),
 ('"SelectCardJoin你的Deck"', '"Select cards to join your Deck"'),
 ('"重掷Pack"', '"Reroll Pack"'),
 ('"重掷Pack:"', '"Reroll Pack:"'),
 ('"选这张"', '"Select"'),
 ('"放弃"', '"Abandon"'),
 ('"领取Rew', '"Claim Rew'),
 ('"Energy曲线"', '"Energy Curve"'),
 ('"JoinAlliance可获得额外Rewards"', '"Join an Alliance for extra Rewards"'),
 ('_toast("先DonePackSelect")', '_toast("Finish pack selection first")'),
 ('"name": "选秀Deck",', '"name": "Draft Deck",'),
 ('btn.text = "领取Rewards"', 'btn.text = "Claim Rewards"'),
 ('_toast("已领取选秀Rewards: Common通配符×5 + Rare×%d" % max(0, _wins / 3))', '_toast("Draft rewards claimed: Common wildcards x5 + Rare x%d" % max(0, _wins / 3))'),
],
'd:/warpforge/scripts/ranked.gd': [
 ('"排行榜"', '"Leaderboard"'),
 ('"当前Rank"', '"Current Rank"'),
 ('TooltipManager.show_tooltip("Rank", "Ranked分决定Rank: 1000 起\\n1250+ Division IV ·', 'TooltipManager.show_tooltip("Rank", "Ranked score determines Rank: starts at 1000\\n1250+ Division IV -'),
 ('var deck_name := "未命名Deck"', 'var deck_name := "Unnamed Deck"'),
 ('["上一个Deck", "更换Deck", "ViewDeck", "下一个Deck"][i]', '["Previous Deck", "Change Deck", "View Deck", "Next Deck"][i]'),
 ('"单机版仅一个PlayerDeck"', '"Single-player has one Player Deck"'),
 ('"更换Deck: 请前往收藏-Deck界面"', '"Change Deck: visit Collection - Deck"'),
 ('"暂无Deck"', '"No Deck"'),
 ('"Deck (%d 张) · View详情请前往收藏-Deck"', '"Deck (%d cards) - view details in Collection - Deck"'),
 ('"正在Search对手..."', '"Searching for opponent..."'),
 ('_rating_label.text = "Ranked分: %d" % _rating', '_rating_label.text = "Ranked score: %d" % _rating'),
 ('"上一赛季" if _lb_season == 0 else "当前赛季"', '"Last Season" if _lb_season == 0 else "Current Season"'),
 ('"结束于: 23天 5小时"', '"Ends in: 23d 5h"'),
 ('var my_name := str(_profile.get("playerName", "指挥官"))', 'var my_name := str(_profile.get("playerName", "Commander"))'),
 ('"Ranked分"', '"Ranked Score"'),
 ('"（你）"', '"(you)"'),
],
'd:/warpforge/scripts/shop.gd': [
 ('["cosmetics", "美容品"', '["cosmetics", "Cosmetics"'),
 ('["resources", "资源"', '["resources", "Resources"'),
 ('var box := _make_pack_item("包_" + fname, "「%s」Pack" % faction.get("cn", fname),', 'var box := _make_pack_item("Pack_" + fname, "%s Pack" % faction.get("name", fname),'),
 ('["新手礼包", 300, _on_buy_pack.bind("新手礼包", 300)],', '["Starter Pack", 300, _on_buy_pack.bind("Starter Pack", 300)],'),
 ('_flash("Gold不足!")', '_flash("Not enough Gold!")'),
 ('inst.setup("「%s」Pack" % fname, "FactionPack", "500 金币一包', 'inst.setup("%s Pack" % fname, "FactionPack", "500 Gold per pack'),
 ('5 张随机卡（稀有度权重）', '5 random cards (rarity weighted)'),
 ('开包动画 + 通配符入库存", TEX_CRATE, price,', 'open animation + wildcards to inventory", TEX_CRATE, price,'),
 ('_make_label(tab, "美容品 · 卡背/Avatar/称号"', '_make_label(tab, "Cosmetics - Cardbacks / Avatars / Titles"'),
 ('var box := _make_shop_item(id, "卡背 " + str(cb).get_basename().replace("cardback_', 'var box := _make_shop_item(id, "Cardback " + str(cb).get_basename().replace("cardback_'),
 ('_flash("已拥有该%s" % kind)', '_flash("Already owned: %s" % kind)'),
 ('inst.setup("美容品", "「%s」%s" % [file.get_basename().replace("Avatar_", "").replace', 'inst.setup("Cosmetics", "%s %s" % [file.get_basename().replace("Avatar_", "").replace'),
 ('"购买后可在PlayerProfile/图鉴美容品中使用"', '"Usable in Player Profile / Collection cosmetics"'),
 ('_flash("已购买%s! 可在Profile/卡背Select中使用" % kind))', '_flash("Purchased %s! Usable in Profile / cardback selection" % kind))'),
 ('_make_label(tab, "资源 · 通配符包"', '_make_label(tab, "Resources - Wildcard Packs"'),
 ('["Common通配符 x20", "common", 20, 200],', '["Common Wildcards x20", "common", 20, 200],'),
 ('["Rare通配符 x10", "rare", 10, 300],', '["Rare Wildcards x10", "rare", 10, 300],'),
 ('["Epic通配符 x5", "epic", 5, 400],', '["Epic Wildcards x5", "epic", 5, 400],'),
 ('["Legendary通配符 x2", "legendary", 2, 500],', '["Legendary Wildcards x2", "legendary", 2, 500],'),
 ('["混合包: 全Rarity各 x5", "mix", 5, 600],', '["Mixed Pack: all rarities x5", "mix", 5, 600],'),
 ('inst.setup(name_s, "通配符包", "购买后直接加入通配符库存', 'inst.setup(name_s, "Wildcard Pack", "Added to wildcard inventory on purchase'),
 ('可用于卡牌详情弹窗制作副本", icon_path, price,', 'usable in card detail Craft popup", icon_path, price,'),
 ('_flash("已购买 %s" % name_s))', '_flash("Purchased %s" % name_s))'),
 ('price_btn.tooltip_text = "购买"', 'price_btn.tooltip_text = "Buy"'),
 ('square_btn.tooltip_text = "更多优惠"', 'square_btn.tooltip_text = "More offers"'),
 ('owned_tag.text = "✓ 已拥有"', 'owned_tag.text = "Owned"'),
],
'd:/warpforge/scripts/gacha.gd': [
 ('["Legendary通配符", "legendary", 2, "wild"],', '["Legendary Wildcard", "legendary", 2, "wild"],'),
 ('["Epic通配符", "epic", 3, "wild"],', '["Epic Wildcard", "epic", 3, "wild"],'),
 ('["Rare通配符", "rare", 5, "wild"],', '["Rare Wildcard", "rare", 5, "wild"],'),
 ('_make_btn(Vector2(422, 941), Vector2(357, 58), "Card来源"', '_make_btn(Vector2(422, 941), Vector2(357, 58), "Card Sources"'),
 ('_toast("Ticket每天 +1 张 · Card可从ShopPack、Daily Rewards与Campaign获得"))', '_toast("Tickets: +1 per day - cards from Shop Packs, Daily Rewards and Campaign"))'),
 ('_make_label("每箱至少获得一件SpecialItem"', '_make_label("Each crate grants at least one Special Item"'),
 ('done.text = "全部CollectedDone!"', 'done.text = "All collected - done!"'),
 ('info.text = "你已Collected全部SpecialItem · 点击Crate开启新一轮"', 'info.text = "You collected all Special Items - click the Crate to start a new round"'),
 ('badge_txt.text = "已Collected"', 'badge_txt.text = "Collected"'),
 ('_toast("Vault已清空 · Start新一轮")', '_toast("Vault cleared - start a new round")'),
 ('_toast("Ticket不足 · 明天再来 (每天 +1 张)")', '_toast("Not enough Tickets - come back tomorrow (+1 per day)")'),
 ('_toast("PityRewards: Legendary通配符 ×1")', '_toast("Pity Rewards: Legendary Wildcard x1")'),
],
'd:/warpforge/scripts/social.gd': [
 ('"JoinAlliance可获得额外Rewards"', '"Join an Alliance for extra Rewards"'),
 ('"暂无Alliance\\n创建或Join一个Alliance，与战友一起积累Event', '"No Alliance\\nCreate or join an Alliance to earn Event'),
 ('"排行榜"', '"Leaderboard"'),
 ('_toast("单机版无Online排行榜")', '_toast("No online leaderboard in single-player")'),
 ('_ally_name.text = str(_alliance.get("name", "我的Alliance"))', '_ally_name.text = str(_alliance.get("name", "My Alliance"))'),
 ('_make_label(row, "得分 %d" % score', '_make_label(row, "Score %d" % score'),
 ('var opt := _make_btn(row, Vector2(790, 14), Vector2(130, 48), "操作"', 'var opt := _make_btn(row, Vector2(790, 14), Vector2(130, 48), "Actions"'),
 ('["挑战", func(): _toast("挑战 %s (进入练习对战)" % _options_name.text)],', '["Challenge", func(): _toast("Challenge %s (practice battle)" % _options_name.text)],'),
 ('["加为Friends", func():', '["Add Friend", func():'),
 ('_toast("已是Friends")', '_toast("Already friends")'),
],
}

total = 0
for path, pairs in MAPS.items():
    try:
        s = io.open(path, encoding='utf-8').read()
    except Exception as e:
        print('skip %s' % path)
        continue
    n = 0
    for zh, en in pairs:
        if zh in s:
            s = s.replace(zh, en)
            n += 1
        else:
            print('MISS %s: %s' % (path.split('/')[-1], zh[:35]))
    io.open(path, 'w', encoding='utf-8', newline='').write(s)
    total += n
    print('%s: %d/%d' % (path.split('/')[-1], n, len(pairs)))
print('total %d' % total)
