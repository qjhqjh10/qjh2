#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui_layout_parser.py — 解析解包 UI 场景 JSON，还原原版界面布局 (P2.5 核心工具)
来源: d:/2/解包整理/03_界面UI/<界面>/  (GameObject / RectTransform / MonoBehaviour / Sprite / Texture2D)
输出: d:/2/Warpforge_tools/data/ui_layout/<界面>.json
      树形布局清单: 元素名/层级/锚点/位置/尺寸/纹理/文字/字体 —— Godot 端照此重建

原理 (Unity 序列化):
  - GameObject.m_Component[].m_PathID -> 组件 JSON (MonoBehaviour 等) 的 m_GameObject.m_PathID
  - RectTransform: m_GameObject(归属) / m_Father(父) / m_Children / 锚点/位置/尺寸/pivot
  - MonoBehaviour 组件按字段特征识别类型:
      m_Sprite+m_Type      -> Image
      m_text               -> TextMeshProUGUI
      m_Interactable       -> Button
      m_blocksRaycasts     -> CanvasGroup
      m_movementType       -> ScrollRect
  - Image.m_Sprite.m_PathID -> Sprite JSON (文件名 PathID) -> m_RD.texture.m_PathID -> Texture2D (同目录 PNG)
  - PathID 从文件名提取: <名>_<PathID>.json (无后缀者为无 PathID 副本, 用内容匹配)

用法: d:/2/Warpforge_tools/py312/python.exe ui_layout_parser.py <界面目录名>
      例: ui_layout_parser.py 主菜单
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SRC = 'd:/2/解包整理/03_界面UI/'
OUT_DIR = 'd:/2/Warpforge_tools/data/ui_layout/'

# ---------- 索引: PathID -> 文件 ----------

def file_pathid(name: str) -> int:
    """从文件名提取 PathID: <名>_<PathID>.json (最后一段纯数字=PathID, 负数可带-)"""
    m = re.search(r'_(-?\d+)\.json$', name)
    return int(m.group(1)) if m else None


def build_index(ui_dir: str):
    """扫描目录, 建立 PathID -> {type, path, data} 索引; 另建 name->files"""
    index = {}          # pathid -> dict
    by_name = {}        # m_Name -> [files]
    for root, _, files in os.walk(ui_dir):
        for f in files:
            if not f.endswith('.json'):
                continue
            path = os.path.join(root, f)
            try:
                with open(path, encoding='utf-8') as fh:
                    d = json.load(fh)
            except Exception:
                continue
            pid = file_pathid(f)
            ftype = os.path.basename(root)  # 类型在目录名 (GameObject/RectTransform/...)
            if ftype not in ('GameObject', 'RectTransform', 'MonoBehaviour',
                             'Sprite', 'Texture2D', 'SpriteAtlas'):
                ftype = 'Other'
            entry = {'file': f, 'path': path, 'type': ftype, 'data': d}
            if pid is not None:
                # 同名同 PathID 去重 (UnityPy 常导出双份)
                if pid not in index:
                    index[pid] = entry
            nm = d.get('m_Name')
            if isinstance(nm, str) and nm:
                by_name.setdefault(nm, []).append(entry)
    return index, by_name


# ---------- 组件类型识别 ----------

def classify_component(d: dict) -> str:
    keys = set(d.keys())
    if 'm_Sprite' in keys or 'm_FillCenter' in keys:
        return 'Image'
    if 'm_text' in keys or 'm_fontAsset' in keys:
        return 'Text'
    if 'm_Interactable' in keys or 'm_TargetGraphic' in keys:
        return 'Button'
    if 'm_blocksRaycasts' in keys and 'm_ignoreParentGroups' in keys:
        return 'CanvasGroup'
    if 'm_movementType' in keys or 'm_verticalScrollbar' in keys:
        return 'ScrollRect'
    if 'm_HorizontalFit' in keys or 'm_ChildControlWidth' in keys:
        return 'Layout'
    return 'Unknown'


