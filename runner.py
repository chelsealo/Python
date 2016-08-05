import random
import pygame

from city_scroller import Scroller

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
SKYBLUE = (204, 255, 255)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
	return random.choice(colors)

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FRONT_SCROLLER_COLOR = (141,138,138)
MIDDLE_SCROLLER_COLOR = (186,182,182)
BACK_SCROLLER_COLOR = (226,226,226)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 400, (SCREEN_HEIGHT- 200), FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 250), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 300), BACK_SCROLLER_COLOR, 1)


pygame.display.set_caption("CityScroller")

speed = 3

class Road(object):
	def __init__(self, color, x_point, y_point, width, height):
		self.color = color
		self.x_point = x_point
		self.y_point = y_point
		self.width = width
		self.height = height
		
	def draw(self):
		pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

class RunnerSprite(pygame.sprite.Sprite):
	def __init__(self, color, size, x_loc, y_loc, speed):
		super().__init__()
		self.image = pygame.Surface((50,50))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.x_loc = x_loc
		self.y_loc = y_loc
		#self.speed = x_loc - speed
		#self.color = color
		#self.width = width
		#self.height = height
		self.image = pygame.image.load("capunderpants.png")
		
class BadSprite(pygame.sprite.Sprite):
	def __init__(self, color, size, x_loc, y_loc, speed):
		super().__init__()
		self.image = pygame.Surface((1000,50))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x_loc
		self.rect.y = y_loc
		#self.speed = x_loc - speed
		self.image = pygame.image.load("capblunderpants.png")
	
	def update(self):
		self.rect.x -= 5

class MovingBadGuy():
	def __init__(self, width, height, base, color, speed):
		self.width  = width
		self.height = height
		self.base = base
		self.color = color
		self.speed = speed
		self.blunder_list = []
#       self.add_buildings()

	def movebadguys (self):
		for k in self.blunder_list:
			blunder_list.add(badguy)
			blunderpants.move(self.speed)




player1 = RunnerSprite(RED, 50, 200, 600,0)
badguy = BadSprite(RED, 1080, 200, 600, 3)

badguy_list = pygame.sprite.Group()



all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player1)
badguy_list.add(badguy)

road = Road(BLACK, 0, 600, 1080, 200)


done = False

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
		
	#pos = pygame.mouse.get_pos()
	#player1.rect.x = pos[0]
	#player1.rect.y = pos[1]
	
	player1.rect.x = 150
	player1.rect.y = 550
	
# 	badguy.rect.x = 700
# 	badguy.rect.y = 550

	screen.fill(SKYBLUE)
	
	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()
	road.draw()
	all_sprites_list.draw(screen)
	badguy_list.draw(screen)
	badguy_list.update()

	for j in all_sprites_list:
		screen.blit(j.image, j.rect)
		
	for i in badguy_list:
		screen.blit(i.image, i.rect)


	pygame.display.flip()

	clock.tick(60)

pygame.quit()
exit() 
