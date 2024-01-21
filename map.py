# Sang T. Truong
# Assignment 1
# map.py
from inventory import *

#this is a Add-ons function  
def playAgain():
#I don't put the lowercase here is, because I want users know exactly what they type wrong!
	usertext = input('Try again (Yes/No)? ') #.lower()
	if usertext.lower() in ['yes','y']:
		print('\n\nRestarting...')
		return Existingin0_0()
	elif usertext.lower() in ['no','n']:
		pass
	else: 
		print(f'\"{usertext}\" is not a valid answer\n')
		print('\n\n')
		return playAgain()



def stopgame():
	return print('The game stopped!')

def Existingin0_0():
	print("You are in a forest glade!")
	print('\nNorth & West are rock walls!\nThere is a path to the south and to the east\nThere is a treasure chest in the hollow of a tree\n')
	print(
		'''
Commands to play:\n'west' or 'w' to go West\n'e' or 'east' to go East\n'north' or 'n' to go North\n'south' or 's' to go South\nexit to stop!\n'look' or 'l' to view where you are\n'take' or 't' to collect stuffs\n'h' or 'help' to show instructions
		''')
	while True:
		usertext = input('Your text here >> ').lower()
		if usertext in Look: #same as =='look' or =='l'. Just make it cleaner
			print('You are in a forest glade!\nNorth & West are rock walls!\nThere is a path to the south and to the east\nItem: a treasure chest in the hollow of a tree\n')
		elif usertext in Down:
			print("You have moved to South in (0_1)")
			existingin0_1()	
			break	
		elif usertext in Right:
			print("You have moved to East (in 1_0)")
			existingin1_0()
			break
		elif usertext in Left or usertext in Up:
			print("Ouch, that rock wall hurt")
		elif usertext in Take:
			global obj0_0 #Set global scope so I can change the value of object from inventory file even I am in the function
			if obj0_0==False:
				print('There is a treasure chest in the hollow of a tree')
				usertext = input('press TAKE or \'T\' to collect it:\n').lower() 
				if usertext in Take:
					print('You collected a treasure chest in 0_0 map')
					 #Set global scope for variable to change it value
					obj0_0=True #change value to True and always True out side the scope. In case you ask me and I forgot why i did this!
					pass 

				else: 
					print(f'\'{usertext}\' is not a valid input!')
					print('Please try again!')
					pass
			else: 
				print("You already took it, you greedy!")
				

		elif usertext in ['help', 'h']:
			print('''Commands to play:\n'west' or 'w' to go West\n'e' or 'east' to go East\n'north' or 'n' to go North\n'south' or 's' to go South\nexit to stop!\n'look' or 'l' to view where you are\n'take' or 't' to collect stuffs\n'h' or 'help' to show instructions''')
		elif usertext in ['move', 'm']:
			print('Which direction?')
		elif usertext == 'exit':
			return stopgame()
		else:
			print(f"The action \"{usertext}\" is invalid!\n")

def existingin0_1():
	print('You are in a pitch black cave!')
	while True:
		usertext = input('Your text here >> ').lower()
		if usertext in ['south', 's', 'west', 'w', 'east', 'e']:
			print("If you move a grue will eat you\n")
		elif usertext in Take:
			print("There is nothing to take here!\n")
		elif usertext in Look:
			print('You are in a pitch black cave\nNorth is an exit from here!\n')
		elif usertext in Up:
			print('You have moved North')
			Existingin0_0()
			break
		elif usertext in ['help', 'h']:
			print('''Commands to play:\n'west' or 'w' to go West\n'e' or 'east' to go East\n'north' or 'n' to go North\n'south' or 's' to go South\nexit to stop!\n'look' or 'l' to view where you are\n'take' or 't' to collect stuffs\n'h' or 'help' to show instructions''')
		elif usertext in ['move', 'm']:
			print('Which direction?')
		elif usertext == 'exit':
			return stopgame()
		else:
			print(f"The action \"{usertext}\" is invalid!\n")

