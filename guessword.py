import random
# A list of words that
potential_words = ["example", "dog", "hello", "happy", "smile"]
possible_letters = ["e", "x", "a", "m", "p", "l", "e", "d", "o", "g", "d", "h", "l", "p", "y", "s", "i"]
possible_input = [potential_words, possible_letters]
iter = 0
word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
length = len(word)

 # TIP: the number of letters should match the word
current_word = []
for letter in word:
    current_word.append("_")
print (current_word)
# Some useful variables
guesses = []
maxfails = 7
fails = 0
CorrectLetters = 0
#for let in word:
#    current_word.append("_")

remaining = str(maxfails-fails)

while fails < maxfails:
    guess = input("Guess a letter: ")
    for letter in range(0, len(word)):
        if word[letter] == guess:
            current_word[letter] = guess
            CorrectLetters +=1
    print (current_word)
    if guess == word:
        print ("Win!")
        break
    elif guess != word:
        maxfails = 7
        remaining = maxfails-fails
        fails += 0
        print (str(remaining) + " tries left!")
    if CorrectLetters == len(word):
        print ("Win!")
        break
#    if guess ==
#        current_word[iter] = guess
#    iter +=1
    #for let in word:
    #    if let == (possible_input):
    #        current_word[iter] = guess
    #    iter +=1

#    elif input () != possible_input:
#        print("You have "+ str(maxfails-1 + " tries left!")
    #if possible_letters in input():
        #print (right)
#    elif input () != possible_input:
#        print("You have "+ str(maxfails-1 + " tries left!")


	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
