###1~3번 문제
#1. items, counts 리스트 변수를 선언하고, 둘을 합친 딕셔너리 변수를 선언.
#2. 색소폰의 개수를 1000개로 변경
#3. 트럼펫을 삭제
###

items = ['색소폰', '바이올린', '피아노', '트럼펫', '일렉기타', '베이스기타', '통기타', '리코더', '우쿨렐레', '플루트']
counts = [80, 74, 92, 52, 21, 94, 48, 64, 20, 89]
dic = {}

#1
for i in range(len(items)):
	dic[items[i]] = counts[i]

print("\n#1\n", dic)

#2
dic['색소폰'] = 1000
print("\n#2\n", dic)

#3
del(dic['트럼펫'])
print("\n#3\n", dic)


###4~6번 문제
#4. 악기 개수의 총합을 출력
#5. 가장 적은 악기와 개수를 출력
#6. 가장 많은 악기와 개수를 출력
###

#4
lis = list(dic.values())
num = 0

for j in range(len(lis)):
	num += lis[j]

print("\n#4\n", f"총합:{num}")

#5
minnum = 100000
maxnum = -999999

for h in dic.keys():
	if minnum > dic[h]:
		minnum = dic[h]
		mintems = h

	if maxnum < dic[h]:
		maxnum = dic[h]
		maxtems = h

print("\n#5\n", f"가장 적은 악기 : {mintems}, 개수 : {minnum}")

#6

print("\n#6\n", f"가장 많은 악기 : {maxtems}, 개수 : {maxnum}")

###7~9번 문제
#7. 딕셔너리 변수 값을 [개수, 가격]으로 변경하기
# 가격은 10,000 ~ 99,999 사이의 랜덤한 가격을 추가하기
#8. 개수 가격이 가장 높은 악기명을 출력
#9. 각각 악기명, 개수, 가격 리스트 변수로 복사
###

#7
import random as r 

for i in dic.keys():
	dic[i] = [dic[i], r.randint(10000,99999)]

print("\n#7\n", dic)

#8
for i in dic.keys():
	if dic[i][0] * dic[i][1] > maxnum:
		maxtems = i
print("\n#8\n", f"개수 X 가격이 가장 높은 악기명 :{maxtems}")

#9
cnt = []
mon = []

for i in dic.keys():
	cnt.append(dic[i][0])
	mon.append(dic[i][1])

print("\n#9")
print("악기명 리스트 :", list(dic.keys()))
print("개수 리스트 :", cnt)
print("가격 리스트 :", mon)