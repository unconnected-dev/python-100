#Basic Data Types
print("......................................................................")
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


print("-End of script-")
