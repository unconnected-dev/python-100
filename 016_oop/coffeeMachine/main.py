import os
from menu import Menu
from coffeeMaker import CoffeeMaker
from moneyMachine import MoneyMachine

def main() -> None:
    menu = Menu()
    moneyMachine = MoneyMachine()
    coffeeMaker = CoffeeMaker()

    running = True
    while running == True:



        response = input("Would you like another coffee? y/n\n").lower()
        if response == 'y':
            running = True
        else:
            running = False
        
        os.system('cls')
    
    print("Shutting down...")

main()