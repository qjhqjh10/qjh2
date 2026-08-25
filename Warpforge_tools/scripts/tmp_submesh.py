#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tmp_submesh.py — battlearena2 MeshRenderer 子网格字段检查 (2026-08-26 F 映射 firstSubMesh)"""
import json, glob, os, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
for fp in glob.glob('D:/2/解包整理/07_场景/battlearena2/MeshRenderer/*.json')[:200]:
    try:
        j = json.load(open(fp, encoding='utf-8'))
    except Exception:
        continue
    sbi = j.get('m_StaticBatchInfo')
    if sbi and (sbi.get('m_SubMeshCount', 0) > 1 or (sbi.get('m_SubMeshIndex', 0) or 0) != 0):
        nm = os.path.basename(fp)
        print(nm, '| StaticBatchInfo=', sbi)
