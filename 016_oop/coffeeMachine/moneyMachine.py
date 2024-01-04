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
    
    def report(self):
        print(f"Money: {self.currencyHandler.getFormattedCurrency(self.profit)}")
    
    def processCoins(self):
        for coin in self.COINS:
            self.moneyReceived += int(input(f"How many {coin}?: ")) * self.COINS[coin]
        
        return self.moneyReceived

    def makePayment(self, cost):
        self.processCoins()
    
        if self.moneyReceived >= cost:
            change = round(self.moneyReceived - cost, 2)
            print(f"Here is {change} in change")
            self.totalStored += cost
            self.moneyReceived = 0
            return True
        else:
            short = round(cost - self.moneyReceived, 2)
            print(f"You are {short} short")
            print(f"Returning coins...")
            self.moneyReceived = 0
            return False