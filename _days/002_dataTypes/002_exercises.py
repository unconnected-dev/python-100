
#Given an integer, take the individual digits and add them togeather
if False:
    input = 39

    print(type(input))
    inputString = str(input)

    result = 0
    for char in inputString:
        result += int(char)

    print(result)


#BMI Calculator
if False:
    height = input("Please enter your height (m):\n")
    weight = input("Please enter your weight (kg):\n")

    heightFloat = float(height)
    weightFloat = float(weight)

    bmi = weightFloat / (heightFloat ** 2)
    bmiInteger = int(bmi)
    print("Your BMI is: " + str(bmiInteger))


#Based off the age of 90
#Calculate how many weeks a person has given their age
if False:
    totalPossibleWeeks = 52*90
    currentWeeksUsed = 52 * int(input("How old are you?\n"))
    currentWeeksLeft = totalPossibleWeeks - currentWeeksUsed

    print(f"You have {currentWeeksLeft} weeks left.")
