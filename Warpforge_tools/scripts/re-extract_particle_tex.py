# -*- coding: utf-8 -*-
"""
re-extract_particle_tex.py — 从原始 bundle 重新提取战斗特效贴图
背景: 解包目录导出的粒子贴图 alpha 通道损坏 (预乘错误: 全 255 / 透明区 RGB 黑),
      2D 粒子时代尺寸小不明显, 3D 化后暴露为硬边方块。
修复: 按特效 Material m_TexEnvs → tex_pid → UnityPy 从 bundle 提取原始 Texture2D → 覆盖 assets/particles/
用法: py312/python.exe scripts/re-extract_particle_tex.py
"""
import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PREFAB = r'D:\2\解包整理\08_预制体特效\战斗预制体'
OUT_TEX = r'D:\warpforge\assets\particles'
BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
BUNDLES = ['battleprefabs_vfxandmisc_assets_all', 'battlesharedresources_assets_all']

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import UnityPy

env = UnityPy.Environment()
for b in BUNDLES:
    p = os.path.join(BUNDLE_DIR, b + '.bundle')
    if os.path.exists(p):
        try:
            env.load_file(p)
            print(f'加载 {b}')
        except Exception as e:
            print(f'加载失败 {b}: {e}')

tex_by_pid = {}
for o in env.objects:
    if o.type.name == 'Texture2D':
        try:
            tex_by_pid[o.path_id] = o
        except Exception:
            pass
print(f'bundle Texture2D 总数: {len(tex_by_pid)}')


def pid_of(fn):
    stem = fn[:-5]
    try:
        return int(stem.rsplit('_', 1)[1])
    except Exception:
        return None


def extract(tex_pid, out_name):
    """按 pid 从 bundle 提取纹理 → png"""
    o = tex_by_pid.get(tex_pid)
    if o is None:
        return None
    try:
        img = o.read().image
        if img is None:
            return None
        fp = os.path.join(OUT_TEX, out_name + '.png')
        img.save(fp)
        return fp
    except Exception:
        return None


# 扫描所有特效 Material → tex_pid → 提取 (覆盖已有, 但跳过生成物 soft_dot)
done = {}
for mf in glob.glob(os.path.join(PREFAB, 'Material', '*.json')):
    try:
        mat = json.load(open(mf, encoding='utf-8'))
    except Exception:
        continue
    for te in mat.get('m_SavedProperties', {}).get('m_TexEnvs', []):
        slot = te[0] if isinstance(te, (list, tuple)) and te else None
        if slot not in ('_BaseMap', '_MainTex'):
            continue
        tref = te[1].get('m_Texture', {})
        tpid = tref.get('m_PathID')
        if tpid is None or tpid in done:
            continue
        done[tpid] = True
        fp = extract(tpid, str(mat.get('m_Name', tpid)))
        if fp:
            print(f'✓ {mat.get("m_Name", tpid)} <- pid {tpid}')
print(f'提取 {len(done)} 个纹理')
