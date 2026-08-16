#!/usr/bin/env python3
"""Fix exports using UnityPy 1.24 (py312): textures, meshes, fonts, videos, vorbis oggs."""
import os, sys, io, re, json, time
import UnityPy
from UnityPy.export import MeshExporter
import fsb_audio as FA
import ogg_build as OB

GAME = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data"
BUNDLES = os.path.join(GAME, "StreamingAssets", "aa", "StandaloneWindows64")
OUT = r"d:/2/Warpforge_assets_full"
HARVEST = r"d:/2/解包整理"  # vorbis setup 头收割源 (递归找 .ogg)

def load_files():
    files = []
    for fn in sorted(os.listdir(GAME)):
        if fn.endswith((".assets", ".resource")) or fn.startswith(("globalgamemanagers", "level0", "level1", "sharedassets")):
            files.append((os.path.join(GAME, fn), fn))
    for fn in sorted(os.listdir(BUNDLES)):
        if fn.endswith(".bundle"):
            files.append((os.path.join(BUNDLES, fn), "bundle_" + fn))
    return files

# harvest ogg headers: by name and by (ch, rate) (递归扫描 HARVEST 根)
harvest_by_name = {}
harvest_by_combo = {}
for dirpath, _, fns in os.walk(HARVEST):
    for fn in fns:
        if not fn.endswith(".ogg"):
            continue
        try:
            pkts = OB.parse_ogg_packets(open(os.path.join(dirpath, fn), "rb").read())
            info = OB.vorbis_id_info(pkts[0])
            if info and len(pkts) >= 3:
                key = (info[0], info[1])
                harvest_by_name[os.path.splitext(fn)[0]] = (pkts[0], pkts[1], pkts[2])
                harvest_by_combo.setdefault(key, (pkts[0], pkts[1], pkts[2]))
        except Exception:
            pass
print(f"harvest: {len(harvest_by_name)} by name, {len(harvest_by_combo)} combos", flush=True)

def read_streamed_data(obj, env, tt):
    r = tt.get("m_Resource")
    if r:
        src = r.get("m_Source") or ""
        m = re.search(r"archive:/CAB-([a-f0-9]+)/CAB-[a-f0-9]+\.resource", src)
        if m and hasattr(env.file, "files"):
            f = env.file.files.get("CAB-" + m.group(1) + ".resource")
            if f is not None:
                off = r.get("m_Offset", 0)
                size = r.get("m_Size", 0)
                if hasattr(f, "seek"):
                    f.seek(off)
                    return f.read(size)
                f.Position = off  # EndianBinaryReader
                return f.read_bytes(size)
        path = src.replace("archive:/", "").split("/")[-1]
        full = os.path.join(GAME, path)
        if os.path.exists(full):
            with open(full, "rb") as f:
                f.seek(r.get("m_Offset", 0))
                return f.read(r.get("m_Size", 0))
    for key in ("m_ExternalResources", "m_StreamData"):
        r2 = tt.get(key)
        if r2:
            src2 = r2.get("m_Source") or r2.get("path") or ""
            m2 = re.search(r"archive:/CAB-([a-f0-9]+)/CAB-[a-f0-9]+\.resource", src2)
            if m2 and hasattr(env.file, "files"):
                f = env.file.files.get("CAB-" + m2.group(1) + ".resource")
                if f is not None:
                    off = r2.get("m_Offset", 0)
                    size = r2.get("m_Size", 0)
                    if hasattr(f, "seek"):
                        f.seek(off)
                        return f.read(size)
                    f.Position = off
                    return f.read_bytes(size)
            full = os.path.join(GAME, os.path.basename(src2))
            if os.path.exists(full):
                with open(full, "rb") as f:
                    f.seek(r2.get("m_Offset", 0))
                    return f.read(r2.get("m_Size", 0))
    sd = tt.get("m_StreamData")
    if sd:
        path = sd.get("path") or ""
        full = os.path.join(GAME, os.path.basename(path))
        if not os.path.exists(full):
            full = path
        if os.path.exists(full):
            with open(full, "rb") as f:
                f.seek(sd.get("offset", 0))
                return f.read(sd.get("size", 0))
    return None

