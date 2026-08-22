#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_misc.py — 战斗/游戏数据/特效/模型/主程序资源 说明书生成器

输出:
  01_战斗_对战/README.md + 战斗规则摘要.md + 战斗HUD说明.md + 教程流程.md
  04_界面UI/README.md (索引)
  05_游戏数据/README.md + 卡包.md + 动画曲线.md + 脚本定义.md
  06_特效_预制体/README.md + 战斗预制体.md + 共享资源.md
  07_模型/README.md
  08_主程序资源/README.md
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

U = 'd:/2/解包整理/'
W = 'd:/2/解包整理/说明书/'
BATTLE = os.path.join(W, '01_战斗_对战')
DATA = os.path.join(W, '05_游戏数据')
VFX = os.path.join(W, '06_特效_预制体')
MODEL = os.path.join(W, '07_模型')
MAIN = os.path.join(W, '08_主程序资源')
UI = os.path.join(W, '04_界面UI')

RULEBOOK = 'd:/2/Warpforge部队卡片/Warpforge_Offline_Rulebook_1_5-3_中文翻译.md'
RULEBOOK_EN = 'd:/2/Warpforge部队卡片/Warpforge_Offline_Rulebook_1_5-3_英文原版.md'


def wfile(fp, txt):
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(txt)
    print('✓ %s (%d 行)' % (os.path.relpath(fp, W), txt.count(chr(10))))


def count_files(p):
    n = 0
    for _, _, fs in os.walk(p):
        n += len(fs)
    return n


