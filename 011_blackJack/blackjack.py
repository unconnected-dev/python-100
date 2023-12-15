#Blackjack
import logo
import random

suites = {
    "h":"Hearts",
    "d":"Diamonds",
    "s":"Spades",
    "c":"Clubs"
}
    
cardValues = {
    "2": [2,"Two"],
    "3": [3,"Three"],
    "4": [4,"Four"],
    "5": [5,"Five"],
    "6": [6,"Six"],
    "7": [7,"Seven"],
    "8": [8,"Eight"],
    "9": [9,"Nine"],
    "10":[10,"Ten"],
    "J": [10,"Jack"],
    "Q": [10,"Queen"],
    "K": [10,"King"],
    "A": [11,"Ace"],
}

cardsInPlay = dict()
playerCardHandValues = []
dealerCardHandValues = []

def randomCard():
    suite = random.choice(list(suites))
    value = random.choice(list(cardValues))

    return suite, value

def generateCard(playerCard):
    cardGenerating = True
    
    while cardGenerating == True:
        cSuite, cValue = randomCard()
        cardId = cSuite + cValue[1]
        if cardId not in cardsInPlay:
            cardGenerating = False

            #If a player card is being generated
            if playerCard == True:
                print(f"You get a {cValue[1]} of {cSuite}")
            else:
                print(f"The dealer gets a {cValue[1]} of {cSuite}")
            
            cardsInPlay[cardId] = 1

            return cValue[0]
    
def generateInitialHand():
    playerCardHandValues.append(generateCard(True))
    playerCardHandValues.append(generateCard(True))
    dealerCardHandValues.append(generateCard(False))

def askToHit():
    response = input("Would you like one more card? y/n")

    if response == 'y':
        hitMe(True)

def hitMe(playerCard):
    if playerCard == True:
        playerCardHandValues.append(generateCard(True))
    else:    
        dealerCardHandValues.append(generateCard(False))

def checkOver21():
    playerTotal = sum(playerCardHandValues)

    if playerTotal > 21 and 11 not in playerCardHandValues:
        return True
    
    while sum(playerCardHandValues) > 21 and 11 in playerCardHandValues:
        playerCardHandValues[playerCardHandValues.index(11)] = 1
    
    if playerTotal > 21:
        return True
    
    return False

def mainGame():
    generateInitialHand()

        



print(logo.logo)


