# -*- coding: utf-8 -*-
"""
按阵营资源索引生成器 (2026-08-17)
盘点 解包整理/ 与 D:\\warpforge/assets/ 里按阵营/种族可分的资源，
按 13 阵营建立分类索引 → D:\\2\\按阵营资源索引.md

用法: py312/python.exe scripts/faction_resources_index.py
"""
import os, sys, json, re
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

UNPACK = r"D:\2\解包整理"
PNPS   = r"D:\2\Warpforge部队卡片"
CB     = r"D:\2\Warpforge Cardbacks"
CF     = r"D:\2\Warpforge cardframes"
PROJ   = r"D:\warpforge"

# ---------------- 阵营映射表 ----------------
# game=factions.json 名 / pnp=PnP 目录 / dir01=01_卡牌中文目录 / vo=语音前缀 /
# cb=卡背前缀 / av=头像前缀 / alliance=联盟徽章名(可多个) / bg=战役背景名(可多个) /
# scene=07_场景 battlearena 后缀 / model=06_模型目录 / tut=教程语音
FACTIONS = [
    dict(cn="极限战士", id=10, game="Ultramarines", pnp="Ultramarines", dir01="Ultramarines_极限战士",
         vo=["UM"], cb=["UM"], av=["UM"], alliance=["Ultramarines"], bg=["Ultramarines"],
         scene="1", model=None, tut=["Tutorial1"], note="battlearena1=通用场景（教程用）"),
    dict(cn="高夫兽人", id=20, game="Goff", pnp="Orks", dir01="Orks_兽人",
         vo=["Goff", "Orks"], cb=["GOF", "ORK"], av=["Ork", "GOF"], alliance=["Goff", "Ork"], bg=["Orks"],
         scene="2", model=None, tut=["Tutorial2"], note="battlearena2=兽人风格（Fort Wall/Skull/Steam pipes）"),
    dict(cn="赛姆汉灵族", id=30, game="SaimHann", pnp="Aeldari", dir01="Aeldari_灵族",
         vo=["CW_SaimHann"], cb=["ASH"], av=["ASH"], alliance=["SaimHann"], bg=["Saim-Hann"],
         scene="aeldari", model=None, tut=[], note=""),
    dict(cn="索泰克死灵", id=40, game="Sautekh", pnp="Necron", dir01="Necrons_死灵族",
         vo=["Sautekh"], cb=["SAU"], av=["SAU"], alliance=["Sautekh"], bg=["Sautekh"],
         scene=None, model=None, tut=[], note="无专属战场场景"),
    dict(cn="黑色军团", id=50, game="BlackLegion", pnp="Chaos", dir01="BlackLegion_黑色军团",
         vo=["BL"], cb=["BL"], av=["BL"], alliance=["BlackLegion"], bg=["BlackLegion"],
         scene="blacklegion", model="scenes_scenes_battlearenablacklegion", tut=[], note=""),
    dict(cn="利维坦泰伦", id=60, game="Leviathan", pnp="Tyranid", dir01="Tyranids_泰伦虫族",
         vo=["Tyranid_Leviathan", "TL"], cb=["TL"], av=["TL"], alliance=["Leviathan"], bg=["Leviathan"],
         scene="leviathan", model=None, tut=[], note=""),
    dict(cn="钛帝国", id=70, game="TauEmpire", pnp="Tau", dir01="Tau_钛帝国",
         vo=["Tau_Empire", "Tau"], cb=["TAU"], av=["TAU", "Tau"], alliance=["Tau"], bg=["Tau_Empire"],
         scene="tauviorla", model="scenes_scenes_battlearenatauviorla", tut=[], note="场景名 tauviorla"),
    dict(cn="战斗修女", id=80, game="Sororitas", pnp="Sorotitas", dir01="Sororitas_战斗修女",
         vo=["ADS"], cb=["SOR"], av=["SOR"], alliance=["Sororitas"], bg=["Sororitas"],
         scene="sororitas", model=None, tut=[], note="语音前缀 ADS=Adepta Sororitas"),
    dict(cn="基因窃取者教派", id=90, game="Genestealers", pnp="Genestealer Cult", dir01="GenestealerCults_基因窃取者教派",
         vo=["GSC"], cb=["GSC"], av=["GSC"], alliance=["GSC"], bg=["Genestealers"],
         scene="genestealers", model="scenes_scenes_battlearenagenestealers", tut=[], note=""),
    dict(cn="星界军", id=100, game="AstraMilitarum", pnp="Astra Militarum", dir01="AstraMilitarum_星界军",
         vo=["AM"], cb=["AM"], av=["AM"], alliance=["AM"], bg=["AstraMilitarum"],
         scene="astramilitarum", model="scenes_scenes_battlearenaastramilitarum", tut=[], note=""),
    dict(cn="暗黑天使", id=110, game="DarkAngels", pnp="Dark Angels", dir01="DarkAngels_暗黑天使",
         vo=["DA"], cb=["DA"], av=["DA"], alliance=["Dark Angels"], bg=["Dark Angels"],
         scene="darkangels", model="scenes_scenes_battlearenadarkangels", tut=[], note=""),
    dict(cn="帝皇之子", id=120, game="EmperorsChildren", pnp="Emperor_s Children", dir01="EmperorsChildren_帝皇之子",
         vo=["CSM_EC"], cb=["CSM", "EC"], av=["EC"], alliance=["Emperors Children"], bg=["Emperors Children"],
         scene="emperorschildren", model="scenes_scenes_battlearenaemperorschildren", tut=[], note="卡背前缀 CSM_EmperorsChildren（旧版 1 张 EC_）"),
    dict(cn="太空野狼", id=130, game="SpaceWolves", pnp="Space Wolves", dir01="SpaceWolves_太空野狼",
         vo=["SpaceWolves"], cb=["SW"], av=["SW"], alliance=["Space Wolves"], bg=["Space Wolves"],
         scene="spacewolves", model="scenes_scenes_battlearenaspacewolves", tut=[], note=""),
]

