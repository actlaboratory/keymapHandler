from .keymapHandler import KeymapHandler
from .keyFilter import KeyFilter
from .acceleratorEntry import AcceleratorEntry
from .menuItemsStore import get_ref
from .str_to_key import str_to_key

def make_entry(ref, key, filter, log):
	"""ref(String)と、/区切りでない単一のkey(String)からwx.AcceleratorEntryを生成"""
	key = key.upper()  # 大文字に統一して処理

	modifier_keys = {
		"CTRL": wx.ACCEL_CTRL,
		"ALT": wx.ACCEL_ALT,
		"SHIFT": wx.ACCEL_SHIFT
	}

	if filter and ("WINDOWS" in filter.modifier_key):
		modifier_keys["WINDOWS"] = wx.MOD_WIN

	flags = 0
	flag_count = 0
	for name, value in modifier_keys.items():
		if name + "+" in key:
			flags |= value
			flag_count += 1
	# 修飾キーのみのもの、修飾キーでないキーが複数含まれるものはダメ
	codestr = key.split("+")
	if not len(codestr) - flag_count == 1:
		log.warning("%s is invalid pattern." % key)
		return False

	codestr = codestr[len(codestr) - 1]
	if not codestr in str_to_key:  # 存在しないキーの指定はエラー
		log.warning("keyname %s is wrong" % codestr)
		return False

	# フィルタの確認
	if filter and not filter.check(key):
		log.warning("%s(%s): %s" % (ref, key, filter.get_last_error()))
		return False
	return AcceleratorEntry(flags, str_to_key[codestr], get_ref(ref.upper()), ref.upper())