# ---------- 引用解析 ----------

def resolve_sprite(index, comp: dict, extra_spr=None):
    """Image 组件 -> Sprite 信息 (name/rect/atlas/texture 路径)
    extra_spr: pathid -> {name, file} 补充索引 (AssetBundle 提取出的 sprite)"""
    sp = comp.get('m_Sprite') or {}
    pid = sp.get('m_PathID')
    if pid is None:
        return None
    ent = index.get(pid)
    if ent:
        d = ent['data']
        tex = (d.get('m_RD') or {}).get('texture') or {}
        tex_pid = tex.get('m_PathID')
        tex_name = None
        if tex_pid is not None:
            te = index.get(tex_pid)
            if te:
                tex_name = te['data'].get('m_Name')
        return {
            'name': d.get('m_Name'),
            'rect': d.get('m_Rect'),
            'atlas': (d.get('m_AtlasTags') or [None])[0],
            'texture': tex_name,
            'type': d.get('m_Type'),
        }
    # 补充索引 (bundle 提取)
    if extra_spr is not None and pid in extra_spr:
        e = extra_spr[pid]
        return {'name': e['name'], 'rect': e.get('rect'), 'from': 'bundle'}
    return None


def comp_to_dict(index, comp: dict, extra_spr=None) -> dict:
    t = classify_component(comp)
    out = {'type': t}
    if t == 'Image':
        sp = resolve_sprite(index, comp, extra_spr)
        if sp:
            out['sprite'] = sp
        color = comp.get('m_Color') or {}
        if color:
            out['color'] = {k: color.get(k) for k in ('r', 'g', 'b', 'a')}
    elif t == 'Text':
        out['text'] = comp.get('m_text', '')
        fa = comp.get('m_fontAsset') or {}
        if fa.get('m_PathID'):
            ent = index.get(fa['m_PathID'])
            out['font'] = ent['data'].get('m_Name') if ent else None
        out['font_size'] = comp.get('m_fontSize')
        out['color'] = (comp.get('m_fontColor') or comp.get('m_color') or {})
        out['align'] = comp.get('m_textAlignment') or comp.get('m_HorizontalAlignment')
    elif t == 'Button':
        out['interactable'] = comp.get('m_Interactable')
        tg = comp.get('m_TargetGraphic') or {}
        if tg.get('m_PathID'):
            ent = index.get(tg['m_PathID'])
            if ent and 'm_Sprite' in ent['data']:
                out['target_sprite'] = resolve_sprite(index, ent['data'], extra_spr)
    elif t == 'ScrollRect':
        out['movement'] = comp.get('m_movementType')
    return out


def rect_to_dict(rt: dict) -> dict:
    return {
        'anchor_min': rt.get('m_AnchorMin') or {},
        'anchor_max': rt.get('m_AnchorMax') or {},
        'pos': rt.get('m_AnchoredPosition') or {},
        'size': rt.get('m_SizeDelta') or {},
        'pivot': rt.get('m_Pivot') or {},
        'scale': rt.get('m_LocalScale') or {},
        'rotation': rt.get('m_LocalRotation') or {},
    }


# ---------- 树构建 ----------

def load_extra_sprites() -> dict:
    """扫描 ui_extract 提取目录, 建立 pathid -> sprite 补充索引"""
    extra = {}
    base = 'd:/2/Warpforge_tools/data/ui_extract/'
    if not os.path.isdir(base):
        return extra
    for bundle in os.listdir(base):
        sdir = os.path.join(base, bundle, 'Sprite')
        if not os.path.isdir(sdir):
            continue
        for f in os.listdir(sdir):
            if not f.endswith('.json'):
                continue
            try:
                with open(os.path.join(sdir, f), encoding='utf-8') as fh:
                    d = json.load(fh)
            except Exception:
                continue
            pid = d.get('pathid')
            if pid is not None:
                extra[pid] = {'name': d.get('m_Name'), 'rect': d.get('m_Rect'),
                              'file': os.path.join(sdir, d.get('m_Name', '') + '.png')}
    return extra


