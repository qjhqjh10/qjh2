#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parse_addr_catalog.py — 解析 Addressables catalog.bin, 查 GUID → (bundle, 资源路径)
Unity ContentCatalogData 格式:
  int32 字符串数 + 字符串表 (utf8 len+bytes)
  providerIds / internalIds 字符串表
  keyData: 每项 (internalIdIndex, providerIndex, deps[], data[] 变长)
  keys: 16 字节 GUID
  keyDataStrings: 资源路径字符串表
  buckets: 每桶 (bucketSize, keyCount, (keyIndex, dataIndex)*)
用法: python parse_addr_catalog.py [GUID前缀...]   (默认查 Smite/Orbital 相关)
"""
import json
import struct
import sys

sys.stdout.reconfigure(encoding='utf-8')

CATALOG = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/catalog.bin'
BUNDLE_DIR = 'd:/2/Warhammer 40k Warpforge/Warpforge_Data/StreamingAssets/aa/StandaloneWindows64/'


def read_strings(buf, off):
    n = struct.unpack_from('<i', buf, off)[0]
    off += 4
    out = []
    for _ in range(n):
        ln = struct.unpack_from('<i', buf, off)[0]
        off += 4
        out.append(buf[off:off + ln].decode('utf-8', errors='replace'))
        off += ln
    return out, off


def parse(buf):
    off = 0
    magic = struct.unpack_from('<i', buf, off)[0]
    off += 4
    if magic > 1000000:  # 压缩标识
        # 压缩数据: (uncompressedSize, compressedSize, zlib)
        comp = struct.unpack_from('<i', buf, off)[0]
        off += 4
        raw = buf[off:off + comp]
        import zlib
        buf = zlib.decompress(raw)
        off = 0
        magic = struct.unpack_from('<i', buf, off)[0]
        off += 4
    # 字符串表 (m_Ids)
    strs, off = read_strings(buf, off)
    # providerIds
    providers, off = read_strings(buf, off)
    # internalIds
    internal_ids, off = read_strings(buf, off)
    # keyData: count + 每项 (internalIdx, providerIdx, depCount, deps, dataCount, data)
    kd = struct.unpack_from('<i', buf, off)[0]
    off += 4
    key_data = []
    for _ in range(kd):
        iid = struct.unpack_from('<i', buf, off)[0]
        off += 4
        pid = struct.unpack_from('<i', buf, off)[0]
        off += 4
        dc = struct.unpack_from('<i', buf, off)[0]
        off += 4
        deps = list(struct.unpack_from('<%di' % dc, buf, off)) if dc else []
        off += 4 * dc
        data = []
        dc2 = struct.unpack_from('<i', buf, off)[0]
        off += 4
        for _ in range(dc2):
            bl = struct.unpack_from('<i', buf, off)[0]
            off += 4
            data.append(buf[off:off + bl])
            off += bl
        key_data.append((iid, pid, deps, data))
    # keys: GUID bytes
    kc = struct.unpack_from('<i', buf, off)[0]
    off += 4
    guids = []
    for _ in range(kc):
        g = buf[off:off + 16]
        off += 16
        guids.append(g.hex())
    # keyDataStrings
    kds, off = read_strings(buf, off)
    # buckets
    bc = struct.unpack_from('<i', buf, off)[0]
    off += 4
    buckets = []
    for _ in range(bc):
        bs = struct.unpack_from('<i', buf, off)[0]
        off += 4
        kk = struct.unpack_from('<i', buf, off)[0]
        off += 4
        items = []
        for _ in range(kk):
            ki = struct.unpack_from('<i', buf, off)[0]
            off += 4
            di = struct.unpack_from('<i', buf, off)[0]
            off += 4
            items.append((ki, di))
        buckets.append((bs, items))
    return {'strs': strs, 'internal_ids': internal_ids, 'key_data': key_data,
            'guids': guids, 'key_data_strings': kds, 'buckets': buckets}


def main() -> int:
    with open(CATALOG, 'rb') as f:
        buf = f.read()
    cat = parse(buf)
    guid2data = {}
    for bs, items in cat['buckets']:
        for ki, di in items:
            if ki >= len(cat['guids']):
                continue
            g = cat['guids'][ki]
            guid2data[g] = di
    print(f'catalog: {len(cat["guids"])} keys / {len(guid2data)} 索引')
    # 查目标
    targets = sys.argv[1:] if len(sys.argv) > 1 else ['smite', 'orbital', 'bombard']
    found = 0
    for g, di in guid2data.items():
        if di >= len(cat['key_data']):
            continue
        iid, pid, deps, data = cat['key_data'][di]
        path = cat['key_data_strings'][di] if di < len(cat['key_data_strings']) else ''
        low = (g + ' ' + path).lower()
        if any(t in low for t in targets):
            bundle = cat['internal_ids'][iid] if iid < len(cat['internal_ids']) else f'idx{iid}'
            print(f'{g} | {path} | bundle={bundle}')
            found += 1
    print(f'命中 {found}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
