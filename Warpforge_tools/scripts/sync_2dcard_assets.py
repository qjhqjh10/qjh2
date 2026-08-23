#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_2dcard_assets.py — 2DCard 分层重建的资产同步（2026-08-21）
1) SDF 卡框(128x128 高亮/阴影源) → d:/warpforge/assets/cards/frames/<Faction>/<type>_sdf_tier<N>.png
   （全彩卡框 1024x1024 项目已有: <type>_tier<N>.png，SDF 是新补的高亮层素材）
2) 稀有度宝石衍生：只有 rare(绿) 原图，按稀有度色相衍生 common/epic/legendary/special
   （宝石为运行时 2DCard 叠加层，PnP 卡面不含宝石）
用法: py312 python.exe sync_2dcard_assets.py
"""
import os
import glob
import shutil
from PIL import Image, ImageEnhance

SRC = r"d:/2/解包整理/01_卡牌"
DST = r"d:/warpforge/assets/cards/frames"

# 解包阵营目录 -> 项目 frames 阵营名
FACTION_DIR = {
    "Aeldari_灵族": "SaimHann",
    "AstraMilitarum_星界军": "AstraMilitarum",
    "BlackLegion_黑色军团": "BlackLegion",
    "DarkAngels_暗黑天使": "DarkAngels",
    "EmperorsChildren_帝皇之子": "EmperorsChildren",
    "GenestealerCults_基因窃取者教派": "Genestealers",
    "Necrons_死灵族": "Sautekh",
    "Orks_兽人": "Goff",
    "Sororitas_战斗修女": "Sororitas",
    "SpaceWolves_太空野狼": "SpaceWolves",
    "Tau_钛帝国": "TauEmpire",
    "Tyranids_泰伦虫族": "Leviathan",
    "Ultramarines_极限战士": "Ultramarines",
}
# 阵营令牌 -> 项目阵营名 (文件名里 40k_Cardframe[s]_<TOKEN>_SDF_tierN)
TOKEN_MAP = {
    "SaimHann": "SaimHann", "Astra Militarum": "AstraMilitarum",
    "BlackLegion": "BlackLegion", "DarkAngels": "DarkAngels",
    "EmperorsChildren": "EmperorsChildren", "Genestealers": "Genestealers",
    "Sautekh": "Sautekh", "Orks": "Goff", "Sororitas": "Sororitas",
    "Space Wolves": "SpaceWolves", "SpaceWolves": "SpaceWolves",
    "Tau": "TauEmpire", "Leviathan": "Leviathan", "GSC": "Genestealers",
    "Emperor Children": "EmperorsChildren", "Ultramarines": "Ultramarines",
}

GEM_SRC = r"d:/2/解包整理/11_着色器/配套材质/Texture2D/2_40k_cardframe_rarity_rare.png"
GEM_DST = r"d:/warpforge/assets/cards/gems"


def copy_sdf_frames():
    """SDF 帧复制 + 转 alpha 贴图: 原图是不透明灰度 (白=卡体, 黑=外围),
    转成 alpha=亮度、RGB=白 —— Godot 标准材质按 alpha 渲染 → 白体不透明(被卡盖住),
    外围渐变压成软阴影/光晕环。"""
    n = 0
    for src_dir, dst_fac in FACTION_DIR.items():
        td = os.path.join(SRC, src_dir, "Texture2D")
        if not os.path.isdir(td):
            print("MISS dir", td)
            continue
        for f in os.listdir(td):
            if not (f.endswith(".png") and "_SDF_tier" in f):
                continue
            # 40k_Cardframe[s]_<TOKEN>_SDF_tier<N>.png → troop/stratagem
            name = f[:-4]
            for pre in ("40k_Cardframes_", "40k_Cardframe_"):
                if name.startswith(pre):
                    name = name[len(pre):]
                    break
            parts = name.split("_SDF_tier")
            if len(parts) != 2:
                continue
            token, tier = parts[0], parts[1]
            low = token.lower()
            ctype = "troop" if low.startswith("troop") else "stratagem"
            token = token[6:] if low.startswith("troop_") else (token[10:] if low.startswith("stratagem_") else token)
            fac = TOKEN_MAP.get(token)
            if fac is None:
                print("SKIP token:", token, f)
                continue
            dst_dir = os.path.join(DST, fac)
            os.makedirs(dst_dir, exist_ok=True)
            dst = os.path.join(dst_dir, "%s_sdf_tier%s.png" % (ctype, tier))
            im = Image.open(os.path.join(td, f)).convert("L")
            alpha = im.point(lambda p: p)  # 亮度 → alpha
            out = Image.merge("RGBA", (Image.new("L", im.size, 255),) * 3 + (alpha,))
            out.save(dst)
            n += 1
    print("SDF frames copied:", n)


def _hue_shift(img, target_hue):
    """色相移到 target_hue (度), 保留 S/V; 全灰像素不动。"""
    hsv = img.convert("HSV")
    h, s, v = hsv.split()
    h = h.point(lambda p: int(target_hue / 360.0 * 255))
    return Image.merge("HSV", (h, s, v)).convert("RGBA")


def make_gems():
    """rare 原图(绿) → common(灰)/epic(紫)/legendary(金)/special(红) 衍生。"""
    if not os.path.isfile(GEM_SRC):
        print("MISS rare gem:", GEM_SRC)
        return
    gem = Image.open(GEM_SRC).convert("RGBA")
    os.makedirs(GEM_DST, exist_ok=True)
    # 目标色相: common 灰(S=0), rare 绿 120°(原图), epic 紫 275°, legendary 金 42°, special 红 5°
    variants = {
        "common": "gray", "epic": 275, "legendary": 42, "special": 5,
    }
    gem.save(os.path.join(GEM_DST, "rare.png"))
    for name, spec in variants.items():
        if spec == "gray":
            out = ImageEnhance.Color(gem).enhance(0.0)
        else:
            out = _hue_shift(gem, spec)
        out.save(os.path.join(GEM_DST, name + ".png"))
        print("gem:", name, "ok")
    print("gems total:", len(variants) + 1)


if __name__ == "__main__":
    copy_sdf_frames()
    make_gems()
    print("done")
