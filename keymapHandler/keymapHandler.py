# keymapHandler
#Copyright (C) 2019 Yukio Nozawa <personal@nyanchangames.com>
#Copyright (C) 2019-2025 yamahubuki <itiro.ishino@gmail.com>

import logging
import os
import wx

import configparser
from . import menuItemsStore
from .str2key import *
from .acceleratorEntry import AcceleratorEntry

# errorCodes定数
# 元々import errorCodesしていたのをひっぺがしている。追加していいが、変更してはいけない。
OK=0
FILE_NOT_FOUND=2
PARSING_FAILED=3
ACCESS_DENIED=4

class KeymapHandler():
	"""wxのアクセラレーターテーブルを生成"""

	def __init__(self, dict=None, filter=None, permitConfrict=None, log_prefix="app"):
		"""
			permitConfrictは(調べたいAcceleratorEntryのリスト,logger)を引数とし、booleanを返す任意の関数。
		"""
		self.log=logging.getLogger("%s.keymapHandler" % log_prefix)
		self.errors={}
		self.entries={}				#生成したAcceleratorEntry
		self.map={}					#ref番号→ショートカットキーに変換
		self.refMap={}				#キーの重複によりこのインスタンスで処理する必要のあるメニューと、そのとび先の本来のref
		self.permitConfrict=permitConfrict
		self.filter=filter			#指定の妥当性をチェックするフィルタ

		if dict:
			self.addDict(dict)


	def addDict(self,dict,sections=None):
		"""
			sectionsにlistまたはsetを指定すると、読み込むセクションを指定したもののみに制限できる。大文字で指定する。
			sectionsを指定しない場合、セクション名にHOTKEYが含まれるものはスキップされる
		"""
		read=configparser.ConfigParser()
		read.read_dict(dict)
		for identifier in read.sections():
			if (sections and (identifier.upper() not in sections)) or ((not sections) and "HOTKEY" in identifier):
				self.log.debug("skip section %s" % identifier)
				continue

			self.log.debug("read section %s" % identifier)
			self.entries[identifier]=[]
			for elem in read.items(identifier):
				if elem[1]!="":						#空白のものは無視する
					self.add(identifier,elem[0],elem[1])


	def addFile(self, filename,sections=None):
		"""
			指定されたファイルからキーマップを読もうと試みる。
			ファイルが見つからなかった場合は、FILE_NOT_FOUND を返す。
			ファイルがパースできなかった場合は、PARSING_FAILED を返す。
			 OKが返された場合であっても、キーの重複などで追加できなかったものがあった可能性があり、これについては、その情報がself.errorsに格納されるので呼出元で検証する必要がある。
			sectionsにlistまたはsetを指定すると、読み込むセクションを指定したもののみに制限できる。大文字で指定する。
			sectionsを指定しない場合、セクション名にHOTKEYが含まれるものはスキップされる
		"""
		self.log.debug("read file %s sections=%s" % (filename,str(sections)))
		if not os.path.exists(filename):
			self.log.warning("Cannot find %s" % filename)
			return FILE_NOT_FOUND
		newKeys=configparser.ConfigParser()
		ret=newKeys.read(filename, encoding="UTF-8")
		ret= OK if len(ret)>0 else PARSING_FAILED
		if ret==PARSING_FAILED:
			self.log.warning("Cannot parse %s" % filename)
			return ret

		#newKeysの情報を、検証しながらaddしていく
		for identifier in newKeys.sections():
			if (sections and (identifier.upper() not in sections)) or ((not sections) and "HOTKEY" in identifier):
				self.log.debug("skip section %s" % identifier)
				continue

			self.log.debug("read section %s" % identifier)
			for elem in newKeys.items(identifier):
				if elem[1]!="":				#空白のものは無視する
					self.add(identifier,elem[0],elem[1])
		return OK

	def SaveFile(self,fileName):
		"""
			指定した名前でキーマップの保存を試みる
			成功時はOKを、失敗時は理由に関わらずACCESS_DENIEDを返す
		"""
		c=configparser.ConfigParser()
		try:
			別セクションがあればそれを残せるので一応読み込んでおく
			c.read(fileName)
		except:
			#ファイル不存在等だが問題なし
			pass
		for section in self.entries.keys():
			c.add_section(section)
			for entry in self.entries[section]:
				c[section][entry.refName]=self.map[section][entry.refName]
		try:
			with open(fileName,"w", encoding='UTF-8') as f: return c.write(f)
			return OK
		except Exception as e:
			self.log.warning("keymap save (fn=%s) failed. %s" % (fileName,str(e)))
			return ACCESS_DENIED

	def GetError(self,identifier):
		"""指定されたビューのエラー内容を返し、内容をクリアする"""
		identifier=identifier.upper()
		try:
			ret=self.errors[identifier]
		except KeyError:
			return {}
		self.errors[identifier]={}
		return ret

	def GetKeyString(self,identifier,ref):
		"""指定されたコマンドのショートカットキー文字列を取得する"""
		ref=ref.upper()
		identifier=identifier.upper()

		try:
			return self.map[identifier][ref]
		except KeyError:
			#他のビューを検索
			for i in self.map:
				if ref in self.map[i]:
					return self.map[i][ref]
			return None
		#end except


	def GetTable(self, identifier):
		"""
			アクセラレーターテーブルを取得する。
			identifier で、どのビューでのテーブルを取得するかを指定する。
		"""
		if identifier.upper() in self.entries:
			return wx.AcceleratorTable(self.entries[identifier.upper()])
		else:
			return wx.AcceleratorTable([])


	def GetEntries(self,identifier):
		"""
			登録されているエントリーの一覧を取得する。
			identifier で、どのビューでのテーブルを取得するかを指定する。
		"""
		return self.entries[identifier.upper()]

	def Set(self,identifier,window,eventHandler=None):
		"""
			アクセラレータテーブルを指定されたウィンドウに登録する
			identifier で、どのビューでのテーブルを取得するかを指定する。
			windowには、登録先としてwx.windowを継承したインスタンスを指定する
			eventHandlerを指定すると、EVT_MENUをBindする
		"""
		if eventHandler:
			window.Bind(wx.EVT_MENU,eventHandler)
		return window.SetAcceleratorTable(self.GetTable(identifier))

	def makeEntry(self,*pArgs, **kArgs):
		return makeEntry(*pArgs,*kArgs)

	def add(self,identifier,ref,key):
		"""重複をチェックしながらキーマップにショートカットを追加する"""
		#refとidentifierは大文字・小文字の区別をしないので大文字に統一
		ref=ref.upper()
		identifier=identifier.upper()

		#identifierが新規だった場合、self.mapとself.entriesにセクション作成
		if not identifier in self.map.keys():
			self.entries[identifier]=[]
			self.map[identifier]={}

		#エントリーの作成・追加
		for e in key.split("/"):
			entry=self.makeEntry(ref,e,self.filter,self.log)
			if entry==False:
				self.addError(identifier,ref,key,"make entry failed")
				continue

			#キーの重複確認
			checkList=[]		#要確認リスト
			for i in self.entries[identifier]:
				if entry==i:
					checkList.append(i)
			if checkList:
					checkList.append(entry)
					if self.permitConfrict and self.permitConfrict(checkList,self.log):
						self.replaceOriginalRef(checkList,identifier)
						entry=None
					else:
						self.addError(identifier,ref,key,"confrict")
						continue

			#GetKeyStringに備えてself.mapに追加
			if ref in self.map[identifier]:
				#refが重複の場合、既存のself.map上のエントリの末尾に追加
				self.map[identifier][ref]=self.map[identifier][ref]+"/"+e
			else:
				#self.mapに新規エントリとして追加
				self.map[identifier][ref]=e

			#self.entriesに追加
			#重複確認・置換処理の関係でNoneになってる場合には既に追加済みを意味するのでここでは何もしない
			if entry:
				self.entries[identifier].append(entry)
		return

	def addError(self,identifier,ref,key,reason=""):
		"""エラー発生時、情報を記録する。"""
		self.log.warning("Cannot add %s=%s in %s reason=%s" % (ref,key,identifier,reason))
		try:
			self.errors[identifier][ref]=key
		except KeyError:
			self.errors[identifier]={}
			self.errors[identifier][ref]=key

	def replaceOriginalRef(self,items,identifier):
		"""
			refを独自のものに置き換えることによって、キーの重複を許容しながら登録する

			items		重複したキーが設定されているAcceleratorEntryのリスト
			identifier	itemsが設定されているウィンドウの識別名
		"""
		#keymap_keynameのrefを取得
		newref=menuItemsStore.getRef("keymap_"+items[0].ToRawString())
		self.refMap[newref]=[]

		#self.entriesからいったん削除
		for i in range(len(items)-1):
			self.entries[identifier].remove(items[0])

		#refを差し替えて再登録し、元のrefを記録
		for i in items:
			self.refMap[newref].append(i.GetCommand())
			self.entries[identifier].append(AcceleratorEntry(i.GetFlags(),i.GetKeyCode(),newref,i.GetRefName()))
		return True

	def isRefHit(self,ref):
		return ref in self.refMap

	def GetOriginalRefs(self,ref):
		return self.refMap[ref]


