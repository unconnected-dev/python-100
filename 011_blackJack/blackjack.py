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
        hit(True)
        return True
    else:
        return False
    
def askDealerToHit():
    while sum(dealerCardHandValues) > 21 and 11 in dealerCardHandValues:
        dealerCardHandValues[dealerCardHandValues.index(11)] = 1

    if sum(dealerCardHandValues) >= 17:
        return False
    
    #Dealer hits if able
    hit(False)
    return True

def hit(playerCard):
    if playerCard == True:
        playerCardHandValues.append(generateCard(True))
    else:    
        dealerCardHandValues.append(generateCard(False))

def checkOver21(cardHandValues):
    total = sum(cardHandValues)

    while sum(cardHandValues) > 21 and 11 in cardHandValues:
        cardHandValues[cardHandValues.index(11)] = 1
    
    if total > 21:
        return True
    
    return False

def playBlackjack():
    generateInitialHand()

    #Check if player wants to get more cards
    playerWantsCards = True
    while playerWantsCards == True and checkOver21(playerCardHandValues) == False:
        playerWantsCards = askPlayerToHit()

    if checkOver21(playerCardHandValues) == True:
        print(f"Your total is over 21, you lost...\n")
        return True
    else:
        dealerWantsCards = True

        while dealerWantsCards == True and checkOver21(dealerCardHandValues) == False:
            dealerWantsCards = askDealerToHit()

        #Compare hands
        playerTotal = sum(playerCardHandValues)
        dealerTotal = sum(dealerCardHandValues)

        if playerTotal > 21:
            print(f"Your total is over 21, you lost")
        elif dealerTotal > 21 and playerTotal <= 21:
            print(f"Dealer is over 21, you win")
        elif playerTotal != 21 and dealerTotal == playerTotal:
            print(f"You tied with the dealer")
        elif playerTotal > dealerTotal:
            print(f"You beat the dealer, you win")
        elif dealerTotal > playerTotal:
            print(f"The dealer beat you, you lost")

        return True


print(logo.logo)


