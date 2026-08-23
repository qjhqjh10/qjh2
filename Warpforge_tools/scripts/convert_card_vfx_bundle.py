#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert_card_vfx_bundle.py — battleprefabs_vfxandmisc bundle 卡牌 VFX → particles3d JSON
任务⑩: card_anim_map GUID 反查 → 原版 3D 卡牌动画 VFX 预制体 → Godot 粒子数据
输入: 原始 bundle (StreamingAssets/aa/StandaloneWindows64/battleprefabs_vfxandmisc_assets_all.bundle)
      data/card_vfx_tree.json (dump_card_vfx_tree.py 生成: GUID→定义名/根 GO/粒子分布)
用法: python convert_card_vfx_bundle.py [--all | --names X,Y | --atk] [--2d]
      --2d = 输出 data/particles/ 2D 20字段单主粒子 (unity_particles.gd 消费; 子粒子丢弃;
             贴图写 assets/particles/ m_Name 命名), 需置于 --names/--all 之前 (2026-08-23)
      --all = 全部 400 预制体 (每预制体取主粒子系统)
      --atk = 攻击类全部 (01_卡牌/卡牌动画/MonoBehaviour 全部 Atk_* 定义 → GUID 去重 → 批量转换,
              命名用预制体根 GO 名; 输出 data/atk_vfx_map.json 定义名→预制体名映射)
输出: D:/warpforge/data/particles[3d]/<VFX名>.json (与 convert_unity_particles.py 同格式)
      D:/warpforge/assets/particles/[tex3d_card/]*.png (贴图)
