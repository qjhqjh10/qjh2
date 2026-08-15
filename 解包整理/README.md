# Warpforge 解包资源 — 使用说明

> 战锤40K Warpforge（Unity IL2CPP 卡牌游戏）的完整解包资源，44.9 万文件 / 6.2G。
> 本文件是**新会话的第一份资料**——先读这里，再动手。

## 0. 配套目录（D:\2 下）

| 目录 | 内容 |
|---|---|
| `解包整理/` | 本目录：按内容分类的资源（12 大类） |
| `Warhammer 40k Warpforge/` | 游戏本体（资源源文件，1.8G） |
| `Warpforge_code/` | 反编译的 C# 游戏代码（14996 文件，130 程序集）——**查逻辑/字段/枚举先翻这里** |
| `Warpforge_tools/` | Python 工具集（py312 + UnityPy，提取/解码/验证脚本，见其 README） |

## 1. 目录结构（12 大类）

| 目录 | 文件数 | 内容 |
|---|---|---|
| `01_卡牌/` | ~10.6K | 13 阵营 ×（Texture2D 立绘 / Sprite 精灵 / AudioClip 语音）+ 动画 + 卡组数据 |
| `02_装饰品/` | ~5.5K | 卡背 / 头像 / 督军立绘 / 边框 / 战役奖励 |
| `03_界面UI/` | ~154K | 菜单 / 图集 / 图标 / 按钮 / 横幅（UI 层级 JSON 为主） |
| `04_音频/` | ~1.9K | 音效库(618) / 音乐 / 督军语音 / 音频控制 |
| `05_视频/` | 18 | 8 个视频（h264×1 / VP8×7，mp4 容器） |
| `06_模型/` | 834 | 全部 OBJ 网格（跨包收集，子目录=来源包名） |
| `07_场景/` | ~139K | 13 个战斗场景（GameObject/组件/灯光/材质 JSON） |
| `08_预制体特效/` | ~119K | 战斗预制体(15734 GO) / 共享资源 |
| `09_游戏数据/` | ~4.6K | 卡包 / 教程 / 动画曲线 / 脚本定义(monoscripts) |
| `10_字体/` | 189 | TTF 字体 + 配套贴图材质 |
| `11_着色器/` | 527 | 全部 Shader 转储（跨包收集） |
| `12_主程序资源/` | ~12.9K | 引擎设置 / 全局管理器 / 主数据文件对象 |

## 2. 文件格式速查

| 扩展名 | 内容 | Godot 可用性 |
|---|---|---|
| `.png` | 贴图 | ✅ 直接导入 |
| `.ogg` / `.wav` | 音频（wav=IMA 解码，ogg=vorbis 重建） | ✅ 直接导入 |
| `.ttf` | 字体 | ✅ 直接导入 |
| `.obj` | 网格模型 | ✅ 可导入（建议转 glb/gltf 更好） |
| `.mp4` | 视频（h264/vp8） | ⚠️ Godot 4 不支持 h264，**需转 webm(VP8)/ogv** |
| `.json` | Unity 对象转储（见下节） | ⚠️ 用 Godot JSON 解析读字段 |
| `.vorbis` | 1 个未重建的原始音频包（OvertimeStart） | ❌ 需解码 |

## 3. JSON 转储是什么、怎么读

每个 JSON = **Unity 序列化对象的一个完整字段转储**（type tree 原文），不是人读的导出数据。
文件命名：`<对象名>.json`；无名字的对象 = `<类名>_<pathID>.json`（如 `Material_2.json`）。

子目录名 = Unity 对象类名，常见类：
- `MonoBehaviour` — 游戏数据（ScriptableObject）/ 组件。**卡牌、卡组、商店、成就等一切游戏数据都在这**
- `GameObject` / `Transform` / `RectTransform` — 场景/预制体层级结构
- `Material` — 材质（Unity 格式，Godot 需重建）
- `Sprite` / `Texture2D` — 精灵元数据 + 贴图（同名的 .png 是它的图）
- `AnimationClip` / `Animator` / `ParticleSystem` — 动画/特效
- `Shader` — 着色器转储（不可直接运行，需翻译成 Godot shader）

关键字段：
- `m_Name` — 对象名（搜资源先搜名字）
- `m_Script` — `{m_Collection: "cab-<哈希>", m_PathID: N}` — 指向脚本类；cab 哈希=来源包
- `m_GameObject` / `m_PathID` — 对象间引用（跨文件引用靠 cab+pathID 对应）

**想查对象是什么脚本类**：跑 `Warpforge_tools/scripts/classify.py`（用 monoscripts 包把 pathID 映射成类名），或直接翻 `Warpforge_code/Scripts/Assembly-CSharp/` 同名类。

## 4. 卡牌数据（做卡牌游戏的核心）

- **卡牌定义**：`01_卡牌/卡组数据/MonoBehaviour/*.json`（2210 个）— `PrebuiltPack` 类：
  ```json
  { "m_Name": "Canoness", "packName": "Canoness", "packId": "SOR_Canoness",
    "packArmy": 80, "cardIds": [3 个卡牌ID] }
  ```
  `packArmy` = 阵营 ID；`cardIds` 指向具体卡牌数据（卡牌本体定义在 `08_预制体特效/战斗预制体` 的组件 JSON 里）
