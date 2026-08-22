#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_scenes.py — 战场场景说明书批量生成器

对 07_场景/ 下全部 15 个场景生成完整说明书 (md):
  - 场景概览 (GO/TF/PS/MAT 计数, 根清单)
  - 3D 结构树 (Scenario/Baked 等: GO 名 + 局部 pos/quat/scale + 组件)
  - Transform 全表 (局部变换 + 世界链结算 — 复刻坐标的权威数据)
  - 网格表 (GO → OBJ 名 → 材质 → 贴图)
  - 材质表 (shader/blend/cull/zwrite/颜色/发光/贴图)
  - 粒子表 (shape/rate/lifetime/size/speed/颜色曲线/renderMode/贴图/网格)
  - 相机/灯/RenderSettings
  - 2D UI 根指引 (详情见 01_战斗/04_界面UI)

输出: d:/2/解包整理/说明书/02_战场_场景/<arena>.md + README.md
用法: py312 gen_spec_scenes.py [arena...]   (缺省=全部)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unity_scene_to_godot import (Assembler, SCENE_ROOT, q_mul, q_rot_vec)

OUT = 'd:/2/解包整理/说明书/02_战场_场景'
ALL = ['battlearena1', 'battlearena2', 'battlearena3',
       'battlearenaaeldari', 'battlearenaastramilitarum', 'battlearenablacklegion',
       'battlearenadarkangels', 'battlearenaemperorschildren',
       'battlearenagenestealers', 'battlearenaleviathan', 'battlearenasororitas',
       'battlearenaspacewolves', 'battlearenatauviorla',
       'mainmenuwarpforge', 'simpletransition']

ARENAS = sys.argv[1:] if len(sys.argv) > 1 else ALL

MIRROR_NOTE = ('> 坐标基准: 原版 Unity 世界 x 基准 100 (阵营变体 BattleBoardElements 均挂 x=100)\n'
               '> 手性: 本说明书坐标=Unity 原始数值 (左手系); 转 Godot 见 unity_scene_to_godot.py\n'
               '> (整世界 scale.x=-1 镜像 + 相机 conjX 共轭, 勿只转相机=左右镜像)\n')


def world_chain(a, tpid):
    chain = []
    cur = tpid
    while cur is not None and cur in a.TF:
        chain.append(a.local_trans(cur))
        cur = a.TF[cur].get('m_Father', {}).get('m_PathID')
    p = [0.0, 0.0, 0.0]
    q = [0.0, 0.0, 0.0, 1.0]
    for lt in reversed(chain):
        rp = q_rot_vec(tuple(q), lt[0:3])
        p = [p[0] + rp[0], p[1] + rp[1], p[2] + rp[2]]
        q = list(q_mul(tuple(q), lt[3]))
    return p, q


