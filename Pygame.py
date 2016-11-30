#How to simulate animation

#required 
import pygame
import random
import os
pygame.init();

WIDTH = 500
HEIGHT = 800
#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#position vars
x_pos = 100
y_pos = 200
bg_x = 0
bg_y = 0
logo_x = 0
logo_y = 0
logo2_x = 560
logo2_y = 0


#create a surface
gameDisplay = pygame.display.set_mode((560,700)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Football")

def redraw():
	gameDisplay.fill(white)

pygame.display.update()		#only updates portion specified

bg = pygame.image.load(os.path.join('footballfield.png'))
harbaugh = pygame.image.load(os.path.join('harbaugh.png'))
logo = pygame.image.load(os.path.join('logo.png'))
logo2 = pygame.image.load(os.path.join('logo2.png'))
buckeye = pygame.image.load(os.path.join('buckeye.png'))
x = random.randrange(100, 560)
y = random.randrange(0, 700)
x2 = random.randrange(100, 560)
y2 = random.randrange(0, 700)
x3 = random.randrange(100, 560)
y3 = random.randrange(0, 700)
x4 = random.randrange(100, 560)
y4 = random.randrange(0, 700)
x5 = random.randrange(100, 560)
y5 = random.randrange(0, 700)
x6 = random.randrange(100, 560)
y6 = random.randrange(0, 700)
x7 = random.randrange(100, 560)
y7 = random.randrange(0, 700)
x8 = random.randrange(100, 560)
y8 = random.randrange(0, 700)
x9 = random.randrange(100, 560)
y9 = random.randrange(0, 700)
x10 = random.randrange(100, 560)
y10 = random.randrange(0, 700)
x11 = random.randrange(100, 560)
y11 = random.randrange(0, 700)
x12 = random.randrange(100, 560)
y12 = random.randrange(0, 700)



gameExit = False
while not gameExit:
	redraw()
	timer = pygame.time.get_ticks()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_pos -= 10
		if event.key == pygame.K_RIGHT:
			x_pos += 10
		if event.key == pygame.K_UP:
			y_pos -= 10
		if event.key == pygame.K_DOWN:
			y_pos += 10


	gameDisplay.blit(bg, (bg_x, bg_y))
	gameDisplay.blit(logo, (logo_x,logo_y))
	gameDisplay.blit(logo2, (logo2_x,logo2_y))
	gameDisplay.blit(buckeye, (x,y))
	gameDisplay.blit(buckeye, (x2,y2))
	gameDisplay.blit(buckeye, (x3,y3))
	gameDisplay.blit(buckeye, (x4,y4))
	gameDisplay.blit(buckeye, (x5,y5))
	gameDisplay.blit(buckeye, (x6,y6))
	gameDisplay.blit(buckeye, (x7,y7))
	gameDisplay.blit(buckeye, (x8,y8))
	gameDisplay.blit(buckeye, (x9,y9))
	gameDisplay.blit(buckeye, (x10,y10))
	gameDisplay.blit(buckeye, (x11,y11))
	gameDisplay.blit(buckeye, (x12,y12))
	gameDisplay.blit(harbaugh, (x_pos,y_pos))
                


	if x_pos>=WIDTH:
		x_pos = 0
		if bg_x == 0:
			bg_x -=560
			logo_x = -200
			logo2_x = 460
		else:
			bg_x = 0
	pygame.display.update()		




#required
pygame.quit()
quit()				#exits python
