#required 
import pygame
pygame.init();

bg = pygame.image.load(os.path.join('images', 'footballfield.png'))

gameExit = False
while not gameExit:
	redraw()
	if bg_x == 0:
		bg_x -=200
	else:
		bg_x = 0
	gameDisplay.blit(bg, (bg_x, bg_y))