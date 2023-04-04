numList_x = []
numList_y = []
n = 0
rn = 0

x = int(input("시뮬레이션 할 x의 길이 : "))
y = int(input("시뮬레이션 할 y의 길이 : "))

while True :
    for j in range(1, x+1, 1):
        numList_x.append(j)

    if len(numList_x) > x:
        del(numList_x[x:])
        if len(numList_y) > 0:
            rn += 1
            for l in range(rn):
                first = numList_x[0]
                numList_x.append(first)
                del(numList_x[0])
                n += 1
        n = 0
        numList_y.append(numList_x)
        numList_x = []
        continue

    if len(numList_y) > y-1:
        break

for i in range(len(numList_y)) :
    for k in range(len(numList_y[i])) :
        print(" ", numList_y[i][k], end='')
    print("")
