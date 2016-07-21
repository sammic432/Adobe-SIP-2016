number = 31
user_guess = input ("guess my favorite number")

while number != int(user_guess):
	if number < int(user_guess):
		print ("your guess was too high")
		user_guess = input ("try again: ")
	elif number > int(user_guess):
		print ("your guess was too low")
		user_guess = input ("try again: ")

if number == int(user_guess):
	print ("you got it right")
	print ("game over")