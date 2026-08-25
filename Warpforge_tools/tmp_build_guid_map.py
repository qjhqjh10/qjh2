import UnityPy, glob, os, json

aa = r'D:/2/unity_run_ref/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'

ALL_MAP = {}
for f in sorted(glob.glob(aa + '*.bundle')):
    try:
        env = UnityPy.load(f)
        files = list(env.files.values()) if isinstance(env.files, dict) else list(env.files)
    except Exception as e:
        print('load fail', os.path.basename(f), e)
        continue
    for sf in files:
        try:
            cont = sf.container
        except Exception:
            continue
        if not cont:
            continue
        # build path_id -> object (name/type)
        byid = {}
        try:
            for obj in sf.objects:
                byid[obj.path_id] = obj
        except Exception:
            pass
        for key, ptr in cont.items():
            pid = getattr(ptr, 'm_PathID', None)
            if pid is None:
                continue
            obj = byid.get(pid)
            if obj is None:
                # negative path ids are synthetic; try to find by abs id
                obj = byid.get(abs(pid))
            name = None
            if obj is not None:
                try:
                    if obj.type.name == 'GameObject':
                        name = obj.read().m_Name
                    else:
                        name = getattr(obj, 'name', None)
                except Exception:
                    name = None
            ALL_MAP[key] = (name, obj.type.name if obj is not None else '?', os.path.basename(f))

print('total GUID entries:', len(ALL_MAP))
rows = [(g, nm, ty, bn) for g, (nm, ty, bn) in ALL_MAP.items()]
# save
with open(r'D:/2/tmp_unity_scene/guid_map.tsv', 'w', encoding='utf-8') as fh:
    for g, nm, ty, bn in rows:
        fh.write(f'{g}\t{nm}\t{ty}\t{bn}\n')

# UI-ish sample
uis = [r for r in rows if r[1] and any(k in r[1].lower() for k in ('menu', 'panel', 'window', 'nav', 'popup', 'screen', 'tab', 'card', 'preview', 'modal', 'toast', 'collection', 'deck', 'shop', 'quest', 'chat', 'profile', 'rank', 'crate', 'pack', 'campaign', 'achievement', 'settings', 'status'))]
print('UI-ish entries:', len(uis))
for g, nm, ty, bn in sorted(uis, key=lambda r: r[1])[:60]:
    print(f'  {g[:12]}.. {nm} [{ty}] ({bn})')
