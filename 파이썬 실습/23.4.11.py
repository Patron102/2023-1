#전역변수와 지역변수
'''
a = 10 #전역변수

def f01():
	a = 0 #지역변수

def f02():
	b = 0

## 함수 정의 부분
def func1() :
	a = 10 # 지역변수
	print("func1()에서 a의 값 ", a)

def func2() :
	print("func2()에서 a의 값 ", a)

## 전역변수 선언 부분
a = 20

## 메인 코드 부분
func1()
func2()
'''

#global 예약어
'''
## 함수 정의 부분
def func1() :
	global a # a라는 변수를 전역변수로 선언
	a = 10 # 전역변수처럼 쓸 수 있게 됨.
	print("func1()에서 a의 값 ", a)

def func2() :
	print("func2()에서 a의 값 ", a)

## 전역변수 선언 부분
a = 20 #전역변수

## 메인 코드 부분
func1()
func2()
'''

#100일 기념일 날짜 구하기
'''
from datetime import datetime, timedelta

def getCurrent():
	curDate = datetime.now()
	return curDate

def getAfterDate(now, day):
	retDate = now + timedelta(days = day)
	return retDate

nowDate, afterDate = None, None
nowDate = getCurrent()
print(nowDate)

afterDate = getAfterDate(nowDate, 100)
print(afterDate)
'''

#비밀번호 생성하기
'''
password = input("input passowrd : ")

def chekPassword(str):
	if str.isalnum():
		return True

	else:
		return False

for i in range(10):
	pw = input("input password : ")

	if chekPassword(pw):
		print("ok")

	else:
		print("no")
'''
'''
#실습문제(자유과제)
#1 “letters” 문자열을 선언하고 첫 번째와 세 번째 문자를 출력
str1 = "letters"
print("#1\n",str1[1], str1[3])

#2 “12가3450” 문자열을 선언하고 뒤에 4자리만 출력
str2 = "12가3450"
print("\n#2\n", str2[3:])

#3 [‘배트맨’, ‘슈퍼맨’, ‘아이언맨’] 리스트를 선언하고, 슈퍼맨과 아이언맨 사이에 ‘헐크＇를 추가 후 출력
newList = ["배트맨", "슈퍼맨", "아이언맨"]
newList.insert(2, '헐크')
print("\n#3\n", newList)

#4 3번의 리스트 [‘배트맨’, ‘슈퍼맨’, ‘헐크’, ‘아이언맨’]에서 ‘헐크’를 삭제 후 출력
del(newList[2])
print("\n#4\n", newList)

#5 [1, 2, 3]과 [4, 5, 6] 리스트를 각각 선언하고 2개의 리스트 원소를 모두 가진 리스트를 생성 후 출력
numList1, numList2 = [1, 2, 3], [4, 5, 6]
totList = numList1 + numList2
print("\n#5\n", totList)

#6 [1, 2, 3, …, 9, 10] 리스트를 선언하고, 리스트의 최대값, 최소값을 각각 출력
tenList = []
for i in range(1, 11, 1):
	tenList.append(i)
print("\n#6\n", f"최대값 : {max(tenList)}, 최소값 : {min(tenList)}")

#7 [1, 3, 5, …, 99] 리스트를 생성하고, 리스트의 길이와 총합을 각각 출력
hunList = []
for j in range(1, 100, 1):
	hunList.append(j)
print("\n#7\n", f"리스트의 길이 : {len(hunList)}, 총합 : {sum(hunList)}")

#8 (1, 2, 3, 4, 5) 튜플을 선언하고, 리스트로 변환 후 출력
newtup = (1, 2, 3, 4, 5)
ttList = list(newtup)
print("\n#8\n", ttList)

#9 [1, 2, 3, 4, 5] 리스트를 선언하고, 튜플로 변환 후 출력
fiveList = [1, 2, 3, 4, 5]
fivdtup = tuple(fiveList)
print("\n#9\n", fivdtup)

#10 [0.1, 0.2, … 9.9, 10.0] 리스트를 선언 후 리스트와 길이를 출력
sosuList = [w/10 for w in range(1, 101)]
print("\n#10\n", f"리스트의 길이 : {len(sosuList)}, 총합 : {int(sum(sosuList))}")

#11 10번의 리스트를 [1, 2, 3, …, 99, 100]으로 변경 후 출력
nssList = []
for x in range(len(sosuList)):
	nssList.append(int(sosuList[x] * 10))
print("\n#11\n",nssList)
'''