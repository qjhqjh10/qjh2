#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui_spec_audit.py — 界面规格审计器 (说明书 → 权威期望表 → 项目代码对照)

做什么: 输入界面根 GO 名 → ①从原始 Unity JSON 自动构建全元素规格表
       (Godot 绝对坐标/尺寸/贴图/文字/active, 坐标算法=chain_rect.py 同源)
       ②扫描 D:/warpforge 代码中该元素名的出现位置
       ③输出 命中 ✅ / 未命中 ⚠️ 清单 → 供 ui-spec-auditor 子代理逐项判断修复

用法:
  py312 ui_spec_audit.py <界面根GO名> [--src 解包目录] [--proj d:/warpforge]
                         [--out 输出.md] [--depth N] [--json 输出.json]

说明:
  - 坐标=chain_rect.py v2 算法 (y翻转/pivot修正/锚点中心/父链累加/rt_scale_map), 与权威工具一致
  - 子代理/人不需再手动换算坐标 — 机器解析不打盹 (19 轮遗漏全部发生在人工环节)
  - "未命中"≠缺失 (动态生成/命名不同/容器遍历都可能), 标记供人工判断
  - 权威=原始 Unity JSON; 本工具输出是换算产物, 冲突时以原始 JSON 为准
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DEFAULT_SRC = 'd:/2/解包整理/03_界面UI/菜单'
DEFAULT_PROJ = 'd:/warpforge'
W, H = 1920.0, 1080.0
SCALE_MAP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              '..', 'data', 'ui_layout', 'rt_scale_map.json')


def build_index(src):
    """全量索引 (GO/RT/Transform/MonoBehaviour/Sprite/Texture2D), pid 全局唯一"""
    idx = {}
    name_idx = {}
    tr_by_go = {}
    rt_scale = {}
    if os.path.exists(SCALE_MAP_PATH):
        try:
            rt_scale = json.load(open(SCALE_MAP_PATH, encoding='utf-8'))
        except Exception:
            rt_scale = {}
    for t in ['GameObject', 'RectTransform', 'Transform', 'MonoBehaviour', 'Sprite', 'Texture2D']:
        td = os.path.join(src, t)
        if not os.path.isdir(td):
            continue
        for fn in os.listdir(td):
            if not fn.endswith('.json'):
                continue
            m = fn.rsplit('_', 1)
            pid = None
            if len(m) == 2 and m[1].replace('.json', '').lstrip('-').isdigit():
                pid = int(m[1].replace('.json', ''))
            try:
                d = json.load(open(os.path.join(td, fn), encoding='utf-8'))
            except Exception:
                continue
            if pid is None or pid in idx:
                continue
            idx[pid] = {'type': t, 'path': os.path.join(td, fn), 'data': d}
            if t == 'GameObject':
                nm = d.get('m_Name')
                if isinstance(nm, str) and nm:
                    name_idx.setdefault(nm, []).append(pid)
            elif t == 'Transform':
                gop = d.get('m_GameObject', {}).get('m_PathID')
                if gop is not None:
                    tr_by_go.setdefault(gop, []).append(d)
    return idx, name_idx, tr_by_go, rt_scale


