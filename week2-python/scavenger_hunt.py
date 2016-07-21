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
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
NAVY = (0, 0, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
VIOLET = (238, 130, 238)

LIGHTPINK = (255, 170, 146)
BLUEGREEN = (116, 255, 129)
MAGENTA = (255, 0, 67)
# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
circlex = random.randint (0, 700)
circley = random.randint (0, 500)
speedx = random.randint (-10, 10)
speedy = random.randint (-10, 10)
circlesize = random.randint (20,80)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ballcolors = [BLACK, WHITE, GREEN, RED, BLUE, GREY, NAVY, YELLOW, ORANGE, PINK, VIOLET]
    ballcolor = random.choice (ballcolors)

    screencolors = [BLACK, WHITE, GREEN, RED, BLUE, LIGHTPINK, BLUEGREEN, MAGENTA]
    screencolor = random.choice (screencolors)

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(screencolor)

    # --- Drawing code should go here

    pygame.draw.circle (screen, ballcolor, (circlex,circley), circlesize, 0)
    circlex += speedx
    circley += speedy

    if circlex < 0 or circlex > 700:
        speedx = -speedx
    if circley < 0 or circley > 500:
        speedy = -speedy

    


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
