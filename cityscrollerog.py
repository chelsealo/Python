
import pygame
import random

# Define some colors
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


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
	def __init__(self, x_point, y_point, width, height, color):
		self.x_point = x_point
		self.y_point = y_point
		self.width = width
		self.height = height
		self.color = color

	def draw(self):
		pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

	def move(self, speed):
		self.x_point -= speed
        


class Scroller(object):
	def __init__(self, width, height, base, color, speed):
		self.width = width
		self.height = height
		self.base = base
		self.color = color
		self.speed = speed
		self.building_list = []
		self.add_buildings()
		

	def add_buildings(self):
		current_width = 0
		while current_width <= self.width:
			build = current_width
			self.add_building(build)
			current_width += self.building_list[-1].width
        
	def add_building(self, x_location):
		max_height = self.base - self.height
		building_height = random.randint ((max_height // 4), (max_height - 1))
		building_width = random.randint(25, 100)
		y_location = self.base - building_height 
		self.building_list.append(Building(x_location, y_location, self.width, building_height, self.color))

	def draw_buildings(self):
		for i in self.building_list:
			i.draw()
			
		
	def move_buildings(self):
		for j in self.building_list:
			j.move(self.speed)
			lastbuildwidth = self.building_list[-1].width
			lastbuild = lastbuildwidth + self.building_list[-1].x_point
			print(lastbuild)
			self.add_building(lastbuild)


FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 400, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here

	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()


    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
