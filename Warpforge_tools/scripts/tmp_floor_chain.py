#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tmp_floor_chain.py — Floor plane 原版权威位置链 (2026-08-26 用户指示"位置错了"排查)
读 07_场景/battlearena1 原始 JSON: GO m_Transform → Transform localPosition/scale/m_Father 链到根"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
SRC = 'D:/2/解包整理/07_场景/battlearena1'
TYPES = ['GameObject', 'Transform', 'RectTransform', 'MeshRenderer', 'Material', 'MeshFilter', 'Shader']

_index = {}
for t in TYPES:
    td = os.path.join(SRC, t)
    if not os.path.isdir(td):
        continue
    for f in sorted(os.listdir(td)):
        if not f.endswith('.json'):
            continue
        m = f.rsplit('_', 1)
        pid = None
        if len(m) == 2 and m[1].replace('.json', '').lstrip('-').isdigit():
            pid = int(m[1].replace('.json', ''))
        try:
            d = json.load(open(os.path.join(td, f), encoding='utf-8'))
        except Exception:
            continue
        if pid is not None and pid not in _index:
            _index[pid] = {'type': t, 'path': os.path.join(td, f), 'data': d}


def get(pid):
    return _index.get(pid)


def go_name(pid):
    e = get(pid)
    if e and e['type'] == 'GameObject':
        return e['data'].get('m_Name')
    return None


def chain_from_go(gopid, maxdepth=12):
    e = get(gopid)
    if e is None or e['type'] != 'GameObject':
        return None
    # Transform 组件: 在 m_Component 里找类型为 Transform/RectTransform 的 pathID
    tpid = None
    for comp in e['data'].get('m_Component', []):
        cid = comp.get('component', {}).get('m_PathID')
        ce = get(cid)
        if ce and ce['type'] in ('Transform', 'RectTransform'):
            tpid = cid
            break
    if tpid is None:
        return [('NONE', 'no transform component')]
    cur = tpid
    out = []
    for _ in range(maxdepth):
        te = get(cur)
        if te is None:
            out.append((cur, 'TRANSFORM MISSING %s' % cur))
            break
        d = te['data']
        lp = d.get('m_LocalPosition', {})
        ls = d.get('m_LocalScale', {})
        q = d.get('m_LocalRotation', {})
        name = _name_on_chain(cur)
        out.append((cur, '%-30s pos=(%.4f, %.4f, %.4f) scale=(%.4f, %.4f, %.4f) rot=(%.4f,%.4f,%.4f,%.4f)' % (
            name,
            lp.get('x', 0), lp.get('y', 0), lp.get('z', 0),
            ls.get('x', 1), ls.get('y', 1), ls.get('z', 1),
            q.get('x', 0), q.get('y', 0), q.get('z', 0), q.get('w', 1))))
        f = d.get('m_Father', {}).get('m_PathID')
        if f == 0 or f is None:
            break
        fgo = _transform_owner(f)
        if fgo is None:
            out.append((f, 'FATHER-OWNER MISSING (Transform %s)' % f))
            break
        gopid = fgo
        cur = get(fgo)['data'].get('m_Transform', {}).get('m_FileID')
        # 重新找 fgo 的 transform
        nxt = None
        for comp in get(fgo)['data'].get('m_Component', []):
            cid = comp.get('component', {}).get('m_PathID')
            ce = get(cid)
            if ce and ce['type'] in ('Transform', 'RectTransform'):
                nxt = cid
                break
        cur = nxt
        if cur is None:
            break
    return out


_go_transform_owner = None


def _transform_owner(tpid):
    """Transform → 拥有它的 GO (反向索引)"""
    global _go_transform_owner
    if _go_transform_owner is None:
        _go_transform_owner = {}
        for pid, e in _index.items():
            if e['type'] == 'GameObject':
                for comp in e['data'].get('m_Component', []):
                    cid = comp.get('component', {}).get('m_PathID')
                    if cid == tpid:
                        _go_transform_owner[tpid] = pid
    return _go_transform_owner.get(tpid)


def _name_on_chain(tpid):
    gop = _transform_owner(tpid)
    if gop and get(gop):
        return go_name(gop)
    return '?'


# 根: 找 m_Father=0 的最高 GO
for gopid_name in ['Floor plane_1050', 'Floor plane_1201']:
    f = os.path.join(SRC, 'GameObject', gopid_name + '.json')
    if not os.path.exists(f):
        print(gopid_name, '文件不存在')
        continue
    d = json.load(open(f, encoding='utf-8'))
    pid = int(gopid_name.rsplit('_', 1)[1])
    print('=== %s (GO pid=%d) ===' % (gopid_name, pid))
    # 组件: MeshRenderer/MeshFilter 引用
    for comp in d.get('m_Component', []):
        cid = comp.get('component', {}).get('m_FileID')
        ce = get(cid)
        if ce:
            cd = ce['data']
            if ce['type'] == 'MeshRenderer':
                mats = [mm.get('m_FileID') for mm in cd.get('m_Materials', [])]
                print('  MeshRenderer materials:', mats)
                for mid in mats:
                    me = get(mid)
                    if me and me['type'] == 'Material':
                        mdata = me['data']
                        print('    Material', mdata.get('m_Name'), '| _Mode=', mdata.get('m_ShaderKeywords', '')[:0] or mdata.get('m_Name'))
                        # 属性
                        try:
                            props = mdata.get('m_SavedProperties', {}).get('m_TexEnvs', {})
                            for k in props:
                                if '_MainTex' in k or 'BaseMap' in k:
                                    print('      tex:', k, props[k].get('m_Texture', {}).get('m_FileID'))
                        except Exception:
                            pass
    for pid2, e in sorted(_index.items()):
        if e['type'] == 'Transform' and e['data'].get('m_GameObject', {}).get('m_FileID') == pid:
            # 直接打印其局部值
            pass
    ch = chain_from_go(pid)
    if ch:
        for c in ch:
            print('  ', c[1])
    print()
