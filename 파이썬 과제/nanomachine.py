'''
#로또번호 뽑기
#sample 변수 사용 X
import random

for i in range(10):
	lottoList = [lotto for lotto in range(1, 46, 1)]
	result = []
	lottoNum = 0

	for j in range(6):
		lottoNum = random.choice(lottoList)
		lottoList.remove(lottoNum)
		result.append(lottoNum)

	print(result)

print("\nor\n")

#sample 변수 사용 O
lotto = list(range(46))

for i in range(10):
    lottoSample = random.sample(lotto, 6)
    print(lottoSample)
'''
'''
#####################################
import random as r 
items = ['색소폰', '바이올린', '피아노', '트럼펫', '일렉기타', '베이스기타', '통기타', '리코더', '우쿨렐레', '플루트']
counts = [80, 74, 92, 52, 21, 94, 48, 64, 20, 89]
dic = {}
#####################################
#1. items, counts 리스트 변수를 선언하고, 둘을 합친 딕셔너리 변수를 선언.
for i in range(len(items)):
	dic[items[i]] = counts[i]

print("#1\n", dic)

#2. 색소폰의 개수를 1000개로 변경
dic['색소폰'] = 1000
print("\n#2\n", dic)

#3. 트럼펫을 삭제
del[dic['트럼펫']]
print("\n#3\n", dic)

#4. 악기 개수의 총합을 출력
instList = list(dic.values())
totalNum = 0
for j in instList:
	totalNum += j

print("\n#4\n", f"총합 : {totalNum}")

#5. 가장 적은 악기와 가장 많은 악기의 개수를 출력
minnum = 100000
maxnum = -999999

for k in dic.keys():
	if minnum > dic[k]:
		minnum = dic[k]
		minInst = k

	if maxnum < dic[k]:
		maxnum = dic[k]
		maxInst = k

print("\n#5\n", f"가장 적은 악기 : {minInst}, {minnum}개 / 가장 많은 악기 : {maxInst}, {maxnum}개")

#6. 딕셔너리 변수 값을 [개수, 가격]으로 변경하기
for h in dic.keys():
	dic[h] = [dic[h], r.randint(10000,99999)]

print("\n#6\n", dic)

#7. 개수 x 가격이 가장 높은 악기명을 출력
maxNum = -999999
for l in dic.keys():
	if maxNum < dic[l][0] * dic[l][1]:
		maxNum = dic[l][0] * dic[l][1]
		highInst = l

print("\n#7\n", f"개수 X 가격이 가장 높은 악기 : {highInst}")

#8. 각각 악기명, 개수, 가격 리스트 변수로 복사
InstCountList = []
InstPirceList = []

for n in dic.keys():
	InstCountList.append(dic[n][0])
	InstPirceList.append(dic[n][1])

print("\n#8\n", f"악기명 : {list(dic.keys())}\n 개수 : {InstCountList} \n 가격 : {InstPirceList}")
'''
'''
nList = [i+1 for i in range(40)]
nList[0] = 1000
bigNum = 0

for j in range(len(nList)):
	if nList[j] > bigNum:
		bigNum = nList[j]
		nList[j] = 1
		break


print("5:", nList)
'''

x = int(input("x : "))
y = int(input("y : "))

for i in range(x):
    pl = i
    for j in range(y):
        pl+=1
        if pl > y:
            pl=1
        print(pl, end=' ')
    print()
