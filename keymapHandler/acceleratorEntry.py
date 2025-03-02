# AcceleratorEntry
#Copyright (C) 2019 Yukio Nozawa <personal@nyanchangames.com>
#Copyright (C) 2019-2025 yamahubuki <itiro.ishino@gmail.com>

import wx

class AcceleratorEntry(wx.AcceleratorEntry):
	#ショートカットキーの一致によって判定され、登録されたメニューコマンドの一致は無視される
	#refをstrで保持する

	def __init__(self,flags,key,cmd,ref_ame=""):
		super().__init__(flags,key,cmd)
		self.ref_name=ref_name

	def __eq__(self,other):
		# isinstance(other, Person)を除去
		if other is None or type(self) != type(other): return False
		if self.GetFlags()==other.GetFlags() and self.GetKeyCode()==other.GetKeyCode():
			return True
		return False

	def get_ref_name(self):
		return self.ref_name

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return "<AcceleratorEntry %s>" % self.get_ref_name()
