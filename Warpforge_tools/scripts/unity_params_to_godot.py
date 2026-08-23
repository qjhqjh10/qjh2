#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unity_params_to_godot.py — Unity 说明书参数 → Godot 参数自动转化器（表驱动）

用户指示(2026-08-23): 制作工具对说明书的参数自动转化调整为适合 Godot 引擎的参数。
本项目已验证的转换知识全部固化于此（来源=解包资源使用地图 坑1-58 + CLAUDE.md + 实测）：
  * UI 坐标: anchoredPosition≠直接照抄 (y 翻转/pivot 修正/锚点拉伸中心/父链累加/根偏移) → chain_rect.py 同源
  * UI 9-slice: Sprite m_Border=(左,下,右,上) → Godot patch_margin 左/上/右/下 (b→bottom 直接对应)
  * UI 元素: Image(m_Sprite→texture)/Text(m_text/fontSize→Label 配置)/m_Color→modulate
  * 材质: _BaseMap→albedo_texture, _Color→albedo_color, _Blend(0/1/2/4/5)→transparency,
          _Cull(0/1/2)→cull_mode(BACK/FRONT/DISABLED), _ZWrite→no_depth_test/alpha
  * 粒子: MinMaxCurve(st 0=scalar/其它=minScalar), startSize=直径勿×2, Gradient ctime/atime 独立轴,
          ShapeType 枚举(0 球/1 球壳/2-3 半球/4 锥/5 盒/7 圆环), 翻页 tilesX/Y, m_Color 可 HDR>1→clamp 1.0
  * 相机: FOV 直通, LensShift y→frustum_offset(仅 FRUSTUM 投影有效), Unity +Z 朝前→Godot -Z(Y180),
          正交 orthographicSize→size
  * 灯/环境: 单位光强直通 Godot 过曝 2-3 倍→能量校准因子(实测 1.0 匹配参考图), 环境光在 SH probe
          不在 Trilight(Trilight 仅 skybox 配置), RenderSettings m_Fog=false 勿开雾
  * 曲线: AnimationCurve/ColorGradient keys → Godot Curve(点数组)/GradientTexture1D(颜色+alpha 独立)

用法:
  python unity_params_to_godot.py --ui-mapping            # 打印全部映射表 (知识库)
  python unity_params_to_godot.py --translate "m_AnchoredPosition" "x,-3, y,10"  # 单键值转换
  python unity_params_to_godot.py --json  <RectTransform.json...>  # 批量转换 UI JSON (Godot 行输出)
  python unity_params_to_godot.py --json --screen 1920x1080 <RectTransform.json...>  # +y 翻转/父链(需 --father 链)

