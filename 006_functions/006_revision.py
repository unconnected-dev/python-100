#Basic Functions
print("......................................................................")
print("Basic Functions")

#Basic function call
if False:
    def aFunction():
        print("This is a function call")

    aFunction()

#Passing parameters
if False:
    def hello(name):
        print(f"Hello {name}, how are you?")
    
    hello("Paul")

#Loop with function calls
if False:
    def fizzBuzz(n):
        r = ""
        if n % 3 == 0 and n % 5 == 0:
            r = "FizzBuzz"
        elif n % 3 == 0:
            r = "Fizz"
        elif n % 5 == 0:
            r = "Buzz"
        else:
            r = str(n)

        return r

    max = 15
    i = 0
    while i <= max:
        print(fizzBuzz(i))
        i += 1

print("-End of script-")