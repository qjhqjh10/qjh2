# Unity 几何资源→Godot 转化映射表（子代理 A 完工版 · 2026-08-25）

> 来源：bundle 原始 Mesh 字节解码（typetree 转储 d:/2/Warpforge_tools/tmp/mesh_dump/）+ UnityPy 源码 + Godot mesh.html/camera3d.html + 项目 .import 实参。

## A1 坐标系/手性（根因实锤：三个网格逐字段实证）
| | Unity | Godot |
|---|---|---|
| 手性 | 左手 | 右手 |
| 轴向 | x 右 y 上 z 前 | x 右 y 上 z 后 |
| 相机 | +Z（Cinemachine） | -Z |
| UV 原点 | 左下 | 顶左（v=0 顶） |
| 正面 | 顺时针 | 逆时针 |
- **UnityPy 导出变换（MeshExporter.py:33/45/39/54 实证）**：顶点 `v x'=-x`、法线 `vn x'=-x`、**UV 原样（不翻 v）**、面序 `f c+1 b+1 a+1` 反转——"左手→右手"不完整转换（缺 UV u 镜像）
- **根因数学（A1.3）**：场景 MESH 节点旋转绝大多数为 **RotX**（battlearena1：identity×151/RotX+90×23/RotX−90×16/RotX180×4/复合×4），**RotX 与 M=diag(−1,1,1) 对易**（M·Rx=Rx·M）→ 世界结果=T_w·M·v=**绕网格自身枢轴的镜像**（位置不变、图案翻转）；链上全正 scale → 只能从网格数据还原
- **正解=fix_obj_xmirror**（v x'=-x + vn x'=-x + f 引用倒序=自逆变换精确还原）——**严禁 --flip-tex/flip_obj_vt 混用（二次翻转）**
- 定案=MirrorZ（内容 M_z=diag(1,1,−1)+相机移出镜像根 z 取反+四元数 (−x,−y,z,w)）；glTF 路径=顶点折入 (x,y,−z)+绕序翻转+conj_z_trs（等价）；**勿只转相机=镜像（16 轮）**
- 四元数共轭：M_z→(−x,−y,z,w)；M_x→(x,−y,−z,w)；**反射世界下"共轭+单位向量定轴"会方向反转→必须 rot_from_to 最短弧**（相机/灯分支已用）

## A2 网格通道映射（权威）
- 通道：0 pos3→ARRAY_VERTEX /1 nrm3→ARRAY_NORMAL（**非单位会被引擎归一化**）/2 tan4→ARRAY_TANGENT（**末位 binormal 符号必须 ±1**）/3 color4→ARRAY_COLOR（战场网格全无 color 通道）/4 uv2→**ARRAY_TEX_UV（唯一导出）**/5-11 uv1-7→不导出/12-13 skin→ARRAY_WEIGHTS/BONES；索引 m_IndexBuffer（>65535 须 Int32）
- **dimension 读取必须 &0xF**（raw=52=48+4 高位 flags，Terminal_R2 等实测）
- b1 通道分布：[pos3,nrm3,uv2] 主流 / [pos3,uv2]（**Floor plane 无法线**）/ [pos3,nrm3,tan4,uv2]（旗/覆盖物）
- UV：Unity raw v=0 底→OBJ 原样→**Godot 导入器只做 1−v**（位置/u 原样=导入器内建固定，.import 无 flip_v 参数）；glTF 路径 obj_parse 手动同 1−v（渲染一致）
- 绕序：还原后 OBJ=原序 (a,b,c)，GFX 整体手性由 MirrorZ 恰好一次提供；直接代码生成 ArrayMesh 时 Unity 绕序须整体反序 (a,c,b)
- 非均匀 scale 留节点不折顶点（Floor plane (30.34,7.46,17.69)——网格本体小 y 极薄，非均匀只在叶子）；无法线网格 fix_obj_normals 在导出器输出上算的 face 法线经 vn.x 取负=原版方向（两次 Mx 抵消闭环）

## A3 蒙皮/形态键
- 全库：形态键 blacklegion×2（Chain11 5 shapes/Firepits.002 7 shapes）；含 skin（bindpose>0）：blacklegion×2+battleshared×2+**battleprefabs_vfxandmisc×12（单位模型骨架！）**；battlearena2×2 与 tau&viorla×2 多 submesh
- Chain 案例：单骨骼（m_Bones=[1391]=GO 自身）+bindpose 1 条+5 形态键→静态呈现+export_morph_gltf（gd 路径 autoplay SceneAnim）方案成立
- **⚠️ 当前 unity_arena_battlearenablacklegion.gd 里 Chain 节点未实例化**（旧版生成物：MESH_PATHS 有 Chain11.obj 但无节点+无 .gltf 文件）→**需当前生成器重跑才带 clip17 形态键动画**
- 通用 SMR 规则：m_Bones 顺序=Skeleton3D 骨骼 id；Godot 不用 bindpose（rest 隐式替代）；rest=Unity 骨骼 GO 世界 TRS——glTF 管线自动处理勿手算
- **⚠️ 形态键帧/通道错位**：sh.shapes 按帧展平 vs channels 按通道——多帧通道会错位（现有 Chain 1 帧/通道恰好一致）；BlendShapeVertex.normal/tangent 增量丢弃（export_blend_shapes:817-824，需时补 NORMAL target）

