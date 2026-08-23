#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_cosmetics.py — 02_装饰品 说明书生成器 (09_装饰品)

输出 (说明书/09_装饰品/):
  README.md         — 七子目录总览 + 13 定义类表 + 使用状态
  卡背.md            — Cardback_* (Main/SDF 成对, Texture2D 全清单按阵营标注)
  头像.md            — Avatar_* (Texture2D 全清单)
  督军立绘.md         — UI_Deck_Warlord_*/UI_Deck_Master_* (全清单)
  联盟徽章.md         — Alliance_Trophies_* 徽章 (全清单)
  战役奖励背景.md      — Campaign_Faction_Bck_* (全清单)
  边框.md            — 40K_display_Flavortext 13 阵营 (卡牌详情 FlavourText 背景)
  定义数据.md         — 13 个 MonoBehaviour 定义类 (字段表/样本/前缀统计)

用法: py312/python.exe Warpforge_tools/scripts/gen_spec_cosmetics.py
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

C = 'd:/2/解包整理/02_装饰品/'
W = 'd:/2/解包整理/说明书/09_装饰品/'

# 阵营映射: cardArmy id -> 阵营名 (card_index.json factions)
FACTION = {
    10: 'Ultramarines', 20: 'Goff(Orks)', 30: 'SaimHann(Aeldari)', 40: 'Sautekh(Necrons)',
    50: 'BlackLegion', 60: 'Leviathan(Tyranids)', 70: 'TauEmpire', 80: 'Sororitas',
    90: 'Genestealers', 100: 'AstraMilitarum', 110: 'DarkAngels', 120: 'EmperorsChildren',
    130: 'SpaceWolves',
}


def wfile(fp, txt):
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(txt)
    print('✓ %s (%d 行)' % (os.path.relpath(fp, 'd:/2/解包整理/说明书'), txt.count(chr(10))))


def list_dir(p):
    return sorted(os.listdir(p)) if os.path.isdir(p) else []


def texs(sub):
    d = os.path.join(C, sub, 'Texture2D')
    return [f for f in list_dir(d) if f.endswith('.png')]


def sprites(sub):
    d = os.path.join(C, sub, 'Sprite')
    return [f for f in list_dir(d) if f.endswith('.json')]


def load_defs():
    """读 02_装饰品/定义数据/MonoBehaviour 全部, 按 m_Script pid 分组"""
    d = os.path.join(C, '定义数据', 'MonoBehaviour')
    groups = {}
    for fn in list_dir(d):
        if not fn.endswith('.json'):
            continue
        try:
            obj = json.load(open(os.path.join(d, fn), encoding='utf-8'))
        except Exception:
            continue
        if not isinstance(obj, dict):
            continue
        pid = obj.get('m_Script', {}).get('m_PathID')
        if pid is not None:
            groups.setdefault(pid, []).append(obj)
    return groups


