
import math

#Paint Calculator
if False:
    def paintCalc(h, w, c):
        print("")
        totalArea = h * w
        numberOfCans = math.ceil((totalArea / c))
        print(f"You need {numberOfCans} can(s)...")


    height = int(input("Height of the wall (m)\n"))
    width = int(input("Width of the wall (m)\n"))
    coverage = 5
    paintCalc(height, width, coverage)


#Prime Number Checker
if False:
    def primeChecker(number):
        prime = True
        for i in range(2, number):
            if number % i == 0 and number != i:
                prime = False
                break

        if prime == True:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")
            
    n = int(input("Enter a number\n"))
    primeChecker(n)