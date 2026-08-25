import UnityPy
import glob, os, sys

aa = r'D:/2/unity_run_ref/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'
names = {}
for f in sorted(glob.glob(aa + '*.bundle')):
    try:
        env = UnityPy.load(f)
        for file in env.files:
            try:
                cont = file.container
                if cont:
                    for k in cont:
                        names.setdefault(k, os.path.basename(f))
            except Exception:
                pass
    except Exception as e:
        print('ERR', os.path.basename(f), e)

print('total container entries:', len(names))
prefabs = [n for n in names if n.lower().endswith('.prefab')]
print('prefabs:', len(prefabs))
for n in sorted(prefabs)[:40]:
    print('  ', n, '<-', names[n])
with open(r'D:/2/tmp_unity_scene/prefab_names.txt', 'w', encoding='utf-8') as fh:
    for n in sorted(prefabs):
        fh.write(n + '\n')