class Audit:
    def __init__(self, src, depth=99):
        self.idx, self.name_idx, self.tr_by_go, self.rt_scale = build_index(src)
        self.depth = depth
        self.rows = []          # [{name,pid,active,rect,sprite,text,color,path}]
        self.visited = set()

    def go_rt(self, goid):
        d = self.idx.get(goid, {}).get('data')
        if not d:
            return None
        for c in d.get('m_Component', []):
            pid = c.get('component', {}).get('m_PathID')
            if pid in self.idx and self.idx[pid]['type'] == 'RectTransform':
                return pid
        return None

    def go_scale(self, goid):
        for tr in self.tr_by_go.get(goid, []):
            sc = tr.get('m_LocalScale') or {}
            sx = sc.get('x', 1) or 1
            sy = sc.get('y', sx) or sx
            if sx != 1 or sy != 1:
                return (sx, sy)
        return (1.0, 1.0)

    def rt_rect(self, rtid):
        """chain_rect.py v2 同源算法 (勿改 — 与权威工具保持逐行一致)"""
        rt = self.idx.get(rtid, {}).get('data')
        if rt is None:
            return None
        fid = rt.get('m_Father', {}).get('m_PathID')
        if fid is not None and fid in self.idx and self.idx[fid]['type'] == 'RectTransform':
            par = self.rt_rect(fid)
            if par is None:
                return None
            ps, pl, psc = par['s'], par['l'], par['scale']
            ppvx, ppvy = par['pivot']
        else:
            amn0 = rt.get('m_AnchorMin') or {}
            amx0 = rt.get('m_AnchorMax') or {}
            ap0 = rt.get('m_AnchoredPosition') or {}
            sd0 = rt.get('m_SizeDelta') or {}
            if all(v == 0 for dct in (amn0, amx0, ap0, sd0) for v in dct.values()):
                return {'s': (0.0, 0.0, W, H), 'l': (0.0, 0.0, W, H),
                        'scale': 1.0, 'pivot': (0.5, 0.5)}
            ps, pl, psc, ppvx, ppvy = (0.0, 0.0, W, H), (0.0, 0.0, W, H), 1.0, 0.5, 0.5
        pw, ph = pl[2] - pl[0], pl[3] - pl[1]
        amn = rt.get('m_AnchorMin') or {}
        amx = rt.get('m_AnchorMax') or {}
        ap = rt.get('m_AnchoredPosition') or {}
        sd = rt.get('m_SizeDelta') or {}
        pv = rt.get('m_Pivot') or {}
        ax0, ay0 = amn.get('x', 0), amn.get('y', 0)
        ax1, ay1 = amx.get('x', ax0), amx.get('y', ay0)
        apx, apy = ap.get('x', 0), ap.get('y', 0)
        sdx, sdy = sd.get('x', 0), sd.get('y', 0)
        pvx, pvy = pv.get('x', 0.5), pv.get('y', 0.5)
        amin_x = pl[0] + ax0 * pw
        amax_x = pl[0] + ax1 * pw
        amin_gy = pl[1] + (1.0 - ay0) * ph
        amax_gy = pl[1] + (1.0 - ay1) * ph
        lx1 = amin_x + (apx - pvx * sdx)
        lx2 = amax_x + (apx + (1.0 - pvx) * sdx)
        ly1 = amax_gy - (apy + (1.0 - pvy) * sdy)
        ly2 = amin_gy - (apy - pvy * sdy)
        ppiv_sx = ps[0] + (ps[2] - ps[0]) * ppvx
        ppiv_sy = ps[1] + (ps[3] - ps[1]) * ppvy
        ppiv_lx = pl[0] + (pl[2] - pl[0]) * ppvx
        ppiv_ly = pl[1] + (pl[3] - pl[1]) * ppvy
        sx1 = ppiv_sx + (lx1 - ppiv_lx) * psc
        sy1 = ppiv_sy + (ly1 - ppiv_ly) * psc
        sx2 = ppiv_sx + (lx2 - ppiv_lx) * psc
        sy2 = ppiv_sy + (ly2 - ppiv_ly) * psc
        scx, scy = 1.0, 1.0
        smap = self.rt_scale.get(str(rtid))
        if smap:
            scx = float(smap.get('x', 1))
            scy = float(smap.get('y', scx))
        else:
            scx, scy = self.go_scale(rt.get('m_GameObject', {}).get('m_PathID'))
        if scx != 1.0 or scy != 1.0:
            spx = sx1 + (sx2 - sx1) * pvx
            spy = sy1 + (sy2 - sy1) * pvy
            sx1 = spx + (sx1 - spx) * scx
            sx2 = spx + (sx2 - spx) * scx
            sy1 = spy + (sy1 - spy) * scy
            sy2 = spy + (sy2 - spy) * scy
        return {'s': (sx1, sy1, sx2, sy2), 'l': (lx1, ly1, lx2, ly2),
                'scale': psc * scx, 'pivot': (pvx, pvy)}

    # ---- 组件摘要 ----
    def comp_summary(self, goid):
        d = self.idx.get(goid, {}).get('data')
        if not d:
            return None
        sprite, text, color, active = '', '', '', None
        font_size = None
        for c in d.get('m_Component', []):
            pid = c.get('component', {}).get('m_PathID')
            e = self.idx.get(pid)
            if not e:
                continue
            if e['type'] == 'MonoBehaviour':
                mb = e['data']
                if isinstance(mb, dict):
                    sp = mb.get('m_Sprite')
                    if isinstance(sp, dict) and sp.get('m_PathID'):
                        se = self.idx.get(sp['m_PathID'])
                        if se and se['type'] == 'Sprite':
                            sprite = str(se['data'].get('m_Name', '')) or sprite
                    t = mb.get('m_text')
                    if isinstance(t, str) and t.strip():
                        text = t
                    co = mb.get('m_Color')
                    if isinstance(co, dict) and color is None:
                        color = co
                    fs = mb.get('m_fontSize')
                    if fs is None:
                        fs = mb.get('m_fontSizeFloat')
                    if isinstance(fs, (int, float)) and fs > 0:
                        font_size = float(fs)
        return {'sprite': sprite, 'text': text, 'color': color,
                'active': bool(d.get('m_IsActive', True)), 'font_size': font_size}

    def walk(self, goid, indent=0, out=None):
        if goid in self.visited or indent > self.depth:
            return
        self.visited.add(goid)
        d = self.idx.get(goid, {}).get('data')
        if not d:
            return
        name = str(d.get('m_Name', '?'))
        rtid = self.go_rt(goid)
        rect = self.rt_rect(rtid) if rtid else None
        cs = self.comp_summary(goid)
        row = {'name': name, 'pid': goid, 'active': cs['active'],
               'sprite': cs['sprite'], 'text': cs['text'],
               'font_size': cs['font_size'],
               'rect': rect['s'] if rect else None, 'depth': indent}
        self.rows.append(row)
        if out is not None:
            out.write('  ' * indent + self.fmt_row(row) + '\n')
        if not rtid:
            return
        rt = self.idx[rtid]['data']
        for ch in rt.get('m_Children', []):
            cpid = ch.get('m_PathID')
            ce = self.idx.get(cpid)
            if ce and ce['type'] == 'RectTransform':
                cgoid = ce['data'].get('m_GameObject', {}).get('m_PathID')
                self.walk(cgoid, indent + 1, out)

    @staticmethod
    def fmt_row(r):
        tags = []
        if not r['active']:
            tags.append('inactive')
        if r['sprite']:
            tags.append('sprite=' + r['sprite'])
        if r['text']:
            tags.append('txt=' + r['text'][:40].replace('\n', '\\n'))
        if r['rect']:
            x1, y1, x2, y2 = [round(v, 1) for v in r['rect']]
            tags.append('godot(x%.1f y%.1f w%.1f h%.1f)' % (x1, y1, x2 - x1, y2 - y1))
        return '%s [%s]' % (r['name'], ' '.join(tags)) if tags else r['name']