def existingin1_0():
	print('You are in the foot hills of a mountain range!')
	while True:
		usertext = input('Your text here >> ').lower()
		if usertext in Up:
			print('Ouch, that rock wall hurt\n')
		elif usertext in Right:
			print('You kick off your shoes and start to swim to the setting sun, then change your mind and return and put your shoes back on!\n')
		elif usertext in Left:
			print("You have moved to West (in 0_0)")
			Existingin0_0()
			break
		elif usertext in Down:
			print("You have gone down 1 step (1_1)")
			existingin1_1()	
			break
		elif usertext in Take:
			print("There is nothing to take here!\n")
		elif usertext in Look:
			print('You are in the foot hills of a mountain range\nNorth is a mountain\nEast is an ocean<There are paths to the adjoining map cells>\nThere is a watch in the sand')
		elif usertext in ['help', 'h']:
			print('''Commands to play:\n'west' or 'w' to go West\n'e' or 'east' to go East\n'north' or 'n' to go North\n'south' or 's' to go South\nexit to stop!\n'look' or 'l' to view where you are\n'take' or 't' to collect stuffs\n'h' or 'help' to show instructions''')
		elif usertext in ['move', 'm']:
			print('Which direction?')
		elif usertext == 'exit':
			return stopgame()
		else:
			print(f"The action \"{usertext}\" is invalid!\n")

def existingin1_1():
	print("You are in a canyon in the ground!")
	while True:
		usertext = input('Your text here >> ').lower()
		if usertext in Look:
			print("You are in a canyon in the ground\nAbe Lincoln’s golden top hat\nPaths to the north, south and east\n")
		elif usertext in Right:
			print("You have moved one step to the East! (in 2_1)\n")
			Existingin2_1()
			break
		elif usertext in Down:
			print("You have moved a step to the south! (in 1_2)\n")
			Existingin1_2()
			break
		elif usertext in Left:
			print("You\'re back in the cave (1_0)\n")
			existingin0_1()
			break
		elif usertext in Up:
			print("Nope! that's not the way!\n.")
		elif usertext in Take:
			global obj1_1
			if obj1_1==False:
				print('The Abe Lincoln’s golden top hat')
				usertext = input('press TAKE or \'T\' to collect it:\n').lower()
				if usertext in Take:
					print('You collected the Abe Lincoln’s golden top hat in 1_1 map')

					obj1_1=True
				else: 
					print(f'\'{usertext}\' is not a valid input!')
					print('Please try again!')
					pass
			else: print("You already took it, you greedy!")
			

		elif usertext in ['help','h']:
			print('''Commands to play:\n'west' or 'w' to go West\n'e' or 'east' to go East\n'north' or 'n' to go North\n'south' or 's' to go South\nexit to stop!\n'look' or 'l' to view where you are\n'take' or 't' to collect stuffs\n'h' or 'help' to show instructions''')
		elif usertext in ['move', 'm']:
			print('Which direction?')
		elif usertext == 'exit':
			return stopgame()
		else:
			print(f"The action \"{usertext}\" is invalid!\n")

def Existingin1_2():
	print("You are in a swamp!")
	while True:
		usertext = input('Your text here >> ').lower()

		if usertext in Look:
			print('''
You are in a swamp
There is a jeweled skull in the muck
There is a mysterious portal to the west.
Paths to the north and east\n
''')
		elif usertext in Up:
			print('Ok 1 step back\n')
			existingin1_1()
			break
		elif usertext in Down:
			print("Hm... This seems to be the end of the world. You cannot go that way\n.")
		elif usertext in Left:
			usertext = input("Are you sure? (Yes/No)").lower()
			if usertext in ['y','yes']:
				print('GAME OVER!\nYou\'re at the starting point (0_0)\n')
				Existingin0_0()
				break
			elif usertext in ['n', 'no']: 
				pass #continue the process
			else:	
				print(f'{usertext} is invalid\nPlease try again!\n')
				Existingin1_2()
				break
		elif usertext in Right:
			print('One step to the East...\n')
			Existingin2_2()
			break
		elif usertext in Take:
			global obj1_2
			if obj1_2 ==False:
				print('There is a jeweled skull in the muck!')
				usertext = input('press TAKE or \'T\' to collect it:\n').lower()
				if usertext in Take:
					print('You looted a precious jeweled skull in 1_2 map')
					
					obj1_2=True
					pass
				else: 
					print(f'\'{usertext}\' is not a valid input!')
					print('Please try again!')
					pass
			else: 
				print("You already took it, you greedy!")
				

		elif usertext in ['help','h']:
			print('''Commands to play:\n'west' or 'w' to go West\n'e' or 'east' to go East\n'north' or 'n' to go North\n'south' or 's' to go South\nexit to stop!\n'look' or 'l' to view where you are\n'take' or 't' to collect stuffs\n'h' or 'help' to show instructions''')
		elif usertext in ['move', 'm']:
			print('Which direction?')
		elif usertext == 'exit':
			return stopgame()
		else:
			print(f"The action \"{usertext}\" is invalid!\n")

