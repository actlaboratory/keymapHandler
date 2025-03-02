# str2key
#Copyright (C) 2019 Yukio Nozawa <personal@nyanchangames.com>
#Copyright (C) 2019-2025 yamahubuki <itiro.ishino@gmail.com>


import wx


str2ControlCommand={
	#制御キー
	"CONTROL_A":wx.WXK_CONTROL_A,
	"CONTROL_B":wx.WXK_CONTROL_B,
	"CONTROL_C":wx.WXK_CONTROL_C,
	"CONTROL_D":wx.WXK_CONTROL_D,
	"CONTROL_E":wx.WXK_CONTROL_E,
	"CONTROL_F":wx.WXK_CONTROL_F,
	"CONTROL_G":wx.WXK_CONTROL_G,
	"CONTROL_H":wx.WXK_CONTROL_H,
	"CONTROL_I":wx.WXK_CONTROL_I,
	"CONTROL_J":wx.WXK_CONTROL_J,
	"CONTROL_K":wx.WXK_CONTROL_K,
	"CONTROL_L":wx.WXK_CONTROL_L,
	"CONTROL_M":wx.WXK_CONTROL_M,
	"CONTROL_N":wx.WXK_CONTROL_N,
	"CONTROL_O":wx.WXK_CONTROL_O,
	"CONTROL_P":wx.WXK_CONTROL_P,
	"CONTROL_Q":wx.WXK_CONTROL_Q,
	"CONTROL_R":wx.WXK_CONTROL_R,
	"CONTROL_S":wx.WXK_CONTROL_S,
	"CONTROL_T":wx.WXK_CONTROL_T,
	"CONTROL_U":wx.WXK_CONTROL_U,
	"CONTROL_V":wx.WXK_CONTROL_V,
	"CONTROL_W":wx.WXK_CONTROL_W,
	"CONTROL_X":wx.WXK_CONTROL_X,
	"CONTROL_Y":wx.WXK_CONTROL_Y,
	"CONTROL_Z":wx.WXK_CONTROL_Z
}

#マウスボタン
str2MouseKey={
	"LBUTTON":wx.WXK_LBUTTON,
	"MBUTTON":wx.WXK_MBUTTON,
	"RBUTTON":wx.WXK_RBUTTON
}

#他の全てのキーの修飾キーとして利用可能
str2ModifierKey={
	#修飾キー
	"ALT":wx.WXK_ALT,
	"CTRL":wx.WXK_CONTROL,
	"WINDOWS":wx.WXK_WINDOWS_LEFT,
	"WINDOWS_RIGHT":wx.WXK_WINDOWS_RIGHT,
	"SHIFT":wx.WXK_SHIFT
}

#不明なもの・Windowsでは使えないもの、
str2UnknownKey={
	"START":wx.WXK_START,					#Ctrl+ESC
	"CANCEL":wx.WXK_CANCEL,
	"MENU":wx.WXK_MENU,
	"CAPITAL":wx.WXK_CAPITAL,
	"SELECT":wx.WXK_SELECT,
	"PRINT":wx.WXK_PRINT,
	"EXECUTE":wx.WXK_EXECUTE,
	"HELP":wx.WXK_HELP,
	"SCROLL":wx.WXK_SCROLL,					#ScrLk
	"COMMAND":wx.WXK_COMMAND,				#CONTROLと同じ
	"RAW_CONTROL":wx.WXK_RAW_CONTROL,		#CONTROLと同じ

	#記号キー 動作しない
	"MULTIPLY":wx.WXK_MULTIPLY,
	"ADD":wx.WXK_ADD,
	"SEPARATOR":wx.WXK_SEPARATOR,
	"SUBTRACT":wx.WXK_SUBTRACT,
	"DECIMAL":wx.WXK_DECIMAL,
	"DIVIDE":wx.WXK_DIVIDE,
}

#単独でも修飾キーとの組み合わせでも利用可能
str2FunctionKey={
	#ファンクションキー
	"F1":wx.WXK_F1,
	"F2":wx.WXK_F2,
	"F3":wx.WXK_F3,
	"F4":wx.WXK_F4,
	"F5":wx.WXK_F5,
	"F6":wx.WXK_F6,
	"F7":wx.WXK_F7,
	"F8":wx.WXK_F8,
	"F9":wx.WXK_F9,
	"F10":wx.WXK_F10,
	"F11":wx.WXK_F11,
	"F12":wx.WXK_F12,
	"F13":wx.WXK_F13,
	"F14":wx.WXK_F14,
	"F15":wx.WXK_F15,
	"F16":wx.WXK_F16,
	"F17":wx.WXK_F17,
	"F18":wx.WXK_F18,
	"F19":wx.WXK_F19,
	"F20":wx.WXK_F20,
	"F21":wx.WXK_F21,
	"F22":wx.WXK_F22,
	"F23":wx.WXK_F23,
	"F24":wx.WXK_F24,
}

