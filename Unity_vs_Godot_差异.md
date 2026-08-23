# Unity → Godot 引擎差异对照（复刻项目适用，2026-08-19）

> 用途：按 Unity JSON（说明文件）复刻时，明确 Unity 概念在 Godot 中如何对应、哪些数值可直接照抄、哪些需转换。
> 分辨率基础：原版 1920×1080（m_ReferenceResolution），项目 viewport 1920×1080，**所有坐标/尺寸数值可直接照抄**。

## 1. 坐标系统（已处理）
| Unity | Godot | 转换 |
|---|---|---|
| 原点左下，y 向上 | 原点左上，y 向下 | `Godot_y = 1080 - Unity_y`（仅绝对坐标换算时需要；**用锚点+offset 时无需**） |
| m_AnchoredPosition + m_SizeDelta + m_Pivot | offset_left/right/top/bottom + anchor_* | `offset_left = ap.x - sd.x*pivot.x` 等（dump_go_tree.py 已内置输出） |

## 2. UI 布局系统（已处理）
- Unity RectTransform（anchorMin/Max + anchoredPosition + sizeDelta + pivot）↔ Godot Control（anchor_left/right/top/bottom + offsets）——**一一对应，dump_go_tree.py 输出 Godot 直用值**
- Unity CanvasScaler（ScaleWithScreenSize、匹配宽度 1920）↔ Godot `stretch/mode="canvas_items"` + `aspect="expand"` + viewport 1920×1080——**已验证等价，JSON 数值直用**

## 3. 组件对照
| Unity 组件 | Godot 对应 | 注意 |
|---|---|---|
| Image（m_Sprite/m_Color） | TextureRect / StyleBoxTexture | 纯图 TextureRect；带 border 用 StyleBoxTexture(texture_margin) |
| Image sliced（m_Border） | StyleBoxTexture.texture_margin_* | **m_Border 四值 → texture_margin 四值直用** |
| TextMeshProUGUI（m_text/m_fontSize） | Label（text/font_size） | fontSize 数值直用（同参考分辨率）；对齐 m_textAlignment→horizontal/vertical_alignment |
| Button（m_Interactable/m_TargetGraphic） | Button（disabled/mouse_default_cursor_shape） | **flat=true 禁用 stylebox 绘制**（坑）；4 态 stylebox |
| Toggle（Background+Checkmark） | CheckButton / 自绘 | 原版 40_main_bt_toggle_on/off 需手动切图 |
| TMP_InputField（Placeholder/Text） | LineEdit（placeholder_text） | 自绘搜索图标做子节点 |
| ScrollRect（Viewport+Content） | ScrollContainer | 自带裁剪；Unity Mask ↔ Godot clip（默认 Container 裁剪） |
| Slider | Slider / 自绘 | 原版 40k_CardAmount_bar_bg/fill 需 HSlider 或 ProgressBar 自绘 |
| VideoPlayer + RawImage | VideoStreamPlayer（.ogv） | **渲染区域 = 节点 rect**；原版视频多为 3840×1080 超宽（已转 1920×540 版） |
| ParticleSystem | GPUParticles2D/3D | 已有 convert_unity_particles.py / convert_arena_particles.py |
| Animator/AnimationClip | AnimationPlayer | 已有 convert_unity_anim.py |
| AudioSource | AudioStreamPlayer | 已有 fsb_audio.py/ogg_build.py |

## 4. 事件与交互
| Unity | Godot | 注意 |
|---|---|---|
| Button.onClick | Button.pressed | 语义一致 |
| PointerEnter/Exit | mouse_entered/mouse_exited | 悬浮特效用（原版 Card Highlight And Shadow） |
| IDragHandler（TouchInputManager） | set_drag_forwarding | drag_threshold 项目默认 ~10px；**微移即拖拽会吞 pressed**（战斗手牌注意） |
| EventSystem raycast | Godot GUI 自动 | 无遮挡问题：全屏 STOP 节点挡住子节点时检查 mouse_filter |

## 5. 资源格式
- SpriteAtlas → 切片独立 PNG（UnityPy image 自动裁，已处理）
- Sprite m_Rect/m_Pivot → 独立 PNG 后天然一致
- 预乘 alpha 损坏需修复（坑已记录）
- 字体：原版 TMP 字体资产不通用 → 项目用 Godot 默认/系统字体（中文显示为项目自适配，原版无中文）
- **视频**：原版 .ogv 3840×1080 → 1920×540 版（4K 解码 GPU 异常，已处理）

## 6. 显示/层级
- m_IsActive ↔ visible（active=false 的元素不显示不交互）
- SortingOrder ↔ z_index（同父级先后顺序优先）
- Canvas Group alpha ↔ modulate（透明过渡）
- **特效铺设注意（用户 2026-08-19）**：原版按钮/图标常挂 hover 动画、进出场动画、粒子——审查时查该元素子节点/Animator 是否有特效，Godot 端需等效实现，不是"放上去"就行

## 7. 已知坑（本项目实战）
1. headless --script 模式 `_process_frame` 不回调（引擎行为）——测试/截图脚本用 `_initialize`+`call_deferred`+`await process_frame` 协程
2. headless `get_image()` 永久阻塞——截图必须窗口模式
3. headless GUI 事件注入不可靠——事件链验证用窗口模式
4. Button.flat=true 禁用 stylebox 绘制
5. 底图当 icon 会"图标+文字并排"分离——底图用 StyleBoxTexture
6. set_anchors_preset(CENTER) 不居中——手动算 offset
7. 拉伸锚点下负 offset 语义不同——FULL_RECT 锚点 + 正/负 offset
8. GPUParticles2D 默认 emitting=true（入树前关）
9. Unity Canvas 是世界空间 vs 屏幕空间——本项目全部屏幕空间（1920×1080）
