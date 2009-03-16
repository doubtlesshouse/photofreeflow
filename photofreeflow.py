# CopyRight james at doubtlesshouse dot org dot uk & Released under GPLv3

import sys, os, os.path, glob, wx



class pffDirectory:
	photoDir = ""
	confDir =  ""
	photos = []
	def __init__(self, folder):
		self.photoDir = folder
		self.confDir = os.path.abspath(os.getenv("HOME")+"/.photofreeflow/"+self.photoDir)
		if not os.path.isdir(self.confDir):
			os.makedirs(self.confDir)
		for infile in glob.glob(os.path.join(self.photoDir, '*.*')):
			self.photos.append(	pffPhoto(self, infile) )
		return
	def getConfDir(self):
		return self.confDir
	def getPhotoDir(self):
		return self.photoDir
	def getImage(self,idx):
		return self.photos[idx]


class pffPhoto:
	fileName = ""
	DirObj = ""
	def __init__(self, DirObj, photo):
		self.fileName = os.path.basename(photo)
		self.DirObj = DirObj
		photoConfFile = os.path.join(self.DirObj.getConfDir(), self.fileName+".xml")
		if os.path.isfile(photoConfFile):
			print(photo)
		else:
			open(photoConfFile, 'w').close()
	def getFullFileName(self):
		return os.path.join(self.DirObj.getPhotoDir(), self.fileName)

currentDir = pffDirectory(sys.argv[1])

class MyPaintingWindow(wx.Window):
	def __init__(self, parent, ppfdir):
		wx.Window.__init__(self, parent)

		print ppfdir.getImage(1).getFullFileName()
		image = wx.Image(ppfdir.getImage(1).getFullFileName(), type=wx.BITMAP_TYPE_ANY)
		w, h  = image.GetWidth(), image.GetHeight()
		ww, wh = parent.GetSizeTuple()
		resize = min(float(wh)/float(h),float(ww)/float(w))
		scaled_image = image.Scale(w*resize,h*resize)
		self.bitmap = wx.BitmapFromImage(scaled_image)
		self.Bind(wx.EVT_PAINT, self.on_paint)


	def on_paint(self, event):
		dc = wx.PaintDC(self)
		dc.DrawBitmap(self.bitmap, 0, 0, useMask=False)

class MyFrame(wx.Frame):
	def __init__(self, ppfDir):
		wx.Frame.__init__(self, None, title="Drawing Frame", size=(800, 300))
		window = MyPaintingWindow(self, ppfDir)



app = wx.PySimpleApp(redirect=False)

frame = MyFrame(pffDirectory(sys.argv[1]))
frame.Show()

app.MainLoop()















