#연산자2
"""
score = int(input("필기 시험점수를 입력하세요 ==>"))
print(score >= 70)
"""

#기말 평균 학점 구하기
"""
py = 3
mo = 2
ex = 1

B = 3.5
A0 = 4.0
A = 4.5

avg = (py*B + mo*A0 + ex*A) / (py+mo+ex)
print("평균학점 : %.2f" %avg)
"""
#반복문 while
"""
d=0
while True:
    d += 1
    print("SCV가",d,"번째 미네랄을 채취했습니다.")
"""

#거북이를 그리는 펜의 변화
"""
import turtle

turtle.shape('turtle')

turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.forward(50)

turtle.pensize(5)
turtle.pencolor("red")
turtle.right(90)
turtle.forward(100)
"""

#입력한 값만큼 거북이 움직이기
"""
import turtle
turtle.shape('turtle')
turtle.pensize(5)
turtle.pencolor("blue")

while True:
    ang = int(input("거북이의 회전 각도 :"))
    dis = int(input("거북이의 이동 거리 :"))
    turtle.right(ang)
    turtle.forward(dis)
"""

#You spin round round round round round
"""
import turtle
turtle.shape("turtle")
turtle.pensize(200)

while True:
    turtle.pencolor("red")
    turtle.right(15)
    turtle.forward(20)
    turtle.pencolor("orange")
    turtle.right(15)
    turtle.forward(20)
    turtle.pencolor("yellow")
    turtle.right(15)
    turtle.forward(20)
    turtle.pencolor("green")
    turtle.right(15)
    turtle.forward(20)
    turtle.pencolor("blue")
    turtle.right(15)
    turtle.forward(20)
"""

#stop
while False :












