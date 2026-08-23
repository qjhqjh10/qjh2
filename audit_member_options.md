# UI 规格审计: Member Options Panel

> 来源: d:/2/解包整理/03_界面UI/菜单 (原始 Unity JSON; 坐标=chain_rect.py v2 算法权威换算) — 生成 2026-08-23 17:47
> 项目: d:/warpforge ; 未命中⚠️元素 = 需人工判断 (动态生成/命名不同/确实缺失)

## 规格表 (说明书期望)

```
Member Options Panel [godot(x766.3 y763.3 w387.4 h0.0)]
  Menu Dark Background [godot(x-1327.3 y-522.9 w4574.6 h2572.4)]
  bg shadow [godot(x733.9 y723.8 w450.5 h79.0)]
  bg [godot(x766.3 y763.3 w387.4 h0.0)]
  Name [txt=Pepito el de siempre godot(x588.8 y763.3 w355.0 h0.0)]
  Buttons [godot(x766.3 y763.3 w0.0 h0.0)]
    Challenge [godot(x587.7 y763.3 w357.3 h0.0)]
      Button Text [txt=Retar godot(x600.4 y763.3 w330.8 h0.0)]
    Add as a friend [godot(x587.7 y763.3 w357.3 h0.0)]
      Button Text [txt=Añadir como amigo godot(x600.4 y763.3 w330.8 h0.0)]
    Profile [godot(x587.7 y763.3 w357.3 h0.0)]
      Button Text [txt=Perfil godot(x600.4 y763.3 w330.8 h0.0)]
    Promote [godot(x587.7 y763.3 w357.3 h0.0)]
      Button Text [txt=Promote godot(x600.4 y763.3 w330.8 h0.0)]
    Demote [godot(x587.7 y763.3 w357.3 h0.0)]
      Button Text [txt=Degradar godot(x600.4 y763.3 w330.8 h0.0)]
    Kick [godot(x587.7 y763.3 w357.3 h0.0)]
      Button Text [txt=Expulsar Jugador godot(x600.4 y763.3 w330.8 h0.0)]
    Quit [godot(x587.7 y763.3 w357.3 h0.0)]
      Button Text [txt=Abandonar Alianza godot(x600.4 y763.3 w330.8 h0.0)]
    Debug Add Skulls [godot(x587.7 y763.3 w357.3 h0.0)]
      Button Text [txt=ADD SKULLS TO CURRENT EVENT godot(x600.4 y763.3 w330.8 h0.0)]
```

## 项目代码命中

| 元素 | 命中 |
|---|---|
| Member Options Panel | ✅ `scripts\social.gd:350 # 操作按钮 (→ Member Options Panel); scripts\social.gd:358 ## 成员操作面板 (说明书 Member Options Panel [766,763 387x0]: ` |
| Menu Dark Background | ✅ `scripts\achievements.gd:114 # 背景 (原版 Menu Dark Background + Fake Background 晕影 + Noise); scripts\base_event_popup.gd:31 csb.bg_col` |
| bg shadow | ⚠️ 未命中 |
| bg | ✅ `scripts\achievements.gd:9 const TEX_BAR_BG := SPR + "40k_campaign_bar_bg.png"        # 进度条底 (0.3,0.29,0.69); scripts\achievements.` |
| Name | ✅ `scripts\battle.gd:57 const CARD_NAME_Y := (-0.77 + 0.5) * CARD2D_KY   # NameTextUnit (0,+0.5) 于 Name 容器 (0,-0.77); scripts\battle.` |
| Buttons | ✅ `scripts\battle.gd:2087 # ===== 回放条 (ReplayButtons chain_rect 权威: (GO143) x[410.2,703.8] y[37.3,94.7] 293.6×57.4 屏幕内顶部,; scripts\ba` |
| Challenge | ✅ `scripts\main_menu.gd:23 const TOP_CHALLENGE := "res://assets/ui/mainmenu/scenes_sprites/40K_icon_duel.png"  # Challenge butt; scri` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Add as a friend | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Profile | ✅ `scripts\main_menu.gd:18 const TOP_PLAYER_FRAME := "res://assets/ui/mainmenu/scenes_sprites/40k_main_player frame.png"  # Pla; scri` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Promote | ✅ `scripts\social.gd:398 ["Promote", func(): _toast("Promoted")],; scripts\social.gd:398 ["Promote", func(): _toast("Promoted")],` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Demote | ✅ `scripts\social.gd:399 ["Demote", func(): _toast("Demoted")],; scripts\social.gd:399 ["Demote", func(): _toast("Demoted")],` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Kick | ✅ `scripts\social.gd:400 ["Kick from Alliance", func(): _toast("Kicked (offline demo)")],; scripts\social.gd:400 ["Kick from Alliance` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Quit | ✅ `scripts\battle.gd:2392 ## + Skip Tutorial + Match Skulls 说明 + Auto Zoom 开关 — 2026-08-21 审查补全: 此前仅标题+Resume+Quit); scripts\battle.g` |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |
| Debug Add Skulls | ⚠️ 未命中 |
| Button Text | ✅ `scripts\card_displayer.gd:407 # Button Text '1' 40px = 通配符消耗数 — 2026-08-21 审查修正: 此前 40K_button + "Craft Copy" 文案); scripts\deck_bu` |

## 摘要

- 规格元素: 22
- 代码命中: 19
- ⚠️未命中: 3 (以下需人工判断)

- `bg shadow`
- `Add as a friend`
- `Debug Add Skulls`