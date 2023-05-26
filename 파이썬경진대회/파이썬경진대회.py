import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps

##################################
def WhatName(num):
	global imgName, nchise, chise
	if num == 0:
		imgName = str1.get()
		chise = Image.open(f"{imgName}")
		chise.save(f"image_converter/{imgName}")
		nchise = chise

	elif num == 1:
		nchise = chise.transpose(Image.FLIP_LEFT_RIGHT)

	elif num == 2:
		nchise = chise.transpose(Image.FLIP_TOP_BOTTOM)

	elif num == 3:
		angle = int.get()
		nchise = chise.rotate(angle)

	elif num == 4:
		nchise = ImageOps.grayscale(chise)

	elif num == 5:
		nchise = chise.filter(ImageFilter.EMBOSS)

	elif num == 6:
		nchise = chise.filter(ImageFilter.BLUR)

	elif num == 7:
		nchise = chise.filter(ImageFilter.FIND_EDGES)

	elif num == 8:
		nchise = chise.filter(ImageFilter.CONTOUR)

	#tk_chise = ImageTk.PhotoImage(f"image_converter/{imgName}")
	#canvas.create_image(565, 565, image=tk_chise)
	nchise.save(f"image_converter/{imgName}")
	chise = nchise

def Start():
	WhatName(0)

def RightLeft():
	WhatName(1)

def UpDown():
	WhatName(2)

def Expand():
	WhatName(3)

def Grayscale():
	WhatName(4)

def Emboss():
	WhatName(5)

def Blur():
	WhatName(6)

def Find_Edge():
	WhatName(7)

def Contour():
	WhatName(8)

def Save():
	if str2.get() == '':
		nchise.save(f"{imgName}")
		os.remove(f"image_converter/{imgName}")

	else :
		changeName = str2.get()
		nchise.save(f"{changeName}")
		os.remove(f"image_converter/{imgName}")
		os.remove(f"{imgName}")

def Exit():
	window.destroy()
##################################

##################################
window = Tk()

window.geometry("835x565")
window.resizable(width=FALSE, height=FALSE)
window.title("사진 변환기")

canvas = Canvas(window, width=565, height=565, bg="white")
canvas.place(x=270, y=0)

bt_Name = Button(window, text="사진 불러오기", command=Start)
bt_RL = Button(window, text="좌우반전", command=RightLeft)
bt_UD = Button(window, text="상하반전", command=UpDown)
bt_EP = Button(window, text="회전하기", command=Expand)
bt_GR = Button(window, text="흑백효과", command=Grayscale)
bt_EM = Button(window, text="엠보효과", command=Emboss)
bt_BL = Button(window, text="블러처리", command=Blur)
bt_CO = Button(window, text="경계추출", command=Find_Edge)
bt_FE = Button(window, text="연필효과", command=Contour)

int = IntVar()
Angle_Input = ttk.Entry(window, width=12, textvariable=int)

str1 = StringVar()
Image_Name = ttk.Entry(window, width=25, textvariable=str1)

str2 = StringVar()
New_Name = ttk.Entry(window, width=12, textvariable=str2)

bt_Save = Button(window, text="저장하기", command=Save)
bt_Exit = Button(window, text="화면 종료하기", width=37, command=Exit)

Image_Name.grid(row=1, column=1, columnspan=3)
Angle_Input.grid(row=2, column=4)
New_Name.grid(row=4, column=4)

bt_Name.grid(row=1, column=4)
bt_RL.grid(row=2, column=1)
bt_UD.grid(row=2, column=2)
bt_EP.grid(row=2, column=3)
bt_GR.grid(row=3, column=1)
bt_EM.grid(row=3, column=2)
bt_BL.grid(row=3, column=3)
bt_CO.grid(row=4, column=1)
bt_FE.grid(row=4, column=2)
bt_Save.grid(row=4, column=3)
bt_Exit.grid(row=5, column=1, columnspan=4)

window.mainloop()
##################################