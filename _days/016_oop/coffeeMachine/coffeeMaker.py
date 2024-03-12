class CoffeeMaker:
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
    
    def report(self) -> None:
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def resourcesAvailable(self, menuItem) -> bool:
        valid = True
        for ingredient in menuItem.ingredients:
            if menuItem.ingredients[ingredient] > self.resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient} available")
                valid = False
        
        return valid
    
    def makeCoffee(self, menuItem) -> None:
        for ingredient in menuItem.ingredients:
            self.resources[ingredient] -= menuItem.ingredients[ingredient]
        
        print(f"Your {menuItem.name} is ready...")