# ---- 13 定义类静态知识 (2026-08-22 调查, MonoScript 类名经 09_游戏数据/脚本定义 反查) ----
DEF_CLASSES = [
    ('PlayerAvatar', 562972769022917651, '头像',
     'autoAssign cardArmy cardRarity descriptionTextReference expansionPack imageReference '
     'inDropTables inInventory itemDescriptionKey itemLoreKey nameTextReference '
     'showInCollectionOptions uniqueId'),
    ('CosmeticItemTitle', -3133590969968446585, '称号',
     'autoAssign cardArmy cardRarity descriptionTextReference expansionPack imageReference '
     'inDropTables inInventory itemDescriptionKey itemLoreKey nameTextReference '
     'showInCollectionOptions uniqueId'),
    ('CosmeticItemCardback', 5795978134593289333, '卡背',
     'autoAssign cardArmy cardBackSDF cardRarity descriptionTextReference expansionPack '
     'imageReference inDropTables inInventory itemDescriptionKey itemLoreKey nameTextReference '
     'showInCollectionOptions uniqueId'),
    ('DropTableItem', -2313241570638646064, '掉落表',
     'dropTableItems dropTableItemsWeight obtainableItems obtainableItemsWeight autoAssign '
     'cardArmy cardRarity expansionPack itemDescriptionKey itemLoreKey uniqueId'),
    ('AllianceBadge', 8712395647440592121, '联盟/熔炉徽章',
     'badgeImage cardArmy cardRarity itemDescriptionKey itemLoreKey uniqueId'),
    ('ShopContainer', -5965435178007098505, '商店卡包容器',
     'containerItems containerNameKey containerPreviewImage containerType currencyItems '
     'dropTableItems expansion itemDescriptionKey itemLoreKey legendaryContainer securedItems '
     'uniqueId useManualId visualPrefab cardArmy cardRarity'),
    ('CosmeticItemAvatarBorder', 1207469734600494903, '头像边框',
     'autoAssign cardArmy cardRarity descriptionTextReference expansionPack imageReference '
     'inDropTables inInventory itemDescriptionKey itemLoreKey nameTextReference '
     'parentEvent showInCollectionOptions uniqueId'),
    ('ParentEventData', 3885813256827862744, '活动(父)',
     'activationType dates drawData enabled eventId filter location mainMenuOptions '
     'notificationsToWatch priority references showInMainMenu showInNavigationBar '
     'uploadToLive uploadToPreprod'),
    ('ExpansionPassPoints', 1890508439449491322, '通票积分',
     'cardArmy cardRarity itemDescriptionKey itemLoreKey parentEvent pointNameKey'),
    ('ShopOfferDataV2', 296048164972309843, '商店特惠',
     'activationType createXSollaBundle dates displayOnlyOffers drawData enabled eventId '
     'filter location mainMenuOptions offerItems priceDefinition priority rarity references '
     'showInMainMenu showRewardOnPurchase showWebShopButton uploadToLive uploadToPreprod '
     'xsollaBundleData'),
    ('ExpansionPremiumItem', -6115383005132979948, '特惠商品',
     'backgroundSprite cardArmy cardRarity expansionPack id itemDescriptionKey itemIcon '
     'itemLoreKey localizationKey'),
    ('ExpansionPassData', -6525319201646887420, '通票',
     'activationType dates drawData enabled eventId filter howToScoreDescription location '
     'mainMenuOptions milestones premiumItem premiumOffer premiumPercentageBonus priority '
     'references scoringItem showInMainMenu uploadToLive uploadToPreprod xpPerGold'),
    ('Currency', -4185286980102898918, '货币',
     'bigIcon cardArmy cardRarity code displayName itemDescriptionKey itemLoreKey smallIcon type'),
]


def build_uid_faction_map(groups):
    """m_Name -> cardArmy 阵营 (权威) 精确映射 (uniqueId 是 GUID 哈希, 名字才是键)"""
    m = {}
    for objs in groups.values():
        for o in objs:
            nm = str(o.get('m_Name', '')).strip()
            army = o.get('cardArmy')
            if not nm:
                continue
            if isinstance(army, (int, float)) and int(army) != 0:
                m[nm] = FACTION.get(int(army), '军%d' % int(army))
    return m


def faction_of_unique(name, fmap):
    """m_Name 匹配: ①精确 ②name 是定义名前缀(取最短定义名) ③定义名是 name 前缀(取最长)"""
    if name in fmap:
        return fmap[name]
    cands = [n for n in fmap if name.startswith(n) or n.startswith(name)]
    if not cands:
        return ''
    if name in cands:
        return fmap[name]
    supers = [n for n in cands if name.startswith(n) and n != name]   # 定义名更短
    if supers:
        return fmap[max(supers, key=len)]
    subs = [n for n in cands if n.startswith(name) and n != name]     # 定义名更长
    if subs:
        return fmap[min(subs, key=len)]
    return ''