# 通用前缀（非阵营专属）
GENERIC_CB = ["All", "Ranked", "Season"]   # 卡背通用
GENERIC_AV = ["Player", "WF", "All"]       # 头像通用

def files(d, suffix=None):
    """目录下文件列表（含 .import 但只按实际资源统计）"""
    try:
        return [f for f in os.listdir(d) if suffix is None or f.lower().endswith(suffix)]
    except FileNotFoundError:
        return []

def count_ext(d, *exts):
    exts = tuple(e.lower() for e in exts)
    return sum(1 for f in files(d) if f.lower().endswith(exts))

def count_ext_recursive(d, *exts):
    """递归统计目录树内文件（含子目录），排除 .import"""
    exts = tuple(e.lower() for e in exts)
    n = 0
    for root, _, fs in os.walk(d):
        for f in fs:
            if f.lower().endswith(exts) and not f.lower().endswith(".png.import"):
                n += 1
    return n

def subdirs(d):
    try:
        return sorted([x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))])
    except FileNotFoundError:
        return []

# ---------------- 加载数据 ----------------
card_stats = json.load(open(os.path.join(PROJ, "data", "card_stats.json"), encoding="utf-8"))["cards"]
cards_by_name = {}
for c in card_stats:
    cards_by_name[c["name"]] = c
card_cnt = Counter(c.get("faction") for c in card_stats)
card_type = {}
for c in card_stats:
    card_type.setdefault(c.get("faction"), Counter())[c.get("type")] += 1

warlord_ids = json.load(open(os.path.join(PROJ, "data", "warlord_ids.json"), encoding="utf-8"))
# 前缀 → 阵营 game
PREF2GAME = {}
for f in FACTIONS:
    for p in f["cb"]: PREF2GAME.setdefault(p, f["game"])
    for p in f["av"]: PREF2GAME.setdefault(p, f["game"])
