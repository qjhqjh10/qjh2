# Unity 动画/音频资源→Godot 转化映射表（子代理 E 完工版 · 2026-08-25）

> 来源：全库 128 唯一 AnimationClip + 51 Animation 组件 + 16 Animator + 6 AnimatorController + 148 DOTween=动画曲线文件 + AudioSource JSON + 容器头实测 + Warpforge_code 反编译枚举（WrapMode/RotationOrder/Ease/PositionOption 权威）。

## 资源清点
- AnimationClip 128 唯一（57 VFX+卡牌/14 UI/57 场景；说明书计数=文件数×2 的副本件）；legacy 124（曲线明文可转）/非 legacy 4（Card Explosion/Shield Enter-Exit/SporeArmature/Recorded——m_MuscleClip 未导出=**不可恢复**，代码近似）
- 形态键：黑军团 Chain1/Chain2（5 shapes）+ Firepits×2 旋转/位移曲线；VFX 包 22 SMR
- 音频：04_音频 607wav+10ogg（清单 10_资源清单/音频.md:65-683）+07_场景 25 BGM ogg+01_卡牌 245 VO+12_主程序 5wav；**AudioClip 元数据 JSON 全库 0 命中=只能容器头实测**（PCM16 mono 44.1k wav / Vorbis stereo 44.1k ogg；Multiplayer 48000）
- 动画曲线 148 文件=**DOTween 序列化**（tweens.list+references.RefIds：Punch62/ResetBody17/Rotate17/Move14/Shake13/Scale7；**自定义 curve 仅 2 个**）
- AnimInfo：1182→594 唯一（原始全字段 animinfo_0824.json 591 键 99.5% 命中）；运行时 418 键（**口径不同=键名截断，需用 0824 重生成**）

