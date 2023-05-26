#pygame
import pygame as p

#거북이 게임 만들기
import random as r
import sys

monitor = None
colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"]

p.init()
monitor = p.display.set_mode((500, 700))
'''
cnt = 0
while True:
	color = r.choice(colorList)
	monitor.fill(color)
	p.display.update()
	print('#', end='')
	cnt += 1
	if cnt == 1000000:
		break
'''
color = r.choice(colorList)
turtle = p.image.load('turtle.png')
tx, ty = 200, 300
leftFlag, rightFlag, upFlag, downFlag, spaceFlag = False, False, False, False, False
vel = 0.1
jumpCnt = 0

while True:
	monitor.fill(color)
	monitor.blit(turtle, (tx, ty))
	p.display.update()

	for e in p.event.get():
		if e.type in [p.QUIT]:
			p.quit()
			sys.exit()

		if e.type in [p.KEYDOWN]:
			if e.key == p.K_LEFT: leftFlag = True
			elif e.key == p.K_RIGHT: rightFlag = True
			elif e.key == p.K_UP: upFlag = True
			elif e.key == p.K_DOWN: downFlag = True
			elif e.key == p.K_SPACE: spaceFlag = True

		if e.type in [p.KEYUP]:
			if e.key == p.K_LEFT: leftFlag = False
			elif e.key == p.K_RIGHT: rightFlag = False
			elif e.key == p.K_UP: upFlag = False
			elif e.key == p.K_DOWN: downFlag = False
			elif e.key == p.K_SPACE:
				spaceFlag = False
				jumpCnt = 0

	if leftFlag : tx -= vel
	elif rightFlag : tx += vel
	elif upFlag : ty -= vel
	elif downFlag : ty += vel
	elif spaceFlag:
		