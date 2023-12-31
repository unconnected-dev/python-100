#Coffee Machine

import os

recipes = {
    "Espresso": [1.50, 50, 18],
    "Latte": [2.50, 200, 24, 150],
    "Cappuccino": [3.00, 250, 24, 100]
}

contents = {
    "water": 300,
    "milk": 200,
    "coffee": 100
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
    # response = input("What would you like?")

def main():
    inGame = True
    while inGame == True:
        playCoffeeMenu()

        response = input("Would you like another coffee? y/n\n").lower()
        if response == 'y':
            inGame = True
        else:
            inGame = False
        
        os.system('cls')

    print("Shutting down...")

main()