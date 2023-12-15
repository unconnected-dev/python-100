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

def askPlayerToHit():
    response = input("Would you like one more card? y/n")

    if response == 'y':
        playerCardHandValues.append(generateCard(True))
        return True
    
    return False
    
def askDealerToHit():
    while sum(dealerCardHandValues) > 21 and 11 in dealerCardHandValues:
        dealerCardHandValues[dealerCardHandValues.index(11)] = 1

    if sum(dealerCardHandValues) >= 17:
        return False
    
    #Dealer hits if able
    dealerCardHandValues.append(generateCard(False))
    return True

def checkOver21(cardHandValues):
    total = sum(cardHandValues)

    while sum(cardHandValues) > 21 and 11 in cardHandValues:
        cardHandValues[cardHandValues.index(11)] = 1
    
    if total > 21:
        return True
    
    return False

def checkResult():
    #Compare hands
    playerTotal = sum(playerCardHandValues)
    dealerTotal = sum(dealerCardHandValues)

    if len(playerCardHandValues) == 2 and playerTotal == 21:
        print(f"You got Blackjack, you win")
    elif dealerTotal == playerTotal:
        print(f"You tied with the dealer")
    elif dealerTotal > 21 and playerTotal <= 21:
        print(f"Dealer is over 21, you win")
    elif playerTotal > 21:
        print(f"Your total is over 21, you lost")
    elif playerTotal > dealerTotal:
        print(f"You beat the dealer, you win")
    elif dealerTotal > playerTotal:
        print(f"The dealer beat you, you lost")
    else:
        print(f"Error...")

def playBlackjack():
    generateInitialHand()

    #Check for natural 21
    if sum(playerCardHandValues) == 21:
        return True

    #Check if player wants to get more cards
    playerWantsCards = True
    while playerWantsCards == True and checkOver21(playerCardHandValues) == False:
        playerWantsCards = askPlayerToHit()

    if checkOver21(playerCardHandValues) == True:
        return True
    else:
        dealerWantsCards = True

        while dealerWantsCards == True and checkOver21(dealerCardHandValues) == False:
            dealerWantsCards = askDealerToHit()

        return True

def mainGame():
    playAgain = True
    while playAgain == True:
        print(logo.logo)
        playBlackjack()
        checkResult()
        
        response = input("Would you like one more hand? y/n")
        if response == 'y':
            playAgain == True
        else:
            playAgain = False
    
        input("Press Enter to continue...")

    print(f"Thank you for playing...")

mainGame()