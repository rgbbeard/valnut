#!/usr/bin/python3
from tkinter import *
from functools import partial
from tkinter import ttk


class Object:
	_this = None
	__objects:int = 0

	def __init__(self):
		pass

	def _is_xscrollable(self)->bool:
		return hasattr(self._this, "xview")

	def _is_yscrollable(self)->bool:
		return hasattr(self._this, "yview")

	def append(self):
		self._this.pack()
		self.__objects+=1

	def objects(self)->int:
		return self.__objects


class Box(Object):
	__frame = None

	def __init__(self, root):
		super().__init__()

		# self.__frame = Frame(root, width=root.winfo_width(), height=root.winfo_height())
		self.__frame = Frame(root, width=800, height=800)
		self._this = self.__frame

	def scrollx(self):
		if super()._is_xscrollable():
			scrollX = Scrollbar(self._frame, orient='horizontal')
			scrollX.pack(side=BOTTOM, fill=X)

	def scrolly(self):
		if super()._is_yscrollable():
			scrollY = Scrollbar(self._frame, orient='vertical')
			scrollY.pack(side=LEFT, fill=Y)

	def scroll(self):
		self.scrollx()
		self.scrolly()


class Row(Object):
	def __init__(self):
		self._this = self


class Col(Object):
	def __init__(self):
		self._this = self
