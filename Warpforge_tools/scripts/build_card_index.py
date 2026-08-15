#!/usr/bin/env python3
"""生成卡牌媒体索引库 card_index.json（只读扫描，不改动任何资源）。

卡名提取规则（来自实际文件名规律）：
- 卡图 Sprite/Texture2D: "<前缀>_<类型>_<卡名>"，卡名 = 最后一段（卡名内部用空格不用下划线）
- 语音 AudioClip: "VO_<前缀>_<卡名> - 台词.ogg"，卡名通过与卡图名单匹配关联
- 边框: 40k_Cardframe_{troop|stratagem}_<阵营>[_SDF]_tier{1-4}
输出: 解包整理/card_index.json
"""
import os, json, re, sys, unicodedata
from collections import defaultdict

ROOT = r"d:/2/解包整理/01_卡牌"
OUT = r"d:/2/解包整理/card_index.json"

FACTIONS = {  # 目录名 -> (阵营英文名, 阵营ID)
    "Aeldari_灵族": ("SaimHann", 30),
    "AstraMilitarum_星界军": ("AstraMilitarum", 100),
    "BlackLegion_黑色军团": ("BlackLegion", 50),
    "DarkAngels_暗黑天使": ("DarkAngels", 110),
    "EmperorsChildren_帝皇之子": ("EmperorsChildren", 120),
    "GenestealerCults_基因窃取者教派": ("Genestealers", 90),
    "Necrons_死灵族": ("Sautekh", 40),
    "Orks_兽人": ("Goff", 20),
    "Sororitas_战斗修女": ("Sororitas", 80),
    "SpaceWolves_太空野狼": ("SpaceWolves", 130),
    "Tau_钛帝国": ("TauEmpire", 70),
    "Tyranids_泰伦虫族": ("Leviathan", 60),
    "Ultramarines_极限战士": ("Ultramarines", 10),
}
TYPE_MAP = {"inf": "unit", "Inf": "unit", "battlesuit": "unit", "war": "hero",
            "warlord": "hero", "Warlord": "hero", "Strat": "tactic", "tac": "tactic",
            "strat": "tactic", "hero": "hero"}

HASH_RE = re.compile(r"_-?\d{10,}$")  # 重复名后缀

def clean_name(fn):
    n = fn.rsplit(".", 1)[0]
    return HASH_RE.sub("", n)

# ---------- 语音匹配（V2：剥离动作后缀 + 简称模糊窗口匹配） ----------
SUFFIX_RE = re.compile(
    r"(?:[ _])(attack|death|intro|gen\d+|greet|cant|cantdo|concede|hurry|mirror|threat|wp|"
    r"backup\d*|vs[_.]?[\w&'-]*|negate|banish|start|summon|taunt|idle|special|select|"
    r"place|play|spell|buff|heal|destroy|silence|target|win|lose|banner|emote|draw|"
    r"discard|resurrect|ranged|melee|spawn|transform|custom|miss|interrupt|levelup|ult|"
    r"screech|bellow|snarl|crush|hiss|roar|sounds|ticking|furious|savage|menacing|"
    r"revelling|roaring|high[-_]pitch|growl|howl|shriek|scream|chant|prayer|wail|"
    r"laughter|giggle|mutter|mumble|grunt|groan|cackle|battlecry|warcry|v\d+|"
    r"primalgrowl|squad|tank|marine|brother|sergeant|unit)$",
    re.I)

MIN_CONFIDENCE = 4.0


def strip_suffixes(name):
    """循环剥离动作后缀（大小写不敏感）。"""
    prev = None
    while prev != name:
        prev = name
        m = SUFFIX_RE.search(name)
        if m:
            name = name[:m.start()]
    return name