def gen_battle():
    os.makedirs(BATTLE, exist_ok=True)
    # --- 战斗规则摘要 (从规则书翻译提炼) ---
    try:
        with open(RULEBOOK, encoding='utf-8') as f:
            rb = f.read()
    except Exception as e:
        rb = ''
        print('规则书读取失败:', e)
    lines = ['# 战斗规则摘要 (规则书翻译版索引)\n',
             '> 完整规则: `d:/2/Warpforge部队卡片/Warpforge_Offline_Rulebook_1_5-3_中文翻译.md` (791 行)',
             '> 英文原版: `..._英文原版.md`; 本文件为条款速览+代码实现对应关系\n',
             '']
    # 提取 1-12 主条款标题
    for m in re.finditer(r'^## (\d+\.\s+.+)$', rb, re.M):
        lines.append('- **%s**' % m.group(1))
    lines.append('')
    lines.append('## 与代码实现对应\n')
    lines.append('| 规则 | 代码文件 | 关键函数/字段 |')
    lines.append('|---|---|---|')
    lines.append('| 能量 N+1 | rule_core.gd | turn_p / energy |')
    lines.append('| 后手奖励 | rule_core.gd | second player bonus |')
    lines.append('| 手牌 | battle.gd / rule_core.gd | mulligan / hand limit |')
    lines.append('| 攻击/反击 | rule_core.gd | declare_attack / counter |')
    lines.append('| 护甲 | rule_core.gd | _damage_unit |')
    lines.append('| 关键词 | rule_core.gd | KEYWORDS |')
    lines.append('| 教程 | battle.gd | _tutorial (turnScriptedData) |')
    lines.append('')
    wfile(os.path.join(BATTLE, '战斗规则摘要.md'), '\n'.join(lines))

    # --- 战斗 HUD 说明 ---
    hud = ['# 战斗 HUD 说明 (battlearena1 2D 层)\n',
           '> 完整 2D 全树: [battlearena1_2D层全树.md](battlearena1_2D层全树.md) (854 行, dump_scene_tree.py 生成)',
           '> 本文件按功能分组导读\n',
           '',
           '## 层结构',
           '',
           '- **Root**: Scenario (3D) / ChooseCardMenuAnchor / Card Info / Tactic Container ×4 /',
           '  EffectAnchor ×5 / MinionOrWarlord Container ×7 / Textbackgrounds / MulliganAnchor /',
           '  HandArea / PlayerArea / EnemyAssetArea / BattlePrefab / Bg / Energy Accumulation VFX 等\n',
           '- **BattlePrefab**: Scene Initializer / BattleManager / BattleHud / BattleTipController /',
           '  BattleBoardElements (Colliders / BoardCamera / Cinemachine Vcam / PlayerBoardArea / EnemyBoardArea)\n',
           '',
           '## 功能地图',
           '',
           '| 功能 | 根/容器 | 说明 |',
           '|---|---|---|',
           '| 手牌 | HandArea -> HandAnchor | 玩家手牌区 |',
           '| 出牌区 | PlayerBoardArea -> MinionArea | LeftMinionArea/RightMinionArea 槽位 |',
           '| 敌方区 | EnemyBoardArea -> MinionArea | 敌方 9 槽 |',
           '| 高亮 | Minion Position Highlight | Glow/Shadow (SpriteRenderer) |',
           '| 相机 | BattleBoardElements -> BoardCamera | FOV 46.4, 世界 x=100 |',
           '| 卡面 | MinionOrWarlord Container | 3D 卡 (2DCard 组合) |',
           '| 提示 | BattleTipController | 教程/战斗提示 |',
           '| 能量 | Energy Accumulation VFX On/Off | 能量积攒特效 |',
           '',
           '## 分辨率/坐标',
           '',
           '- CanvasScaler 1920×1080 (UI Camera 正交, 挂 BattleHud)',
           '- RectTransform 坐标=Godot 1920×1080 y 向下 (chain_rect 权威换算)',
           ''
           ]
    wfile(os.path.join(BATTLE, '战斗HUD说明.md'), '\n'.join(hud))

    # --- 教程流程 ---
    tut = ['# 教程流程 (turnScriptedData)\n',
           '> 来源: 09_游戏数据/教程/MonoBehaviour/Warpforge_TutorialStage1-6.json',
           '> 生成: build_tutorial_data.py -> D:/warpforge/data/tutorial_stages.json (battle.gd 教程模式数据)\n',
           '',
           '## 结构',
           '',
           '- 每关卡 = TutorialStageN.json (MonoBehaviour, turnScriptedData 字段)',
           '- 每回合: tips[] (提示文本, TMP 富文本) + actions[] (玩家动作要求)',
           '- 关卡: 6 关 (Warpforge_TutorialStage1..6)',
           '',
           '## 数据管线',
           '',
           '1. 09_游戏数据/教程/MonoBehaviour/Warpforge_TutorialStage{1-6}.json',
           '2. scripts/build_tutorial_data.py 清洗 (`<link=..>`/`<sprite>`/`<nobr>` 富文本)',
           '3. D:/warpforge/data/tutorial_stages.json → battle.gd 按关卡+回合显示提示/校验动作',
           '',
           '## 提示文本清洗规则',
           '',
           '- `<link=武库>` → 删标签留文本; `<sprite N>` → 删; `<br>` → 换行',
           '- 关键词解析: 中文 2-4 字符 vs 英文 8-13 字符, 偏移/索引不同 (battle.gd _fx_from_event)',
           ''
           ]
    wfile(os.path.join(BATTLE, '教程流程.md'), '\n'.join(tut))