# 英雄卡按前缀归阵营（warlord_ids 键如 ASH1/BL35）
hero_by_game = {}
for k, v in warlord_ids.items():
    if isinstance(v, str) and "_" in v:
        pref = v.split("_")[0]
        game = PREF2GAME.get(pref)
        if game:
            hero_by_game.setdefault(game, set()).add(v.split("_", 1)[1])
# 补充：card_stats 里 type=hero 的卡名（更全）
for c in card_stats:
    if c.get("type") == "hero" and c.get("faction"):
        hero_by_game.setdefault(c["faction"], set()).add(c["name"])

deck_btn_map = json.load(open(os.path.join(PROJ, "data", "deck_btn_map.json"), encoding="utf-8"))
btn_to_card = deck_btn_map.get("btn_to_card", {})
btn_by_game = {}
btn_unmatched = []
for btn, card in btn_to_card.items():
    c = cards_by_name.get(card)
    if c:
        btn_by_game.setdefault(c["faction"], []).append(btn)
    else:
        btn_unmatched.append((btn, card))

# 阵营图标文件名映射（实际提取文件名 ≠ factions.json 名，GameData.army_icon_path() 已封装别名）
ICON_FILE = {
    "Ultramarines": "FactionUM", "Goff": "FactionOrks", "SaimHann": "FactionSaimHann",
    "Sautekh": "FactionSautekh", "BlackLegion": "FactionBlackLegion", "Leviathan": "FactionLeviathan",
    "TauEmpire": "FactionTauEmpire", "Sororitas": "FactionSororitas", "Genestealers": "Genestealers",
    "AstraMilitarum": "FactionAstraMilitarum", "DarkAngels": "FactionDarkAngels",
    "EmperorsChildren": "FactionEmperorsChildren", "SpaceWolves": None,
}

# 卡框文件名阵营名映射（与 factions.json 名不同：GSC/Orks/Tau/Astra Militarum 等）
FRAME_NAME = {
    "Ultramarines": "Ultramarines", "Goff": "Orks", "SaimHann": "SaimHann", "Sautekh": "Sautekh",
    "BlackLegion": "BlackLegion", "Leviathan": "Leviathan", "TauEmpire": "Tau", "Sororitas": "Sororitas",
    "Genestealers": "GSC", "AstraMilitarum": "Astra Militarum", "DarkAngels": "DarkAngels",
    "EmperorsChildren": "Emperor Children", "SpaceWolves": "Space Wolves",
}

