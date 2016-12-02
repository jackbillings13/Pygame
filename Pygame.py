#required 
from pygame import *
from pygame.sprite import *
from random import *
import os

pygame.init();


#position vars
x_pos = 50
y_pos = 400
bg_x = 0
bg_y = 0
logo_x = 15
logo_y = 15
logo2_x = 1275
logo2_y = 15
scoreX = 460
scoreY = 0

gamefont = font.Font(None, 25)
gamefont2 = font.Font(None, 100)

DELAY = 5000; 

class Buckeye(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('buckeye.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.velocity = randint(1, 3)
        randX = randint(200, 1400)
        randY = randint(30, 790)
        self.rect.center = (randX,randY)


    def reset(self):
    	self.velocity = randint(1, 3)
    	randX = randint(200, 1400)
    	randY = randint(30, 790)
    	self.rect.center = (randX,randY)
    	pygame.mixer.music.load("michigan_fight_song.wav")
    	pygame.mixer.music.play(-1, 0.0)

    def update(self):
    	x, y = self.rect.center
    	x, y = x - self.velocity, y
    	if x <= 0:
    		self.rect.center = 1400, y
    	else:
    		self.rect.center = x, y


class Player(Sprite):
	def __init__(self):
  		Sprite.__init__(self)
  		self.image = image.load('harbaugh.png').convert_alpha()
  		self.rect = self.image.get_rect()
  		self.rect.center = (50, 400)

	def move(self):
		global x_pos
		global y_pos
		if e.key == pygame.K_LEFT:
			x_pos -= 20
		if e.key == pygame.K_RIGHT:
			x_pos += 20
		if e.key == pygame.K_UP:
			y_pos -= 20
		if e.key == pygame.K_DOWN:
			y_pos += 20
		if y_pos <= 50:
			y_pos = 50
		if y_pos >= 750:
			y_pos = 750
		if x_pos <= 25:
			x_pos = 25
		if x_pos >= 1375:
			x_pos = 1375
		self.rect.center = (x_pos, y_pos)

	def reset(self):
		global x_pos
		global y_pos
		x_pos = 50
		y_pos = 400
		self.rect.center = (x_pos, y_pos)


#create a surface
gameDisplay = pygame.display.set_mode((1400,800)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Football")

pygame.display.update()		#only updates portion specified

pygame.mixer.music.load("michigan_fight_song.wav")
pygame.mixer.music.play(-1, 0.0)

score = 0
oppscore = 0
down = 0


bg = pygame.image.load(os.path.join('footballfield.png'))
logo = pygame.image.load(os.path.join('logo.png'))
logo2 = pygame.image.load(os.path.join('logo2.png'))
scoreb = pygame.image.load(os.path.join('scoreb.png'))

b = Buckeye()
b2 = Buckeye()
b3 = Buckeye()
b4 = Buckeye()
b5 = Buckeye()
b6 = Buckeye()
b7 = Buckeye()
b8 = Buckeye()
b9 = Buckeye()
b10 = Buckeye()
b11 = Buckeye()
b12 = Buckeye()
b13 = Buckeye()
b14 = Buckeye()
b15 = Buckeye()
b16 = Buckeye()
b17 = Buckeye()
b18 = Buckeye()
b19 = Buckeye()
b20 = Buckeye()
b21 = Buckeye()
b22 = Buckeye()
b23 = Buckeye()
b24 = Buckeye()
b25 = Buckeye()
b26 = Buckeye()
b27 = Buckeye()
b28 = Buckeye()
b29 = Buckeye()
b30 = Buckeye()
bucks = pygame.sprite.Group()
bucks.add(b, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30)
harbaugh = Player()


sprites = RenderPlain(harbaugh, b, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30)


gameExit = False
while not gameExit:
	e = event.poll()

	if len(pygame.sprite.spritecollide(harbaugh, bucks, False)) > 0:
		harbaugh.reset()
		down+=1
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b7.reset()
		b8.reset()
		b9.reset()
		b10.reset()
		b11.reset()
		b12.reset()
		b13.reset()
		b14.reset()
		b15.reset()
		b16.reset()
		b17.reset()
		b18.reset()
		b19.reset()
		b20.reset()
		b21.reset()
		b22.reset()
		b23.reset()
		b24.reset()
		b25.reset()
		b26.reset()
		b27.reset()
		b28.reset()
		b29.reset()
		b30.reset()


	if e.type == pygame.KEYDOWN:
		harbaugh.move()

	if x_pos >= 1300:
		harbaugh.reset()
		score+=7
		r = choice([0,7])
		down = 0
		oppscore+=r		
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b7.reset()
		b8.reset()
		b9.reset()
		b10.reset()	
		b11.reset()
		b12.reset()
		b13.reset()
		b14.reset()
		b15.reset()
		b16.reset()
		b17.reset()
		b18.reset()
		b19.reset()
		b20.reset()
		b21.reset()
		b22.reset()
		b23.reset()
		b24.reset()
		b25.reset()
		b26.reset()
		b27.reset()
		b28.reset()
		b29.reset()
		b30.reset()

	if down == 4:
		r = choice([0,7])
		down = 0
		oppscore+=r

	gameDisplay.blit(bg, (bg_x, bg_y))
	gameDisplay.blit(scoreb, (scoreX,scoreY))
	scoretext = gamefont.render("UM Score: " + str(score), False, [215, 209, 39])
	gameDisplay.blit(scoretext, (500, 0))

	oppscoretext = gamefont.render("OSU Score: " + str(oppscore), False, [215, 209, 39])
	gameDisplay.blit(oppscoretext, (650, 0))	

	downtext = gamefont.render("Down: " + str(down), False, [215, 209, 39])
	gameDisplay.blit(downtext, (800, 0))

	gameDisplay.blit(logo, (logo_x,logo_y))
	gameDisplay.blit(logo2, (logo2_x,logo2_y))

	if score == 28:
		win = gamefont2.render("You Win!", False, [0, 0, 0])
		gameDisplay.blit(win, (550, 400))
		display.update()	
		pygame.time.wait(DELAY)
		gameExit = True
		break

	if oppscore == 28:
		if score != 28:
			lose = gamefont2.render("You Lose :(", False, [0, 0, 0])
			gameDisplay.blit(lose, (500, 400))
			display.update()	
			pygame.time.wait(DELAY)
			gameExit = True
			break

	if x_pos >= 125:
		sprites.update()
	sprites.draw(gameDisplay)
	display.update()		





#required
pygame.quit()
quit()				#exits python
