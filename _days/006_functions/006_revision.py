#Basic Functions
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

#Passing functions as arguments
if False:
    def apply_operation(x, y, operation):
        return operation(x, y)
    
    def add(x, y):
        return x + y
    
    def multiply(x, y):
        return x * y
    
    result_add = apply_operation(3, 4, add)
    result_multiply = apply_operation(3, 4, multiply)

    print(f"result_add: {result_add}")
    print(f"result_multiply: {result_multiply}")

#Lambda
if False:
    call = lambda a: a * 2

    print(f"{call(2)}")

#Sorting function
if False:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_even = lambda x: x % 2 == 0

    #This splits the even numbers to the second half
    sorted_numbers = sorted(numbers, key=is_even)
    print(f"{sorted_numbers}")