import random
import pygame

from city_scroller import Scroller

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
	return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)


HERO = RunnerSprite(SCREEN_WIDTH, 50, SCREEN_HEIGHT, 50, HERO_SPRITE, 3)
#ENEMY_


class RunnerSprite(pygame.sprite.Sprite):
	def __init__(self, color, size):
		#pygame.sprite.Sprite.__init__(self)
		super().__init__()
		#self.color = color
		#self.size = size
		#self.speed = speed
		self.image = pygame.Surface((50,50))
		self.image.fill(color)
		self.rect = self.image.get_rect()
	
	#def move_sprite(self):
		 #for sprite in self.all_sprites_list:
		 	#sprite.move(self.speed)


HERO_SPRITE = RunnerSprite(GREY, 30)


all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(HERO_SPRITE)

done=False
clock = pygame.time.Clock()

while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pos = pygame.mouse.get_pos()
	HERO_SPRITE.rect.x = pos [0]
	HERO_SPRITE.rect.y = pos [1]
	
	screen.fill(BACKGROUND_COLOR)
	#HERO_SPRITE.draw_sprite()
	#ENEMY_SPRITE.draw_sprite()
	#HERO_SPRITE.move_sprite()
	#ENEMY_SPRITE.move_sprite()
	
	back_scroller.draw_buildings(screen)
	back_scroller.move_buildings()
	middle_scroller.draw_buildings(screen)
	middle_scroller.move_buildings()
	front_scroller.draw_buildings(screen)
	front_scroller.move_buildings()
	all_sprites_list.draw(screen)
	

 # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit()