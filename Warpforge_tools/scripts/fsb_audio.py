#!/usr/bin/env python3
"""FSB5 audio extraction: IMA-ADPCM decode + vorbis packet extraction.

FSB5 IMA-ADPCM layout (per fsbext source: wBlockAlign = 36 * channels):
  channel header:  u16 initial sample (LE, signed), u8 step index, u8 reserved
  blocks of 36 bytes: u16 initial sample, u8 step index, u8 reserved, 32 bytes
  (64 samples, 2 samples/byte, LOW nibble first)
  multi-channel: blocks interleaved per channel (36 bytes each, alternating)
"""
import io, struct

IMA_STEP = [7,8,9,10,11,12,13,14,16,17,19,21,23,25,28,31,34,37,41,45,50,55,60,66,
            73,80,88,97,107,118,130,143,157,173,190,209,230,253,279,307,337,371,
            408,449,494,544,598,658,724,796,876,963,1060,1166,1282,1411,1552,1707,
            1878,2066,2272,2499,2749,3024,3327,3660,4026,4428,4871,5358,5894,6484,
            7132,7845,8630,9493,10442,11487,12635,13899,15289,16818,18500,20350,
            22385,24623,27086,29794,32767]
IMA_INDEX = [-1,-1,-1,-1,2,4,6,8]
FREQ_VALUES = [0, 8000, 11000, 11025, 16000, 22050, 24000, 32000, 44100, 48000]

class FSB5Error(Exception):
    pass

def parse_fsb5(data):
    """Minimal FSB5 header parse (matches fsbext's fr_FSOUND_FSB_HEADER_FSB5)."""
    if data[:4] != b"FSB5":
        raise FSB5Error(f"bad magic {data[:4]!r}")
    version = struct.unpack_from("<I", data, 4)[0]
    numsamples = struct.unpack_from("<I", data, 8)[0]
    shdrsize = struct.unpack_from("<I", data, 12)[0]
    namesize = struct.unpack_from("<I", data, 16)[0]
    datasize = struct.unpack_from("<I", data, 20)[0]
    mode = struct.unpack_from("<I", data, 24)[0]
    return {"version": version, "num_samples": numsamples,
            "shdrsize": shdrsize, "namesize": namesize,
            "datasize": datasize, "mode": mode}

def _data_region_start(h):
    """Base FSB5 header is 60 bytes (64 if version==0); sample headers follow."""
    return 60 + (4 if h["version"] == 0 else 0) + h["shdrsize"] + h["namesize"]

def get_sample_layout(data, idx=0):
    """Parse the idx-th sample's 8-byte packed header + metadata chunks."""
    h = parse_fsb5(data)
    table_off = 60 + (4 if h["version"] == 0 else 0) + idx * 8
    raw = struct.unpack_from("<Q", data, table_off)[0]
    next_chunk = raw & 1
    freq_idx = (raw >> 1) & 0xF
    channels = ((raw >> 5) & 1) + 1
    data_offset = ((raw >> 6) & 0xFFFFFFF) * 16
    n_samples = (raw >> 34) & 0x3FFFFFFF
    freq = FREQ_VALUES[freq_idx] if freq_idx < len(FREQ_VALUES) else 44100
    # metadata chunks (FSB5 extended sample header)
    pos = table_off + 8
    while next_chunk:
        word = struct.unpack_from("<I", data, pos)[0]
        pos += 4
        next_chunk = word & 1
        size = (word >> 1) & 0xFFFFFF
        ctype = (word >> 25) & 0x7F
        if ctype == 2 and size >= 4:  # FREQUENCY
            freq = struct.unpack_from("<I", data, pos)[0]
        pos += size
    data_start = 60 + (4 if h["version"] == 0 else 0) + h["shdrsize"] + h["namesize"]
    return {"next_chunk": next_chunk, "freq": freq, "channels": channels,
            "data_offset": data_offset + data_start, "n_samples": n_samples,
            "mode": h["mode"]}

def decode_ima(data_bytes, channels, n_samples):
    """Decode FSB5 IMA-ADPCM to 16-bit PCM interleaved (vgmstream layout).

    Per channel per block (0x24 = 36 bytes):
      hist s16le at 0 (2 bytes per channel, interleaved for stereo)
      step u8 + reserved u8 at 2*channels (interleaved)
      nibbles from 4*channels, 2 samples/byte, low nibble first
    Samples per block: 64 = 1 header sample + 63 nibble samples (last nibble skipped).
    """
    pcm = bytearray(n_samples * channels * 2)
    block = 0x24 * channels
    block_samples = 64
    n_blocks = len(data_bytes) // block
    hist = [0] * channels
    step = [0] * channels
    out = 0
    for b in range(n_blocks):
        base = b * block
        for ch in range(channels):
            hist[ch] = struct.unpack_from("<h", data_bytes, base + 2 * ch)[0]
            step[ch] = data_bytes[base + 2 * channels + 2 * ch]
            if step[ch] < 0:
                step[ch] = 0
            elif step[ch] > 88:
                step[ch] = 88
        # header samples
        for ch in range(channels):
            if out < n_samples:
                pcm[(out * channels + ch) * 2:(out * channels + ch) * 2 + 2] = struct.pack("<h", hist[ch])
        out += 1
        # 63 nibble samples
        for i in range(1, block_samples):
            for ch in range(channels):
                byte_off = base + 4 * channels + 2 * ch + ((i - 1) // 4) * 2 * channels + ((i - 1) % 4) // 2
                byte = data_bytes[byte_off]
                nib = byte >> 4 if (i - 1) & 1 else byte & 0xF
                st = IMA_STEP[step[ch]]
                diff = st >> 3
                if nib & 1:
                    diff += st >> 2
                if nib & 2:
                    diff += st >> 1
                if nib & 4:
                    diff += st
                hist[ch] += -diff if (nib & 8) else diff
                if hist[ch] > 32767:
                    hist[ch] = 32767
                elif hist[ch] < -32768:
                    hist[ch] = -32768
                step[ch] += IMA_INDEX[nib & 7]
                if step[ch] < 0:
                    step[ch] = 0
                elif step[ch] > 88:
                    step[ch] = 88
                if out < n_samples:
                    pcm[(out * channels + ch) * 2:(out * channels + ch) * 2 + 2] = struct.pack("<h", hist[ch])
            out += 1
    return bytes(pcm), min(out, n_samples)

def extract_vorbis_packets(data):
    """Extract u16-size-prefixed vorbis packets from FSB5 vorbis sample data."""
    packets = []
    pos = 0
    while pos + 2 <= len(data):
        size = struct.unpack_from("<H", data, pos)[0]
        pos += 2
        if size == 0 or pos + size > len(data):
            break
        packets.append(data[pos:pos + size])
        pos += size
    return packets

def pcm_to_wav(pcm, channels, freq):
    import wave
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(channels)
        w.setsampwidth(2)
        w.setframerate(freq)
        w.writeframes(pcm)
    return buf.getvalue()
