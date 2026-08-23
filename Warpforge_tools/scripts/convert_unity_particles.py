# -*- coding: utf-8 -*-
"""
convert_unity_particles.py — Unity ParticleSystem JSON → Godot 粒子中间格式
输入: 特效名 (GO 名, 如 AttackHitSmall) 或 ParticleSystem JSON 路径 (可多个)
输出: D:/warpforge/data/particles/<名>.json (2D 简化参数, 拍平由 unity_particles.gd 做)
      --3d 模式: D:/warpforge/data/particles3d/<名>.json (3D 世界空间, 保留形状/速度/挂点偏移, unity_particles3d.gd 读取)
      + 纹理 (从 bundle 或解包目录)
用法: py312/python.exe scripts/convert_unity_particles.py AttackHitSmall Actual_Explosion ...
      py312/python.exe scripts/convert_unity_particles.py --3d AttackHitSmall ...
"""
import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PREFAB = r'D:\2\解包整理\08_预制体特效\战斗预制体'
SHARED = r'D:\2\解包整理\08_预制体特效\共享资源'
OUT_JSON = r'D:\warpforge\data\particles'
OUT_JSON3D = r'D:\warpforge\data\particles3d'
OUT_TEX = r'D:\warpforge\assets\particles'
BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'


def find_files(d, fname, pid):
    """按文件名或 PathID 后缀找文件"""
    out = glob.glob(os.path.join(d, fname, f'*_{pid}.json')) + \
          glob.glob(os.path.join(d, fname, f'{pid}.json'))
    return out


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
    """MinMaxCurve → (min, max)"""
    if isinstance(v, dict):
        st = v.get('minMaxState', 0)
        if st == 0:
            return v.get('scalar'), v.get('scalar')
        return v.get('minScalar'), v.get('maxCurve', {}).get('m_Curve') and None or None
    return v, v


def load_tex_png(tex_pid, name):
    """纹理: 先解包目录 (战斗预制体/共享资源 Texture2D), 再 bundle 提取"""
    for d in (PREFAB, SHARED):
        for f in glob.glob(os.path.join(d, 'Texture2D', f'*_{tex_pid}.json')):
            try:
                j = json.load(open(f, encoding='utf-8'))
                png = os.path.join(os.path.dirname(f), j.get('m_Name', '') + '.png')
                if os.path.exists(png):
                    return png
            except Exception:
                pass
    # bundle 提取
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import UnityPy
        env = UnityPy.Environment()
        for b in ['battleprefabs_vfxandmisc_assets_all', 'battlesharedresources_assets_all']:
            p = os.path.join(BUNDLE_DIR, b + '.bundle')
            if os.path.exists(p):
                try:
                    env.load_file(p)
                except Exception:
                    pass
        for obj in env.objects:
            if obj.type.name == 'Texture2D' and str(obj.path_id) == str(tex_pid):
                try:
                    img = obj.read().image
                    if img is None:
                        return None
                    os.makedirs(OUT_TEX, exist_ok=True)
                    fp = os.path.join(OUT_TEX, (name or str(tex_pid)) + '.png')
                    img.save(fp)
                    return fp
                except Exception:
                    return None
    except Exception as e:
        print(f'  [bundle失败] {e}')
    return None


