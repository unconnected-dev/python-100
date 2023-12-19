#Higher Lower Game
import random
import art
import game_data


def randomData():
    return game_data.data[random.randint(0, len(game_data.data))]

def init():
    initA = randomData()
    initB = randomData()

    while initA["name"] == initB["name"]:
        initB = randomData()

    return initA, initB

def vs(optionA, optionB):
    print(f'{optionA["name"], optionA["description"]}, from {optionA["country"]}')
    print(f"{art.vs}")
    print(f'{optionB["name"], optionB["description"]}, from {optionB["country"]}')

    correctAnswer = 'A'
    if optionA["follower_count"] < optionB["follower_count"]:
        correctAnswer = 'B'

    guess = 'C'
    while guess != 'A' and guess != 'B':
        guess = input("Who has more followers? Type 'A' or 'B':\n")

    return guess == correctAnswer

def mainGame(init):
    if init == True:
        randomA, randomB = init()
        init = False

    print(f"{art.logo}")

    guessCorrect = vs(randomA, randomB)


mainGame(True)