def gen_data():
    os.makedirs(DATA, exist_ok=True)
    # 卡包
    pk = os.path.join(U, '09_游戏数据/卡包')
    lines = ['# 卡包定义 (09_游戏数据/卡包)\n',
             '| 类型 | 文件数 |\n|---|---|']
    for sub in sorted(os.listdir(pk)):
        p = os.path.join(pk, sub)
        if os.path.isdir(p):
            lines.append('| %s | %d |' % (sub, count_files(p)))
    lines.append('')
    lines.append('- MonoBehaviour: 卡包 ScriptableObject (BoosterPack 定义: 稀有度权重/内容)')
    lines.append('- AnimationClip/ParticleSystem: 开包动画与特效')
    lines.append('- Sprite/Texture2D: 包面/卡背贴图')
    lines.append('- 保底系统: 每包+1 出传说重置 200 阈值 (packs.gd)')
    wfile(os.path.join(DATA, '卡包.md'), '\n'.join(lines))

    # 动画曲线
    cv = os.path.join(U, '09_游戏数据/动画曲线')
    lines = ['# 动画曲线 (09_游戏数据/动画曲线)\n',
             '| 类型 | 文件数 |\n|---|---|']
    for sub in sorted(os.listdir(cv)):
        p = os.path.join(cv, sub)
        if os.path.isdir(p):
            lines.append('| %s | %d |' % (sub, count_files(p)))
    lines.append('')
    lines.append('- MonoBehaviour: AnimationCurve 存储 (UI 动画/粒子曲线调参用)')
    wfile(os.path.join(DATA, '动画曲线.md'), '\n'.join(lines))

    # 脚本定义 (MonoScript 类名索引)
    sd = os.path.join(U, '09_游戏数据/脚本定义/MonoScript')
    lines = ['# 脚本定义 (09_游戏数据/脚本定义/MonoScript)\n',
             '> %d 个 MonoScript; 每 JSON 含 m_Name=脚本类名 (C# 全名), 与 Warpforge_code/ 对应\n' %
             sum(1 for f in os.listdir(sd) if f.endswith('.json')),
             '',
             '## 类名清单\n']
    names = set()
    for f in os.listdir(sd):
        if not f.endswith('.json'):
            continue
        try:
            d = json.load(open(os.path.join(sd, f), encoding='utf-8'))
        except Exception:
            continue
        n = d.get('m_Name')
        if isinstance(n, str) and n and ('（' not in n):
            names.add(n)
    for n in sorted(names):
        lines.append('- `%s`' % n)
    wfile(os.path.join(DATA, '脚本定义.md'), '\n'.join(lines))

    # README
    lines = ['# 游戏数据说明书 (09_游戏数据)\n',
             '| 子目录 | 说明 |',
             '|---|---|',
             '| 卡包 | [卡包.md](卡包.md) | 开包定义/保底/动画 |',
             '| 教程 | 教程.md 见 01_战斗 (turnScriptedData 6 关) |',
             '| 动画曲线 | [动画曲线.md](动画曲线.md) | UI/粒子曲线 |',
             '| 脚本定义 | [脚本定义.md](脚本定义.md) | MonoScript 类名 (与 Warpforge_code 对应) |',
             '| 去重定义 | 跨包去重对象 |',
             '']
    wfile(os.path.join(DATA, 'README.md'), '\n'.join(lines))


def gen_vfx():
    os.makedirs(VFX, exist_ok=True)
    for cat, dname in (('战斗预制体', '06_特效_预制体'), ('共享资源', '06_特效_预制体')):
        pass
    lines = ['# 预制体特效说明书 (08_预制体特效)\n',
             '## 战斗预制体 (%s 文件)\n' % count_files(os.path.join(U, '08_预制体特效/战斗预制体')),
             '| 类型 | 文件数 |',
             '|---|---|']
    pk = os.path.join(U, '08_预制体特效/战斗预制体')
    for sub in sorted(os.listdir(pk)):
        p = os.path.join(pk, sub)
        if os.path.isdir(p):
            lines.append('| %s | %d |' % (sub, count_files(p)))
    lines.append('')
    lines.append('> GO 15734: 战斗单位/部署/攻击/受击/死亡特效 + 卡牌动画复用')
    lines.append('> 同步脚本: sync_2dcard_assets.py / convert_card_vfx_bundle.py / dump_card_vfx_tree.py')
    lines.append('> VFX 接续: battle.gd _fx_from_event (事件关键词→VFX 树)')
    lines.append('')
    wfile(os.path.join(VFX, 'README.md'), '\n'.join(lines))
    lines = ['# 战斗预制体说明 (08_预制体特效/战斗预制体)\n',
             '> dump_card_vfx_tree.py 生成逐条 VFX 树 (卡牌动画/攻击/伤害特效)',
             '> VFX 与卡牌效果对应表: ui_layout/../data (convert_card_vfx_bundle.py)',
             '']
    wfile(os.path.join(VFX, '战斗预制体.md'), '\n'.join(lines))


