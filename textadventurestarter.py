start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''


print(start)

left_right= True
while left_right:
	print("Type 'left' to go left or 'right' to go right.")
	user_input = input()
	

	if user_input == "left":
		left_right=False
		print("You decide to go left and there is a river.") 
		print("Swim across? Type 'yes' or 'no'.")
		
		yes_no= True
		while yes_no:
			print("Type 'yes' or 'no'")
			user_input = input()
			if user_input == "yes":
				yes_no=False
				print("You get washed down the waterfall to your death.")
			elif user_input == "no":
				yes_no=False
				print("You accidentally fall in to the river and drown.")
		
		print("The End")
	
	 
	elif user_input == "right":
		left_right=False
		print("You choose to go right and there is a flight of stairs") 
		print("Climb the stairs? Type 'yes' or 'no'.")
		
		yes_no= True
		while yes_no:
			print("Type 'yes' or 'no'")
			user_input = input()
			if user_input == "yes":
				yes_no=False
				print("You climb the stairs and make it back to your room.")
			elif user_input == "no":
				yes_no=False
				print("A boulder rolls down from the top of the stairs and crushes you and you die.")
		print("The End")
	

