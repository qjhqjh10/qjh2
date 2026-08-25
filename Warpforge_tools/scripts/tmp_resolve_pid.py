# -*- coding: utf-8 -*-
"""tmp helper: resolve a PathID within a folder (scene or prefab) to its JSON + class/type.
usage: python tmp_resolve_pid.py <folder> <pid> [pid2 ...]"""
import json, glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

FOLDER = sys.argv[1]
pids = sys.argv[2:]

# class map: script pid -> class name
CLS = {}
for sf in glob.glob('d:/2/解包整理/09_游戏数据/脚本定义/MonoScript/*.json'):
    base = os.path.basename(sf)[:-5]
    key = base.replace('MonoScript_', '')
    if key.endswith('_' + key):
        key = key[:key.rfind('_')]
    try:
        dd = json.load(open(sf, encoding='utf-8'))
    except Exception:
        continue
    cn = dd.get('m_ClassName')
    if cn:
        CLS[key] = cn
CLS_PID = {}
for k, v in CLS.items():
    try:
        CLS_PID[int(k)] = v
    except Exception:
        pass

idx = {}
TYPE_DIRS = ['GameObject', 'RectTransform', 'Transform', 'MonoBehaviour', 'SpriteRenderer',
             'MeshRenderer', 'MeshFilter', 'CanvasRenderer', 'Animator', 'AudioSource', 'Camera', 'Canvas', 'CanvasGroup', 'MeshCollider', 'BoxCollider2D', 'LineRenderer', 'ParticleSystem', 'TextMeshPro', 'SkinnedMeshRenderer']
for t in TYPE_DIRS:
    td = os.path.join(FOLDER, t)
    if not os.path.isdir(td):
        continue
    for f in os.listdir(td):
        if not f.endswith('.json'):
            continue
        base = f[:-5]
        m = base.rsplit('_', 1)
        if len(m) == 2 and m[1].lstrip('-').isdigit():
            key = int(m[1])
            if key not in idx:
                idx[key] = (f, t)

def show(pid):
    pid = int(pid)
    if pid not in idx:
        print(pid, '-> NOT FOUND')
        return
    f, t = idx[pid]
    full = os.path.join(FOLDER, t, f)
    try:
        d = json.load(open(full, encoding='utf-8'))
    except Exception as e:
        print(pid, '-> JSON ERR', e)
        return
    line = f'[{t}] {os.path.basename(f)}'
    if 'm_Name' in d and d['m_Name']:
        line += f'   name="{d["m_Name"]}"'
    go = d.get('m_GameObject')
    if isinstance(go, dict):
        line += f'   go={go.get("m_PathID")}'
    sc = d.get('m_Script')
    if isinstance(sc, dict) and sc.get('m_PathID'):
        cls = CLS_PID.get(sc['m_PathID'], '?')
        line += f'   script={cls}(pid {sc["m_PathID"]})'
    print(line)
    if t == 'RectTransform':
        print('      anchorMin', d.get('m_AnchorMin'), 'anchorMax', d.get('m_AnchorMax'))
        print('      pos', d.get('m_AnchoredPosition'), 'size', d.get('m_SizeDelta'), 'pivot', d.get('m_Pivot'))
        print('      father', d.get('m_Father'), 'children', d.get('m_Children'))
        print('      localScale', d.get('m_LocalScale'))
    if t in ('MonoBehaviour',):
        for k, v in d.items():
            if k not in ('m_GameObject', 'm_Enabled', 'm_Script', 'm_Name', '_$_serializedVersion'):
                print(f'      {k} = {v}')
    if t in ('SpriteRenderer', 'MeshRenderer', 'MeshFilter', 'Transform', 'Canvas', 'CanvasGroup', 'Camera', 'AudioSource', 'SkinnedMeshRenderer'):
        for k, v in d.items():
            if k not in ('m_GameObject', 'm_Enabled', 'm_Name'):
                s = json.dumps(v, ensure_ascii=False)
                if len(s) > 400:
                    s = s[:400] + '...'
                print(f'      {k} = {s}')

for p in pids:
    show(p)
