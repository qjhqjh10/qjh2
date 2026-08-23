#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_deep.py — 说明书深度补全生成器 (2026-08-22)

补任务文件〇第7条缺口:
  07_模型/模型逐OBJ清单.md     — 1030 OBJ 逐文件清单 (顶点/面数/所属场景)
  08_主程序资源/运行时管理器.md — 管理器 GO→类全名→C# 源码路径
  06_特效_预制体/共享资源.md    — 场景共享资源 303 根清单
  04_界面UI/界面索引.md         — 313 根界面: 行号/尺寸/要点块 索引
"""
import json
import os
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

U = 'd:/2/解包整理/'
W = os.path.join(U, '说明书')
NL = chr(10)

UI_TREE = os.path.join(W, '04_界面UI/菜单全树.md')


def wfile(fp, txt):
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(txt)
    print('✓ %s (%d 行)' % (os.path.relpath(fp, W), txt.count(NL)))


def obj_stats(path):
    v = f = 0
    with open(path, encoding='utf-8', errors='ignore') as fh:
        for line in fh:
            if line[0:2] == 'v ':
                v += 1
            elif line[0:2] == 'f ':
                f += 1
    return v, f


ARENA_BY_PACK = {
    'scenes_scenes_battlearena1': 'battlearena1',
    'scenes_scenes_battlearena2': 'battlearena2',
    'scenes_scenes_battlearena3': 'battlearena3',
    'scenes_scenes_battlearenaaeldari': 'battlearenaaeldari',
    'scenes_scenes_battlearenaastramilitarum': 'battlearenaastramilitarum',
    'scenes_scenes_battlearenablacklegion': 'battlearenablacklegion',
    'scenes_scenes_battlearenadarkangels': 'battlearenadarkangels',
    'scenes_scenes_battlearenaemperorschildren': 'battlearenaemperorschildren',
    'scenes_scenes_battlearenagenestealers': 'battlearenagenestealers',
    'scenes_scenes_battlearenaleviathan': 'battlearenaleviathan',
    'scenes_scenes_battlearenasororitas': 'battlearenasororitas',
    'scenes_scenes_battlearenaspacewolves': 'battlearenaspacewolves',
    'scenes_scenes_battlearenatauviorla': 'battlearenatauviorla',
}


# ---------------- 07_模型 逐 OBJ 清单 ----------------
def gen_models():
    out = []
    out.append('# 模型逐OBJ清单 (06_模型, 1030 个 OBJ)')
    out.append('')
    out.append('> 计数: `v`=顶点行 / `f`=面行 (OBJ 文本行数, 非三角数)')
    out.append('> OBJ 是 Unity 归一化小模型 → Godot 放大 500-800x (泰伦例外 1-20x); 无 mtl, 材质在 Unity 侧')
    out.append('> 场景归属: `scenes_scenes_battlearenaX` 包 = 该场景专用; `battlesharedresources`/`battleprefabs_vfxandmisc` = 跨场景共享 (Baked 网格/道具/VFX mesh)')
    out.append('')
    md = os.path.join(U, '06_模型')
    for sub in sorted(os.listdir(md)):
        p = os.path.join(md, sub)
        if not os.path.isdir(p):
            continue
        arena = ARENA_BY_PACK.get(sub, '共享 (无专属场景)')
        objs = sorted([f for f in os.listdir(p) if f.lower().endswith('.obj')])
        nonobj = [f for f in os.listdir(p) if not f.lower().endswith('.obj')]
        out.append('## %s (%d OBJ) — 场景: %s' % (sub, len(objs), arena))
        if nonobj:
            out.append('')
            out.append('> 该包含非 OBJ 文件: %s' % ', '.join(nonobj))
        out.append('')
        out.append('| OBJ | v | f |')
        out.append('|---|---|---|')
        for fn in objs:
            v, f = obj_stats(os.path.join(p, fn))
            out.append('| %s | %d | %d |' % (fn, v, f))
        out.append('')
    wfile(os.path.join(W, '07_模型/模型逐OBJ清单.md'), NL.join(out))


# ---------------- 08_主程序资源 运行时管理器 ----------------
def go_pid(fname):
    m = fname.rsplit('_', 1)
    if len(m) == 2 and m[1].replace('.json', '').lstrip('-').isdigit():
        return int(m[1].replace('.json', ''))
    return None


def gen_managers():
    root = os.path.join(U, '12_主程序资源')
    # 索引: MonoBehaviour_<pid>.json (pid = 组件自身 pathID)
    mb_path = {}
    for f in os.listdir(os.path.join(root, 'MonoBehaviour')):
        if not f.endswith('.json') or f.endswith('_11.json') and f.startswith('MonoBehaviour_11_'):
            continue
    mb_files = {}
    for f in os.listdir(os.path.join(root, 'MonoBehaviour')):
        if not f.endswith('.json'):
            continue
        pid = go_pid(f)
        if pid is None or '_' in f.replace('.json', '').replace(str(pid), '', 1) and False:
            pass
        # 只取 <pid>_<pid> 中一个及纯 <pid> 中首个, 用 dict 覆盖即可
        mb_files[pid] = os.path.join(root, 'MonoBehaviour', f)
    ms_dir = os.path.join(root, 'MonoScript')
    ms_cache = {}

    def script_class(spid):
        if spid in ms_cache:
            return ms_cache[spid]
        p = os.path.join(ms_dir, 'MonoScript_%d.json' % spid)
        cl = None
        if os.path.exists(p):
            try:
                d = json.load(open(p, encoding='utf-8'))
                cl = d.get('m_ClassName')
            except Exception:
                pass
        ms_cache[spid] = cl
        return cl

    tf_dir = os.path.join(root, 'Transform')

    def transform_go_pid(pid):
        p = os.path.join(tf_dir, 'Transform_%d.json' % pid)
        if not os.path.exists(p):
            return None
        try:
            d = json.load(open(p, encoding='utf-8'))
            return d.get('m_GameObject', {}).get('m_PathID')
        except Exception:
            return None

    # GO 列表 (先去重: (name, comps) 相同即同一对象的多份导出)
    gos = {}
    for f in sorted(os.listdir(os.path.join(root, 'GameObject'))):
        if not f.endswith('.json'):
            continue
        try:
            d = json.load(open(os.path.join(root, 'GameObject', f), encoding='utf-8'))
        except Exception:
            continue
        comps = tuple(sorted(c['component']['m_PathID'] for c in d.get('m_Component', [])))
        key = (d.get('m_Name'), comps)
        gos.setdefault(key, []).append(f)

    # 管理器集合: 有 MonoBehaviour 组件的 GO
    rows = []
    for (name, comps), files in gos.items():
        # 找 GO 自身 pid
        go_pid_self = None
        for f in files:
            pid = go_pid(f)
            if pid is not None:
                go_pid_self = pid
                break
        if go_pid_self is None:
            for c in comps:
                t = transform_go_pid(c)
                if t is not None:
                    go_pid_self = t
                    break
        # 找脚本组件: comp pid 的 MonoBehaviour 且 GO 反查一致
        cls = None
        for c in comps:
            p = mb_files.get(c)
            if not p:
                continue
            try:
                mb = json.load(open(p, encoding='utf-8'))
            except Exception:
                continue
            if mb.get('m_GameObject', {}).get('m_PathID') != go_pid_self:
                continue
            spid = mb.get('m_Script', {}).get('m_PathID')
            cls = script_class(spid)
            if cls:
                break
        if cls:
            rows.append((name, cls, comps))

    rows.sort(key=lambda r: (r[0].lower(), r[1]))
    out = []
    out.append('# 运行时管理器清单 (12_主程序资源, UnityEngine 对象)')
    out.append('')
    out.append('> 解析链: GameObject → m_Component[] → MonoBehaviour_<pid>.json (m_GameObject 反查校验) → m_Script.m_PathID → MonoScript m_ClassName')
    out.append('> 共 %d 个带脚本组件的唯一 GameObject (去重后); 类名对应 Warpforge_code/Scripts/Assembly-CSharp/<类名>.cs' % len(rows))
    out.append('')
    out.append('## 清单')
    out.append('')
    out.append('| GameObject | 类 (MonoScript) | 组件 pid |')
    out.append('|---|---|---|')
    for name, cls, comps in rows:
        out.append('| %s | `%s` | %s |' % (name, cls, ','.join(map(str, comps))))
    out.append('')
    # 按类聚合
    out.append('## 按类聚合 (%d 唯一类)' % len({r[1] for r in rows}))
    out.append('')
    by_cls = defaultdict(list)
    for name, cls, comps in rows:
        by_cls[cls].append(name)
    out.append('| 类 | 挂载 GO 数 |')
    out.append('|---|---|')
    for cls in sorted(by_cls):
        out.append('| `%s` | %d |' % (cls, len(by_cls[cls])))
    wfile(os.path.join(W, '08_主程序资源/运行时管理器.md'), NL.join(out))


# ---------------- 06_特效 共享资源 ----------------
def gen_shared():
    root = os.path.join(U, '08_预制体特效/共享资源')
    gos = {}
    for f in sorted(os.listdir(os.path.join(root, 'GameObject'))):
        if not f.endswith('.json'):
            continue
        try:
            d = json.load(open(os.path.join(root, 'GameObject', f), encoding='utf-8'))
        except Exception:
            continue
        comps = tuple(sorted(c['component']['m_PathID'] for c in d.get('m_Component', [])))
        gos.setdefault((d.get('m_Name'), comps), 0)
        gos[(d.get('m_Name'), comps)] += 1
    names = sorted({k[0] for k in gos})
    out = []
    out.append('# 场景共享资源清单 (08_预制体特效/共享资源, %d 个唯一根)' % len(names))
    out.append('')
    out.append('> 与 12_主程序资源不同: 这里是被 15 个战场场景/战斗特效共享的**场景道具资源**')
    out.append('> 含各阵营 Baked 场景根 (Battle Arena X Baked) / 通用道具 (Altar/Banner/Pillar...) / 特效 mesh (Glow/Flame...)')
    out.append('> 引用方: unity_scene_to_godot.py (场景组装) / sync_arena_props.py (主项目道具)')
    out.append('')
    for n in names:
        out.append('- %s' % n)
    wfile(os.path.join(W, '06_特效_预制体/共享资源.md'), NL.join(out))


# ---------------- 04_界面UI 界面索引 ----------------
def gen_ui_index():
    try:
        lines = open(UI_TREE, encoding='utf-8').read().split(NL)
    except Exception as e:
        print('菜单全树读取失败:', e)
        return
    roots = []
    for i, ln in enumerate(lines, 1):
        if ln.startswith('- '):
            rest = ln[2:].strip()
            if not rest:
                continue
            name = rest.split(' [')[0].rstrip()
            size = ''
            if ' [' in rest:
                size = rest.split(' [', 1)[1].split(']')[0]
            roots.append((name, i, size))
    def block(i):
        if i <= 4200:
            return 1
        if i <= 8400:
            return 2
        if i <= 12600:
            return 3
        return 4
    out = []
    out.append('# 界面索引 (03_界面UI/菜单 + 07_场景/菜单 — 菜单全树.md 根界面对照)')
    out.append('')
    out.append('> 全树: 菜单全树.md (%d 行, %d 个根, dump_scene_tree.py 生成)' % (len(lines), len(roots)))
    out.append('> 块: 要点_第%d块 是逐界面详表 (元素/坐标/未实现清单); 原始 JSON: 03_界面UI/菜单/<类型>/<名>_<pid>.json')
    out.append('')
    out.append('| 根界面 | 行号 | 尺寸 | 要点块 |')
    out.append('|---|---|---|---|')
    for name, i, size in roots:
        out.append('| %s | %d | %s | %d |' % (name, i, size, block(i)))
    wfile(os.path.join(W, '04_界面UI/界面索引.md'), NL.join(out))


def main():
    gen_models()
    gen_managers()
    gen_shared()
    gen_ui_index()


if __name__ == '__main__':
    main()
