#Basic Loops
print("Basic Loops")

letters = ["a", "b", "c", "d", "e"]

#Iterating in different ways
if False:
    for index, letter in enumerate(letters):
        print(f"index: {index}, letter: {letter}")

if False:
    for letter in letters:
        print(f"{letter}")
    
if False:
    for i in range(len(letters)):
        print(f"{letters[i]}")

#While loops
if False:
    i = 0
    while i < 5:
        print(f"{i}")
        i += 1

#Loop control statements
if False:
    for i in range(10):
        #Stop at 7
        if i == 7:
            break
        #Skip even numbers
        if i % 2 == 0:
            continue

        print(f"{i}")