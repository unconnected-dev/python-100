#Number Guessing
import random

def generateRandomNumber(low, high):
    print(f"I'm thinking of a number between {low} and {high}.")
    return random.randint(low, high)

def hardOrEasy():
    response = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if response == 'easy':
        return 10
    elif response == 'hard':
        return 5
    else:
        return 1
    
def guess(a):
    print(f"You have {a} attmpts remaining to guess the number.")
    aGuess = int(input(f"Make a guess: "))
    return aGuess

def correctGuess(gameNum, playerNum):
    if gameNum == playerNum:
        return True
    elif gameNum > playerNum:
        print(f"Too high.")
    else:
        print(f"Too low.")

def mainGame():
    playAgain = True
    while playAgain:
        print(f"Welcome to the Number Guessing Game...")
        numberToGuess = generateRandomNumber(1, 100)
        attemptsLeft = hardOrEasy()

        while attemptsLeft > 0:
            playerGuess = guess(attemptsLeft)
            attemptsLeft -= 1