from io import StringIO
from datetime import datetime


def fmt_row(r):
    tags = []
    if not r['active']:
        tags.append('inactive')
    if r['sprite']:
        tags.append('sprite=' + r['sprite'])
    if r['text']:
        tags.append('txt=' + r['text'][:40].replace('\n', '\\n'))
    if r['rect']:
        x1, y1, x2, y2 = [round(v, 1) for v in r['rect']]
        tags.append('godot(x%.1f y%.1f w%.1f h%.1f)' % (x1, y1, x2 - x1, y2 - y1))
    return '%s [%s]' % (r['name'], ' '.join(tags)) if tags else r['name']


def walk_tree(aud, goid, buf, indent=0):
    """返回行数; 树输出到 buf (缩进)"""
    if goid in aud.visited or indent > aud.depth:
        return 0
    aud.visited.add(goid)
    d = aud.idx.get(goid, {}).get('data')
    if not d:
        return 0
    rtid = aud.go_rt(goid)
    rect = aud.rt_rect(rtid) if rtid else None
    cs = aud.comp_summary(goid)
    row = {'name': str(d.get('m_Name', '?')), 'pid': goid, 'active': cs['active'],
           'sprite': cs['sprite'], 'text': cs['text'], 'font_size': cs['font_size'],
           'rect': rect['s'] if rect else None, 'depth': indent}
    aud.rows.append(row)
    buf.write('  ' * indent + fmt_row(row) + '\n')
    n = 1
    if not rtid:
        return n
    rt = aud.idx[rtid]['data']
    for ch in rt.get('m_Children', []) or []:
        cpid = ch.get('m_PathID')
        ce = aud.idx.get(cpid)
        if ce and ce['type'] == 'RectTransform':
            cgoid = ce['data'].get('m_GameObject', {}).get('m_PathID')
            n += walk_tree(aud, cgoid, buf, indent + 1)
    return n