def make_entry(ref,key,filter,log):
	"""ref(String)と、/区切りでない単一のkey(String)からwx.AcceleratorEntryを生成"""
	key=key.upper()					#大文字に統一して処理

	modifire_keys ={
		"CTRL":wx.ACCEL_CTRL,
		"ALT":wx.ACCEL_ALT,
		"SHIFT":wx.ACCEL_SHIFT
	}

	if filter and ("WINDOWS" in filter.modifier_key):
		modifire_keys["WINDOWS"]=wx.MOD_WIN

	flags=0
	flag_count=0
	for name,value in modifire_keys.items():
		if name+"+" in key:
			flags|=value
			flag_count+=1
	#修飾キーのみのもの、修飾キーでないキーが複数含まれるものはダメ
	codestr=key.split("+")
	if not len(codestr)-flag_count==1:
		log.warning("%s is invalid pattern." % key)
		return False

	codestr=codestr[len(codestr)-1]
	if not codestr in str2key:			#存在しないキーの指定はエラー
		log.warning("keyname %s is wrong" % codestr)
		return False

	#フィルタの確認
	if filter and not filter.check(key):
		log.warning("%s(%s): %s" % (ref,key,filter.get_last_error()))
		return False
	return AcceleratorEntry(flags,str2key[codestr],menuItemsStore.getRef(ref.upper()),ref.upper())
