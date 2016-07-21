from random import *

article = ["the", "a", "an"]
adjectives = ["good", "new", "first", "young", "small", "true"]
nouns = ["tables", "stones", "plants", "lights", "words"]

print (article[randrange(0, len(article))] + " " + adjectives[randrange(0, len(adjectives))] + " " + nouns[randrange(0, len(nouns))])
