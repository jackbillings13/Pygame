#required 
from pygame import *
from pygame.sprite import *
from random import *
import os

pygame.init();

WIDTH = 1260
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
logo_x = 15
logo_y = 15
logo2_x = 1275
logo2_y = 15

gamefont = font.Font(None, 25)

DELAY = 5000; 

class Buckeye(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('buckeye.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.velocity = randint(1, 3)
        randX = randint(130, 1270)
        randY = randint(10, 790)
        self.rect.center = (randX,randY)


    def reset(self):
    	self.velocity = randint(1, 2)
    	randX = randint(130, 1270)
    	randY = randint(10, 790)
    	self.rect.center = (randX,randY)
		scoretext = gamefont.render("Player Score: " + str(score), False, [215, 209, 39])
		gameDisplay.blit(scoretext, (565, 20))
    

    # move gold to a new random location
    # def move(self):
    # 	randX = randint(130, 1270)
    # 	randY = randint(10, 790)
    # 	self.rect.center = (randX,randY)
    	# self.rect.center = (randX - 10, randY - 10)
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
  		self.rect.center = (x_pos, y_pos)

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
		self.rect.center = (x_pos, y_pos)

	def hit(self, target):
		return self.rect.colliderect(target)

# class Touchdown(Sprite):
# 	def __init__(self):
# 		Sprite.__init__(self)
# 		self.image = image.load('logo2.png').convert()
# 		self.rect = self.image.get_rect()
# 		self.rect.center = (1330, 395)


#create a surface
gameDisplay = pygame.display.set_mode((1400,800)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Football")

# def redraw():
# 	gameDisplay.fill(white)

pygame.display.update()		#only updates portion specified

pygame.mixer.music.load("crowd.wav")
pygame.mixer.music.play(-1, 0.0)

score = 0
down = 0


bg = pygame.image.load(os.path.join('footballfield.png'))
# harbaugh = pygame.image.load(os.path.join('harbaugh.png'))
logo = pygame.image.load(os.path.join('logo.png'))
logo2 = pygame.image.load(os.path.join('logo2.png'))

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
# t = Touchdown()
harbaugh = Player()


sprites = RenderPlain(b, b2, b3, b4, b5, b6, b7, b8, b9, b10, harbaugh)


time.set_timer(USEREVENT + 1, DELAY)


gameExit = False
while not gameExit:
	# redraw()
	e = event.poll()
	# for event in pygame.event.get():
	if e.type == QUIT:
		gameExit = True

	#if e.type == USEREVENT + 1:
		# position1 = b.pos()
		# b.move(position1)
		# b.move()
		# b2.move()
		# b3.move()
		# b4.move()
		# b5.move()
		# b6.move()
		# b7.move()
		# b8.move()
		# b9.move()
		# b10.move()

	if harbaugh.hit(b):
		x_pos = 0
		down+=1
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()			
		
	if harbaugh.hit(b2):
		down+=1
		x_pos = 0
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	

	if harbaugh.hit(b3):
		down+=1
		x_pos = 0
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	

	if harbaugh.hit(b4):
		down+=1
		x_pos = 0
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	

	if harbaugh.hit(b5):
		x_pos = 0
		down+=1
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	
		
	if harbaugh.hit(b6):
		down+=1
		x_pos = 0
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	

	if harbaugh.hit(b7):
		down+=1
		x_pos = 0
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	

	if harbaugh.hit(b8):
		down+=1
		x_pos = 0
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	

	if harbaugh.hit(b9):
		down+=1
		x_pos = 0
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	

	if harbaugh.hit(b10):
		down+=1
		x_pos = 0
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	


	if e.type == pygame.KEYDOWN:
		harbaugh.move()

	if x_pos >= 1300:
		x_pos = 0
		pygame.mixer.music.load("michigan_fight_song.wav")
		pygame.mixer.music.play(-1, 0.0)
		score+=7
		down = 0
		time.set_timer(USEREVENT + 1, DELAY)
		b.reset()
		b2.reset()
		b3.reset()
		b4.reset()
		b5.reset()
		b6.reset()
		b8.reset()
		b9.reset()
		b10.reset()	

	gameDisplay.blit(bg, (bg_x, bg_y))

	scoretext = gamefont.render("Player Score: " + str(score), False, [215, 209, 39])
	gameDisplay.blit(scoretext, (565, 20))

	downtext = gamefont.render("Down: " + str(down), False, [215, 209, 39])
	gameDisplay.blit(downtext, (715, 20))

	gameDisplay.blit(logo, (logo_x,logo_y))
	gameDisplay.blit(logo2, (logo2_x,logo2_y))

	# gameDisplay.blit(buckeye, (x,y))
	# gameDisplay.blit(buckeye, (x,y))
	# gameDisplay.blit(buckeye, (x2,y2))
	# gameDisplay.blit(buckeye, (x3,y3))
	# gameDisplay.blit(buckeye, (x4,y4))
	# gameDisplay.blit(buckeye, (x5,y5))
	# gameDisplay.blit(buckeye, (x6,y6))
	# gameDisplay.blit(buckeye, (x7,y7))
	# gameDisplay.blit(buckeye, (x8,y8))
	# gameDisplay.blit(buckeye, (x9,y9))
	# gameDisplay.blit(buckeye, (x10,y10))
	# gameDisplay.blit(buckeye, (x11,y11))
	# gameDisplay.blit(buckeye, (x12,y12))

	# gameDisplay.blit(harbaugh, (x_pos,y_pos))
                
		# if e.type == pygame.KEYDOWN:

	# if x_pos>=WIDTH:
	# 	x_pos = 1259
	# 	pygame.mixer.music.load("michigan_fight_song.wav")
	# 	pygame.mixer.music.play(-1, 0.0)


	sprites.update()
	sprites.draw(gameDisplay)
	display.update()		




#required
pygame.quit()
quit()				#exits python