# ---------------- 统计函数 ----------------
def stat(g):
    """返回某个阵营的统计 dict"""
    r = {}
    r["cn"] = g["cn"]; r["game"] = g["game"]; r["id"] = g["id"]
    # 卡牌
    r["cards_total"] = card_cnt.get(g["game"], 0)
    t = card_type.get(g["game"], Counter())
    r["cards_type"] = dict(t)
    # 01_卡牌 语音（解包源）
    ac = os.path.join(UNPACK, "01_卡牌", g["dir01"], "AudioClip")
    r["voice_unpack"] = count_ext(ac, ".ogg", ".wav")
    # 项目已同步语音/立绘/卡面
    r["voice_proj"] = count_ext(os.path.join(PROJ, "assets", "cards", "voice", g["dir01"]), ".ogg", ".wav")
    r["art_proj"] = count_ext(os.path.join(PROJ, "assets", "cards", "art", g["dir01"]), ".png")
    r["face_proj"] = count_ext(os.path.join(PROJ, "assets", "cards", "faces", g["dir01"]), ".png")
    r["face_thumbs"] = count_ext(os.path.join(PROJ, "assets", "cards", "faces_thumbs", g["dir01"]), ".png")
    r["art_unpack"] = count_ext(os.path.join(UNPACK, "01_卡牌", g["dir01"], "Texture2D"), ".png")
    # PnP 卡面（递归统计子目录）
    pnp_d = os.path.join(PNPS, g["pnp"])
    r["pnp_total"] = count_ext_recursive(pnp_d, ".png")
    r["pnp_exts"] = subdirs(pnp_d)
    # 卡框（顶层平铺：40k_Cardframe_<troop/stratagem>_<名>_tierN.png 新式 / 40k_Cardframes_<Troop/stratagem>_<名> 旧式）
    frame_files = files(CF, ".png")
    fname = FRAME_NAME[g["game"]]
    r["frame_total"] = sum(1 for f in frame_files
                           if re.match(rf"^40k_Cardframes?_(?:[Tt]roop|stratagem)_{re.escape(fname)}_tier\d+\.png$", f))
    r["frame_proj"] = count_ext(os.path.join(PROJ, "assets", "cards", "frames", g["game"]), ".png")
    # 卡背（按文件名前缀匹配，卡背目录顶层是 Cardback_<前缀>_*.png 文件）
    cb_dir_files = files(CB, ".png")
    cb_proj_files = files(os.path.join(PROJ, "assets", "deco", "cardbacks"), ".png")
    r["cb_pnp"] = {}; r["cb_proj"] = {}
    for p in g["cb"]:
        r["cb_pnp"][p] = sum(1 for f in cb_dir_files if f.startswith(f"Cardback_{p}"))
        r["cb_proj"][p] = sum(1 for f in cb_proj_files if f.startswith(f"Cardback_{p}"))
    # 督军立绘
    hero_list = sorted(hero_by_game.get(g["game"], []))
    r["heroes"] = hero_list
    portraits = files(os.path.join(UNPACK, "02_装饰品", "督军立绘", "Texture2D"), ".png")
    r["portrait_unpack"] = count_ext(os.path.join(UNPACK, "02_装饰品", "督军立绘", "Texture2D"), ".png")
    r["portrait_proj"] = count_ext(os.path.join(PROJ, "assets", "deco", "portraits"), ".png")
    # 头像（按文件名前缀匹配）
    av_dir_files = files(os.path.join(UNPACK, "02_装饰品", "头像", "Texture2D"), ".png")
    av_proj_files = files(os.path.join(PROJ, "assets", "ui", "avatars"), ".png")
    r["av_unpack"] = {}
    for p in g["av"]:
        r["av_unpack"][p] = sum(1 for f in av_dir_files if f.startswith(f"Avatar_{p}"))
    r["av_proj"] = len(av_proj_files)
    # 阵营图标（army_icons bundle 提取，实际文件名有别名）
    icon_name = ICON_FILE.get(g["game"])
    r["icon_file"] = icon_name
    r["army_icon"] = bool(icon_name and os.path.exists(os.path.join(
        PROJ, "assets", "ui", "army_icons", f"40k_DeckSelection_icon_{icon_name}.png")))
    # 卡组按钮
    r["deck_btns"] = sorted(btn_by_game.get(g["game"], []))
    # 联盟徽章 / 战役背景
    r["alliance"] = []
    for a in g["alliance"]:
        r["alliance"] += files(os.path.join(UNPACK, "02_装饰品", "联盟徽章", "Texture2D"), ".png") and \
            [f for f in files(os.path.join(UNPACK, "02_装饰品", "联盟徽章", "Texture2D"), ".png")
             if f.startswith("Alliance_Trophies_" + a + ".")] or []
    r["campaign_bg"] = []
    for b in g["bg"]:
        r["campaign_bg"] += [f for f in files(os.path.join(UNPACK, "02_装饰品", "战役奖励背景", "Texture2D"), ".png")
                             if f.startswith("Campaign_Faction_Bck_" + b)]
    r["flavortext"] = []
    for b in g["bg"]:
        r["flavortext"] += [f for f in files(os.path.join(UNPACK, "02_装饰品", "战役奖励背景", "Texture2D"), ".png")
                            if f.startswith("40K_display_Flavortext " + b + ".")]
    # 战场场景/模型（07_场景 递归 json 计数）
    scene_d = os.path.join(UNPACK, "07_场景")
    r["scene_total"] = 0
    if g["scene"]:
        r["scene_total"] = count_ext_recursive(os.path.join(scene_d, "battlearena" + g["scene"]), ".json")
    model_d = os.path.join(UNPACK, "06_模型")
    r["model_obj"] = count_ext(os.path.join(model_d, g["model"]), ".obj") if g["model"] else 0
    # 音效库带阵营名（词边界匹配，避免 Taunt 误命中 Tau）
    sfx = files(os.path.join(UNPACK, "04_音频", "音效库", "AudioClip"), None)
    names = [g["pnp"]]
    if g["game"] == "Goff": names = ["Ork", "Goff"]
    pats = [re.compile(r"(?i)(^|[^A-Za-z])" + re.escape(n) + r"($|[^A-Za-z])") for n in names]
    r["sfx"] = sorted({f for f in sfx if any(p.search(f) for p in pats)})
    # 教程语音
    tut = []
    for t in g.get("tut", []):
        tut += [f for f in files(os.path.join(UNPACK, "04_音频", "督军语音", "AudioClip"), ".ogg") if f.startswith(t + "_")]
    r["tutorial"] = tut
    return r

