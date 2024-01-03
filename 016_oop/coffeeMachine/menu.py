class MenuItem:
    def __init__(self, name, water, milk, coffee, cost) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self) -> None:
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.50),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.50),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.00)
        ]
    
    def formatCurrency(self, curr) -> str:
        """Formats float to string"""
        return '${:,.2f}'.format(curr)

    def getMenu(self) -> str:
        """Returns string of all menu items and cost"""
        lineLength = 20
        prefix = "This machine serves:\n"
        options = ""
        
        for item in self.menu:
            dotInt = lineLength - (len(item.name) + len(str(item.cost)))
            dotStr = ""
            for i in range(dotInt):
                dotStr += "."

            options += f"{item.name.capitalize()}{dotStr}{self.formatCurrency(item.cost)}\n"
        
        return prefix + options

    def getItem(self, itemName):
        """Returns MenuItem from Menu"""
        for item in self.menu:
            if item.name == itemName:
                return item
        
        return None            