#!/usr/bin/env python3
"""Harvest vorbis setup headers from old oggs, rebuild the 11 vorbis FSB5 clips."""
import os, io, struct
import UnityPy
import fsb_audio as FA
import ogg_build as OB

BUNDLES = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64"
OLD = r"d:/2/Warpforge_assets/Assets"
SRC = r"d:/2/Warpforge_assets_full/bundle_soundcollection_assets_all/AudioClip"

# 1) harvest (ch, rate) -> (id, comment, setup) from old oggs
harvest = {}
for fn in os.listdir(OLD):
    if not fn.endswith(".ogg"):
        continue
    try:
        with open(os.path.join(OLD, fn), "rb") as f:
            data = f.read()
        pkts = OB.parse_ogg_packets(data)
        if len(pkts) < 3:
            continue
        info = OB.vorbis_id_info(pkts[0])
        if not info:
            continue
        key = (info[0], info[1])  # ch, rate
        if key not in harvest:
            harvest[key] = (pkts[0], pkts[1], pkts[2])
    except Exception:
        pass
print("harvested (ch,rate) combos:", sorted(harvest.keys()))

# 2) for each clip: rebuild and validate with av
import av
env = UnityPy.load(os.path.join(BUNDLES, "soundcollection_assets_all.bundle"))
res = env.file.files["CAB-62d1945b7005c115fb946f0d264a205b.resource"]
res.seek(0); resdata = res.read()
clips = [o for o in env.objects if o.type.name == "AudioClip"]

fixed, failed = [], []
for o in clips:
    tt = o.read_typetree()
    r = tt["m_Resource"]
    chunk = resdata[r["m_Offset"]:r["m_Offset"]+r["m_Size"]]
    lay = FA.get_sample_layout(chunk)
    if lay["mode"] != 15:
        continue
    name = tt.get("m_Name")
    key = (lay["channels"], lay["freq"])
    if key not in harvest:
        failed.append((name, "no harvest match"))
        continue
    id_pkt, com_pkt, setup_pkt = harvest[key]
    packets = FA.extract_vorbis_packets(chunk[lay["data_offset"]:])
    ogg = OB.build_ogg_stream(id_pkt, com_pkt, setup_pkt, packets)
    # validate with av
    try:
        c = av.open(io.BytesIO(ogg))
        dur = c.duration / av.time_base if c.duration else 0
        st = c.streams[0]
        c.close()
        ok = dur > 0.05
    except Exception:
        ok = False
    if ok:
        out = os.path.join(SRC, name + ".ogg")
        with open(out, "wb") as f:
            f.write(ogg)
        os.remove(os.path.join(SRC, name + ".vorbis"))
        fixed.append((name, round(dur, 2)))
    else:
        failed.append((name, "decode failed"))
print("\nfixed:", fixed)
print("failed:", failed)