stats = [stat(g) for g in FACTIONS]

# ---------------- 通用资源 ----------------
def generic_cb():
    """通用卡背（All/Ranked/Season 前缀）"""
    files_all = files(CB, ".png")
    out = {}
    for p in GENERIC_CB:
        out[p] = sum(1 for f in files_all if f.startswith(f"Cardback_{p}"))
    return out

def generic_av():
    """通用头像（Player/WF/All 前缀；Player 实际文件名为 Player_Avatar_selected.png）"""
    files_all = files(os.path.join(UNPACK, "02_装饰品", "头像", "Texture2D"), ".png")
    out = {}
    for p in GENERIC_AV:
        out[p] = sum(1 for f in files_all if f.startswith(f"Avatar_{p}"))
    out["Player"] = sum(1 for f in files_all if f.startswith("Player_Avatar"))
    return out

# ---------------- 输出 markdown ----------------
L = []
A = L.append
A("# Warpforge 按阵营资源索引")
A("")
A("> 用途：各种族资源（语音/图标/卡图/立绘/音效等）散落在解包整理与游戏项目中，本索引按 13 阵营汇总路径，查询资源先查这里。")
A("> 生成：2026-08-17 ｜ 脚本：`Warpforge_tools/scripts/faction_resources_index.py`（可重跑）")
A("> 路径约定：`解包整理/` = `D:\\2\\解包整理\\`；`项目` = `D:\\warpforge\\`；`PnP` = `D:\\2\\Warpforge部队卡片\\`；`卡背` = `D:\\2\\Warpforge Cardbacks\\`；`卡框` = `D:\\2\\Warpforge cardframes\\`")
A("")
A("## 一、13 阵营对照表")
A("")
A("| 阵营 | ID | factions.json | PnP 目录 | 01_卡牌 目录 | 语音前缀 | 卡背前缀 | 头像前缀 | 联盟徽章名 | 战役背景名 | 战场场景 |")
A("|---|---|---|---|---|---|---|---|---|---|---|")
for g, s in zip(FACTIONS, stats):
    A(f"| {g['cn']} | {g['id']} | {g['game']} | {g['pnp']} | {g['dir01']} | {'/'.join(g['vo'])} | {'/'.join(g['cb'])} | {'/'.join(g['av'])} | {'/'.join(g['alliance'])} | {'/'.join(g['bg'])} | battlearena{g['scene'] or '—'} |")
