#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unity_scene_to_godot.py — 阵营战场 Unity 场景 → Godot 场景脚本 (完全复刻路线)

读 07_场景/<arena>/ 的 GameObject/Transform/MeshFilter/MeshRenderer/SkinnedMeshRenderer/
Material/ParticleSystem/ParticleSystemRenderer/Camera/Light/RenderSettings JSON,
按说明书链路组装出 Godot 场景 (原版层级 + 局部变换 + 材质链 + 粒子):

  - 层级: Transform m_Father/m_Children 原版嵌套, m_LocalPosition/m_LocalRotation/m_LocalScale
          (解包 OBJ 为原始 Unity Y-up 顶点, 与场景局部变换同轴; 输出用 node.quaternion 直赋,
          避免 tscn 矩阵序列化的轴序歧义; **OBJ 的 vt v 勿手动翻转——Godot 导入器自动 1-v**)
  - 网格: MeshFilter.m_Mesh {m_FileID, m_PathID} → Mesh 名 → OBJ
          (fid=3 场景 bundle; fid=N 按场景 externals CAB→bundle 解析)
  - 材质: MeshRenderer.m_Materials → Material JSON/typetree →
          m_SavedProperties.m_TexEnvs(_BaseMap/_MainTex) → 贴图名 → PNG
          _Blend 0=alpha(透明看 _SURFACE_TYPE_TRANSPARENT) 1=LUT(跳过) 2=ADD
          _Cull 2=back(默认) 0=both 1=front; _ZWrite; _BaseColor/_EmissionColor; _UVSpeed
  - 粒子: InitialModule/EmissionModule/ShapeModule/SizeModule/ColorModule/VelocityModule/
          RotationModule → GPUParticles3D (billboard/mesh, 贴图混合, 大小/颜色曲线)
  - 相机/灯: Camera fov/near/far + 相机 Y+180 (Unity +Z 朝前 / Godot -Z);
            DirectionalLight 同 Y+180 (方向 = -R·Z)
  - 环境: RenderSettings ambient(SkyColor/Intensity)/fog(color/density)/背景色

输出 (--out 为 Godot 项目目录):
  assets/meshes/<Mesh名>.obj / assets/textures/<贴图名>.png   缺失才导出
  scenes/unity_arena_<arena>.gd + <arena>.tscn               自动生成场景 (根 x-100)

用法:
  py312/python.exe unity_scene_to_godot.py --arena battlearenablacklegion
  py312/python.exe unity_scene_to_godot.py --arena battlearena2 --out d:/2/战场演示
  (--roots 留空 = 按子树含量自动识别 3D 根: 各变体根名不统一, 名字过滤会漏 battlearena2/leviathan)
多变体要点 (2026-08-22):
  - 资源同名异内容: 'Combined Mesh (root: scene)'/Flame03/Atlas 等跨变体常见 → 内容哈希去重, 不同则 <名>__<arena> 后缀
  - 环境逐变体读 m_AmbientSky/Equator/GroundColor (平均×AMB_TRILIGHT_FACTOR), 光色=m_Color×LIGHT_WARM_FACTOR
  - 相机 m_Enabled=0 (reflection camera) → enabled=false; 背景色取 3D 相机 m_BackGroundColor
