#Coffee Machine

import os

#Price, Water, Coffee, Milk
recipes = {
    "espresso": [1.50, 50, 18],
    "latte": [2.50, 200, 24, 150],
    "cappuccino": [3.00, 250, 24, 100]
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
    print(f"{k.capitalize()}{dotStr}{currVal}")

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

#Get user order and check valid
def getOrder():
    order = input("What would you like?\n").lower()
    orderValid = False

    while order not in recipes and orderValid == False:
        if order not in recipes:
            input("Invalid order, press Enter to try again...")
            os.system('cls')
            playCoffeeMenu()
            order = input("What would you like?\n").lower()

        if order in recipes:
            orderValid = validateOrder(order)

    return order

#Insert coins
def coinInsert() -> float:
    total = 0
    for k in coins:
        val = int(f"How many {coins[k][0]}?: ") * coins[k][1]
        total += val
    
    return total

#Get payment and check enough
def payment(o):
    expectedCost = recipes[o][0]

    print(f"Please insert {currency(expectedCost)} to the machine...")
    coinTotal = coinInsert()

    while coinTotal < expectedCost:
        diff = expectedCost - coinTotal
        print(f"You are {currency(diff)} short")
        input(f"Returning coins, press Enter to try again...")
        os.system('cls')
        print(f"Please insert {currency(expectedCost)} to the machine...")
        coinTotal = coinInsert()
    

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