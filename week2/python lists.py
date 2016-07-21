from random import *

adjectives = ["sour", "sweet", "salty", "spicy", "savory", "mild", "chewy", "bittersweet", "fried", "sweet and sour"]
cooking_styles = ["steamed", "seasoned", "chinese styled", "deep fried", "grilled", "roasted", "indian styled", "boiled", "fried", "barbeque"]
foods = ["chicken", "beef", "tofu", "pho", "soup", "shrimp", "fish", "pasta", "ramen", "chicken wings"]

print (adjectives[randrange(0, len(adjectives))] + " " + cooking_styles[randrange(0, len(cooking_styles))] + " " + foods[randrange(0, len(foods))])
