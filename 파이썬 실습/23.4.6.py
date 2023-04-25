#사용자 정의 함수의 필요성
"""
print("A.")
num1 = int(input("1 ==> "))
num2 = int(input("2 ==> "))
hap = num1 + num2
print(f"result : {hap}")

print("\nB.")
num1 = int(input("1 ==> "))
num2 = int(input("2 ==> "))
hap = num1 + num2
print(f"result : {hap}")

print("\nC.")
num1 = int(input("1 ==> "))
num2 = int(input("2 ==> "))
hap = num1 + num2
print(f"result : {hap}")
"""

"""
def hapFunc():
	num1 = int(input("1 ==> "))
	num2 = int(input("2 ==> "))
	return num1 + num2

print("A.")
hap = hapFunc()
print(f"result : {hap}")

print("\nB.")
hap = hapFunc()
print(f"result : {hap}")

print("\nC.")
hap = hapFunc()
print(f"result : {hap}")
"""

"""
import hap #파이썬 실습의 "hap"파일 참고

print("A.")
hap.hapFunc()

print("\nB.")
hap.hapFunc()

print("\nC.")
hap.hapFunc()
"""

#함수의 기본 형태
"""
## 함수 정의 부분
def plus(v1, v2) :
	result = 0
	result = v1 + v2
	return result

## 전역변수 선언 부분
hap = 0

## 메인 코드 부분
hap = plus(100, 200)
print("100과 200의 plus() 함수 결과는 ", hap)
"""

#함수를 이용한 계산기 구현
"""
## 계산기 함수 정의
def calculater(v1, v2, op):
	result = 0
	if op == '+':
		result = v1 + v2

	elif op == '-':
		result = v1 - v2

	elif op == '*':
		result = v1 * v2

	elif op == '/':
		result = v1 / v2

	return result	

## 전역변수 선언
res = 0
var1, var2, oper = 0, 0, ""

## 메인 코드
oper = input("계산 입력(+, -, *, /) : ")
var1 = int(input("첫 번째 숫자 입력 : "))
var2 = int(input("두 번째 숫자 입력 : "))

res = calculater(var1, var2, oper)
print(f"## 계산기 : {var1} {oper} {var2} = {res}")
"""

#반환값이 2개 있는 함수
"""
## 함수 정의
def func3():
	result1 = 100
	result2 = 200
	return result1, result2

## 전역변수 선언
hap1, hap2 = 0, 0

## 메인 코드
hap1, hap2 = func3()
print(f"func3()에서 돌려준 값 ==> {hap1} {hap2}")
"""

#함수 만들기로 로또 추첨하기
"""
import random as r

## 함수 정의
def getNum(l):
	while True :
		ranNum = r.randint(1, 45)
		if ranNum in lisNum:
			pass
		else:
			break
	return ranNum

## 전역변수 선언
lottoList = []
for i in range(6):
	lottoList.append(getNum(lottoList))

## 메인 코드
lottoList.sort()
print("로또번호 => ", end='')
for j in lottoList:
	print(j, end='')
"""

#완벽히 이해했어!
import 완벽해

완벽히_이해했어()