# Unity ParticleSystem → Godot 粒子转化映射表（子代理 D 完工版 · 2026-08-25）

> 来源：解包说明书 06_特效_预制体/02_战场_场景 + 原始 Unity JSON（07_场景/08_预制体特效 双语料）+ Godot 4.7.1 本地 extension API（d:/2/Warpforge_tools/tmp/extension_api.json）。
> ❗ 注意：d:/2/资料_Godot文档/ 下 gpu_particles3d/particles_process_material/gpu_particles2d.html 是 404 空壳页（不可用），权威=extension_api.json。

## 数据全景
- 战斗 VFX 根 977（根级 PS/PSR 仅 163；其余根=空容器）；战斗预制体 PS/PSR 27852 文件、Material 1142、TrailRenderer 26；battlearena1 PS/PSR 60/60；共享资源根 303
- 全库模块启用统计：UVModule 6312 / VelocityModule 4318 / ClampVelocity 3504 / SubModule 3632（子发射器引用 10224 条）/ Noise 3168 / Collision 2026 / Trail 1642 / Mesh-shape 20 / Sprite-shape 2
- PSR renderMode 分布：0=18438、1=3972(Stretch)、2=2084(HorizBillboard)、5=1714(None)、4=1632(Mesh)、3=12
- **两套语料关键键名（最易踩）**：ShapeModule 用 `type`（shapeType 恒 None）、radius=MultiModeParameter structure、scale=`m_Scale`（scale 键 null）

## P0 键名/语义错误（三个 JSON 转换器共有，影响面大）
1. **shapeType 键错**：convert_unity_particles.py:387/443、convert_arena_particles.py:341、convert_card_vfx_bundle.py:395 读 `shapeType`，语料键=`type` → 战斗 VFX JSON 99% shape=Sphere（实测分布 0:1374/2:300/4:1516/5:86/6:20/8:6/10:1100/12:192/13:4/15:2/17:2/18:142）
2. **scale 键错**：convert_unity_particles.py:392 读 `scale`（恒 None→[1,1,1]）应为 `m_Scale`
3. **minMaxState 枚举混用**（unity_scene_to_godot.py:154-159）：真枚举=0 Constant/1 Curve/2 TwoCurves/3 TwoConstants；state=3 是"端点对 {scalar,minScalar}"（非曲线）；state=2 带真双曲线 → 28+4 例读错
4. **Velocity 曲线全丢**：convert_unity_particles.py:418 与 convert_card_vfx_bundle.py:399 硬编码 `"velocity": {}`；VelocityModule x/y/z=MinMaxCurve 曲线（消逝漂移/热浪主体）→ 需读 keys+CurveXYZTexture
5. **SubEmitters 全链未读**（10224 条引用）：battlearena1 SmokeEffect(1)（Droppods 子发射器 50%+Glow 100%）实证丢弃；Godot 4.7.1 原生支持（ParticleProcessMaterial.sub_emitter_mode SUB_EMITTER_CONSTANT/AT_END/AT_COLLISION/AT_START + GPUParticles3D.sub_emitter NodePath + emitProbability→sub_emitter_frequency）
6. **RotationModule 读键 bug**：separateAxes=false 时用 `curve` 键（非 z），unity_scene_to_godot.py:2369/convert_arena_particles.py:356 读 z → Steam ±10°/s 全丢；JSON 路径硬 0
7. **renderMode=5（None）误渲染 quad**（1714 个子发射器宿主显示错误光点）

