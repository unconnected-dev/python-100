
#Odd or Even
#Return if a given number is odd or even
if False:
    num = int(input("Please enter a number\n"))
    answer = num % 2

    if(answer == 0):
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")


#BMI Calculator
if False: 
    height = input("Please enter your height (m):\n")
    weight = input("Please enter your weight (kg):\n")

    heightFloat = float(height)
    weightFloat = float(weight)

    bmi = weightFloat / (heightFloat ** 2)
    bmiInteger = int(bmi)

    respone = ""

    if bmi < 18.5:
        respone = "underweight"
    elif bmi <= 25:
        response = "your ideal weight"
    elif bmi <= 30:
        response = "over-weight"
    elif bmi <= 35:
        response = "obese"
    else:
        response = "clinically-obese"

    print("Your BMI is: " + str(bmiInteger))
    print(f"You are {response}")


#Leap Year
if False:
    year = int(input("Please enter a year\n"))
    leapYear = False

    if year % 4 == 0:
        if year % 100 != 0:
            leapYear = True
        elif year % 400 == 0:
            leapYear = True

    if leapYear == True:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


#Pizza Orders
if False:
    print("Thank you for choosing Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L\n")
    addPepperoni = input("Do you want pepperoni? Y/N\n")
    extraCheese = input("Do you want extra cheese? Y/N\n")

    bill = 0
    if size == "S" or size == "s":
        bill += 15
    elif size == "M" or size == "m":
        bill += 20
    elif size == "L" or size == "l":
        bill += 25

    if addPepperoni == "Y" or addPepperoni == "y":
        if size == "S" or size == "s":
            bill += 2
        else:
            bill += 3

    if extraCheese == "Y" or extraCheese == "y":
        bill += 1

    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}")


#Love Calculator
if False:
    print("The Love Calculator is calculating your score...")
    name1 = input("What is your name?\n")
    name2 = input("What is their name?\n")
    combinedNames = name1.lower() + name2.lower()

    loveScore = 0
    firstDigit = 0
    secondDigit = 0

    for c in "true":
        firstDigit += combinedNames.count(c)

    for c in "love":
        secondDigit += combinedNames.count(c)

    loveScore = int(str(firstDigit) + str(secondDigit))

    if loveScore < 10:
        print(f"Your score is {loveScore}, you go togeather like coke and mentos")
    elif loveScore >= 40 and loveScore <= 50:
        print(f"Your score is {loveScore}, you are alright togeather")
    else:
        print(f"Your score is {loveScore}")