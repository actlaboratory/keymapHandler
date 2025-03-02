# KeyFilter
#Copyright (C) 2019 Yukio Nozawa <personal@nyanchangames.com>
#Copyright (C) 2019-2025 yamahubuki <itiro.ishino@gmail.com>

from .str_to_key import *

class KeyFilter:
	"""
		利用できるショートカットキーを制限するためのフィルタ
	"""

	def __init__(self):
		"""
			必用な変数を作成し、OSが利用するコマンドとの重複は設定できないようブロックする
		"""
		self.error_string = ""  # 最後に検知したエラーの原因を格納
		self.modifier_key = set()  # 有効な修飾キー
		self.function_key = set()  # 有効なファンクションキー。単独または修飾キーとの組み合わせで利用可能
		self.enable_key = set()  # 修飾キーとの組み合わせで利用可能
		self.no_shift_enable_key = set()  # SHIFTキー以外の修飾キーとの組み合わせで利用可能(modifier_keyにSHIFTを指定していない場合は無視される)
		self.disable_pattern = []  # 無効なキーの組み合わせ
		self.add_disable_pattern("CTRL+ESCAPE")  # スタートメニュー
		self.add_disable_pattern("CTRL+SHIFT+ESCAPE")  # タスクマネージャ
		self.add_disable_pattern("CTRL+WINDOWS+RETURN")  # ナレーターの起動と終了
		self.add_disable_pattern("ALT+SHIFT+PRINTSCREEN")  # ハイコントラストの切り替え
		self.add_disable_pattern("ALT+ESCAPE")  # 最前面ウィンドウの最小化
		self.add_disable_pattern("ALT+TAB")  # ウィンドウ間の移動
		self.add_disable_pattern("ALT+SHIFT+TAB")  # ウィンドウ間の移動
		self.add_disable_pattern("ALT+ESCAPE")  # ウィンドウの最小化

	def set_default(self, support_input_char, is_system, arrow_char_key=False):
		"""
			フィルタを一般的な設定に構成する。

			support_input_charには、そのウィンドウでの文字入力の可否を設定する。
			ここでFalseを設定すると、Home,BS,Enterなど文字入力と競合する修飾キーを単体でショートカットとして利用可能になる

			is_systemには、システム内部で設定する場合にはTrue、ユーザが独自で設定する場合にはFalseを指定する。
			ユーザが独自にキーをカスタマイズする場合に、指定することが望ましくないキーの組み合わせをブロックする。
			将来、開発者が機能拡張する際の問題を和らげることを目的としている。
			なお、開発者であってもコメントで記した目的以外に利用することは避けるべきである。

			arrow_char_keyには、原則Falseを指定する。
			ここでTrueを設定すると英数字や各種記号文字のキーを単体でショートカットキーとして利用可能になる。
			ただし、各種コントロールのインクリメンタルサーチ等と競合するため、この設定は推奨されない。
		"""
		self.modifier_key.add("CTRL")
		self.modifier_key.add("ALT")
		self.modifier_key.add("SHIFT")

		self.function_key |= str_to_function_key.keys()
		self.function_key |= str_to_special_key.keys()

		if support_input_char:
			# 文字入力に関わる共通のショートカットは設定不可
			self.add_disable_pattern("CTRL+INSERT")  # コピー
			self.add_disable_pattern("SHIFT+INSERT")  # 貼り付け
			self.add_disable_pattern("CTRL+Z")  # 元に戻す
			self.add_disable_pattern("CTRL+X")  # 切り取り
			self.add_disable_pattern("CTRL+C")  # コピー
			self.add_disable_pattern("CTRL+V")  # 貼り付け
			self.add_disable_pattern("CTRL+A")  # すべて選択
			self.add_disable_pattern("CTRL+Y")  # やり直し
			self.add_disable_pattern("CTRL+F7")  # 単語登録(日本語変換時のみ)
			self.add_disable_pattern("CTRL+F10")  # IMEメニュー表示(日本語変換時のみ)

			# 単独で文字入力の制御に利用されるので修飾キー必須
			self.enable_key |= str_to_input_control_key.keys()
		else:
			# 単独で文字入力の制御に利用されるが、それがないなら単独利用可能
			self.function_key |= str_to_input_control_key.keys()

		if is_system:
			self.function_key |= str_to_standalone_key.keys()
		else:
			self.add_disable_pattern("APPLICATIONS")  # コンテキストメニューの表示
			self.add_disable_pattern("SHIFT+F10")  # コンテキストメニューの表示
			self.add_disable_pattern("F10")  # ALTキーの代わり
			self.add_disable_pattern("ESCAPE")  # 操作の取り消し
			self.add_disable_pattern("ALT+F4")  # アプリケーションの終了
			self.add_disable_pattern("SPACE")  # ボタンの押下
			self.add_disable_pattern("ALT+SPACE")  # リストビュー等で全ての選択を解除
			self.enable_key |= str_to_standalone_key.keys()

		if arrow_char_key:
			self.function_key |= str_to_character_key.keys()
		else:
			self.no_shift_enable_key |= str_to_character_key.keys()

		return self

	def add_disable_pattern(self, pattern_string):
		patterns = pattern_string.split("+")
		for ptn in patterns:
			ptn = ptn.upper()
			if not ptn in str_to_key:
				raise ValueError(_("%s は存在しないキーです。") % (ptn))
		self.disable_pattern.append(set(patterns))

	def add_enable_key(self, keys):
		if type(keys) == str:
			return self._set_key_group(keys, self.enable_key)
		for key in keys:
			self._set_key_group(key, self.enable_key)

	def add_function_key(self, keys):
		if type(keys) == str:
			return self._set_key_group(keys, self.function_key)
		for key in keys:
			self._set_key_group(key, self.function_key)

	def add_modifier_key(self, keys):
		if type(keys) == str:
			return self._set_key_group(keys, self.modifier_key)
		for key in keys:
			self._set_key_group(key, self.modifier_key)

	def add_no_shift_enable_key(self, keys):
		if type(keys) == str:
			return self._set_key_group(keys, self.no_shift_enable_key)
		for key in keys:
			self._set_key_group(key, self.no_shift_enable_key)

	def _set_key_group(self, key, target):
		key = key.upper()
		if not key in str_to_key:
			raise ValueError(_("%s は存在しないキーです。" % key))
		try:
			self.disable_pattern.remove(set(key))
		except ValueError:
			pass
		self.enable_key.discard(key)
		self.function_key.discard(key)
		self.modifier_key.discard(key)
		self.no_shift_enable_key.discard(key)
		target.add(key)

	def check(self, key_string):
		if key_string == "":
			self.error_string = "キーが指定されていません。"
			return False

		self.error_string = ""
		keys = key_string.upper().split("+")
		mod_flg = False
		shift_flg = False
		func_count = 0
		enable_count = 0
		no_shift_count = 0
		for key in keys:
			if key in self.modifier_key:
				if key == "SHIFT":
					shift_flg = True
				else:
					mod_flg = True
				continue
			if key in self.function_key:
				func_count += 1
				continue
			if key in self.enable_key:
				enable_count += 1
				continue
			if key in self.no_shift_enable_key:
				no_shift_count += 1
				continue

			# ここまでcontinueされなかったらエラー
			self.error_string = _("%s は使用できないキーです。") % (key)
			return False

		# 組み合わせの妥当性確認
		if len(keys) == 1:
			if func_count > 0:
				return True
			else:
				if mod_flg > 0 or shift_flg > 0:
					self.error_string = _("修飾キーのみのパターンは設定できません。")
				else:
					self.error_string = _("このキーは修飾キーと合わせて指定する必要があります。")
				return False

		# ２つ以上が指定されている場合
		if func_count + enable_count + no_shift_count > 1:
			self.error_string = _("修飾キーでないキーを複数指定することはできません。")
			return False
		elif mod_flg == False and shift_flg == False and func_count == 0:
			self.error_string = _("このキーは、SHIFTキー以外の修飾キーと合わせて指定する必要があります。")
			return
		elif func_count == 0 and no_shift_count == 0 and enable_count == 0:
			self.error_string = _("修飾キーのみの組み合わせは指定できません。")
			return False
		if enable_count > 0 and mod_flg == False and shift_flg == False:
			raise Error("コードのバグです。")
		if no_shift_count > 0 and mod_flg == False:
			self.error_string = _("このキーは、SHIFTキー以外の修飾キーと合わせて指定する必要があります。")
			return False

		if set(keys) in self.disable_pattern:
			self.error_string = _("この組み合わせは別の用途で予約されているため、利用できません。")
			return False

		return True

	def get_last_error(self):
		return self.error_string

	def get_usable_keys(self):
		ret = []
		ret.extend([*self.modifier_key, *self.function_key, *self.enable_key, *self.no_shift_enable_key])
		return ret
