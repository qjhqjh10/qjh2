# -*- coding: utf-8 -*-
"""
audit_fx2d_0823.py — B3 2D 战斗特效补转数据审计 (2026-08-23)
检查: data/particles/ 下 28 个目标特效 JSON 存在 + texture 非空(或列入允许空名单) + 字段 sanity
用法: py312/python.exe Warpforge_tools/scripts/audit_fx2d_0823.py
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PDIR = 'D:/warpforge/data/particles'
APO = 'res://assets/particles/'

# battle.gd 引用但先前缺失的 28 名 (A19 转换名 + B8 + D2 以最终产物名判)
TARGETS = [
    'Healing_Projectile', 'Healing_Projectile_Frost', 'Healing_Projectile_Green',
    'Healing_Projectile_Ork', 'BulletImpact_1shot_trail', 'BulletImpact_1shot_random_chaos',
    'BulletImpact_1shot_random_EC', 'BulletImpact_1hit_trail_ork', 'BulletImpact_Tyranid_Small',
    'BulletImpact_autogun_1shot', 'BulletImpact_Shuriken_Short', 'Lasrifle_basic',
    'Sword Slash', 'Slash Repeating 2x', 'Cut Axe SW', 'Whip Attack EC Normal',
    'StunEffect_proc', 'Forewarned Board', 'Godspear Warhead',
    'BulletImpact_Tau_Pulse Rifle', 'Buff_Drachnyen', 'Master Interromancer Hit',
    'Orbital Bombardment Hit', 'Rapturous Ruination', 'Rapacious Claw Slash', 'Cut Wulfen',
    'Energy Accumulation VFX On', 'Glow Acummulated',
]

# 允许 texture 为空的名单 (原版无贴图/纯色染色型/材质链跨 bundle 断链) — 依审计结果增补
# Energy Accumulation VFX On: 场景材质 m_FileID=8 外部 bundle 引用, 解包链断 → 2026-08-23 已补
#   Glow.png 金色光斑视觉补偿 (不再豁免 tex)
# Master Interromancer Hit: bundle 全 13 子粒子贴图链跨 bundle 断 (无 3D 可提先例) → 暖金白金点近似
ALLOW_NO_TEX = ['Master Interromancer Hit']


def audit() -> int:
    bad = 0
    missing = []
    no_tex = []
    for n in TARGETS:
        fp = os.path.join(PDIR, n + '.json')
        if not os.path.exists(fp):
            missing.append(n)
            print('✗ MISSING JSON:', n)
            bad += 1
            continue
        d = json.load(open(fp, encoding='utf-8'))
        issues = []
        tex = d.get('texture', '')
        if not tex:
            if n in ALLOW_NO_TEX:
                print('● %-32s tex=空 (豁免)' % n)
                continue
            no_tex.append(n)
            issues.append('tex=空')
        elif tex.startswith(APO):
            real = 'D:/warpforge/assets/particles/' + tex[len(APO):]
            if not os.path.exists(real):
                issues.append('tex文件不存在: ' + real)
        else:
            issues.append('tex前缀异常: ' + tex)
        # sanity
        if float(d.get('lifetime', 0) or 0) <= 0:
            issues.append('lifetime<=0')
        if float(d.get('size_min', 0) or 0) <= 0:
            issues.append('size_min<=0')
        br = d.get('bursts') or []
        rate = float(d.get('emission_rate', 0) or 0)
        if not br and rate <= 0:
            issues.append('无 bursts/rate (不发射)')
        if d.get('name') != n:
            issues.append('name!=文件名')
        if issues:
            bad += 1
            print('✗ %-32s %s' % (n, '; '.join(issues)))
        else:
            print('✓ %-32s tex=%s lifetime=%s size=%s bursts=%s rate=%s' % (
                n, os.path.basename(tex) if tex else '空',
                d.get('lifetime'), d.get('size_min'), br, rate))
    print('---')
    print('审计: %d 名, 缺失 %d, tex空 %d, 异常 %d' % (len(TARGETS), len(missing), len(no_tex), bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(audit())
