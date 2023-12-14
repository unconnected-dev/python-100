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

def clearCards(pCards):
    pCards.clear()
        
def randomCard():
    suite = random.choice(list(suites))
    number = random.choice(list(cards))

    return suite, number

def generateCard(playerCard, pCards):
    cardGenerating = True
    
    while cardGenerating == True:
        suite, number = randomCard()
        cardId = suite + str(number)
        if cardId not in cardsInPlay:
            cardGenerating = False

            if playerCards == True:
                print(f"You get a {number} of {suite}")
                pCards[cardId] = 1
            else:
                print(f"The dealer gets a {number} of {suite}")
                dCards[cardId] = 1

            return number
    
def generateHands(pCards):
    playerCardHandValues.append(generateCard(True, pCards))
    playerCardHandValues.append(generateCard(True, pCards))

    dealerCardHandValues.append(generateCard(False, pCards))
    
    

print(logo.logo)


