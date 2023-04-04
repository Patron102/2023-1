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
