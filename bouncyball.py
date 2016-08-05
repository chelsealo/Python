import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
colors=[RED, BLUE]

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

done = False

clock = pygame.time.Clock()
    
x = 350
y = 250
dx = 1
dy = 2
color=random.choice(colors)
size=30

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type== pygame.MOUSEBUTTONDOWN:
			mouse_location = pygame.mouse.get_pos()
			size=random.randint(20,100)
			x, y=mouse_location
			color=random.choice(colors)        
	x += dx
	y += dy
	if y<0 or y>SCREEN_HEIGHT - 40:
		dy *= -1
	if x<0 or x>SCREEN_WIDTH - 40:
		dx *= -1

	screen.fill(GREEN)
	pygame.draw.circle(screen, color, (x, y), size)

	pygame.display.flip()
	clock.tick(60)
	


pygame.exitonclick()
exit()