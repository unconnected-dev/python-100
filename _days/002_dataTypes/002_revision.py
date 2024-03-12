#Basic Data Types
print("Basic Data Types")

#Check data types
if False:
    strg = input("What is your first name?\n")
    strglen = len(strg)

    #Check variable type
    print("str type: " + str(type(strg)))
    print("strlen type: " + str(type(strglen)))

#Iterate through a string of numbers
if False:
    number = 134
    numberString = str(number)

    result = 0

    for c in numberString:
        result += int(c)
    
    print(result)

#Including values within print
if False:
    name = "Paul"
    age = 40

    print(f"{name} will be {age} soon enough...\n")

#Converting types
if False:
    s = "120.2"
    n = 4
    f = 1.2

    total = float(s) + n + f
    print(f"{total}")

#Converting with comprehension
if True:
    numbers = ["1", "2", "3", "4", "5", "6"]
    new_list = [int(n) for n in numbers]
    print(new_list)