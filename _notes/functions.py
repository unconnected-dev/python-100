#Functions

#Default arguments
if False:
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}"
    
    print(f"{greet('bob')}")

if False:
    def a_function(a=1,b=2,c=3):
        return a + b + c

    print(a_function())
    print(a_function(c=5))

#Variable length arguments
if False:
    def sum_values(*args):
        return sum(args)

    result = sum_values(1, 2, 3, 4, 5)
    print(f"{result}")

#Unlimited keyword arguments
#kwargs creates a dictionary
if False:
    def configure_settings(**kwargs):
        for key, value in kwargs.items():
            print(f"Setting {key} to {value}")

    configure_settings(language="Python", version="3.9", mode="debug")

#Return multiple values
if False:
    def get_coordinates():
        return 3, 4
    
    x, y = get_coordinates()
    print(f"{x}, {y}")