def build_tree(ui_dir: str) -> dict:
    if not os.path.isabs(ui_dir):
        ui_dir = os.path.join(SRC, ui_dir)
    index, by_name = build_index(ui_dir)
    extra_spr = load_extra_sprites()
    # GameObject -> 组件列表
    gos = {}  # pathid -> {'name','active','comps':[...]}
    for pid, ent in index.items():
        if ent['type'] != 'GameObject':
            continue
        d = ent['data']
        comps = []
        for c in (d.get('m_Component') or []):
            cpid = (c.get('component') or {}).get('m_PathID')
            if cpid is None:
                continue
            ce = index.get(cpid)
            if not ce or ce['type'] != 'MonoBehaviour':
                continue
            cd = ce['data']
            # 确认组件归属该 GameObject (双份导出时 m_GameObject 可能不同)
            if (cd.get('m_GameObject') or {}).get('m_PathID') in (pid, None):
                comps.append(comp_to_dict(index, cd, extra_spr))
        gos[pid] = {'name': d.get('m_Name', ''), 'active': d.get('m_IsActive', True),
                    'comps': comps}
    # RectTransform (Transform 组件) -> 归属 GameObject / 父 / 子
    # 注意: m_Father/m_Children 引用的是 Transform 的 PathID, 不是 GameObject 的
    go_by_transform = {}  # transform_pid -> gameobj_pid
    rts = {}              # transform_pid -> rect 数据
    parents = {}          # transform_pid -> father transform pid
    children = {}         # father -> [children transforms]
    for pid, ent in index.items():
        if ent['type'] != 'RectTransform':
            continue
        d = ent['data']
        go = (d.get('m_GameObject') or {}).get('m_PathID')
        if go is None:
            continue
        go_by_transform[pid] = go
        rts[pid] = rect_to_dict(d)
        f = (d.get('m_Father') or {}).get('m_PathID')
        parents[pid] = f
        for ch in (d.get('m_Children') or []):
            cpid = (ch or {}).get('m_PathID')
            if cpid is not None:
                children.setdefault(f, []).append(cpid)

    # 构建树: 节点=Transform, 名字/组件取归属 GameObject
    def node(tid, depth=0):
        gid = go_by_transform.get(tid)
        go = gos.get(gid, {'name': f'<obj {gid}>', 'active': True, 'comps': []})
        n = {
            'name': go['name'],
            'pathid': tid,
            'active': go['active'],
            'depth': depth,
        }
        if tid in rts:
            n['rect'] = rts[tid]
        if go['comps']:
            n['components'] = go['comps']
        chs = [c for c in children.get(tid, []) if c in rts]
        if chs:
            n['children'] = [node(c, depth + 1) for c in chs]
        return n

    roots = [t for t in rts if parents.get(t) not in rts]
    tree = [node(t) for t in sorted(roots, key=lambda t: str(
        gos.get(go_by_transform.get(t, t), {}).get('name', t)))]
    # 统计
    stats = {'gameobjects': len(gos), 'rects': len(rts),
             'components': sum(len(g['comps']) for g in gos.values()),
             'roots': len(roots)}
    return {'ui': os.path.basename(ui_dir.rstrip('/\\')),
            'stats': stats, 'tree': tree}

def main() -> int:
    if len(sys.argv) < 2:
        print('用法: ui_layout_parser.py <界面目录名>  (如 主菜单 / 菜单 / 卡组选择按钮)')
        return 1
    ui = sys.argv[1]
    ui_dir = os.path.join(SRC, ui)
    if not os.path.isdir(ui_dir):
        print(f'[错误] 目录不存在: {ui_dir}')
        return 1
    out = build_tree(ui_dir)
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, ui + '.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    s = out['stats']
    print(f"✓ {ui}: {s['gameobjects']} GameObject / {s['rects']} RectTransform "
          f"/ {s['components']} 组件 / {s['roots']} 根节点 -> {out_path}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
