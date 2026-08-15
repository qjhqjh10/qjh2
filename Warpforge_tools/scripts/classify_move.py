#!/usr/bin/env python3
"""将 Warpforge_assets_full 按内容分类整理到 解包整理/ 文件夹（移动，不复制）。
移动清单写入 解包整理/manifest.json（目录级，可逆）。
用法: python classify_move.py
"""
import os, json, shutil

SRC = r"d:/2/Warpforge_assets_full"
DST = r"d:/2/解包整理"

FACTIONS = [
    ("aeldarisaimhann", "Aeldari_灵族"),
    ("astramilitarum", "AstraMilitarum_星界军"),
    ("chaosspacemarinesblacklegion", "BlackLegion_黑色军团"),
    ("chaosspacemarinesemperorschildren", "EmperorsChildren_帝皇之子"),
    ("genestealercults", "GenestealerCults_基因窃取者教派"),
    ("necronssautekh", "Necrons_死灵族"),
    ("orksgoff", "Orks_兽人"),
    ("sororitas", "Sororitas_战斗修女"),
    ("spacemarinesdarkangels", "DarkAngels_暗黑天使"),
    ("spacemarinesspacewolves", "SpaceWolves_太空野狼"),
    ("spacemarinesultramarines", "Ultramarines_极限战士"),
    ("tauempire", "Tau_钛帝国"),
    ("tyranidsleviathan", "Tyranids_泰伦虫族"),
]

GATHER = {  # 跨包收集的类型 -> 目标目录
    "Mesh": "06_模型",
    "Font": "10_字体",
    "VideoClip": "05_视频",
    "Shader": "11_着色器",
}

def base_of(dirname):
    name = dirname
    if name.startswith("bundle_"):
        name = name[len("bundle_"):]
    for suf in ("_assets_all", ".assets", ".resource"):
        if name.endswith(suf):
            name = name[: -len(suf)]
    return name

def short_of(dirname):
    """短名称用于收集目录（去掉 bundle_ / 阵营前缀部分）。"""
    b = base_of(dirname)
    b = b.replace("_assets_all", "").replace(".assets", "")
    return b

def faction_of(base):
    for k, v in FACTIONS:
        if base.startswith(k):
            return v
    return None

def bundle_target(dirname):
    """整包移动目标；返回 None 表示不该整包移动（内容已被收集或不存在）。"""
    base = base_of(dirname)
    if "cardassets" in base:
        f = faction_of(base)
        if f:
            return f"01_卡牌/{f}"
        return "01_卡牌/卡牌资源"
    if "cardanims" in base:
        f = faction_of(base)
        return f"01_卡牌/{f}/动画" if f else "01_卡牌/卡牌动画"
    if base == "cardanimsgeneral":
        return "01_卡牌/通用动画"
    if base in ("draftpacks", "prebuiltdecks"):
        return "01_卡牌/卡组数据"
    if base == "cosmeticavatarsimages":
        return "02_装饰品/头像"
    if base == "cosmeticscardbacksimages":
        return "02_装饰品/卡背"
    if base == "cosmeticsso":
        return "02_装饰品/定义数据"
    if base == "uiwarlords":
        return "02_装饰品/督军立绘"
    if base == "flavourframes":
        return "02_装饰品/边框"
    if base == "campaignrewardbackgrounds":
        return "02_装饰品/战役奖励背景"
    if base == "alliancesbadgesimages":
        return "02_装饰品/联盟徽章"
    if base == "soundcollection":
        return "04_音频/音效库"
    if base == "menumusic":
        return "04_音频/音乐"
    if base == "tutorialwarlordchats":
        return "04_音频/督军语音"
    if base.startswith("scenes_scenes"):
        return "07_场景/" + base[len("scenes_scenes"):]
    if base == "battleprefabs_vfxandmisc":
        return "08_预制体特效/战斗预制体"
    if base == "battlesharedresources":
        return "08_预制体特效/共享资源"
    if base == "boosterpacks":
        return "09_游戏数据/卡包"
    if base == "tutorialso":
        return "09_游戏数据/教程"
    if base == "tweenandshakes":
        return "09_游戏数据/动画曲线"
    if base == "duplicateassetisolationso":
        return "09_游戏数据/去重定义"
    if base == "Waprforge_monoscripts":
        return "09_游戏数据/脚本定义"
    if base == "Warpforge_unitybuiltinassets":
        return "12_主程序资源/内置资源"
    if base.startswith("atlasindividual"):
        sub = base[len("atlasindividual_assets_"):]
        return f"03_界面UI/图集/{sub}"
    if base == "atlasgroup":
        return "03_界面UI/图集"
    if base == "menus":
        return "03_界面UI/菜单"
    if base == "menusharedresources":
        return "03_界面UI/共享资源"
    if base == "mainmenualwaysloaded":
        return "03_界面UI/主菜单"
    if base == "generalgamewindows":
        return "03_界面UI/通用窗口"
    if base == "armycursors":
        return "03_界面UI/光标"
    if base == "armyicons":
        return "03_界面UI/军队图标"
    if base == "deckselectionbuttons":
        return "03_界面UI/卡组选择按钮"
    if base == "rankeddivisionicons":
        return "03_界面UI/排位图标"
    if base == "liveopsicons":
        return "03_界面UI/运营图标"
    if base == "liveopsmenuimages":
        return "03_界面UI/运营菜单图"
    if base == "inboxmessagesheaderslocal":
        return "03_界面UI/收件箱横幅"
    if base == "specialofferscontentlocal":
        return "03_界面UI/特惠内容"
    if base == "duplicateassetisolation":
        return "03_界面UI/去重资源"
    if base == "staticgeneralassets":
        return "03_界面UI/通用静态资源"
    if base == "audiocontrol":
        return "04_音频/音频控制"
    if base == "fonts":
        return "10_字体/字体资源"
    if base == "shaders":
        return "11_着色器/配套材质"
    if base == "videos":
        return "05_视频"
    if base.startswith(("globalgamemanagers", "resources", "sharedassets", "level")):
        return "12_主程序资源"
    return f"99_其他/{dirname}"

