def welcome_fun():
	print ("Welcome. ")
def select_fun():
	answer = ("Do you want to see our games? Let me know if you want. (Y/N): ")
	start_answer = input (answer)
	return start_answer
def games_fun():
	slots = {"Burning ice. ": "Burning ice is slot game which has 27 lines and FREE spins.", 
			"Book of Bruno. ": "Book of Bruno is slot game which has 10 lines and FREE spins.", 
			"Pirates.": "Pirates is slot game which has 15 lines and FREE spins.\n" }
	video_poker = {"Jolly poker. ": "Jolly poker is type of video poker which is very popular. 	You can try it online for free.\n"}
	table_games = {"Roulette. ": "Roulette is type of table games which you can play online for free. There are 37 nubers, 0 and 36 numbers.",
			  "Live roulette. ": "Live roulette is type of table games which you can play online for free. There is a girl which leads the game.\n"}  
	games = ["1. Slots", "2. Video poker", "3. Table games"]
	for i in games:
		print (i)
	user_input=input("Your choice is (1-3): ")
	if user_input == "1":
		for s in slots:
			print (s)
		game_input = input("Do you need some additional information? (Y/N): ")
		if (game_input == "Y" or game_input == "y"):
			for s in slots:
				print (s, slots[s])
			# here might be elif for "N" and else for wrong answer
	elif user_input == "2":
			for v in video_poker:
				print (v)
			game_input = input("Do you need some additional information? (Y/N): ")
			if (game_input == "Y" or game_input == "y"):
				for v in video_poker:
					print (v, video_poker[v])
	elif user_input == "3":
			for t in table_games:
				print (t)
			game_input = input("Do you need some additional information? (Y/N): ")
			if (game_input == "Y" or game_input == "y"):
				for t in table_games:
					print (t, table_games[t])
	else:
			print("Wrong input. Please choose between 1-3")
def start_again ():
	restart_msg = ("If you want to see our games again press(y/n):")
	restart_answer =input(restart_msg)
	return restart_answer
def start_my_program():
	welcome_fun()
	x = select_fun()
	if (x == "Y" or x == "y"):
		games_fun()
		z = start_again()
		if z == "y" or z == "Y":
			return start_my_program()
		else:
			print ("Thank you for your interest for our games! See you next time...")
	elif x == "n" or x == "N":
		print ("Thank you for your interest for our games! See you next time...")
	else:
		print ("Wrong input.")
		return start_my_program()

if __name__ == "__main__":
    start_my_program()

