# CopyRight james at doubtlesshouse dot org dot uk & Released under GPLv3

import sys, os, os.path


class pffDirectory:
	def __init__(self, folder):
		confDir = os.path.abspath(os.getenv("HOME")+"/.photofreeflow/"+folder)
		if not os.path.isdir(confDir):
			os.makedirs(confDir)


		return




currentDir = pffDirectory(sys.argv[1])


import wx
app = wx.PySimpleApp()
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
#frame.Show(True)
# app.MainLoop()