def find_ps_recursive(go_name, depth=0):
    """沿子 GO 递归找含 ParticleSystem 的 GO (组合特效: 根 GO 只是空容器)"""
    if depth > 6:
        return None
    go_files = glob.glob(os.path.join(PREFAB, 'GameObject', go_name + '*.json'))
    if not go_files:
        return None
    g = json.load(open(go_files[0], encoding='utf-8'))
    comps = [c['component']['m_PathID'] for c in g.get('m_Component', [])]
    for c in comps:
        for f in glob.glob(os.path.join(PREFAB, 'ParticleSystem', f'*_{c}.json')):
            if f.endswith(f'_{c}.json') and not f.endswith(f'_{c}_{c}.json'):
                return (go_name, f, c, comps)
    tr = None
    for c in comps:
        for f in glob.glob(os.path.join(PREFAB, 'Transform', f'*_{c}.json')):
            if f.endswith(f'_{c}.json') and not f.endswith(f'_{c}_{c}.json'):
                tr = json.load(open(f, encoding='utf-8'))
                break
        if tr:
            break
    if not tr:
        return None
    for ch in tr.get('m_Children', []):
        cpid = ch.get('m_PathID') if isinstance(ch, dict) else ch
        for gf in os.listdir(os.path.join(PREFAB, 'GameObject')):
            if not gf.endswith('.json'):
                continue
            try:
                gg = json.load(open(os.path.join(PREFAB, 'GameObject', gf), encoding='utf-8'))
            except Exception:
                continue
            gcomps = [c['component']['m_PathID'] for c in gg.get('m_Component', [])]
            if cpid in gcomps:
                r = find_ps_recursive(gg.get('m_Name'), depth + 1)
                if r:
                    return r
                break
    return None


def load_go_transform(comps):
    """GO 组件列表 → 根 Transform localPosition/localScale (特效挂点偏移/缩放, 3D 模式用)"""
    for c in comps:
        for f in glob.glob(os.path.join(PREFAB, 'Transform', f'*_{c}.json')):
            if f.endswith(f'_{c}.json') and not f.endswith(f'_{c}_{c}.json'):
                tr = json.load(open(f, encoding='utf-8'))
                pos = tr.get('m_LocalPosition', {})
                sc = tr.get('m_LocalScale', {})
                return [pos.get('x', 0), pos.get('y', 0), pos.get('z', 0)], \
                       [sc.get('x', 1), sc.get('y', 1), sc.get('z', 1)]
    return [0, 0, 0], [1, 1, 1]


