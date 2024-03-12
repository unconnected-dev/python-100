from currencyHandler import CurrencyHandler
    
class MoneyMachine:

    COINS = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self) -> None:
        self.totalStored = 0
        self.moneyReceived = 0
    
        self.currencyHandler = CurrencyHandler()
    
    def report(self) -> None:
        print(f"Money: {self.currencyHandler.getFormattedCurrency(self.totalStored)}")
    
    def processCoins(self) -> None:
        for coin in self.COINS:
            self.moneyReceived += int(input(f"How many {coin}?: ")) * self.COINS[coin]
        
    def makePayment(self, cost) -> bool:
        self.processCoins()
    
        if self.moneyReceived >= cost:
            change = round(self.moneyReceived - cost, 2)
            print(f"Here is {self.currencyHandler.getFormattedCurrency(change)} in change")
            self.totalStored += cost
            self.moneyReceived = 0
            return True
        else:
            short = round(cost - self.moneyReceived, 2)
            print(f"You are {self.currencyHandler.getFormattedCurrency(short)} short")
            print(f"Returning coins...")
            self.moneyReceived = 0
            return False