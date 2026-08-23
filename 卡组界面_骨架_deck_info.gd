# UI 骨架自动生成 (ui_spec_audit.py --gen-godot; 坐标=chain_rect 权威绝对屏幕坐标)
# 用法: 整个函数粘贴进界面脚本 (extends Control), _ready 里调用 _ui_stub(); 手工处理 TODO 处 (信号/Button 类型)
func _ui_stub() -> void:
	# Deck info Popup (原版 GO pid=-4402140163719919192)
	var Deck_info_Popup := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_info_Popup.name = "Deck info Popup"
	Deck_info_Popup.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_info_Popup.offset_left = 0
	Deck_info_Popup.offset_top = 0
	Deck_info_Popup.offset_right = 1920
	Deck_info_Popup.offset_bottom = 1080
	add_child(Deck_info_Popup)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Menu Dark Background (原版 GO pid=5609092133016799656)
	var Menu_Dark_Background := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Menu_Dark_Background.name = "Menu Dark Background"
	Menu_Dark_Background.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Menu_Dark_Background.offset_left = -1327.3
	Menu_Dark_Background.offset_top = -746.18
	Menu_Dark_Background.offset_right = 3247.3
	Menu_Dark_Background.offset_bottom = 1826.18
	add_child(Menu_Dark_Background)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Generic Window Red Background Big (原版 GO pid=-1806349429157623384)
	var Generic_Window_Red_Background_Big := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Generic_Window_Red_Background_Big.name = "Generic Window Red Background Big"
	Generic_Window_Red_Background_Big.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Generic_Window_Red_Background_Big.offset_left = 134.5
	Generic_Window_Red_Background_Big.offset_top = 82
	Generic_Window_Red_Background_Big.offset_right = 1839.5
	Generic_Window_Red_Background_Big.offset_bottom = 1032
	add_child(Generic_Window_Red_Background_Big)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Warlord Image (原版 GO pid=-6735770576364533336)
	var Warlord_Image := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Warlord_Image.name = "Warlord Image"
	Warlord_Image.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Warlord_Image.offset_left = -108.98
	Warlord_Image.offset_top = -33.99
	Warlord_Image.offset_right = 999.02
	Warlord_Image.offset_bottom = 1074
	add_child(Warlord_Image)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck Details (原版 GO pid=-4684002234477344344)
	var Deck_Details := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_Details.name = "Deck Details"
	Deck_Details.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_Details.offset_left = 659
	Deck_Details.offset_top = 106.1
	Deck_Details.offset_right = 1329.84
	Deck_Details.offset_bottom = 217.3
	add_child(Deck_Details)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Game Mode Icon (原版 GO pid=-3697130443239552600)
	var Game_Mode_Icon := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Game_Mode_Icon.name = "Game Mode Icon"
	Game_Mode_Icon.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Game_Mode_Icon.offset_left = 659
	Game_Mode_Icon.offset_top = 162.3
	Game_Mode_Icon.offset_right = 759
	Game_Mode_Icon.offset_bottom = 272.3
	add_child(Game_Mode_Icon)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Game Mode Separator (原版 GO pid=-7198048626225215064)
	var Game_Mode_Separator := TextureRect.new()
	Game_Mode_Separator.texture = load("res://assets/ui/mainmenu/menus_assets_all/40k_Generic Smooth line.png")   # 原版 sprite=40k_Generic Smooth line
	Game_Mode_Separator.name = "Game Mode Separator"
	Game_Mode_Separator.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Game_Mode_Separator.offset_left = 659
	Game_Mode_Separator.offset_top = 162.3
	Game_Mode_Separator.offset_right = 667.87
	Game_Mode_Separator.offset_bottom = 272.3
	add_child(Game_Mode_Separator)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck Details (原版 GO pid=437809300479445416)
	var Deck_Details_2 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_Details_2.name = "Deck Details"
	Deck_Details_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_Details_2.offset_left = 363.1
	Deck_Details_2.offset_top = 161.7
	Deck_Details_2.offset_right = 954.9
	Deck_Details_2.offset_bottom = 272.9
	add_child(Deck_Details_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck Name (原版 GO pid=-290753778423461464)
	var Deck_Name := Label.new()
	Deck_Name.add_theme_font_size_override("font_size", 44)
	Deck_Name.text = "DECK NAME"   # 原版 m_text
	Deck_Name.name = "Deck Name"
	Deck_Name.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_Name.offset_left = 468.1
	Deck_Name.offset_top = 170.05
	Deck_Name.offset_right = 953.7
	Deck_Name.offset_bottom = 224.55
	add_child(Deck_Name)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Army Icon (原版 GO pid=-8591164184527599192)
	var Army_Icon := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Army_Icon.name = "Army Icon"
	Army_Icon.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Army_Icon.offset_left = 363.1
	Army_Icon.offset_top = 162.3
	Army_Icon.offset_right = 463.1
	Army_Icon.offset_bottom = 272.3
	add_child(Army_Icon)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Warlord Name (原版 GO pid=-7270839655137113688)
	var Warlord_Name := Label.new()
	Warlord_Name.add_theme_font_size_override("font_size", 40)
	Warlord_Name.text = "Warlord name"   # 原版 m_text
	Warlord_Name.name = "Warlord Name"
	Warlord_Name.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Warlord_Name.offset_left = 468.1
	Warlord_Name.offset_top = 222.3
	Warlord_Name.offset_right = 955.1
	Warlord_Name.offset_bottom = 272.3
	add_child(Warlord_Name)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Buttons (原版 GO pid=-1990530920041838168)
	var Buttons := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Buttons.name = "Buttons"
	Buttons.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Buttons.offset_left = 669.3
	Buttons.offset_top = 885.81
	Buttons.offset_right = 1770.7
	Buttons.offset_bottom = 965.91
	add_child(Buttons)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Practice Deck (原版 GO pid=87525286650677672)
	var Practice_Deck := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Practice_Deck.name = "Practice Deck"
	Practice_Deck.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Practice_Deck.offset_left = 344.8
	Practice_Deck.offset_top = 925.86
	Practice_Deck.offset_right = 669.3
	Practice_Deck.offset_bottom = 1005.96
	add_child(Practice_Deck)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Button Text (原版 GO pid=-5808072720119723608)
	var Button_Text := Label.new()
	Button_Text.add_theme_font_size_override("font_size", 40)
	Button_Text.text = "Práctica"   # 原版 m_text
	Button_Text.name = "Button Text"
	Button_Text.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Button_Text.offset_left = 359.32
	Button_Text.offset_top = 933.69
	Button_Text.offset_right = 653.73
	Button_Text.offset_bottom = 998.09
	add_child(Button_Text)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Edit Deck (原版 GO pid=3764344879984970152)
	var Edit_Deck := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Edit_Deck.name = "Edit Deck"
	Edit_Deck.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Edit_Deck.offset_left = 344.8
	Edit_Deck.offset_top = 925.86
	Edit_Deck.offset_right = 669.3
	Edit_Deck.offset_bottom = 1005.96
	add_child(Edit_Deck)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Button Text (原版 GO pid=7777757045402012072)
	var Button_Text_2 := Label.new()
	Button_Text_2.add_theme_font_size_override("font_size", 40)
	Button_Text_2.text = "Editar"   # 原版 m_text
	Button_Text_2.name = "Button Text"
	Button_Text_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Button_Text_2.offset_left = 359.32
	Button_Text_2.offset_top = 933.69
	Button_Text_2.offset_right = 653.73
	Button_Text_2.offset_bottom = 998.09
	add_child(Button_Text_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Select Deck (原版 GO pid=-2762387755822970456)
	var Select_Deck := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Select_Deck.name = "Select Deck"
	Select_Deck.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Select_Deck.offset_left = 344.8
	Select_Deck.offset_top = 925.86
	Select_Deck.offset_right = 669.3
	Select_Deck.offset_bottom = 1005.96
	add_child(Select_Deck)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Button Text (原版 GO pid=-5713133855230031448)
	var Button_Text_3 := Label.new()
	Button_Text_3.add_theme_font_size_override("font_size", 40)
	Button_Text_3.text = "Seleccionar"   # 原版 m_text
	Button_Text_3.name = "Button Text"
	Button_Text_3.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Button_Text_3.offset_left = 359.32
	Button_Text_3.offset_top = 933.69
	Button_Text_3.offset_right = 653.73
	Button_Text_3.offset_bottom = 998.09
	add_child(Button_Text_3)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck Options (原版 GO pid=-6650388652169066072)
	var Deck_Options := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_Options.name = "Deck Options"
	Deck_Options.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_Options.offset_left = 1263.74
	Deck_Options.offset_top = 93
	Deck_Options.offset_right = 1783.62
	Deck_Options.offset_bottom = 243
	add_child(Deck_Options)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Switch Deck Info Button (原版 GO pid=8747309826094762408)
	var Switch_Deck_Info_Button := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Switch_Deck_Info_Button.name = "Switch Deck Info Button"
	Switch_Deck_Info_Button.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Switch_Deck_Info_Button.offset_left = 1226.55
	Switch_Deck_Info_Button.offset_top = 205.2
	Switch_Deck_Info_Button.offset_right = 1300.93
	Switch_Deck_Info_Button.offset_bottom = 280.8
	add_child(Switch_Deck_Info_Button)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-3652700642612246104)
	var Background := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background.name = "Background"
	Background.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background.offset_left = 1234.7
	Background.offset_top = 213.18
	Background.offset_right = 1291.56
	Background.offset_bottom = 271.3
	add_child(Background)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Icon (原版 GO pid=2411625793357646248)
	var Icon := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Icon.name = "Icon"
	Icon.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Icon.offset_left = 1234.7
	Icon.offset_top = 213.18
	Icon.offset_right = 1291.56
	Icon.offset_bottom = 271.3
	add_child(Icon)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Duplicate Button (原版 GO pid=-7973835643830695512)
	var Duplicate_Button := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Duplicate_Button.name = "Duplicate Button"
	Duplicate_Button.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Duplicate_Button.offset_left = 1226.55
	Duplicate_Button.offset_top = 205.2
	Duplicate_Button.offset_right = 1300.93
	Duplicate_Button.offset_bottom = 280.8
	add_child(Duplicate_Button)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-5741544880533173848)
	var Background_2 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_2.name = "Background"
	Background_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_2.offset_left = 1234.7
	Background_2.offset_top = 213.18
	Background_2.offset_right = 1291.56
	Background_2.offset_bottom = 271.3
	add_child(Background_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Icon (原版 GO pid=-1888595073814853208)
	var Icon_2 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Icon_2.name = "Icon"
	Icon_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Icon_2.offset_left = 1234.7
	Icon_2.offset_top = 213.18
	Icon_2.offset_right = 1291.56
	Icon_2.offset_bottom = 271.3
	add_child(Icon_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Share Button (原版 GO pid=8159457256253327784)
	var Share_Button := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Share_Button.name = "Share Button"
	Share_Button.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Share_Button.offset_left = 1226.55
	Share_Button.offset_top = 205.2
	Share_Button.offset_right = 1300.93
	Share_Button.offset_bottom = 280.8
	add_child(Share_Button)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-1474738656115979864)
	var Background_3 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_3.name = "Background"
	Background_3.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_3.offset_left = 1234.7
	Background_3.offset_top = 213.18
	Background_3.offset_right = 1291.56
	Background_3.offset_bottom = 271.3
	add_child(Background_3)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Icon (原版 GO pid=1782555166114089384)
	var Icon_3 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Icon_3.name = "Icon"
	Icon_3.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Icon_3.offset_left = 1234.7
	Icon_3.offset_top = 213.18
	Icon_3.offset_right = 1291.56
	Icon_3.offset_bottom = 271.3
	add_child(Icon_3)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Share On Chat (原版 GO pid=747779688961116584)
	var Share_On_Chat := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Share_On_Chat.name = "Share On Chat"
	Share_On_Chat.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Share_On_Chat.offset_left = 1226.55
	Share_On_Chat.offset_top = 205.2
	Share_On_Chat.offset_right = 1300.93
	Share_On_Chat.offset_bottom = 280.8
	add_child(Share_On_Chat)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=7903880063633557928)
	var Background_4 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_4.name = "Background"
	Background_4.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_4.offset_left = 1234.7
	Background_4.offset_top = 213.18
	Background_4.offset_right = 1291.56
	Background_4.offset_bottom = 271.3
	add_child(Background_4)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Icon (原版 GO pid=2796729937614506408)
	var Icon_4 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Icon_4.name = "Icon"
	Icon_4.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Icon_4.offset_left = 1234.7
	Icon_4.offset_top = 213.18
	Icon_4.offset_right = 1291.56
	Icon_4.offset_bottom = 271.3
	add_child(Icon_4)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Delete Button (原版 GO pid=-133312745514956376)
	var Delete_Button := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Delete_Button.name = "Delete Button"
	Delete_Button.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Delete_Button.offset_left = 1226.55
	Delete_Button.offset_top = 205.2
	Delete_Button.offset_right = 1300.93
	Delete_Button.offset_bottom = 280.8
	add_child(Delete_Button)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-2030358483163248216)
	var Background_5 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_5.name = "Background"
	Background_5.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_5.offset_left = 1234.7
	Background_5.offset_top = 213.18
	Background_5.offset_right = 1291.56
	Background_5.offset_bottom = 271.3
	add_child(Background_5)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Icon (原版 GO pid=5427167081675131304)
	var Icon_5 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Icon_5.name = "Icon"
	Icon_5.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Icon_5.offset_left = 1234.7
	Icon_5.offset_top = 213.18
	Icon_5.offset_right = 1291.56
	Icon_5.offset_bottom = 271.3
	add_child(Icon_5)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Info Panel (原版 GO pid=-1987138722815768152)
	var Info_Panel := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Info_Panel.name = "Info Panel"
	Info_Panel.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Info_Panel.offset_left = 659
	Info_Panel.offset_top = 218.1
	Info_Panel.offset_right = 1799
	Info_Panel.offset_bottom = 868.1
	add_child(Info_Panel)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck List (原版 GO pid=-5961826162901939800)
	var Deck_List := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_List.name = "Deck List"
	Deck_List.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_List.offset_left = 659
	Deck_List.offset_top = 218.1
	Deck_List.offset_right = 1799
	Deck_List.offset_bottom = 868.1
	add_child(Deck_List)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Content (原版 GO pid=5907272997049108904)
	var Content := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Content.name = "Content"
	Content.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Content.offset_left = 659
	Content.offset_top = 218.1
	Content.offset_right = 1799
	Content.offset_bottom = 868.1
	add_child(Content)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck Selector Card Info button (原版 GO pid=2994867481076140456)
	var Deck_Selector_Card_Info_button := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_Selector_Card_Info_button.name = "Deck Selector Card Info button"
	Deck_Selector_Card_Info_button.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_Selector_Card_Info_button.offset_left = 659
	Deck_Selector_Card_Info_button.offset_top = 868.1
	Deck_Selector_Card_Info_button.offset_right = 659
	Deck_Selector_Card_Info_button.offset_bottom = 868.1
	add_child(Deck_Selector_Card_Info_button)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Content (原版 GO pid=-7679470253512357464)
	var Content_2 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Content_2.name = "Content"
	Content_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Content_2.offset_left = 659
	Content_2.offset_top = 868.1
	Content_2.offset_right = 659
	Content_2.offset_bottom = 868.1
	add_child(Content_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=2598074037214874024)
	var Background_6 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_6.name = "Background"
	Background_6.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_6.offset_left = 659
	Background_6.offset_top = 868.1
	Background_6.offset_right = 659
	Background_6.offset_bottom = 868.1
	add_child(Background_6)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Rarity Gradient (原版 GO pid=-6316424082366494296)
	var Rarity_Gradient := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Rarity_Gradient.name = "Rarity Gradient"
	Rarity_Gradient.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Rarity_Gradient.offset_left = 658.55
	Rarity_Gradient.offset_top = 868.1
	Rarity_Gradient.offset_right = 659
	Rarity_Gradient.offset_bottom = 867.99
	add_child(Rarity_Gradient)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background Border (原版 GO pid=7632206211278997928)
	var Background_Border := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_Border.name = "Background Border"
	Background_Border.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_Border.offset_left = 642.66
	Background_Border.offset_top = 868.1
	Background_Border.offset_right = 659
	Background_Border.offset_bottom = 868.1
	add_child(Background_Border)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cost Image (原版 GO pid=5116550742365997480)
	var Cost_Image := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Cost_Image.name = "Cost Image"
	Cost_Image.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cost_Image.offset_left = 658.82
	Cost_Image.offset_top = 865.1
	Cost_Image.offset_right = 658.82
	Cost_Image.offset_bottom = 871.1
	add_child(Cost_Image)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cost (原版 GO pid=-6382713825537717848)
	var Cost := Label.new()
	Cost.add_theme_font_size_override("font_size", 50)
	Cost.text = "5"   # 原版 m_text
	Cost.name = "Cost"
	Cost.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cost.offset_left = 634.41
	Cost.offset_top = 865.77
	Cost.offset_right = 683.23
	Cost.offset_bottom = 870.43
	add_child(Cost)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# banned Icon (原版 GO pid=-1953084190287492696)
	var banned_Icon := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	banned_Icon.name = "banned Icon"
	banned_Icon.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	banned_Icon.offset_left = 655.9
	banned_Icon.offset_top = 861.99
	banned_Icon.offset_right = 655.9
	banned_Icon.offset_bottom = 867.99
	add_child(banned_Icon)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Text fill (原版 GO pid=4259737316137666984)
	var Text_fill := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Text_fill.name = "Text fill"
	Text_fill.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Text_fill.offset_left = 659
	Text_fill.offset_top = 868.1
	Text_fill.offset_right = 654
	Text_fill.offset_bottom = 868.1
	add_child(Text_fill)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Name (原版 GO pid=-1415568086583637592)
	var Card_Name := Label.new()
	Card_Name.add_theme_font_size_override("font_size", 38)
	Card_Name.text = "Card Name"   # 原版 m_text
	Card_Name.name = "Card Name"
	Card_Name.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Name.offset_left = 659
	Card_Name.offset_top = 868.1
	Card_Name.offset_right = 659
	Card_Name.offset_bottom = 868.1
	add_child(Card_Name)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Count (原版 GO pid=-6456593523228767832)
	var Count := Label.new()
	Count.add_theme_font_size_override("font_size", 32)
	Count.text = "x2"   # 原版 m_text
	Count.name = "Count"
	Count.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Count.offset_left = 659
	Count.offset_top = 868.1
	Count.offset_right = 659
	Count.offset_bottom = 868.1
	add_child(Count)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck Info (原版 GO pid=-2234076232798205528)
	var Deck_Info := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_Info.name = "Deck Info"
	Deck_Info.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_Info.offset_left = 659
	Deck_Info.offset_top = 218.1
	Deck_Info.offset_right = 1799
	Deck_Info.offset_bottom = 868.1
	add_child(Deck_Info)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Lore Text [原版隐藏] (原版 GO pid=1419208951706519976)
	var Lore_Text := Label.new()
	Lore_Text.add_theme_font_size_override("font_size", 28)
	Lore_Text.text = "Start here! Overwhelm your opponent with endless tides of Orks."   # 原版 m_text
	Lore_Text.name = "Lore Text"
	Lore_Text.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Lore_Text.offset_left = 1014
	Lore_Text.offset_top = 667.26
	Lore_Text.offset_right = 1458.16
	Lore_Text.offset_bottom = 807.66
	Lore_Text.visible = false   # 原版 m_IsActive=0
	add_child(Lore_Text)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cardback (原版 GO pid=823622314319841704)
	var Cardback := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Cardback.name = "Cardback"
	Cardback.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cardback.offset_left = 1271.75
	Cardback.offset_top = 270.47
	Cardback.offset_right = 1660.25
	Cardback.offset_bottom = 834.72
	add_child(Cardback)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cardback Front (原版 GO pid=-3191159665266357848)
	var Cardback_Front := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Cardback_Front.name = "Cardback Front"
	Cardback_Front.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cardback_Front.offset_left = 1292.88
	Cardback_Front.offset_top = 263.87
	Cardback_Front.offset_right = 1680.56
	Cardback_Front.offset_bottom = 823.19
	add_child(Cardback_Front)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck Information Cost/balance text (原版 GO pid=-5409665404060989016)
	var Deck_Information_Cost_balance_text := Label.new()
	Deck_Information_Cost_balance_text.add_theme_font_size_override("font_size", 44)
	Deck_Information_Cost_balance_text.text = "Cartas / Coste"   # 原版 m_text
	Deck_Information_Cost_balance_text.name = "Deck Information Cost/balance text"
	Deck_Information_Cost_balance_text.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_Information_Cost_balance_text.offset_left = 740.05
	Deck_Information_Cost_balance_text.offset_top = 305.6
	Deck_Information_Cost_balance_text.offset_right = 1213.75
	Deck_Information_Cost_balance_text.offset_bottom = 365.6
	add_child(Deck_Information_Cost_balance_text)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck Information cost drawer (原版 GO pid=2985515044265626024)
	var Deck_Information_cost_drawer := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_Information_cost_drawer.name = "Deck Information cost drawer"
	Deck_Information_cost_drawer.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_Information_cost_drawer.offset_left = 825.4
	Deck_Information_cost_drawer.offset_top = 378.82
	Deck_Information_cost_drawer.offset_right = 1113.4
	Deck_Information_cost_drawer.offset_bottom = 738.82
	add_child(Deck_Information_cost_drawer)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=5033467469734316456)
	var Background_7 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_7.name = "Background"
	Background_7.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_7.offset_left = 827.06
	Background_7.offset_top = 379.67
	Background_7.offset_right = 1111.73
	Background_7.offset_bottom = 737.97
	add_child(Background_7)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Content (原版 GO pid=-3420151324237198936)
	var Content_3 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Content_3.name = "Content"
	Content_3.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Content_3.offset_left = 768.17
	Content_3.offset_top = 379.67
	Content_3.offset_right = 1170.63
	Content_3.offset_bottom = 737.97
	add_child(Content_3)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (原版 GO pid=2404291423583766952)
	var Deck_CostQuanityt_Row_Drawer := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer.name = "Deck CostQuanityt Row Drawer"
	Deck_CostQuanityt_Row_Drawer.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=6128682608225847720)
	var Card_Cost := Label.new()
	Card_Cost.add_theme_font_size_override("font_size", 25)
	Card_Cost.text = "0"   # 原版 m_text
	Card_Cost.name = "Card Cost"
	Card_Cost.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost.offset_left = 573.01
	Card_Cost.offset_top = 720.06
	Card_Cost.offset_right = 619.02
	Card_Cost.offset_bottom = 755.89
	add_child(Card_Cost)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=-536884398052767320)
	var Cards_in_deck := Label.new()
	Cards_in_deck.add_theme_font_size_override("font_size", 25)
	Cards_in_deck.text = "0"   # 原版 m_text
	Cards_in_deck.name = "Cards in deck"
	Cards_in_deck.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck.offset_left = 916.58
	Cards_in_deck.offset_top = 719.97
	Cards_in_deck.offset_right = 962.59
	Cards_in_deck.offset_bottom = 755.97
	add_child(Cards_in_deck)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=7730843803244530088)
	var Slider := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider.name = "Slider"
	Slider.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider.offset_left = 631.96
	Slider.offset_top = 719.97
	Slider.offset_right = 904.37
	Slider.offset_bottom = 755.97
	add_child(Slider)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-6817812909785642584)
	var Background_8 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_8.name = "Background"
	Background_8.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_8.offset_left = 631.96
	Background_8.offset_top = 723.55
	Background_8.offset_right = 904.37
	Background_8.offset_bottom = 753.38
	add_child(Background_8)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=8142242727857392040)
	var Fill := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill.name = "Fill"
	Fill.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill.offset_left = 631.96
	Fill.offset_top = 760.24
	Fill.offset_right = 631.96
	Fill.offset_bottom = 751.71
	add_child(Fill)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (1) (原版 GO pid=7018426048797706664)
	var Deck_CostQuanityt_Row_Drawer__1_ := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer__1_.name = "Deck CostQuanityt Row Drawer (1)"
	Deck_CostQuanityt_Row_Drawer__1_.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer__1_.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer__1_.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer__1_.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer__1_.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer__1_)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=3818172269714246056)
	var Card_Cost_2 := Label.new()
	Card_Cost_2.add_theme_font_size_override("font_size", 25)
	Card_Cost_2.text = "0"   # 原版 m_text
	Card_Cost_2.name = "Card Cost"
	Card_Cost_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost_2.offset_left = 573.01
	Card_Cost_2.offset_top = 720.06
	Card_Cost_2.offset_right = 619.02
	Card_Cost_2.offset_bottom = 755.89
	add_child(Card_Cost_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=-2480160756600305240)
	var Cards_in_deck_2 := Label.new()
	Cards_in_deck_2.add_theme_font_size_override("font_size", 25)
	Cards_in_deck_2.text = "0"   # 原版 m_text
	Cards_in_deck_2.name = "Cards in deck"
	Cards_in_deck_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck_2.offset_left = 916.58
	Cards_in_deck_2.offset_top = 719.97
	Cards_in_deck_2.offset_right = 962.59
	Cards_in_deck_2.offset_bottom = 755.97
	add_child(Cards_in_deck_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=-5039208690425296472)
	var Slider_2 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider_2.name = "Slider"
	Slider_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider_2.offset_left = 631.96
	Slider_2.offset_top = 719.97
	Slider_2.offset_right = 904.37
	Slider_2.offset_bottom = 755.97
	add_child(Slider_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-4086507367820916312)
	var Background_9 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_9.name = "Background"
	Background_9.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_9.offset_left = 631.96
	Background_9.offset_top = 723.55
	Background_9.offset_right = 904.37
	Background_9.offset_bottom = 753.38
	add_child(Background_9)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=-5568121545459201624)
	var Fill_2 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill_2.name = "Fill"
	Fill_2.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill_2.offset_left = 631.96
	Fill_2.offset_top = 760.24
	Fill_2.offset_right = 631.96
	Fill_2.offset_bottom = 751.71
	add_child(Fill_2)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (2) (原版 GO pid=3989655189797702056)
	var Deck_CostQuanityt_Row_Drawer__2_ := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer__2_.name = "Deck CostQuanityt Row Drawer (2)"
	Deck_CostQuanityt_Row_Drawer__2_.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer__2_.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer__2_.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer__2_.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer__2_.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer__2_)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=-568687358903613016)
	var Card_Cost_3 := Label.new()
	Card_Cost_3.add_theme_font_size_override("font_size", 25)
	Card_Cost_3.text = "0"   # 原版 m_text
	Card_Cost_3.name = "Card Cost"
	Card_Cost_3.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost_3.offset_left = 573.01
	Card_Cost_3.offset_top = 720.06
	Card_Cost_3.offset_right = 619.02
	Card_Cost_3.offset_bottom = 755.89
	add_child(Card_Cost_3)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=2837721445167237544)
	var Cards_in_deck_3 := Label.new()
	Cards_in_deck_3.add_theme_font_size_override("font_size", 25)
	Cards_in_deck_3.text = "0"   # 原版 m_text
	Cards_in_deck_3.name = "Cards in deck"
	Cards_in_deck_3.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck_3.offset_left = 916.58
	Cards_in_deck_3.offset_top = 719.97
	Cards_in_deck_3.offset_right = 962.59
	Cards_in_deck_3.offset_bottom = 755.97
	add_child(Cards_in_deck_3)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=2133092245226817960)
	var Slider_3 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider_3.name = "Slider"
	Slider_3.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider_3.offset_left = 631.96
	Slider_3.offset_top = 719.97
	Slider_3.offset_right = 904.37
	Slider_3.offset_bottom = 755.97
	add_child(Slider_3)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-4830675080672015960)
	var Background_10 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_10.name = "Background"
	Background_10.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_10.offset_left = 631.96
	Background_10.offset_top = 723.55
	Background_10.offset_right = 904.37
	Background_10.offset_bottom = 753.38
	add_child(Background_10)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=688185432097458600)
	var Fill_3 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill_3.name = "Fill"
	Fill_3.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill_3.offset_left = 631.96
	Fill_3.offset_top = 760.24
	Fill_3.offset_right = 631.96
	Fill_3.offset_bottom = 751.71
	add_child(Fill_3)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (3) (原版 GO pid=992598853595007400)
	var Deck_CostQuanityt_Row_Drawer__3_ := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer__3_.name = "Deck CostQuanityt Row Drawer (3)"
	Deck_CostQuanityt_Row_Drawer__3_.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer__3_.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer__3_.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer__3_.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer__3_.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer__3_)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=-5996536895391757912)
	var Card_Cost_4 := Label.new()
	Card_Cost_4.add_theme_font_size_override("font_size", 25)
	Card_Cost_4.text = "0"   # 原版 m_text
	Card_Cost_4.name = "Card Cost"
	Card_Cost_4.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost_4.offset_left = 573.01
	Card_Cost_4.offset_top = 720.06
	Card_Cost_4.offset_right = 619.02
	Card_Cost_4.offset_bottom = 755.89
	add_child(Card_Cost_4)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=-8612494170519533144)
	var Cards_in_deck_4 := Label.new()
	Cards_in_deck_4.add_theme_font_size_override("font_size", 25)
	Cards_in_deck_4.text = "0"   # 原版 m_text
	Cards_in_deck_4.name = "Cards in deck"
	Cards_in_deck_4.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck_4.offset_left = 916.58
	Cards_in_deck_4.offset_top = 719.97
	Cards_in_deck_4.offset_right = 962.59
	Cards_in_deck_4.offset_bottom = 755.97
	add_child(Cards_in_deck_4)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=8456720808701954472)
	var Slider_4 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider_4.name = "Slider"
	Slider_4.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider_4.offset_left = 631.96
	Slider_4.offset_top = 719.97
	Slider_4.offset_right = 904.37
	Slider_4.offset_bottom = 755.97
	add_child(Slider_4)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=1045797220734044584)
	var Background_11 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_11.name = "Background"
	Background_11.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_11.offset_left = 631.96
	Background_11.offset_top = 723.55
	Background_11.offset_right = 904.37
	Background_11.offset_bottom = 753.38
	add_child(Background_11)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=6027051573829732776)
	var Fill_4 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill_4.name = "Fill"
	Fill_4.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill_4.offset_left = 631.96
	Fill_4.offset_top = 760.24
	Fill_4.offset_right = 631.96
	Fill_4.offset_bottom = 751.71
	add_child(Fill_4)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (4) (原版 GO pid=3019116363328358824)
	var Deck_CostQuanityt_Row_Drawer__4_ := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer__4_.name = "Deck CostQuanityt Row Drawer (4)"
	Deck_CostQuanityt_Row_Drawer__4_.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer__4_.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer__4_.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer__4_.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer__4_.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer__4_)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=-8447063191315445336)
	var Card_Cost_5 := Label.new()
	Card_Cost_5.add_theme_font_size_override("font_size", 25)
	Card_Cost_5.text = "0"   # 原版 m_text
	Card_Cost_5.name = "Card Cost"
	Card_Cost_5.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost_5.offset_left = 573.01
	Card_Cost_5.offset_top = 720.06
	Card_Cost_5.offset_right = 619.02
	Card_Cost_5.offset_bottom = 755.89
	add_child(Card_Cost_5)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=-4796297468852467288)
	var Cards_in_deck_5 := Label.new()
	Cards_in_deck_5.add_theme_font_size_override("font_size", 25)
	Cards_in_deck_5.text = "0"   # 原版 m_text
	Cards_in_deck_5.name = "Cards in deck"
	Cards_in_deck_5.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck_5.offset_left = 916.58
	Cards_in_deck_5.offset_top = 719.97
	Cards_in_deck_5.offset_right = 962.59
	Cards_in_deck_5.offset_bottom = 755.97
	add_child(Cards_in_deck_5)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=-8913505618252822104)
	var Slider_5 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider_5.name = "Slider"
	Slider_5.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider_5.offset_left = 631.96
	Slider_5.offset_top = 719.97
	Slider_5.offset_right = 904.37
	Slider_5.offset_bottom = 755.97
	add_child(Slider_5)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-3905401559793170008)
	var Background_12 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_12.name = "Background"
	Background_12.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_12.offset_left = 631.96
	Background_12.offset_top = 723.55
	Background_12.offset_right = 904.37
	Background_12.offset_bottom = 753.38
	add_child(Background_12)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=8803191960022976936)
	var Fill_5 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill_5.name = "Fill"
	Fill_5.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill_5.offset_left = 631.96
	Fill_5.offset_top = 760.24
	Fill_5.offset_right = 631.96
	Fill_5.offset_bottom = 751.71
	add_child(Fill_5)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (5) (原版 GO pid=-4624615996300818008)
	var Deck_CostQuanityt_Row_Drawer__5_ := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer__5_.name = "Deck CostQuanityt Row Drawer (5)"
	Deck_CostQuanityt_Row_Drawer__5_.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer__5_.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer__5_.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer__5_.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer__5_.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer__5_)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=8194153489190128040)
	var Card_Cost_6 := Label.new()
	Card_Cost_6.add_theme_font_size_override("font_size", 25)
	Card_Cost_6.text = "0"   # 原版 m_text
	Card_Cost_6.name = "Card Cost"
	Card_Cost_6.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost_6.offset_left = 573.01
	Card_Cost_6.offset_top = 720.06
	Card_Cost_6.offset_right = 619.02
	Card_Cost_6.offset_bottom = 755.89
	add_child(Card_Cost_6)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=2845407606903310760)
	var Cards_in_deck_6 := Label.new()
	Cards_in_deck_6.add_theme_font_size_override("font_size", 25)
	Cards_in_deck_6.text = "0"   # 原版 m_text
	Cards_in_deck_6.name = "Cards in deck"
	Cards_in_deck_6.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck_6.offset_left = 916.58
	Cards_in_deck_6.offset_top = 719.97
	Cards_in_deck_6.offset_right = 962.59
	Cards_in_deck_6.offset_bottom = 755.97
	add_child(Cards_in_deck_6)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=-7326345078336616024)
	var Slider_6 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider_6.name = "Slider"
	Slider_6.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider_6.offset_left = 631.96
	Slider_6.offset_top = 719.97
	Slider_6.offset_right = 904.37
	Slider_6.offset_bottom = 755.97
	add_child(Slider_6)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=5722389864387348904)
	var Background_13 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_13.name = "Background"
	Background_13.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_13.offset_left = 631.96
	Background_13.offset_top = 723.55
	Background_13.offset_right = 904.37
	Background_13.offset_bottom = 753.38
	add_child(Background_13)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=-3729472373258942040)
	var Fill_6 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill_6.name = "Fill"
	Fill_6.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill_6.offset_left = 631.96
	Fill_6.offset_top = 760.24
	Fill_6.offset_right = 631.96
	Fill_6.offset_bottom = 751.71
	add_child(Fill_6)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (6) (原版 GO pid=4010134763377756584)
	var Deck_CostQuanityt_Row_Drawer__6_ := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer__6_.name = "Deck CostQuanityt Row Drawer (6)"
	Deck_CostQuanityt_Row_Drawer__6_.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer__6_.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer__6_.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer__6_.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer__6_.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer__6_)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=8790551783196887464)
	var Card_Cost_7 := Label.new()
	Card_Cost_7.add_theme_font_size_override("font_size", 25)
	Card_Cost_7.text = "0"   # 原版 m_text
	Card_Cost_7.name = "Card Cost"
	Card_Cost_7.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost_7.offset_left = 573.01
	Card_Cost_7.offset_top = 720.06
	Card_Cost_7.offset_right = 619.02
	Card_Cost_7.offset_bottom = 755.89
	add_child(Card_Cost_7)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=-8804768408991069784)
	var Cards_in_deck_7 := Label.new()
	Cards_in_deck_7.add_theme_font_size_override("font_size", 25)
	Cards_in_deck_7.text = "0"   # 原版 m_text
	Cards_in_deck_7.name = "Cards in deck"
	Cards_in_deck_7.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck_7.offset_left = 916.58
	Cards_in_deck_7.offset_top = 719.97
	Cards_in_deck_7.offset_right = 962.59
	Cards_in_deck_7.offset_bottom = 755.97
	add_child(Cards_in_deck_7)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=-2610241449402267224)
	var Slider_7 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider_7.name = "Slider"
	Slider_7.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider_7.offset_left = 631.96
	Slider_7.offset_top = 719.97
	Slider_7.offset_right = 904.37
	Slider_7.offset_bottom = 755.97
	add_child(Slider_7)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-3571060624327472728)
	var Background_14 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_14.name = "Background"
	Background_14.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_14.offset_left = 631.96
	Background_14.offset_top = 723.55
	Background_14.offset_right = 904.37
	Background_14.offset_bottom = 753.38
	add_child(Background_14)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=2963112321218152872)
	var Fill_7 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill_7.name = "Fill"
	Fill_7.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill_7.offset_left = 631.96
	Fill_7.offset_top = 760.24
	Fill_7.offset_right = 631.96
	Fill_7.offset_bottom = 751.71
	add_child(Fill_7)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (7) (原版 GO pid=-2670607095577343576)
	var Deck_CostQuanityt_Row_Drawer__7_ := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer__7_.name = "Deck CostQuanityt Row Drawer (7)"
	Deck_CostQuanityt_Row_Drawer__7_.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer__7_.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer__7_.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer__7_.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer__7_.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer__7_)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=7287468177215490472)
	var Card_Cost_8 := Label.new()
	Card_Cost_8.add_theme_font_size_override("font_size", 25)
	Card_Cost_8.text = "0"   # 原版 m_text
	Card_Cost_8.name = "Card Cost"
	Card_Cost_8.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost_8.offset_left = 573.01
	Card_Cost_8.offset_top = 720.06
	Card_Cost_8.offset_right = 619.02
	Card_Cost_8.offset_bottom = 755.89
	add_child(Card_Cost_8)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=3904992540087585192)
	var Cards_in_deck_8 := Label.new()
	Cards_in_deck_8.add_theme_font_size_override("font_size", 25)
	Cards_in_deck_8.text = "0"   # 原版 m_text
	Cards_in_deck_8.name = "Cards in deck"
	Cards_in_deck_8.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck_8.offset_left = 916.58
	Cards_in_deck_8.offset_top = 719.97
	Cards_in_deck_8.offset_right = 962.59
	Cards_in_deck_8.offset_bottom = 755.97
	add_child(Cards_in_deck_8)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=-5128945474065233496)
	var Slider_8 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider_8.name = "Slider"
	Slider_8.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider_8.offset_left = 631.96
	Slider_8.offset_top = 719.97
	Slider_8.offset_right = 904.37
	Slider_8.offset_bottom = 755.97
	add_child(Slider_8)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-7249035986396280408)
	var Background_15 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_15.name = "Background"
	Background_15.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_15.offset_left = 631.96
	Background_15.offset_top = 723.55
	Background_15.offset_right = 904.37
	Background_15.offset_bottom = 753.38
	add_child(Background_15)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=-704248337810028120)
	var Fill_8 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill_8.name = "Fill"
	Fill_8.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill_8.offset_left = 631.96
	Fill_8.offset_top = 760.24
	Fill_8.offset_right = 631.96
	Fill_8.offset_bottom = 751.71
	add_child(Fill_8)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Deck CostQuanityt Row Drawer (8) (原版 GO pid=-4578812512142390872)
	var Deck_CostQuanityt_Row_Drawer__8_ := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Deck_CostQuanityt_Row_Drawer__8_.name = "Deck CostQuanityt Row Drawer (8)"
	Deck_CostQuanityt_Row_Drawer__8_.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Deck_CostQuanityt_Row_Drawer__8_.offset_left = 566.94
	Deck_CostQuanityt_Row_Drawer__8_.offset_top = 720.95
	Deck_CostQuanityt_Row_Drawer__8_.offset_right = 969.4
	Deck_CostQuanityt_Row_Drawer__8_.offset_bottom = 754.99
	add_child(Deck_CostQuanityt_Row_Drawer__8_)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Card Cost (原版 GO pid=2794055738578733480)
	var Card_Cost_9 := Label.new()
	Card_Cost_9.add_theme_font_size_override("font_size", 25)
	Card_Cost_9.text = "0"   # 原版 m_text
	Card_Cost_9.name = "Card Cost"
	Card_Cost_9.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Card_Cost_9.offset_left = 573.01
	Card_Cost_9.offset_top = 720.06
	Card_Cost_9.offset_right = 619.02
	Card_Cost_9.offset_bottom = 755.89
	add_child(Card_Cost_9)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Cards in deck (原版 GO pid=-8906404708716344920)
	var Cards_in_deck_9 := Label.new()
	Cards_in_deck_9.add_theme_font_size_override("font_size", 25)
	Cards_in_deck_9.text = "0"   # 原版 m_text
	Cards_in_deck_9.name = "Cards in deck"
	Cards_in_deck_9.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Cards_in_deck_9.offset_left = 916.58
	Cards_in_deck_9.offset_top = 719.97
	Cards_in_deck_9.offset_right = 962.59
	Cards_in_deck_9.offset_bottom = 755.97
	add_child(Cards_in_deck_9)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Slider (原版 GO pid=-4421553556660647512)
	var Slider_9 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Slider_9.name = "Slider"
	Slider_9.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Slider_9.offset_left = 631.96
	Slider_9.offset_top = 719.97
	Slider_9.offset_right = 904.37
	Slider_9.offset_bottom = 755.97
	add_child(Slider_9)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=-4047653668667487832)
	var Background_16 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_16.name = "Background"
	Background_16.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_16.offset_left = 631.96
	Background_16.offset_top = 723.55
	Background_16.offset_right = 904.37
	Background_16.offset_bottom = 753.38
	add_child(Background_16)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Fill (原版 GO pid=-1246969960694511192)
	var Fill_9 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Fill_9.name = "Fill"
	Fill_9.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Fill_9.offset_left = 631.96
	Fill_9.offset_top = 760.24
	Fill_9.offset_right = 631.96
	Fill_9.offset_bottom = 751.71
	add_child(Fill_9)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Generic Close Button Orange (原版 GO pid=-4868612507233777240)
	var Generic_Close_Button_Orange := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Generic_Close_Button_Orange.name = "Generic Close Button Orange"
	Generic_Close_Button_Orange.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Generic_Close_Button_Orange.offset_left = 1782.81
	Generic_Close_Button_Orange.offset_top = 63.2
	Generic_Close_Button_Orange.offset_right = 1857.19
	Generic_Close_Button_Orange.offset_bottom = 138.8
	add_child(Generic_Close_Button_Orange)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Background (原版 GO pid=2179961863809436072)
	var Background_17 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Background_17.name = "Background"
	Background_17.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Background_17.offset_left = 1790.96
	Background_17.offset_top = 71.18
	Background_17.offset_right = 1847.82
	Background_17.offset_bottom = 129.3
	add_child(Background_17)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)

	# Icon (原版 GO pid=751936349810297256)
	var Icon_6 := Control.new()   # TODO: 原版组件查 GO (容器/Border/骨架), Button 需手动换
	Icon_6.name = "Icon"
	Icon_6.set_anchors_preset(Control.PRESET_TOP_LEFT)   # 绝对坐标已含 y 翻转+父链; 局部容器内须改锚点
	Icon_6.offset_left = 1790.96
	Icon_6.offset_top = 71.18
	Icon_6.offset_right = 1847.82
	Icon_6.offset_bottom = 129.3
	add_child(Icon_6)
	# TODO: 信号/交互接线 (原版 Button/Toggle/InputField 事件)
