import random

#Basic Lists
print("......................................................................")
print("Basic Lists")

#Appending to list
if False:
    aList = []

    for i in range(1,11):
        aList.append(random.randint(0, 10))

    print(f"{aList}")

#Remove from a list
if False:
    aList = [0, 7, 1, 2, 3, 4, 5]

    print(f"{aList}")
    #Searches for a value and removes it
    aList.remove(1)
    print(f"{aList}")

if False:
    aList = [0, 7, 1, 2, 3, 4, 5]

    print(f"{aList}")
    #Pops from a certain index
    aList.pop(2)
    print(f"{aList}")

#Reference negative points
if False:
    names = ["Bob", "Dan", "Ken", "Ben", "Bill"]

    print(f"0: {names[0]}")
    print(f"1: {names[1]}")
    print(f"-1: {names[-1]}")
    print(f"-2: {names[-2]}")

#Iterating over list
if False:
    fruits = ["Apples", "Strawberries", "Pineapples", "Tomatoes", "Mangoes"]

    # for fruit in fruits:
    #     print(f"{fruit}")

    # for i in range(len(fruits)):
    #     print(f"{fruits[i]}")

    for i, val in enumerate(fruits):
        print(f"i: {i}, val:{val}")

#Merging lists
if False:
    someList = ["a", "b", "c", "e"]
    someOtherList = ["d", "f", "g", "h"]

    #* is the spread operator
    #without it, you have 2 lists in a list
    combinedList = [*someList, *someOtherList]

    print(f"{combinedList}")

    combinedList.sort()
    print(f"{combinedList}")

#Multi dimensional lists
if False:
    line1 = [" ", " ", " "]
    line2 = [" ", " ", " "]
    line3 = [" ", " ", " "]
    map = [line1, line2, line3]

    position = input("Where do you want to put X? A-C, 1-3\n")

    #position is a string
    x = position[0].lower()
    y = position[1]

    letters = ["a", "b", "c"]
    letterIndex = letters.index(x)
    numberIndex = int(y) - 1

    #this is not a shallow copy
    #it references directly to the original line1, line2, line3
    map[letterIndex][numberIndex] = "X"
    print(f"{line1}\n{line2}\n{line3}")

print("-End of script-")