def Existingin2_1():
	print("You are in Volcanic wasteland!")
	while True:
		usertext = input('Your text here >> ').lower()
		if usertext in Look:
			print('You are in Volcanic wasteland\nA diamond in a pile of ash\nPaths to west and south\nOcean to the north\n')
		elif usertext in Right:
			print("You forgot your skis and cannot go that way\n")
		elif usertext in Left:
			print("Too fast. Did you drop something? let's go back! (1_1)\n")
			existingin1_1()
			break
		elif usertext in Up:
			print("You see a sea serpent in the water and decide it is best to stay on land\n.")
		elif usertext in Down:
			print("Brave warrior!\nYou\'re almost there! (in 2_2)\n")
			Existingin2_2()
			break
		elif usertext in Take:
			global obj2_1
			if obj2_1 == False:
				print('There is a DIAMOND in a pile of ash!')
				usertext = input('press TAKE or \'T\' to collect it:\n').lower()
				if usertext in Take:
					print('You just looted a precious diamond in 2_1 map')
					
					obj2_1=True
					pass
				else: 
					print(f'\'{usertext}\' is not a valid input!')
					print('Please try again!')
					pass
			else: 
				print("You already took it, you greedy!")
				

		elif usertext in ['help','h']:
			print('''Commands to play:\n'west' or 'w' to go West\n'e' or 'east' to go East\n'north' or 'n' to go North\n'south' or 's' to go South\nexit to stop!\n'look' or 'l' to view where you are\n'take' or 't' to collect stuffs\n'h' or 'help' to show instructions''')
		elif usertext in ['move', 'm']:
			print('Which direction?')
		elif usertext == 'exit':
			return stopgame()
		else:
			print(f"The action \"{usertext}\" is invalid!\n")

def Existingin2_2():
	print("You are in a grass plain")
	while True:
		usertext = input('Your text here >> ').lower()
		if usertext in Look:
			print('''A grass plain
East: a huge chasm in the ground 
West and north are the paths
A pot of gold in the grass
A glowing exit to the south''')
		elif usertext in Right:
			print("You make a spectacular swan dive and vanishinto a void, never to be seen again.\nGAME OVER!")
			playAgain()
			break
		elif usertext in Left:
			print('Prepare to get wet in a swamp!')
			Existingin1_2()
			break
		elif usertext in Up:
			print("Redirect to the Volcanic wasteland")
			Existingin2_1()
			break
		elif usertext in Take:
			global obj2_2
			if obj2_2== False:
				print('There is a pot of gold in the grass right there')
				usertext = input('press TAKE or \'T\' to collect it:\n').lower()
				if usertext in Take:
					print('You just collected a pot of gold in the last map')
					
					obj2_2=True
					pass
				else: 
					print(f'\'{usertext}\' is not a valid input!')
					print('Please try again!')
					pass
			else: 
				print("You already took it, you greedy!")
				
		
		elif usertext in Down:
			print('You\'ve escaped!')
			# print(COLLECTIONS)
			break

		elif usertext in ['help','h']:
			print('''Commands to play:\n'west' or 'w' to go West\n'e' or 'east' to go East\n'north' or 'n' to go North\n'south' or 's' to go South\nexit to stop!\n'look' or 'l' to view where you are\n'take' or 't' to collect stuffs\n'h' or 'help' to show instructions''')
		elif usertext in ['move', 'm']:
			print('Where to go?')
		elif usertext == 'exit':
			return stopgame()
		else:
			print(f"The action \"{usertext}\" is invalid!\n")
			break
	#These codes will run when the loop breaks
	print('Your loot:')
	if obj0_0:
		print("- A treasure chest in the hollow of a tree contain a magic powder") 
	if obj1_1:
		print('- Abe Lincoln’s golden top hat on the mount') 
	if obj1_2:
		print('- A jeweled skull in the muck') 
	if obj2_1:
		print('- A diamond burried in a Volcanic wasteland')
	if obj2_2:
		print('- A shining pot of gold')
	elif obj0_0==False and obj1_1==False and obj1_2==False and obj2_1==False and obj2_2==False:
		print('nothing :(')
