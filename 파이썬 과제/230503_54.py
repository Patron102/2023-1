#상속 구현
'''
class Rabbit():
	shape = ""
	xPos = 0 
	yPos = 0

	def __init__(self, value="없음"):
		self.shape = value

	def goto(self, x, y) :
		self.xPos = x
		self.yPos = y

	def showMe(self):
		print(f"shape: {self.shape}")
		print(f"X: {self.xPos}")
		print(f"Y: {self.yPos}")

	def __del__(self):
		print("Bye~!")

	def __add__(self, other):
		print(f"{self.shape}과 {other.shape}이 만났습니다.")

class MountainRabbit(Rabbit):
	mountain = ""

	def __init__(self, shp="없음", value="남산"):
		self.shape = shp
		self.mountain = value

	#Method overriding
	def showMe(self):
		super().showMe()
		print(f"산: {self.mountain}")

mr = MountainRabbit("토끼", "백두산")
mr.showMe()
'''

#상속 실습
#학생 클래스를 생성하기
# 속성: 국어, 수학, 영어, 평균 점수
# 생성자: (국어, 수학, 영어) 점수를 입력 받고, 평균점을 계산함
# 평균점 리턴 함수: 학생의 평균 점수를 리턴
'''
class Student():
	kor = 0
	mat = 0
	eng = 0
	ave = None

	def __init__(self, korNum, mathNum, engNum):
		self.kor = korNum
		self.mat = mathNum
		self.eng = engNum
		self.ave = (korNum + mathNum + engNum) / 3

	def ave_Cal(self):
		return round(self.ave)

k = int(input("국어 : "))
m = int(input("수학 : "))
e = int(input("영어 : "))

s1 = Student(k, m, e)
print(f"평균 : {s1.ave_Cal()}")
'''

#실습2
'''
class MSG():
	ClName1 = ""
	ClName2 = ""

	def __init__(self, ClNa1="", ClNa2=""):
		self.ClName1 = ClNa1
		self.ClName2 = ClNa2

	def showMe(self):
		print(f"이 학과에 포함된 과목\n1. {self.ClName1}\n2. {self.ClName2}")

mg = MSG("파이썬", "메타버스")
mg.showMe()
'''

#GUI, TKinter 사용
from tkinter import *
'''
root = Tk()
#
root.title("창 조절 연습")
root.geometry("885x545")
root.resizable(width=FALSE, height=FALSE)
#
label1 = Label(root, text="난생처음~~ 파이썬을")
label1.pack()
label2 = Label(root, text="열심히", font=("궁서체", 30), fg="red")
label2.pack()
label3 = Label(root, text="코디 중입니다.", bg="yellow", width=20, height=5, anchor=CENTER)
label3.pack()
#
from tkinter import messagebox

def myFunc():
	messagebox.showinfo("버튼 클릭", "버튼을 눌렀군요 ^^")

root = Tk()
root.geometry('985x540')

button1 = Button(root, text="클릭하세요", font=30, fg="blue", bg="white", width=30, height=10, command=myFunc)
button1.pack()
#
from tkinter import messagebox

def myFunc2():
	if chk.get() == 0:
		messagebox.showinfo("", "체크박스 OFF네요.")
	else:
		messagebox.showinfo("", "체크박스 ON이네요.")

root = Tk()
root.geometry('300x100')

chk = IntVar()
cb1 = Checkbutton(root, text="클릭하세요", variable=chk, command=myFunc2)
cb1.pack()
'''

root.mainloop()