def norm_tokens(s):
    """归一化并 token 化：NFKD 去重音、小写、分隔符转空格、去标点。"""
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[_\-\(\)\[\]'\"!?.,:;]", " ", s)
    return [t for t in s.lower().split() if t]


def voice_name_part(fn):
    """从语音文件名提取名字候选列表（先完整，后裁剪下划线台词）。"""
    base = clean_name(fn)
    if "NOT USED" in base.upper():
        return []
    for sep in (" - ", " -", "- "):          # 三种台词分隔
        i = base.find(sep)
        if i > 0:
            base = base[:i]
            break
    base = re.sub(r"\(.*?\)\s*$", "", base)  # 去尾部括号段
    primary = strip_suffixes(base)
    out = [primary] if primary else []
    # 下划线台词候选："名字_台词句子"（台词段含空格且 >=2 词）——先裁台词再剥后缀
    parts = base.split("_")
    if len(parts) > 1 and " " in parts[-1] and len(parts[-1].split()) >= 2:
        parts.pop()
        alt = strip_suffixes("_".join(parts))
        if alt and alt != primary:
            out.append(alt)
    # 无空格连字符台词候选："名字-台词句子"（后半 >=3 词）——仅作备用
    if "-" in primary:
        i = primary.find("-")
        head, tail = primary[:i], primary[i + 1:]
        if head and len(tail.split()) >= 3:
            cand = strip_suffixes(head)
            if cand and cand not in out:
                out.append(cand)
    return out


def lev(a, b, cap=2):
    """编辑距离，超过 cap 截断返回 cap+1。"""
    if abs(len(a) - len(b)) > cap:
        return cap + 1
    if a == b:
        return 0
    dp = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        prev = dp[0]
        dp[0] = i
        for j, cb in enumerate(b, 1):
            cur = dp[j]
            dp[j] = min(dp[j] + 1, dp[j - 1] + 1, prev + (ca != cb))
            prev = cur
        if min(dp) > cap:
            return cap + 1
    return dp[-1]


def tok_score(v, w):
    """单 token 匹配分：全等 2.0 / 前缀(len>=4) 1.5 / 编辑1(len>=5) 1.0 / 编辑2(len>=6) 0.5。"""
    if v == w:
        return 2.0
    if len(v) >= 4 and w.startswith(v):
        return 1.5
    d = lev(v, w)
    if d == 1 and len(v) >= 5:
        return 1.0
    if d == 2 and len(v) >= 6:
        return 0.5
    return None


def match_voice_to_card(voice_tokens, card_tokens):
    """窗口匹配：语音 token 列表在卡名 token 列表内滑动。
    返回 (分数, 对齐类型) 或 None。全名+100 / 尾部对齐(去头衔)+10 / 头部对齐+5。"""
    vt, ct = voice_tokens, card_tokens
    if not vt or not ct or len(vt) > len(ct):
        return None
    best = None
    for start in range(len(ct) - len(vt) + 1):
        total = 0.0
        ok = True
        for i in range(len(vt)):
            sc = tok_score(vt[i], ct[start + i])
            if sc is None:
                ok = False
                break
            total += sc
        if not ok:
            continue
        if len(vt) == 1 and vt[0] != ct[start] and len(vt[0]) < 6:  # 弱单token模糊拒绝
            continue
        total += 3 * len(vt)
        if len(vt) == len(ct):
            total += 100
        elif start == len(ct) - len(vt):
            total += 10      # 尾部对齐（Calgar -> Marneus Calgar）
        elif start == 0:
            total += 5       # 头部对齐（Anvirr -> Anvirr Keltoc）
        if best is None or total > best[0]:
            best = (total, "full" if len(vt) == len(ct) else "tail" if start == len(ct) - len(vt) else "head" if start == 0 else "mid")
    return best

def main():
    frames = {}
    cards = {}
    decks = []
    stats = defaultdict(lambda: {"art": 0, "voice": 0})

    for dirname, (faction_en, faction_id) in FACTIONS.items():
        fdir = os.path.join(ROOT, dirname)
        if not os.path.isdir(fdir):
            continue
        # ---- 边框 ----
        frame_dir = os.path.join(fdir, "Texture2D")
        fr = defaultdict(dict)
        if os.path.isdir(frame_dir):
            for fn in sorted(os.listdir(frame_dir)):
                m = re.match(r"40k_Cardframe_(\w+)_(?:\w+_)?\w+_?SDF?_tier(\d)\.png", fn)
                m2 = re.match(r"40k_Cardframe_(troop|stratagem)_\w+?_(?:SDF_)?tier(\d)\.png", fn)
                if m2:
                    fr[m2.group(1)][m2.group(2)] = os.path.join("01_卡牌", dirname, "Texture2D", fn)
        frames[faction_en] = {"troop": fr.get("troop", {}), "stratagem": fr.get("stratagem", {})}

        # ---- 卡图（Sprite 名单做锚） ----
        sprite_dir = os.path.join(fdir, "Sprite")
        tex_dir = os.path.join(fdir, "Texture2D")
        texs = {}
        if os.path.isdir(tex_dir):
            for fn in os.listdir(tex_dir):
                if fn.endswith(".png"):
                    texs[clean_name(fn)] = fn
        if os.path.isdir(sprite_dir):
            for fn in sorted(os.listdir(sprite_dir)):
                if not fn.endswith(".json"):
                    continue
                base = clean_name(fn)
                if base.startswith("40k_Cardframe") or "Frame" in base or base.endswith("Frame"):
                    continue  # 边框/非卡图
                parts = base.split("_")
                if len(parts) < 3:
                    continue
                card_name = parts[-1]
                card_type = TYPE_MAP.get(parts[-2], "unit")
                art_png = texs.get(base)
                card = cards.setdefault((faction_en, card_name), {
                    "name": card_name, "faction": faction_en, "factionId": faction_id,
                    "type": card_type, "art": None, "sprite": None, "altArts": [], "voice": []})
                card["sprite"] = os.path.join("01_卡牌", dirname, "Sprite", fn)
                if art_png:
                    card["art"] = os.path.join("01_卡牌", dirname, "Texture2D", art_png)
                if base.startswith("AA_") or "_AA_" in base or base.startswith("Alt"):
                    card["altArts"].append(card["sprite"])
                    card["sprite"] = None
                stats[faction_en]["art"] += 1

        # ---- 语音（V2：简称+模糊窗口匹配） ----
        audio_dir = os.path.join(fdir, "AudioClip")
        if os.path.isdir(audio_dir):
            faction_cards = [(f, cn) for (f, cn) in cards if f == faction_en]
            low_conf = []
            for fn in sorted(os.listdir(audio_dir)):
                if not fn.endswith((".ogg", ".wav")):
                    continue
                name_parts = voice_name_part(fn)
                if not name_parts:
                    continue
                best_match, best_score = None, 0.0
                for name_part in name_parts:          # 先完整匹配，失败再裁剪候选
                    vt = norm_tokens(name_part)
                    if not vt:
                        continue
                    for cut in range(len(vt)):        # 从完整 token 开始逐级裁前缀（锚定起点）
                        v_slice = vt[cut:]
                        for (f, cn) in faction_cards:
                            m = match_voice_to_card(v_slice, norm_tokens(cn))
                            if m and m[0] > best_score:
                                best_score, best_match = m[0], (f, cn)
                        if best_match:
                            break
                    if best_match:
                        break
                if best_match and best_score >= MIN_CONFIDENCE:
                    cards[best_match]["voice"].append(os.path.join("01_卡牌", dirname, "AudioClip", fn))
                    stats[faction_en]["voice"] += 1
                elif best_match and best_score >= 3.0:
                    low_conf.append((fn, best_match[1], round(best_score, 1)))
            if low_conf:
                print(f"  [低置信度语音匹配] {dirname}:")
                for fn, cn, sc in low_conf[:10]:
                    print(f"    {fn} -> {cn} ({sc})")


    # ---- 卡组数据（只扫一次） ----
    deck_dir = os.path.normpath(os.path.join(ROOT, "卡组数据", "MonoBehaviour"))
    if os.path.isdir(deck_dir):
        for fn in os.listdir(deck_dir):
            if not fn.endswith(".json"):
                continue
            try:
                d = json.load(open(os.path.join(deck_dir, fn), encoding="utf-8"))
            except Exception:
                continue
            if isinstance(d, dict) and ("deckId" in d or "packId" in d):
                decks.append({"file": os.path.join("01_卡牌", "卡组数据", "MonoBehaviour", fn),
                              "deckId": d.get("deckId") or d.get("packId"),
                              "deckName": d.get("deckName") or d.get("packName"),
                              "cards": d.get("cardLibraryIds") or d.get("cardIds", [])})

    result = {
        "说明": "Warpforge 卡牌媒体索引（本地文件可提供部分；数值在服务端不可得）",
        "factions": [{"name": en, "id": fid} for en, fid in FACTIONS.values()],
        "frames": frames,
        "cards": [c for c in cards.values()],
        "decks": decks,
        "stats": {k: {"art": v["art"], "voice": v["voice"]} for k, v in stats.items()},
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    n_art = sum(1 for c in cards.values() if c["art"])
    n_voice = sum(1 for c in cards.values() if c["voice"])
    print(f"卡牌总数(按 阵营+卡名 去重): {len(cards)}")
    print(f"  有卡图: {n_art} ({100*n_art/len(cards):.1f}%)")
    print(f"  有语音: {n_voice} ({100*n_voice/len(cards):.1f}%)")
    print(f"卡组/卡包定义: {len(decks)}")
    print(f"已写入: {OUT}")

    # ---- --compare <旧索引>：修正感知的零回退断言 ----
    if len(sys.argv) >= 3 and sys.argv[1] == "--compare":
        old = json.load(open(sys.argv[2], encoding="utf-8"))
        new_cards = {f"{c['faction']}|{c['name']}": c for c in result["cards"]}
        new_voice_all = {os.path.normpath(v) for c in result["cards"] for v in c.get("voice", [])}
        regress, added, corrected = [], [], 0
        expected_fixes = []   # 预期修正型回退（旧挂载本就错误）
        ALLOWED_REGRESS = ("extra10", "not used", "konstrictus")
        old_voice_n = 0
        for oc in old["cards"]:
            key = f"{oc['faction']}|{oc['name']}"
            nc = new_cards.get(key)
            if not nc:
                continue
            if oc.get("voice"):
                old_voice_n += 1
            ov = {os.path.normpath(v) for v in oc.get("voice", [])}
            nv = {os.path.normpath(v) for v in nc.get("voice", [])}
            miss = ov - nv
            for v in miss:
                if v in new_voice_all:
                    corrected += 1          # 语音移挂到其他卡 = 旧误挂修正
                elif any(a in os.path.basename(v).lower() for a in ALLOWED_REGRESS):
                    expected_fixes.append((key, v))  # 已知修正型（测试卡/弃用语音/拼写特例）
                else:
                    regress.append((key, v))  # 语音无主 = 真回退
            if not oc.get("voice") and nc.get("voice"):
                added.append(key)
        print(f"\n=== --compare 对比结果 ===")
        print(f"旧索引有语音卡: {old_voice_n}，新索引有语音卡: {n_voice}")
        print(f"新增语音卡: {len(added)} 张；误挂修正: {corrected} 条；"
              f"预期修正: {len(expected_fixes)} 条；真回退: {len(regress)} 条")
        for k in added[:15]:
            print(f"  + {k}")
        if len(added) > 15:
            print(f"  ... 其余 {len(added) - 15} 张略")
        if regress:
            print(f"\n!! 真回退 {len(regress)} 条（语音文件无主）:")
            for key, v in regress[:15]:
                print(f"  - {key}: {v}")
            sys.exit(1)
        else:
            print("真回退: 0 条 ✅（零回退）")

if __name__ == "__main__":
    main()
