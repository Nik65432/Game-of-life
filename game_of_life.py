import pygame
import sys
from time import sleep

pygame.init()
width = 500
hight = 500
prop = 10
screen = pygame.display.set_mode((width,hight))
screen.fill((0,0,0))
pygame.display.set_caption("Game of life")

class Cube():
	def __init__(self,x,y,live):
		self.x = x
		self.y = y
		self.live = live
	def draw_cube(self):
		if self.live == True:
			pygame.draw.rect(screen,'gray',pygame.Rect(self.x*prop,self.y*prop,prop,prop),2)
			pygame.draw.rect(screen,'white',pygame.Rect(self.x*prop+1,self.y*prop+1,prop-2,prop-2))
		else:
			pygame.draw.rect(screen,'black',pygame.Rect(self.x*prop,self.y*prop,prop,prop))

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
	cube = {}
	for k,v in cubes.items():
		status = around(v)
		if ((status <= 1) or (status >= 4)) and v.live:
			cube[k] = False
		elif (status == 3) and (v.live == False):
			cube[k] = True
	for k,v in cube.items():
		if v:
			around(cubes[k],True)
		cubes[k].live = v
	for i in cubes.values():
		i.draw_cube()

pause = True
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x = int(pygame.mouse.get_pos()[0]//prop)
			y = int(pygame.mouse.get_pos()[1]//prop)
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