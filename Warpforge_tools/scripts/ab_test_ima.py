#!/usr/bin/env python3
"""A/B test IMA decode variants (nibble order, block header usage) to confirm decoder config."""
import struct
import UnityPy
import fsb_audio as FA

BUNDLES = r"d:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64"

env = UnityPy.load(BUNDLES + "/soundcollection_assets_all.bundle")
res = env.file.files["CAB-62d1945b7005c115fb946f0d264a205b.resource"]
res.seek(0)
resdata = res.read()
clips = [o for o in env.objects if o.type.name == "AudioClip"]

def decode_variant(data_bytes, channels, n_samples, nibble_hi_first, use_block_headers):
    pcm = bytearray(n_samples * channels * 2)
    pred = [0] * channels
    step = [0] * channels
    pos = 0
    for ch in range(channels):
        pred[ch] = struct.unpack_from("<h", data_bytes, pos)[0]
        step[ch] = min(data_bytes[pos + 2], 88)
        pos += 4
    block = 36 * channels
    per_ch = 36
    n_blocks = (len(data_bytes) - pos) // block
    out = 0
    for b in range(n_blocks):
        for ch in range(channels):
            base = pos + b * block + ch * per_ch
            if use_block_headers:
                pred[ch] = struct.unpack_from("<h", data_bytes, base)[0]
                step[ch] = min(data_bytes[base + 2], 88)
            d = base + 4
            for i in range(64):
                nib = data_bytes[d + (i >> 1)]
                if nibble_hi_first:
                    nib = (nib >> 4) if (i & 1) == 0 else (nib & 0xF)
                else:
                    nib = (nib & 0xF) if (i & 1) == 0 else (nib >> 4)
                st = FA.IMA_STEP[step[ch]]
                diff = st >> 3
                if nib & 1: diff += st >> 2
                if nib & 2: diff += st >> 1
                if nib & 4: diff += st
                pred[ch] += -diff if (nib & 8) else diff
                pred[ch] = max(-32768, min(32767, pred[ch]))
                step[ch] = max(0, min(88, step[ch] + FA.IMA_INDEX[nib & 7]))
                if out < n_samples:
                    pcm[(out * channels + ch) * 2:(out * channels + ch) * 2 + 2] = struct.pack("<h", pred[ch])
        out += 64
    return bytes(pcm)

def score(pcm, label):
    n = len(pcm) // 2
    if n == 0:
        return
    s = struct.unpack(f"<{n}h", pcm)
    sat = sum(1 for x in s if abs(x) >= 32767) / n
    diff_e = sum((s[i] - s[i-1]) ** 2 for i in range(1, n, 8))
    tot_e = sum(x * x for x in s[::8]) or 1
    rms = (sum(x * x for x in s) / n) ** 0.5
    print(f"  {label}: n={n} rms={rms:.0f} sat={sat:.2%} hf={diff_e/(2*tot_e):.3f}")

for o in clips[:3] + clips[20:22]:
    tt = o.read_typetree()
    r = tt["m_Resource"]
    chunk = resdata[r["m_Offset"]:r["m_Offset"]+r["m_Size"]]
    lay = FA.get_sample_layout(chunk)
    data = chunk[lay["data_offset"]:]
    print(f"=== {tt.get('m_Name')} (mode={lay['mode']}) ===")
    for hi in (False, True):
        for bh in (True, False):
            pcm = decode_variant(data, lay["channels"], lay["n_samples"], hi, bh)
            score(pcm, f"hi_first={hi} block_headers={bh}")
