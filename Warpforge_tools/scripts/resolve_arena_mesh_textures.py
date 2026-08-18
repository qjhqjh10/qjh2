#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resolve_arena_mesh_textures.py — 解析阵营战场每个 Mesh 的贴图（说明书链路）
MeshFilter.m_Mesh -> m_GameObject -> GameObject.m_Component -> MeshRenderer.m_Materials -> Material._BaseMap -> Texture2D.m_Name
输出: 每阵营 mesh名 -> (贴图名, 外部文件与否)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import UnityPy

ARENAS = ['battlearena2', 'battlearena3', 'battlearenaaeldari', 'battlearenaastramilitarum',
          'battlearenablacklegion', 'battlearenadarkangels', 'battlearenaemperorschildren',
          'battlearenagenestealers', 'battlearenaleviathan', 'battlearenasororitas',
          'battlearenaspacewolves', 'battlearenatauviorla']
SCENE_ROOT = 'd:/2/解包整理/07_场景/'
BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
SHARED = BUNDLE_DIR + 'battlesharedresources_assets_all.bundle'


def pid_of(fn: str) -> int:
    """文件名尾部的 pid: MeshFilter_1602.json -> 1602; MeshFilter_1602_1602.json -> 1602"""
    stem = fn[:-5]
    try:
        return int(stem.rsplit('_', 1)[1])
    except Exception:
        return None


def load_json_dir(d):
    out = {}
    if not os.path.isdir(d):
        return out
    for fn in os.listdir(d):
        if not fn.endswith('.json'):
            continue
        pid = pid_of(fn)
        if pid is None:
            continue
        try:
            with open(os.path.join(d, fn), encoding='utf-8') as f:
                out[pid] = json.load(f)
        except Exception:
            continue
    return out


def main() -> int:
    # 共享 bundle: mesh/材质/纹理 pid->name
    shared_mesh = {}
    shared_tex = {}
    shared_mat = {}
    env = UnityPy.load(SHARED)
    for o in env.objects:
        if o.type.name == 'Mesh':
            try:
                shared_mesh[o.path_id] = str(o.read().m_Name)
            except Exception:
                pass
        elif o.type.name == 'Texture2D':
            try:
                shared_tex[o.path_id] = str(o.read().m_Name)
            except Exception:
                pass
        elif o.type.name == 'Material':
            try:
                shared_mat[o.path_id] = o.read_typetree()
            except Exception:
                pass

    for arena in ARENAS:
        root = os.path.join(SCENE_ROOT, arena)
        meshfilters = load_json_dir(os.path.join(root, 'MeshFilter'))
        gameobjects = load_json_dir(os.path.join(root, 'GameObject'))
        meshref = load_json_dir(os.path.join(root, 'MeshRenderer'))
        materials = load_json_dir(os.path.join(root, 'Material'))
        textures = load_json_dir(os.path.join(root, 'Texture2D'))

        # 本地 bundle 的 mesh pid->name + texture pid->name
        local_mesh = {}
        local_tex = {}
        try:
            env2 = UnityPy.load(os.path.join(BUNDLE_DIR, f'scenes_scenes_{arena}.bundle'))
            for o in env2.objects:
                if o.type.name == 'Mesh':
                    try:
                        local_mesh[o.path_id] = str(o.read().m_Name)
                    except Exception:
                        pass
                elif o.type.name == 'Texture2D':
                    try:
                        local_tex[o.path_id] = str(o.read().m_Name)
                    except Exception:
                        pass
        except Exception:
            pass
        mesh_name = {**shared_mesh, **local_mesh}
        tex_name_of = {**shared_tex, **local_tex}

        # mesh名 -> 贴图
        res = {}
        for pid, mf in meshfilters.items():
            m = mf.get('m_Mesh')
            if not m:
                continue
            mpid = m.get('m_PathID')
            if mpid is None:
                continue
            name = mesh_name.get(mpid)
            if name is None or name in res:
                continue
            go = gameobjects.get(mf.get('m_GameObject', {}).get('m_PathID'))
            if not go:
                continue
            tex_name = None
            tex_ext = 0
            for comp in go.get('m_Component', []):
                cpid = comp.get('component', {}).get('m_PathID')
                if cpid is None:
                    continue
                mr = meshref.get(cpid)
                if not mr:
                    continue
                for ref in mr.get('m_Materials', []):
                    mpid2 = ref.get('m_PathID')
                    if mpid2 is None:
                        continue
                    # 本地 Material JSON 优先（解包已重映射部分外部引用），miss 再查共享 bundle
                    mat = materials.get(mpid2) or shared_mat.get(mpid2)
                    if not mat:
                        continue
                    for te in mat.get('m_SavedProperties', {}).get('m_TexEnvs', []):
                        # 本地 JSON 是 list 对, UnityPy typetree 是 tuple 对
                        slot = te[0] if isinstance(te, (list, tuple)) and te else None
                        if slot not in ('_BaseMap', '_MainTex'):
                            continue
                        tref = te[1].get('m_Texture', {})
                        tpid = tref.get('m_PathID')
                        tex_ext = tref.get('m_FileID', 0)
                        if tpid is None:
                            continue
                        if tex_ext != 0:
                            tex_name = tex_name_of.get(tpid) or f'ext_pid{tpid}'
                        else:
                            td = textures.get(tpid)
                            tex_name = td.get('m_Name', f'pid{tpid}') if td else (tex_name_of.get(tpid) or f'pid{tpid}')
                        break
                    if tex_name is not None:
                        break
                if tex_name is not None:
                    break
            res[name] = (tex_name, tex_ext)
        print(f'=== {arena}')
        for k, v in sorted(res.items()):
            ext = '[EXT]' if v[1] != 0 else ''
            print(f'  {k} -> {v[0]} {ext}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
