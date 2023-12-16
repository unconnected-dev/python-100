#Number Guessing
import os
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
    return int(aGuess)

def correctGuess(gameNum, playerNum):
    print(f"{gameNum}, {playerNum}")
    if gameNum == playerNum:
        return True
    elif gameNum > playerNum:
        print(f"Too low.")
    else:
        print(f"Too high.")

    return False

def mainGame():
    playAgain = True
    while playAgain:
        print(f"Welcome to the Number Guessing Game...")
        numberToGuess = generateRandomNumber(1, 100)
        attemptsLeft = hardOrEasy()
        playerWon = False

        while attemptsLeft > 0:
            playerGuess = guess(attemptsLeft)
            attemptsLeft -= 1

            if correctGuess(numberToGuess, playerGuess):
                print(f"You got it! The answer was {numberToGuess}")
                playerWon = True
                break

        if not playerWon:
            print(f"You've run out of guesses, you lose.")
        
        response = input("Would you like to play again? y/n\n")
        if response == 'y':
            playAgain == True
        else:
            playAgain = False
    
        os.system('cls')

    print(f"Thank you for playing...")

mainGame()