def move_merge(src, dst, manifest, collision_prefix=""):
    """把 src 目录/文件移入 dst（dst 已存在时合并；文件重名加前缀）。"""
    if os.path.isfile(src):
        d = os.path.join(dst, os.path.basename(src))
        if os.path.exists(d):
            d = os.path.join(dst, collision_prefix + os.path.basename(src))
        os.makedirs(dst, exist_ok=True)
        shutil.move(src, d)
        manifest.append({"from": src, "to": d})
        return
    if not os.path.isdir(src):
        return
    os.makedirs(dst, exist_ok=True)
    for entry in sorted(os.listdir(src)):
        s = os.path.join(src, entry)
        t = os.path.join(dst, entry)
        if os.path.isdir(s):
            if os.path.isdir(t):
                move_merge(s, t, manifest, collision_prefix)  # 递归合并
            else:
                shutil.move(s, t)
                manifest.append({"from": s, "to": t})
        else:
            if os.path.exists(t):
                stem, ext = os.path.splitext(entry)
                t = os.path.join(dst, f"{stem}_{os.path.basename(src)}{ext}")
            shutil.move(s, t)
            manifest.append({"from": s, "to": t})

def main():
    if not os.path.isdir(SRC):
        print("源目录不存在:", SRC)
        return
    manifest = []
    os.makedirs(DST, exist_ok=True)

    dirs = sorted(os.listdir(SRC))
    # 第一步：跨包收集（Mesh/Font/VideoClip/Shader 类目录）
    for d in dirs:
        src_dir = os.path.join(SRC, d)
        if not os.path.isdir(src_dir):
            continue
        for cls, cat in GATHER.items():
            cdir = os.path.join(src_dir, cls)
            if not os.path.isdir(cdir):
                continue
            target = os.path.join(DST, cat, short_of(d))
            move_merge(cdir, target, manifest, collision_prefix=short_of(d) + "_")
            # 清掉空的类目录
            if not os.listdir(cdir):
                os.rmdir(cdir)
        if not os.listdir(src_dir):
            os.rmdir(src_dir)

    # 第二步：整包移动
    for d in sorted(os.listdir(SRC)):
        src_dir = os.path.join(SRC, d)
        if not os.path.isdir(src_dir):
            continue
        target = os.path.join(DST, bundle_target(d))
        if os.path.isdir(target):
            move_merge(src_dir, target, manifest)
        else:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.move(src_dir, target)
            manifest.append({"from": src_dir, "to": target})

    with open(os.path.join(DST, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print(f"移动完成: {len(manifest)} 项")
    print("清单: 解包整理/manifest.json")

if __name__ == "__main__":
    main()