#文字入力時に利用できない単独キー
str2InputControlKey={
	"BACK":wx.WXK_BACK,
	"SPACE":wx.WXK_SPACE,
	"DELETE":wx.WXK_DELETE,
	"INSERT":wx.WXK_INSERT,

	#ジャンプキー
	"HOME":wx.WXK_HOME,
	"END":wx.WXK_END,
	"PAGEUP":wx.WXK_PAGEUP,
	"PAGEDOWN":wx.WXK_PAGEDOWN,
}

#主要キー
str2StandaloneKey={
	"TAB":wx.WXK_TAB,
	"RETURN":wx.WXK_RETURN,
	"ESCAPE":wx.WXK_ESCAPE,
	"APPLICATIONS":wx.WXK_WINDOWS_MENU,		#コンテキストメニューを開くアプリケーションキー
	"PRINTSCREEN":wx.WXK_SNAPSHOT,		#PrintScr
	"PAUSE":wx.WXK_PAUSE,

	#テンキー記号キー
	"NUMPAD_EQUAL":wx.WXK_NUMPAD_EQUAL,
	"NUMPAD_MULTIPLY":wx.WXK_NUMPAD_MULTIPLY,
	"NUMPAD_ADD":wx.WXK_NUMPAD_ADD,
	"NUMPAD_SEPARATOR":wx.WXK_NUMPAD_SEPARATOR,
	"NUMPAD_SUBTRACT":wx.WXK_NUMPAD_SUBTRACT,
	"NUMPAD_DIVIDE":wx.WXK_NUMPAD_DIVIDE,
	"NUMPAD_DECIMAL":wx.WXK_NUMPAD_DECIMAL,

	#矢印キー
	"LEFTARROW":wx.WXK_LEFT,
	"UPARROW":wx.WXK_UP,
	"RIGHTARROW":wx.WXK_RIGHT,
	"DOWNARROW":wx.WXK_DOWN,
	"CLEAR":wx.WXK_CLEAR,					#テンキー5
}

#単独または修飾キーとの組み合わせで利用できる
str2SpecialKey={
	#メディア制御キー
	"VOLUME_DOWN":wx.WXK_VOLUME_DOWN,
	"VOLUME_MUTE":wx.WXK_VOLUME_MUTE,
	"VOLUME_UP":wx.WXK_VOLUME_UP,
	"MEDIA_NEXT":wx.WXK_MEDIA_NEXT_TRACK,
	"MEDIA_PLAY":wx.WXK_MEDIA_PLAY_PAUSE,
	"MEDIA_BACK":wx.WXK_MEDIA_PREV_TRACK,
	"MEDIA_STOP":wx.WXK_MEDIA_STOP,

	#ブラウザ制御キー
	"BROWSER_BACK":wx.WXK_BROWSER_BACK,
	"BROWSER_FAVORITES":wx.WXK_BROWSER_FAVORITES,
	"BROWSER_FORWARD":wx.WXK_BROWSER_FORWARD,
	"BROWSER_HOME":wx.WXK_BROWSER_HOME,
	"BROWSER_REFRESH":wx.WXK_BROWSER_REFRESH,
	"BROWSER_SEARCH":wx.WXK_BROWSER_SEARCH,
	"BROWSER_STOP":wx.WXK_BROWSER_STOP,

	#アプリケーション起動キー
	"LAUNCH_APP1":wx.WXK_LAUNCH_APP1,
	"LAUNCH_APP2":wx.WXK_LAUNCH_APP2,
	"LAUNCH_MAIL":wx.WXK_LAUNCH_MAIL,

	#スペシャル
	"SPECIAL1":wx.WXK_SPECIAL1,
	"SPECIAL2":wx.WXK_SPECIAL2,
	"SPECIAL3":wx.WXK_SPECIAL3,
	"SPECIAL4":wx.WXK_SPECIAL4,
	"SPECIAL5":wx.WXK_SPECIAL5,
	"SPECIAL6":wx.WXK_SPECIAL6,
	"SPECIAL7":wx.WXK_SPECIAL7,
	"SPECIAL8":wx.WXK_SPECIAL8,
	"SPECIAL9":wx.WXK_SPECIAL9,
	"SPECIAL10":wx.WXK_SPECIAL10,
	"SPECIAL11":wx.WXK_SPECIAL11,
	"SPECIAL12":wx.WXK_SPECIAL12,
	"SPECIAL13":wx.WXK_SPECIAL13,
	"SPECIAL14":wx.WXK_SPECIAL14,
	"SPECIAL15":wx.WXK_SPECIAL15,
	"SPECIAL16":wx.WXK_SPECIAL16,
	"SPECIAL17":wx.WXK_SPECIAL17,
	"SPECIAL18":wx.WXK_SPECIAL18,
	"SPECIAL19":wx.WXK_SPECIAL19,
	"SPECIAL20":wx.WXK_SPECIAL20,
}