"""
import json
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

BUNDLE = 'D:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/battleprefabs_vfxandmisc_assets_all.bundle'
TREE = 'D:/warpforge/data/card_vfx_tree.json'
OUT_JSON = 'D:/warpforge/data/particles3d/'
OUT_JSON2D = 'D:/warpforge/data/particles/'      # --2d 模式 (2026-08-23)
OUT_TEX = 'D:/warpforge/assets/particles/tex3d_card/'
OUT_TEX2D = 'D:/warpforge/assets/particles/'     # --2d 模式 (m_Name 命名, 与 2D 转换器一致)
ATK_ANIM_DIR = 'D:/2/解包整理/01_卡牌/卡牌动画/MonoBehaviour'
ATK_MAP = 'D:/warpforge/data/atk_vfx_map.json'

# VFX 名后缀变体 (基名还原)
_SUFFIX = ('_self', '_quick', '_ability', '_target_UI', '_warlord', '_reverse',
           '_ground', '_UI', '_self_quick', '_warlord_self', '_reverse_warlord',
           '_twinlink', '_enchantment', '_arc', '_big', '_intense_warlord',
           '_blast', '_quick_self', '_quick_target', '_dual', '_ability_quick',
           '_spider', '_spider_twinlink', '_twinlink_large', '_target')


def base_of(nm: str) -> str:
    for s in _SUFFIX:
        if nm.endswith(s):
            return nm[:-len(s)]
    return nm


def collect_atk_defs() -> dict:
    """收集全部 Atk_* 定义 → {GUID: [定义名...]}
    两个来源合并: ① 01_卡牌/卡牌动画/MonoBehaviour 共享去重目录 ② card_anim_map.json 阵营目录 Atk_*"""
    defs = {}
    for fn in os.listdir(ATK_ANIM_DIR):
        if not fn.endswith('.json'):
            continue
        base = fn[:-5]
        # 去掉 PathID 后缀 (如 Atk_StikkaThrow_-12345.json)
        if '_' in base and base.rsplit('_', 1)[1].lstrip('-').isdigit():
            base = base.rsplit('_', 1)[0]
        if not base.startswith('Atk_'):
            continue
        try:
            d = json.load(open(os.path.join(ATK_ANIM_DIR, fn), encoding='utf-8'))
            g = d.get('animInfo', {}).get('animAdressable', {}).get('m_AssetGUID', '')
        except Exception:
            continue
        if g:
            defs.setdefault(g, []).append(base)
    # ② 阵营目录定义 (map 已解析, 补共享目录没有的 GUID)
    if os.path.exists(TREE) and os.path.exists('D:/warpforge/data/card_anim_map.json'):
        cam = json.load(open('D:/warpforge/data/card_anim_map.json', encoding='utf-8'))
        for fac, cdefs in cam.items():
            if fac == '_guid_summary':
                continue
            for name, info in cdefs.items():
                if not name.startswith('Atk_'):
                    continue
                g = info.get('guid', '')
                if g and g not in defs:
                    defs[g] = ['%s:%s' % (fac, name)]
    return defs


def cv(v, default=None):
    """MinMaxCurve → 常数 (scalar / minScalar 优先)"""
    if isinstance(v, dict):
        st = v.get('minMaxState', 0)
        if st == 0:
            return v.get('scalar') if v.get('scalar') is not None else default
        return v.get('minScalar') if v.get('minScalar') is not None else default
    if v is None:
        return default
    return v


def cv2(v):
    """MinMaxCurve → (min, max) (2026-08-23: 取到 maxScalar/maxCurve 上界)"""
    if isinstance(v, dict):
        st = v.get('minMaxState', 0)
        if st == 0:
            s = v.get('scalar')
            return s, s
        lo = v.get('minScalar')
        hi = v.get('maxScalar')
        if hi is None:
            mc = v.get('maxCurve')
            if isinstance(mc, dict):
                if mc.get('scalar') is not None:
                    hi = mc['scalar']
                else:
                    pts = mc.get('m_Curve') or []
                    if pts:
                        hi = pts[0].get('value')
        return lo, hi
    return v, v


def main() -> int:
    import UnityPy
    env = UnityPy.load(BUNDLE)
    sf = env.file
    cont = sf.container
    by_pathid = {}
    for o in env.objects:
        by_pathid[o.path_id] = o
    # GO/Transform/PS 索引
    go_names = {}
    trans_children = defaultdict(list)
    trans_go = {}
    ps_by_go = defaultdict(list)
    renderer_by_go = {}
    for o in env.objects:
        t = o.type.name
        if t == 'GameObject':
            try:
                go_names[o.path_id] = str(o.read().m_Name)
            except Exception:
                pass
        elif t == 'Transform':
            try:
                r = o.read()
                trans_go[o.path_id] = r.m_GameObject.m_PathID
                for c in (r.m_Children or []):
                    trans_children[o.path_id].append(c.m_PathID)
            except Exception:
                pass
        elif t == 'ParticleSystem':
            try:
                ps_by_go[o.read().m_GameObject.m_PathID].append(o.path_id)
            except Exception:
                pass
        elif t == 'ParticleSystemRenderer':
            try:
                renderer_by_go[o.read().m_GameObject.m_PathID] = o.path_id
            except Exception:
                pass

    # GUID 索引
    tree = json.load(open(TREE, encoding='utf-8'))
    base_to_guid = {}
    for g, v in tree.items():
        for n in v['names']:
            fac, nm = n.split(':', 1)
            b = base_of(nm)
            if b not in base_to_guid:
                base_to_guid[b] = g

    # 目标清单
    args = sys.argv[1:]
    atk_mode = False
    as2d = False
    if args and args[0] == '--atk':
        atk_mode = True
    elif args and args[0] == '--2d':          # --2d 模式 (2026-08-23): 输出 data/particles/ 20 字段单主粒子
        as2d = True
        args = args[1:]
    out_json_dir = OUT_JSON2D if as2d else OUT_JSON
    out_tex_dir = OUT_TEX2D if as2d else OUT_TEX
    tex_prefix = '' if as2d else 'tex3d_card/'
    if not args or args == ['--all']:
        targets = sorted(base_to_guid.keys())
    elif args[0] == '--names':
        targets = [a.strip() for a in args[1].split(',')]
    else:
        targets = args

    def extract_texture(ps_go_pid):
        """GO → Renderer → Material → 贴图; 返回 (png路径, 贴图名, render_mode) (2026-08-23: 读 m_RenderMode)"""
        rid = renderer_by_go.get(ps_go_pid)
        if not rid:
            return None, None, 0
        try:
            r = by_pathid[rid].read_typetree()
        except Exception:
            return None, None, 0
        rm = r.get('m_RenderMode', 0)
        for m in r.get('m_Materials', []) or []:
            if not isinstance(m, dict):
                continue
            mid = m.get('m_PathID')
            mo = by_pathid.get(mid)
            if mo is None:
                continue
            try:
                mat = mo.read_typetree()
            except Exception:
                continue
            for pair in mat.get('m_SavedProperties', {}).get('m_TexEnvs', []) or []:
                # ⚠️ typetree 里 m_TexEnvs 是 tuple 对 ('_MainTex', {...}); JSON 导出才是 dict
                if isinstance(pair, tuple) and len(pair) == 2:
                    tev = pair[1]
                elif isinstance(pair, dict):
                    tev = pair.get('value') or pair.get('m_Value') or pair
                else:
                    continue
                tid = tev.get('m_Texture', {}).get('m_PathID') if isinstance(tev, dict) else None
                if not tid:
                    continue
                to = by_pathid.get(tid)
                if to is None or to.type.name != 'Texture2D':
                    continue
                try:
                    obj = to.read()
                    img = obj.image
                    if img is None:
                        continue
                    os.makedirs(out_tex_dir, exist_ok=True)
                    tname = str(obj.m_Name) or str(tid)
                    fp = os.path.join(out_tex_dir, tname + '.png')
                    if os.path.exists(fp) and not as2d:
                        return fp, tname, rm          # 3D: 幂等跳过
                    # 2026-08-23: 预乘 alpha 修复 (同 convert_unity_particles.py — bundle 提取
                    # 贴图 ~50-90% α 损坏: RGB 完整但 α≈0 → 内容透明化; 仅 --2d 强制重写修复)
                    from PIL import Image
                    rgba = img.convert('RGBA')
                    w0, h0 = rgba.size
                    px0 = rgba.load()
                    n0 = tr0 = rgb_sum = 0
                    for yy in range(0, h0, 2):
                        for xx in range(0, w0, 2):
                            n0 += 1
                            p = px0[xx, yy]
                            if p[3] < 10:
                                tr0 += 1
                            rgb_sum += (p[0] + p[1] + p[2]) / 3
                    if as2d and n0 > 0 and tr0 / n0 > 0.5 and rgb_sum / n0 > 100:
                        r, g, b, a = rgba.split()
                        rgba = Image.merge('RGBA', (r, g, b, a.point(lambda v: 255)))
                        print('  [alpha修复] %s (%d%% α=0)' % (tname, int(100 * tr0 / n0)))
                    rgba.save(fp)
                    return fp, tname, rm
                except Exception:
                    continue
        return None, None, rm

    def walk_tree(root_go):
        """BFS Transform 子树 → [GO path_id] (根在前)"""
        out = []
        seen = set()
        # 根 GO 的 Transform
        start_t = None
        for tid, gid in trans_go.items():
            if gid == root_go:
                start_t = tid
                break
        if start_t is None:
            return [root_go]
        q = [start_t]
        while q:
            tid = q.pop(0)
            if tid in seen:
                continue
            seen.add(tid)
            gid = trans_go.get(tid)
            if gid is not None and gid not in seen:
                seen.add(gid)
                out.append(gid)
            q.extend(trans_children.get(tid, []))
        return out

    def build_particle(ps_target, vfx_name, tex_suffix=''):
        """单个粒子系统 → 粒子 dict (particles3d 格式); 返回 dict"""
        ps_id = ps_by_go[ps_target][0]
        try:
            ps = by_pathid[ps_id].read_typetree()
        except Exception as e:
            print('  ✗ 读取失败:', vfx_name, e)
            return None
        im = ps.get('InitialModule', {})
        em = ps.get('EmissionModule', {})
        shp = ps.get('ShapeModule', {})
        tex_path, tex_name, rm = extract_texture(ps_target)
        # 爆发
        bursts = []
        blist = em.get('m_Bursts') or em.get('bursts') or []
        if isinstance(blist, list):
            for b in blist:
                if isinstance(b, dict):
                    t = b.get('time', 0)
                    cnt = cv(b.get('countCurve'))
                    bursts.append([t, cnt or 1])
        # Size/Color over lifetime
        size_curve = []
        sm = ps.get('SizeModule', {})
        if sm.get('enabled'):
            c = sm.get('curve', {}).get('maxCurve', {}).get('m_Curve', [])
            size_curve = [[k.get('time', 0), k.get('value', 1)] for k in c]
        color_curve = []
        cm = ps.get('ColorModule', {})
        if cm.get('enabled'):
            grad = cm.get('gradient', {}).get('maxGradient', {})
            keys = []
            for i in range(8):
                k = grad.get('key%d' % i)
                if k:
                    keys.append([i / 7.0, [k.get('r', 1), k.get('g', 1), k.get('b', 1), k.get('a', 1)]])
            color_curve = keys
        # 图集帧 (UVModule)
        tex_final = tex_path
        uv = ps.get('UVModule', {})
        frame_grid = None
        if uv.get('enabled') and (uv.get('tilesX') or 1) * (uv.get('tilesY') or 1) > 1:
            tx = int(uv.get('tilesX') or 1)
            ty = int(uv.get('tilesY') or 1)
            frame_grid = [tx, ty]
            total = tx * ty
            sf = uv.get('startFrame', {}).get('scalar', 0.0)
            start_frame = int(sf * total) % total if sf else 0
            if tex_path and os.path.exists(tex_path):
                from PIL import Image
                img_tex = Image.open(tex_path).convert('RGBA')
                w, h = img_tex.size
                fw, fh = w // frame_grid[0], h // frame_grid[1]
                row, col = divmod(start_frame, frame_grid[0])
                crop = img_tex.crop((col * fw, row * fh, (col + 1) * fw, (row + 1) * fh))
                crop = crop.resize((128, 128), Image.LANCZOS)
                tex_final = os.path.join(out_tex_dir, vfx_name + tex_suffix + '_frame.png')
                crop.save(tex_final)
        sc = im.get('startColor', {})
        life = cv(im.get('startLifetime')) or 1.0
        spd_lo, spd_hi = cv2(im.get('startSpeed'))
        sz = cv(im.get('startSize')) or 1.0
        # Transform 偏移/缩放 (预制体局部)
        offset = [0, 0, 0]
        escale = [1, 1, 1]
        for tid, gid in trans_go.items():
            if gid == ps_target:
                try:
                    tr = by_pathid[tid].read()
                    p = tr.m_LocalPosition
                    s = tr.m_LocalScale
                    offset = [p.x, p.y, p.z] if p else [0, 0, 0]
                    escale = [s.x, s.y, s.z] if s else [1, 1, 1]
                except Exception:
                    pass
                break
        common = {
            "system_lifetime": ps.get('lengthInSec', 1.0),
            "one_shot": not bool(ps.get('looping', False)),
            "play_on_awake": bool(ps.get('playOnAwake', True)),
            "amount": im.get('maxNumParticles', 100),
            "gravity": cv(im.get('gravityModifier')) or 0.0,
            "color_min": [sc.get('minColor', {}).get(k, 1.0) for k in 'rgba'] if sc.get('minColor') else [1, 1, 1, 1],
            "color_max": [sc.get('maxColor', {}).get(k, 1.0) for k in 'rgba'] if sc.get('maxColor') else [1, 1, 1, 1],
            "emission_rate": cv(em.get('rateOverTime')) or 0.0,
            "bursts": bursts,
            "size_over_lifetime": size_curve,
            "color_over_lifetime": color_curve,
            "render_mode": rm,
            "texture": ("res://assets/particles/" + tex_prefix + os.path.basename(tex_final)) if tex_final else "",
        }
        if as2d:
            return dict(common, **{
                "name": vfx_name,
                "lifetime": life,
                "speed_min": spd_lo or 0.0,
                "speed_max": (spd_hi if spd_hi is not None else spd_lo) or 0.0,
                "size_min": sz,
                "size_max": sz,
                "shape_type": shp.get('shapeType'),
            })
        return dict(common, **{
            "effect_offset": [round(v, 3) for v in offset],
            "effect_scale": [round(v, 3) for v in escale],
            "lifetime_min": life,
            "lifetime_max": life,
            "speed_min": spd_lo or 0.0,
            "speed_max": (spd_hi if spd_hi is not None else spd_lo) or 0.0,
            "size_min": sz,
            "size_max": sz,
            "shape": {
                'type': shp.get('shapeType', 0),
                'radius': cv(shp.get('radius'), 1),
                'radiusThickness': cv(shp.get('radiusThickness'), 1),
                'angle': cv(shp.get('angle'), 0),
                'scale': [cv(shp.get('scale', {}).get('x'), 1), cv(shp.get('scale', {}).get('y'), 1),
                          cv(shp.get('scale', {}).get('z'), 1)] if isinstance(shp.get('scale'), dict) else [1, 1, 1],
            },
            "velocity": {},
            "rot_z_speed": 0.0,
        })

    def convert_root(root_go, vfx_name):
        """根 GO path_id 直转 (通用事件 VFX 不在 card_vfx_tree 索引; 2026-08-23)"""
        gos = walk_tree(root_go)
        ps_gos = [g for g in gos if ps_by_go.get(g)]
        if not ps_gos:
            print('  ✗ 无 ParticleSystem:', vfx_name)
            return None, 0
        # 主粒子 = 有贴图的 GO 优先 (视觉主体), 否则 BFS 首个
        def go_has_tex(g):
            rid = renderer_by_go.get(g)
            if not rid:
                return False
            try:
                r = by_pathid[rid].read_typetree()
                for m in r.get('m_Materials', []) or []:
                    if not isinstance(m, dict):
                        continue
                    mo = by_pathid.get(m.get('m_PathID'))
                    if mo is None or mo.type.name != 'Material':
                        continue
                    try:
                        mt = mo.read_typetree()
                    except Exception:
                        continue
                    for pair in mt.get('m_SavedProperties', {}).get('m_TexEnvs', []) or []:
                        tev = pair[1] if isinstance(pair, tuple) and len(pair) == 2 else \
                              (pair.get('value') if isinstance(pair, dict) else None)
                        tid = tev.get('m_Texture', {}).get('m_PathID') if isinstance(tev, dict) else None
                        if tid:
                            # 2026-08-23: 必须验证纹理对象真实存在本 bundle (同名 pid 可能在
                            # battlesharedresources — has_tex 曾误判 Sparks → 主粒子选到无贴图者)
                            to = by_pathid.get(tid)
                            if to is not None and to.type.name == 'Texture2D':
                                return True
                return False
            except Exception:
                return False
        main_g = None
        for g in ps_gos:
            if go_has_tex(g):
                main_g = g
                break
        if main_g is None:
            main_g = ps_gos[0]
        main_d = build_particle(main_g, vfx_name)
        if main_d is None:
            return None, 0
        children = []
        if not as2d:
            for g in ps_gos:
                if g == main_g:
                    continue
                d = build_particle(g, vfx_name, '_c%d' % len(children))
                if d is not None:
                    d['go'] = go_names.get(g, '?')
                    children.append(d)
                if len(children) >= 12:
                    break   # 子粒子数量钳制 (运行时性能)
        elif len(ps_gos) > 1:
            print('  [2D] %s: 合并特效子粒子 %d 个丢弃 (unity_particles.gd 单粒子模式, 仅取主粒子)'
                  % (vfx_name, len(ps_gos) - 1))
        out = {"name": vfx_name}
        out.update(main_d)
        if children:
            out["children"] = children
        os.makedirs(out_json_dir, exist_ok=True)
        fp = os.path.join(out_json_dir, vfx_name + '.json')
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        n_ps = len(ps_gos)
        print('✓ %s: lifetime=%s size=%s bursts=%s tex=%s (GO %d/粒子 %d/子粒子 %d)' % (
            vfx_name, main_d['lifetime_min' if not as2d else 'lifetime'], main_d['size_min'], main_d['bursts'],
            os.path.basename(main_d['texture']) if main_d['texture'] else '无',
            len(gos), n_ps, len(children)))
        return fp, n_ps

    def convert_guid(guid, vfx_name):
        """预制体 → 主粒子 JSON + 子粒子; 返回 (文件名, 粒子数)"""
        pptr = cont.get(guid)
        if not pptr:
            print('  ✗ GUID 不在 bundle:', guid)
            return None, 0
        return convert_root(pptr.m_PathID, vfx_name)

    ok = 0
    done = set()
    if atk_mode:
        # 攻击类全部: 定义 → GUID 去重 → 按预制体根 GO 名转换
        defs = collect_atk_defs()
        guid_root = {}
        skipped = 0
        for g in sorted(defs):
            pptr = cont.get(g)
            if not pptr:
                print('✗ GUID 不在 bundle:', g)
                continue
            root_name = go_names.get(pptr.m_PathID)
            if not root_name:
                print('✗ 根 GO 名缺失:', g)
                continue
            guid_root[g] = root_name
            if os.path.exists(os.path.join(OUT_JSON, root_name + '.json')):
                skipped += 1
                continue
            if convert_guid(g, root_name):
                ok += 1
        # 映射表: 定义名 → 预制体名 (接线参考; 阵营目录独有定义去前缀还原原名)
        atk_map = {}
        for g, names in defs.items():
            for n in names:
                atk_map[n.removeprefix(n.split(':')[0] + ':') if ':' in n else n] = guid_root.get(g)
        with open(ATK_MAP, 'w', encoding='utf-8') as f:
            json.dump(atk_map, f, ensure_ascii=False, indent=1)
        print('--atk 完成: 转换 %d 个 (去重 %d 唯一 GUID / %d 唯一预制体, 跳过已有 %d); 映射表 %s' % (
            ok, len(defs), len(guid_root), skipped, ATK_MAP))
        return 0
    # 通用事件 VFX 根名直查索引 (不在 card_vfx_tree 的 bundle 根 GO;
    # 如 Healing_Projectile/StunEffect/Summon_Generic 等战斗事件类; 2026-08-23)
    go_by_name = {}
    for pid, nm in go_names.items():
        go_by_name.setdefault(nm, []).append(pid)
    for t in targets:
        if t in done:
            continue
        done.add(t)
        guid = base_to_guid.get(t)
        if guid:
            if convert_guid(guid, t):
                ok += 1
            continue
        # fallback: bundle 根 GO 名直查
        roots = go_by_name.get(t)
        if not roots:
            print('✗ 无 GUID/bundle 根名:', t)
            continue
        if len(roots) > 1:
            print('  ⚠ %s 在 bundle 有 %d 个同名 GO, 取第一个' % (t, len(roots)))
        if convert_root(roots[0], t):
            ok += 1
    print('完成 %d/%d' % (ok, len(targets)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
