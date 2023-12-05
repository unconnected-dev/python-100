#Basic Loops
print("......................................................................")
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
    
print("-End of script-")