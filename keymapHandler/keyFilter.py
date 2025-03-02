# KeyFilter
#Copyright (C) 2019 Yukio Nozawa <personal@nyanchangames.com>
#Copyright (C) 2019-2025 yamahubuki <itiro.ishino@gmail.com>

from .str2key import *

class KeyFilter:
	"""
		利用できるショートカットキーを制限するためのフィルタ
	"""

	def __init__(self):
		"""
			必用な変数を作成し、OSが利用するコマンドとの重複は設定できないようブロックする
		"""
		self.errorString=""									#最後に検知したエラーの原因を格納
		self.modifierKey=set()								#有効な修飾キー
		self.functionKey=set()								#有効なファンクションキー。単独または修飾キーとの組み合わせで利用可能
		self.enableKey=set()								#修飾キーとの組み合わせで利用可能
		self.noShiftEnableKey=set()							#SHIFTキー以外の修飾キーとの組み合わせで利用可能(modifierKeyにSHIFTを指定していない場合は無視される)
		self.disablePattern=[]								#無効なキーの組み合わせ
		self.AddDisablePattern("CTRL+ESCAPE")				#スタートメニュー
		self.AddDisablePattern("CTRL+SHIFT+ESCAPE")			#タスクマネージャ
		self.AddDisablePattern("CTRL+WINDOWS+RETURN")		#ナレーターの起動と終了
		self.AddDisablePattern("ALT+SHIFT+PRINTSCREEN")		#ハイコントラストの切り替え
		self.AddDisablePattern("ALT+ESCAPE")				#最前面ウィンドウの最小化
		self.AddDisablePattern("ALT+TAB")					#ウィンドウ間の移動
		self.AddDisablePattern("ALT+SHIFT+TAB")				#ウィンドウ間の移動
		self.AddDisablePattern("ALT+ESCAPE")				#ウィンドウの最小化

	def SetDefault(self,supportInputChar,isSystem,arrowCharKey=False):
		"""
			フィルタを一般的な設定に構成する。

			supportInputCharには、そのウィンドウでの文字入力の可否を設定する。
			ここでFalseを設定すると、Home,BS,Enterなど文字入力と競合する修飾キーを単体でショートカットとして利用可能になる

			isSystemには、システム内部で設定する場合にはTrue、ユーザが独自で設定する場合にはFalseを指定する。
			ユーザが独自にキーをカスタマイズする場合に、指定することが望ましくないキーの組み合わせをブロックする。
			将来、開発者が機能拡張する際の問題を和らげることを目的としている。
			なお、開発者であってもコメントで記した目的以外に利用することは避けるべきである。

			arrowCharKeyには、原則Falseを指定する。
			ここでTrueを設定すると英数字や各種記号文字のキーを単体でショートカットキーとして利用可能になる。
			ただし、各種コントロールのインクリメンタルサーチ等と競合するため、この設定は推奨されない。
		"""
		self.modifierKey.add("CTRL")
		self.modifierKey.add("ALT")
		self.modifierKey.add("SHIFT")

		self.functionKey|=str2FunctionKey.keys()
		self.functionKey|=str2SpecialKey.keys()

		if supportInputChar:
			#文字入力に関わる共通のショートカットは設定不可
			self.AddDisablePattern("CTRL+INSERT")		#コピー
			self.AddDisablePattern("SHIFT+INSERT")			#貼り付け
			self.AddDisablePattern("CTRL+Z")			#元に戻す
			self.AddDisablePattern("CTRL+X")			#切り取り
			self.AddDisablePattern("CTRL+C")			#コピー
			self.AddDisablePattern("CTRL+V")			#貼り付け
			self.AddDisablePattern("CTRL+A")			#すべて選択
			self.AddDisablePattern("CTRL+Y")			#やり直し
			self.AddDisablePattern("CTRL+F7")			#単語登録(日本語変換時のみ)
			self.AddDisablePattern("CTRL+F10")			#IMEメニュー表示(日本語変換時のみ)

			#単独で文字入力の制御に利用されるので修飾キー必須
			self.enableKey|=str2InputControlKey.keys()
		else:
			#単独で文字入力の制御に利用されるが、それがないなら単独利用可能
			self.functionKey|=str2InputControlKey.keys()

		if isSystem:
			self.functionKey|=str2StandaloneKey.keys()
		else:
			self.AddDisablePattern("APPLICATIONS")				#コンテキストメニューの表示
			self.AddDisablePattern("SHIFT+F10")					#コンテキストメニューの表示
			self.AddDisablePattern("F10")						#ALTキーの代わり
			self.AddDisablePattern("ESCAPE")					#操作の取り消し
			self.AddDisablePattern("ALT+F4")					#アプリケーションの終了
			self.AddDisablePattern("SPACE")						#ボタンの押下
			self.AddDisablePattern("ALT+SPACE")					#リストビュー等で全ての選択を解除
			self.enableKey|=str2StandaloneKey.keys()

		if arrowCharKey:
			self.functionKey|=str2CharactorKey.keys()
		else:
			self.noShiftEnableKey|=str2CharactorKey.keys()

		return self

	def AddDisablePattern(self,patternString):
		patterns=patternString.split("+")
		for ptn in patterns:
			ptn=ptn.upper()
			if not ptn in str2key:
				raise ValueError(_("%s は存在しないキーです。") % (ptn))
		self.disablePattern.append(set(patterns))

	def AddEnableKey(self,keys):
		if type(keys)==str:
			return self._SetKeyGroup(keys,self.enableKey)
		for key in keys:
			self._SetKeyGroup(key,self.enableKey)

	def AddFunctionKey(self,keys):
		if type(keys)==str:
			return self._SetKeyGroup(keys,self.functionKey)
		for key in keys:
			self._SetKeyGroup(key,self.functionKey)

	def AddModifierKey(self,keys):
		if type(keys)==str:
			return self._SetKeyGroup(keys,self.modifierKey)
		for key in keys:
			self._SetKeyGroup(key,self.modifierKey)
 
	def AddNoShiftEnableKey(self,keys):
		if type(keys)==str:
			return self._SetKeyGroup(keys,noShiftEnableKey)
		for key in keys:
			self._SetKeyGroup(key,self.noShiftEnableKey)

	def _SetKeyGroup(self,key,target):
		key=key.upper()
		if not key in str2key:
			raise ValueError(_("%s は存在しないキーです。" % key))
		try:
			self.disablePattern.remove(set(key))
		except ValueError:
			pass
		self.enableKey.discard(key)
		self.functionKey.discard(key)
		self.modifierKey.discard(key)
		self.noShiftEnableKey.discard(key)
		target.add(key)

	def Check(self,keyString):
		if keyString=="":
			self.errorString="キーが指定されていません。"
			return False

		self.errorString=""
		keys=keyString.upper().split("+")
		modFlg=False
		shiftFlg=False
		funcCount=0
		enableCount=0
		noShiftCount=0
		for key in keys:
			if key in self.modifierKey:
				if key=="SHIFT":
					shiftFlg=True
				else:
					modFlg=True
				continue
			if key in self.functionKey:
				funcCount+=1
				continue
			if key in self.enableKey:
				enableCount+=1
				continue
			if key in self.noShiftEnableKey:
				noShiftCount+=1
				continue

			#ここまでcontinueされなかったらエラー
			self.errorString=_("%s は使用できないキーです。") % (key)
			return False

		#組み合わせの妥当性確認
		if len(keys)==1:
			if funcCount>0:
				return True
			else:
				if modFlg>0 or shiftFlg>0:
					self.errorString=_("修飾キーのみのパターンは設定できません。")
				else:
					self.errorString=_("このキーは修飾キーと合わせて指定する必要があります。")
				return False

		#２つ以上が指定されている場合
		if funcCount+enableCount+noShiftCount>1:
			self.errorString=_("修飾キーでないキーを複数指定することはできません。")
			return False
		elif modFlg==False and shiftFlg==False and funcCount==0:
			self.errorString=_("このキーは、SHIFTキー以外の修飾キーと合わせて指定する必要があります。")
			return
		elif funcCount==0 and noShiftCount==0 and enableCount==0:
			self.errorString=_("修飾キーのみの組み合わせは指定できません。")
			return False
		if enableCount>0 and modFlg==False and shiftFlg==False:
			raise Error("コードのバグです。")
		if noShiftCount>0 and modFlg==False:
			self.errorString=_("このキーは、SHIFTキー以外の修飾キーと合わせて指定する必要があります。")
			return False

		if set(keys) in self.disablePattern:
			self.errorString=_("この組み合わせは別の用途で予約されているため、利用できません。")
			return False

		return True

	def GetLastError(self):
			return self.errorString

	def GetUsableKeys(self):
		ret=[]
		ret.extend([*self.modifierKey,*self.functionKey,*self.enableKey,*self.noShiftEnableKey])
		return ret
