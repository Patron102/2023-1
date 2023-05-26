#클래스 만들기
'''
class Rabbit:
	shape = ""
	xPos = 0
	yPos = 0

	def goto(self, x, y):
		self.xPos = x
		self.yPos = y

	def showMe(self):
		print(f"shape:{self.shape}")
		print(f"X:{self.xPos}")
		print(f"Y:{self.yPos}")


rabbit1 = Rabbit()
rabbit2 = Rabbit()
rabbit3 = Rabbit()

rabbit1.shape = "원"
rabbit2.shape = "삼각형"
rabbit3.shape = "토끼"

rabbit1.goto(100,200)
rabbit1.showMe()

rabbit2.showMe()
'''

#생성자
class Rabbit:
	shape = ""
	xPos = 0
	yPos = 0

	def __init__(self, value="없음", x=10, y=10):
		self.shape = value
		self.xPos = x
		self.yPos = y

	#def __init__(self):
		#self.shape = "없음"


	def goto(self, x, y):
		self.xPos = x
		self.yPos = y

	def showMe(self):
		print(f"shape:{self.shape}")
		print(f"X:{self.xPos}")
		print(f"Y:{self.yPos}")

	def __add__(self, other):
		print(f"{self.shape}와 {other.shape}가 만났습니다")

	#def __del__(self):
		#print("Bye~!")

rabbit1 = Rabbit()
rabbit1.shape = "엽기토끼"
rabbit2 = Rabbit()
rabbit2.shape = "커비"

rabbit1 + rabbit2
