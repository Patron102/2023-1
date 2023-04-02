#가위 바위 보 만들기
"""
import random
score = 0

while True :
    print("=" * 50)
    print("나의 점수는 : ", score)
    myHand = input("나의 가위/바위/보 ==> ")

    comHand = random.choice(["가위", "바위", "보"])
    print("컴퓨터의 가위/바위/보 ==> ", comHand)

    if myHand == comHand :
        print("비겼습니다.")

    if myHand == "가위" :
        if comHand == "바위" :
            print("졌습니다.")
            score -= 1
        else :
            print("이겼습니다.")
            score += 1

    if myHand == "바위" :
        if comHand == "가위" :
            print("이겼습니다.")
            score += 1
        else :
            print("졌습니다.")
            score -= 1

    if myHand == "보" :
        if comHand == "가위" :
            print("졌습니다.")
            score -= 1
        else :
            print("이겼습니다.")
            score += 1
    print("=" * 50)
if score <= -3 :
    print("총체적 패배")
    done

if score >= 3 :
    print("총체적 승리")
    done
"""
#반복문2
"""
for i in range(0, 3, 1):
    print(i)
for i in range(3):
    print(i)
for i in ["a", "b", "c"]:
    print(i)
for abcd in ["a", "b", "c"]:
    print("-------------")
    print(abcd)
    print(i)
"""
#슈도코드
"""
hap 선언

for 변수 i가 1을 시작으로 10까지 1씩 증가:
    hap 값에 i 값을 더해 줌

hap의 값을 출력

hap = 0

for i in range(1, 11, 1) :
    hap += i

print(hap)
"""
#for문을 활용한 합계 구하기
"""
hap = 0

for i in range(1, 11, 1):
    hap += i
    if i < 10 :
        print(i, "+ ", end='')
    else :
        print(i, "= ", end='')

print(hap)
"""
#학생 줄 세우기(팩토리얼 계산하기)
"""
d0 = 1

for i in range(1, 6, 1):
    d0 *= i

print("A, B, C, D, E 학생들을 순서대로 세우는 경우의 수 : ", d0)
"""
#for문을 활용한 합계 구하기2
"""
hap = 0

for i in range(1001, 2001, 2):
    hap += i

print("1000에서 2000까지의 홀수의 합 : ", hap)
"""











