A("")
A("**命名规律说明**：")
A("- 阵营 ID/英文名以 `D:\\warpforge\\data\\factions.json` 为准（Goff=Orks、SaimHann=Aeldari、Sautekh=Necrons、Leviathan=Tyranids、Genestealers=基因窃取者教派）")
A("- `01_卡牌/` 与 `项目 assets/cards/{art,voice,faces}/` 用**中文目录名**（Ultramarines_极限战士 等）；`卡框/卡背` 用**前缀体系**（见下表）")
A("- 语音文件名前缀：VO_UM_*/VO_AM_*/VO_BL_*/VO_DA_*/VO_CSM_EC_*/VO_GSC_*/VO_Sautekh_*/VO_Goff_*/VO_ADS_*/VO_SpaceWolves_*/VO_Tau_Empire_*/VO_Tyranid_Leviathan_*/VO_CW_SaimHann_*")
A("")
A("## 二、通用资源（非阵营专属）")
A("")
A(f"- **卡背通用**（卡背目录 Cardback_ 前缀）：All={generic_cb().get('All',0)} 张（Closed alpha/Early Backer/Premium 等）、Ranked={generic_cb().get('Ranked',0)} 张（排位 Generic/Skirmish Tier1-3）、Season={generic_cb().get('Season',0)} 张（赛季）")
A(f"- **头像通用**（Avatar_ 前缀）：Player={generic_av().get('Player',0)}（玩家默认）、WF={generic_av().get('WF',0)}、All={generic_av().get('All',0)}")
A("- **中立/通用音效库**（`04_音频/音效库/` 共 618 个）：Ambush/Artifice/Shield/Explosion 等通用战斗音效，无阵营归属（战斗特效阶段用）")
A("")
A("## 三、按阵营资源清单")
A("")
for g, s in zip(FACTIONS, stats):
    A(f"### {g['cn']}（{g['game']}，ID {g['id']}）")
    A("")
    A(f"**卡牌**：`项目 data/card_stats.json` 共 **{s['cards_total']} 张**（" +
      "，".join(f"{k} {v}" for k, v in s['cards_type'].items()) + f"）｜卡框 `卡框/{g['game']}/` {s['frame_total']} 张（troop/stratagem × tier1-4）→ 已同步 `项目 assets/cards/frames/`")
    if g["note"]: A(f"> 📌 {g['note']}")
    A("")
    A(f"| 资源 | 解包源 | 项目已同步 | 说明 |")
    A("|---|---|---|---|")
    A(f"| 语音 | `解包整理/01_卡牌/{g['dir01']}/AudioClip/` **{s['voice_unpack']} 个** | `assets/cards/voice/{g['dir01']}/` {s['voice_proj']} 个 | 卡牌台词+督军情绪语音（attack/death/gen1-7 等），文件名前缀 {'/'.join(g['vo'])} |")
    A(f"| 卡图立绘 | `01_卡牌/{g['dir01']}/Texture2D/` {s['art_unpack']} 张 | `assets/cards/art/{g['dir01']}/` {s['art_proj']} 张 | ⚠️ 卡图已弃用（PnP 完整卡面替代），立绘部分仍可做背景/头像 |")
    A(f"| PnP 完整卡面 | `PnP/{g['pnp']}/` **{s['pnp_total']} 张** | `assets/cards/faces/` {s['face_proj']} 张 + 缩略图 {s['face_thumbs']} | 扩展：{' / '.join(s['pnp_exts']) or '—'}（900×1200 原版卡面，图鉴/对战在用） |")
    A(f"| 卡背 | `卡背/Cardback_{'/','Cardback_'.join(g['cb'])}`" if False else f"| 卡背 | `卡背/Cardback_{' 或 Cardback_'.join(g['cb'])}*` {sum(s['cb_pnp'].values())} 张 | `assets/deco/cardbacks/` {sum(s['cb_proj'].values())} 张 | 前缀 {'/'.join(g['cb'])}；另有通用 All/Ranked/Season 共 {sum(generic_cb().values())} 张 |")
    A(f"| 督军立绘 | `02_装饰品/督军立绘/Texture2D/UI_Deck_Warlord_*` {s['portrait_unpack']} 张 | `assets/deco/portraits/` {s['portrait_proj']} 张 | 本阵营英雄 {len(s['heroes'])} 名：{('、'.join(s['heroes'][:6]) + (' 等' if len(s['heroes'])>6 else '')) if s['heroes'] else '—'} |")
    av_desc = "、".join(f"{p} {n}" for p, n in s['av_unpack'].items())
    A(f"| 头像 | `02_装饰品/头像/Texture2D/Avatar_{' 或 Avatar_'.join(g['av'])}*` {sum(s['av_unpack'].values())} 张 | `assets/ui/avatars/` {s['av_proj']} 张(128px) | 前缀 {av_desc}；472 张总数含通用 |")
    icon = "✅ 有" if s["army_icon"] else "❌ 无（SpaceWolves 唯一缺失，代码回退首字母）"
    A(f"| 阵营图标 | armyicons_assets_all bundle | `assets/ui/army_icons/40k_DeckSelection_icon_{s['icon_file']}.png` | {icon}（GameData.army_icon_path() 已封装别名） |")
    A(f"| 卡组按钮 | deckselectionbuttons bundle（84 张） | `assets/ui/deck_buttons/40k_DeckSelection_bt_*.png`（329²）+ 缩略图 | 本阵营按钮 {len(s['deck_btns'])} 个{('：' + '、'.join(s['deck_btns'][:6]) + (' 等' if len(s['deck_btns'])>6 else '')) if s['deck_btns'] else '（无）'} |")
    A(f"| 联盟徽章 | `02_装饰品/联盟徽章/Texture2D/Alliance_Trophies_*` | — | {len(s['alliance'])} 张：{'、'.join(s['alliance'][:4]) or '—'}{' 等' if len(s['alliance'])>4 else ''} |")
    A(f"| 战役奖励背景 | `02_装饰品/战役奖励背景/Texture2D/Campaign_Faction_Bck_*` | — | {len(s['campaign_bg'])} 张 + 卡面文字背景 40K_display_Flavortext {len(s['flavortext'])} 张 |")
    A(f"| 战场场景 | `07_场景/battlearena{g['scene'] or '—'}/` {s['scene_total']} 个 JSON | — | 场景说明（Unity 序列化） |")
    A(f"| 战场模型 | `06_模型/{g['model'] or '—'}/` {s['model_obj']} 个 OBJ | — | 场景烘焙散件（需拼接） |")
    A(f"| 专属音效 | `04_音频/音效库/AudioClip/` 文件名含阵营名 | — | {len(s['sfx'])} 个：{'、'.join(s['sfx'][:5]) or '—'}{' 等' if len(s['sfx'])>5 else ''} |")
    if s["tutorial"]:
        A(f"| 教程语音 | `04_音频/督军语音/AudioClip/` | — | {len(s['tutorial'])} 个：{s['tutorial'][0]} 等（{g.get('tut',[''])[0]} 教程） |")
    else:
        A(f"| 教程语音 | — | — | 无（教程1=极限战士 Calgar/Ventris，教程2=兽人 Ghazghkull/Makari） |")
    A("")
    A("---")
    A("")