def convert_effect(go_name, as3d=False):
    """按 GO 名转换特效: GO → ParticleSystem + Renderer → Material → 纹理 (组合特效递归子 GO)"""
    go_files = glob.glob(os.path.join(PREFAB, 'GameObject', go_name + '*.json')) or \
               globals().get('go_files', [])
    if not go_files:
        print(f'✗ 未找到 GO: {go_name}')
        return False
    g = json.load(open(go_files[0], encoding='utf-8'))
    comps = [c['component']['m_PathID'] for c in g.get('m_Component', [])]
    # 找 ParticleSystem (直接组件; 无则递归子 GO)
    ps_path = None
    for c in comps:
        for f in glob.glob(os.path.join(PREFAB, 'ParticleSystem', f'*_{c}.json')):
            if f.endswith(f'_{c}.json') and not f.endswith(f'_{c}_{c}.json'):
                ps_path = f
                break
        if ps_path:
            break
    if not ps_path:
        r = find_ps_recursive(go_name)
        if r:
            resolved_name, ps_path, _, rcomps = r
            g = json.load(open(glob.glob(os.path.join(PREFAB, 'GameObject', resolved_name + '*.json'))[0],
                               encoding='utf-8'))
            comps = rcomps
            print(f'  [子GO] {go_name} → {resolved_name}')
    if not ps_path:
        print(f'✗ {go_name}: 无 ParticleSystem 组件')
        return False
    ps = json.load(open(ps_path, encoding='utf-8'))
    im = ps.get('InitialModule', {})
    # Renderer + 纹理
    tex_path = None
    tex_name = None
    render_mode = 0
    for c in comps:
        rf = glob.glob(os.path.join(PREFAB, 'ParticleSystemRenderer', f'*_{c}.json'))
        if not rf:
            continue
        r = json.load(open(rf[0], encoding='utf-8'))
        render_mode = r.get('m_RenderMode', 0)
        for m in r.get('m_Materials', []):
            pid = m.get('m_PathID')
            for mf in glob.glob(os.path.join(PREFAB, 'Material', f'*_{pid}.json')):
                mat = json.load(open(mf, encoding='utf-8'))
                sp = mat.get('m_SavedProperties', {})
                for key, val in sp.get('m_TexEnvs', []):
                    if isinstance(val, dict) and val.get('m_Texture', {}).get('m_PathID'):
                        tex_pid = val['m_Texture']['m_PathID']
                        tex_name = mat.get('m_Name', '') or go_name
                        tex_path = load_tex_png(tex_pid, go_name)
                        if tex_path:
                            break
                if tex_path:
                    break
            if tex_path:
                break
    # 爆发 (EmissionModule bursts)
    bursts = []
    em = ps.get('EmissionModule', {})
    blist = em.get('m_Bursts') or em.get('bursts') or []
    if isinstance(blist, list):
        for b in blist:
            if isinstance(b, dict):
                t = b.get('time', 0)
                cnt = cv(b.get('countCurve'))
                bursts.append([t, cnt or 1])
    # Size/Color over lifetime (简化: 取曲线关键帧)
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
            k = grad.get(f'key{i}')
            if k:
                keys.append([i / 7.0, [k.get('r', 1), k.get('g', 1), k.get('b', 1), k.get('a', 1)]])
        color_curve = keys
    # 图集帧 (UVModule: tilesX/tilesY + startFrame) → 切片纹理
    frame_grid = None
    start_frame = 0
    uv = ps.get('UVModule', {})
    if uv.get('enabled') and (uv.get('tilesX') or 1) * (uv.get('tilesY') or 1) > 1:
        tx = int(uv.get('tilesX') or 1)
        ty = int(uv.get('tilesY') or 1)
        frame_grid = [tx, ty]
        total = tx * ty
        sf = uv.get('startFrame', {}).get('scalar', 0.0)
        start_frame = int(sf * total) % total if sf else 0
    tex_final = tex_path
    if tex_path and os.path.exists(tex_path):
        # 预乘 alpha 修复 (解包纹理 ~54% alpha 损坏: RGB 完整但 alpha≈0 → 粒子全透明)
        # ⚠️ 只对"RGB 完整"型损坏修复 (RGB 平均 >100); 合法半透明纹理 (暗底亮芯火花图) 不动
        from PIL import Image
        img_tex = Image.open(tex_path).convert('RGBA')
        w0, h0 = img_tex.size
        px0 = img_tex.load()
        n0 = 0; tr0 = 0; rgb_sum = 0
        for yy in range(0, h0, 2):
            for xx in range(0, w0, 2):
                n0 += 1
                p = px0[xx, yy]
                if p[3] < 10:
                    tr0 += 1
                rgb_sum += (p[0] + p[1] + p[2]) / 3
        if n0 > 0 and tr0 / n0 > 0.5 and rgb_sum / n0 > 100:
            r, g, b, a = img_tex.split()
            img_tex = Image.merge('RGBA', (r, g, b, a.point(lambda v: 255)))
            img_tex.save(tex_path)
            print(f'  [alpha修复] {os.path.basename(tex_path)}')
    if tex_path and frame_grid:
        # 切片: 取 start_frame 对应帧
        from PIL import Image
        img_tex = Image.open(tex_path).convert('RGBA')
        w, h = img_tex.size
        fw, fh = w // frame_grid[0], h // frame_grid[1]
        row, col = divmod(start_frame, frame_grid[0])
        crop = img_tex.crop((col * fw, row * fh, (col + 1) * fw, (row + 1) * fh))
        crop = crop.resize((128, 128), Image.LANCZOS)
        tex_final = os.path.join(OUT_TEX, go_name + '_frame.png')
        crop.save(tex_final)
    sc = im.get('startColor', {})
    if as3d:
        # ── 3D 世界空间输出 (unity_particles3d.gd 读取) ──
        offset, escale = load_go_transform(comps)
        shp = ps.get('ShapeModule', {})
        shape = {
            'type': shp.get('shapeType', 0),
            'radius': cv(shp.get('radius'), 1),
            'radiusThickness': cv(shp.get('radiusThickness'), 1),
            'angle': cv(shp.get('angle'), 0),
            'scale': [cv(shp.get('scale', {}).get('x'), 1), cv(shp.get('scale', {}).get('y'), 1),
                      cv(shp.get('scale', {}).get('z'), 1)] if isinstance(shp.get('scale'), dict) else [1, 1, 1],
        }
        life = cv(im.get('startLifetime')) or 1.0
        spd = cv(im.get('startSpeed')) or 0.0
        sz = cv(im.get('startSize')) or 1.0
        out = {
            "name": go_name,
            "effect_offset": [round(v, 3) for v in offset],
            "effect_scale": [round(v, 3) for v in escale],
            "system_lifetime": ps.get('lengthInSec', 1.0),
            "one_shot": not bool(ps.get('looping', False)),
            "play_on_awake": bool(ps.get('playOnAwake', True)),
            "amount": im.get('maxNumParticles', 100),
            "lifetime_min": life,
            "lifetime_max": life,
            "speed_min": spd,
            "speed_max": spd,
            "size_min": sz,
            "size_max": sz,
            "gravity": cv(im.get('gravityModifier')) or 0.0,
            "color_min": [sc.get('minColor', {}).get(k, 1.0) for k in 'rgba'] if sc.get('minColor') else [1, 1, 1, 1],
            "color_max": [sc.get('maxColor', {}).get(k, 1.0) for k in 'rgba'] if sc.get('maxColor') else [1, 1, 1, 1],
            "emission_rate": cv(em.get('rateOverTime')) or 0.0,
            "bursts": bursts,
            "shape": shape,
            "velocity": {},
            "rot_z_speed": 0.0,
            "size_over_lifetime": size_curve,
            "color_over_lifetime": color_curve,
            "render_mode": render_mode,
            "texture": ("res://assets/particles/" + os.path.basename(tex_final)) if tex_final else "",
        }
        os.makedirs(OUT_JSON3D, exist_ok=True)
        fp = os.path.join(OUT_JSON3D, go_name + '.json')
    else:
        out = {
            "name": go_name,
            "system_lifetime": ps.get('lengthInSec', 1.0),
            "one_shot": not bool(ps.get('looping', False)),
            "play_on_awake": bool(ps.get('playOnAwake', True)),
            "amount": im.get('maxNumParticles', 100),
            "lifetime": cv(im.get('startLifetime')) or 1.0,
            "speed_min": cv(im.get('startSpeed')) or 0.0,
            "speed_max": cv(im.get('startSpeed')) or 0.0,
            "size_min": cv(im.get('startSize')) or 1.0,
            "size_max": cv(im.get('startSize')) or 1.0,
            "gravity": cv(im.get('gravityModifier')) or 0.0,
            "color_min": [sc.get('minColor', {}).get(k, 1.0) for k in 'rgba'] if sc.get('minColor') else [1, 1, 1, 1],
            "color_max": [sc.get('maxColor', {}).get(k, 1.0) for k in 'rgba'] if sc.get('maxColor') else [1, 1, 1, 1],
            "emission_rate": cv(em.get('rateOverTime')) or 0.0,
            "bursts": bursts,
            "shape_type": ps.get('ShapeModule', {}).get('shapeType'),
            "render_mode": render_mode,
            "size_over_lifetime": size_curve,
            "color_over_lifetime": color_curve,
            "texture": ("res://assets/particles/" + os.path.basename(tex_final)) if tex_final else "",
        }
        os.makedirs(OUT_JSON, exist_ok=True)
        fp = os.path.join(OUT_JSON, go_name + '.json')
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f'✓ {go_name}: lifetime={out["lifetime_max" if as3d else "lifetime"]} size={out["size_min"]} '
          f'bursts={bursts} tex={os.path.basename(tex_path) if tex_path else "无"} -> {fp}')
    return True


def main():
    args = sys.argv[1:] or ['AttackHitSmall', 'Actual_Explosion']
    as3d = False
    if args and args[0] == '--3d':
        as3d = True
        args = args[1:]
    ok = 0
    for a in args:
        if a.endswith('.json'):
            go_name = os.path.basename(a).split('_')[0]
        else:
            go_name = a
        if convert_effect(go_name, as3d):
            ok += 1
    print(f'完成 {ok}/{len(args)}' + (' (3D)' if as3d else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