"""
import argparse
import glob
import json
import math
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SCENE_ROOT = 'd:/2/解包整理/07_场景/'
BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
CAB_MAP_CACHE = os.path.join(DATA_DIR, 'cab_bundle_map.json')
PID_RE = re.compile(r'^(.+?)_(\d+)\.json$')
# 外部资源固定回退搜查包 (粒子材质/贴图/网格主要在共享包)
SHARED_PACKS = ['battlesharedresources_assets_all.bundle',
                'duplicateassetisolation_assets_all.bundle',
                'battleprefabs_vfxandmisc_assets_all.bundle',
                'atlasindividual_assets_battleatlasui.bundle',
                'boosterpacks_assets_all.bundle']
# Trilight 平均 → Godot 平坦环境色校准残差 (黑军团实测值: 平均(0.638,0.631,0.892)→发射(0.674,0.641,0.870))
# 逐变体读取 m_AmbientSky/Equator/GroundColor 平均后乘此因子, 黑军团再生=原校准值不变
AMB_TRILIGHT_FACTOR = (1.0559, 1.0160, 0.9759)
# 太阳暖色校正: 黑军团验证 = 原版白日光 × (1, 0.957, 0.839) (Filmic 压缩 G/B 的 LUT 补偿)
LIGHT_WARM_FACTOR = (1.0, 0.957, 0.839)


# ---------------------------------------------------------------- JSON 读取
def load_pid_dir(d):
    out = {}
    if not os.path.isdir(d):
        return out
    for fn in os.listdir(d):
        m = PID_RE.match(fn)
        if not m or not fn.endswith('.json'):
            continue
        try:
            out[int(m.group(2))] = json.load(open(os.path.join(d, fn), encoding='utf-8'))
        except Exception:
            continue
    return out


def load_go_dir(d):
    known, plain = {}, {}
    if not os.path.isdir(d):
        return known, plain
    for fn in os.listdir(d):
        if not fn.endswith('.json'):
            continue
        m = PID_RE.match(fn)
        try:
            data = json.load(open(os.path.join(d, fn), encoding='utf-8'))
        except Exception:
            continue
        if m:
            known[int(m.group(2))] = data
        else:
            plain.setdefault(data.get('m_Name', ''), []).append(data)
    return known, plain


# ---------------------------------------------------------------- 数学
def q_mul(a, b):
    ax, ay, az, aw = a
    bx, by, bz, bw = b
    return (
        aw * bx + ax * bw + ay * bz - az * by,
        aw * by - ax * bz + ay * bw + az * bx,
        aw * bz + ax * by - ay * bx + az * bw,
        aw * bw - ax * bx - ay * by - az * bz,
    )


def q_rot_vec(q, v):
    """四元数 (x,y,z,w) 旋转向量 v"""
    x, y, z, w = q
    vx, vy, vz = v
    tx = 2.0 * (y * vz - z * vy)
    ty = 2.0 * (z * vx - x * vz)
    tz = 2.0 * (x * vy - y * vx)
    return (vx + w * tx + y * tz - z * ty,
            vy + w * ty + z * tx - x * tz,
            vz + w * tz + x * ty - y * tx)


def reflect_z_q(q):
    """Z 反射共轭: R' = M·R·M (M=diag(1,1,-1)) → 四元数 (x,y,z,w)→(-x,-y,z,w).
    Unity(左手系, +Z 前) 数据放进 Godot(右手系, -Z 前) 的标准转换:
    整世界内容进 scale=(1,1,-1) 根 (z 镜像, Godot 自动翻绕序),
    相机移出镜像根: 位置 z 取反 + 四元数 Z 反射共轭 (无需 Y180).
    只给相机转 Y180 而不做世界镜像 = 画面水平镜像 (左右互换, 本战场 bug 根因)."""
    return (-q[0], -q[1], q[2], q[3])


def reflect_x_q(q):
    """X 反射共轭: M=diag(-1,1,1), R' = M·R·M → 四元数 (x,y,z,w)→(x,-y,-z,w).
    Unity (左手系, +Z 前) 导出数据 → Godot (右手系, -Z 前) 必须整世界 X 反射,
    OBJ 顶点+绕序同时反射, 否则画面水平镜像 (相机 Y180 只转正朝向, 无法修手性)."""
    return (q[0], -q[1], -q[2], q[3])


def curve_min_max(v, default=1.0):
    if isinstance(v, dict):
        if v.get('minMaxState', 0) == 0:
            return v.get('scalar', default), v.get('scalar', default)
        return v.get('minScalar', default), v.get('maxScalar', v.get('scalar', default))
    return v, v


def curve_scalar(v, default=0.0):
    if isinstance(v, dict):
        return v.get('scalar', default)
    return v


def curve_keys(v):
    if not isinstance(v, dict):
        return []
    mc = v.get('maxCurve', {}) or {}
    return [(k.get('time', 0.0), k.get('value', 1.0))
            for k in (mc.get('m_Curve', []) or []) if isinstance(k, dict)]


def grad_keys(v):
    """Unity Gradient → 8 点梯度: color keys 按 ctime, alpha keys 按 atime 独立插值
    (旧实现按 key 序号均匀分布, 会把 a=1 的早淡出段错位到中段 → 烟半生即透明)"""
    if not isinstance(v, dict):
        return []
    g = v.get('maxGradient', {}) or {}
    ncol = int(g.get('m_NumColorKeys', 2) or 2)
    nalpha = int(g.get('m_NumAlphaKeys', 2) or 2)

    def pairs(kind, n, key):
        out = []
        for i in range(n):
            k = g.get('key%d' % i)
            if not isinstance(k, dict):
                continue
            t = (g.get('%s%d' % (kind, i), 0) or 0) / 65535.0
            out.append((t, key(k)))
        return out

    cols = pairs('ctime', ncol, lambda k: (float(k.get('r', 0.0)), float(k.get('g', 0.0)), float(k.get('b', 0.0))))
    alphas = pairs('atime', nalpha, lambda k: float(k.get('a', 0.0)))

    def interp(ps, t):
        if not ps:
            return None
        if t <= ps[0][0]:
            return ps[0][1]
        if t >= ps[-1][0]:
            return ps[-1][1]
        for i in range(len(ps) - 1):
            t0, v0 = ps[i]
            t1, v1 = ps[i + 1]
            if t0 <= t <= t1:
                f = 0.0 if t1 == t0 else (t - t0) / (t1 - t0)
                if isinstance(v0, tuple):
                    return tuple(a + (b - a) * f for a, b in zip(v0, v1))
                return v0 + (v1 - v0) * f
        return ps[-1][1]

    # 联合时间轴 (color 键+alpha 键的并集): 每个时间点 color/alpha 各自插值 —
    # 比 8 点均匀重采样精确 (原版键位如 Light Shaft 呼吸脉动 α .2265/.447/.659 会保留)
    ts = sorted(set([t for t, _ in cols] + [t for t, _ in alphas]))
    out = []
    for t in ts:
        c = interp(cols, t) or (1.0, 1.0, 1.0)
        a = float(interp(alphas, t) if alphas else 1.0)
        out.append((t, (c[0], c[1], c[2], a)))
    return out


def col_str(c):
    return 'Color(%.4f, %.4f, %.4f, %.4f)' % (
        c.get('r', 1.0), c.get('g', 1.0), c.get('b', 1.0), c.get('a', 1.0))


def safe_name(nm):
    s = re.sub(r'[^0-9A-Za-z_]', '_', nm).strip('_') or 'Node'
    if s[0].isdigit():
        s = '_' + s
    return s


# ---------------------------------------------------------------- Bundle 解析


def _saved_props_dict(sp):
    """UnityPy typed m_SavedProperties → {'m_TexEnvs': [[slot, {m_Texture {...}, ...}], ...],
    'm_Floats': [[k, v], ...], 'm_Colors': [[k, {...}], ...]} (和本地 JSON 同构)"""
    out = {'m_TexEnvs': [], 'm_Floats': [], 'm_Colors': []}
    for sect, key in [('m_TexEnvs', 'm_Texture'), ('m_Floats', None), ('m_Colors', None)]:
        items = getattr(sp, sect, None) or []
        for it in items:
            try:
                name = str(it[0])
            except Exception:
                continue
            val = it[1]
            if sect == 'm_TexEnvs':
                ent = {'m_Texture': {}, 'm_Scale': {'x': 1, 'y': 1}, 'm_Offset': {'x': 0, 'y': 0}}
                try:
                    t = val.m_Texture
                    ent['m_Texture'] = {'m_FileID': getattr(t, 'm_FileID', 0), 'm_PathID': getattr(t, 'm_PathID', 0)}
                    sc = val.m_Scale
                    ent['m_Scale'] = {'x': getattr(sc, 'x', 1.0), 'y': getattr(sc, 'y', 1.0)}
                except Exception:
                    pass
                out['m_TexEnvs'].append([name, ent])
            elif sect == 'm_Floats':
                out['m_Floats'].append([name, float(val) if not isinstance(val, tuple) else float(val[0])])
            else:
                try:
                    c = val
                    out['m_Colors'].append([name, {'r': float(getattr(c, 'r', 1.0)),
                                                   'g': float(getattr(c, 'g', 1.0)),
                                                   'b': float(getattr(c, 'b', 1.0)),
                                                   'a': float(getattr(c, 'a', 1.0))}])
                except Exception:
                    pass
    return out

class BundleResolver:
    """场景 bundle + externals(CAB→bundle) 引用解析; 索引 Mesh/Texture2D/Material"""

    def __init__(self, arena):
        self.arena = arena
        self.path = os.path.join(BUNDLE_DIR, 'scenes_scenes_%s.bundle' % arena)
        if not os.path.exists(self.path):
            raise SystemExit('[错误] 场景 bundle 不存在: %s' % self.path)
        import UnityPy
        self.UnityPy = UnityPy
        self.env = UnityPy.load(self.path)
        self.local = {}
        self._index_env(self.env, self.local)
        sf = self.env.objects[0].assets_file
        self.ext = {}
        for i, e in enumerate(sf.externals):
            m = re.search(r'CAB-[0-9a-f]+', str(e))
            if m:
                self.ext[i + 1] = m.group(0)
        self.cab_map = self._cab_map()
        self.ext_index = {}

    def _index_env(self, env, target):
        for o in env.objects:
            t = o.type.name
            if t in ('Mesh', 'Texture2D', 'Material'):
                target.setdefault(t, {})[o.path_id] = o

    def obj_name(self, o):
        """对象名: dict(本地MAT JSON) 或 UnityPy ObjectReader (read_typetree 元数据, 不解码数据)"""
        if o is None:
            return ''
        if isinstance(o, dict):
            return str(o.get('m_Name', ''))
        try:
            return str(o.read_typetree().get('m_Name', ''))
        except Exception:
            try:
                return str(o.read().m_Name)
            except Exception:
                return ''

    def _cab_map(self):
        if os.path.exists(CAB_MAP_CACHE):
            try:
                return json.load(open(CAB_MAP_CACHE, encoding='utf-8'))
            except Exception:
                pass
        m = {}
        for fn in os.listdir(BUNDLE_DIR):
            if not fn.endswith('.bundle'):
                continue
            with open(os.path.join(BUNDLE_DIR, fn), 'rb') as f:
                head = f.read(1 << 20)
            if not head.startswith(b'UnityFS'):
                continue
            for c in re.findall(rb'CAB-[0-9a-f]{32}', head):
                m.setdefault(c.decode(), []).append(fn)
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(CAB_MAP_CACHE, 'w', encoding='utf-8') as f:
            json.dump(m, f, ensure_ascii=False, indent=1)
        return m

    def read_obj(self, ref, want=None):
        fid = ref.get('m_FileID', 0)
        pid = ref.get('m_PathID')
        if pid in (None, 0):
            return None
        # 本地优先: 各变体 dripped JSON 的 fid 语义不一 (0/3=本地; 也有 2/5/6=本地),
        # 本地能命中就直接返回 (darkangels fid2 pid34='Background space' 等); want=期望类型防跨类型撞号
        if want:
            d = self.local.get(want)
            if d and pid in d:
                return d[pid]
        else:
            for d in self.local.values():
                if pid in d:
                    return d[pid]
        if fid in (0, 3):
            found = self._find_ext(pid, want)
            if found is not None:
                return found
        # 外部引用: 先按 externals CAB→bundle 候选扫, 再扫固定共享包 (头部扫描映射不可靠)
        # (fid 0/3 也会走到这里 — dripped JSON 的 fid 语义不一, 贴图常在 battlesharedresources)
        cab = self.ext.get(fid)
        bundles = list(self.cab_map.get(cab, [])) if cab else []
        for bname in SHARED_PACKS:
            if bname not in bundles:
                bundles.append(bname)
        found = self._scan_bundles(pid, bundles, want)
        if found is not None:
            return found
        return self._find_ext(pid, want)

    def _scan_bundles(self, pid, bundles, want=None):
        for bname in bundles:
            if bname not in self.ext_index:
                try:
                    env = self.UnityPy.load(os.path.join(BUNDLE_DIR, bname))
                    d = {}
                    self._index_env(env, d)
                    self.ext_index[bname] = d
                except Exception:
                    self.ext_index[bname] = None
            idx = self.ext_index.get(bname)
            if not idx:
                continue
            if want:
                d = idx.get(want)
                if d and pid in d:
                    return d[pid]
            else:
                for d in idx.values():
                    if pid in d:
                        return d[pid]
        return None

    def _find_ext(self, pid, want=None):
        for idx in self.ext_index.values():
            if not idx:
                continue
            if want:
                d = idx.get(want)
                if d and pid in d:
                    return d[pid]
            else:
                for d in idx.values():
                    if pid in d:
                        return d[pid]
        return None

    def mat_data(self, ref):
        """external Material → dict (UnityPy typed 对象直接读 m_SavedProperties)"""
        obj = self.read_obj(ref, 'Material')
        if obj is None:
            return None
        if isinstance(obj, dict):
            return obj
        # typed Material 对象 → read(): m_SavedProperties 转 dict
        try:
            obj = obj.read()
            sp = getattr(obj, 'm_SavedProperties', None)
            if sp is None:
                return None
            d = {'m_Name': getattr(obj, 'm_Name', '') or 'ext_mat',
                 'm_ValidKeywords': list(getattr(obj, 'm_ValidKeywords', []) or []),
                 'm_SavedProperties': _saved_props_dict(sp)}
            return d
        except Exception:
            return None


# ---------------------------------------------------------------- 材质
class MatInfo:
    def __init__(self, name, tex_ref, blend, keywords, cull, zwrite,
                 base_color, emission_color, uv_speed, mat_color=None,
                 tex_ref2=None, vector4_1=None):
        self.name = name
        self.tex_ref = tex_ref
        self.tex_name = None
        self.tex_obj = None
        self.tex_ref2 = tex_ref2       # _SecondaryTex (UV Scroll Runes 第二贴图)
        self.tex_name2 = None
        self.tex_obj2 = None
        self.blend = blend
        self.keywords = keywords or []
        self.cull = cull
        self.zwrite = zwrite
        self.base_color = base_color
        self.emission_color = emission_color
        self.mat_color = mat_color
        self.uv_speed = uv_speed
        self.vector4_1 = vector4_1     # Runes 滚动参数 (r,g,b=tex2平铺, 滚动速率) 疑似 (1,1,0.02,0)

    def is_transparent(self):
        return '_SURFACE_TYPE_TRANSPARENT' in self.keywords or \
            '_ALPHABLEND_ON' in self.keywords or self.blend > 0

    def emission_energy(self):
        c = self.emission_color or {}
        return max(abs(c.get('r', 0.0)), abs(c.get('g', 0.0)), abs(c.get('b', 0.0)), 1.0)


def parse_mat(raw, name_hint=''):
    if not isinstance(raw, dict):
        return None
    sp = raw.get('m_SavedProperties', {}) or {}
    texenvs = sp.get('m_TexEnvs', []) or []
    floats = {k: v for k, v in (sp.get('m_Floats', []) or [])}
    colors = {k: v for k, v in (sp.get('m_Colors', []) or [])}
    tex_ref = None
    tex_ref2 = None
    for pair in texenvs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            continue
        slot = pair[0]
        t = pair[1].get('m_Texture', {}) if isinstance(pair[1], dict) else {}
        if not t.get('m_PathID'):
            continue
        if slot == '_SecondaryTex' and tex_ref2 is None:
            tex_ref2 = t
        elif slot in ('_BaseMap', '_MainTex') and tex_ref is None:
            tex_ref = t
    uv = floats.get('_UVSpeed')
    uv_speed = (float(uv.get('x', 1.0)), float(uv.get('y', 1.0))) if isinstance(uv, dict) else None
    return MatInfo(str(raw.get('m_Name') or name_hint), tex_ref,
                   float(floats.get('_Blend', 0.0) or 0.0),
                   list(raw.get('m_ValidKeywords', []) or []),
                   float(floats.get('_Cull', 2.0) or 2.0),
                   float(floats.get('_ZWrite', 1.0) or 1.0),
                   colors.get('_BaseColor') or colors.get('_Color'),
                   colors.get('_EmissionColor'), uv_speed,
                   raw.get('m_Color') or colors.get('m_Color'),
                   tex_ref2, colors.get('Vector4_1'))


# ---------------------------------------------------------------- 汇编
class Assembler:
    def __init__(self, arena, out_dir):
        self.arena = arena
        self.out = out_dir
        self.root_dir = os.path.join(SCENE_ROOT, arena)
        self.b = BundleResolver(arena)
        self.TF = load_pid_dir(os.path.join(self.root_dir, 'Transform'))
        self.GO, _ = load_go_dir(os.path.join(self.root_dir, 'GameObject'))
        self.MF = load_pid_dir(os.path.join(self.root_dir, 'MeshFilter'))
        self.MR = load_pid_dir(os.path.join(self.root_dir, 'MeshRenderer'))
        self.SMR = load_pid_dir(os.path.join(self.root_dir, 'SkinnedMeshRenderer'))
        self.MAT = load_pid_dir(os.path.join(self.root_dir, 'Material'))
        self.PS = load_pid_dir(os.path.join(self.root_dir, 'ParticleSystem'))
        self.PSR = load_pid_dir(os.path.join(self.root_dir, 'ParticleSystemRenderer'))
        self.CAM = load_pid_dir(os.path.join(self.root_dir, 'Camera'))
        self.LIG = load_pid_dir(os.path.join(self.root_dir, 'Light'))
        self.REN = load_pid_dir(os.path.join(self.root_dir, 'RenderSettings'))
        self.TEXDIR = os.path.join(self.root_dir, 'Texture2D')
        # 后处理 ColorLookup 的 LUT 贴图引用 (PostProcessing Profile: Bloom/Vignette/ColorLookup)
        self.lut_ref_val = None
        for f in glob.glob(os.path.join(self.root_dir, 'MonoBehaviour', '*.json')):
            try:
                d = json.load(open(f, encoding='utf-8'))
            except Exception:
                continue
            if d.get('m_Name') == 'ColorLookup':
                t = d.get('texture', {}).get('m_Value', {})
                if t.get('m_PathID'):
                    self.lut_ref_val = t
                    break
        self.go_comps = {}
        for pid, g in self.GO.items():
            for c in g.get('m_Component', []):
                self.go_comps.setdefault(pid, []).append(c.get('component', {}).get('m_PathID'))
        self.mat_cache = {}

    def go(self, pid):
        return self.GO.get(pid, {'m_Name': 'GO%d' % pid, 'm_Component': []})

    def root_transforms(self):
        return [tp for tp in self.TF if self.TF[tp].get('m_Father', {}).get('m_PathID') not in self.TF]

    def children_of(self, tpid):
        return [c.get('m_PathID') for c in self.TF[tpid].get('m_Children', [])
                if c.get('m_PathID') in self.TF]

    def local_trans(self, tpid):
        td = self.TF[tpid]
        lp = td.get('m_LocalPosition', {})
        lr = td.get('m_LocalRotation', {})
        ls = td.get('m_LocalScale', {})
        return (lp.get('x', 0.0), lp.get('y', 0.0), lp.get('z', 0.0),
                (lr.get('x', 0.0), lr.get('y', 0.0), lr.get('z', 0.0), lr.get('w', 1.0)),
                (ls.get('x', 1.0), ls.get('y', 1.0), ls.get('z', 1.0)))

    def mesh_of(self, gopid):
        for c in self.go_comps.get(gopid, []):
            mf = self.MF.get(c)
            if mf:
                ref = mf.get('m_Mesh', {})
                obj = self.b.read_obj(ref, 'Mesh')
                if obj is None:
                    return None, None
                return (self.b.obj_name(obj) or 'mesh%d' % ref.get('m_PathID')), obj
        # SkinnedMeshRenderer (黑军团 Chain1/Chain2 铁链: 单骨骼=自身, 绑定位=GO 变换; 静态呈现即可,
        # 形态键甩鞭动画见 clip17 接入) — 没有 SMR 就返回 None
        for c in self.go_comps.get(gopid, []):
            smr = self.SMR.get(c)
            if smr:
                ref = smr.get('m_Mesh', {})
                obj = self.b.read_obj(ref, 'Mesh')
                if obj is None:
                    return None, None
                return (self.b.obj_name(obj) or 'mesh%d' % ref.get('m_PathID')), obj
        return None, None

    def mats_of(self, gopid):
        out = []
        for c in self.go_comps.get(gopid, []):
            mr = self.MR.get(c) or self.SMR.get(c)
            if not mr:
                continue
            for ref in mr.get('m_Materials', []):
                mi = self.mat_of(ref)
                if mi:
                    out.append(mi)
        return out

    def mat_of(self, ref):
        pid, fid = ref.get('m_PathID'), ref.get('m_FileID', 0)
        key = (fid, pid)
        if key in self.mat_cache:
            return self.mat_cache[key]
        raw = self.MAT.get(pid)
        if raw is None:
            raw = self.b.mat_data(ref)
        mi = parse_mat(raw, 'mat_%s' % pid) if raw else None
        if mi and mi.tex_ref:
            obj = self.b.read_obj(mi.tex_ref, 'Texture2D')
            if obj is not None:
                mi.tex_name = self.b.obj_name(obj) or 'tex_%s' % mi.tex_ref.get('m_PathID')
                mi.tex_obj = obj
        if mi and mi.tex_ref2:
            obj2 = self.b.read_obj(mi.tex_ref2, 'Texture2D')
            if obj2 is not None:
                mi.tex_name2 = self.b.obj_name(obj2) or 'tex2_%s' % mi.tex_ref2.get('m_PathID')
                mi.tex_obj2 = obj2
        self.mat_cache[key] = mi
        return mi

    def ps_of(self, gopid):
        for c in self.go_comps.get(gopid, []):
            if c in self.PS:
                ps = self.PS[c]
                render_mode, mesh_ref, mats = 0, None, []
                for c2 in self.go_comps.get(gopid, []):
                    psr = self.PSR.get(c2)
                    if psr:
                        render_mode = psr.get('m_RenderMode', 0)
                        mesh_ref = psr.get('m_Mesh', {}) or None
                        for ref in psr.get('m_Materials', []):
                            mats.append(self.mat_of(ref))
                        break
                return ps, render_mode, mesh_ref, [m for m in mats if m]
        return None, 0, None, []

    def has_ps(self, gopid):
        return any(c in self.PS for c in self.go_comps.get(gopid, []))

    def has_comp(self, gopid, comps):
        return any(c in comps for c in self.go_comps.get(gopid, []))

    def has_smr(self, gopid):
        return any(c in self.SMR for c in self.go_comps.get(gopid, []))

    def subtree_has_3d(self, tpid, seen=frozenset()):
        """子树内是否含可见 3D (PS/相机/灯/带材质网格) — 自动识别 3D 根用
        (各变体根名不统一: Scrap_4/Battle Arena X Baked/Particle Effects/Scenario/BattlePrefab)"""
        if tpid in seen:
            return False
        seen = seen | {tpid}
        gopid = self.TF[tpid].get('m_GameObject', {}).get('m_PathID')
        comps = self.go_comps.get(gopid, [])
        for c in comps:
            if c in self.PS or c in self.CAM or c in self.LIG:
                return True
            if c in self.MF and self.MF[c].get('m_Mesh', {}).get('m_PathID'):
                return True
            if c in self.MR and self.MR[c].get('m_Materials'):
                return True
        for ch in self.TF[tpid].get('m_Children', []):
            cid = ch.get('m_PathID')
            if cid in self.TF:
                if self.subtree_has_3d(cid, seen):
                    return True
        return False

    def auto_roots(self):
        return [tp for tp in self.root_transforms() if self.subtree_has_3d(tp)]


# ---------------------------------------------------------------- GDScript 写器
class GdWriter:
    def __init__(self, f):
        self.f = f
        self._var = 0

    def var(self, base='n'):
        self._var += 1
        return '%s%d' % (base, self._var)

    def line(self, s=''):
        self.f.write(s + '\n')

    def next_id(self, prefix):
        self._var += 1
        return '%s_%d' % (prefix, self._var)


# 原版 shader "Unlit UV scroll" (11_着色器 shaders/Shader_5091587426579848444): _MainTex+_SecondaryTex 双层,
# "UV Scale (XY) Speed (ZW)" 属性 → 黑军团 Vector4_1=(1,1,0.02,0) 副贴图 U 向 0.02/s 慢滚动 (Runes 符文);
# _Layers_Blend_Opacity 1.0 / unlit 无光照。Godot: unshaded spatial 双层 mix + TIME 滚动。
UV_SCROLL_SHADER = '''shader_type spatial;
render_mode unshaded, blend_mix;
uniform sampler2D main_tex : filter_linear, repeat_enable;
uniform sampler2D secondary_tex : filter_linear, repeat_enable;
uniform float layers_blend_opacity : hint_range(0.0, 1.0) = 1.0;
uniform vec4 uv_scroll = vec4(1.0, 1.0, 0.02, 0.0);

void fragment() {
	vec4 c1 = texture(main_tex, UV);
	vec4 c2 = texture(secondary_tex, UV * uv_scroll.xy + vec2(uv_scroll.z, uv_scroll.w) * TIME);
	vec4 c = mix(c1, c2, layers_blend_opacity);
	ALBEDO = c.rgb;
	ALPHA = c.a;
}
'''


def mat_gd(w, var, mi, tex_paths):
    """生成 StandardMaterial3D 代码, 返回变量名; _SecondaryTex 双贴图材质 → UV scroll ShaderMaterial"""
    if mi.tex_name2 and mi.tex_name2 in tex_paths:
        # 双贴图 (Runes "Unlit UV scroll"): shader 双层 + TIME 滚动
        w.line('var %s := ShaderMaterial.new()' % var)
        w.line('%s.shader = load("res://assets/uv_scroll.gdshader")' % var)
        w.line('%s.set_shader_parameter("main_tex", load(%r))' % (var, tex_paths[mi.tex_name]))
        w.line('%s.set_shader_parameter("secondary_tex", load(%r))' % (var, tex_paths[mi.tex_name2]))
        v4 = mi.vector4_1 or {}
        sc = (float(v4.get('r', 1.0) or 1.0), float(v4.get('g', 1.0) or 1.0),
              float(v4.get('b', 0.0) or 0.0), float(v4.get('a', 0.0) or 0.0))
        w.line('%s.set_shader_parameter("uv_scroll", Vector4(%.3f, %.3f, %.3f, %.3f))' % (var, *sc))
        op = 1.0  # _Layers_Blend_Opacity (黑军团 UV Scroll Runes=1.0)
        w.line('%s.set_shader_parameter("layers_blend_opacity", %.2f)' % (var, op))
        if mi.cull == 0:
            w.line('%s.cull_mode = BaseMaterial3D.CULL_DISABLED' % var)
        return var
    w.line('var %s := StandardMaterial3D.new()' % var)
    if mi.tex_name and mi.tex_name in tex_paths:
        w.line('%s.albedo_texture = load(%r)' % (var, tex_paths[mi.tex_name]))
    if mi.base_color:
        w.line('%s.albedo_color = %s' % (var, col_str(mi.base_color)))
    if mi.is_transparent():
        w.line('%s.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA' % var)
        if mi.zwrite <= 0:
            w.line('%s.depth_draw_mode = BaseMaterial3D.DEPTH_DRAW_DISABLED' % var)
    if mi.blend >= 2:
        w.line('%s.blend_mode = BaseMaterial3D.BLEND_MODE_ADD' % var)
    if mi.cull == 0:
        w.line('%s.cull_mode = BaseMaterial3D.CULL_DISABLED' % var)
    elif mi.cull == 1:
        w.line('%s.cull_mode = BaseMaterial3D.CULL_FRONT' % var)
    if mi.emission_color:
        w.line('%s.emission_enabled = true' % var)
        w.line('%s.emission_energy_multiplier = %.3f' % (var, mi.emission_energy()))
    w.line('%s.roughness = 0.9' % var)
    return var


# 原版 Battle Arena 4 PostProcessing 按说明文件 (原始 Unity JSON) 复刻:
# Bloom(threshold 1.15/intensity 5.0/scatter 1.0/skipIterations 6) + Vignette(0.297, smoothness 0.2 默认)
# + ColorLookup(LUT 图, contribution 1.0) + LUTBlender 全屏 pass(_LUT2=同图, _Blend 1.0 纯上屏)
# → 黑军团 ColorLookup=LUT Normal(共享资源, 标准 16^3 identity LUT: 行=G 层/格=B 层/格内=R 渐变, 直采=本色=
#   无颜色分级; 其余阵营各引用自家 LUT Battle Arena <X>.png)。LUT 布局采样: 半像素偏移 + bilinear。
LUT_SHADER = '''shader_type canvas_item;
uniform sampler2D screen_tex : hint_screen_texture, filter_linear_mipmap;
uniform sampler2D lut : filter_linear, repeat_disable;
uniform float lut_contribution = 1.0;
uniform float vignette_intensity = 0.297;
uniform float vignette_smoothness = 0.2;
uniform vec2 vignette_center = vec2(0.5, 0.5);

// 标准 Unity 3D LUT 256x16: 16 格 x 16 行。格内=R 渐变(每格 16 px), 行=G 层, 格=B 层。
vec3 lut_sample(vec3 c) {
	vec3 v = clamp(c, vec3(0.0), vec3(1.0));
	float g_step = v.g * 15.0;
	float b_step = v.b * 15.0;
	ivec2 g_row = ivec2(int(floor(g_step + 0.5)));
	ivec2 b_col = ivec2(int(floor(b_step + 0.5)));
	vec2 uv = vec2(
		(float(b_col.x) * 16.0 + v.r * 15.0 + 0.5) / 256.0,
		(15.0 - float(g_row.x) + 0.5) / 16.0);
	return texture(lut, uv).rgb;
}

void fragment() {
	vec4 c = texture(screen_tex, SCREEN_UV);
	vec3 lut_out = lut_sample(c.rgb);
	c.rgb = mix(c.rgb, lut_out, lut_contribution);
	float d = distance(SCREEN_UV, vignette_center);
	float falloff = smoothstep(1.0, 1.0 - vignette_intensity - vignette_smoothness, d);
	c.rgb *= mix(1.0, falloff, vignette_intensity);
	COLOR = c;
}
'''


def win_safe(s):
    """Windows 文件名消毒: ':' 会被 NTFS 当 ADS 流 ('Combined Mesh (root: scene)' → 数据写进隐藏流=不可见)
    *?\"<>| 同样非法; '/'→'_' 防止目录穿越"""
    return re.sub(r'[\/:*?"<>|]', '_', s)[:80]


