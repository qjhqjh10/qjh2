#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert_arena_particles.py — 阵营战场场景粒子 (ParticleSystem) → Godot GPUParticles3D 中间格式
输入: <arena> <粒子GO名> [更多名...]  (arena 如 battlearena3)
输出: D:/warpforge/data/arena_particles/<arena>/<名>.json
      + 粒子纹理 -> assets/particles3d/  + Mesh 粒子 OBJ -> assets/models/particles/<arena>/
用法: py312/python.exe convert_arena_particles.py battlearena3 Lightning Scarab\ Swarm\ 1
"""
import json
import math
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SCENE_ROOT = 'd:/2/解包整理/07_场景/'
BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
OUT_JSON = 'd:/warpforge/data/arena_particles'
OUT_TEX = 'd:/warpforge/assets/particles3d'
OUT_MESH = 'd:/warpforge/assets/models/particles'
SHARED = BUNDLE_DIR + 'battlesharedresources_assets_all.bundle'


def pid_of(fn):
    stem = fn[:-5]
    try:
        return int(stem.rsplit('_', 1)[1])
    except Exception:
        return None


def load_dir(d):
    out = {}
    if not os.path.isdir(d):
        return out
    for fn in os.listdir(d):
        if not fn.endswith('.json'):
            continue
        p = pid_of(fn)
        if p is None:
            continue
        try:
            with open(os.path.join(d, fn), encoding='utf-8') as f:
                out[p] = json.load(f)
        except Exception:
            continue
    return out


def cv(v, default=0.0):
    """MinMaxCurve → 常数 (scalar 优先, 随机取 min)"""
    if isinstance(v, dict):
        st = v.get('minMaxState', 0)
        if st == 0:
            return v.get('scalar', default)
        return v.get('minScalar', v.get('scalar', default))
    return v if isinstance(v, (int, float)) else default


def cv_pair(v, default=1.0):
    """MinMaxCurve → (min, max)"""
    if isinstance(v, dict):
        st = v.get('minMaxState', 0)
        if st == 0:
            return v.get('scalar', default), v.get('scalar', default)
        return v.get('minScalar', default), v.get('maxScalar', v.get('scalar', default))
    return v, v


def color_val(c, key, default=1.0):
    if not c:
        return default
    return c.get(key, default)


def main() -> int:
    if len(sys.argv) < 3:
        print('用法: convert_arena_particles.py <arena> <粒子GO名> [更多名...]')
        return 1
    arena = sys.argv[1]
    want = sys.argv[2:]
    root = os.path.join(SCENE_ROOT, arena)
    ps_all = load_dir(os.path.join(root, 'ParticleSystem'))
    pr_all = load_dir(os.path.join(root, 'ParticleSystemRenderer'))
    go_all = load_dir(os.path.join(root, 'GameObject'))
    tr_all = load_dir(os.path.join(root, 'Transform'))
    mat_all = load_dir(os.path.join(root, 'Material'))
    tex_all = load_dir(os.path.join(root, 'Texture2D'))
    mf_all = load_dir(os.path.join(root, 'MeshFilter'))

    # 共享 bundle: mesh/材质/纹理
    import UnityPy
    env = UnityPy.load(SHARED)
    shared_mesh = {}
    shared_tex = {}
    shared_mat = {}
    shared_ps = {}
    shared_pr = {}
    for o in env.objects:
        t = o.type.name
        if t == 'Mesh':
            try:
                shared_mesh[o.path_id] = o.read()
            except Exception:
                pass
        elif t == 'Texture2D':
            try:
                shared_tex[o.path_id] = o.read()
            except Exception:
                pass
        elif t == 'Material':
            try:
                shared_mat[o.path_id] = o.read_typetree()
            except Exception:
                pass
        elif t == 'ParticleSystem':
            try:
                shared_ps[o.path_id] = o.read_typetree()
            except Exception:
                pass
        elif t == 'ParticleSystemRenderer':
            try:
                shared_pr[o.path_id] = o.read_typetree()
            except Exception:
                pass

    go_transform = {}
    for tpid, td in tr_all.items():
        g = td.get('m_GameObject', {}).get('m_PathID')
        if g is not None:
            go_transform[g] = tpid

    def world_pos(gopid):
        """GO 世界位置 (Transform 链累积)"""
        cur = go_transform.get(gopid)
        pos = [0.0, 0.0, 0.0]
        scale = [1.0, 1.0, 1.0]
        chain = 0
        while cur is not None and chain < 64:
            td = tr_all.get(cur)
            if td is None:
                break
            lp = td.get('m_LocalPosition', {})
            ls = td.get('m_LocalScale', {})
            pos[0] += lp.get('x', 0) * scale[0]
            pos[1] += lp.get('y', 0) * scale[1]
            pos[2] += lp.get('z', 0) * scale[2]
            scale[0] *= ls.get('x', 1)
            scale[1] *= ls.get('y', 1)
            scale[2] *= ls.get('z', 1)
            cur = td.get('m_Father', {}).get('m_PathID')
            chain += 1
        return pos, scale, chain

    def _find_camera(root_dir, tr_d, go_d):
        """场景战斗相机世界位置 (BoardCamera; 无则 None)"""
        cam_all = load_dir(os.path.join(root_dir, 'Camera'))
        for cpid, cd in cam_all.items():
            gopid = cd.get('m_GameObject', {}).get('m_PathID')
            g = go_d.get(gopid)
            if not g:
                continue
            if 'oard' in g.get('m_Name', ''):
                pos, _, _ = world_pos(gopid)
                return pos
        return None

    def _find_floor(root_dir, tr_d, go_d):
        """地板中心世界位置 (第一块 Floor/Floor plane/Ground)"""
        for gopid, gd in go_d.items():
            nm = gd.get('m_Name', '')
            if nm in ('Floor', 'Floor plane', 'Ground') and 'Fence' not in nm:
                pos, _, _ = world_pos(gopid)
                return pos
        return None

    def resolve_tex(tpid, mfid, out_name):
        """纹理: 本地 JSON 名 → PNG; 外部 → shared bundle 提取"""
        if mfid == 0:
            td = tex_all.get(tpid)
            if td:
                nm = td.get('m_Name', '')
                png = os.path.join(root, 'Texture2D', nm + '.png')
                if os.path.exists(png):
                    return png
        t = shared_tex.get(tpid)
        if t is not None:
            os.makedirs(OUT_TEX, exist_ok=True)
            fp = os.path.join(OUT_TEX, out_name + '.png')
            if not os.path.exists(fp):
                img = t.image
                if img is None:
                    return None
                img.save(fp)
            return fp
        return None

    def resolve_mesh(mpid, mfid, out_name):
        """Mesh 粒子: shared bundle 导出 OBJ"""
        if mpid is None:
            return None, None
        m = shared_mesh.get(mpid)
        if m is None:
            return None, None
        nm = str(m.m_Name)
        os.makedirs(OUT_MESH, exist_ok=True)
        fp = os.path.join(OUT_MESH, arena + '_' + out_name + '.obj')
        if not os.path.exists(fp):
            raw = m.export()
            if not raw:
                return None, None
            with open(fp, 'w', encoding='utf-8', errors='replace') as f:
                f.write(raw)
        return fp, nm

    ok = 0
    for wn in want:
        # 找 GO (精确名优先, 再 startswith/包含)
        gopid = None
        gname = None
        for pid, gd in go_all.items():
            if gd.get('m_Name', '') == wn:
                gopid = pid
                gname = wn
                break
        if gopid is None:
            for pid, gd in go_all.items():
                nm = gd.get('m_Name', '')
                if nm.startswith(wn) or wn in nm:
                    gopid = pid
                    gname = nm
                    break
        if gopid is None:
            print(f'✗ {wn}: GO 未找到')
            continue
        gd = go_all[gopid]
        comps = [c['component']['m_PathID'] for c in gd.get('m_Component', [])]
        # ParticleSystem 组件
        ps = None
        for c in comps:
            if c in ps_all:
                ps = ps_all[c]
                break
        if ps is None:
            print(f'✗ {wn}: 无 ParticleSystem 组件')
            continue
        # Renderer
        pr = None
        for c in comps:
            if c in pr_all:
                pr = pr_all[c]
                break
        render_mode = pr.get('m_RenderMode', 0) if pr else 0
        mesh_pid = None
        mesh_fid = 0
        if pr:
            m = pr.get('m_Mesh', {})
            mesh_pid = m.get('m_PathID')
            mesh_fid = m.get('m_FileID', 0)
        # 材质 → 纹理
        tex_path = None
        if pr:
            for ref in pr.get('m_Materials', []):
                mpid2 = ref.get('m_PathID')
                mfid2 = ref.get('m_FileID', 0)
                mat = mat_all.get(mpid2) or shared_mat.get(mpid2)
                if not mat:
                    continue
                for te in mat.get('m_SavedProperties', {}).get('m_TexEnvs', []):
                    slot = te[0] if isinstance(te, (list, tuple)) and te else None
                    if slot not in ('_BaseMap', '_MainTex'):
                        continue
                    tref = te[1].get('m_Texture', {})
                    tpid = tref.get('m_PathID')
                    if tpid is None:
                        continue
                    tex_path = resolve_tex(tpid, tref.get('m_FileID', 0), wn.replace(' ', '_'))
                    if tex_path:
                        break
                if tex_path:
                    break
        # 网格粒子
        mesh_path = None
        mesh_name = None
        if render_mode == 4 and mesh_pid:
            mesh_path, mesh_name = resolve_mesh(mesh_pid, mesh_fid, wn.replace(' ', '_'))
        # 世界位置
        pos, scale, chain = world_pos(gopid)
        # 相机基准: BoardCamera (若有, 各阵营统一 (100,2.22,-13.57)) → 偏移 (100,0,0)
        # 无 BoardCamera 场景: 地板中心 (fx, fz), 假设相机 (fx, 2.22, fz-13.57)
        cam = _find_camera(root, tr_all, go_all)
        if cam is not None:
            off = [cam[0] - 0.0, cam[1] - 2.2, cam[2] + 13.57]
        else:
            floor = _find_floor(root, tr_all, go_all)
            if floor is not None:
                off = [floor[0], 0.0, floor[2] + 13.57]
            else:
                off = [100.0, 0.0, 0.0]
        godot_pos = [pos[0] - off[0], pos[1] - off[1], pos[2] - off[2]]
        im = ps.get('InitialModule', {})
        em = ps.get('EmissionModule', {})
        shp = ps.get('ShapeModule', {})
        sm = ps.get('SizeModule', {})
        cm = ps.get('ColorModule', {})
        vm = ps.get('VelocityModule', {})
        rm = ps.get('RotationModule', {})
        # 爆发
        bursts = []
        blist = em.get('m_Bursts') or em.get('bursts') or []
        if isinstance(blist, list):
            for b in blist:
                if isinstance(b, dict):
                    t = b.get('time', 0)
                    cnt = cv(b.get('countCurve'), 1)
                    bursts.append([t, cnt or 1])
        # Size/Color 随生命 (首尾关键帧)
        size_curve = []
        if sm.get('enabled'):
            c = sm.get('curve', {}).get('maxCurve', {}).get('m_Curve', [])
            size_curve = [[k.get('time', 0), k.get('value', 1)] for k in c]
        color_curve = []
        if cm.get('enabled'):
            grad = cm.get('gradient', {}).get('maxGradient', {})
            keys = []
            for i in range(8):
                k = grad.get(f'key{i}')
                if k:
                    keys.append([i / 7.0,
                                 [color_val(k, 'r', 1), color_val(k, 'g', 1),
                                  color_val(k, 'b', 1), color_val(k, 'a', 1)]])
            color_curve = keys
        sc = im.get('startColor', {})
        sc_min = sc.get('minColor') or {}
        sc_max = sc.get('maxColor') or {}
        speed_min, speed_max = cv_pair(im.get('startSpeed'), 0)
        size_min, size_max = cv_pair(im.get('startSize'), 1)
        life_min, life_max = cv_pair(im.get('startLifetime'), 1)
        shape = {
            'type': shp.get('type', shp.get('shapeType', 0)),
            'radius': cv(shp.get('radius'), 1),
            'radiusThickness': cv(shp.get('radiusThickness'), 1),
            'angle': cv(shp.get('angle'), 0),
            'scale': [cv(shp.get('m_Scale', shp.get('scale', {})).get('x')), cv(shp.get('m_Scale', shp.get('scale', {})).get('y')),
                      cv(shp.get('m_Scale', shp.get('scale', {})).get('z'))] if isinstance(shp.get('m_Scale', shp.get('scale')), dict) else [1, 1, 1],
        }
        vel = {}
        if vm.get('enabled'):
            vel = {
                'x': cv(vm.get('x', {}).get('minMaxCurve') if isinstance(vm.get('x'), dict) else vm.get('x')),
                'y': cv(vm.get('y', {}).get('minMaxCurve') if isinstance(vm.get('y'), dict) else vm.get('y')),
                'z': cv(vm.get('z', {}).get('minMaxCurve') if isinstance(vm.get('z'), dict) else vm.get('z')),
            }
        rot_z = 0.0
        if rm.get('enabled'):
            rz = rm.get('z', {})
            if isinstance(rz, dict):
                rot_z = cv(rz.get('minMaxCurve')) if isinstance(rz.get('minMaxCurve'), dict) else rz.get('scalar', 0)
        out = {
            'name': wn,
            'go': gname,
            'world_pos': [round(pos[0], 2), round(pos[1], 2), round(pos[2], 2)],
            'world_scale': [round(scale[0], 2), round(scale[1], 2), round(scale[2], 2)],
            'chain': chain,
            'godot_pos': [round(godot_pos[0], 2), round(godot_pos[1], 2), round(godot_pos[2], 2)],
            'system_lifetime': ps.get('lengthInSec', 1.0),
            'looping': bool(ps.get('looping', False)),
            'play_on_awake': bool(ps.get('playOnAwake', True)),
            'amount': im.get('maxNumParticles', 100),
            'lifetime_min': round(life_min, 3),
            'lifetime_max': round(life_max, 3),
            'speed_min': round(speed_min, 3),
            'speed_max': round(speed_max, 3),
            'size_min': round(size_min, 4),
            'size_max': round(size_max, 4),
            'gravity': cv(im.get('gravityModifier'), 0),
            'color_min': [color_val(sc_min, k, 1.0) for k in 'rgba'],
            'color_max': [color_val(sc_max, k, 1.0) for k in 'rgba'],
            'emission_rate': cv(em.get('rateOverTime'), 0),
            'bursts': bursts,
            'shape': shape,
            'velocity': vel,
            'rot_z_speed': round(rot_z, 3),
            'size_over_lifetime': size_curve,
            'color_over_lifetime': color_curve,
            'render_mode': render_mode,
            'mesh': ('res://assets/models/particles/' + os.path.basename(mesh_path)) if mesh_path else '',
            'mesh_name': mesh_name or '',
            'texture': ('res://assets/particles3d/' + os.path.basename(tex_path)) if tex_path else '',
        }
        out_dir = os.path.join(OUT_JSON, arena)
        os.makedirs(out_dir, exist_ok=True)
        fp = os.path.join(out_dir, wn.replace(' ', '_') + '.json')
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        print(f'✓ {arena}/{wn}: pos=({pos[0]:.1f},{pos[1]:.1f},{pos[2]:.1f}) '
              f'life={out["lifetime_min"]}-{out["lifetime_max"]} rate={out["emission_rate"]} '
              f'shape={shape["type"]} render={render_mode} tex={"有" if tex_path else "无"} mesh={mesh_name or "无"}')
        ok += 1
    print(f'完成 {ok}/{len(want)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
