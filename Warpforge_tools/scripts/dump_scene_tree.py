# -*- coding: utf-8 -*-
"""场景全树解析: 解包场景目录 → 完整布局清单 (层级/坐标/纹理/文字/特效)
用法: python dump_scene_tree.py <场景目录> [输出md]
输出: 树形清单, 每行: 缩进-GO名 [Godot坐标 宽x高] active 组件摘要
"""
import json, glob, os, sys

sys.stdout.reconfigure(encoding='utf-8')

SCENE = sys.argv[1] if len(sys.argv) > 1 else 'D:/2/解包整理/07_场景/mainmenuwarpforge'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'D:/2/Warpforge_tools/data/ui_layout/主菜单全树.md'
W, H = 1920, 1080  # 原版设计分辨率

def load(t, pid):
    for f in glob.glob(os.path.join(SCENE, t, f'*_{pid}.json')):
        try:
            return json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
    return None

def go_file(pid):
    for f in glob.glob(os.path.join(SCENE, 'GameObject', f'*_{pid}.json')):
        return f
    return None

# 1) GO 索引
go_names, go_comps = {}, {}
for f in glob.glob(os.path.join(SCENE, 'GameObject', '*.json')):
    base = os.path.basename(f)
    m = base.rsplit('_', 1)
    if len(m) != 2 or not m[1].replace('.json', '').lstrip('-').isdigit():
        continue  # 跳过无 pathid 的重复文件
    pid = int(m[1].replace('.json', ''))
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    go_names[pid] = d.get('m_Name', '?')
    go_comps[pid] = [c['component']['m_PathID'] for c in d.get('m_Component', [])]

# 2) RectTransform + Transform
rects = {}
for f in glob.glob(os.path.join(SCENE, 'RectTransform', '*.json')):
    base = os.path.basename(f)
    m = base.rsplit('_', 1)
    if len(m) != 2 or not m[1].replace('.json', '').lstrip('-').isdigit():
        continue
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    rects[int(m[1].replace('.json', ''))] = d

transforms = {}
for f in glob.glob(os.path.join(SCENE, 'Transform', '*.json')):
    base = os.path.basename(f)
    m = base.rsplit('_', 1)
    if len(m) != 2 or not m[1].replace('.json', '').lstrip('-').isdigit():
        continue
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    transforms[int(m[1].replace('.json', ''))] = d

# 3) 组件索引 (MonoBehaviour 摘要)
def mb_summary(d):
    ks = d.keys()
    out = []
    if 'm_Sprite' in ks:
        sp = d.get('m_Sprite', {})
        if sp and sp.get('m_PathID'):
            out.append(f'sprite:{sp["m_PathID"]}')
    if 'm_text' in ks:
        t = d.get('m_text', '')
        if t:
            out.append(f'text:{t[:40]!r}')
    if 'm_OnClick' in ks:
        out.append('Button')
    if 'm_SliderValue' in ks:
        out.append('Slider')
    if 'm_horizontalScrollbarSpacing' in ks or 'm_VerticalScrollPosition' in ks:
        out.append('ScrollRect')
    if 'm_Script' in ks:
        out.append('script')
    return out

# 4) 树构建: 找所有根 (father=0), 递归
def abs_rect(pid, pabs=(0, 0, W, H)):
    r = rects.get(pid)
    if not r:
        return None
    amin, amax = r.get('m_AnchorMin', {}), r.get('m_AnchorMax', {})
    pp = r.get('m_AnchoredPosition', {})
    sd = r.get('m_SizeDelta', {})
    pv = r.get('m_Pivot', {})
    p0x, p0y, p1x, p1y = pabs
    pw, ph = p1x - p0x, p1y - p0y
    ax0 = p0x + amin.get('x', 0) * pw; ay0 = p0y + amin.get('y', 0) * ph
    ax1 = p0x + amax.get('x', 0) * pw; ay1 = p0y + amax.get('y', 0) * ph
    w = (ax1 - ax0) + sd.get('x', 0); h = (ay1 - ay0) + sd.get('y', 0)
    cx = ax0 + (ax1 - ax0) * pv.get('x', 0.5) + pp.get('x', 0)
    cy = ay0 + (ay1 - ay0) * pv.get('y', 0.5) + pp.get('y', 0)
    return (cx - w * pv.get('x', 0.5), cy - h * pv.get('y', 0.5),
            cx + w * (1 - pv.get('x', 0.5)), cy + h * (1 - pv.get('y', 0.5)))

def godot(a):
    return (a[0], H - a[3], a[2] - a[0], a[3] - a[1])

children_map = {}
for pid, d in list(rects.items()) + list(transforms.items()):
    for c in d.get('m_Children', []):
        children_map.setdefault(pid, []).append(c['m_PathID'])

lines = []
def walk(go_pid, depth, pabs, is_root=False):
    name = go_names.get(go_pid, f'<GO{go_pid}>')
    go = load('GameObject', go_pid)
    active = go.get('m_IsActive', True) if go else True
    # 找该 GO 的 RT
    rt = None
    for cpid in go_comps.get(go_pid, []):
        if cpid in rects:
            rt = cpid
            break
    npabs = pabs
    extra = []
    parts = []
    if rt:
        a = abs_rect(rt, pabs)
        if a:
            g = godot(a)
            parts.append(f'[{g[0]:.0f},{g[1]:.0f} {g[2]:.0f}x{g[3]:.0f}]')
            npabs = a
    # 组件摘要
    for cpid in go_comps.get(go_pid, []):
        mb = load('MonoBehaviour', cpid)
        if mb:
            s = mb_summary(mb)
            if s:
                parts.append(','.join(s))
        if cpid in go_comps and False:
            pass
    mark = ' (inactive)' if not active else ''
    line = '  ' * depth + f'- {name}{mark} ' + ' '.join(parts)
    lines.append(line)
    if rt:
        for c in children_map.get(rt, []):
            child_go = None
            for gpid, comps in go_comps.items():
                if c in comps:
                    child_go = gpid
                    break
            if child_go:
                walk(child_go, depth + 1, npabs)

roots = 0
for pid, d in list(rects.items()) + list(transforms.items()):
    f = d.get('m_Father', {})
    fpid = f.get('m_PathID') if isinstance(f, dict) else f
    if not fpid and pid in go_comps or (fpid == 0):
        pass
# 根: 无 father 的 RT 对应 GO
for pid in rects:
    f = rects[pid].get('m_Father', {})
    fpid = f.get('m_PathID') if isinstance(f, dict) else f
    if not fpid:
        for gpid, comps in go_comps.items():
            if pid in comps:
                walk(gpid, 0, (0, 0, W, H))
                roots += 1
                break

header = f"""# 主菜单场景全树 (解包 07_场景/mainmenuwarpforge)
> 生成: dump_scene_tree.py | GO {len(go_names)} / RT {len(rects)} / 根 {roots}
> 坐标=Godot(1920x1080, y向下); sprite=PathID(查 ui_extract 索引); 标注 (inactive) 的场景中禁用

"""
with open(OUT, 'w', encoding='utf-8') as fp:
    fp.write(header + '\n'.join(lines))
print(f'输出 {OUT}: {len(lines)} 行, {roots} 根')
