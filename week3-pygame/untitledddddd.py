import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED, WHITE, GREY] 
colors_length = len(colors)
random_index = random.randint (0, colors_length)

def random_color ():
	print (random_index)