
print ("start")
print ("You wake up one morning and find that you are not in your bed. you are not even in your room. You are in the middle of a giant maze. A sign is hanging from the ivy. You have one hour. Do not touch the walls. There is a hallway to your right and to your left."
)


user_input = input("Type 'left' to go left or 'right' to go right.")
while (user_input != 'left' and user_input != 'right'):
	print ("invalid answer")
	user_input = input ("Type 'left' to go left or 'right' to go right.")
if user_input == "left":
	print("You decide to go left and you continue walking forward. you see a lost boy, who is also trying to find his way out. should you follow him?")
	user_input1 = input("type 'yes' to follow him or 'no' to go your own way.")
	while (user_input1 != 'yes' and user_input1 != 'no'):
		print ("invalid answer")
		user_input1 = input("type 'yes' to follow him or 'no' to go your own way.")
	if user_input1 == "yes":
		print ("you go up to him and ask him if you can join him. he says yes, and you walk with him for a bit before the road splits. you have a strong feeling in your gut that you should go right, but he wants to go left.")
		user_input2 = input("type 'left' to go with him or type 'right' to leave and go by yourself.")
		while (user_input2 != 'left' and user_input2 != 'right'):
			print ("invalid answer")
			user_input2 = input("type 'left' to go with him or type 'right' to leave and go by yourself.")
		if user_input2 == "left":
			print ("you follow him and he seems pretty confident, until you both reach a dead end. you turn back around. he decides to go a separate path again so you follow him.")
			print ("you continue to follow him, and you reach the exit. ")
		elif user_input2 == "right":
			print ("YOU LOSE, HE HAS A MAP OF THE MAZE")
	elif user_input1 == "no":
		print ("you continue the path you were headed, and you make a few turns then you reach a dead end. you turn back around. you take a different path, but you see a treasure chest.")
		user_input3 = input("type  'open' to open the chest or type 'leave' to leave it alone")
		while (user_input3 != 'open' and user_input3 != 'leave'):
			print ("invalid answer")
			user_input3 = input("type  'open' to open the chest or type 'leave' to leave it alone")
		if user_input3 == "open":
			print ("you open the chest and it's filled with random things, but the two things stuck out: a compass and a map of the maze. you only get to choose one.")
			user_input4 = input("type 'compass' for the compass or type 'map' for the map")
			while (user_input4 != 'compass' and user_input4 != 'map'):
				print ("invalid answer")
				user_input4 = input("type 'compass' for the compass or type 'map' for the map")
			if user_input4 == "map":
				print ("you use the map to find the way out of the maze, and you reach the exit.")
			elif user_input4 == "compass":
				print ("YOU LOSE.")
		elif user_input3 == "leave":
			print ("YOU LOSE. THE CHEST HAD A MAP OF THE MAZE.")

    
elif user_input == "right":
	print("You choose to go right and you continue on the path, then you reach a dead end. but you see a treasure chest at the end..")
	user_input5=input("type 'open' to open the chest or type 'leave' to leave it")
	while (user_input5 != 'open' and user_input5 != 'leave'):
		print ("invalid answer")
		user_input5=input("type 'open' to open the chest or type 'leave' to leave it")
	if user_input5 == "open":
		print ("you open the chest and it's filled with random things, but the two things stuck out: a compass and a map of the maze. you only get to choose one.")
		user_input6 = input("type 'compass' for the compass or type 'map' for the map")
		while (user_input6 != "compass" and user_input6 != "map"):
			print ("invalid answer")
			user_input6 = input("type 'compass' for the compass or type 'map' for the map")
		if user_input6 == "map":
			print ("you use the map to find the way out of the maze, and you finally reach the exit.")
		elif user_input6 == "compass":
			print ("you use the compass and after a lot of turns, you finally reach the exit.")
	elif user_input5 == "leave":
		print ("you keep walking and you find an old notebook. you read it, and it has a map in it. you follow the map and you finally find the exit")
	    
