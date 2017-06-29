import sys
import os
import shutil
import PIL.Image
import tkMessageBox
import glob
import win32api
from tkFileDialog import *
from Tkinter import *


mGui = Tk()

mGui.geometry('900x500')
mGui.title('Swipe')

image_list = []
lb = Listbox(mGui, width = 50)
lbv = Listbox(mGui, width = 50)
content = ''
filepath = ''
filepathSave = ''
drives = []
mydrive = ''
srchbox = IntVar()
drive1 = IntVar()
drive2 = IntVar()
drive3 = IntVar()
drive4 = IntVar()
allf = []

driveCheckbox = Checkbutton()
driveCheckbox2 = Checkbutton()
driveCheckbox3 = Checkbutton()
driveCheckbox4 = Checkbutton()


def open_file():
	global content
	global filepath
	global entry
	filename = askdirectory()
	filepath = os.path.dirname(filename)
	entry.delete(0, END)
	entry.insert(0, filepath)
	return content

def save_file():
	global content
	global filepathSave
	global entrySave
	filename = askdirectory()
	filepathSave = os.path.dirname(filename)
	entrySave.delete(0, END)
	entrySave.insert(0, filepathSave)
	return content


def location():

	global entry, entrySave
	global filepath, filepathSave

	entryLabel = Label(mGui, text='Start Location')
	entryLabel.place(x = 20, y = 100)

	entry = Entry(mGui, width = 40, textvariable = filepath)
	entry.place(x = 120, y = 100)

	entrySave = Entry(mGui, width = 35, textvariable = filepathSave)
	entrySave.place(x = 650, y = 330)

	BrowseButton = Button(mGui, text = '...', command = open_file)
	BrowseButton.place(x = 350, y = 100)

	BrowseButtonSave = Button(mGui, text = '...', command = save_file)
	BrowseButtonSave.place(x = 850, y = 330)

def imgSearch():
	global filepath, srchbox
	global image_list
	global lb, lbv
	global allf
	filetypes = ('*.ras', '*.xwd', '*.bmp', '*.jpe', '*.jpg', '*.jpeg', '*.xpm', '*.ief', '*.pbm', '*.tif', '*.gif', '*.ppm', '*.xbm', '*.tiff', '*.rgb', '*.pgm', '*.png','*.mp4', '*.pnm', '*.m1v', '*.mpeg', '*.mov', '*.qt', '*.mpa', '*.mpg', '*.mpe', '*.avi', '*.movie')

	x = srchbox.get()
	if x == 1:
		logicalDriveSearch()


	for filetype in filetypes:
		for filename in glob.iglob(filepath + '/' + filetype):
			if filetype == '*.mp4'or filetype == '*.m1v'or filetype == '*.mpeg'or filetype == '*.mov'or filetype == '*.qt'or filetype == '*.mpa'or filetype == '*.mpg'or filetype == '*.mpe'or filetype == '*.avi'or filetype == '*.movie':
				vid = filename
				allf.append(filename)
				lbv.insert(END, vid)
				
			else:
				imgfile=PIL.Image.open(filename)
				im = filename
				allf.append(filename)
		    	lb.insert(END, im)

		for filename in glob.iglob(filepath + '/*/' + filetype):
			if filetype == '*.mp4'or filetype == '*.m1v'or filetype == '*.mpeg'or filetype == '*.mov'or filetype == '*.qt'or filetype == '*.mpa'or filetype == '*.mpg'or filetype == '*.mpe'or filetype == '*.avi'or filetype == '*.movie':
				vid = filename
				allf.append(filename)
				lbv.insert(END, vid)
				
			else:
				imgfile=PIL.Image.open(filename)
				im = filename
				allf.append(filename)
		    	lb.insert(END, im)
		   
		for filename in glob.iglob(filepath + '/*/*/' + filetype):
			if filetype == '*.mp4'or filetype == '*.m1v'or filetype == '*.mpeg'or filetype == '*.mov'or filetype == '*.qt'or filetype == '*.mpa'or filetype == '*.mpg'or filetype == '*.mpe'or filetype == '*.avi'or filetype == '*.movie':
				vid = filename
				allf.append(filename)
				lbv.insert(END, vid)
				
			else:
				imgfile=PIL.Image.open(filename)
				im = filename
				allf.append(filename)
		    	lb.insert(END, im)

	imageBox = Label(mGui, text='Image Files:')
	imageBox.place(x = 20, y = 280)

	videoBox = Label(mGui, text='Video Files:')
	videoBox.place(x = 330, y = 280)
	lb.place(x = 20, y = 300)
	lbv.place(x = 330, y = 300)

def logicalDrives():
	global driveCheckbox, driveCheckbox2, driveCheckbox3, driveCheckbox4
	global drives, mydrive, filepath, drive1, drive2, drive3, drive4
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]
	count = len(drives)
	if count == 1 or count == 2 or count == 3 or count == 4:
		driveCheckbox = Checkbutton(mGui, text = drives[0],  onvalue = 1, offvalue = 0, variable = drive1)
		driveCheckbox.place(x = 200, y = 60)
	if count == 2 or count == 3 or count == 4:
		driveCheckbox2 = Checkbutton(mGui, text = drives[1], onvalue = 1, offvalue = 0, variable = drive2)
		driveCheckbox2.place(x = 250, y = 60)
	if count == 3 or count == 4:
		driveCheckbox3 = Checkbutton(mGui, text = drives[2], onvalue = 1, offvalue = 0, variable = drive3)
		driveCheckbox3.place(x = 300, y = 60)
	if count == 4:
		driveCheckbox4 = Checkbutton(mGui, text = drives[3], onvalue = 1, offvalue = 0, variable = drive3)
		driveCheckbox4.place(x = 450, y = 60)
	print(drives)

def logicalDriveSearch():
	global driveCheckbox, driveCheckbox2, driveCheckbox3, driveCheckbox4
	global drive1, drive2, drive3, drive4, filepath
	if drive1.get() == 1:
		driveCheckbox2.deselect()
		driveCheckbox3.deselect()
		driveCheckbox4.deselect()
		filepath = drives[0]

	if drive2.get() == 1:
		driveCheckbox.deselect()
		driveCheckbox3.deselect()
		driveCheckbox4.deselect()
		filepath = drives[1]

	if drive3.get() == 1:
		driveCheckbox2.deselect()
		driveCheckbox.deselect()
		driveCheckbox4.deselect()
		filepath = drives[2]

	if drive4.get() == 1:
		driveCheckbox2.deselect()
		driveCheckbox3.deselect()
		driveCheckbox.deselect()
		filepath = drives[3]

def saveFiles():
	global allf
	global filepathSave
	for i in allf:
		shutil.copy2(i,filepathSave)

OptionsLabel = Label(mGui, text='Search Options')
OptionsLabel.place(x = 20, y = 30)

SearchCheckBox = Checkbutton(mGui, text='Search Logical Drives', onvalue = 1, variable = srchbox, command = logicalDrives)
SearchCheckBox.place(x = 20, y = 60)


SearchButton = Button(mGui, text = 'Search', command = imgSearch)
SearchButton.place(x = 200, y = 190)

SaveButton = Button(mGui, text = 'Save Files', command = saveFiles)
SaveButton.place(x = 770, y = 370)

location()
input()
mGui.mainloop()