#他の修飾キーとの組み合わせで利用できるキー
str2CharactorKey={
	#アルファベットキー
	"A": ord('A'),
	"B": ord('B'),
	"C": ord('C'),
	"D": ord('D'),
	"E": ord('E'),
	"F": ord('F'),
	"G": ord('G'),
	"H": ord('H'),
	"I": ord('I'),
	"J": ord('J'),
	"K": ord('K'),
	"L": ord('L'),
	"M": ord('M'),
	"N": ord('N'),
	"O": ord('O'),
	"P": ord('P'),
	"Q": ord('Q'),
	"R": ord('R'),
	"S": ord('S'),
	"T": ord('T'),
	"U": ord('U'),
	"V": ord('V'),
	"W": ord('W'),
	"X": ord('X'),
	"Y": ord('Y'),
	"Z": ord('Z'),

	#数字キー
	"0": ord('0'),
	"1": ord('1'),
	"2": ord('2'),
	"3": ord('3'),
	"4": ord('4'),
	"5": ord('5'),
	"6": ord('6'),
	"7": ord('7'),
	"8": ord('8'),
	"9": ord('9'),

	#テンキー数字キー
	"NUMPAD0":wx.WXK_NUMPAD0,
	"NUMPAD1":wx.WXK_NUMPAD1,
	"NUMPAD2":wx.WXK_NUMPAD2,
	"NUMPAD3":wx.WXK_NUMPAD3,
	"NUMPAD4":wx.WXK_NUMPAD4,
	"NUMPAD5":wx.WXK_NUMPAD5,
	"NUMPAD6":wx.WXK_NUMPAD6,
	"NUMPAD7":wx.WXK_NUMPAD7,
	"NUMPAD8":wx.WXK_NUMPAD8,
	"NUMPAD9":wx.WXK_NUMPAD9,

	#記号キー
	",": ord(','),
	".": ord('.'),
	"/": ord('/'),
	"\\": ord('\\'),	#上段側のみにマッチ
	";": ord(';'),
	":": ord(':'),
	"[": ord('['),
	"]": ord(']'),
	"@": ord('@'),
	"-": ord('-'),
	"^": ord('^'),
}

#利用不可
str2categoryKey={
	#カテゴリ制御キー
	"CATEGORY_ARROW":wx.WXK_CATEGORY_ARROW,
	"CATEGORY_CUT":wx.WXK_CATEGORY_CUT,
	"CATEGORY_JUMP":wx.WXK_CATEGORY_JUMP,
	"CATEGORY_NAVIGATION":wx.WXK_CATEGORY_NAVIGATION,
	"CATEGORY_PAGING":wx.WXK_CATEGORY_PAGING,
	"CATEGORY_TAB":wx.WXK_CATEGORY_TAB,
}

#テンキー関連の内、本来のキーと重複して判定されてしまうキー
str2numpadKey={
	"NUMPAD_F1":wx.WXK_NUMPAD_F1,
	"NUMPAD_F2":wx.WXK_NUMPAD_F2,
	"NUMPAD_F3":wx.WXK_NUMPAD_F3,
	"NUMPAD_F4":wx.WXK_NUMPAD_F4,

	"NUMPAD_SPACE":wx.WXK_NUMPAD_SPACE,
	"NUMPAD_INSERT":wx.WXK_NUMPAD_INSERT,
	"NUMPAD_DELETE":wx.WXK_NUMPAD_DELETE,

	"NUMPAD_LEFT":wx.WXK_NUMPAD_LEFT,	#4
	"NUMPAD_UP":wx.WXK_NUMPAD_UP,		#8
	"NUMPAD_RIGHT":wx.WXK_NUMPAD_RIGHT,	#6
	"NUMPAD_DOWN":wx.WXK_NUMPAD_DOWN,	#2

	"NUMPAD_PAGEUP":wx.WXK_NUMPAD_PAGEUP,#9
	"NUMPAD_PAGEDOWN":wx.WXK_NUMPAD_PAGEDOWN,#3
	"NUMPAD_HOME":wx.WXK_NUMPAD_HOME,	#7
	"NUMPAD_END":wx.WXK_NUMPAD_END,		#9

	"NUMPAD_TAB":wx.WXK_NUMPAD_TAB,
	"NUMPAD_ENTER":wx.WXK_NUMPAD_ENTER,
}

str2key={}
str2key.update(**str2ControlCommand,**str2MouseKey,**str2ModifierKey,**str2UnknownKey,**str2FunctionKey,**str2InputControlKey,**str2StandaloneKey,**str2SpecialKey,**str2CharactorKey,**str2categoryKey,**str2numpadKey)
