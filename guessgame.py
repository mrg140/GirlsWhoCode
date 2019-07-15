#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
tries = 0
# For Testing: print(aRandomNumber)
#while tries < 3:
for tries in range(3):
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess)
# converts a string to an integer
	if guess == aRandomNumber:
		print("Correct!")
		break
	elif guess < aRandomNumber:
		print ("Too low!")
		tries +=1
	else:
		print ("Too high!")
if tries == 3:
	print ("Try Again!")
