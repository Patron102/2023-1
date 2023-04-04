###실습1~3
#1. 1~30의 값을 가진 리스트 생성
#2. 첫번째 값을 1000으로 변경
#3. 끝의 값을 3000으로 변경
###
nList = []
for i in range(1,31,1):
	nList.append(i)
print("1:", nList)

nList[0] = 1000
print("2:", nList)

nList[-1] = 3000
print("3:", nList)

###실습 4~6
#4. 리스트 값에 31~40을 추가
#5. 리스트에서 100 이상인 값을 인덱스+1 값으로 변경
#6. 리스트에서 인덱스 0~5의 값을 출력
###
for j in range(30, 41, 1):
	nList.append(j)
print("4:", nList)

idx = 0
while True:
	if nList[idx] >= 100:
		nList.remove(nList[idx])
		idx -= 1
	idx += 1

	if idx >= len(nList):
		for k in range(1, 2, 1):
			nList.append(k)
		nList.sort()
		break
print("5:", nList)

print("6:", nList[0:6])

###실습 7~10
#7. 리스트에서 인덱스 5~10의 값을 출력
#8. 리스트에서 인덱스 10의 값을 [0, 0, 0] 으로 변경
#9. 리스트에서 정수형이 아닌 값을 인덱스+1 값으로 변경
#10. 리스트 변수를 복사해 내림차순으로 출력
###
print("7:", nList[5:11])

nList[9] = [0, 0, 0]
print("8:", nList)

for l in range(len(nList)):
	if type(nList[l]) is not int:
		nList[l] = l+1
print("9:", nList)

nList2 = nList.copy()
nList2.sort(reverse = True)
print("10:", nList2)

###실습 11~13
#11. 리스트에서 값이 짝수인 값은 10배인 값으로 변경
###
nList.sort()
idx = 0
for z in range(len(nList)) :
	if idx%2 == 1 :
		nList[idx] = nList[idx] * 10
	idx += 1
print("11:", nList)

#실습 16
#100명의 학생의 수학 점수를 무작위로 0~100사이로 생성하고, 성적 리스트와 최고점, 최하점, 평균점을 출력하시오.
import random as r

ma = 0
mi = 100
d = 0
mList = []
for x in range(100):
	n = r.randint(0, x)
	mList.append(n)

for v in range(len(mList)):
	d += mList[v]
	
for w in range(len(mList)):
	if mList[w] > ma :
		ma = mList[w]
	if mList[w] < mi :
		mi = mList[w]


print("16:", mList)
print("최고 :",ma,"점,","최하 : ",mi,"점,", "평균 :", d/len(mList))





















































































































































































































