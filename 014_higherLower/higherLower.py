#Higher Lower Game
import os
import random
import art
import game_data

def randomData():
    """Return random entry of data"""
    return game_data.data[random.randint(0, len(game_data.data))]

def initGame():
    """Generates two initial data entries to compare"""
    initA = randomData()
    initB = randomData()

    while initA["name"] == initB["name"]:
        initB = randomData()

    return initA, initB

def vs(optionA, optionB):
    """Compares two options and returns if player guess is correct"""
    print(f'{optionA["name"], optionA["description"]}, from {optionA["country"]}')
    print(f"{art.vs}")
    print(f'{optionB["name"], optionB["description"]}, from {optionB["country"]}')

    correctAnswer = 'a'
    if int(optionA["follower_count"]) < int(optionB["follower_count"]):
        correctAnswer = 'b'

    guess = 'c'
    while guess != 'a' and guess != 'a':
        guess = input("Who has more followers? Type 'A' or 'B':\n").lower()

    return guess == correctAnswer

def playHigherLower(init):
    winning = True
    score = 0
    guessCorrect = False

    if init == True:
        randomA, randomB = initGame()
        init = False

    while winning == True:
        print(f"{art.logo}")
        
        if guessCorrect == True:
            print(f"You're right! Current score: {score}")

        guessCorrect = vs(randomA, randomB)

        if guessCorrect == True:
            score += 1
        else:
            winning = False
        
        randomA = randomB
        while randomA["name"] == randomB["name"]:
            randomB = randomData()
        
        os.system('cls')
    
    print(f"{art.logo}")
    print(f"Sorry, that's wrong. Final score: {score}")
    

def mainGame():
    playAgain = True
    while playAgain == True:
        playHigherLower(True)

        response = input("Would you like one more game? y/n\n").lower()
        if response == 'y':
            playAgain == True
        else:
            playAgain = False
    
        os.system('cls')

    print(f"Thank you for playing...")

mainGame()