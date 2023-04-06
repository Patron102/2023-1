#이아현 교수님1
x = 20
y = 10

def printList(a, i):
    for _ in range(len(a)):
        print(a[i], end = " ")

        i += 1 
        if i >= len(a):
            i = 0


xList = [i for i in range(1, x+1, 1)]
idx = 0

for i in range(y):
    printList(xList, idx)
    idx += 1
    if i != y-1:
        print("")


#이아현 교수님2
x = 20
y = 10

def printList(a, i):
	for _ in range(len(a)):
		print(a[i], end = " ")

		i += 1 
		if i >= len(a):
			i = 0


xList = [i for i in range(1, x+1, 1)]
idx = 0

for i in range(y):
	printList(xList, idx)
	idx += 1
	if i != y-1:
		print("")


#민서홍1
x = int(input("x : "))
y = int(input("y : "))

lx = list(range(x))

for dx in range(0, x, 1) :
    ly = []
    for dy in range(dx, y + dx, 1) :
        if (dy + 1 > y) :
            ly.append(dy + 1 - y)
        else :
            ly.append(dy + 1)
    lx[dx] = ly

for i in range(0, x, 1) :
    for j in range(0, y, 1) :
        print(lx[i][j], end=" ")
    print("")


#민서홍2
x = int(input("x : "))
y = int(input("y : "))

for dy in range(0, y, 1) :
    for dx in range(dy, x + dy, 1) :
        if (dx + 1 > x) :
            print(dx + 1 - x, end = " ")
        else :
            print(dx + 1,  end = " ")
    print("")
