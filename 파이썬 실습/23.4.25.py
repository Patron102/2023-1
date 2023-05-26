#파일 읽기, 쓰기
'''
one = open("1.txt", "r", encoding="UTF-8")
#one = open("C:/Users/ASUS/Desktop/파이썬 실습/1.txt", "r", encoding="UTF-8")


oneStr = one.readline()
print("-" + oneStr)

oneStr = one.readline()
print("-" + oneStr)

oneStr = one.readline()
print("-" + oneStr)

oneStr = one.readline()
print("-" + oneStr)

oneStr = one.readline()
print("-" + oneStr)

oneStr = one.readline()
print("-" + oneStr)
'''
'''
while True:
	oneStr = one.readline()
	if oneStr == '':
		break
	print(oneStr, end='')
'''
'''
oneStrs = one.readlines()
print(oneStrs)

for i in oneStrs:
	print(i, end='')

one.close()
'''

#텍스트 출력
'''
kia = open("C:/Users/ASUS/Desktop/파이썬 실습/kia.txt", "r", encoding="UTF-8")

kiaStrs = kia.readlines()

for i in range(len(kiaStrs)):
	print(f"{i+1} : {kiaStrs[i]}", end='')

kia.close()
'''

#파일 쓰기
one = open("C:/Users/ASUS/Desktop/파이썬 실습/1.txt", "w", encoding="UTF-8")
'''
one.writelines("ㅎㅇ\n")
one.writelines("ㅂㅇ")

one.close()
'''
#사용자에게 입력받은 	내용을 파일에 쓰기
filename = input("# 파일명 입력 : ")
one = open(f"C:/Users/ASUS/Desktop/파이썬 실습/{filename}.txt", "w", encoding="UTF-8")

while True:
	strs = input(": ")
	one.writelines(f"{strs}\n")
	if strs == '':
		break
one.close()
print(f"{filename}.txt 파일이 저장되었습니다!")