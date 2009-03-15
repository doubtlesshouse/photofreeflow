# CopyRight james at doubtlesshouse dot org dot uk & Released under GPLv3

import sys, os, os.path, glob



class pffDirectory:
	confDir =  ""
	photos = []
	def __init__(self, folder):
		self.confDir = os.path.abspath(os.getenv("HOME")+"/.photofreeflow/"+folder)
		if not os.path.isdir(self.confDir):
			os.makedirs(self.confDir)
		for infile in glob.glob(os.path.join(folder, '*.*')):
			self.photos.append(	pffPhoto(self, infile) )
		return
	def getConfDir(self):
		return self.confDir


class pffPhoto:
	fileName = ""
	def __init__(self, DirObj, photo):
		self.fileName = os.path.basename(photo)
		photoConfFile = os.path.join(DirObj.getConfDir(), self.fileName+".xml")
		if os.path.isfile(photoConfFile):
			print(photo)
		else:
			open(photoConfFile, 'w').close()


currentDir = pffDirectory(sys.argv[1])


import wx
app = wx.PySimpleApp()
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
#frame.Show(True)
# app.MainLoop()

