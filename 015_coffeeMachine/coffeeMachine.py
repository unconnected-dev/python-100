#Coffee Machine

import os

#Price, Water, Coffee, Milk
recipes = {
    "Espresso": [1.50, 50, 18],
    "Latte": [2.50, 200, 24, 150],
    "Cappuccino": [3.00, 250, 24, 100]
}

contents = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}

coins = {
    "penny": ["pennies", 0.01],
    "nickel": ["nickles", 0.05],
    "dime": ["dimes", 0.10],
    "quarter": ["quarters", 0.25]
}

def report():
    print(f"+ Machine Contents +")
    print(f"Water: {contents['water']}ml")
    print(f"Milk: {contents['milk']}ml")
    print(f"Coffee: {contents['coffee']}g")

def currency(curr) -> str:
    return  '${:,.2f}'.format(curr)

def printLine(k):
    totalLength = 20
    dotInt = totalLength - (len(k) + len(str(recipes[k][0])))
    dotStr = ""
    for i in range(dotInt):
        dotStr += "."
    
    currVal = currency(recipes[k][0])
    print(f"{k}{dotStr}{currVal}")

def playCoffeeMenu():
    print(f"This machine serves:")
    for key in recipes:
        printLine(key)
    print("")

#Check machine has contents available
def validateOrder(o) -> bool:
    recipe = recipes[o]
    valid = True
    if contents["water"] < recipe[1]:
        print(f"Sorry, there is not enough water")
        valid = False

    if contents["coffee"] < recipe[2]:
        print(f"Sorry, there is not enough coffee")
        valid = False

    if len(recipe) > 3 and contents["milk"] < recipe[3]:
        print(f"Sorry, there is not enough milk")
        valid = False
    
    return valid

#Get order from user
def getOrder():
    response = input("What would you like?\n").lower()
    orderValid = False

    while order not in recipes and orderValid == False:
        print(f"Invalid option please try again...")
        if order not in recipes:
            order = input("What would you like?\n").lower()

        orderValid = validateOrder(order)

    return response

def playCoffee():
    playCoffeeMenu()

    order = getOrder()


def main():
    inGame = True
    while inGame == True:
        playCoffee()

        response = input("Would you like another coffee? y/n\n").lower()
        if response == 'y':
            inGame = True
        else:
            inGame = False
        
        os.system('cls')

    print("Shutting down...")

main()