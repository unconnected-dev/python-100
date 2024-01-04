import os
from menu import Menu
from coffeeMaker import CoffeeMaker
from moneyMachine import MoneyMachine
from currencyHandler import CurrencyHandler

def main() -> None:
    menu = Menu()
    moneyMachine = MoneyMachine()
    coffeeMaker = CoffeeMaker()
    currencyHandler = CurrencyHandler()

    while True:
        
        #Looping menu for valid order that can be made
        while True:
            menu.printMenu()
            order = input(f"What would you like?\n").lower()

            if order == "report":
                coffeeMaker.report()
                moneyMachine.report()
                input("Press Enter to continue...")
                os.system('cls')
            elif menu.getItem(order) != None and coffeeMaker.resourcesAvailable(menu.getItem(order)) == True:
                orderItem = menu.getItem(order)
                break
            else:
                input("Invalid order, press Enter to try again...")
                os.system('cls')
                

        #Get payment from customer
        paymentMade = False
        while paymentMade == False:
            print(f"Please insert {currencyHandler.getFormattedCurrency(orderItem.cost)}")
            response = ""
            paymentMade = moneyMachine.makePayment(orderItem.cost)
            
            if paymentMade == False:
                response = input(f"Would you like to reinsert the coins? y/n: ")
            else:
                input("Press enter to continue...")

            os.system('cls')

            if paymentMade == False and response == "n":
                break


        #Make coffee
        if paymentMade == True:
            coffeeMaker.makeCoffee(orderItem)


        response = input("Would you like another coffee? y/n\n").lower()
        if response == 'n':
            break
        
        os.system('cls')
    
    print("Shutting down...")

main()