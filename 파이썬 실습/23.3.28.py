#리스트의 개념
"""
numList = [0, 0, 0, 0]
hap = 0

numList[0] = int(input("숫자 : "))
numList[1] = int(input("숫자 : "))
numList[2] = int(input("숫자 : "))
numList[3] = int(input("숫자 : "))

hap = numList[0] + numList[1] + numList[2] + numList[3]

print("합계 ==>", hap)
"""

#for문을 활용한 리스트
"""
numList = []
numList.append(0)
numList.append(0)
numList.append(0)
numList.append(0)

print(numList)
"""
"""
numList = []

for i in range(0,4):
	numList.append(0)
print(len(numList))
"""

"""
numList = []

for i in range(0,4):
	numList.append(0)
hap = 0

for i in range(0,4):
	numList[i] = int(input(" 숫자 : "))

for i in range(0, len(numList)):
	hap += numList[i]

print("합계 ==> ", hap)
"""

#리스트 값에 접근하기
"""
numList = [10, 20, 30, 40]
print("numList[-1]은 ", numList[-1], ", numList[-2]", numList[-2])
"""

#콜론(:)을 사용하여 범위 지정
"""
numList = [10, 20, 30, 40]
print(numList[0:3]) #[10, 20, 30]
print(numList[2:4]) #[30, 40]
print(numList[2:]) #[30, 40]
print(numList[:2]) #[10, 20]
"""

#리스트의 덧셈, 곱셈
"""
numList = [10, 20, 30]
mylist = [40, 50, 60]

print(numList + mylist) #[10, 20, 30, 40, 50, 60]
print(numList*2) #[10, 20, 30, 10, 20, 30]
"""

#실습1. 오늘의 명언 출력하기
"""
import random as r 

wiseSay = [
"삶이 있는 한 희망은 있다",
"언제나 현재에 집중할 수 있다면 행복할 것이다",
"신은 용기있는 자를 결코 버리지 않는다",
"피할 수 없으면 즐겨라",
"행복한 삶을 살기위해 필요한 것은 거의 없다",
"내일은 내일의 태양이 뜬다",
"계단을 밟아야 계단 위에 올라설 수 있다",
"행복은 습관이다, 그것을 몸에 지니라",
"1퍼센트의 가능성, 그것이 나의 길이다",
"작은 기회로 부터 종종 위대한 업적이 시작된다" ]

today = r.randint(0, len(wiseSay)-1)
print("오늘의 명언 ==>", wiseSay[today])
"""

#실습2. 리스트 실습
nList = list(range(0, 10)) #1
print("#1", nList)

nList[1] = 100 #2 
print("#2", nList)

sum = 0 #3
for i in nList:
	sum += i
print("#3", sum)

nList[2] = 'not number' #4
print("#4", nList)

dList = [] #5
for i in range(10, 21):
	dList.append(i)
tList = nList+dList
print("#5", tList)

print("#6", len(tList)) #6

print("#7", tList[9:]) #7

print("#8", nList[0:3]) #8

if type('not number') is str : #9
	tList[2] = 2
	print("#9", tList)

idx = 0 #10
while True:
	if tList[idx] >= 10:
		tList.remove(tList[idx])
		idx -= 1
	idx += 1

	if idx >= len(tList):
		break

print("#10", tList)