## 模块→属性映射要点（完整表见子代理会话，此处为落盘摘要）
- 系统级：maxNumParticles→amount=rate×life（场景 clamp 上限 800；运行时 clamp(4,500) 下限 4 偏差）；looping→one_shot=!looping；playOnAwake→emitting；prewarm→preprocess（仅场景路径）；simulationSpeed→speed_scale（**仅场景路径**，JSON 路径全丢：光柱 0.3/毒气 0.4/烟 0.75 案例）；moveWithTransform→local_coords（未用=偏差）；startDelay/randomSeed/ringBuffer/cullingMode=无/未用
- Initial：startSpeed→initial_velocity_min/max（负值直通需钳制）；startLifetime→lifetime+lifetime_randomness（**未设 randomness=区间退化为统一上限**）；startSize→scale_min/max（size3D 未映射）；startColor→color+vertex_color_use_as_albedo（场景取 maxColor/均值；运行时恒均值）；gravityModifier→gravity=Vector3(0,-9.81×g,0)；startRotation→angle/rotation_3d（**全部未映射**）
- Emission：rateOverTime=amount/lifetime 等效；rateOverDistance 无（需 emit_particle() 信号）；m_Bursts：场景只算总量+one_shot；运行时 explosiveness=1 单爆点——**cycleCount/repeatInterval/probability 全丢**（实测 0.3s×2 案例；burst+looping 被错误 one_shot）
- Shape 枚举（Unity type→Godot EMISSION_SHAPE）：0 Sphere→SPHERE ✓；1 SphereShell→**错落 SPHERE**（应 SPHERE_SURFACE）；2/3 Hemisphere→SPHERE_SURFACE ✓近似；4 Cone→SPHERE+radius 硬钳 0.35（angle 反推未做）；5 Box/15 Rect→BOX m_Scale/2 ✓；6/10/11/12/13/18→BOX 近似；7 Circle→RING ✓；**8 CircleEdge→错落 SPHERE（应 RING，battlearena1 有 8 个）**；9 SingleSidedEdge→RING（错）；14 Donut→RING inner=donutRadius（错）；17 Sprite→无；**m_Position/m_Rotation（射源偏移）→emission_shape_offset 未读**；angle/arc→spread 近似（arc 全丢，Battle 44° 光锥错）；alignToDirection→transform_align 未用
- Size/Color OL：size→scale_curve=CurveTexture（场景仅首尾差>0.01 才建；JSON 首点钳 0.35）；color→color_ramp=GradientTexture1D（**梯度读取 bug：JSON 路径 8 点均匀采样含 stale keys 2..7 全 0→中途变黑+atime/ctime 忽略**——应复用 unity_scene_to_godot.grad_keys L176-223 的 NumKeys+并集插值）；Curve 模式乘子 scalar 未乘（TinyExplosion_Far size 差 2 倍案例 scalar=2.0）
- Velocity/Limit/Rotation/Noise/Collision/Trail：见 P0-4/6 + LimitVelocity（velocity_limit_curve+damping，collision 阻尼全丢）；Noise→turbulence_*（全未用，3168 系统）；Collision→collision_mode+bounce/friction+碰撞平面（2026 系统，ElectricalSparks m_Planes=[1419] 案例）；Trail→**Godot 4.7.1 原生 trail_enabled/trail_lifetime+BaseMaterial3D.use_particle_trails**（1642 系统全未用）；SubEmitter→原生 sub_emitter_mode/GPUParticles3D.sub_emitter（见 P0-5）
- UV flipbook：场景路径 ✓（anim_speed+particles_anim_h/v_frames+particles_anim_loop）；JSON 路径"黑帧回退单帧切片"（动画感丢）；cycles>1/rowIndex 不支持
- renderMode→draw_pass：0 Billboard→QuadMesh+BILLBOARD_PARTICLES ✓；1 Stretch→无原生（transform_align Y_TO_VELOCITY 近似，3972 系统）→**当前按普通 billboard**；2 Horizontal→BILLBOARD_FIXED_Y 未用；3 Vertical→shader；4 Mesh→draw_pass_1 ✓场景（JSON 路径不导出 mesh→运行时回退 quad，1632 系统受影响）；5 None→应跳过（当前渲染光点）

## 粒子材质要点
- _SrcBlend=1/_DstBlend=0=opaque；5/10=AlphaBlend（预乘）→TRANSPARENCY_ALPHA（若确预乘→BLEND_MODE_PREMULT_ALPHA）；5/1→ADD →BLEND_MODE_ADD（项目约定 _Blend 0=alpha/2=add）
- _Cull 0/1/2→CULL_DISABLED/FRONT/BACK（坑 83 None 判空）；_ZWrite 0→DEPTH_DRAW_DISABLED（粒子材质当前未应用）；_Color/_BaseColor→albedo_color（HDR>1 clamp，Embers 2.828 案例）
- 双贴图 → uv_scroll.gdshader 双层 mix+TIME 滚动（Vector4_1=(UV Scale XY, Speed ZW)，黑军团 (1,1,0.02,0)）
- 粒子必需：billboard_mode=BILLBOARD_PARTICLES、vertex_color_use_as_albedo=true、SHADING_MODE_UNSHADED、TRANSFERENCY_ALPHA
- 贴图 alpha 修复（预乘损坏）：tr≥50% 且 RGB>100（convert_unity_particles.py:336-354）；运行时 _tex_shape_ok 四角 α>200 判硬边损坏→soft_dot 降级
- b3 坑：ShaderMaterial 无 cull_mode（已删行）；Heat Distortion=Glow 贴图+α0.16+ADD 近似；烟=UNSHADED+原贴图+白 albedo

