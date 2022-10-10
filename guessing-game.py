import random

def Name():
    global name
    name = input("Hello what is your name? ")
    Game()

# Sets Low Limit
def LowLimit():
    global Low
    LowB = False
    while not LowB:
        try:
            Low = int(input("What number would you like for the range to start at? "))
            LowB = True
        except ValueError:
            print(f"Selection is invalid, please try again")

def HighLimit():
    global High
    HighB = False
    while not HighB:
        try:
            High = int(input("What number would you like for the range to start at? "))
            if High > Low:
                HighB = True
            else:
                print(f"Selection must be higher than {Low}")
                HighB = False
        except ValueError:
            print(f"Selection is invalid, please try again")

def Guess():
    global guess
    GuessB = False
    while not GuessB:
        try:
            guess = int(input("Take a guess. "))
            if guess < Low:
                print(f"Please chose a number higher than {Low}")
            elif guess > High:
                print(f"Please chose a number Lower than {High}")
            else:
                GuessB = True
        except ValueError:
            print("Selection is invalid, please try again")

def Game():
    Continue = True
    # Game Loop
    while Continue:
        LowLimit()
        HighLimit()
        
        secretNumber = random.randint(Low,High)
        print(f"Well, {name}, I am thinking of a number between {Low} and {High}")

        # Ask the player to guess 6 times
        for guessesTaken in range(1,7):
            Guess()
            if guess < secretNumber:
                print("Your guess is too low.")
                Guess()
            elif guess > secretNumber:
                print("Your guess is too high.")
                Guess()
            else:
                break # This condition is the correct guess

        if guess == secretNumber:
            print("Good job, " + name + '! You guessed my number in ' + str(guessesTaken) + " guesses!")
        else:
            print("Nope the number i was thinking of was " + str(secretNumber))
        Cont = input("Would you like to try again? (y/n)")
        if Cont != "y" or Cont != "yes":
            print("Have a good day!")
            Continue = False

Name()




# Write the following loop:
# a) Prompt the user for a limit (SET)
# b) Call a function to play the game which will: (SET)
# Calculate a random number using the limit entered by the user (SET)
# Display a message showing the range to be guessed (SET)
# Write a loop that will: (SET)
# Prompt the user for a number (SET)
# Compare the user guess to the generated random number (SET)
# If the guess is too high, display message and retry (SET)
# If the guess is too low, display message and retry (SET)
# If the guess is correct, display message and exit loop (SET)
# Prompt the user to play again (SET)
# If y, replay the game (SET)
# If n, terminate the program (SET)