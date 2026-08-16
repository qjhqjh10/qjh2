#!/usr/bin/env python3
"""Full extraction of all Unity objects via UnityPy + custom FSB5 audio decoder.

Output layout: OUT/<file-stem>/<ClassName>/<name>.<ext>
- Texture2D -> png, Mesh -> obj, Font -> ttf, TextAsset -> txt, VideoClip -> mp4/raw
- AudioClip -> ogg/wav via UnityPy export; streamed FSB5 -> IMA decode to wav,
  Vorbis packets -> .vorbis raw; other -> .bin
- everything else (MonoBehaviour, GameObject, Material, AnimationClip, Shader,
  Sprite, ...) -> typetree JSON dump
"""
import os, sys, json, base64, re, time, struct

GAME = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data"
BUNDLES = os.path.join(GAME, "StreamingAssets", "aa", "StandaloneWindows64")
OUT = r"d:/2/Warpforge_assets_full"
SAFE = re.compile(r'[\\/:*?"<>|\x00-\x1f]')
import fsb_audio as FA

def safe_name(name, fallback):
    name = SAFE.sub("_", (name or "").strip())
    return name[:120] or fallback

def load_files():
    files = []
    for fn in sorted(os.listdir(GAME)):
        if fn.endswith((".assets", ".resource")) or fn.startswith(("globalgamemanagers", "level0", "level1", "sharedassets")):
            files.append((os.path.join(GAME, fn), fn))
    for fn in sorted(os.listdir(BUNDLES)):
        if fn.endswith(".bundle"):
            files.append((os.path.join(BUNDLES, fn), "bundle_" + fn))
    return files

def read_streamed_data(obj, env, tt):
    """Read streamed audio/video data: embedded resource or external resS."""
    r = tt.get("m_Resource")
    if r:
        src = r.get("m_Source") or ""
        m = re.search(r"archive:/CAB-([a-f0-9]+)/CAB-[a-f0-9]+\.resource", src)
        if m:
            name = "CAB-" + m.group(1) + ".resource"
            f = env.file.files.get(name) if hasattr(env.file, "files") else None
            if f is not None:
                off, size = r.get("m_Offset", 0), r.get("m_Size", 0)
                # EndianBinaryReader 无 seek: 用 Position/read_bytes 兼容
                if hasattr(f, "seek"):
                    f.seek(off)
                    return f.read(size)
                f.Position = off
                return f.read_bytes(size)
        # external file path
        path = src.replace("archive:/", "").split("/")[-1]
        full = os.path.join(GAME, path)
        if os.path.exists(full):
            with open(full, "rb") as f:
                f.seek(r.get("m_Offset", 0))
                return f.read(r.get("m_Size", 0))
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

def handle_audio(obj, env, tt, path_stem):
    """Export audio: embedded (m_AudioData) -> streamed FSB5 -> UnityPy direct fallback."""
    # 1) 内嵌音频 (m_AudioData): 音效库等无 m_Resource 的 AudioClip
    raw = tt.get("m_AudioData")
    if isinstance(raw, (bytes, bytearray)) and raw:
        try:
            lay = FA.get_sample_layout(raw)
            if lay:
                data = raw[lay["data_offset"]:]
                if lay["mode"] == 7:  # IMAADPCM
                    pcm, n = FA.decode_ima(data, lay["channels"], lay["n_samples"])
                    with open(path_stem + ".wav", "wb") as f:
                        f.write(FA.pcm_to_wav(pcm, lay["channels"], lay["freq"]))
                    return "wav"
                elif lay["mode"] == 15:  # VORBIS packets
                    pkts = FA.extract_vorbis_packets(data)
                    with open(path_stem + ".vorbis", "wb") as f:
                        f.write(b"".join(pkts))
                    return "vorbis"
                with open(path_stem + ".bin", "wb") as f:
                    f.write(raw)
                return "bin"
        except Exception:
            pass
        with open(path_stem + ".bin", "wb") as f:
            f.write(raw)
        return "bin"
    try:
        data = obj.export()
        if data:
            with open(path_stem + ".ogg", "wb") as f:
                f.write(data)
            return "ogg"
    except Exception:
        pass
    chunk = read_streamed_data(obj, env, tt)
    if not chunk:
        try:
            data = obj.export()
            if data:
                with open(path_stem + ".wav", "wb") as f:
                    f.write(data)
                return "wav"
        except Exception:
            pass
        return None
    try:
        lay = FA.get_sample_layout(chunk)
    except Exception:
        with open(path_stem + ".bin", "wb") as f:
            f.write(chunk)
        return "bin"
    mode = lay["mode"]
    data = chunk[lay["data_offset"]:]
    if mode == 7:  # IMAADPCM
        pcm, n = FA.decode_ima(data, lay["channels"], lay["n_samples"])
        with open(path_stem + ".wav", "wb") as f:
            f.write(FA.pcm_to_wav(pcm, lay["channels"], lay["freq"]))
        return "wav"
    elif mode == 15:  # VORBIS - packets only (no native libvorbis available)
        pkts = FA.extract_vorbis_packets(data)
        with open(path_stem + ".vorbis", "wb") as f:
            f.write(b"".join(pkts))
        return "vorbis"
    else:
        with open(path_stem + ".bin", "wb") as f:
            f.write(data)
        return "bin"

