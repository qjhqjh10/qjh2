# Unity 材质→Godot 材质转化映射表（子代理 B 完工版 · 2026-08-25）

> 来源：battlearena1 16 材质原始 JSON + 全库 1575 材质扫描 + 11_着色器 90 个 Shader JSON（m_Props=属性名单权威）+ Godot 4.7.1 BaseMaterial3D 文档（curl 下载 /tmp/bm3.html——**本地库缺该页，建议补入 资料_Godot文档/**）。

## 关键事实
- shader 归属：URP/Particles/Unlit 479 个、URP/Unlit 、**URP/Lit 仅 4 个**、URP/Particles/Lit 2、Simple Lit 2；其余 **Everguild 自研 ShaderGraph**（UnlitAmbient 73、Unlit UV scroll 48、Unlit Wind 23、shadows receiver、LUTBlender、Particle Distortion、UI Glow SDF Noise、UI Border Highlight、Nebula、TMP 61/62、Skybox/Procedural、Mobile/Particles/Additive）→ **映射表以参数族为单位**
- **判据核心：shader 的 m_Props 名单 = 哪个 Unity 属性真实存在**（_Color vs _BaseColor 权威）

## B1 参数映射要点（重点差异）
- `_BaseMap`/`_MainTex`→albedo_texture + `m_Scale/m_Offset`→uv1_scale/uv1_offset（25 个非单位平铺，黑 Hexagon 5×5）
- `_BaseColor`/`_Color`→albedo_color（**按 shader prop list 选**；HDR>1 合法：Lightning 1012/8.0/18.16——UNSHADED 下需 clamp）
- `_Metallic`→metallic（21 个非 0！**当前工具全忽略了**）；`_Smoothness`→roughness=1-_Smoothness（**工具硬编码 0.9 覆盖全部真值**）；`_SpecColor`→specular（**SPECULAR_DISABLED 一刀切杀掉金属高光**）
- `_BumpMap/_BumpScale`→normal_enabled+normal_texture+normal_scale（13 个，未解析）
- `_EmissionMap`（84 个）→emission_texture；`_EmissionColor`→emission（**工具只设 enabled+energy 从不写颜色=黑发射=没发射！glTF 路径才对**）
- `_Cutoff`（38 个非 0.5）/`_ClipThreshold`（Everguild 用，少量非 0.5）→alpha_scissor_threshold（**当前硬编码 0.5**）
- `_Surface`(0=Opaque/1=Transparent) 为主判据；`_Blend`≠旧 m_BlendMode——**URP _Blend: 0 Alpha/1 Premultiply/2 Additive/3 Multiply**
- `_ZWrite` 0×1015/1×255→depth_draw_mode DISABLED/OPAQUE_ONLY；`_Cull` 0=Off×474/2=Back×758→CULL_DISABLED/CULL_BACK（**0 值 None 判空**）
- `_QueueOffset`+m_CustomRenderQueue（3000×924/2450/2000/3005/5000）→render_priority（未映射）

## B2 keyword（全库 m_ValidKeywords 分布）
`_SURFACE_TYPE_TRANSPARENT` 966 / `_APPLYAMBIENTCOLOR` 123（Everguild UnlitAmbient：材质内 `_ExtraAmbientColor` 0.44/0.51/0.78/0.32 叠"伪环境"——UNSHADED 直出最接近，**别再叠 Unity 环境光**）/ `_EMISSION` 110 / `_FLIPBOOKBLENDING_ON` 38（→particles_anim_h/v_frames+loop，帧间无插值近似）/ `_COLORADDSUBDIFF_ON` 62（Add/Sub/Diff——Sub/Diff 需 shader，Spirit Stones=Add/Glow Rays=(1,0,0)→Sub 但名"Add"**语义未读到确切定义**）/ `_SOFTPARTICLES_ON` 100+29（Godot 无软粒子→近似）/ `_FADING_ON` 100 / `_ALPHABLEND_ON` 7 / `_ALPHATEST_ON` 19 / `_USEMASK` 8（Particle Distort）/ `_PREMULTIPLY` 0 / TMP UNDERLAY 15
battlearena1 16 材质 keyword：_SURFACE_TYPE_TRANSPARENT×8/_ALPHATEST_ON×4/_APPLYAMBIENTCOLOR×7/_FLIPBOOKBLENDING_ON×1

## B3 混合四元组表（**权威**：(_Surface, SrcBlend, DstBlend, AlphaClip) 判定）
| _Blend | (Src,Dst) | 数量 | 公式 | Godot |
|---|---|---|---|---|
| 0 | (5,10) | 580 | SrcAlpha/OneMinusSrcAlpha | ALPHA+MIX |
| 0 | (1,0) | 201 | One/Zero=不透明 | DISABLED |
| 1 | (1,10) | 11 | 预乘 | BLEND_MODE_PREMULT_ALPHA(4) |
| 2 | (5,1) | 420 | 加色 | ALPHA+BLEND_MODE_ADD |
| 3 | (2,0) | 12 | 乘法 | BLEND_MODE_MUL |
- **unity_params_to_godot.py:73/11 `_Cull` 翻译表写反了**（0→BACK/2→DISABLED；Unity 真值 0=Off/2=Back）——与工具代码自身也冲突！
- unity_params_to_godot.py MAT_BLEND（L173/179-184）=built-in 管线枚举（Fade/Transparent），对 URP `_Blend` 不适用——**两套枚举混用=翻译表混乱根源**

## B4 贴图通道
- _MainTex/_BaseMap 判据=shader m_Props 名单（M3/M12 只有 _MainTex）；同 pathID 的残余属性（M14）忽略
- pathID 解析链：m_TexEnvs→UnityPy Texture2D→ensure_tex 落盘（fid>0 外部 bundle 走 BundleResolver._scan_bundles；**陷阱=同名多 pathID/多 bundle 撞号**）
- SpriteAtlas（m_RenderDataMap=[UVRect,贴图ref]+m_PackedSpriteNamesToIndex）——UI 走 Sprite JSON 链不经材质；图集 alpha=0 RGB=内容（坑 51/56）→repair_uv_alpha

## B5 特殊材质
- Unlit 系：UNSHADED（--unshaded-bake）；--unshaded-gain=RT 实测标定（非 JSON 可推）
- UV scroll（黑军团）：uv_scroll.gdshader；**发现缺陷：render_mode 无 cull_disabled**（L1868 注释"双面由 shader 处理"与实际矛盾！M3/M12 _Cull=0 双面=现渲染单面）
- VFX 粒子材质：URP/Particles/Unlit props=_BaseColor/_Cutoff/_Emission*_/_ColorMode/_BaseColorAddSubDiff/_FlipbookBlending/_SoftParticles*；**convert_card_vfx_bundle.py 材质参数 0 处理**（只出贴图/帧）；renderMode 5=None 应跳过
- LUT/Vignette：Bloom(threshold 1.15/intensity 5.0/scatter 1.0/skipIterations 6)+Vignette(0.297/0.2)+ColorLookup(contribution 1.0)+Hidden/LUTBlender→现有 glow_levels 6-7+lut_vignette.gdshader 近似；**无 tonemap（TONE_MAPPER_LINEAR vs URP ACES 曲线差）**
- Heat Distortion：真折射无解→Glow 贴图+α0.16+ADD 近似（roadmap：hint_screen_texture shader）
- 三档判定改进：_Surface==1 或 TRANSPARENT keywords→ALPHA；_ALPHATEST_ON 或(_AlphaClip==1 and _Surface==0)→SCISSOR；否则+_Blend∈{2,3}→对应 blend_mode；RenderType=TransparentCutout 交叉验证

## B6 光照/环境（battlearena1）
- RenderSettings: m_AmbientMode=**3**（Custom；工具注释"Trilight"存疑）、Sky(1,1,1)/Equator(0.325,0.586,1)/Ground(0.5896,0.5896,1)、intensity **0.41**（工具未用=--ambient-energy 1.15 覆盖）、m_AmbientProbe SH DC=(0.289,0.183,-0.080)（B<0 负值被 max(0)截）、fog=false（勿开）、m_Sun=Light type1 intensity 1.0 暖白 shadows Type2 Soft
- LightmapSettings: **m_Lightmaps=[] 无烘焙光贴图**（场景=纯实时+烘焙贴图——UNSHADED 直出成立的根基）
- 灯 intensity 1.0 vs --light-energy 1.1（引擎差异校准）；ambient 实际=Emitted 自材质 _ExtraAmbientColor（B2）——**绝不再叠一次**

## B8 现有工具缺失/错误 TOP（应改）
1. **emission 颜色从不写**（L1897-1899；emission=col_str(_EmissionColor)+energy；84 个 EmissionMap 加 emission_texture）
2. **parse_mat L499 只取 _BaseColor or _Color**：Smoke Clouds Light HDR (18.16,7.70,3.23,0.247)/Smoke Clouds (0.811,0.767,0.731,0.149)/Card 3d Stealth (0.126,0.176,0.264) 全被丢——按 shader m_Props 选
3. **scissor 0.5 硬编码**（L1886）→_ClipThreshold/_Cutoff
4. **blend 只看 _Blend>=2**（L1891-1892）→B3 四元组表
5. **roughness=0.9+SPECULAR_DISABLED 一刀切**（L1906-1907）→1-_Smoothness；金属（21 个 _Metallic>0）保留 SCHLICK_GGX+metallic
6. **UNSHADED 一刀切全部非透明材质**——金属/护甲（Card 3d 系/ShellCasing）不能 UNSHADED
7. 未解析 _BumpMap/_BumpScale/_EmissionMap/_Metallic/_Smoothness/_MetallicSpecGlossMap/_Detail*/_Matrix/uv1_scale/uv1_offset/render_priority
8. uv_scroll.gdshader 加 cull_disabled
9. unity_params_to_godot.py _Cull 表更正+MAT_BLEND 换 URP 四元组
10. --light-energy/--ambient-energy 默认改从 JSON 读（1.0/0.41），CLI 仅覆盖
11. glTF alphaMode MASK 分支（gltf_material L1148 只有 BLEND）

## 未读到（标注）
自研 shader HLSL 源码不在解包（只有 m_ParsedForm）；_BaseColorAddSubDiff/_Depth_X_Falloff_Y 等精确公式=按命名+注释推断；Unity AmbientMode 枚举官方值需外网（工具注释可能错）；本地缺 class_basematerial3d.html（已 curl 到 /tmp/bm3.html——**应补入资料库**）

## 关键文件:行号
unity_scene_to_godot.py:437-464(MatInfo)/467-502(parse_mat)/458-460(is_transparent)/1120-1158(gltf_material)/1420-1435(Env)/1855-1908(emit_mat)/2201-2206(smoke_lit)/2402-2437(粒子材质)/732-800(repair)/1512-1523(参数)；unity_params_to_godot.py:11/64-77(MAT_TRANSLATE)/173/179-186(MAT_BLEND 旧枚举)；convert_card_vfx_bundle.py:281-401（材质 0 处理）；Shader_-4055751637662985151.json（URP/Lit props 默认）；Material_3.json:284-318（Vector4_1 滚动/烟雾 HDR）