def res_to_fs(out, res):
    return os.path.join(out, res[len('res://'):].replace('/', os.sep))


def dedupe_file(final_p, tmp_p, arena):
    """同名资源内容去重: 内容相同→复用已有; 内容不同→落 <name>__<arena> 后缀
    (各变体贴图/网格同名异内容很常见: 'Combined Mesh (root: scene)'/'Flame03'/'Atlas' 等)"""
    import hashlib
    if not os.path.exists(final_p):
        os.replace(tmp_p, final_p)
        return final_p
    h1 = hashlib.md5(open(final_p, 'rb').read()).hexdigest()
    h2 = hashlib.md5(open(tmp_p, 'rb').read()).hexdigest()
    if h1 == h2:
        os.remove(tmp_p)
        return final_p
    d = os.path.dirname(final_p)
    stem, ext = os.path.splitext(os.path.basename(final_p))
    alt = os.path.join(d, '%s__%s%s' % (stem, arena, ext))
    if os.path.exists(alt):
        os.remove(alt)
    os.replace(tmp_p, alt)
    return alt


def make_white_tex(fp, wp):
    """烟材质的白版贴图: RGB→255 保留 alpha (原贴图 RGB≈0.2 灰 × 暗棕 albedo 双重乘≈黑不可见;
    原版做法=发光白烟由 albedo 定色)"""
    if os.path.exists(wp):
        return
    try:
        from PIL import Image
    except Exception:
        return
    try:
        img = Image.open(fp).convert('RGBA')
    except Exception:
        return
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            px[x, y] = (255, 255, 255, a)
    img.save(wp)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--arena', default='battlearenablacklegion')
    ap.add_argument('--out', default='d:/2/战场演示')
    ap.add_argument('--roots', default='',
                    help='只保留根名包含这些子串的 (逗号分隔); 留空=按子树含量自动识别 3D 根 (推荐)')
    ap.add_argument('--skip', default=('Scene Initializer,BattleManager,EnvironmentConditions,'
                                       'Battle Events,BattleHud,BattleTipController,Cinemachine,'
                                       'PlayerBoardArea,EnemyBoardArea,Particle colliders,'
                                       'Board Center,Friend Hand,Enemy Hand,TapParticleController,'
                                       'BattleManagerPositions,BattleErrors,NoCanvas2D,'
                                       'TouchInputManager,Battle Music,AudioMixer,Cache [,'
                                       'CardMaterialHelper,TutorialController,BattleCacheManager,'
                                       'Shadow Receiver,CardLowBoardLimit,TMP SubMesh,CardBack,'
                                       'Card Info,Textbackgrounds,ChooseCardMenuAnchor,'
                                       'MulliganAnchor,CemeteryGroup,EffectList,EffectAnchor,'
                                       'Energy Accumulation,HandArea,PlayerArea,EnemyAssetArea,'
                                       'MinionOrWarlord,Tactic Container,Bg,arrow1,TutorialArrows'),
                    help='跳过名字包含这些子串的整棵子树 (逗号分隔)')
    ap.add_argument('--all-roots', action='store_true', help='不过滤根')
    ap.add_argument('--light-energy', type=float, default=1.0,
                    help='方向光能量校准系数 (Unity intensity 1.0 直通在 Godot 过曝; 黑军团等效 ~0.2-0.25)')
    ap.add_argument('--ambient-energy', type=float, default=1.0,
                    help='环境光能量校准系数 (Trilight intensity 0.41 直通偏亮时的等效系数)')
    args = ap.parse_args()
    skips = [s.strip() for s in args.skip.split(',') if s.strip()]

    a = Assembler(args.arena, args.out)
    print('=== %s | GO %d, TF %d, PS %d, MAT %d' % (
        args.arena, len(a.GO), len(a.TF), len(a.PS), len(a.MAT)))
    roots = a.root_transforms()
    if args.all_roots:
        pass
    elif args.roots:
        roots = [t for t in roots if any(
            k in a.go(a.TF[t].get('m_GameObject', {}).get('m_PathID')).get('m_Name', '')
            for k in args.roots.split(','))]
    else:
        roots = a.auto_roots()
    print('根: %s' % sorted(a.go(a.TF[t].get('m_GameObject', {}).get('m_PathID')).get('m_Name', '?') for t in roots))

    # ---- 资源落地 ----
    mesh_paths, tex_paths = {}, {}
    white_paths = {}  # mi.tex_name → 白版烟贴图 res (RGB 白保留 alpha)

    def ensure_lut_shader():
        p = os.path.join(args.out, 'assets', 'lut_vignette.gdshader')
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if not os.path.exists(p) or open(p, encoding='utf-8').read() != LUT_SHADER:
            with open(p, 'w', encoding='utf-8') as f:
                f.write(LUT_SHADER)
        p2 = os.path.join(args.out, 'assets', 'uv_scroll.gdshader')
        if not os.path.exists(p2) or open(p2, encoding='utf-8').read() != UV_SCROLL_SHADER:
            with open(p2, 'w', encoding='utf-8') as f:
                f.write(UV_SCROLL_SHADER)

    ensure_lut_shader()

    def ensure_mesh(name, obj):
        safe = win_safe(name)
        p = os.path.join(args.out, 'assets', 'meshes', safe + '.obj')
        if not os.path.exists(p):
            raw = None
            try:
                raw = obj.export()
            except Exception:
                raw = None
            # UnityPy 版本差异: export() 可能返回 None 或抛 TypeError — 分开 try,
            # 保证 read().export() 回退总能执行 (踩坑 2026-08-22: 同一 try 内回退被 except 吞掉)
            if raw is None and not isinstance(obj, dict):
                try:
                    raw = obj.read().export()
                except Exception:
                    raw = None
            if raw:
                os.makedirs(os.path.dirname(p), exist_ok=True)
                tmp = p + '.tmp'
                with open(tmp, 'w', encoding='utf-8', errors='replace') as f:
                    f.write(raw)
                fix_obj_normals(tmp)
                p = dedupe_file(p, tmp, args.arena)
                imp = p + '.import'
                if os.path.exists(imp):
                    os.remove(imp)
            else:
                print('  [网格导出失败] %s' % name)
                return None
        elif not obj_valid(p):
            fix_obj_normals(p)
            imp = p + '.import'
            if os.path.exists(imp):
                os.remove(imp)
        res = 'res://assets/meshes/' + os.path.basename(p)
        mesh_paths[name] = res
        return res

    def ensure_tex(mi, which=1):
        tn, to = (mi.tex_name, mi.tex_obj) if which == 1 else (mi.tex_name2, mi.tex_obj2)
        if not tn:
            return None
        safe = win_safe(tn)
        p = os.path.join(args.out, 'assets', 'textures', safe + '.png')
        if not os.path.exists(p):
            os.makedirs(os.path.dirname(p), exist_ok=True)
            img = None
            try:
                img = getattr(to.read(), 'image', None)
            except Exception:
                img = None
            if img is not None:
                try:
                    img.save(p + '.tmp', format='PNG')  # PIL 按扩展名判格式, .tmp 需显式
                except Exception:
                    pass
            if not os.path.exists(p + '.tmp'):
                src = os.path.join(a.TEXDIR, tn + '.png')
                if os.path.exists(src):
                    import shutil
                    shutil.copy(src, p + '.tmp')
            if os.path.exists(p + '.tmp'):
                p = dedupe_file(p, p + '.tmp', args.arena)
            else:
                print('  [贴图导出失败] %s' % tn)
                return None
        res = 'res://assets/textures/' + os.path.basename(p)
        tex_paths[tn] = res
        return res

    # 收集用到的材质/粒子, 先落地贴图网格
    all_nodes = []

    def collect(tpid, parent_tpid=None):
        td = a.TF[tpid]
        gopid = td.get('m_GameObject', {}).get('m_PathID')
        g = a.go(gopid)
        nm = str(g.get('m_Name', 'GO%d' % gopid))
        # m_IsActive=0: 原版禁用 (如黑军团 CrosshairLine 3D/Cache Stealth) → 整树跳过
        if g.get('m_IsActive', 1) not in (1, True, None):
            return
        for sk in skips:
            if sk in nm:
                return
        kind = 'container'
        payload = None
        mesh_name, mesh_obj = a.mesh_of(gopid)
        if mesh_name:
            mats = a.mats_of(gopid)
            if not mats:
                kind = 'skip-mesh'  # 无材质 = 碰撞/逻辑网格
            else:
                kind = 'mesh'
                for mi in mats:
                    if mi.tex_name and mi.tex_name not in tex_paths:
                        ensure_tex(mi)
                    if mi.tex_name2 and mi.tex_name2 not in tex_paths:
                        ensure_tex(mi, 2)
                mesh_res = ensure_mesh(mesh_name, mesh_obj)
                if mesh_res is None:
                    return  # 导出失败 → 跳过该网格节点及子树
                payload = mesh_name
        elif a.has_ps(gopid):
            ps, render_mode, mref, mats = a.ps_of(gopid)
            if ps is not None:
                kind = 'particle'
                for mi in mats:
                    if mi.tex_name and mi.tex_name not in tex_paths:
                        ensure_tex(mi)
                        if mi.tex_name not in tex_paths:
                            print('  [粒子贴图缺失] %s' % mi.tex_name)
                    if mi.tex_name and mi.tex_name in tex_paths and smoke_lit(mi):
                        # 白版烟贴图 (RGB→白保留 alpha): 原贴图灰 0.2×暗棕 albedo≈黑不可见
                        fp = res_to_fs(args.out, tex_paths[mi.tex_name])
                        wp = os.path.join(os.path.dirname(fp), 'white_' + os.path.basename(fp))
                        make_white_tex(fp, wp)
                        if os.path.exists(wp):
                            white_paths[mi.tex_name] = 'res://assets/textures/' + os.path.basename(wp)
                payload = (ps, render_mode, mref, mats)
                # renderMode=4 (Mesh): 粒子用网格 draw pass (Light Shaft Plane1x1 等)
                if render_mode == 4 and mref and mref.get('m_PathID'):
                    mo = a.b.read_obj(mref, 'Mesh')
                    if mo is not None:
                        mn = a.b.obj_name(mo) or 'psmesh%d' % mref.get('m_PathID')
                        mesh_res = ensure_mesh(mn, mo)
                        if mesh_res is None:
                            return  # draw mesh 导出失败 → 跳过该粒子
                        payload = (ps, render_mode, (mn, mesh_res), mats)
                        print('  [粒子 draw mesh] %s' % mn)
        elif a.has_comp(gopid, a.CAM):
            kind = 'camera'
        elif a.has_comp(gopid, a.LIG):
            kind = 'light'
        all_nodes.append((kind, tpid, gopid, nm, payload, parent_tpid))
        for c in a.children_of(tpid):
            collect(c, tpid)

    for t in roots:
        collect(t)

    counts = {}
    for k, *_ in all_nodes:
        counts[k] = counts.get(k, 0) + 1
    print('节点统计:', counts, '| 网格 %d 贴图 %d' % (len(mesh_paths), len(tex_paths)))

    # ---- 生成 .gd ----
    out_gd = os.path.join(args.out, 'scenes', 'unity_arena_%s.gd' % args.arena)
    os.makedirs(os.path.dirname(out_gd), exist_ok=True)
    with open(out_gd, 'w', encoding='utf-8') as f:
        w = GdWriter(f)
        w.line('# 由 unity_scene_to_godot.py 自动生成 — 勿手改, 重跑脚本即可')
        w.line('# 来源: 解包整理/07_场景/%s (原版 Unity 序列化 JSON 说明书)' % args.arena)
        w.line('extends Node3D')
        w.line('')
        w.line('## 网格/贴图落地清单 (调试统计用)')
        w.line('const MESH_PATHS: Array[String] = [%s]' % ', '.join(
            repr(mesh_paths[k]) for k in sorted(mesh_paths)))
        w.line('const TEX_PATHS: Array[String] = [%s]' % ', '.join(
            repr(tex_paths[k]) for k in sorted(tex_paths)))
        w.line('')
        w.line('func _ready() -> void:')
        w.line('\t_build()')
        w.line('')
        w.line('func _build() -> void:')
        w.line('\tposition = Vector3(-100, 0, 0)  # 原版世界 x 基准 100 → 场景原点')
        w.line('')
        w.line('\t# Unity(左手系, 相机+X 朝屏幕右)→Godot(右手系): 内容整体做一次 X 镜像')
        w.line('\t# (绕相机 x=100 平面; 相机移出镜像根, 见下方 camera 分支), 否则画面左右互换')
        w.line('\tvar mirror := Node3D.new()')
        w.line("\tmirror.name = 'MirrorX'")
        w.line('\tmirror.position = Vector3(200.0, 0.0, 0.0)')
        w.line('\tmirror.scale = Vector3(-1.0, 1.0, 1.0)')
        w.line('\tself.add_child(mirror)')
        w.line('')

        mat_line_buf = []  # 材质创建行 (每网格内联)
        used_names = {}
        _mat_n = [0]

        def node_var(gopid):
            return 'n_%d' % gopid

        def parent_ref(pt):
            """父变换节点变量名 (根/父被跳过时挂镜像根 mirror; 相机单独挂 self, 见 camera 分支)"""
            if pt is None:
                return 'mirror'
            for k, tp2, gp2, nm2, py2, pp2 in all_nodes:
                if tp2 == pt:
                    if k == 'skip-mesh':
                        return 'mirror'
                    return node_var(gp2)
            return 'mirror'

        def world_chain(tpid):
            """沿 m_Father 链连乘局部 pos/quat (链上 scale 均为 1) → 场景根系世界变换"""
            chain = []
            cur = tpid
            while cur is not None and cur in a.TF:
                chain.append(a.local_trans(cur))
                cur = a.TF[cur].get('m_Father', {}).get('m_PathID')
            p = (0.0, 0.0, 0.0)
            q = (0.0, 0.0, 0.0, 1.0)
            for lt in reversed(chain):
                lp, lq = lt[0:3], lt[3]
                rp = q_rot_vec(q, lp)
                p = (p[0] + rp[0], p[1] + rp[1], p[2] + rp[2])
                q = q_mul(q, lq)
            return p, q

        def emit_local(tvar, tpid):
            lt = a.local_trans(tpid)
            pos, q, sc = (lt[0], lt[1], lt[2]), lt[3], lt[4]
            w.line('\t%s.position = Vector3(%.4f, %.4f, %.4f)' % (tvar, pos[0], pos[1], pos[2]))
            w.line('\t%s.quaternion = Quaternion(%.6f, %.6f, %.6f, %.6f)' % (tvar, q[0], q[1], q[2], q[3]))
            w.line('\t%s.scale = Vector3(%.6f, %.6f, %.6f)' % (tvar, sc[0], sc[1], sc[2]))

        def emit_mat(mi, mv):
            """材质创建行列表 (mv=材质变量名), 无贴图返回 None"""
            if mi.tex_name2 and mi.tex_name2 in tex_paths:
                # 双贴图 (Runes "Unlit UV scroll"): shader 双层 + TIME 滚动 (Vector4_1=(1,1,0.02,0))
                lines = ['var %s := ShaderMaterial.new()' % mv]
                lines.append('%s.shader = load("res://assets/uv_scroll.gdshader")' % mv)
                lines.append('%s.set_shader_parameter("main_tex", load(%r))' % (mv, tex_paths[mi.tex_name]))
                lines.append('%s.set_shader_parameter("secondary_tex", load(%r))' % (mv, tex_paths[mi.tex_name2]))
                v4 = mi.vector4_1 or {}
                sc = (float(v4.get('r', 1.0) or 1.0), float(v4.get('g', 1.0) or 1.0),
                      float(v4.get('b', 0.0) or 0.0), float(v4.get('a', 0.0) or 0.0))
                lines.append('%s.set_shader_parameter("uv_scroll", Vector4(%.3f, %.3f, %.3f, %.3f))' % (mv, *sc))
                lines.append('%s.set_shader_parameter("layers_blend_opacity", 1.00)' % mv)
                if mi.cull == 0:
                    lines.append('%s.cull_mode = BaseMaterial3D.CULL_DISABLED' % mv)
                return lines
            if not (mi.tex_name and mi.tex_name in tex_paths):
                return None
            lines = ['var %s := StandardMaterial3D.new()' % mv]
            lines.append('%s.albedo_texture = load(%r)' % (mv, tex_paths[mi.tex_name]))
            if mi.base_color:
                lines.append('%s.albedo_color = ' % mv + col_str(mi.base_color))
            if mi.is_transparent():
                lines.append('%s.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA' % mv)
                if mi.zwrite <= 0:
                    lines.append('%s.depth_draw_mode = BaseMaterial3D.DEPTH_DRAW_DISABLED' % mv)
            if mi.blend >= 2:
                lines.append('%s.blend_mode = BaseMaterial3D.BLEND_MODE_ADD' % mv)
            if mi.cull == 0:
                lines.append('%s.cull_mode = BaseMaterial3D.CULL_DISABLED' % mv)
            elif mi.cull == 1:
                lines.append('%s.cull_mode = BaseMaterial3D.CULL_FRONT' % mv)
            if mi.emission_color:
                lines.append('%s.emission_enabled = true' % mv)
                lines.append('%s.emission_energy_multiplier = %.3f' % (mv, mi.emission_energy()))
            lines.append('%s.roughness = 0.9' % mv)
            return lines

        bg_color = None  # 3D 相机 (BoardCamera) 的 m_BackGroundColor, 供环境背景用
        for kind, tpid, gopid, nm, payload, parent_tpid in all_nodes:
            nv = node_var(gopid)
            cam_added = False
            if kind == 'skip-mesh':
                continue
            if kind == 'mesh':
                mats = a.mats_of(gopid)
                mi = mats[0] if mats else None
                _mat_n[0] += 1
                mv = 'm_%d' % _mat_n[0]
                ml = emit_mat(mi, mv) if mi is not None else None
                if ml is None:
                    w.line('\t# 跳过不可见网格: %s' % nm)
                    continue
                w.line('\tvar %s := MeshInstance3D.new()' % nv)
                w.line('\t%s.name = %r' % (nv, nm))
                w.line('\t%s.mesh = load(%r)' % (nv, mesh_paths[payload]))
                for l in ml:
                    w.line('\t' + l)
                # SkinnedMeshRenderer 薄片 (黑军团 Chain 链平面): 镜像 scale.x=-1 + yaw180 背面朝相机,
                # cull_back 会被剔除 (原版单面可见) → SMR 网格强制双面
                if a.has_smr(gopid):
                    w.line('\t%s.cull_mode = BaseMaterial3D.CULL_DISABLED' % mv)
                w.line('\t%s.material_override = %s' % (nv, mv))
                emit_local(nv, tpid)
                w.line('\t%s.add_child(%s)' % (parent_ref(parent_tpid), nv))
                w.line('')
                continue
            elif kind == 'particle':
                emit_particle_gd(w, a, nv, tpid, nm, payload, tex_paths, parent_ref(parent_tpid), white_paths)
                continue
            elif kind == 'camera':
                cd = next(a.CAM[c] for c in a.go_comps[gopid] if c in a.CAM)
                if not cd.get('m_Enabled', 1):
                    print('  [跳过禁用相机] %s' % nm)
                    continue  # reflection camera (原版 enabled=0) 不生成 — 否则先入树成 current 抢渲染
                w.line('\tvar %s := Camera3D.new()' % nv)
                w.line('\t%s.name = %r' % (nv, nm))
                cd = next(a.CAM[c] for c in a.go_comps[gopid] if c in a.CAM)
                # 相机必须移出镜像根 (mirror 是反射, 相机带反射基 = 画面再次镜像);
                # 位置 = 镜像世界坐标 (100 - p_u.x), 旋转 = conjX(q_u) ⊗ Y180
                # (推导: R_g = M·R_u·D, M=reflect_x, D=RotX(180°) 手性修正)
                wp, wq = world_chain(tpid)
                w.line('\t%s.position = Vector3(%.4f, %.4f, %.4f)' % (nv, 200.0 - wp[0], wp[1], wp[2]))
                # conjX(q) = (x, -y, -z, w)  (M·R·M 反射共轭)
                qq = q_mul((wq[0], -wq[1], -wq[2], wq[3]), (0.0, 1.0, 0.0, 0.0))
                w.line('\t%s.quaternion = Quaternion(%.6f, %.6f, %.6f, %.6f)' % (nv, qq[0], qq[1], qq[2], qq[3]))
                w.line('\t%s.scale = Vector3(%.6f, %.6f, %.6f)' % (nv, 1.0, 1.0, 1.0))
                fov = cd.get('field of view')
                if fov:
                    w.line('\t%s.fov = %.3f' % (nv, float(fov)))
                w.line('\t%s.near = %.4f' % (nv, float(cd.get('near clip plane', 0.3))))
                w.line('\t%s.far = %.4f' % (nv, float(cd.get('far clip plane', 300.0))))
                # CinemachineVirtualCamera m_Lens.LensShift.y=-0.205 → Godot frustum_offset
                if cd.get('m_LensShift', {}).get('y'):
                    w.line('\t%s.frustum_offset = Vector2(0, %.4f)' % (nv, float(cd.get('m_LensShift').get('y')) * 0.86))
                if bg_color is None and 'UI' not in nm:
                    bc = cd.get('m_BackGroundColor') or {}
                    bg_color = (float(bc.get('r', 0.0288)), float(bc.get('g', 0.0288)), float(bc.get('b', 0.0294)))
                w.line('\tself.add_child(%s)  # 相机挂在镜像根之外' % nv)
                w.line('')
                cam_added = True
            elif kind == 'light':
                w.line('\tvar %s := DirectionalLight3D.new()' % nv)
                w.line('\t%s.name = %r' % (nv, nm))
                ld = next(a.LIG[c] for c in a.go_comps[gopid] if c in a.LIG)
                lt = a.local_trans(tpid)
                pos, q, sc = (lt[0], lt[1], lt[2]), lt[3], lt[4]
                w.line('\t%s.position = Vector3(%.4f, %.4f, %.4f)' % (nv, pos[0], pos[1], pos[2]))
                # Unity 定向灯旋转 R 时照亮方向 = R·(0,-1,0) (默认垂直向下);
                # Godot 灯照亮 = B·(0,0,-1) → B = R ⊗ RotX(-90)
                qq = q_mul(q, (-0.70710678, 0.0, 0.0, 0.70710678))
                w.line('\t%s.quaternion = Quaternion(%.6f, %.6f, %.6f, %.6f)' % (nv, qq[0], qq[1], qq[2], qq[3]))
                # 按说明书: Light m_Color(1,1,1) 白光 + m_Intensity 1.0 直通 (此前暖色修正的依据
                # "原版白光→含 LUT 暖调" 已被推翻: ColorLookup=LUT Normal identity → 无暖调, 颜色零自造)
                lc = ld.get('m_Color', {}) or {}
                w.line('\t%s.light_color = Color(%.4f, %.4f, %.4f)' % (nv,
                    float(lc.get('r', 1.0) or 1.0),
                    float(lc.get('g', 1.0) or 1.0),
                    float(lc.get('b', 1.0) or 1.0)))
                # (黑军团验算: Unity 光强直通=过曝 2-3 倍, energy 作引擎物理等效校准, 颜色保持说明书值)
                w.line('\t%s.light_energy = %.3f' % (nv, float(ld.get('m_Intensity', 1.0) or 1.0) * args.light_energy))
                sh = ld.get('m_Shadows', {})
                if sh.get('m_Type', 0) != 0 and ld.get('m_Type') == 1:
                    w.line('\t%s.shadow_enabled = true' % nv)
            else:  # container
                w.line('\tvar %s := Node3D.new()' % nv)
                w.line('\t%s.name = %r' % (nv, nm))
                emit_local(nv, tpid)
                w.line('\t%s.add_child(%s)' % (parent_ref(parent_tpid), nv))
                w.line('')
                continue
            if cam_added:
                continue
            w.line('\t%s.add_child(%s)' % (parent_ref(parent_tpid), nv))
            w.line('')

        # 环境 (按说明书 RenderSettings: m_AmbientMode=3 Trilight 三色 + m_AmbientIntensity 原值;
        # URP Volume 无 Tonemapping 组件 → Linear 直出; Bloom(1.15/5.0) + Vignette(0.297/0.2) + ColorLookup(LUT))
        for r in a.REN.values():
            w.line('\tvar env := WorldEnvironment.new()')
            w.line('\tvar e := Environment.new()')
            # 环境间接光 = RenderSettings m_AmbientProbe SH DC 项 (sh[0..2]=平均间接光 RGB;
            # 黑军团 (0.289,0.183,-0.080) 暖橙! Trilight 三色仅天空盒配置, 单色平均会偏蓝 —
            # 说明书完整读取: 环境光按 SH probe, 不是 Trilight 平均)。B<0 夹 0。
            sk, eq, gd = (r.get('m_AmbientSkyColor') or {}), (r.get('m_AmbientEquatorColor') or {}), (r.get('m_AmbientGroundColor') or {})
            probe = r.get('m_AmbientProbe') or {}
            def _sh(i):
                v = probe.get('sh[ %d]' % i) or probe.get('sh[%d]' % i)
                return float(v) if v is not None else 1.0
            sh_c = (_sh(0), _sh(1), _sh(2))
            w.line('\te.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR')
            w.line('\te.ambient_light_color = Color(%.4f, %.4f, %.4f, 1.0000)' %
                   tuple(max(0.0, c) for c in sh_c))
            # SH DC 已含强度 → energy 直通; --ambient-energy 做引擎等效校准
            w.line('\te.ambient_light_energy = %.3f' % args.ambient_energy)
            if r.get('m_Fog'):
                w.line('\te.fog_enabled = true')
                w.line('\te.fog_light_color = ' + col_str(r.get('m_FogColor', {})))
                w.line('\te.fog_density = %.5f' % float(r.get('m_FogDensity', 0.01)))
            # URP: Volume 无 Tonemapping 组件 → m_RenderPostProcessing 直出 = Linear (勿用 Filmic/ACES)
            w.line('\te.tonemap_mode = Environment.TONE_MAPPER_LINEAR')
            w.line('\te.glow_enabled = true')
            w.line('\te.glow_intensity = 5.0')
            w.line('\te.glow_hdr_threshold = 1.15')
            # URP Bloom skipIterations 6+maxIterations 6 ≈ 大扩散层; Godot 4.7 glow_levels/N 层强度
            # (默认 L2/L3 近距叠加会泛白) → 只开最糊两层 L6+L7 (大范围柔光, 发光源内核仍亮)
            w.line('\te.set("glow_levels/6", 1.0)')
            w.line('\te.set("glow_levels/7", 1.0)')
            w.line('\te.set("glow_levels/1", 0.0)')
            w.line('\te.set("glow_levels/2", 0.0)')
            w.line('\te.set("glow_levels/3", 0.0)')
            w.line('\te.set("glow_levels/4", 0.0)')
            w.line('\te.set("glow_levels/5", 0.0)')
            w.line('\te.background_mode = Environment.BG_COLOR')
            bg = bg_color or (0.0288, 0.0288, 0.0294)
            w.line('\te.background_color = Color(%.4f, %.4f, %.4f, 1)' % bg)
            w.line('\tenv.environment = e')
            w.line('\tenv.name = "Env"')
            w.line('\tadd_child(env)')
            # 原版 Battle Arena 4 PostProcessing: ColorLookup(场景引用 LUT, contribution 1.0) + Vignette(0.297)
            # layer=-1: LUT 只作用于 3D 画面, 不遮 HUD (主项目 HUD 在默认 canvas layer 0 之上)
            w.line('\tvar pp := CanvasLayer.new()')
            w.line('\tpp.layer = -1')
            w.line('\tvar cr := ColorRect.new()')
            w.line('\tcr.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)')
            w.line('\tcr.mouse_filter = Control.MOUSE_FILTER_IGNORE')
            w.line('\tvar pm := ShaderMaterial.new()')
            w.line('\tpm.shader = load("res://assets/lut_vignette.gdshader")')
            lut_res = None
            lref = a.lut_ref_val
            if lref:
                try:
                    lobj = a.b.read_obj(lref, 'Texture2D')
                    if lobj is not None:
                        limg = getattr(lobj.read(), 'image', None)
                        if limg is not None:
                            ln = a.b.obj_name(lobj) or 'lut_%s' % lref.get('m_PathID')
                            lp = os.path.join(args.out, 'assets', 'textures', win_safe(ln) + '.png')
                            if not os.path.exists(lp):
                                os.makedirs(os.path.dirname(lp), exist_ok=True)
                                limg.save(lp + '.tmp', format='PNG')
                                lp = dedupe_file(lp, lp + '.tmp', args.arena)
                            lut_res = 'res://assets/textures/' + os.path.basename(lp)
                except Exception:
                    lut_res = None
            if lut_res is None and os.path.exists(os.path.join(args.out, 'assets', 'textures', 'LUT Normal.png')):
                lut_res = 'res://assets/textures/LUT Normal.png'  # 回退: LUT Blender 共享默认(黑军团)
            if lut_res:
                w.line('\tpm.set_shader_parameter("lut", load(%r))' % lut_res)
                w.line('\tpm.set_shader_parameter("lut_contribution", 1.0)')
            w.line('\tpm.set_shader_parameter("vignette_intensity", 0.297)')
            w.line('\tpm.set_shader_parameter("vignette_smoothness", 0.2)')
            w.line('\tcr.material = pm')
            w.line('\tpp.add_child(cr)')
            w.line('\tadd_child(pp)')
            break

    # 包装 tscn (挂脚本)
    out_tscn = os.path.join(args.out, 'scenes', 'unity_arena_%s.tscn' % args.arena)
    with open(out_tscn, 'w', encoding='utf-8') as f:
        f.write('[gd_scene load_steps=2 format=3]\n\n')
        f.write('[ext_resource type="Script" path="res://scenes/unity_arena_%s.gd" id="1"]\n\n' % args.arena)
        f.write('[node name="Arena" type="Node3D"]\n')
        f.write('script = ExtResource("1")\n')

    print('✓ 输出:', out_gd)
    return 0