- **卡牌立绘**：`01_卡牌/<阵营>/Texture2D/*.png`（与 `Sprite/*.json` 同名配对）
- **卡牌语音**：`01_卡牌/<阵营>/AudioClip/`（索引已挂载 602/1193 张卡，含督军全套语音；无语音的卡多为战术卡/测试卡）
- **卡牌动画**：`01_卡牌/<阵营>/动画/`（Spine 骨骼动画数据）
- **阵营 ID 表**（来自反编译代码 CardArmy.cs，权威）：
  Neutral=0, Ultramarines=10, Goff(兽人)=20, SaimHann(灵族)=30, Sautekh(死灵)=40,
  BlackLegion=50, Leviathan(泰伦)=60, TauEmpire=70, Sororitas=80, Genestealers=90,
  AstraMilitarum=100, DarkAngels=110, EmperorsChildren=120, SpaceWolves=130

## 5. 音频/视频说明

- 音频源格式是 **FSB5（FMOD）**，已解码为 wav（IMA-ADPCM 手写解码器）/ ogg（vorbis 重建）
- 卡牌语音在各阵营目录；战斗音效 618 个在 `04_音频/音效库`；音乐 2 首在 `04_音频/音乐`
- 视频在 `05_视频/`：`Gacha Crate Opening` 是 h264，其余 7 个 VP8 —— Godot 用需转 webm

## 6. 已知限制（不完整清单）

1. `OvertimeStart.vorbis` — 48kHz 立体声，缺 setup 头无法重建 ogg（1/2555 音频）
2. 2 张 `Font Texture` 特殊格式贴图未解码
3. 3 个空网格（CandleFlame）只有 JSON
4. ~0.4% 对象（899 个，主数据文件 UI 组件）type tree 解析失败，无转储
5. 重名对象合并时少数文件以 `_来源包` 后缀区分（manifest 可查）
6. `07_场景/_battlearena1` 因系统占用未重命名（内容正常）

## 7. 常见需求速查

| 想找 | 路径 |
|---|---|
| X 阵营的卡图 | `01_卡牌/<阵营>/Texture2D/` |
| 全部卡背 | `02_装饰品/卡背/` |
| 头像/督军立绘 | `02_装饰品/头像/` `02_装饰品/督军立绘/` |
| 某个音效 | `04_音频/音效库/AudioClip/` |
| 主菜单背景图 | `03_界面UI/主菜单/` |
| 战斗场地模型 | `06_模型/` + `07_场景/` |
| 卡牌数值/卡组构成 | `01_卡牌/卡组数据/MonoBehaviour/` |
| 某个脚本的字段含义 | `Warpforge_code/Scripts/Assembly-CSharp/<类名>.cs` |
| 素材来自哪个包 | 子目录名（06/11 类带来源包名）；分类映射见 `Warpforge_tools/scripts/classify_move.py` |

## 8. Godot 开发建议

- **直接导入**：PNG / OGG / WAV / TTF / OBJ
- **需转换**：MP4→webm（Godot 4.3+ VideoStreamWebm）；OBJ→glb（Blender/trimesh）
- **需重建**：材质、着色器、预制体（Unity 格式，Godot 里用标准材质/Shader 重做）
- **卡牌数据**：用 GDScript `JSON.parse_string()` 读 `卡组数据` 的 JSON，按 `packArmy`/`packId`/`cardIds` 组织
- **动画**：Spine 数据需用 Godot 社区 Spine 插件（或导出 glTF）
- **资源命名即索引**：文件名就是对象名，用 `DirAccess` 递归扫描 + 名字匹配即可建资源库

## 8.5 视觉副模型（vision MCP + skill）

主模型（Claude Code）无法直接查看图片，所有图像理解通过视觉副模型完成：
- **MCP server**：`Warpforge_tools/scripts/vision_mcp_server.py`（stdio，调用 MiniMax M3 / OpenCode Go）
- **工具**：`vision_analyze(image_path, prompt)` 单图识别；`vision_batch(inputs|directory, prompt_template)` 批量（并发2/重试/错误隔离/摘要，单批≤20 张）
- **Skill**：`~/.claude/skills/vision/SKILL.md`（自动触发：说"看看这张卡图"、"检查这批立绘"、"提取卡面文字"即自动调用）
- **配置**：cc-switch MCP 面板（服务器 ID `vision`，stdio，命令 `d:/2/Warpforge_tools/py312/python.exe`，参数 `d:/2/Warpforge_Tools/scripts/vision_mcp_server.py`，env 留空）
- **环境变量**：`MINIMAX_API_KEY`（系统环境，setx 设置）；可选 `MINIMAX_BASE_URL`（默认 OpenCode Go）、`MINIMAX_MODEL`（默认 MiniMax-M3，自动探测）
- **测试**：`Warpforge_tools/scripts/test_vision_mcp.py`（mock 冒烟 / `--live` 真实调用）

## 9. 重新提取/工具链

需要重新提取或解码时用 `Warpforge_tools/`（自带的 py312 运行，勿用系统 Python 3.14）：
- `extract_full.py` 全量提取 → `fix_exports.py` 补充导出 → `verify_extract.py` 验证 → `classify_move.py` 分类
- `build_card_index.py` 生成卡牌索引（`--compare <旧索引>` 做零回退断言）→ `vision_mcp_server.py` / `test_vision_mcp.py` 视觉副模型
- `fsb_audio.py` / `ogg_build.py` — FSB5 音频解码与 OGG 重建
- 详见 `Warpforge_tools/README.md`
