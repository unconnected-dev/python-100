#Coffee Machine

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

def main():
    report()

main()