## 曲线/梯度 JSON 语义（落盘）
- AnimationCurve：m_Curve[{time,value,inSlope,outSlope,weightedMode,inWeight,outWeight}]+m_PreInfinity/m_PostInfinity(0 Cycle/1 CycleRelative/2 Oscillate/3 Clamp)+m_RotationOrder；Godot Curve.add_point 默认线性——保真=set_point_right/left_tangent（dx=1,dy=slope）
- Gradient：key0..7+ctimeN/atimeN(0..65535)+m_NumColorKeys/m_NumAlphaKeys+m_Mode(0 Blend/1 Freeform)；正确=按 Num 数取+ctime/atime÷65535+并集时间轴插值；错误=8 点均匀 i/7.0
- _m_Modifier（MinMaxCurve 修饰器）：本语料未读到，标注"未读到"

## 覆盖率矩阵（模块×转换工具；✓/△/✗）
| 模块 | 场景内联 | JSON 3 转换器 | 运行时 |
|---|---|---|---|
| Initial | ✓ | △（state 混用） | △（randomness 缺/clamp 4） |
| Emission rate/burst | △（cycle 丢） | △ | △（单爆点） |
| Shape | △（8/9/14/1 错） | ✗ 恒 Sphere | 读 JSON（输入已错） |
| Size/Color OL | ✓ | △（8 点含 stale） | △ |
| Velocity | △（仅常数） | ✗ 空 dict | ✗ |
| Rotation | △（z 键 bug） | ✗ 硬 0 | ✗ |
| LimitVelocity | ✗ | ✗ | ✗ |
| Noise→turbulence | ✗（Godot 已具备） | ✗ | ✗ |
| Collision | ✗（Godot 已具备） | ✗ | ✗ |
| Trail | ✗（4.7.1 已具备） | ✗ | ✗ |
| SubEmitter | ✗（4.7.1 已具备） | ✗ | ✗ |
| UV flipbook | ✓ | △（单帧回退） | ✗ |
| simSpeed/prewarm/startDelay | ✓✓✗✓（场景） | ✗ | ✗ |
| 材质/贴图 | ✓ | ✓ | ✓（soft_dot） |
| renderMode 4/5 | ✓/✗ | ✗ | △ |

## battlearena1 60 项具体结论
- 33/60 生成（33 个 GPUParticles3D）全部对应 ✓；26 个=layer5 UI 世界粒子（设计排除，2D 只补 3/26：Accumulated Energy/Energy Moving Left/Shrink glow/Glow Acummulated Ring 缺 2D 数据）；**真洞=SmokeEffect (1)**（Droppods 子发射器，rate=0+burst=[] 生成器早退——修复靠子发射器接线）
- 正确数量=60-26(层5)=34；现状 33；缺口 1
- 已建粒子 2 处小偏差：Bullets Burst 1×2/Ship Burst 速度被 velocity-over-lifetime 二次覆盖（15→10）；Shape 8→SPHERE

## 推荐修复顺序
① 三 JSON 转换器改 type/m_Scale 键 + grad_keys 复用 → ② SubEmitter 原生接线（含 renderMode=5 静默）→ ③ Velocity 曲线+Rotation curve 键 → ④ Noise/Collision/Trail/LimitVelocity 原生属性落地 → ⑤ randomness/simSpeed/burst 周期补全

## 关键证据文件:行号
unity_scene_to_godot.py:154-173,176-223,616-629,1032-1046,1657-1664,2209-2437,1868-1869,488-495,918-935；convert_unity_particles.py:270-333,386-421,443；convert_arena_particles.py:254-300,341-359；convert_card_vfx_bundle.py:289-401,459-460,174-176；unity_particles3d.gd:59-89,148-170,172-230；unity_particles.gd:45-67；battle.gd:637-645；battlearena1.md:5,459-522；战斗VFX预制体清单.md:4；06 README.md:21-43