def gen_model():
    os.makedirs(MODEL, exist_ok=True)
    md = os.path.join(U, '06_模型')
    lines = ['# 模型说明书 (06_模型)\n',
             '| 来源包 | OBJ 数 |',
             '|---|---|']
    tot = 0
    for sub in sorted(os.listdir(md)):
        p = os.path.join(md, sub)
        if os.path.isdir(p):
            n = count_files(p)
            tot += n
            lines.append('| %s | %d |' % (sub, n))
    lines.append('| **合计** | **%d** |' % tot)
    lines.append('')
    lines.append('## 使用约定')
    lines.append('- OBJ 是 Unity 归一化小模型 (顶点 ~0.02) → Godot 放大 500-800x (泰伦例外 1-20x)')
    lines.append('- 平躺 OBJ (y 薄 z 长) → rot_x +90 立起 (原版场景根 -90°X 补偿)')
    lines.append('- 无 mtl (材质在 Unity 侧) → 用纹理图集或单色金属材质')
    lines.append('- 场景 Baked 网格: 07_场景/<arena>/ MeshFilter (OBJ 导出: extract_arena_meshes.py)')
    lines.append('- 用途清单: sync_arena_props.py / unity_scene_to_godot.py (原版 Transform 表)')
    wfile(os.path.join(MODEL, 'README.md'), '\n'.join(lines))


def gen_main():
    os.makedirs(MAIN, exist_ok=True)
    mp = os.path.join(U, '12_主程序资源')
    lines = ['# 主程序资源说明书 (12_主程序资源)\n',
             '| 类型 | 文件数 | 说明 |',
             '|---|---|---|',
             '| 引擎设置 | GraphicsSettings/LightmapSettings 等 | 渲染/光照全局 |',
             '| 全局管理器 | MonoBehaviour (GameManager/AudioManager 等) | 游戏运行时单例 |',
             '| Sprite/图集 | 主界面图标/共用 UI 元素 | ui_extract 已索引 |',
             '| 字体 | 子目录 10_字体 (TTF) | UI 字体 |',
             '| Shader | 11_着色器 (527) | 需翻译成 Godot shader |',
             '',
             '## 运行时管理器 (MonoBehaviour, 与 Warpforge_code 对应)',
             '',
             '- GameManager / AudioManager / SaveManager (profile.json)',
             '- 货币/卡组/商店/任务 数据管理器',
             '- BoardCamera / BattleHud 场景单例',
             '',
             '## 重要数据对象',
             '',
             '- 图集: 菜单可用 SpriteAtlas (03_界面UI/图集)',
             '- 引擎资源: 12_主程序资源 (Settings/Input/Quality)',
             '']
    for sub in sorted(os.listdir(mp)):
        p = os.path.join(mp, sub)
        if os.path.isdir(p):
            n = count_files(p)
            lines.insert(3, '| %s | %d | |' % (sub, n))
    wfile(os.path.join(MAIN, 'README.md'), '\n'.join(lines))


def gen_ui_readme():
    lines = ['# 界面 UI 说明书 (03_界面UI)\n',
             '> 解析产物 (Warpforge_tools/data/ui_layout/) 已迁入本目录;\n',
             '> **权威=原始 JSON**: 03_界面UI/菜单/ 下 GameObject/RectTransform/MonoBehaviour/Sprite\n',
             '',
             '## 本目录文件',
             '',
             '| 文件 | 内容 |',
             '|---|---|',
             '| 菜单全树.md | 313 根界面全景 (坐标/纹理/文字) |',
             '| 菜单全树_要点_第{1-4}块.md | 逐界面元素表+未实现清单 |',
             '| 主菜单全树.md | 主菜单场景全树 |',
             '| 卡组界面说明书.md | 卡组编辑界面详表 |',
             '| 主菜单聊天面板.json | 聊天面板原始解析 |',
             '',
             '## 解析工具',
             '',
             '- dump_go_tree.py (按 GO 名 dump 子树) / dump_scene_tree.py (场景全树)',
             '- ui_layout_parser.py (03_界面UI/菜单 → json)',
             '- chain_rect.py (链式坐标换算 → Godot 绝对坐标, 权威)',
             '',
             '## 目录索引 (03_界面UI 顶层)',
             '',
             '- 主菜单 / 菜单 (148877 文件, UI 层级 JSON 主库) / 通用窗口 / 通用静态资源',
             '- 图集 / 去重资源 / 光标 / 军队图标 / 排位图标 / 收件箱横幅 / 特惠内容',
             '- 运营图标 / 运营菜单图 / 共享资源 / 卡组选择按钮',
             '']
    wfile(os.path.join(UI, 'README.md'), '\n'.join(lines))


def main():
    gen_battle()
    gen_data()
    gen_vfx()
    gen_model()
    gen_main()
    gen_ui_readme()


if __name__ == '__main__':
    main()
