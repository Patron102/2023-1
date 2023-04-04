#11. 리스트에서 짝수인 값은 10배인 값으로 변경
for i in range(0, len(numList), 1):
    if numList[i] % 2 == 0:
        numList[i] *= 10

print("11:", numList, "\n")    

#12. 2차원 리스트 변수를 생성. 4x10 행렬 형태

numMat = [[0 for c in range(10)] for r in range(4)]
#print(numMat)

idx = 0

for r in range(4):
    for c in range(10):
        idx = 10 * r + c        
        numMat[r][c] = numList[idx]

print("12:", numMat, "\n")

#13. 2차원 리스트에서 1행의 값을 1차원 리스트로 복사
numList = numMat[0].copy()
print("13:", numList, "\n")

#14. 1차원 리스트 변수에서 총합을 가장 마지막 위치에 저장
hap = 0
for i in numList:
    hap += i

numList[-1] = hap
print("14:", numList, "\n")

#15. 리스트의 길이가 1이 될때까지 pop()을 실행하고, pop()의 리턴의 총 합을 출력
hap = 0
while len(numList) > 1:
    hap += numList.pop()

print(f"15: 총합({hap}), 남은 리스트:({numList})", "\n")
