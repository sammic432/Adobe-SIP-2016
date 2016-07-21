"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc 
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
# colors = [BLACK, GREEN, BLUE, RED, WHITE, GREY]
colors = ["red", "green", "blue", "yellow"]
colors_length = len(colors)
random_index = random.randint(0, colors_length-1)
# print (colors[random_index])

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


    def __init__ (self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = random_color


    def draw(self):
        pygame.draw.rect (screen, BLUE, (self.x_point, self.y_point, self.width, self.height), 0)


    def move(self, speed):
        self.x_point += speed
        


class Scroller(object):


    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.list1 =[]


    def create_buildings(self):
        combined_width += building.width
        for building in self.list1:
            combined_width += building.width
        while self.combined_width < self.width:
            self.create_building(combined_width)


    def create_building(self, x_location):
        building_width = random.randint (10, 60)
        building_height = random.randint(80, 200)
        self.combined_width += width
        building1 = Building (0, random.randint(0, 600), building_width, building_height, random.choice(colors))

        self.list1.append (building1)


    def draw_buildings(self):
        # for each building in list1 draw it on the screen

        """
        This calls the draw method on each building.
        """


    def move_buildings(self):
        
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """


FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

# build = Building (0, random.randint (0, 600), random.randint (10,60), (600 - self.height), BLUE)


building_width = random.randint (10, 60)
building_y = random.randint (0,600)
build = Building (0, building_y, building_width, (600 - building_y), random_color)

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
    screen.fill(WHITE)

    # --- Drawing code should go here
    build.draw ()
    build.move (10)

    # back_scroller.draw_buildings()
    # back_scroller.move_buildings()
    # middle_scroller.draw_buildings()
    # middle_scroller.move_buildings()
    # front_scroller.draw_buildings()
    # front_scroller.move_buildings()



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
