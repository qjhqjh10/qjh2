#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_arena_props.py — 同步 11 阵营战场环境装饰到游戏项目
每阵营: 4 类标志模型 OBJ -> assets/models/<阵营>/ + 1 张阵营图集 -> assets/ui/battle/3d/<阵营>/
来源: d:/2/解包整理/06_模型/scenes_scenes_<arena>/ + d:/2/Warpforge_tools/data/ui_scene/scenes_scenes_<arena>/Texture2D/
"""
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

OBJ_SRC = 'd:/2/解包整理/06_模型/scenes_scenes_{arena}/'
TEX_SRC = 'd:/2/Warpforge_tools/data/ui_scene/scenes_scenes_{arena}/Texture2D/'
OBJ_DST = 'd:/warpforge/assets/models/{faction}/'
TEX_DST = 'd:/warpforge/assets/ui/battle/3d/{faction}/'

# arena -> (阵营目录, 模型清单, 图集)
PLAN = {
    'battlearena2': ('goff', [
        'Banner1.obj', 'Skull_Left1.obj', 'Skull_Right1.obj',
        'Tower_Silk_11.obj', 'Rubble1.obj',
    ], 'BattleArena2Atlas Baked.png'),
    'battlearena3': ('sautekh', [
        'Monolith Front Left1.obj', 'Monolith Front Right1.obj',
        'Broken Monolith 11.obj', 'Ground Lights1.obj', 'Props 1.0011.obj',
    ], 'BattleArena3Atlas-mat-_BaseMap-atlas-0.png'),
    'battlearenaaeldari': ('saimhann', [
        'Banner 11.obj', 'Banner 21.obj', 'Tower 11.obj',
        'Bridge 11.obj', 'Platform 11.obj',
    ], 'Battle Arena Aeldari Atlas-mat-_BaseMap-atlas-0.png'),
    'battlearenaastramilitarum': ('astramilitarum', [
        'Banner 11.obj', 'Banner 41.obj', 'Statue1.obj',
        'Barricade 11.obj', 'Bunker Antenna 11.obj',
    ], 'Battle Arena Astra Militarum Texture Bake result-mat-_BaseMap-atlas-0.png'),
    'battlearenadarkangels': ('darkangels', [
        'Turret 1 Banner1.obj', 'Skull vent 11.obj',
        'Generator1.obj', 'Container 11.obj',
    ], 'Battle Arena Dark Angels Texture Bake result-mat-_BaseMap-atlas-0.png'),
    'battlearenaemperorschildren': ('emperorschildren', [
        'Curtain 11.obj', 'Cauldron 11.obj', 'Cauldron 21.obj',
        'Glass Tube 11.obj', 'Spike 11.obj',
    ], "Battle Arean Emperor's Children Baked Mat-_BaseMap-atlas-0.png"),
    'battlearenagenestealers': ('genestealers', [
        'Banner 31.obj', 'Genestaler Fan.obj',
        'Machinery Center1.obj', 'Hanging Hook1.obj',
    ], 'Genestealers Atlas 1-_BaseMap-atlas-0.png'),
    'battlearenaleviathan': ('leviathan', [
        'Thorn_51.obj', 'Capillary_11.obj',
        'Prop_front_11.obj', 'Floor Tentacle1.obj',
    ], 'Data-mat-_MainTex-atlas-0.png'),
    'battlearenasororitas': ('sororitas', [
        'Banner 12.obj', 'Statue L2.obj', 'Statue R2.obj',
        'Cauldron L2.obj', 'Candle 202.obj',
    ], 'Sororitas Atlas 3-_BaseMap-atlas-0.png'),
    'battlearenaspacewolves': ('spacewolves', [
        'Banner 11.obj', 'Wolf Left1.obj', 'Wolf Right1.obj',
        'Cauldron 11.obj', 'Rock 11.obj',
    ], 'Space Wolves Battle Arena Baked Atlas-_BaseMap-atlas-0.png'),
    'battlearenatauviorla': ('tauviorla', [
        'Plasma Generator1.obj', 'Drone 11.obj',
        'Railgun Tower1.obj', 'Bunker console1.obj',
    ], 'Battle Arena Tau Viorla Combined Material-mat-_BaseMap-atlas-0.png'),
}


def main() -> int:
    ok = 0
    miss = []
    for arena, (faction, models, atlas) in PLAN.items():
        od = OBJ_DST.format(faction=faction)
        td = TEX_DST.format(faction=faction)
        os.makedirs(od, exist_ok=True)
        os.makedirs(td, exist_ok=True)
        for m in models:
            src = OBJ_SRC.format(arena=arena) + m
            if not os.path.exists(src):
                miss.append(src)
                continue
            shutil.copy2(src, os.path.join(od, m))
            ok += 1
        tsrc = TEX_SRC.format(arena=arena) + atlas
        if not os.path.exists(tsrc):
            miss.append(tsrc)
        else:
            shutil.copy2(tsrc, os.path.join(td, atlas))
            ok += 1
        print(f'✓ {faction}: {len(models)} OBJ + {atlas}')
    print(f'\n共同步 {ok} 个文件')
    if miss:
        print('缺失:')
        for m in miss:
            print(' ', m)
    return 0


if __name__ == '__main__':
    sys.exit(main())
