#라디오버튼 컨트롤
from tkinter import *
'''
def myFunc():
	if myVar.get() == 1:
		label1.configure(text="현대")
	elif myVar.get() == 2:
		label1.configure(text="기아")
	else:
		label1.configure(text="KG")

root = Tk()
root.geometry('300x200')

myVar = IntVar()
rb1 = Radiobutton(root, text="현대", variable=myVar, value=1, command=myFunc)
rb1.pack()
rb2 = Radiobutton(root, text="기아", variable=myVar, value=2, command=myFunc)
rb2.pack()
rb3 = Radiobutton(root, text="KG", variable=myVar, value=3, command=myFunc)
rb3.pack()

label1 = Label(root, text="선택한 차량 :",fg="red")
label1.pack()

root.mainloop()	
'''


#컨트롤의 배치
'''
root = Tk()
root.geometry('500x200')

bt1 = Button(root, text="1")
bt2 = Button(root, text="2")
bt3 = Button(root, text="3")

bt1.pack(side=LEFT)
bt2.pack(side=LEFT)
bt3.pack(side=LEFT)

bt1.pack(side=RIGHT)
bt2.pack(side=RIGHT)
bt3.pack(side=RIGHT)

bt1.pack(side=TOP)
bt2.pack(side=TOP)
bt3.pack(side=TOP)

bt1.pack(side=BOTTOM)
bt2.pack(side=BOTTOM)
bt3.pack(side=BOTTOM)

for i in range(1, 11, 1):
	i = Button(root, text=f"{i}")
	i.pack(side=LEFT)

bt1.pack(side=TOP, fill=X, padx=10, pady=10)
bt2.pack(side=TOP, fill=X, padx=10, pady=10)
bt3.pack(side=TOP, fill=X, padx=10, pady=10)

for i in range(1, 11, 1):
	for j in range(1, 11, 1):
		j = Button(root, text=f"{j}")
		j.pack(side=TOP)


root.mainloop()
'''

#마우스 클릭 이벤트
'''
from tkinter import messagebox

def clickLeft(event):
	messagebox.showinfo("마우스", "왼쪽 마우스가 클릭됨")

root = Tk()

root.bind("<Button-1>", clickLeft)
root.mainloop()
'''

#event 매개변수의 활용
def clickMouse(event):
	if event.num == 1:
		txt = "왼쪽 버튼 : (" + str(event.x) + ", " + str(event.y) + ")"
		label1.configure(text = txt, fg="red")

	if event.num == 3:
		txt = f"오른쪽 버튼 : ({str(event.x)}, {str(event.y)})"
		label1.configure(text = txt, fg="blue")
	
root = Tk()
root.geometry("400x400")

label1 = Label(root, text="여기가 바뀝니다.", fg="red")
label1.pack(expand=True, anchor=CENTER)

root.bind("<Button>", clickMouse)
root.mainloop()