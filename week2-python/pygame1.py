import pygame
import random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen.fill(WHITE)
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.flip()

pygame.display.set_caption ("Bouncing Ball Game")

done = False

clock = pygame.time.Clock()

pygame.draw.line (SCREEN, WHITE, [60,60], [100,60], WIDTH = 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = true
            
