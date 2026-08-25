# Unity 纹理/图集→Godot 转化映射表（子代理 C 完工版 · 2026-08-25）

> 来源：bundle 直接 UnityPy 重解验证 + 全库扫描（≥3300 纹理）+ SpriteAtlas/Sprite 原始 JSON + 现有工具代码。数值全部经双次解码一致验证。

## C1 解码链（结论：PNG 已是标准行序，load 进 Godot 无需再翻）
- 链路：bundle Texture2D（DXT/BC）→UnityPy `obj.read().image`（flip=True 默认）→parse_image_data（DXT/BC4×4 补块→Crunched 先解→**FLIP_TOP_BOTTOM** 行序标准）→裁回原尺寸
- Sprite 级 `get_image_from_sprite`：图集定位（m_RenderDataKey→m_RenderDataMap 权威）→textureRect 裁切→settingsRaw 位域（FlipH/FlipV/Rot180/Rot90 :102-123）→Tight 网格精灵 mask 掩码→**末段再 FLIP_TOP_BOTTOM**——**任何 data.image 保存的 PNG=标准图（含 y 翻转+掩码），无需再翻**
- 验证：Back Background 重解=86.9%a0/225.6 与磁盘一致；Black Legion Atlas 2 8192×4096 二次提取 identical；2432 同名一致/650 变体差异
- 格式分布：BC7(25)=2180/DXT5Crunched(29)=201/DXT5=376/RGBA32=173/DXT1=65/BC6H=47/Alpha8=6——**无 16-bit float（"RHalf 损失"论断不成立）**

## C2 alpha 四分类判据（权威裁决顺序：参考图 RT → 材质 keywords/_Cutoff → UV 三角 → 像素统计；禁止只按像素）
- **a) 真设计值**（保持）：Banners a0=77.9% 镂空透光（坑51 灰白矩形教训）、Ground 船影 39-46% 半透明、Background 天空透光、UI 弹窗圆角、SDF 帧 128²
- **b) 解码丢 alpha**（三角内实体化）：**Back Background 86.9%a0+82%padW(白)+225.6 RGB**、Atlas2-mat 内容区 75% a0、Floor rows1311-1551（坑90）、Trait icon atlas a0=74% 但 padW=1.5%（深内容）
- **c) padding/占位**（裁或黑）：卡框 40k_Cardframe 只有 ~31% 子区、卡面 660×1024@(176.5,·)、稀疏图集白 padding（坑89②白斑）
- **d) 图集跨界**（三角掩码区分；Baked 多层 alpha-cut=原版机制坑89③ 勿回退）
- **⚠️ 当前豁免名单 bug**：keep_flat 豁免=文件名 `Floor/Ground/Baked`（:793-795）——**'Battle Arena 1 Back  Background.png' 不在列**→keep_flat 保护其 93.9% flat 白区不实体化→与代码注释（:775 仍实体化）**脱节**；**"全景缺失"最可能剩余点（遗留核查项）**
- 风险：pad_blacken 判据会误伤 ring_warp（设计性白圈 59.3%a0）；convert_card_vfx_bundle/convert_unity_particles 全局判据（>50%a0&RGB>100→全 255）无 UV 区分

## C3 sRGB/线性（实测 m_ColorSpace 分布）
- **=1（sRGB/伽马）99%**：BC7 2180/DXT5/RGBA32/DXT5Crunched/BC6H 全 albedo 卡面 UI 图集——**与 Godot 纹理默认 srgb 采样匹配（项目 .import 无 color_space 键=正确）**
- **=0（线性）~70 张**：RGB24 LUT 系（LUT Normal 256×16 mip9=坑50 identity 直采）、Alpha8 SDF 字体图集 6 张（TMP SDF Godot 不可直用）、Ripple 法线、SmokeLoopAlpha——**需 .import color_space="linear"（当前未设，仅 LUT 无分级影响小）**