## E1 AnimationClip→Godot Animation
- 曲线节：m_RotationCurves（quat 分量切线）/m_EulerCurves（**m_RotationOrder 几乎全 4=ZXY 合成：q=qY·qX·qZ**；现 convert_unity_anim 反向"四元数→欧拉近似"是错的）/m_PositionCurves/m_ScaleCurves/m_FloatCurves/m_PPtrCurves（仅 1 clip 用，转 TYPE_METHOD）/m_Events（→TYPE_METHOD，例 CardHandToBoardAnimationFinished@0.55s）
- 轨映射：Position→TYPE_POSITION_3D（position_track_insert_key Vector3）；Rotation→TYPE_ROTATION_3D（rotation_track_insert_key Quaternion+**INTERPOLATION_LINEAR_ANGLE 最短球插**——分量线性=错）；Scale→TYPE_SCALE_3D；Float→TYPE_VALUE（路径 "path:属性"）；PPtr→TYPE_METHOD
- **曲线斜率→Godot**（核心公式）：default（weightedMode=0）→cp=(t0+dt/3, v0+outSlope·dt/3)/(t1−dt/3, v1−inSlope·dt/3)；标量→**TYPE_BEZIER**（handle 绝对 Vector2：(t−dt·inW, v−inSlope·dt·inW)/(t+dt·outW, v+outSlope·dt·outW)）；3D 轨统一烘焙 LINEAR（官方建议）
- 属性映射（57 VFX+14 UI clip 全谱实测）：m_AnchoredPosition→链 chain_rect 规则（项目=代码补间）/m_Color.r/g/b/a→modulate/m_Alpha(CanvasGroup)→CanvasGroup:alpha/m_IsActive→visible（**UPDATE_DISCRETE**）/m_Enabled→逐案/m_LocalPosition→position/m_LocalRotation/Scale→rotation_degrees:·/scale:·/m_fontColor→font_color/material._XXX→代码 shader_parameter 补间（**注意原版拼写 _DissolveAmmount×11/_DissolveAmount×2 都在**）/bloomIntensity→Environment.bloom_*/blendShape.Key N-→TYPE_BLEND_SHAPE/m_Intensity→light_energy
- wrapMode（权威=WrapMode.cs）：0 Default→Once/1 Once→LOOP_NONE/2 Loop→LOOP_LINEAR/4 PingPong→LOOP_PINGPONG/**8 ClampForever→LOOP_NONE+末键保持**（ScytheAssault/Resurrection Orb 等 6 个）
- Animation 组件：m_PlayAutomatically→autoplay（**必须先 add_child 再设**）；m_WrapMode 组件级全 0=Default

## E2 Animator→Godot（结论：不需要状态机）
6 个控制器全=单状态单 clip 无参数（m_Values 空）；直接"单 Animation+loop 标志"；m_Loop 状态级（Cannon front Idle=true）/m_Duration/m_Speed/m_CycleOffset→speed_scale/seek；**m_TOS=名称哈希表（解码 m_NameID 必须用它）**；root motion 全 false 忽略

## E3 DOTween→Godot Tween（Ease.cs:5-42 直译表）
Linear→TRANS_LINEAR；Sine/Quad/Cubic/Quart/Quint/Expo/Circ/Elastic/Back/Bounce 三型→TRANS_*+EASE_IN/OUT/IN_OUT（InOutBounce 无单独型→EASE_IN_OUT）；Flash 32-35 无 1:1；easeCurve 自定义 2 例→Curve 资源或 set_custom_interpolate
**⚠️ battle.gd:5672-5675 硬编码 TRANS_QUAD/EASE_OUT=未用表**

## E4 形态键动画（黑军团 Chain）
- clip17 "Black Legion Scene Animation"：**5 形状权重（Chain1 Key2-5/Chain2 Key1-2）+Firepits×2 纯 Y 旋转曲线+Firepits×2 位移**（Loop 15.983s）——**现 clip_curves 只转权重 5 条，Firepits 4 条被判丢弃（1/9）**
- 权重域 Unity 0-100→glTF/Godot 0~1（/100 已做，防御 clamp 建议加）；Godot 轨=TYPE_BLEND_SHAPE（mesh:blend_shapes/<morph name>，glTF 导入器自动生成）
- **⚠️ 主项目 unity_arena_battlearenablacklegion.gd 不挂 Chain11.gltf/SceneAnim**（形态键未接入；完整版在 Warpforge备份/战场演示_暂停归档_0823/ 与 tmp_v12/）
- gltf 路径 61 采样纯 LINEAR（ev() 无 Hermite——保形需按 E1.4 公式采样）

## E5 音频
- 容器→Godot：ogg→AudioStreamOggVorbis（**import loop=false=BGM 接缝断——原版 Loop true+POA true，需改 loop=true**）；wav→AudioStreamWAV（**import compress/mode=2=IMA-ADPCM 有损——循环/计时关键音效改 1**）
- AudioSource→player：m_Volume **线性**→volume_db=linear_to_db（sfx.gd:90 已做；MUSIC_DB=-12=无说明书依据的观感近似=待验证项）/m_Pitch→pitch_scale/Spacialize 全 false→AudioStreamPlayer 2D/OutputAudioMixerGroup 空→建议总线 Music/SFX/Voice
- **617 音效未接入**（sfx.gd 仅 ~40 键；VFX 名→音效名对照表=原版 SoundManager 代码查表=解包无数据=下轮深挖）
- BGM 三层：原版=3 AudioSource 同时挂+AudioSourcesController 音量渐变（DecrementVolume/IncrementVolume）——**set_battle_intensity 需交叉淡入**（现即切）
- VO 45 督军教程语音=教程流程用（接线待确认）

## E6 坑
音频元数据全缺（容器头为准）/OGG loop=false/WAV ADPCM/音量线性↔dB/RotationOrder=4/Quat 分量线性=错/m_IsActive 需 DISCRETE/material 参数名拼写/Blend 权重域/镜像根动画（相机级动画根须移出+共轭）/DOTween≠Curve/末键≠周期（clip17 15.983 vs 15.949=Loop 34ms 停顿——按 SampleRate 归一）/音频总线建议

## E7 工具缺失 TOP
1. clip_curves 只取 blendShape 权重（Firepits 4 曲线丢弃=1/9）
2. 主项目黑军团场景不挂 Chain11.gltf/SceneAnim
3. clip16 Camera Intro 只取 pos 首末键+只动 pitch（Euler y/z/中间键/速度曲线全丢+无缓动）
4. convert_unity_anim：RotationOrder 不处理/无 slerp/PingPong→错映射 loop=1/ATTR_MAP 仅 8 条/无 slope
5. **7 个 BattleHud clip 完全未转换**（HUD 滑入/淡出全缺——battle.gd 直接 visible）
6. animinfo_lookup 418 键口径错（用 0824 重生成）+battle.gd 只消费 tm（easeCurve/sp/ep/move/screenShake 未接）
7. 4 非 legacy clip=不可恢复（已近似）
8. 说明书计数含副本件（口径注明"唯一数"）

## 推荐管线
legacy clip 124→Godot Animation（E1.2 矩阵）；形态键=glTF 路线+3 修（Hermite/补 Firepits/接回主项目）；Animator×6→单 Animation 表；DOTween→Tween 查表；音频=直拷+3 修（music loop/关键 wav PCM/set_battle_intensity 淡入）

## 未读到
AudioClip JSON 全字段/AudioMixerController 组与参数/targetUnit semantics/audio_streamplayer.html=404 占位（API 按 4.7 知识）