def main():
    global OUT, HARVEST
    for a in sys.argv[1:]:
        if a.startswith('--out='):
            OUT = a.split('=', 1)[1]
        elif a.startswith('--harvest='):
            HARVEST = a.split('=', 1)[1]
    files = load_files()
    counts = {"png": 0, "obj": 0, "ttf": 0, "mp4": 0, "txt": 0, "ogg": 0, "fail": 0}
    t0 = time.time()
    for i, (path, short) in enumerate(files):
        env = UnityPy.load(path)
        objs = list(env.objects)
        for obj in objs:
            tn = obj.type.name
            if tn not in ("Texture2D", "AudioClip", "Mesh", "Font", "VideoClip", "TextAsset"):
                continue
            try:
                outdir = os.path.join(OUT, os.path.splitext(short)[0], tn)
                name = None
                try:
                    name = getattr(obj.read(), "m_Name", None) or None
                except Exception:
                    pass
                fname = re.sub(r'[\\/:*?"<>|\x00-\x1f]', "_", (name or "")).strip()[:120] or f"{tn}_{obj.path_id}"
                os.makedirs(outdir, exist_ok=True)
                base = os.path.join(outdir, fname)
                if tn == "Texture2D":
                    img = obj.read().image
                    if img:
                        img.save(base + ".png")
                        counts["png"] += 1
                        if os.path.exists(base + ".json"):
                            os.remove(base + ".json")
                elif tn == "Mesh":
                    d = obj.read()
                    s = MeshExporter.export_mesh(d, format="obj")
                    with open(base + ".obj", "w", encoding="utf-8") as f:
                        f.write(s)
                    counts["obj"] += 1
                    if os.path.exists(base + ".json"):
                        os.remove(base + ".json")
                elif tn == "Font":
                    d = obj.read()
                    data = getattr(d, "m_FontData", None) or getattr(d, "m_FontData", b"")
                    if data:
                        with open(base + ".ttf", "wb") as f:
                            f.write(data)
                        counts["ttf"] += 1
                        if os.path.exists(base + ".json"):
                            os.remove(base + ".json")
                elif tn == "VideoClip":
                    tt = obj.read_typetree()
                    raw = read_streamed_data(obj, env, tt)
                    if raw:
                        with open(base + ".mp4", "wb") as f:
                            f.write(raw)
                        counts["mp4"] += 1
                        if os.path.exists(base + ".json"):
                            os.remove(base + ".json")
                elif tn == "TextAsset":
                    d = obj.read()
                    data = d.m_Script
                    with open(base + ".txt", "wb") as f:
                        f.write(bytes(data))
                    counts["txt"] += 1
                    if os.path.exists(base + ".json"):
                        os.remove(base + ".json")
                elif tn == "AudioClip":
                    tt = obj.read_typetree()
                    chunk = read_streamed_data(obj, env, tt)
                    if not chunk:
                        continue
                    try:
                        lay = FA.get_sample_layout(chunk)
                    except Exception:
                        continue
                    if lay["mode"] != 15:
                        continue  # IMA already handled as wav
                    key = (lay["channels"], lay["freq"])
                    hdr = harvest_by_name.get(name) or harvest_by_combo.get(key)
                    if not hdr:
                        continue
                    packets = FA.extract_vorbis_packets(chunk[lay["data_offset"]:])
                    ogg = OB.build_ogg_stream(hdr[0], hdr[1], hdr[2], packets)
                    with open(base + ".ogg", "wb") as f:
                        f.write(ogg)
                    counts["ogg"] += 1
                    for ext in (".vorbis", ".bin"):
                        if os.path.exists(base + ext):
                            os.remove(base + ext)
            except Exception as e:
                counts["fail"] += 1
                print(f"  FAIL {short} {tn} {name}: {str(e)[:80]}", flush=True)
        if (i + 1) % 10 == 0 or i == len(files) - 1:
            print(f"[{i+1}/{len(files)}] {short}: {counts} ({time.time()-t0:.0f}s)", flush=True)
    print("DONE:", counts)

if __name__ == "__main__":
    main()