def gen_readme():
    txt = ['# 装饰品说明书 (02_装饰品)',
           '',
           '> 来源: 02_装饰品/ (7 子目录, 5460 文件) — 全部为"玩家外观/收集物"类资源',
           '> 权威=原始 Unity JSON (Sprite/Texture2D/MonoBehaviour); 本说明书为索引+清单, 生成器可重跑',
           '> 命名规则: 每个外观 = 1 张 Texture2D + 2 个 Sprite JSON (本名 + _<pid> 派生变体, 内容一致)',
           '',
           '## 子目录总览',
           '',
           '| 子目录 | Texture2D | Sprite | 内容 | 说明书 |',
           '|---|---|---|---|---|',
           ]
    for sub, name in (('卡背', '卡背'), ('头像', '头像'), ('督军立绘', '督军立绘'),
                      ('联盟徽章', '联盟徽章'), ('战役奖励背景', '战役奖励背景'), ('边框', '边框')):
        txt.append('| %s | %d | %d | | [%s.md](%s.md) |' % (sub, len(texs(sub)), len(sprites(sub)) / 2, sub, sub))
    txt += ['| 定义数据 | 0 | 0 | MonoBehaviour 对象定义 (2522) | [定义数据.md](定义数据.md) |',
            '',
            '## 定义数据类 (13 个 MonoBehaviour 定义类, 详见 定义数据.md)',
            '',
            '| 类 (MonoScript) | 对象数 | 内容 |',
            '|---|---|---|']
    groups = load_defs()
    for cls, pid, what, _fields in DEF_CLASSES:
        n = len(groups.get(pid, []))
        txt.append('| %s | %d | %s |' % (cls, n, what))
    txt += ['',
            '## 使用状态 (项目 D:/warpforge)',
            '',
            '- 卡背 233 张 ✅ 在用 (assets/ui/cardback_thumbs/, battle/deck_collection/shop 等)',
            '- 头像 472 张 ✅ 在用 (assets/ui/avatars/, player_profile)',
            '- 督军立绘 65 ✅ 在用 (mode_select 督军行/deck 选择)',
            '- 战役奖励背景 13 ✅ (campaign 轨道)',
            '- 联盟徽章 22 (social 联盟, 按需)',
            '- 边框=40K_display_Flavortext 13 ✅ (card_displayer Lore 区)',
            '- 定义数据 2522 对象: 卡背/头像/称号/徽章定义在用; 掉落表/商店/活动/通票/货币类 = 运营数据 (复刻参考)',
            '',
            '> 补充: 玩家资料边框 (Player Profile Border/Player_Avatar_selected) 在 03_界面UI, 不在本目录',
            '']
    wfile(os.path.join(W, 'README.md'), '\n'.join(txt))


def gen_tex_md(sub, title, note, faction_map=True):
    """通用: 子目录说明书 = 统计 + 命名规则 + 阵营分组 + Texture2D 全清单"""
    ts = texs(sub)
    sp = len(sprites(sub)) / 2
    groups = load_defs()
    # 按阵营分组 (文件名前缀推断 + 定义对象 cardArmy 权威标注)
    lines = ['# %s说明书 (02_装饰品/%s)' % (title, sub), '',
             '> 来源: 02_装饰品/%s/ — Texture2D %d / Sprite JSON %d (含派生变体)' % (sub, len(ts), len(sprites(sub))),
             note, '',
             '## 全量清单 (%d 纹理, 每张 = Main+变体 Sprite JSON)' % len(ts), '',
             '| 纹理文件 | 阵营 |', '|---|---|']
    fmap = build_uid_faction_map(groups) if faction_map else {}
    for f in ts:
        fac = faction_of_unique(f[:-4], fmap) if faction_map else ''
        lines.append('| %s | %s |' % (f, fac))
    lines += ['', '> 阵营标注: 优先按定义数据 uniqueId→cardArmy 权威映射; 空=通用/无定义对应', '']
    wfile(os.path.join(W, '%s.md' % sub), '\n'.join(lines))