COLOR_LIT_TINT = 'Color(0.0380, 0.0090, 0.0060, 1.0000)'  # 烟底标定色 ≈ 参考图 (55,25,20)


def smoke_lit(mi):
    """烟/蒸汽类: alpha混合 且 材质名含 smoke|steam|wispy (排除 add/glow/ember/fire 发光类)"""
    if mi is None or mi.blend >= 2:
        return False
    n = mi.name or ''
    return bool(re.search(r'(?i)smoke|steam|wispy', n)) and not re.search(r'(?i)additive|glow|ember|fire', n)


def emit_particle_gd(w, a, nv, tpid, nm, payload, tex_paths, parent_expr='self', white_paths=None):
    ps, render_mode, mref, mats = payload
    white_paths = white_paths or {}
    mi = mats[0] if mats else None
    im = ps.get('InitialModule', {}) or {}
    em = ps.get('EmissionModule', {}) or {}
    shp = ps.get('ShapeModule', {}) or {}
    sm = ps.get('SizeModule', {}) or {}
    cm = ps.get('ColorModule', {}) or {}
    vm = ps.get('VelocityModule', {}) or {}
    rm = ps.get('RotationModule', {}) or {}
    # UVModule 翻页分片 (Black Smoke 8x8/Floor Grill 6x5/FirePit 7x7/Smoke 6x5 等)
    uvm = ps.get('UVModule', {}) or {}
    uv_en = bool(uvm.get('enabled'))
    tiles_x = int(uvm.get('tilesX', 1) or 1)
    tiles_y = int(uvm.get('tilesY', 1) or 1)
    uv_fps = float(uvm.get('fps', 30.0) or 30.0)
    # Godot GPUParticles3D 无 rate 属性: 池大小 = 平均存活粒子数 = rate × lifetime
    # (Unity maxNumParticles 是上限, 直接用作池会全池同时存活 → 粒子爆炸)
    rate_over_time = float(
        (em.get('rateOverTime', {}) or {}).get('scalar', 0.0) if isinstance(em.get('rateOverTime', {}), dict) else 0.0)
    _life_min, _life_max = curve_min_max(im.get('startLifetime', {}), 1.0)
    _pool = int(rate_over_time * max(_life_min, _life_max))
    if _pool > 0:
        amount = max(1, min(_pool, 800))
        _burst_only = False
    else:
        # rate=0 的 burst 类: 用爆发总量, 上限 200 (Skull Eyes 等一次性粒子)
        _burst_total = 0
        for b in (em.get('m_Bursts', []) or []):
            if isinstance(b, dict):
                _burst_total += int(curve_scalar(b.get('countCurve', {}), 10) or 10)
        if _burst_total <= 0:
            return  # rate=0 且无 burst: 原版不发粒子 (无需生成)
        amount = max(1, min(_burst_total, 200))
        _burst_only = True
    life_min, life_max = curve_min_max(im.get('startLifetime', {}), 1.0)
    lifetime = max(life_min, life_max)
    speed_min, speed_max = curve_min_max(im.get('startSpeed', {}), 0.0)
    size_min, size_max = curve_min_max(im.get('startSize', {}), 1.0)
    size_keys = curve_keys(sm.get('curve', {})) if sm.get('enabled') else []
    color_keys = grad_keys(cm.get('gradient', {})) if cm.get('enabled') else []
    sc0 = im.get('startColor', {}) or {}
    cmin, cmax = sc0.get('minColor') or {}, sc0.get('maxColor') or {}
    stype = shp.get('type', 0)
    radius = curve_scalar(shp.get('radius', {}), 1.0)
    radius_th = float(shp.get('radiusThickness', 1.0) or 1.0)
    sangle = float(shp.get('angle', 0) or 0.0)

    w.line('\tvar %s := GPUParticles3D.new()' % nv)
    w.line('\t%s.name = %r' % (nv, nm))
    lt = a.local_trans(tpid)
    pos, q, sc = (lt[0], lt[1], lt[2]), lt[3], lt[4]
    w.line('\t%s.position = Vector3(%.4f, %.4f, %.4f)' % (nv, pos[0], pos[1], pos[2]))
    w.line('\t%s.quaternion = Quaternion(%.6f, %.6f, %.6f, %.6f)' % (nv, q[0], q[1], q[2], q[3]))
    w.line('\t%s.scale = Vector3(%.6f, %.6f, %.6f)' % (nv, sc[0], sc[1], sc[2]))
    w.line('\t%s.amount = %d' % (nv, max(amount, 1)))
    w.line('\t%s.lifetime = %.3f' % (nv, max(lifetime, 0.01)))
    # burst 类 (rate=0+bursts): 原版 cycleCount 一次性 → one_shot (Skull Eyes 闪一次)
    w.line('\t%s.one_shot = %s' % (nv, 'true' if (_burst_only or not ps.get('looping', True)) else 'false'))
    w.line('\t%s.emitting = %s' % (nv, 'true' if ps.get('playOnAwake', True) else 'false'))
    # simulationSpeed 直通 (光柱 0.3/毒气 0.4/烟 0.75/气体 1.5 — 此前丢失全按 1.0)
    w.line('\t%s.speed_scale = %.3f' % (nv, float(ps.get('simulationSpeed', 1.0) or 1.0)))
    if ps.get('prewarm', False):
        w.line('\t%s.preprocess = %.2f' % (nv, float(ps.get('lengthInSec', 5.0) or 5.0) *
                                           float(ps.get('simulationSpeed', 1.0) or 1.0)))
    else:
        w.line('\t%s.preprocess = 0.0' % nv)
    pmv = w.next_id('pm')
    w.line('\tvar %s := ParticleProcessMaterial.new()' % pmv)
    # Unity ShapeType: 0 Sphere/1 SphereShell/2 Hemisphere/3 HemisphereShell/4 Cone/5 Box/6 Mesh/
    # 7 Circle/8 CircleEdge/9 SingleSidedEdge/10 MeshRenderer/11 SkinnedMeshRenderer(均按 Box 近似)/
    # 12 BoxShell/13 BoxEdge/14 Donut/15 Rectangle/18 Cylinder(按 Box 近似)
    # Godot 4.7 无 CONE 枚举: 锥形发射源用小球面近似 (粒子沿 direction 喷出, 视觉一致)
    if stype in (2, 3):
        w.line('\t%s.emission_shape = ParticleProcessMaterial.EMISSION_SHAPE_SPHERE_SURFACE' % pmv)
        w.line('\t%s.emission_sphere_radius = %.4f' % (pmv, radius))
    elif stype == 4:
        w.line('\t%s.emission_shape = ParticleProcessMaterial.EMISSION_SHAPE_SPHERE' % pmv)
        w.line('\t%s.emission_sphere_radius = %.4f' % (pmv, min(radius, 0.35)))
    elif stype == 7:
        w.line('\t%s.emission_shape = ParticleProcessMaterial.EMISSION_SHAPE_RING' % pmv)
        w.line('\t%s.emission_ring_radius = %.4f' % (pmv, radius))
        w.line('\t%s.emission_ring_inner_radius = %.4f' % (pmv, radius * max(0.0, 1.0 - radius_th)))
    elif stype in (5, 6, 10, 11, 12, 13, 15, 18):
        w.line('\t%s.emission_shape = ParticleProcessMaterial.EMISSION_SHAPE_BOX' % pmv)
        scn = shp.get('m_Scale', {}) or shp.get('scale', {}) or {}

        def scv(k, d=1.0):
            v = scn.get(k, {})
            if isinstance(v, dict):
                return curve_scalar(v, d)
            return float(v if v is not None else d)

        ex, ey, ez = scv('x') / 2.0, scv('y') / 2.0, scv('z') / 2.0
        if abs(ex) < 1e-6 and abs(ey) < 1e-6 and abs(ez) < 1e-6:
            ex = ey = ez = max(radius, 0.5) / 2.0  # scale 全 0 时退化为半径球盒
        w.line('\t%s.emission_box_extents = Vector3(%.4f, %.4f, %.4f)' % (pmv, ex, ey, ez))
    else:
        w.line('\t%s.emission_shape = ParticleProcessMaterial.EMISSION_SHAPE_SPHERE' % pmv)
        w.line('\t%s.emission_sphere_radius = %.4f' % (pmv, radius))
    if speed_max > 0:
        w.line('\t%s.initial_velocity_min = %.3f' % (pmv, speed_min))
        w.line('\t%s.initial_velocity_max = %.3f' % (pmv, speed_max))
    if vm.get('enabled'):
        def vof(x):
            if isinstance(x, dict):
                mc = x.get('minMaxCurve', x)
                return curve_scalar(mc, 0.0) if isinstance(mc, dict) else 0.0
            return 0.0
        vx_, vy_, vz_ = vof(vm.get('x')), vof(vm.get('y')), vof(vm.get('z'))
        # Unity velocity-over-lifetime 恒速 (world) → Godot: direction=归一化方向 +
        # initial_velocity=速率 (仅 direction 无初速 → 粒子钉死不动, 原版热浪/绿气恒漂)
        vlen = math.sqrt(vx_ * vx_ + vy_ * vy_ + vz_ * vz_)
        if vlen > 0.001:
            w.line('\t%s.direction = Vector3(%.4f, %.4f, %.4f)' % (pmv, vx_ / vlen, vy_ / vlen, vz_ / vlen))
            w.line('\t%s.initial_velocity_min = %.3f' % (pmv, vlen))
            w.line('\t%s.initial_velocity_max = %.3f' % (pmv, vlen))
    else:
        w.line('\t%s.direction = Vector3(0, 1, 0)' % pmv)
    g = curve_scalar(im.get('gravityModifier', {}), 0.0)
    w.line('\t%s.gravity = Vector3(0, %.3f, 0)' % (pmv, -9.81 * g))
    if uv_en and tiles_x > 1 and tiles_y > 1:
        w.line('\t%s.anim_speed = Vector2(%.1f, %.1f)' % (pmv, uv_fps, uv_fps))
    # Godot 粒子 scale 直接乘 draw-pass 尺寸: quad.size=1, scale=Unity 直径 (startSize)
    w.line('\t%s.scale_min = %.4f' % (pmv, size_min))
    w.line('\t%s.scale_max = %.4f' % (pmv, size_max))
    if size_keys and len(size_keys) >= 2 and abs(size_keys[0][1] - size_keys[-1][1]) > 0.01:
        cv_ = w.next_id('cv')
        w.line('\tvar %s := Curve.new()' % cv_)
        for t, v in size_keys:
            w.line('\t%s.add_point(Vector2(%.4f, %.4f))' % (cv_, t, v))
        ct_ = w.next_id('ct')
        w.line('\tvar %s := CurveTexture.new()' % ct_)
        w.line('\t%s.curve = %s' % (ct_, cv_))
        w.line('\t%s.scale_curve = %s' % (pmv, ct_))
    # startColor 是全局乘子, 与 colorOverLifetime 相乘 (原版两者都生效)
    sc_mode = sc0.get('minMaxState', 0)
    if sc_mode == 2 and cmin and cmax:
        smc = {k: (cmin.get(k, 0.0) + cmax.get(k, 0.0)) / 2.0 for k in ('r', 'g', 'b', 'a')}
        w.line('\t%s.color = %s' % (pmv, col_str(smc)))
    elif cmax:
        w.line('\t%s.color = %s' % (pmv, col_str((cmax if sc_mode in (0, 2) else cmin) or cmax)))
    if color_keys:
        gr_ = w.next_id('gr')
        gt_ = w.next_id('gt')
        w.line('\tvar %s := Gradient.new()' % gr_)
        w.line('\t%s.offsets = PackedFloat32Array([%s])' % (gr_, ', '.join('%.4f' % t for t, _ in color_keys)))
        w.line('\t%s.colors = PackedColorArray([%s])' % (gr_, ', '.join(
            'Color(%.4f, %.4f, %.4f, %.4f)' % c for _, c in color_keys)))
        w.line('\tvar %s := GradientTexture1D.new()' % gt_)
        w.line('\t%s.gradient = %s' % (gt_, gr_))
        w.line('\t%s.color_ramp = %s' % (pmv, gt_))
    if rm.get('enabled'):
        rz = rm.get('z', {})
        rv = None
        if isinstance(rz, dict):
            mc = rz.get('minMaxCurve', rz)
            rv = curve_scalar(mc, 0.0) if isinstance(mc, dict) else None
        if rv:
            w.line('\t%s.angular_velocity_min = %.2f' % (pmv, math.degrees(rv)))
            w.line('\t%s.angular_velocity_max = %.2f' % (pmv, math.degrees(rv)))
    w.line('\t%s.process_material = %s' % (nv, pmv))
    # draw pass: renderMode=4 (Mesh) 用导出的网格, 否则 quad (边长=1, scale=直径)
    mat_name = str(mi.name) if mi else ''
    if render_mode == 4 and isinstance(mref, tuple):
        mesh_res = mref[1]
        mmv = w.next_id('pm2')
        w.line('\tvar %s := StandardMaterial3D.new()' % mmv)
        w.line('\t%s.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED' % mmv)
        w.line('\t%s.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA' % mmv)
        w.line('\t%s.cull_mode = BaseMaterial3D.CULL_DISABLED' % mmv)
        w.line('\t%s.vertex_color_use_as_albedo = true' % mmv)
        if mi and mi.blend >= 2:
            w.line('\t%s.blend_mode = BaseMaterial3D.BLEND_MODE_ADD' % mmv)
        if mi and mi.tex_name and mi.tex_name in tex_paths:
            w.line('\t%s.albedo_texture = load(%r)' % (mmv, tex_paths[mi.tex_name]))
        if mi and (mi.base_color or mi.mat_color):
            w.line('\t%s.albedo_color = %s' % (mmv, col_str(mi.base_color or mi.mat_color)))
        qdv = w.next_id('qd')
        w.line('\tvar %s := load(%r).duplicate()' % (qdv, mesh_res))
        w.line('\t%s.draw_pass_1 = %s' % (nv, qdv))
        w.line('\t%s.draw_pass_1.surface_set_material(0, %s)' % (nv, mmv))
    else:
        qmv = w.next_id('q')
        w.line('\tvar %s := QuadMesh.new()' % qmv)
        w.line('\t%s.size = Vector2(1.000, 1.000)' % qmv)
        if mi is not None:
            mmv = w.next_id('pm2')
            w.line('\tvar %s := StandardMaterial3D.new()' % mmv)
            w.line('\t%s.billboard_mode = BaseMaterial3D.BILLBOARD_PARTICLES' % mmv)
            # 粒子顶点色(color × color_ramp) 必须显式启用, 否则粒子色/渐变全部不生效
            w.line('\t%s.vertex_color_use_as_albedo = true' % mmv)
            # 烟/蒸汽类材质按原版被环境光染暗棕 (参考图实测 ~55,25,20), 用 unshaded+暗色近似
            if 'Heat Distortion' in mat_name:
                # 原版=屏幕空间折射材质 (Godot StandardMaterial 无法还原) → 用 mask 贴图低透明度近似, 防白块
                if 'Glow' in tex_paths:
                    w.line('\t%s.albedo_texture = load(%r)' % (mmv, tex_paths['Glow']))
                w.line('\t%s.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA' % mmv)
                w.line('\t%s.albedo_color = Color(1.0, 0.85, 0.7, 0.16)' % mmv)
                w.line('\t%s.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED' % mmv)
                w.line('\t%s.cull_mode = BaseMaterial3D.CULL_DISABLED' % mmv)
                w.line('\t%s.blend_mode = BaseMaterial3D.BLEND_MODE_ADD' % mmv)
            else:
                use_lit = smoke_lit(mi)
                # 说明书: 烟/气粒子材质为 Unlit 粒子着色器, 颜色=startColor×colorMod×贴图RGB(0.2灰)
                # → unshaded + 原版贴图 + albedo 白 (受光会洗色; 暗棕 albedo 会双重乘黑)
                if mi.tex_name and mi.tex_name in tex_paths:
                    w.line('\t%s.albedo_texture = load(%r)' % (mmv, tex_paths[mi.tex_name]))
                w.line('\t%s.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED' % mmv)
                w.line('\t%s.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA' % mmv)
                w.line('\t%s.cull_mode = BaseMaterial3D.CULL_DISABLED' % mmv)
                if mi.blend >= 2:
                    w.line('\t%s.blend_mode = BaseMaterial3D.BLEND_MODE_ADD' % mmv)
                if mi.base_color or mi.mat_color:
                    w.line('\t%s.albedo_color = %s' % (mmv, col_str(mi.base_color or mi.mat_color)))
            # UVModule 翻页分片: 材质分帧 + loop (anim_speed 已在 pmv 设置)
            if uv_en and tiles_x > 1 and tiles_y > 1:
                w.line('\t%s.particles_anim_h_frames = %d' % (mmv, tiles_x))
                w.line('\t%s.particles_anim_v_frames = %d' % (mmv, tiles_y))
                w.line('\t%s.particles_anim_loop = true' % mmv)
            w.line('\t%s.material = %s' % (qmv, mmv))
        w.line('\t%s.draw_pass_1 = %s' % (nv, qmv))
    w.line('\t%s.add_child(%s)' % (parent_expr, nv))
    w.line('')


