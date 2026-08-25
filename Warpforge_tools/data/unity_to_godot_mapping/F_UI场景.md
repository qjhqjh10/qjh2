# Unity 场景结构/UI→Godot 转化映射表（子代理 F 完工版 · 2026-08-25）

> 来源：03_界面UI/菜单 33,020 RT/69,982 MB（唯一组件 35,124）+ battlearena1 场景 1224 GO+原始 JSON 逐字段 + chain_rect/ui_spec_audit/unity_params_to_godot 源码审计。权威=原始 Unity JSON。

## F1 RectTransform→Godot Control 权威公式（E1/E2/E3 三例实证验证）
- anchor 四值：anchor_left=ax0/anchor_right=ax1/**anchor_top=1−ay1/anchor_bottom=1−ay0**（y 翻转）
- offset（相对锚点矩形边）：offset_left=apx−pvx·sdx；offset_right=apx+(1−pvx)·sdx；**offset_top=−(apy+(1−pvy)·sdy)；offset_bottom=−(apy−pvy·sdy)**
- **pivot_offset=(pvx·w, (1−pvy)·h)**（Godot 局部 y 向下——1−pvy！）
- 验证：E1 全拉伸根 (0,0,1,1)→全屏✓（界面索引.md:45）；E2 Timer anchor(0,1) pivot(0,1) pos(209.4,−5) size(248.44,55.9)→chain_rect 实测尺寸精确匹配✓；E3 按钮 anchor(0,1) pivot(0.5,0.5)→(−81,−90 162×180) 与索引.md:187 一致✓
- 坑：sizeDelta≠size（坑10）/拉伸锚 offset 相对锚点矩形边（坑31）/m_Father=Transform 非 GO（:216）/m_LocalScale 转置丢（坑37，rt_scale_map.json）

## F2 UI 组件映射（计数=实测）
- **Canvas**：菜单 126 全 renderMode=2 世界空间；主菜单根 "Game UI"=renderMode=1 ScreenSpaceCamera；BattleHud=renderMode=2+**UI Camera cull=32(layer5)**。CanvasScaler battle=MonoBehaviour_4731：**m_UiScaleMode=1 ScaleWithScreenSize/1920×1080/MatchWidthOrHeight=0 匹配宽度**→viewport 同基准+按 F1 换算（≠照抄）
- **Image 6835**：Simple→TextureRect STRETCH_SCALE/Sliced→NinePatchRect（m_Border（左,下,右,上）→patch 左/上/右/下；坑56 权威表）/Tiled→STRETCH_TILE/Filled→TextureProgressBar（campaign 四件套先例）/m_PreserveAspect→KEEP_ASPECT/m_RaycastTarget→mouse_filter/m_Color→modulate（StyleBox=**modulate_color**，坑91②）
- **TMP 4894**（TMProUGUI 4190+EverguildTMP 663）：**m_fontColor 才是 TMP 颜色（非 m_Color！）**；m_fontSizeBase=36 设计字号；autosize（18/72）→无原生（项目 _set_name_size+get_string_size 缩字）；align H 0-3/V 256-1024→horizontal/vertical_alignment；**wordWrapping→autowrap_mode（需 custom_maximum_size）**；overflowMode→text_overrun_behavior+clip_text；**characterSpacing→Godot 无原生=未映射**；m_isRichText→RichTextLabel+bbcode（坑65）；字号权威表=battlearena1_TMP字号权威表_0824.txt（103 条+颜色；'END TURN' fs31/'Cards left: 2/5' fs42/ERROR 红 (0.80,0,0) fs60）
- **Button 905**（EverguildButton 855）：m_Transition(1 ColorTint) m_Colors 色板 Normal(1,1,1,1)/Highlighted(0.96)/Pressed(0.784)/Disabled(0.784,α0.5)——**项目 ColorTint 权威**；m_OnClick 空=代码绑定；映射=flat=true+子底图+子 Label（坑32/59）/ColorTint→modulate_color+font hover/Icon 用真图标（坑27）/EverguildButtonMaterialModifier 色板=金(0.9,0.64,0.18)/绿(0.37,0.89,0.59)（坑61⑤）
- Toggle 163→CheckBox/自绘（40K_toggle_on-off）；Slider 132→HSlider 主题（Volume_bar StyleBox 须 content_margin 否则 0×0）；ScrollRect 93→ScrollContainer（默认深灰 panel 透明化坑23）+子 Content；Scrollbar→自绘 Handle（style_scroll）；**TMP_Dropdown 11→OptionButton**（40K_dropdown_field_closed/opened）；TMP_InputField 40→LineEdit（placeholder_text/主题 caret+selection：m_CaretColor(0.196)/m_SelectionColor(0.66,0.81,1,0.75)/m_CharacterLimit 26）；Mask/RectMask2D 150→**clip_contents（不可嵌套/不可在 CanvasGroup 内）**；SoftMaskScript→内缩层近似；**CanvasGroup 155→无对等：alpha→modulate/interactable+blocksRaycasts→mouse_filter+process_mode**
- **布局生态（最大盲区）**：AspectRatioFitter 2136/ContentSizeFitter 882/HLG 1229/VLG 188/**GLG 46/LayoutElement 1334**——Godot 对应=size_flags/custom_minimum_size；**项目=算法模拟**（坑63/64/70：分离=separation/pad=offsets/ChildAlignment=alignment；**布局组内元素 anchoredPosition 全 0→chain_rect/audit 失效**）

## F3 相机/灯/环境（原始 JSON 实测）
- BoardCamera FOV 46.397/pos(100,2.22,−13.57)/clearFlags 2/背景(0.0288)/cull 1137(层0,4,5,6,10)/LensShift(0,−0.205)；**UI Camera FOV 40 透视**（=战斗HUD说明.md:32"正交"说法=错！）/cull=32 layer5/pos(−343,0,−18.52)；主菜单 UI Camera 602 FOV40/far 1000
- 灯：m_Type=1 暖白(1.0,0.9568,0.8392)/Intensity 1.0/阴影 Type2（**项目 shadow=false 固化=RT 实证**）/对应坑46/83/85/87 校准历史
- RenderSettings：m_Fog=false（勿开雾坑46）/m_AmbientMode=**3 Trilight**（Sky(1,1,1)/Equator(0.325,0.586,1)/Ground(0.59,0.59,1)/Intensity **0.41**）/**m_AmbientProbe SH DC=(0.289,0.183,−0.080)（坑47：环境光在 SH probe 不在 Trilight）**→WorldEnvironment：BG_COLOR+AMBIENT_SOURCE_COLOR（**BG_COLOR 下 AMBIENT_SOURCE_SKY 不渲染=坑47**）；tonemap=FILMIC（非 ACES）；glow_levels/6+7≈URP Bloom 1.15（坑46）；LUT identity（坑50）/Vignette 0.297→lut_vignette.gdshader
- Camera3D 映射：fov/near/far 直通/背景色→clear color/cullingMask→cull_mask/HDR→viewport/**LensShift→frustum_offset（仅 FRUSTUM 有效——教训"旧实现从未生效"+项目用--lensshift-deg pitch 定案坑89）**/m_Enabled=0→跳过（reflection camera）/多相机→树序