def gen(arena):
    a = Assembler(arena, OUT)
    lines = []
    w = lines.append
    w('# %s 场景说明书\n' % arena)
    w('> 来源: 解包整理/07_场景/%s/ (原始 Unity 序列化 JSON, 本文件为索引/摘要, 最终以原始 JSON 为准)\n' % arena)
    w('> 生成: gen_spec_scenes.py | GO %d / TF %d / PS %d / PSR %d / MAT %d / CAM %d / LIG %d' % (
        len(a.GO), len(a.TF), len(a.PS), len(a.PSR), len(a.MAT), len(a.CAM), len(a.LIG)))
    w(MIRROR_NOTE)
    w('')
    roots = a.root_transforms()
    w('## 根节点 (%d)\n' % len(roots))
    for t in roots:
        nm = a.go(a.TF[t].get('m_GameObject', {}).get('m_PathID')).get('m_Name', '?')
        w('- %s [t%d]' % (nm, t))
    w('')

    # 3D 树 (Scenario / Baked / BattlePrefab 主要根)
    w('## 3D 结构树 (主要根; 2D UI 子树省略)\n')
    for t in roots:
        nm = a.go(a.TF[t].get('m_GameObject', {}).get('m_PathID')).get('m_Name', '?')
        if nm in ('Scenario',) or 'Baked' in nm:
            w('```')
            import io
            buf = io.StringIO()
            a2 = a
            def tree2(tpid, depth=0):
                td = a2.TF.get(tpid)
                if td is None:
                    return
                gopid = td.get('m_GameObject', {}).get('m_PathID')
                nm2 = a2.go(gopid).get('m_Name', 'GO%d' % gopid)
                lt = a2.local_trans(tpid)
                comps = []
                mn, _ = a2.mesh_of(gopid)
                if mn:
                    comps.append('MESH')
                for c in a2.go_comps.get(gopid, []):
                    if c in a2.PS:
                        comps.append('PS')
                    elif c in a2.CAM:
                        comps.append('CAM')
                    elif c in a2.LIG:
                        comps.append('LIG')
                buf.write('  ' * depth + '%s pos=(%.2f,%.2f,%.2f)%s\n' % (
                    nm2, lt[0], lt[1], lt[2], (' [%s]' % ','.join(comps)) if comps else ''))
                for c in a2.children_of(tpid):
                    cg = a2.go(a2.TF[c].get('m_GameObject', {}).get('m_PathID')).get('m_Name', '')
                    if cg in ('ChooseCardMenuAnchor', 'Card Info', 'Tactic Container', 'EffectAnchor',
                              'MinionOrWarlord Container', 'Textbackgrounds', 'MulliganAnchor',
                              'HandArea', 'PlayerArea', 'EnemyArea', 'BattleHud', 'BattleTipController',
                              'Battle Events Controller', 'Card Material Helper', 'BattleManager',
                              'BattleScoreUiManager'):
                        buf.write('  ' * (depth + 1) + '%s ...(2D, 见 01_战斗)\n' % cg)
                        continue
                    tree2(c, depth + 1)
            tree2(t)
            w(buf.getvalue())
            w('```')
    w('')

    # Transform 全表 (3D 相关 Transform, 含世界链)
    w('## Transform 全表 (局部 + 世界链)\n')
    w('| tpid | GO 名 | 局部 pos | 局部 quat (x,y,z,w) | 世界 pos | 说明 |')
    w('|---|---|---|---|---|---|')
    done = set()
    for t in sorted(a.TF):
        lt = a.local_trans(t)
        gopid = a.TF[t].get('m_GameObject', {}).get('m_PathID')
        nm = a.go(gopid).get('m_Name', 'GO%d' % gopid)
        p, q = world_chain(a, t)
        note = ''
        mn, _ = a.mesh_of(gopid)
        if mn:
            note = 'MESH:%s' % mn
        for c in a.go_comps.get(gopid, []):
            if c in a.PS:
                note += ' PS'
            if c in a.CAM:
                note += ' CAM'
            if c in a.LIG:
                note += ' LIG'
        w('| %d | %s | (%.3f, %.3f, %.3f) | (%.3f, %.3f, %.3f, %.3f) | (%.3f, %.3f, %.3f) | %s |'
          % (t, nm, lt[0], lt[1], lt[2], lt[3][0], lt[3][1], lt[3][2], lt[3][3], p[0], p[1], p[2], note))
    w('')

    # 网格表
    w('## 网格表 (GO → OBJ → 材质 → 贴图)\n')
    w('| GO 名 | OBJ | 贴图 | 材质名 |')
    w('|---|---|---|---|')
    seen = set()
    for gopid in a.go_comps:
        mn, mo = a.mesh_of(gopid)
        if not mn or gopid in seen:
            continue
        seen.add(gopid)
        mats = a.mats_of(gopid)
        for mi in mats:
            w('| %s | %s | %s | %s |' % (
                a.go(gopid).get('m_Name', '?'), mn, mi.tex_name or '-', mi.name or '-'))
    w('')

    # 材质表
    w('## 材质表\n')
    w('| 材质名 | 贴图 | base_color | blend | cull | zwrite | emission | UVSpeed |')
    w('|---|---|---|---|---|---|---|---|')

    def _color_str(c):
        try:
            if isinstance(c, dict):
                return '(%s,%s,%s)' % (round(float(c.get('r', 0)), 2),
                                       round(float(c.get('g', 0)), 2),
                                       round(float(c.get('b', 0)), 2))
            return '(%s,%s,%s)' % tuple(round(float(v), 2) for v in c[:3])
        except (TypeError, ValueError, KeyError):
            return str(c)

    seen = set()
    for gopid in a.go_comps:
        for mi in a.mats_of(gopid):
            if mi.name in seen:
                continue
            seen.add(mi.name)
            em = mi.emission_color
            w('| %s | %s | %s | %d | %d | %d | %s | %s |' % (
                mi.name or '-', mi.tex_name or '-',
                _color_str(mi.base_color) if mi.base_color else '-',
                mi.blend, mi.cull, mi.zwrite,
                ('%s e=%.2f' % (_color_str(em), mi.emission_energy())) if em else '-',
                getattr(mi, 'uv_speed', '-') or '-'))
    w('')

    # 粒子表
    w('## 粒子表\n')
    w('| GO 名 | Shape | rate | 寿命 | size | speed | 颜色 | renderMode | 贴图/网格 |')
    w('|---|---|---|---|---|---|---|---|---|')
    for t in sorted(a.TF):
        gopid = a.TF[t].get('m_GameObject', {}).get('m_PathID')
        psr = a.ps_of(gopid)
        if psr is None or psr[0] is None:
            continue
        ps, rmode, mref, mats = psr
        im = ps.get('InitialModule', {}) or {}
        em = ps.get('EmissionModule', {}) or {}
        shp = ps.get('ShapeModule', {}) or {}
        rate = float((em.get('rateOverTime', {}) or {}).get('scalar', 0.0)) if isinstance(em.get('rateOverTime', {}), dict) else 0.0
        from unity_scene_to_godot import curve_min_max, curve_scalar
        lm = curve_min_max(im.get('startLifetime', {}), 1.0)
        sm = curve_min_max(im.get('startSize', {}), 1.0)
        sp = curve_min_max(im.get('startSpeed', {}), 0.0)
        tex = mats[0].tex_name if mats else '-'
        cm_raw = ps.get('ColorModule', {}) or {}
        has_color = bool(isinstance(cm_raw, dict) and cm_raw.get('enabled'))
        nm = a.go(gopid).get('m_Name', '?')
        w('| %s | %s(%.2f) | %.1f | %.2f-%.2f | %.2f-%.2f | %.2f-%.2f | %s | %d | %s |' % (
            nm, shp.get('type', 0), curve_scalar(shp.get('radius', {}), 1.0),
            rate, lm[0], lm[1], sm[0], sm[1], sp[0], sp[1],
            '有' if has_color else '-',
            rmode, tex))
    w('')

    # 相机/灯/渲染设置
    w('## 相机/灯/RenderSettings\n')
    for t in sorted(a.TF):
        gopid = a.TF[t].get('m_GameObject', {}).get('m_PathID')
        for c in a.go_comps.get(gopid, []):
            if c in a.CAM:
                cd = a.CAM[c]
                p, q = world_chain(a, t)
                w('- **%s** 相机: FOV=%s near=%s far=%s pos=(%.2f,%.2f,%.2f) lensShift=%s' % (
                    a.go(gopid).get('m_Name', '?'), cd.get('field of view'),
                    cd.get('near clip plane'), cd.get('far clip plane'), p[0], p[1], p[2],
                    cd.get('m_LensShift')))
            elif c in a.LIG:
                ld = a.LIG[c]
                lt = a.local_trans(t)
                w('- **%s** 灯: type=%d color=%s intensity=%s shadow=%s pos=(%.2f,%.2f,%.2f)' % (
                    a.go(gopid).get('m_Name', '?'), ld.get('m_Type'),
                    ld.get('m_Color'), ld.get('m_Intensity'),
                    (ld.get('m_Shadows') or {}).get('m_Type'), lt[0], lt[1], lt[2]))
    for r in a.REN.values():
        w('- RenderSettings: fog=%s ambientSky=%s ambientGround=%s intensity=%s' % (
            r.get('m_Fog'), r.get('m_AmbientSkyColor'), r.get('m_AmbientGroundColor'), r.get('m_AmbientIntensity')))
    w('')
    return '\n'.join(lines)


