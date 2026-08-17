# -*- coding: utf-8 -*-
"""
convert_unity_particles.py — Unity ParticleSystem JSON → Godot 粒子中间格式
输入: 特效名 (GO 名, 如 AttackHitSmall) 或 ParticleSystem JSON 路径 (可多个)
输出: D:/warpforge/data/particles/<名>.json (简化参数) + 纹理 (从 bundle 或解包目录)
用法: py312/python.exe scripts/convert_unity_particles.py AttackHitSmall Actual_Explosion ...
"""
import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PREFAB = r'D:\2\解包整理\08_预制体特效\战斗预制体'
SHARED = r'D:\2\解包整理\08_预制体特效\共享资源'
OUT_JSON = r'D:\warpforge\data\particles'
OUT_TEX = r'D:\warpforge\assets\particles'
BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'


def find_files(d, fname, pid):
    """按文件名或 PathID 后缀找文件"""
    out = glob.glob(os.path.join(d, fname, f'*_{pid}.json')) + \
          glob.glob(os.path.join(d, fname, f'{pid}.json'))
    return out


def cv(v):
    """MinMaxCurve → 常数 (scalar / minScalar 优先)"""
    if isinstance(v, dict):
        st = v.get('minMaxState', 0)
        if st == 0:
            return v.get('scalar')
        return v.get('minScalar')
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


def convert_effect(go_name):
    """按 GO 名转换特效: GO → ParticleSystem + Renderer → Material → 纹理"""
    go_files = glob.glob(os.path.join(PREFAB, 'GameObject', go_name + '*.json')) or \
               globals().get('go_files', [])
    if not go_files:
        print(f'✗ 未找到 GO: {go_name}')
        return False
    g = json.load(open(go_files[0], encoding='utf-8'))
    comps = [c['component']['m_PathID'] for c in g.get('m_Component', [])]
    # 找 ParticleSystem
    ps_path = None
    for c in comps:
        for f in glob.glob(os.path.join(PREFAB, 'ParticleSystem', f'*_{c}.json')):
            if f.endswith(f'_{c}.json') and not f.endswith(f'_{c}_{c}.json'):
                ps_path = f
                break
        if ps_path:
            break
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
        from PIL import Image
        img_tex = Image.open(tex_path).convert('RGBA')
        w0, h0 = img_tex.size
        px0 = img_tex.load()
        n0 = 0; tr0 = 0
        for yy in range(0, h0, 2):
            for xx in range(0, w0, 2):
                n0 += 1
                if px0[xx, yy][3] < 10:
                    tr0 += 1
        if n0 > 0 and tr0 / n0 > 0.5:
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
    print(f'✓ {go_name}: lifetime={out["lifetime"]} size={out["size_min"]} '
          f'bursts={bursts} tex={os.path.basename(tex_path) if tex_path else "无"} -> {fp}')
    return True


def main():
    args = sys.argv[1:] or ['AttackHitSmall', 'Actual_Explosion']
    ok = 0
    for a in args:
        if a.endswith('.json'):
            go_name = os.path.basename(a).split('_')[0]
        else:
            go_name = a
        if convert_effect(go_name):
            ok += 1
    print(f'完成 {ok}/{len(args)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
