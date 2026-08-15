#!/usr/bin/env python3
"""Validate the FSB5 IMA decoder: decode clips and check waveform statistics."""
import os, struct, io, wave
import UnityPy
import fsb_audio as FA

BUNDLES = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64"

env = UnityPy.load(os.path.join(BUNDLES, "soundcollection_assets_all.bundle"))
res = env.file.files["CAB-62d1945b7005c115fb946f0d264a205b.resource"]
res.seek(0)
resdata = res.read()
clips = [o for o in env.objects if o.type.name == "AudioClip"]

def score(pcm, ch, freq, label):
    n = len(pcm) // (2 * ch)
    s = struct.unpack(f"<{n*ch}h", pcm)
    mono = s[0::ch]
    sat = sum(1 for x in mono if abs(x) >= 32767) / n
    diff_e = sum((mono[i] - mono[i-1]) ** 2 for i in range(1, n, 4))
    tot_e = sum(x * x for x in mono[::4]) or 1
    rms = (sum(x * x for x in mono) / n) ** 0.5
    print(f"  {label}: n={n} dur={n/freq:.2f}s rms={rms:.0f} sat={sat:.2%} hf={diff_e/(2*tot_e):.3f}")

for o in clips[:6]:
    tt = o.read_typetree()
    r = tt["m_Resource"]
    chunk = resdata[r["m_Offset"]:r["m_Offset"] + r["m_Size"]]
    lay = FA.get_sample_layout(chunk)
    pcm, n = FA.decode_ima(chunk[lay["data_offset"]:], lay["channels"], lay["n_samples"])
    score(pcm, lay["channels"], lay["freq"], tt.get("m_Name"))
