from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageTk

## 함수 선언 부분 ##
def displayPhoto(img, width, height) :   
    global root, canvas, inPhoto, outPhoto, inX, inY
    if canvas != None :
        canvas.destroy()

    root.geometry(str(width)+"x"+str(height))
    root.resizable(width=FALSE, height=FALSE)
    cImage = ImageTk.PhotoImage(img)
    canvas = Canvas(root, width=width, height=height)
    canvas.create_image(0, 0, anchor=NW, image=cImage)
    canvas.pack()
    root.mainloop()

#파일 열기
def func_open() :     
    global root, cnavas, inPhoto, outPhoto, inX, inY, outX, outY
    filename = askopenfilename(parent=root, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif"), ("모든 파일", "*.*")))
    inPhoto = Image.open(filename)
    inX = inPhoto.width
    inY = inPhoto.height

    outPhoto = inPhoto.copy()
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#파일 저장
def func_save() :      
    global root, canvas, inPhoto, outPhoto, inX, inY
    if outPhoto == None:
        return
    saveFp = asksaveasfile(parent=root, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*")))
    outPhoto.save(saveFp.name)

#프로그램 종료
def func_exit() :
    exit()

#확대
def func_zoomin() :      
    global root, canvas, inPhoto, outPhoto, inX, inY, outX, outY
    scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue=2, maxvalue=8)
    outPhoto = outPhoto.resize((int(outX * scale), int(outY * scale)))
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#축소
def func_zoomout() :    
    global root, canvas, inPhoto, outPhoto, inX, inY, outX, outY
    scale = askinteger("축소배수", "축소할 배수를 입력하세요", minvalue=2, maxvalue=8)
    outPhoto = outPhoto.resize((int(outX / scale), int(outY / scale)))
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#상하 반전
def func_mirror1() :    
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = outPhoto.transpose(Image.FLIP_TOP_BOTTOM)
    outX = outPhoto.width   
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#좌우 반전
def func_mirror2() :      
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = outPhoto.transpose(Image.FLIP_LEFT_RIGHT)
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#회전
def func_rotate() :      
    global root, canvas, inPhoto, outPhoto, inX, inY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    outPhoto = outPhoto.rotate(degree, expand=True)
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#밝게/어둡게
def func_bright() :      
    global root, canvas, inPhoto, outPhoto, inX, inY
    value = askfloat("밝기 조절", "값을 입력하세요(0.0~5.0)", minvalue=0.0, maxvalue=5.0)
    outPhoto = ImageEnhance.Brightness(outPhoto).enhance(value)
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#엠보싱
def func_embos() :       
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = outPhoto.filter(ImageFilter.EMBOSS)
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#블러링
def func_blur() :        
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = outPhoto.filter(ImageFilter.BLUR)
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#연필스케치
def func_sketch() :  
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = outPhoto.filter(ImageFilter.CONTOUR)
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

#경계선추출
def func_contour() :        
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = outPhoto.filter(ImageFilter.FIND_EDGES)
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

## 전역 변수 선언 부분 ##
root, canvas = None, None
inPhoto, outPhoto = None, None
inX, inY = 0, 0
outX, outY = 0, 0

## 메인 코드 부분 ##
root = Tk()

root.geometry("500x500")
root.resizable(width=FALSE, height=FALSE)
root.title("포토 에디터")

mainMenu = Menu(root)
root.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_command(label = "파일 저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

generaterMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리", menu = generaterMenu)
generaterMenu.add_command(label = "확대", command = func_zoomin)
generaterMenu.add_command(label = "축소", command = func_zoomout)
generaterMenu.add_separator()
generaterMenu.add_command(label = "상하반전", command = func_mirror1)
generaterMenu.add_command(label = "좌우반전", command = func_mirror2)
generaterMenu.add_separator()
generaterMenu.add_command(label = "회전", command = func_rotate)

effectMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 효과", menu = effectMenu)
effectMenu.add_command(label = "밝기 조절", command = func_bright)
effectMenu.add_separator()
effectMenu.add_command(label = "엠보싱", command = func_embos)
effectMenu.add_command(label = "블러링", command = func_blur)
effectMenu.add_separator()
effectMenu.add_command(label = "연필 스케치", command = func_sketch)
effectMenu.add_command(label = "경계선 추출", command = func_contour)

root.mainloop()
