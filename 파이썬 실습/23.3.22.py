#중첩 for문
"""
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)
"""

#tip
"""
if True :
    print("true") #Truea면 if가 나옴

else :
    print("false")

if False :
    print("true") #False면  else가 나옴
else :
    print("false")

if True :         #이때도 True인 if만 나옴
    print("1st") 
elif False :
    print("2nd")
elif False :
    print("3rd")
else :
    print("4th")
"""
#elif와 else는 if에 False가 있는게 아닌 이상 무조건 작동 안됨
"""
num = range(5) #시작 = 0. 끝값 + 1, 간격 = 1

print(num)

for i in num:
    print(i)
"""
"""
num = range(1, 5) #시작, 끝 +1, 간격 = 1

for i in num:
    print(i)

"""
"""
num = range(1, 5, 2) #시작, 끝+1, 간격 = 2

for i in num:
    print(i)
"""
"""
for i in range(3):
    for j in range(2):
        print(i,j)
"""






