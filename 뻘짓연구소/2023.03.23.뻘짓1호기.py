import random as r
n = 0
d = 0

result = []

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
        del(result)
        print("시뮬레이션을 종료합니다")
        break

m = max(result)
print("가장 많이 던진 횟수 : ", m)
print("시뮬레이션을 종료합니다.")
