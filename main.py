#2023.03.23.뻘짓
"""
import random as r
n = 0
d = 0

result = list()

while True:
    d = int(input("시뮬레이션 할 횟수 : "))
    for i in range(1, d+1, 1):
        while True:
            d1 = r.randint(1,6)
            d2 = r.randint(1,6)
            d3 = r.randint(1,6)
            n += 1
            if d1 == d2 == d3:
                result.append(n)
                break
        print("3개의 주사위는 모두", d1, "입니다.")
        print("같은 숫자가 나오기까지", n, "번 던졌습니다.")
        n = 0
    if d == 0:
        break
m = max(result)
print("가장 많이 던진 횟수 : ", m)
print("시뮬레이션을 종료합니다.")
"""
#d2023.03.28. 뻘짓2
"""
while True:
    mid = int(input("중간고사 성적 입력 : "))
    if mid > 100 or mid < 0:
        print("다시 입력해주세요")
        continue

    fin = int(input("기말고사 성적 입력 : "))
    if fin > 100 or fin < 0:
        print("다시 입력해주세요")
        continue

    tot = mid + fin
    tot_str = str(tot)
    tot_1 = int(tot_str[-1])
    ave = tot / 2

    print(mid, fin)
    print("합계 =", tot)
    print("평균 =", '%.1f' % ave)

    if tot_1 == 1 or tot_1 == 2:
        print("1반")
    if tot_1 == 3 or tot_1 == 4:
        print("2반")
    if tot_1 == 5 or tot_1 == 6:
        print("3반")
    if tot_1 == 7 or tot_1 == 8:
        print("4반")
    if tot_1 == 9 or tot_1 == 0:
        print("5반")
"""
#2023.