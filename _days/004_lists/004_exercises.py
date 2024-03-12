import random

#Heads or Tails
if(False):
    headTails = random.randint(0, 1)
    if(headTails == 0):
        print("Heads")
    else:
        print("Tails")


#Banker Roulette
if False:
    namesString = "Paul Ben Tom Dan James"
    names = namesString.split(" ")

    randomPick = random.randint(0, len(names) - 1)

    print(f"Today {names[randomPick]} will pay")


#Treasure Map
if False:
    line1 = [" ", " ", " "]
    line2 = [" ", " ", " "]
    line3 = [" ", " ", " "]
    map = [line1, line2, line3]
    print("Hiding your treasure! X marks the spot.")

    position = input("Where do you want to put the treasure? A-C, 1-3\n")

    x = position[0].lower()#Letter
    y = position[1]#Number

    letters = ["a", "b", "c"]
    letterIndex = letters.index(x)
    numberIndex = int(y) - 1

    map[letterIndex][numberIndex] = "X"

    print(f"{line1}\n{line2}\n{line3}")