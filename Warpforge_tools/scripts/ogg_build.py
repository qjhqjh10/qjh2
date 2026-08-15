#!/usr/bin/env python3
"""Pure-python OGG page parsing/building + vorbis packet extraction from FSB5."""
import struct

# ---- ogg page CRC (poly 0x04C11DB7, init 0, no reflection, no final xor) ----
def _make_crc_table():
    tbl = []
    for i in range(256):
        r = i << 24
        for _ in range(8):
            r = ((r << 1) ^ 0x04C11DB7) & 0xFFFFFFFF if (r & 0x80000000) else (r << 1) & 0xFFFFFFFF
        tbl.append(r)
    return tbl
CRC_TABLE = _make_crc_table()

def ogg_crc(data):
    crc = 0
    for b in data:
        crc = ((crc << 8) & 0xFFFFFFFF) ^ CRC_TABLE[((crc >> 24) & 0xFF) ^ b]
    return crc & 0xFFFFFFFF

def parse_ogg_packets(data):
    """Split an ogg stream into raw packets (reassembled across pages)."""
    packets, cur = [], bytearray()
    pos = 0
    while pos + 27 <= len(data):
        if data[pos:pos + 4] != b"OggS":
            break
        seg_count = data[pos + 26]
        segs = data[pos + 27:pos + 27 + seg_count]
        body = data[pos + 27 + seg_count:]
        off = 0
        for s in segs:
            cur += body[off:off + s]
            off += s
            if s < 255:
                packets.append(bytes(cur))
                cur = bytearray()
        pos += 27 + seg_count + off
    if cur:
        packets.append(bytes(cur))
    return packets

def vorbis_id_info(pkt):
    """Parse vorbis identification header: (channels, rate, blocksize_short_exp, blocksize_long_exp)."""
    if pkt[0] != 1 or pkt[1:7] != b"vorbis":
        return None
    ch = pkt[11]
    rate = struct.unpack_from("<I", pkt, 12)[0]
    bs_short_exp = pkt[28] & 0xF
    bs_long_exp = (pkt[28] >> 4) & 0xF
    return ch, rate, bs_short_exp, bs_long_exp

def build_vorbis_id(channels, rate, bs_short_exp, bs_long_exp):
    """Build vorbis identification header packet."""
    p = bytearray()
    p.append(1)
    p += b"vorbis"
    p += struct.pack("<I", 0)  # version
    p.append(channels)
    p += struct.pack("<I", rate)
    p += struct.pack("<i", -1)  # bitrate max
    p += struct.pack("<i", 0)   # bitrate nominal
    p += struct.pack("<i", -1)  # bitrate min
    p.append((bs_long_exp << 4) | bs_short_exp)
    p.append(1)  # framing bit
    return bytes(p)

def build_vorbis_comment(vendor=b"Xiph.Org libVorbis I 20200704"):
    p = bytearray()
    p += struct.pack("<I", len(vendor)) + vendor
    p += struct.pack("<I", 0)  # 0 comments
    p.append(1)  # framing bit
    return bytes(p)

def packets_to_granulepos(packets, bs_short, bs_long, modebits=1):
    """Estimate granulepos per packet (libvorbis: mode 0 = short, mode 1 = long)."""
    gp = 0
    prev = 0
    out = []
    for pkt in packets:
        mode = pkt[0] & ((1 << modebits) - 1) if modebits else 0
        bs = bs_short if mode == 0 else bs_long
        if prev:
            gp += (bs + prev) // 4
        out.append(gp)
        prev = bs
    return out

def make_ogg_page(packets, serial, page_start, granulepos=None, bos=False, eos=False):
    """Pack consecutive packets into one page (headers + body + CRC)."""
    if granulepos is None:
        granulepos = [0] * len(packets)
    body = bytearray()
    segs = []
    for p in packets:
        rem = p
        while len(rem) >= 255:
            segs.append(255)
            body += rem[:255]
            rem = rem[255:]
        segs.append(len(rem))
        body += rem
    header = bytearray(b"OggS")
    header += struct.pack("<B", 0)          # version
    header.append((1 if bos else 0) << 1 | (1 if eos else 0) << 2)  # BOS bit1, EOS bit2
    header += struct.pack("<Q", granulepos[-1] if granulepos else 0)
    header += struct.pack("<I", serial)
    header += struct.pack("<I", page_start)
    header += struct.pack("<I", 0)          # crc placeholder
    header.append(len(segs))
    header += bytes(segs)
    page = header + body
    crc = ogg_crc(page)
    page[22:26] = struct.pack("<I", crc)
    return bytes(page)

def build_ogg_stream(id_pkt, comment_pkt, setup_pkt, audio_packets, serial=1):
    """Build a complete ogg vorbis stream."""
    pages = []
    pageno = 0
    # headers: id page (bos), comment+setup page
    pages.append(make_ogg_page([id_pkt], serial, pageno, bos=True)); pageno += 1
    pages.append(make_ogg_page([comment_pkt, setup_pkt], serial, pageno)); pageno += 1
    info = vorbis_id_info(id_pkt)
    bs_short = 1 << info[2]
    bs_long = 1 << info[3]
    gps = packets_to_granulepos(audio_packets, bs_short, bs_long)
    # pack audio packets into pages (max 250 segments and 65000 body bytes per page)
    chunk, segs_n = [], 0
    chunk_len = 0
    for i, p in enumerate(audio_packets):
        need = len(p) // 255 + 1
        if chunk and (segs_n + need > 250 or chunk_len + len(p) + 1 > 65000):
            pages.append(make_ogg_page(chunk, serial, pageno, granulepos=gps[:len(chunk)])); pageno += 1
            chunk, segs_n, chunk_len = [], 0, 0
        chunk.append(p)
        segs_n += need
        chunk_len += len(p) + 1
    if chunk:
        pages.append(make_ogg_page(chunk, serial, pageno, granulepos=gps[:len(chunk)], eos=True))
    return b"".join(pages)

def vorbis_sample_from_fsb5(data):
    """u16-prefixed vorbis packets from FSB5 vorbis sample data."""
    import fsb_audio as FA
    return FA.extract_vorbis_packets(data)
