# --- Define your functions below! ---

def intro():
    print ("Hello! (The hangman game does not work that well)")
def process_input(answer):
    if is_valid_input (answer):
        say_greeting()
    else:
        say_default()
def is_valid_input(word):
    valid_response = ["hi", "Hi", "hello", "Hello", "hey", "Hey" "sup"]
    if word in valid_response:
        return True
    else:
        return False
def say_greeting():
    answer = input ("How are you?")
    if  valid_feeling(answer):
        say_wonderful()
    else:
        say_why()
def valid_feeling(word):
    valid_greet = ["good", "great", "nice", "happy", "okay", "alright"]
    if word in valid_greet:
        return True
    else:
        return False
def say_wonderful():
    print ("Thats great!")
    game()
def say_why():
    answer = input ("Aww, how come?")
    print ("Feel better!")
    game()
def say_default():
    print ("Okay!")
def game():
    answer = input("Do you want to play HANGMAN or GUESS a number?")
    if answer == "hangman":
        hangman()
    if answer == "guess" or "guess a number":
        numbergame()
def hangman():
    import random
    potential_words = ["example", "dog", "hello", "happy", "smile"]
    possible_letters = ["e", "x", "a", "m", "p", "l", "e", "d", "o", "g", "d", "h", "l", "p", "y", "s", "i"]
    possible_input = [potential_words, possible_letters]
    iter = 0
    word = random.choice(potential_words)
    word = word.lower()
    length = len(word)
    current_word = []
    for letter in word:
        current_word.append("_")
    print (current_word)
    guesses = []
    maxfails = 7
    fails = 0
    CorrectLetters = 0
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
def numbergame():
    #imports the ability to get a random number (we will learn more about this later!)
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
    	else:
    		if guess < aRandomNumber:
    			print ("Too low!")
    			tries +=1
    		else:
    			print ("Too high!")
    if tries == 3:
    	print ("Try Again!")



# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?)")
        answer = answer.lower ()
        process_input(answer)
        print("That's cool!")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