A("## 四、未按阵营分组的资源（查询指引）")
A("")
A("| 资源 | 位置 | 说明 |")
A("|---|---|---|")
A("| 战斗 UI（60 sprite） | `项目 assets/ui/battle/` + `atlasindividual_assets_battleatlasui` bundle | 通用：能量/结束回合/玩家框/日志框/攻击按钮/骷髅/回放按钮 |")
A("| 主菜单 UI | `项目 assets/ui/mainmenu/`（menus_sprites 883 张等） | 通用界面纹理，无阵营属性 |")
A("| 音乐 2 首 | `04_音频/音乐/` → `assets/audio/` | Main Theme / Menu Idle Theme |")
A("| 音频控制 | `04_音频/音频控制/` | AudioMixer 定义（Unity 对象） |")
A("| 卡背通用 | 卡背目录 Cardback_All/Ranked/Season | 非阵营（Close alpha/排位/赛季） |")
A("| 督军立绘通用 | `02_装饰品/督军立绘/Texture2D/` | UI_Deck_Draft Generic Image 等 |")
A("| 模型通用 | `06_模型/battleprefabs_vfxandmisc`（124 obj）/ `battlesharedresources`（246 obj）/ `boosterpacks` / `menus` | 特效/共享建筑/开包/菜单模型 |")
A("| 场景通用 | `07_场景/battlearena3`（空）/ `mainmenuwarpforge` / `simpletransition` | 主菜单/转场场景 |")
A("| 动画 | `01_卡牌/<阵营>/动画/` | 卡牌动画（AssetBundle/MonoBehaviour 定义） |")
A("| 卡组数据 | `01_卡牌/卡组数据/` | AssetBundle/MonoBehaviour 定义（236 套预组卡组已导出 prebuilt_decks_full.json） |")
A("")
A("## 五、卡背/头像前缀速查")
A("")
A("| 前缀 | 阵营 | 前缀 | 阵营 |")
A("|---|---|---|---|")
pairs = [("AM","星界军"),("ASH","灵族"),("BL","黑色军团"),("CSM","帝皇之子"),("DA","暗黑天使"),("EC","帝皇之子(旧1张)"),("GOF","兽人"),("ORK","兽人"),("GSC","基因窃取者"),("SAU","死灵"),("SOR","战斗修女"),("SW","太空野狼"),("TAU","钛帝国"),("TL","泰伦"),("UM","极限战士"),("All/Ranked/Season","通用")]
for i in range(0, len(pairs), 2):
    row = " | ".join(pairs[i])
    if i+1 < len(pairs):
        row += " | " + " | ".join(pairs[i+1])
    else:
        row += " | | "
    A("| " + row + " |")