def flip_obj_vt(fp):
    """Unity OBJ 导出的 vt v 轴是自下而上, Godot 纹理 v=0 在顶部 → 写 1-v"""
    lines = open(fp, encoding='utf-8', errors='replace').readlines()
    out = []
    n = 0
    for l in lines:
        if l.startswith('vt '):
            p = l.split()
            try:
                p[2] = '%.6f' % (1.0 - float(p[2]))
                out.append(' '.join(p) + '\\n')
                n += 1
            except Exception:
                out.append(l)
        else:
            out.append(l)
    if n:
        open(fp, 'w', encoding='utf-8').write(''.join(out))
    return n


def obj_valid(fp):
    try:
        with open(fp, encoding='utf-8', errors='replace') as f:
            head = f.read(1 << 20)
    except Exception:
        return False
    return ('\nv ' in head or head.startswith('v ')) and '\nvn ' in head and '\nvt ' in head


def fix_obj_normals(fp):
    """OBJ 缺 vn/vt 的会被导入器判 invalid → 补法线并重写索引"""
    with open(fp, encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    has_vn = any(l.startswith('vn ') for l in lines)
    has_vt = any(l.startswith('vt ') for l in lines)
    if has_vn and has_vt:
        return
    vs, vts, faces = [], [], []
    for l in lines:
        p = l.strip().split()
        if not p:
            continue
        if p[0] == 'v':
            vs.append((float(p[1]), float(p[2]), float(p[3])))
        elif p[0] == 'vt':
            vts.append((float(p[1]), float(p[2])))
        elif p[0] == 'f':
            faces.append(l)
    if not vs:
        return
    vns = [(0.0, 0.0, 0.0)] * len(vs)
    for l in faces:
        idx = []
        for tok in l.strip().split()[1:]:
            try:
                idx.append(int(tok.split('/')[0]))
            except Exception:
                idx = []
                break
        if len(idx) < 3:
            continue
        a0, b0, c0 = vs[(idx[0] - 1) % len(vs)], vs[(idx[1] - 1) % len(vs)], vs[(idx[2] - 1) % len(vs)]
        ux, uy, uz = b0[0] - a0[0], b0[1] - a0[1], b0[2] - a0[2]
        vx, vy, vz = c0[0] - a0[0], c0[1] - a0[1], c0[2] - a0[2]
        n = (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)
        ln = math.sqrt(n[0] ** 2 + n[1] ** 2 + n[2] ** 2) or 1.0
        for i in idx:
            vi = (i - 1) % len(vns)
            vns[vi] = (vns[vi][0] + n[0] / ln, vns[vi][1] + n[1] / ln, vns[vi][2] + n[2] / ln)
    for i, v in enumerate(vns):
        ln = math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
        vns[i] = (v[0] / ln, v[1] / ln, v[2] / ln) if ln > 1e-6 else (0.0, 0.0, 1.0)
    out = ['# regenerated by unity_scene_to_godot (missing normals)\n']
    for v in vs:
        out.append('v %.6f %.6f %.6f\n' % v)
    for t in vts:
        out.append('vt %.6f %.6f\n' % t)
    for v in vns:
        out.append('vn %.6f %.6f %.6f\n' % v)
    for l in faces:
        parts = l.strip().split()
        new = [parts[0]]
        for tok in parts[1:]:
            ids = tok.split('/')
            vi = ids[0]
            if len(ids) > 1 and ids[1] and has_vt:
                new.append('%s/%s/%s' % (vi, ids[1], vi))
            else:
                new.append('%s//%s' % (vi, vi))
        out.append(' '.join(new) + '\n')
    with open(fp, 'w', encoding='utf-8') as f:
        f.writelines(out)


if __name__ == '__main__':
    sys.exit(main())
