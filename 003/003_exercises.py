
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
