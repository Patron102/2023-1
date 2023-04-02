#실습1. 구구단 출력
"""
num = int(input("출력할 단수 입력 : "))

for i in range(1, 10, 1):
    print(num, "X", i, "=", num*i)
"""

#실습 2. 성적 등급 구분
"""
while True:
    s  = int(input("점수 입력(0~100) : "))
    if s >= 90:
        print("A")
    elif s >= 80:
        print("B")
    elif s >= 70:
        print("C")
    elif s >= 60:
        print("D")
    else :
        print("F")
"""

#실습 3. 입력된 숫자까지 모두 더하기
"""
while True:
    d1 = int(input("숫자 입력 : "))
    for i in range(1, d1, 1):
        d1 += i

    print(d1)
"""

#실습 4. 배수 출력
"""
d1 = int(input("input number : "))
d2 = int(input("배수 입력 : "))

for i in range(d2, d1+1, d2):
    print(i, end=',')
"""

#실습 5. 로또 추천 번호 출력
"""
import random

r1 = list(range(1, 46, 1))

for i in range(0, 10, 1):
    l = random.sample(r1, 6)
    print(l)
"""
