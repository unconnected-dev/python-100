#Basic Variable Combining
print("Basic Variable Combining")

#Combine integers
if False:
    number1 = int(input("Enter the first number...\n"))
    number2 = int(input("Enter the second number...\n"))

    total = number1 + number2

    print("The two numbers combined make " + str(total))

#Combine strings
if False:
    string1 = input("Enter your first name...\n")
    string2 = input("Enter your last name...\n")

    combinedName = string1.capitalize() + " " + string2.capitalize()

    print("Your name is: " + combinedName)

if True:
    number1 = int(input(f"Enter the first number: "))
    number2 = int(input(f"Enter the second number: "))
    total = 0
    total += number1
    total += number2

    print(f"The total is: {total}")