from sys import exit

def game_room():
	print "This is a room full of video game consoles, which do you pick from either the Ps4 or Xbox1"
	game_room = True

	while game_room == True:
		next = raw_input("> ")

		if next == "Ps4":
			print "Great choice!, I see you're a great fan of PlayStation"

		elif next == "Xbox1":
			print "Awesome choice, I see you're really a big fan of microsoft"

		else:
			dead("You have to pick a video game")