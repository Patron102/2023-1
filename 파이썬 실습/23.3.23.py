#구구단 계산기 만들기
"""
for i in range(2, 10, 1):
    print("="*12, i, "단", "="*12)
    for j in range(1, 10, 1):
        print(i, "X", j, "=", i*j)
print("="*30)
"""

#while문의 무한 반복
"""
hap = 0
num1, num2 = 0, 0

while True:
    num1 = int(input("숫자1 ==> "))
    num2 = int(input("숫자2 ==> "))

    hap = num1 + num2
    print(num1, "+", num2, "=", hap)
"""

#break문과 continue문
"""
for i in range(1,1001,1):
    print("반복문을", i, "회 실행합니다.")
    break #1회만 작동하고 반복문을 빠져나옴
"""

"""

hap = 0
num1, num2 = 0, 0

while True:
    num1 = int(input("숫자1 ==> "))
    if num1 == 0 :
        break #변수에 0이 입력되면 반복문을 빠져나옴
    num2 = int(input("숫자2 ==> "))

    hap = num1 + num2
    print(num1, "+", num2, "=", hap)

print("0을 입력해서 계산을 종료합니다.")
"""
"""

i, hap = 0, 0

for i in range(1,101,1):
    if i % 4 == 0 :
        continue #4의 배수일때 for문으로 이동하고 4를 안씀

    hap += i
print("1~100의 합계(4의 배수 제외) : ", hap)
"""
"""
for i in range(5):
    for j in range(5):
        if j == 2:
            break #2가 되면 반복문 탈출
        print("i:", i, ", j:", j)

for i in range(5):
    for j in range(5):
        if j == 2:
            continue #2일때 반복문으로 돌아감
        print("i:", i, ", j:", j)
"""

#주사위 3개를 동시에 던져 동일한 숫자 나오기
"""
import random as r
n = 0
d = 0

while True:
    d = int(input("시뮬레이션 할 횟수 : "))
    for i in range(1, d+1, 1):
        while True:
            d1 = r.randint(1,6)
            d2 = r.randint(1,6)
            d3 = r.randint(1,6)
            n += 1
            if d1 == d2 == d3:
                break
        print("3개의 주사위는 모두", d1, "입니다.")
        print("같은 숫자가 나오기까지", n, "번 던졌습니다.")
        n = 0
    if d == 0:
        break
print("시뮬레이션을 종료합니다.")
"""

#컴퓨터와 인간의 숫자 맞히기 대결
"""
import random as r

comNum, youNum = 0, 0
cnt = 0

while True:
    comNum = r.randint(1,5)
    youNum = int(input("게임 " + str(cnt+1) + "회 :컴퓨터가 생각한 숫자는? ")) #input 안에는 ,가 아닌 +로 문자를 이을 것.
    if youNum == comNum :
        print("맞혔네요. 축하합니다!")
        break
    else :
        print("아까워요.", comNum, "였는데요. 다시 생각해보세요. ㅠ")
print("게임을 마칩니다.")
"""






























