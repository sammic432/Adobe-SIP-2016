

grocery_list = []

while True:
	user_input = input ("Type a grocery item to add on your grocery list. Type 'all done' when you finish")
	if user_input != "all done":
		grocery_list.append (user_input)
	print (grocery_list)
	if user_input == "all done":
		exit()