def main():
    os.makedirs(OUT, exist_ok=True)
    for arena in ARENAS:
        txt = gen(arena)
        fp = os.path.join(OUT, arena + '.md')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(txt)
        print('✓ %s -> %s (%d 行)' % (arena, fp, txt.count(chr(10))))
    # README
    rp = os.path.join(OUT, 'README.md')
    with open(rp, 'w', encoding='utf-8') as f:
        f.write('# 战场场景说明书 (07_场景)\n\n')
        f.write('- 共 %d 场景: 3 个位面团竞技场 + 11 个阵营变体 + 主菜单 + 过渡场景\n' % len(ALL))
        f.write('- 每个 <arena>.md: 场景概览 / 3D 结构树 / Transform 全表(含世界链) / 网格表 / 材质表 / 粒子表 / 相机灯环境\n')
        f.write('- 坐标=Unity 原始数值 (世界 x 基准 100); Godot 手性转换见 unity_scene_to_godot.py 顶部注释\n')
        f.write('- 2D UI 层 (HUD/手牌/容器) 见 **01_战斗_对战** 与 **04_界面UI** 说明书\n')
        f.write('- 阵营变体: aeldari / astramilitarum / blacklegion / darkangels / emperorschildren /\n')
        f.write('  genestealers / leviathan / sororitas / spacewolves / tauviorla\n')
        f.write('\n| 场景 | 说明 |\n|---|---|\n')
        for arena in ALL:
            f.write('| %s | [说明书](%s.md) |\n' % (arena, arena))
    print('✓ README')


if __name__ == '__main__':
    main()