输出: stdout (Godot 参数行, 可直接贴入 tscn/gd); --out 文件
"""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')


# ================= 表驱动映射 (权威=各坑来源, 每个映射条注 [坑号]) =================

# UI: Unity RectTransform 字段 → Godot 语义 (值需换算的给出公式)
UI_TRANSLATE = {
    # 键名 → (Godot 属性, 换算说明)
    'm_AnchoredPosition': ('offset ±', '相对锚点矩形中心的偏移; pivot≠0.5 时须按 pivot 修正; y 轴翻转 godot_top=H-unity_top-h'),
    'm_SizeDelta': ('size', '尺寸直通 (缩放节点需乘 m_LocalScale, 坑37)'),
    'm_AnchorMin': ('anchor_left/top', '锚点直通 (0..1 归一)'),
    'm_AnchorMax': ('anchor_right/bottom', '锚点直通'),
    'm_Pivot': ('pivot_offset', 'pivot≠(0.5,0.5) 必须修正 (如 PlayerDeck pivot(0.5,0))'),
    'm_LocalScale': ('scale', '缩放: 输出乘以 (坑37; mode_select 法力曲线 1.2)'),
    'm_LocalPosition': ('position', '父级局部坐标; 3D 内 Transform 链含 scale (坑58 注)'),
    'm_LocalRotation': ('rotation', '四元数→欧拉; Unity 左手系→Godot 右手系须反射 (手性见坑52)'),
}

# UI: Sprite m_Border (9-slice) → Godot patch_margin —— 顺序: Unity=(左,下,右,上), Godot=(左,上,右,下)
# [坑56] b→bottom 直接对应, 无翻转
def border_to_patch(border):
    l, b, r, t = border
    return l, t, r, b

# UI: m_Image/m_Color → Godot
UI_IMAGE = {
    'm_Sprite': 'texture',                # PathID → Sprite JSON → Godot load() 路径
    'm_Color': 'modulate',                # Color (R,G,B,A) 直通
    'm_Color.a': 'modulate.a',            # alpha 分量直通 (图集 alpha 缺陷另查 坑51/56)
}

# 材质: Unity Material m_SavedProperties → Godot StandardMaterial3D (坑: 光强/alpha/图集)
# m_BlendMode: 0=Opaque 1=Cutout 2=Fade 4=Transparent 5=Additive
MAT_TRANSLATE = {
    '_BaseMap': ('albedo_texture', '贴图直通; 图集 alpha=0 RGB=内容=缺陷 需修复 (坑51/56)'),
    '_MainTex': ('albedo_texture', '同 _BaseMap'),
    '_Color': ('albedo_color', '颜色直通; 但 m_Color 可 HDR>1 (Embers 2.828) → 粒子材质须 clamp 1.0 (坑53)'),
    '_BaseColor': ('albedo_color', '同 _Color'),
    '_EmissionColor': ('emission', 'emission_energy_multiplier 校准 (Godot 无 glow 乘积)'),
    '_Blend': ('transparency', '0→OFF 1→ALPHA 2→ALPHA 4→ALPHA 5→ADD (表: {0:"OFF",1:"ALPHA",2:"ALPHA",4:"ALPHA",5:"ADD"})'),
    '_Cull': ('cull_mode', '0→BACK 1→FRONT 2→DISABLED (薄片面须 DISABLED, 坑19 Chain SMR)'),
    '_ZWrite': ('no_depth_test', '0→true (透明粒子禁用深度写防遮挡) 1→false'),
    '_Surface': ('specular', '0=透明折射(Godot 无等效→Glow 低alpha 近似 坑15)'),
    'm_Glossiness': ('metallic/roughness', 'roughness = 1-glossiness 近似 (光斑 P2)'),
}

# 粒子: Unity ParticleSystem → Godot ParticleProcessMaterial (坑40/41/53 + 持续验证)
# MinMaxCurve 取值: st==0 → scalar, 否则 minScalar (converter cv() 同源)
PARTICLE_TRANSLATE = {
    'm_StartLifetime': ('lifetime', '直通'),
    'm_StartSize': ('scale (直径!)', '**startSize 是 quad 直径 (宽度) 语义, 勿 /2, 勿 ×2** (坑14/19)'),
    'm_StartSpeed': ('initial_velocity', '恒速粒子=velocity-over-lifetime 单点 → direction+initial_velocity (坑46)'),
    'm_SimulationSpeed': ('speed_scale', '直通 (光柱 0.3/毒气 0.4 等)'),
    'm_GravityModifier': ('gravity', 'multiplier ×9.8 且 y 取反 (实测 坑14)'),
    'm_StartColor(mode2)': ('color', 'min/max 随机取中值 (mode 0=常数/2=双色)'),
    'Gradient ctime/atime': ('color_ramp', '**color keys 按 ctime、alpha keys 按 atime 独立插值** (坑40)'),
    'm_Shapes.m_Type': ('emission_shape', '枚举: 0=SPHERE 1=SPHERE_SURFACE 2/3=SPHERE 4=SPHERE(锥近似) 5=BOX 7=RING (坑41)'),
    'UVModule.tilesX/Y': ('particles_anim', '翻页分片 (8×8/6×5/7×7) + anim_speed (坑46)'),
    'm_Bursts': ('burst', 'rate=0 时 burst 一次性 (one-shot, 上限 200)'),
    'renderMode=4': ('mesh draw pass', 'Mesh 粒子 → OBJ draw pass (13 轮)'),
}

# 相机 (坑 52/55/20轮续):
CAMERA_TRANSLATE = {
    'FOV': ('fov', '直通 (46.397)'),
    'LensShift.y': ('frustum_offset.y', '仅 FRUSTUM 投影有效; 旧实现"LensShift 从未生效"教训; 或换算 pitch≈atan2(offsetY,1)'),
    'orthographicSize': ('size', '正交直通'),
    'nearClipPlane/farClipPlane': ('near/far', '直通 (0.3/300)'),
    'm_BackgroundColor': ('clear color / bg', '相机背景色'),
    'Unity +Z 朝前': ('-Z 朝前', 'Y180 左乘 (Rz180 颠倒画面已撞过 坑15)'),
}

# 灯/环境 (坑 19/46):
LIGHT_TRANSLATE = {
    'm_Intensity': ('light_energy', '**Unity 光强直通 Godot 过曝 2-3 倍** → 能量校准实测 1.0 匹配参考图 (坑46); 灯白光 1.0'),
    'm_Color': ('light_color', '直通 (黑军团=白光 1.0 无暖色! LUT identity 修正后)'),
    'm_Shadows': ('shadow_enabled', '直通'),
    'm_AmbientProbe(DC)': ('ambient source', '**环境光在 SH probe (0.289,0.183,-0.08), Trilight 三色仅 skybox 配置** (坑46)'),
    'm_AmbientIntensity': ('ambient_energy', '校准因子 (15 轮: 直通 1.0 匹配参考)'),
    'm_Fog': ('fog', '**原版 m_Fog=false → Godot 勿开雾** (坑46; 曾 fog_sun_scatter 天空全黑)'),
    'm_AmbientMode=3': ('Trilight', '仅配置天空盒; Godot BG_COLOR 下 AMBIENT_SOURCE_SKY 实测不渲染 (坑46)'),
}

# 曲线/渐变:
CURVE_TRANSLATE = {
    'AnimationCurve': ('Curve', 'keys(time,value) 直通为点数组; 动画剪辑走 glTF morph/AnimationPlayer (坑55)'),
    'Gradient': ('GradientTexture1D', '颜色/alpha 双轨独立 (GradientTexture1D 包装)'),
    'm_ReverseArrangement': ('反转布局', 'HorizontalLayoutGroup 反向 = Godot 反向挂载序 (deck_info 圆钮 坑: 8-21)'),
}

# LayoutGroup: Unity Horizontal/VerticalLayoutGroup → Godot 容器 (布局组内元素 chain_rect 不适用!)
LAYOUT_TRANSLATE = {
    'm_Spacing': ('separation', '直通 (卡行 2/负值-16.35)'),
    'm_Padding': ('offsets', 'padding l/r/t/b 直通'),
    'm_ChildAlignment': ('alignment', '枚举映射 (align=5 右对齐等)'),
    'm_ChildControlWidth': ('size flags', 'Expand/Fill 控制'),
    'cellSize (GridLayoutGroup)': ('网格', 'cellSize/spacing/padding 直通 (卡组方块 225×364.5 坑: deck_collection.gd)'),
}


# ================= 工具函数 =================

def ui_json_to_godot(rt: dict, screen_h: int = 1080, chain: list = None) -> list:
    """单个 RectTransform JSON → Godot Control 配置行 (含 y 翻转; chain=父链 [{pos,size,pivot,anchor}...] 则链式累加)
    返回 [godot 行, ...]; 权威换算与 chain_rect.py 同源。"""
    out = []
    anchor_min = rt.get('m_AnchorMin', {'x': 0.5, 'y': 0.5})
    anchor_max = rt.get('m_AnchorMax', {'x': 0.5, 'y': 0.5})
    pivot = rt.get('m_Pivot', {'x': 0.5, 'y': 0.5})
    size = rt.get('m_SizeDelta', {'x': 100, 'y': 100})
    pos = rt.get('m_AnchoredPosition', {'x': 0, 'y': 0})
    # Godot anchors (直接)
    out.append(f'anchor = ({anchor_min.get("x", .5)}, {anchor_min.get("y", .5)}, {anchor_max.get("x", .5)}, {anchor_max.get("y", .5)})')
    # pivot
    out.append(f'pivot_offset = ({pivot.get("x", .5)} * size.x, {pivot.get("y", .5)} * size.y)')
    # 锚点拉伸时 Godot offset 相对锚点矩形中心 (Unity 同语义) → offset 直通但 y 变号
    px, py = pos.get('x', 0), pos.get('y', 0)
    out.append(f'offset (拉伸锚) = left:{px:.2f}  top:{-py:.2f}  right:{px + size.get("x", 0):.2f}  bottom:{-py - size.get("y", 0):.2f}   # y 翻转 (坑56)')
    # 非拉伸 (anchor 端点, 即 pivot 修正): Godot position=锚点位置+pivot 换算
    if anchor_min == anchor_max:
        out.append(f'position (非拉伸) = anchor_point + (px - pivot.x*size.x, -py + pivot.y*size.y - H*0?)  # 见 chain_rect.py 权威')
    # 链式累加绝对坐标
    if chain:
        ax, ay = 0.0, 0.0
        for c in chain:
            cp = c.get('pos', {'x': 0, 'y': 0})
            cx_size = c.get('size', {'x': 0, 'y': 0})
            ax += cp.get('x', 0)
            ay += cp.get('y', 0)
        out.append('chain 父链累加: 请用 chain_rect.py 权威输出 (y 翻转 godot_top = H - unity_top - h, 锚点拉伸时相对锚点矩形中心; 坑56)')
    return out


def border_row(border) -> str:
    l, b, r, t = border
    lp, tp, rp, bp = border_to_patch(border)
    return (f'NinePatchRect.patch_margin = left:{lp} top:{tp} right:{rp} bottom:{bp}   '
            f'# Unity m_Border=({l},{b},{r},{t}) 左/下/右/上 → Godot 左/上/右/下 (坑56)')


MAT_BLEND = {0: 'OFF (不透明)', 1: 'ALPHA (cutout 近似)', 2: 'ALPHA', 4: 'ALPHA', 5: 'ADD'}
CULL = {0: 'BACK', 1: 'FRONT', 2: 'DISABLED'}


def material_row(key: str, val) -> str:
    """材质单键转换 (m_SavedProperties 值) → Godot 行"""
    if key == '_Blend':
        return f'material.transparency = {MAT_BLEND.get(int(val), "?")}   # _Blend={val}'
    if key == '_Cull':
        return f'material.cull_mode = {CULL.get(int(val), "?")}   # _Cull={val} (坑19 薄片)'
    if key == '_ZWrite':
        return f'material.no_depth_test = {"true" if int(val) == 0 else "false"}   # _ZWrite={val}'
    if key in ('_BaseMap', '_MainTex'):
        return f'material.albedo_texture = <tex path>   # {key} 贴图直通 (alpha 缺陷另修)'
    if key in ('_Color', '_BaseColor'):
        c = val[0] if isinstance(val, list) else val
        return f'material.albedo_color = {c}   # {key} 直通 (HDR>1 → clamp{1.0} 坑53)'
    return f'# 未知材质键 {key} = {val} — 查 Material 说明书章节'


# ================= CLI =================

def main() -> int:
    args = sys.argv[1:]
    if not args or args[0] == '--ui-mapping':
        print('=== Unity→Godot 参数映射表 (知识库, 来源=使用地图坑1-58) ===')
        for title, table in [('UI RectTransform', UI_TRANSLATE), ('UI Image', UI_IMAGE),
                             ('材质', MAT_TRANSLATE), ('粒子', PARTICLE_TRANSLATE),
                             ('相机', CAMERA_TRANSLATE), ('灯/环境', LIGHT_TRANSLATE),
                             ('曲线/布局', {**CURVE_TRANSLATE, **LAYOUT_TRANSLATE})]:
            print(f'\n## {title}')
            for k, (godot, note) in table.items():
                print(f'  {k:28} → {godot:22} # {note}')
        print('\n9-slice 示例: m_Border=(150,0,150,0) →', border_row([150, 0, 150, 0]))
        return 0
    if args[0] == '--json':
        files = [a for a in args[1:] if not a.startswith('--')]
        screen_h = 1080
        for a in args[1:]:
            if a.startswith('--screen'):
                screen_h = int(a.split('=')[1])
        for f in files:
            d = json.load(open(f, encoding='utf-8'))
            print(f'## {f}')
            print('\n'.join(ui_json_to_godot(d, screen_h)))
        return 0
    if args[0] == '--translate' and len(args) >= 3:
        key, val = args[1], args[2]
        if key in MAT_TRANSLATE:
            print(material_row(key, float(val) if re.fullmatch(r'-?\d+(\.\d+)?', val) else val))
        else:
            print(f'{key} → {(UI_TRANSLATE.get(key, MAT_TRANSLATE.get(key)) or ("未知键", "查说明书"))[0]}  # 值 {val} 需按说明换算')
        return 0
    if args[0] == '--border' and len(args) >= 2:
        vs = [float(x) for x in args[1].split(',')]
        print(border_row(vs))
        return 0
    print(__doc__)
    return 1


if __name__ == '__main__':
    sys.exit(main())
