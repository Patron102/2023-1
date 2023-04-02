#모험을 떠나는 거북이
"""
import turtle

turtle.shape("turtle")
turtle.penup()

for i in range(2): #while True: 혹은 for i in range(): 
    x = int(input("X위치==> "))
    y = int(input("Y위치==> "))
    text = input("쓰고 싶은 글자 ==> ")

    turtle.goto(x,y)
    turtle.write(text, font=("Arial", 30))

turtle.done()
"""
#random.randint()
"""
import random

for i in range(10):
    print(random.randint(0,100))
"""

#자유롭게 모험을 떠나는 거북이
"""
import random
import turtle

turtle.shape("turtle")
turtle.penup()

d = ["신나는 대학생활", "졸린 수업", "맛있는 음료"]

for i in range(10):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    n = random.randint(0, len(d)-1)

    turtle.goto(x,y)
    turtle.write(d[n], font=("Arial", 30))

turtle.done()
"""
#ififififififififiififif
"""
while True:
    num=int(input("넣을 숫자는? ==> "))

    if num <100 :
        print("100보다 작습니다.")
    
    else :
        print("100보다 큰데용")
"""
#if~else문
"""
while True :
    n=int(input("숫자를 입력 ==> "))
    
    if n%2==0:
        print("짝수입니다.")

    else :
        print("홀수입니다.")
"""
#중첩if문
"""
while True:
    n=int(input("숫자를 입력 ==> "))

    if n>100:
        if n<1000:
            print("100보다 크고 1000보다 작군요.")
        else :
            print("와~ 1000보다 크군요.")
    else :
        print("음~ 100보다 작군요,")
"""
#tip
"""
print(1,end='') #end=''는 출력을 안내리고 바로 옆에 붙여버림.
"""
#elif문
"""
while True:
    s  = int(input("점수를 입력 ==> "))
    if s >= 90:
        print("A", end='')
    elif s >= 80:
        print("B", end='')
    elif s >= 70:
        print("C", end='')
    elif s >= 60:
        print("D", end='')
    else :
        print("F", end='')
    print("학점입니다.")
"""





    
































































