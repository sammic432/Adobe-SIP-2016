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
DBLUE = (1, 15, 21)
colors = [BLACK, WHITE, GREY]

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
        self.color = color


    def draw(self, x_point):
        pygame.draw.rect (screen, self.color, (self.x_point, self.y_point, self.width, self.height))
        


    def move(self, speed):
        self.x_point += speed
        if self.x_point <= -40:
            self.x_point = 820

        

list1 = []
class Scroller(object):


    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.list1 = []
        self.combined_width = 0
        self.create_buildings()


    def create_buildings(self):
        while self.combined_width <= self.width:
            self.create_building(self.combined_width)
            # self.combined_width += self.list1 


    def create_building(self, x_location):
        building_width = random.randint (80, 100)
        building_height = random.randint(-200, -60)
        self.combined_width += building_width
        building1 = Building (x_location, 600, building_width, building_height, self.color)

        self.list1.append (building1)


    def draw_buildings(self):
        for building1 in self.list1:
            building1.draw(0)

        """
        This calls the draw method on each building.
        """

    def move_buildings(self):
        for building1 in self.list1:
            building1.move(-2)

        building_width = random.randint (80, 100)

        building_height = random.randint(-200, -60)
        if self.list1[-1].x_point >= SCREEN_WIDTH:
            self.list1.remove (self.list1[-1])
        if self.list1[0].x_point > 0:
            width = random.randint (0, 60)
            x_location = self.list1[0].x_point - width
            #building1 = Building (x_location, 600, building_width, building_height, self.color)
            #self.list1.insert (0, building1)


        
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """

        class RunnerSprite (pygame.sprite.Sprite):
            def __init__ (self, size, color):
                pygame.sprite.Sprite.__init__ (self)




FRONT_SCROLLER_COLOR = (WHITE)
MIDDLE_SCROLLER_COLOR = (GREY)
BACK_SCROLLER_COLOR = (BLACK)
BACKGROUND_COLOR = (DBLUE)

#(self, width, height, base, color, speed):

front_scroller = Scroller(SCREEN_WIDTH, 200, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 6)
middle_scroller = Scroller(SCREEN_WIDTH, 400, (SCREEN_HEIGHT - 100), MIDDLE_SCROLLER_COLOR, 3)
back_scroller = Scroller(SCREEN_WIDTH, 550, (SCREEN_HEIGHT - 300), BACK_SCROLLER_COLOR, 1)






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
    screen.fill(DBLUE)

    # --- Drawing code should go here
    # build.draw ()
    # build.move (10)

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
