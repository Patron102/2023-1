#튜플
"""
numTup1 = (10, 20, 30)
numTup2 = 10, 20, 30
print(numTup1)
print(numTup2)
"""

#튜플 활용
"""
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myTuple)
"""

#딕셔너리
"""
myDict1 = {1:'a', 2:'b', 3:'c'}
print(myDict1)
myDict2 = {'a':1, 'b':2, 'c':3}
print(myDict2)

empDict = {'사번':1000, '이름':'홍길동', '부서':'케이팝'}
print(empDict)
print(empDict['이름'])
empDict['연락처'] = '010-1111-2222'
print(empDict)

print(empDict.keys())
print(empDict.values())
print(list(empDict.keys()))
print(list(empDict.values()))

print('사번'in empDict)
print('사번2'in empDict)

for k in empDict.keys():
	print(k, empDict[k])
"""

#가수 정보를 딕셔너리에 저장하고 출력하기
"""
singer = {}

singer['이름'] = "트와이스"
singer['구성원수'] = 9
singer['데뷰'] = "서바이벌 식스틴"
singer['대표곡'] = "CRY FOR ME"

for k in singer.keys():
	print(k, "==>", singer[k])
"""

#재고 관리 프로그램
"""
sufe = {}

print("**** 물품과 재고량 입력 ****")
while True :
	a = str(input("입력 물품 : "))
	if a == '':
		break
	b = int(input("재고량 : "))
	sufe[a] = b

print("**** 물품의 재고량 확인 ****")
while True:
	a1 = str(input("찾을 물품 : "))
	if a1 == '':
		break
	elif a1 in sufe:
		print(f"{sufe[a1]}개 남았어요")
	else:
		print("그 물품은 없어요")
"""