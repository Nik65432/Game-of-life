import pygame
import sys
from time import sleep

pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.set_caption("Game of life")

class Cube():
	def __init__(self,x,y,live):
		self.x = x
		self.y = y
		self.live = live
	def draw_cube(self):
		if self.live == True:
			pygame.draw.rect(screen,'gray',pygame.Rect(self.x*20,self.y*20,20,20),2)
			pygame.draw.rect(screen,'white',pygame.Rect(self.x*20+1,self.y*20+1,18,18))
		else:
			pygame.draw.rect(screen,'gray',pygame.Rect(self.x*20,self.y*20,20,20))
cubes = {}

def around(c,border=False):
	count = 0
	around_list = [
	(c.x-1,c.y-1),
	(c.x-1,c.y),
	(c.x-1,c.y+1),
	(c.x+1,c.y-1),
	(c.x+1,c.y),
	(c.x+1,c.y+1),
	(c.x,c.y-1),
	(c.x,c.y+1),
	]
	for i in around_list:
		if border:
			if cubes.get(i,False) == False:
				cubes[i] = Cube(i[0],i[1],False)
				cubes[i].draw_cube()
		elif (cubes.get(i,False) != False) and cubes[i].live:
			count += 1
	return count

def cicle():
	sleep(0.1)
	for i in cubes.values():
		status = around(i)
		print(status)
		if ((status <= 1) or (status >= 4)) and i.live:
			i.live = False
			i.draw_cube()
		elif (status == 3) and (i.live == False):
			i.live = True
			i.draw_cube()
	cube = cubes.copy()
	for j in cube.values():
		if j.live:
			around(j,True)


pause = True
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x = int(pygame.mouse.get_pos()[0]//20)
			y = int(pygame.mouse.get_pos()[1]//20)
			p = (x,y)
			if event.button == 1:
				if cubes.get(p,False) and cubes[p].live:
					cubes[p].live = False
					cubes[p].draw_cube()
				elif cubes.get(p,False) and cubes[p].live == False:
					cubes[p].live = True
					cubes[p].draw_cube()
					around(cubes[p],True)
				elif cubes.get(p,False) == False:
					cubes[p] = Cube(x,y,True)
					cubes[p].draw_cube()
					around(cubes[p],True)
			elif event.button == 3:
				if pause:
					pause = False
				else:
					pause = True
	if pause == False:
		cicle()

	pygame.display.update()