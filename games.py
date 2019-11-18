# The program uses a loop to allow the user to interact with it multiple times 
print ("Welcome. ")
answer = "empty"
games=["1. Slots", "2. Video poker", "3. Table games\n"]
slots = {"Burning ice. ": "Burning ice is slot game which has 27 lines and FREE spins.", 
		 "Book of Bruno. ": "Book of Bruno is slot game which has 10 lines and FREE spins.", 
		 "Pirates.": "Pirates is slot game which has 15 lines and FREE spins.\n" }
video_poker = {"Jolly poker. ": "Jolly poker is type of video poker which is very popular. You can try it online for free.\n"}
table_games = {"Roulette. ": "Roulette is type of table games which you can play online for free. There are 37 nubers, 0 and 36 numbers.",
			  "Live roulette. ": "Live roulette is type of table games which you can play online for free. There is a girl which leads the game.\n"}

while answer != "quit":
	answer = input("Do you want to see our games? Let me know if you want. (Y/N): ")
	if (answer == "Y" or answer == "y"):
		for item in games:
			print (item)
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
	elif answer == "n" or answer == "N":
		print ("Thank you for your interest for our games! See you next time...")
		break
	else:
		print ("Wrong input.")
print ("Goodbue.")
