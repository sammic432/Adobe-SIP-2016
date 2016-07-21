# import random

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREY = (129, 129, 129)
# colors = [BLACK, GREEN, BLUE, RED, WHITE, GREY]

# colors_length = len(colors)
# random_index = random.randint(0, colors_length)
# print (colors[random_index])




import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED, WHITE, GREY]
colors_length = len(colors)
random_index = random.randint(0, colors_length-1)

pygame.draw.rect (screen, BLACK, (400, 300, 100, 150), 0)

screen.fill(WHITE)
