# -*- coding: utf-8 -*-
"""批量替换卡组系列界面中文 UI -> 英文"""
import io

MAPS = {
'd:/warpforge/scripts/deck_collection.gd': [
 ('Toast.show(self, "单机版无需解锁卡组槽"', 'Toast.show(self, "Deck slots are all unlocked in this build"'),
 ('dlg.dialog_text = "%s（单机复刻版占位）\\n原版为收藏系统的%s标签页。" % [tab, tab]', 'dlg.dialog_text = "%s: single-player placeholder for the original %s tab." % [tab, tab]'),
 ('dlg.ok_button_text = "关闭"', 'dlg.ok_button_text = "Close"'),
 ('_detail_hint.text = "点击左侧卡组查看详情', '_detail_hint.text = "Click a deck on the left for details'),
 ('deck_name = "我的卡组"', 'deck_name = "My Deck"'),
 ('hint.text = "还没有卡组', 'hint.text = "No decks yet'),
 ('点击右上角 Create Deck 创建你的第一个卡组', 'Click Create Deck in the top right to build your first deck'),
 ('(1 督军 + 30 张同阵营卡)"', '(1 warlord + 30 cards of the same faction)"'),
 ('var practice := "是" if deck.get("isPractice", 0) == 1 else "否"', 'var practice := "Yes" if deck.get("isPractice", 0) == 1 else "No"'),
 ('_detail_meta.text = "%s · 难度 %d · 模式 %d · AI %d · 练习 %s · 共 %d 卡"', '_detail_meta.text = "%s | Difficulty %d | Mode %d | AI %d | Practice %s | %d cards"'),
 ('_detail_stats.text = "卡组构成:\\n"', '_detail_stats.text = "Deck Composition:\\n"'),
 ('(PnP 完整卡面, 数值/效果见卡牌详情)"', '(Full PnP card face; stats/effects in card details)"'),
 ('return "卡组构成:\\n" + "\\n".join(lines) + "\\n\\n(卡名来自 OCR 数值映射)"', 'return "Deck Composition:\\n" + "\\n".join(lines) + "\\n\\n(Card names from OCR stats mapping)"'),
 ('var text := "卡组构成 (按 ID 前缀):\\n"', 'var text := "Deck Composition (by ID prefix):\\n"'),
 ('"、".join(lines2)', '"\\n".join(lines2)'),
 ('text += "\\n\\n(卡 ID→卡名为服务端数据, 本地缺失;', 'text += "\\n\\n(Card ID->name is server data, missing locally;'),
 (' 督军立绘为阵营默认 — ID→名映射缺失;', ' warlord art is faction default - ID->name mapping missing;'),
 (' 卡背已完整还原)"', ' card backs fully restored)"'),
],
'd:/warpforge/scripts/deck_builder.gd': [
 ('Toast.show(self, "卡组信息: 卡组 %d 张" % _deck_count(),', 'Toast.show(self, "Deck info: %d cards" % _deck_count(),'),
 ('Toast.show(self, "美容品: 请前往收藏-美容品界面",', 'Toast.show(self, "Cosmetics: visit Collection - Cosmetics",'),
 ('_hero_hint.text = "当前阵营督军 %d 个" % shown', '_hero_hint.text = "%d warlords available" % shown'),
 ('_hero_hint.text = "当前阵营无可用督军"', '_hero_hint.text = "No warlords available"'),
 ('title.text = "选择督军 (%s)" % _faction', 'title.text = "Choose Warlord (%s)" % _faction'),
 ('var close_btn := _mulligan_btn("取消", 140, _close_hero_picker)', 'var close_btn := _mulligan_btn("Cancel", 140, _close_hero_picker)'),
 ('"common": "普通", "rare": "稀有", "epic": "史诗",', '"common": "Common", "rare": "Rare", "epic": "Epic",'),
 ('"legendary": "传说", "defence": "特殊"}', '"legendary": "Legendary", "defence": "Special"}'),
 ('lines.append("关键词: " + ", ".join(kws))', 'lines.append("Keywords: " + ", ".join(kws))'),
 ('_flash("请先选择督军")', '_flash("Choose a warlord first")'),
 ('_flash("已达上限: %s (%d 张)" % [name, _rarity_limit(card)])', '_flash("Limit reached: %s (%d copies)" % [name, _rarity_limit(card)])'),
 ('_flash("卡组已满 (%d 张)" % DECK_SIZE)', '_flash("Deck is full (%d cards)" % DECK_SIZE)'),
 ('hero_btn.tooltip_text = "选择督军"', 'hero_btn.tooltip_text = "Choose Warlord"'),
 ('def_btn.tooltip_text = "防御卡槽 (经典模式不可用)"', 'def_btn.tooltip_text = "Defence slot (not available in Classic)"'),
 ('empty.text = "点击卡牌加入卡组"', 'empty.text = "Click a card to add it to the deck"'),
 ('b.tooltip_text = "点击移除: %s" % card.get("name", "?")', 'b.tooltip_text = "Click to remove: %s" % card.get("name", "?")'),
 ('return "未选择督军, 无法保存"', 'return "Choose a warlord first"'),
 ('return "卡组需 %d 张 (%d 当前), 未保存" % [DECK_SIZE, _deck_count()]', 'return "Deck needs %d cards (currently %d), not saved" % [DECK_SIZE, _deck_count()]'),
 ('return "保存失败"', 'return "Save failed"'),
 ('return "卡组已保存: %s" % _hero.get("name", "")', 'return "Deck saved: %s" % _hero.get("name", "")'),
 ('if msg.begins_with("卡组需") or msg == "未选择督军, 无法保存" or msg == "保存失败":', 'if msg.begins_with("Deck needs") or msg == "Choose a warlord first" or msg == "Save failed":'),
],
'd:/warpforge/scripts/deck_info_popup.gd': [
 ('_label("卡组内容", 659.0, 228.0', '_label("Deck Contents", 659.0, 228.0'),
 ('var deck_name := str(_deck.get("name", "卡组"))', 'var deck_name := str(_deck.get("name", "Deck"))'),
 ('empty.text = "卡组为空"', 'empty.text = "Deck is empty"'),
 ('_Toast("模板卡组不可编辑, 请创建自己的卡组")', '_Toast("Template decks cannot be edited; create your own")'),
 ('_Toast("模板卡组不可删除")', '_Toast("Template decks cannot be deleted")'),
 ('dlg.title = "删除卡组"', 'dlg.title = "Delete Deck"'),
 ('dlg.dialog_text = "确定删除卡组「%s」?" % _deck.get("name", "")', 'dlg.dialog_text = "Delete deck \\"%s\\"?" % _deck.get("name", "")'),
 ('dlg.ok_button_text = "删除"', 'dlg.ok_button_text = "Delete"'),
 ('dlg.cancel_button_text = "取消"', 'dlg.cancel_button_text = "Cancel"'),
 ('_Toast("卡组已删除")', '_Toast("Deck deleted")'),
 ('_Toast("卡组信息已切换")', '_Toast("Deck info switched")'),
 ('_Toast("模板卡组不可复制")', '_Toast("Template decks cannot be copied")'),
 ('_Toast("已复制卡组 (同名副本)")', '_Toast("Deck copied (duplicate)")'),
 ('_Toast("分享功能单机版未开放")', '_Toast("Sharing not available in single-player")'),
 ('_Toast("分享到聊天单机版未开放")', '_Toast("Share to chat not available in single-player")'),
],
'd:/warpforge/scripts/collection.gd': [
 ('_detail_hint.text = "点击左侧卡片查看详情', '_detail_hint.text = "Click a card on the left for details'),
 ('· 卡面优先显示 PnP 完整原版卡面\\n· 无卡面资源时回退立绘 + 阵营卡框合成\\n· 数值来自', 'Full PnP card face preferred\\nFallback: art + faction frame\\nStats from'),
 ('parts.append("费用: %s" % _fmt(card.get("cost")))', 'parts.append("Cost: %s" % _fmt(card.get("cost")))'),
 ('parts.append("近战: %s" % _fmt(card.get("attack")))', 'parts.append("Melee: %s" % _fmt(card.get("attack")))'),
 ('parts.append("远程: %s" % _fmt(card.get("ranged_attack")))', 'parts.append("Ranged: %s" % _fmt(card.get("ranged_attack")))'),
 ('parts.append("生命: %s" % _fmt(card.get("health")))', 'parts.append("Health: %s" % _fmt(card.get("health")))'),
 ('_detail_stats.text += "\\n所属: %s" % sub', '_detail_stats.text += "\\nFaction: %s" % sub'),
 ('_detail_stats.text += "\\n关键词: %s" % " · ".join(kws)', '_detail_stats.text += "\\nKeywords: %s" % " ".join(kws)'),
 ('_detail_stats.text += "\\n\\n效果:\\n%s" % desc', '_detail_stats.text += "\\n\\nEffect:\\n%s" % desc'),
 ('_detail_stats.text = "数值缺失\\n\\n(解包资源无此卡的 PnP 卡面)"', '_detail_stats.text = "Stats missing\\n\\n(No PnP card face in unpacked assets)"'),
],
'd:/warpforge/scripts/import_deck_popup.gd': [
 ('_error.text = "请输入卡组代码"', '_error.text = "Paste a deck code"'),
 ('_error.text = "格式错误: 请输入 JSON 格式的卡组代码"', '_error.text = "Invalid format: paste a JSON deck code"'),
 ('var name: String = str(parsed.get("name", "导入卡组"))', 'var name: String = str(parsed.get("name", "Imported Deck"))'),
 ('_error.text = "格式错误: cards 需要是 [{name,count}] 数组"', '_error.text = "Invalid format: cards must be [{name,count}]"'),
 ('_error.text = "督军「%s」不存在" % hero_name', '_error.text = "Warlord \\"%s\\" not found" % hero_name'),
 ('_error.text = "卡「%s」不存在" % cn', '_error.text = "Card \\"%s\\" not found" % cn'),
 ('_error.text = "卡「%s」阵营与督军不符" % cn', '_error.text = "Card \\"%s\\" faction does not match warlord" % cn'),
 ('_error.text = "卡组需 30 张, 当前 %d 张" % total', '_error.text = "Deck needs 30 cards, currently %d" % total'),
 ('_error.text = "保存失败"', '_error.text = "Save failed"'),
 ('Toast.show(self, "卡组已导入: %s" % name)', 'Toast.show(self, "Deck imported: %s" % name)'),
 ('_error.text = "✓ 卡组已导入: %s" % name', '_error.text = "Deck imported: %s" % name'),
],
'd:/warpforge/scripts/mode_select.gd': [
 ('set_btn.tooltip_text = "设置"', 'set_btn.tooltip_text = "Settings"'),
 ('_select_deck({"name": "我的卡组"', '_select_deck({"name": "My Deck"'),
 ('decks.append({"name": "我的卡组"', 'decks.append({"name": "My Deck"'),
 ('clb.text = "%d 卡" % cnt', 'clb.text = "%d cards" % cnt'),
 ('drawer_title.text = "卡组内容"', 'drawer_title.text = "Deck Contents"'),
 ('empty.text = "卡组为空"', 'empty.text = "Deck is empty"'),
 ('name_str = "我的卡组"', 'name_str = "My Deck"'),
],
}

total = 0
for path, pairs in MAPS.items():
    try:
        s = io.open(path, encoding='utf-8').read()
    except Exception as e:
        print('skip %s: %s' % (path, e))
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
