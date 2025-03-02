from .keymapHandler import KeymapHandler
from .keyFilter import KeyFilter
from .acceleratorEntry import AcceleratorEntry
from .menuItemsStore import getRef
from .str2key import str2key

def makeEntry(ref,key,filter,log):
	"""ref(String)と、/区切りでない単一のkey(String)からwx.AcceleratorEntryを生成"""
	key=key.upper()					#大文字に統一して処理

	modifireKeys ={
		"CTRL":wx.ACCEL_CTRL,
		"ALT":wx.ACCEL_ALT,
		"SHIFT":wx.ACCEL_SHIFT
	}

	if filter and ("WINDOWS" in filter.modifierKey):
		modifireKeys["WINDOWS"]=wx.MOD_WIN

	flags=0
	flagCount=0
	for name,value in modifireKeys.items():
		if name+"+" in key:
			flags|=value
			flagCount+=1
	#修飾キーのみのもの、修飾キーでないキーが複数含まれるものはダメ
	codestr=key.split("+")
	if not len(codestr)-flagCount==1:
		log.warning("%s is invalid pattern." % key)
		return False

	codestr=codestr[len(codestr)-1]
	if not codestr in str2key:			#存在しないキーの指定はエラー
		log.warning("keyname %s is wrong" % codestr)
		return False

	#フィルタの確認
	if filter and not filter.Check(key):
		log.warning("%s(%s): %s" % (ref,key,filter.GetLastError()))
		return False
	return AcceleratorEntry(flags,str2key[codestr],menuItemsStore.getRef(ref.upper()),ref.upper())