A("")
A("> 头像前缀另有 Player（玩家默认）/WF（通用）。卡背前缀仅作文件名前缀匹配（如 Cardback_CSM_EmperorsChildren_* 是帝皇之子）。")
A("")
A("## 六、数据源统计")
A("")
A(f"- 卡牌总数：{sum(s['cards_total'] for s in stats)} 张（card_stats.json）")
A(f"- 语音：解包 {sum(s['voice_unpack'] for s in stats)} 个（01_卡牌 AudioClip），项目已同步 {sum(s['voice_proj'] for s in stats)} 个")
A(f"- PnP 卡面：{sum(s['pnp_total'] for s in stats)} 张；项目 faces {sum(s['face_proj'] for s in stats)} 张")
A(f"- 卡背：PnP {sum(sum(s['cb_pnp'].values()) for s in stats)} 张（+通用 {sum(generic_cb().values())} = 233）")
A(f"- 头像：解包 {sum(sum(s['av_unpack'].values()) for s in stats)} 张（+通用 {sum(generic_av().values())} = 472）")
A(f"- 卡组按钮命中：{sum(len(s['deck_btns']) for s in stats)}/84（未命中 {len(btn_unmatched)}：{('、'.join(str(c) for _, c in btn_unmatched[:5])) if btn_unmatched else '—'} 等）")
A(f"- 战场场景：10 个专属（aeldari/astramilitarum/blacklegion/darkangels/emperorschildren/genestealers/leviathan/sororitas/spacewolves/tauviorla）+ battlearena1(通用默认)/2(兽人风格)/3(空)；模型 obj 总数 {sum(s['model_obj'] for s in stats)}（场景 9 套）")

open(r"D:\2\按阵营资源索引.md", "w", encoding="utf-8").write("\n".join(L))
print("生成完成: D:\\2\\按阵营资源索引.md")
print(f"卡牌 {sum(s['cards_total'] for s in stats)} / 语音 {sum(s['voice_unpack'] for s in stats)} / PnP {sum(s['pnp_total'] for s in stats)} / 卡背 {sum(sum(s['cb_pnp'].values()) for s in stats)} / 头像 {sum(sum(s['av_unpack'].values()) for s in stats)} / 按钮 {sum(len(s['deck_btns']) for s in stats)}/84")
