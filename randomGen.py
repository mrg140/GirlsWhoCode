#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = [0, 1, 2 ,3]
FirstName = ["Ashley", "Eric", "Ron", "Karen"]
LastName = ["Smith", "Brown", "Jones", "Wilson"]
#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
RandomIndex = randint(0, len(aList)-1)
print (FirstName[aRandomIndex] + " " + LastName[RandomIndex])
