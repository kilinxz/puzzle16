import pygame
from pygame.locals import *
import sys
import random

SCREEN_SIZE = (222, 222)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("puzzle16")

Img = []
for i in range(16):
	Img.append(pygame.image.load("usagi" + str(i) + ".png").convert())

sysfont = pygame.font.SysFont(None, 80)
clear = sysfont.render("CLEAR!", False, (255, 0, 0))

position = []
now = []
c = 0
for j in range(4):
	for i in range(4):
		masu = [(i*51+10, j*51+10), Img[c]]
		position.append(masu)
		now.append(c)
		c += 1
		

def field():
	for k in range(16):
		screen.blit(position[k][1], position[k][0])
	if now == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
		screen.blit(clear, (5, 80))
	

n = 15
def change(x):
	global n
	position[n][1] = position[x][1]
	now[n] = now[x]
	position[x][1] = Img[15]
	now[x] = 15
	n = x

def get_position(x, y):
	for i in range(16):
		if position[i][0][0] <= x and position[i][0][0] + 50 >= x and position[i][0][1] <= y and position[i][0][1] + 50 >= y:
			return i
			break
		
moveok = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5, 8], [1, 4, 6, 9], [2, 5, 7, 10], [3, 6, 11], [4, 9, 12], [5, 8, 10, 13], [6, 9, 11, 14], [7, 10, 15], [8, 13], [9, 12, 14], [10, 13, 15], [11, 14]]

def set():
	t = random.randint(0, len(moveok[n])-1)
	change(moveok[n][t])
for i in range(300):
	set()
while now[15] != 15:
	set()
	
while True:
	pygame.display.update()
	
	field()

	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			x, y = pygame.mouse.get_pos()
			p = get_position(x, y)
			if p in moveok[n]:
				change(p)