# Sang T. Truong
# Assignment 1
# gameFile.py

from map import *
from inventory import *

#main function runs here!
def runGame():
	print('Welcome the the adventure text-game.')
	username = input("Please enter your character name: ")
	while len(username)==0:
		username = input("Please don't leave your character name blank: ")
		if len(username)!=0:	
			break
	print(f'\nWelcome {username} to the game')
	Existingin0_0()

runGame()