## C4 图集→Godot（权威坐标链，全部实测）
1. Sprite JSON：m_Rect=**源纹理 rect（打包前）不可信**（40K_button (0,0,489,107) vs 打包 (1020,964)——实证切片 diff：裁(0,0)=81.48/裁打包+翻转=0.00）；**打包坐标=m_RenderDataMap（键=m_RenderDataKey）**
2. **y 翻转公式（必用）**：png 像素 `(x, atlas_h−rect.y−rect.h, w, h)`（坑80② 两实例：40k_general_popup_simple greyscale 直接裁=0 透明/翻转=312px✓；40k_campaign_Premium-icon 33030 vs 77661）
3. uvTransform=(pixelsToUnits,centerX,pixelsToUnits,centerY)——**是变换矩阵非 UV 偏移，勿当裁剪坐标**
4. 落地=**预裁独立 PNG**（extract_battle_sprites/extract_ui_bundle 用 data.image 全链）→assets/ui/battle/126 张；**全项目 0 处 AtlasTexture**；省显存方案=AtlasTexture{atlas=sactx, region=Rect2(x,h−y−h,w,h), filter_clip=true}
5. 9-slice：Unity border(L,B,R,T)→**NinePatchRect.patch_margin=(L,T,R,B)**（坑56.2 权威表 3 例）；Button=StyleBoxTexture.texture_margin；**flat=true 不渲染=坑32/59**
6. 卡框 frames：阵营帧 1024² 子区（settingsRaw=64 网格裁 660×1024/707×1020）；**TMP SDF 帧 128² 不可直用**
7. Pivot 在"独立 PNG 方案"下天然一致

## C5 压缩/性能
- filter：**全库 filterMode=1 Bilinear（无 Point/Trilinear 一例）**——Godot 默认 linear ✓ 完美匹配
- wrap：1=Clamp（UI/卡）/0=Repeat（VFX/LUT）/**2=Mirror（Baked/BackBG/Atlas2/Aeldari Vortex）**——⚠️ 生成器是否设 texture_repeat 未读到=warning 级核查项
- mip：99% mipCount=1；例外 Explosion_default 2048² mips=12、LUT Normal mips=9（VFX 类）——对 mips>1 开 generate=true
- BC6H HDR（Inbox banner 47 张）未用

## C6 坑清单（全量）
坑51（Banners 误修→灰白矩形 98270→92 根治）/坑89②（白斑 362→87）/**坑51②+80② y 翻转三处**（图集 rect/OBJ v/三角光栅 1-v）/坑56（9-slice LTRB+flat 坑）/坑91②（m_Rect 不可信+StyleBoxTexture 着色=modulate_color）/卡背 thumbs 模糊（128²→thumbs_hi 500×810）/1-2px alpha=0 顶带=设计值勿修（坑56.4）/坑89③ 构图三层定案勿回退/UTP SDF 全拒直用/同名异内容按 PathID 哈希分

## C7 工具缺口
1. **36 张贴图不进 tex_paths**：parse_mat 只认 _BaseMap/_MainTex/_SecondaryTex——_DistortTex 6/_Noise 4/_EmissionMap 4/_MatCap 4/_NoiseTex1-2 8/_SampleTexture2D 6 等槽（粒子材质无贴图→回退 Default-Particle）
2. **slice_ui_atlas.py 已死且错**：输出 0 张；读的 m_Rect 被 extract_ui_bundle.py:71-78 写成同值；未写 RenderDataKey——删除或改走 UnityPy data.image
3. ui_spec_audit:337-345 仅文件名扫描，图集内精灵无独立 PNG 时 <TODO 贴图> 占位；0_mainmenu(4096²)/battleatlasui(2048²)/RewardsAtlas 等**无 slices 目录**
4. **卡背 233 张=原始 1024²（含 158px 左边距+40% a0 双峰）**——原版显示=mesh 裁剪 Sprite 707×1020 区；详情页直拉原图会露边距/透明带（建议裁剪或 thumbs_hi）
5. repair keep_flat 豁免名单缺 Back Background（C2）
6. mips>1 VFX 贴图未建

## 关键索引
unity_scene_to_godot.py:1617-1646(ensure_tex)/732-830(repair)/832-857(pad_blacken)/685-730(三角掩码)；slice_ui_atlas.py；extract_ui_bundle.py:71-78；ui_spec_audit.py:337-345；convert_card_vfx_bundle.py:232-250；convert_unity_particles.py:336-355；SpriteAtlas_403.json；sactx png×3；坑 51:814/56:823/80:1023/89/90:1135/91:1122
