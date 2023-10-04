import random

#FizzBuzz
if False:
    def fizz():
        print("Fizz")

    def buzz():
        print("Buzz")

    def fizzBuzz():
        print("FizzBuzz")

    max = int(input("Enter a number to count to\n"))
    i = 0
    while i < max:
        i += 1

        if i % 3 == 0 and i % 5 == 0:
            fizzBuzz()
        elif i % 3 == 0:
            fizz()
        elif i % 5 == 0:
            buzz()
        else:
            print(f"{i}")


#Guess Number
if False:
    guessed = False

    while guessed == False:
        num = int(input("Pick a number between 1 and 5\n"))
        ranNum = random.randint(1, 5)

        if num == ranNum:
            print("You guessed right")
            guessed = True
        else:
            print(f"Oh no, it was {ranNum}, try again")

    print("Finished")