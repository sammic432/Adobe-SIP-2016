# attr: dimensions, color, system, generation, brand
# methods: 138x67x7, gold, ios, 6s, apple
# takes pictures, calls, texts

class phones():
	def __init__ (self, dimensions, color, system, generation, brand):
		self.dimensions = dimensions
		self.color = color
		self.system = system
		self.generation = generation
		self.brand = brand


	# methods 
	def takes_pictures():
		print ("Taking a picture")

	def calling():
		print ("ring ring...")

	def texting ():
		print ("...")

iphone = phones(138, "gold", "ios", "6s", "apple")