## A4 格式
OBJ=现状主力（838 个，无 mtl 材质在 Unity 侧）；glTF=morph/骨架路线（**当前项目无任何 .gltf 资产**）；FBX=不可用（UnityPy 未实现）
- Godot OBJ 导入器参数（.import 实证）：generate_tangents=true（由 UV+法线生成近似）/generate_lods/generate_shadow_mesh/scale_mesh=(1,1,1)（**勿用，scale 留节点**）/offset=(0,0,0)；**无 flip_v 参数**（1−v 内建固定）
- glTF 导入器**不翻 UV**（obj_parse 写前完成 1−v）
- OBJ 不可承载：切线/顶点色/UV1-7/蒙皮/形态键/多材质分槽（usemtl 被 Godot 忽略）→ 路由补（法线 fix_obj_normals/切线导入器生成）

## A5 坑清单（17 条，重点）
1. 网格绕枢轴镜像=根因（fix_obj_xmirror 正解）
2. UV 二次翻转（还原后别再 flip）
3. **多 submesh 全库 11 个**（battlearena2 Combined 31 sub/battleshared Floor 2 sub/Cone×5/Card_Remnant）——UnityPy 只写 g 分组，Godot 并为一个 surface→**子网格材质分槽丢失**
4. **负 scale 44 个**（battlearena3×9/sororitas×17 最重）——照抄+材质 cull 按 Unity（负 scale 节点上勿手动改绕序）
5. 形态键帧/通道错位 6. 形态键法线增量丢弃
7. **glTF 形态键索引错位风险**（emit_gltf morph_deltas 用原始索引 vs merge_obj_gltf 去重重排——需验证）
8. 多材质只取 mats[0]（:1180/:1923）
9. **m_StaticBatchInfo.firstSubMesh 未读（高）**：battlearena2Combined 31-submesh 由 33 个 MeshRenderer 各选 1 子网格（firstSubMesh=0..30）——生成器没读→battlearena2 现有 gd 仅 4 节点渲整网格单材质=**场景根本性不对**（与 CLAUDE.md 遗留 battlearena2 对得上！）
10. 无 vt OBJ 4 个（IceShard/Background Structures.0041）→obj_valid 要求 vn+vt=永远 invalid 循环→放宽 v+f
11. OBJ 巨型 head 截断（obj_valid 读 1MB；Floor 2.4MB vt 在 589KB）
12. baseVertex 不处理=潜伏坑（当前全库 0）
13. Lines/Points raise（粒子 LineRenderer=运行时不受影响）
14. 命名截断 80 字符+同名跨 bundle 冲突
15. **说明书滞留旧论**（00_总览/README.md:4+battlearena1.md:7-8 写"整世界 scale.x=-1 镜像+相机 conjX"=已证伪的 MirrorX——代码现行=MirrorZ）→**文档需更正**
16. 勿只转相机/相机必须移出镜像根
17. m_IsReadable=false 可用（1030 OBJ 已导出）

## A6 工具缺失
- **firstSubMesh 未读（高）**：battlearena2 33 渲染器各选一 submesh 全被当整网格
- 多材质只取[0]（中）；submesh 拆分未做（中，11 网格受害）
- gltf_export 只写 POSITION/NORMAL/TEXCOORD_0（无 TANGENT/UV1+）；obj_parse `f a//c`（无 vt）tfi 错位风险（前提=OBJ 都修复后不触发）
- extract_arena_meshes：80 字符截断/无内容去重/不与 bundle 区/形态键元数据不落盘（只跑 extractor 不跑转换器=形态键数据丢失）
- 体系级：SMR 完整链（12 个 VFX 包单位模型）无 Skeleton3D 转换器（折衷=静态呈现）；MeshCollider 跳过正确；UnityPy m_Triangles TODO

## 关键实证文件
mesh_dump/（Background/Bridge1/Floor_plane/Vehicle1/Platform_Flag1/Back_background typetree）；Transform_1375.json；06_模型/scenes_scenes_battlearena1/{Background,Bridge1,Floor plane}.obj；MeshExporter.py:33/39/45/51/54；MeshHelper.py:142-155/269/359/390-444；generated.py:4416-4459/6674-6686/8538-8561；banner1.obj.import（wavefront_obj 8 参数）
