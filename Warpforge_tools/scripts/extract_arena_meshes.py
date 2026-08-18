#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_arena_meshes.py — 从场景 AssetBundle 导出 Mesh -> OBJ (与 06_模型/<bundle> 同构)
用法: d:/2/Warpforge_tools/py312/python.exe extract_arena_meshes.py <bundle名> [<bundle名>...]
输出: d:/2/解包整理/06_模型/<bundle名>/<Mesh名>.obj (UnityPy export 自带 UV/法线)
"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
OUT_DIR = 'd:/2/解包整理/06_模型/'


def main() -> int:
    if len(sys.argv) < 2:
        print('用法: extract_arena_meshes.py <bundle名> ...')
        return 1
    import UnityPy
    for name in sys.argv[1:]:
        path = os.path.join(BUNDLE_DIR, name + '.bundle')
        if not os.path.exists(path):
            print(f'[错误] {path} 不存在')
            continue
        env = UnityPy.load(path)
        out = os.path.join(OUT_DIR, name)
        os.makedirs(out, exist_ok=True)
        counts = {}
        for obj in env.objects:
            try:
                if obj.type.name != 'Mesh':
                    continue
                data = obj.read()
                mname = str(data.m_Name or obj.path_id)
                fname = mname.replace('/', '_')[:80]
                fp = os.path.join(out, fname + '.obj')
                if os.path.exists(fp):
                    continue
                raw = obj.export()
                if not raw:
                    continue
                with open(fp, 'wb') as f:
                    f.write(raw)
                counts[fname] = len(data.m_VertexData is not None and data.m_VertexCount or 0)
            except Exception:
                continue
        print(f'✓ {name}: {len(counts)} 个 OBJ')
        print(f'  -> {out}')
        for k in sorted(counts):
            print(f'    {k}.obj')
    return 0


if __name__ == '__main__':
    sys.exit(main())
