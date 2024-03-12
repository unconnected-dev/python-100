#Debugging Fizz Buzz

target = int(input("Please enter a number...\n"))

for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")
     