def export_obj(obj, path):
    try:
        data = obj.export()
        if not data:
            return None
        with open(path, "wb") as f:
            f.write(data)
        return os.path.splitext(path)[1].lstrip(".")
    except Exception:
        return None

def json_default(o):
    if isinstance(o, bytes):
        return {"$bytes": base64.b64encode(o).decode("ascii")}
    return str(o)

def main():
    global OUT
    for a in sys.argv[1:]:
        if a.startswith('--out='):
            OUT = a.split('=', 1)[1]
            break
    files = load_files()
    print(f"{len(files)} files to process", flush=True)
    stats = {}
    started = time.time()
    for i, (path, short) in enumerate(files):
        t0 = time.time()
        try:
            import UnityPy
            env = UnityPy.load(path)
            objs = list(env.objects)
        except Exception as e:
            print(f"[{i+1}/{len(files)}] {short}: LOAD ERROR {e}", flush=True)
            continue
        outdir = os.path.join(OUT, os.path.splitext(short)[0])
        counts = {"exported": 0, "json": 0, "fail": 0}
        for obj in objs:
            tn = obj.type.name
            try:
                name = None
                if tn in ("MonoBehaviour", "GameObject", "Sprite", "Texture2D", "AudioClip", "Mesh"):
                    try:
                        name = getattr(obj.read(), "m_Name", None) or None
                    except Exception:
                        name = None
                fname = safe_name(name, f"{tn}_{obj.path_id}")
                cls_dir = os.path.join(outdir, tn)
                os.makedirs(cls_dir, exist_ok=True)
                if tn == "AudioClip":
                    tt = obj.read_typetree()   # 必须先取本对象的 typetree (勿用残留值)
                    handle_audio(obj, env, tt, os.path.join(cls_dir, fname))
                    counts["exported"] += 1
                    continue  # 音频已有实体文件 (wav/ogg/vorbis/bin), 不转 JSON
                if tn in ("Texture2D", "Mesh", "Font", "TextAsset", "VideoClip"):
                    continue  # 由 fix_exports 导出
                tt = obj.read_typetree()
                jpath = os.path.join(cls_dir, fname + ".json")
                if os.path.exists(jpath):
                    jpath = os.path.join(cls_dir, f"{fname}_{obj.path_id}.json")
                with open(jpath, "w", encoding="utf-8") as f:
                    json.dump(tt, f, ensure_ascii=False, indent=1, default=json_default)
                counts["json"] += 1
            except Exception:
                counts["fail"] += 1
        dt = time.time() - t0
        stats[short] = {"objects": len(objs), "exported": counts["exported"],
                        "json": counts["json"], "fail": counts["fail"], "secs": round(dt, 1)}
        print(f"[{i+1}/{len(files)}] {short}: obj={len(objs)} exp={counts['exported']} "
              f"json={counts['json']} fail={counts['fail']} ({dt:.1f}s)", flush=True)
    with open(os.path.join(OUT, "_stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    print(f"ALL DONE in {time.time()-started:.0f}s", flush=True)

if __name__ == "__main__":
    main()