## F4 特殊组件
LineRenderer（CrosshairLine/烟柱）→Line2D/自绘；TrailRenderer 26→粒子 trail 近似（坑71 弱项）；VideoPlayer（菜单 Gacha+battle Video Image）→**VideoStreamPlayer 仅 .ogv（坑1）/D3D12 SubViewport 不渲染（坑12）**（战役视频已转）；SpriteMask 266/VFX Graph 8/ComputeShader 6=无对等记录；SortingGroup→z_index；Cinemachine Vcam→固定相机+曲线；EventSystem/GraphicRaycaster→Godot 无对等（Control 事件）

## F5 UI 动画/特效
- **UI 粒子架构真相**：战斗 HUD=世界空间 Canvas(renderMode=2, layer5)+UI Camera(cull=32)；"Energy Accumulation VFX On/Off"=3D 粒子 GO 挂 layer5 在战场区外——**原版"3D 粒子穿 UI"技巧**（坑52 按 layer 排除）→Godot 等价=CanvasLayer+GPUParticles2D（convert_unity_particles --2d 已做 3 个；坑71）
- 菜单粒子 79（开包粒子已量化坑62 R1-4）；UI 面板进出场=CanvasGroup fade→项目 tween modulate 0.3s（tooltip_manager）；Animator 菜单 0（全 legacy：convert_unity_anim 已转 .tres）

## F6/F7 坑与工具缺口（TOP）
1. **布局组件 3 大类=最大盲区**（chain_rect/audit 全不覆盖，算法模拟已固化 5 例）
2. **TMP/按钮/交互在审计表全盲**：ui_spec_audit comp_summary 只读 m_Sprite/m_text/m_Color/m_fontSize/m_IsActive——**m_fontColor（TMP 真色字段）不读**/Button 零字段/CanvasGroup 155 盲区/legacy Text m_FontData 盲区
3. **07_场景 chain_rect 断层**：world-space Canvas m_LocalScale=0.01 未归一→Clock/OffensiveButton/PlayerDeck 输出 0×0——战场 HUD 工具缺位（绕行 dump_go_tree）
4. **unity_params_to_godot.py:147 pivot_offset 公式 bug**：输出 `pivot.y*size.y` 应为 `(1−pivot.y)*size.y`；**L153 占位未完成**（含"−H*0?"碎串）
5. Everguild 包装类（Button 855/Toggle 151/TMP 663/InputField 28）→按基类字段换算+glow 色板坑61⑤
6. dump_scene_tree.py Slider/ScrollRect 字段名写错（m_SliderValue/m_VerticalScrollPosition）→恒 0

## 文档冲突
战斗HUD说明.md:32 "UI Camera 正交"=错（透视 FOV40）；使用地图:611 renderMode=1 ✓；坑82 白盒探针定案 Z 反射=正确
