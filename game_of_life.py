import pygame
import sys
from time import sleep

pygame.init()
width = 500
hight = 500
prop = 10
screen = pygame.display.set_mode((width,hight),pygame.RESIZABLE)
screen.fill((0,0,0))
pygame.display.set_caption("Game of life")

class Cell():
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

cells = {}

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
			if cells.get(i,False) == False:
				cells[i] = Cell(i[0],i[1],False)
				cells[i].draw_cube()
		elif (cells.get(i,False) != False) and cells[i].live:
			count += 1
	return count

def cicle():
	sleep(0.1)
	Cell = {}
	for k,v in cells.items():
		status = around(v)
		if ((status <= 1) or (status >= 4)) and v.live:
			Cell[k] = False
		elif (status == 3) and (v.live == False):
			Cell[k] = True
	for k,v in Cell.items():
		if v:
			around(cells[k],True)
		cells[k].live = v
	for i in cells.values():
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
				if cells.get(p,False) and cells[p].live:
					cells[p].live = False
					cells[p].draw_cube()
				elif cells.get(p,False) and cells[p].live == False:
					cells[p].live = True
					cells[p].draw_cube()
					around(cells[p],True)
				elif cells.get(p,False) == False:
					cells[p] = Cell(x,y,True)
					cells[p].draw_cube()
					around(cells[p],True)
			elif event.button == 3:
				if pause:
					pause = False
				else:
					pause = True
	if pause == False:
		cicle()
	pygame.display.update()