def scan_project(proj, names, out_missing):
    """扫描 project 代码中元素名命中; 返回 {name: [(file,line,snippet)]}"""
    hits = {}
    files = []
    for base in ('scripts', 'scenes'):
        d = os.path.join(proj, base)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith(('.gd', '.tscn')):
                    files.append(os.path.join(d, fn))
    cache = {}
    for f in files:
        try:
            cache[f] = open(f, encoding='utf-8', errors='ignore').read()
        except Exception:
            pass
    for name in names:
        found = []
        for f, txt in cache.items():
            for m in re.finditer(re.escape(name), txt):
                line = txt.count('\n', 0, m.start()) + 1
                snip = txt.splitlines()[line - 1].strip()[:100]
                found.append((os.path.relpath(f, proj), line, snip))
                if len(found) >= 6:
                    break
            if len(found) >= 6:
                break
        if found:
            hits[name] = found
        else:
            out_missing.append(name)
    return hits


def gen_godot(aud, proj, out_path):
    """规格表 → Godot 代码骨架 (坐标/贴图/文字/字号/active 自动落地; 信号接线留人工 TODO)
    输出约定: 骨架粘贴进界面脚本 _build_ui(); 坐标=chain_rect 权威绝对屏幕坐标(1920x1080)"""
    asset_map = {}
    ast = os.path.join(proj, 'assets')
    if os.path.isdir(ast):
        for base, _, files in os.walk(ast):
            for fn in files:
                if fn.lower().endswith(('.png', '.jpg')):
                    key = fn.rsplit('.', 1)[0].lower()
                    asset_map.setdefault(key, 'res://' + os.path.relpath(
                        os.path.join(base, fn), proj).replace('\\', '/'))

    def tex_path(sprite):
        key = sprite.lower()
        if key in asset_map:
            return asset_map[key]
        s2 = key.replace('_', ' ')
        for k, v in asset_map.items():
            if k == s2 or k.replace('_', ' ') == s2:
                return v
        return None

    lines = ['# UI 骨架自动生成 (ui_spec_audit.py --gen-godot; 坐标=chain_rect 权威绝对屏幕坐标)',
             '# 用法: 整个函数粘贴进界面脚本 (extends Control), _ready 里调用 _ui_stub(); 手工处理 TODO 处 (信号/Button 类型)',
             'func _ui_stub() -> void:']
    nm_used = {}
    for r in aud.rows:
        nm = re.sub(r'[^0-9A-Za-z_]', '_', r['name'])
        if nm in nm_used:
            nm_used[nm] += 1
            nm = '%s_%d' % (nm, nm_used[nm])
        else:
            nm_used[nm] = 1
        r['_nm'] = nm
    for r in aud.rows:
        nm = r['_nm']
        lines.append('\t# %s%s (原版 GO pid=%s)' % (r['name'],
                     ' [原版隐藏]' if not r['active'] else '', r['pid']))
        if not r['rect']:
            lines.append('\t# (无 RectTransform 跳过)')
            lines.append('')
            continue
        x1, y1, x2, y2 = [('%g' % round(float(v), 2)) for v in r['rect']]
        if r['sprite']:
            lines.append('\tvar %s := TextureRect.new()' % nm)
            p = tex_path(r['sprite'])
            if p:
                lines.append('\t%s.texture = load("%s")   # 原版 sprite=%s' % (nm, p, r['sprite']))
            else:
                lines.append('\t%s.texture = load("res://assets/<TODO 贴图: %s.png>") if ResourceLoader.exists("res://assets/<TODO 贴图: %s.png>") else null' % (nm, r['sprite'], r['sprite']))
        elif r['text']:
            lines.append('\tvar %s := Label.new()' % nm)
            fs = int(r['font_size']) if r['font_size'] else 32
            lines.append('\t%s.add_theme_font_size_override("font_size", %d)' % (nm, fs))
            lines.append('\t%s.text = "%s"   # 原版 m_text' % (nm, str(r['text']).replace('"', "'").replace('\n', '\\n')[:80]))
        else:
            lines.append('\tvar %s := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换' % nm)
        lines.append('\t%s.name = "%s"' % (nm, str(r['name']).replace('"', "'")))
        lines.append('\t%s.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点' % nm)
        lines.append('\t%s.offset_left = %s' % (nm, x1))
        lines.append('\t%s.offset_top = %s' % (nm, y1))
        lines.append('\t%s.offset_right = %s' % (nm, x2))
        lines.append('\t%s.offset_bottom = %s' % (nm, y2))
        if not r['active']:
            lines.append('\t%s.visible = false   # 原版 m_IsActive=0' % nm)
        lines.append('\tadd_child(%s)' % nm)
        lines.append('\t# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)')
        lines.append('')
    out = '\n'.join(lines)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(out)
    print('✓ 生成: %s (%d 元素)' % (out_path, len(aud.rows)))


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    root = args[0]
    src = DEFAULT_SRC
    proj = DEFAULT_PROJ
    out_path = None
    depth = 99
    for i in range(1, len(args)):
        a = args[i]
        if a == '--src' and i + 1 < len(args):
            src = args[i + 1]
        elif a == '--proj' and i + 1 < len(args):
            proj = args[i + 1]
        elif a == '--out' and i + 1 < len(args):
            out_path = args[i + 1]
        elif a == '--depth' and i + 1 < len(args):
            depth = int(args[i + 1])
    aud = Audit(src, depth)
    cands = aud.name_idx.get(root, [])
    if not cands:
        for nm, pids in aud.name_idx.items():
            if root.lower() in nm.lower():
                cands += pids
    if not cands:
        print('⚠️ 未找到界面根 GO:', root)
        return
    goid = cands[0]
    gen_path = None
    for i in range(1, len(args)):
        if args[i] == '--gen-godot' and i + 1 < len(args):
            gen_path = args[i + 1]
    if gen_path:
        # 仅生成骨架 (不打印审计表): 先填充 rows
        buf = StringIO()
        walk_tree(aud, goid, buf)
        gen_godot(aud, proj, gen_path)
        return
    if len(cands) > 1:
        print('⚠️ 同名 GO %d 个, 取第一个 (pid=%d), 其余: %s' % (len(cands), goid, cands[1:6]))
    print('界面: %s (GO %s) — 来源 %s' % (root, goid, src))
    lines = ['# UI 规格审计: %s' % root, '',
             '> 来源: %s (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 %s' % (src, datetime.now().strftime('%Y-%m-%d %H:%M')),
             '> 项目: %s ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)' % proj, '',
             '## 规格表 (说明书期望)', '', '```']
    buf = StringIO()
    walk_tree(aud, goid, buf)
    lines.append(buf.getvalue().rstrip())
    lines += ['```', '', '## 项目代码命中', '', '| 元素 | 命中 |', '|---|---|']
    missing = []
    hits = scan_project(proj, [r['name'] for r in aud.rows[:400]], missing)
    for r in aud.rows[:400]:
        if r['name'] in hits:
            fl = '; '.join('%s:%d %s' % (f, ln, s) for f, ln, s in hits[r['name']][:2])
            lines.append('| %s | ✅ `%s` |' % (r['name'], fl[:130]))
        else:
            lines.append('| %s | ⚠️ 未命中 |' % r['name'])
    lines += ['', '## 摘要', '',
              '- 规格元素: %d' % len(aud.rows),
              '- 代码命中: %d' % sum(1 for r in aud.rows[:400] if r['name'] in hits),
              '- ⚠️未命中: %d (以下需人工判断)' % len(missing), '']
    for m in missing:
        lines.append('- `%s`' % m)
    out = '\n'.join(lines)
    if out_path:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(out)
        print('✓ 输出: %s' % out_path)
    else:
        print(out[:4000])


if __name__ == '__main__':
    main()
