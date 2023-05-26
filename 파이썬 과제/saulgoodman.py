'''
#1
a, b = 100, 200
print("#1\n", f"{a} + {b} = {a+b}")

#2
c, d = '순천향', '대학교'
print("\n#2\n", c+d)

#3
print("\n#3")
name = input("이름 : ")
age = int(input("나이 : "))

print(f"{name}({age})")

#4
if age > 20:
	print("\n#4\n", f"{name}({age}) 성인")

else:
	print("\n#4\n", f"{name}({age}) 미성년자")

#5
print("\n#5")
numList = [num for num in range(1, 100, 2)]
for i in numList:
	if 55 <= i < 64:
		print(i, end=' ')

#6
print("\n#6")
for j in numList:
	if j > 94 or j < 2:
		print(j, end=' ')

#7
print("\n#7")
cnt = int(input("점수 => "))
print(cnt >= 70)

#8
d1 = "abc"
d2 = "가나다"

print("\n#8\n", d1==d2)

#9
print("\n#9")
cnt2 = int(input("점수 => "))

if cnt2 >= 90:
	print("A")
elif cnt2 >= 80:
	print("B")
else:
	print("C")	

#10
print("\n#10")
for w in range(10):
	print("*"*w)

#11
hunList = [hun for hun in range(101, 200, 2)]
print("\n#11\n", sum(hunList))

#12
print("\n#12")
for x in range(2, 10):
	for y in range(2, 10):
		print(f"{x} x {y} = {x*y}")
	print("-"*20)

#13
print("\n#13")
nanList = [nan+1 for nan in range(100)]

for z in range(len(nanList)):
	if nanList[z]%6 == 1 or nanList[z]%6 == 5:
		print(nanList[z], end=' ')


#14
print("\n#14")
cntfei = 0

while True:
	cntfei += 1

	if cntfei >= 100:
		break

#15
import random as r
diceList = []

for i in range(100):
	diceList.append(r.randint(1,6))

print("\n#15")
for j in range(1, 7):
	print(f"{j}이 나온 횟수 : {diceList.count(j)}")

#16
suList = [i for i in range(5)]
su1List = [j for j in range(5,8)]
hapList = suList+su1List

print(f"\n#16\n {hapList}")

#17
print(f"\n#17\n {hapList[-1:]}")

#18
hapList[1:2] = 9, 9, 9
print(f"\n#18\n {hapList}")

#19
for i in range(hapList.count(9)):
	hapList.remove(9)
print(f"\n#19\n {hapList}")

#20
import random as r
tweList = [r.randint(1,20) for h in range(20)]
tweList.sort(reverse=True)

print(f"\n#20\n {tweList}")


#21
dic = {'a':0, 'b':1, 'c':2}
print(f"\n#21\n {dic}")

#22
dic['a'] = 9
print(f"\n#22\n {dic}")

#23
dic['d'] = 3
print(f"\n#23\n {dic}")

#24
del(dic['a'])
print(f"\n#24\n {dic}")

#25
print(f"\n#25\n {len(dic)}")

#26
print(f"\n#26\n {list(dic.keys())}")

#27
print(f"\n#27\n {list(dic.values())}")

#28
print(f"\n#28")
for i in dic.keys():
	print(i, dic[i])

#29
print(f"\n#29\n {'a' in dic}")

#30
def jakhol(n):
	if type(n) is int:
		if n%2 == 1:
			return True
		else:
			return False
	else:
		return "No"

jakhol(input("숫자 입력 : "))
'''
