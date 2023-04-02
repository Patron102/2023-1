#1. 학번, 이름, 취미를 입력받아 출력하기
print("1. 학번, 이름, 취미를 입력받아 출력하기")

d1 = input("학번을 입력하세요 : ")
d2 = input("이름을 입력하세요 : ")
d3 = input("취미를 입력하세요 : ")

print("--------------------------------------------------")
print("           순천향학교 메탑버스&게임학과           ")
print("--------------------------------------------------")
print("1. 학번 : ", d1)
print("2. 이름 : ", d2)
print("3. 취미 : ", d3)

print()
print()


#2. 소수점 순차적으로 나오게 하기

print("2. 소수점 순차적으로 나오게 하기")

pi = 3.1415926535

print("-",'%d' %(pi))
print("-",'%.1f' %(pi))
print("-",'%.2f' %(pi))
print("-",'%.3f' %(pi))
print("-",'%.4f' %(pi))
print("-",'%.5f' %(pi))

print()
print()


#3. 택배를 ‘받는 사람’, ‘주소’, ‘무게’를 입력하고 택배의 무게를 입력
print("3. 택배를 ‘받는 사람’, ‘주소’, ‘무게’를 입력하고 택배의 무게를 입력")

d4 = input("받는 사람 : ")
d5 = input("주소 : ")
d6 = int(input("무게(g) : "))

print("** 받는 사람 ==> ", d4)
print("** 주소 ==> ", d5)
print("** 배송비 ==> ", d6*5, "원")


#4. 거북이로 자기만의 스카이라인을 그려보세요.
import turtle
turtle.shape('turtle')

turtle.left(90) 
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(50)











