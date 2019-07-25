#tictactoe
import random

print ("play tictactoe")
spots = ["1","2","3","4","5","6","7","8","9"]
def board():
    print (" " + spots[0] + " | " + spots [1] + " | " + spots[2]+ " ")
    print ("_________")
    print (" " + spots[3] + " | " + spots [4] + " | " + spots[5]+ " ")
    print ("_________")
    print (" " + spots[6] + " | " + spots [7] + " | " + spots[8]+ " ")

tries = 0
possible_wins = []
win1=[spots[0],spots[1], spots[2]]
while tries < 9:
    board()
    move = int(input ("You are 'X'. Where do you want to move? (Choose from 1-9)"))
    spots[move - 1] = 'X'
    tries+=1
    spots[random.randrange(1,9)] = 'O'