def gen_defs():
    groups = load_defs()
    lines = ['# 定义数据说明书 (02_装饰品/定义数据)',
             '',
             '> 来源: 02_装饰品/定义数据/MonoBehaviour (2522 对象 json) — 游戏"可收集物品/运营"对象定义, m_Script 指 MonoScript',
             '> 类名经 09_游戏数据/脚本定义/MonoScript 反查 (Assembly-CSharp + Everguild.LiveOps)',
             '> 权威字段值=各对象 JSON; Warpforge_code 可查类实现',
             '',
             '## 13 类定义表',
             '',
             '| 类 | m_Script pid | 对象数 | 内容 | 字段 |',
             '|---|---|---|---|---|']
    for cls, pid, what, fields in DEF_CLASSES:
        n = len(groups.get(pid, []))
        lines.append('| %s | %d | %d | %s | %s |' % (cls, pid, n, what, fields))
    lines += ['',
              '## 各类样本名 (前 12 个)',
              '']
    for cls, pid, what, _f in DEF_CLASSES:
        objs = groups.get(pid, [])
        names = [str(o.get('m_Name', '')) for o in objs][:12]
        lines.append('**%s (%s)** %d 对象' % (cls, what, len(objs)))
        lines.append('')
        lines.append(', '.join('`%s`' % n for n in names if n))
        lines.append('')
    lines += ['## 使用建议',
              '',
              '- 外观类 (PlayerAvatar/CosmeticItemTitle/CosmeticItemCardback/CosmeticItemAvatarBorder/AllianceBadge): uniqueId=物品 id, cardArmy=阵营, imageReference/badgeImage=贴图 GUID → 复刻"收集物"数据源',
              '- 掉落表 DropTableItem: 开包/奖励抽奖权重数据; ShopContainer: 卡包商品数据',
              '- 运营类 (ParentEventData/ExpansionPass/ShopOffer): 线上活动配置, 复刻时按需参考 (排行榜/通票/特惠)',
              '- Currency: Blackstone/Gacha tickets 货币定义 (名称/图标)', '']
    wfile(os.path.join(W, '定义数据.md'), '\n'.join(lines))


def main():
    os.makedirs(W, exist_ok=True)
    gen_readme()
    gen_tex_md('卡背', '卡背',
               '> 命名: Cardback_<阵营缩写>_<名称> — 每张 2 Sprite: Main(全彩) + SDF(高亮/阴影帧)\n'
               '> 阵营列 = 定义数据 m_Name→cardArmy 权威映射; 空 = 无定义对象 (战役/Season/Ranked/Premium Bundle/_AA_HB 运营卡背)',
               faction_map=True)
    gen_tex_md('头像', '头像',
               '> 命名: Avatar_<阵营缩写>_<名称>; 定义类 PlayerAvatar (cardArmy 权威阵营)',
               faction_map=True)
    gen_tex_md('督军立绘', '督军立绘',
               '> 命名: UI_Deck_Warlord_<督军名> / UI_Deck_Master_<名> / UI_Deck_Draft Generic Image(兜底); '
               'mode_select 督军行/deck 选择用; 立绘 905px 级',
               faction_map=False)
    gen_tex_md('联盟徽章', '联盟徽章',
               '> 命名: Alliance_Trophies_<阵营/活动>; 定义类 AllianceBadge (Badge image)',
               faction_map=False)
    gen_tex_md('战役奖励背景', '战役奖励背景',
               '> 命名: Campaign_Faction_Bck_<阵营>; campaign 轨道奖励背景',
               faction_map=False)
    gen_tex_md('边框', '边框 (FlavourText 背景)',
               '> 注意: 本目录实际内容 = 40K_display_Flavortext <13 阵营> — 卡牌详情弹窗 Lore/FlavourText 背景框 '
               '(card_displayer 13 阵营 flavortext/ 在用), 与"玩家资料边框"不同',
               faction_map=False)
    gen_defs()


if __name__ == '__main__':
    main()
