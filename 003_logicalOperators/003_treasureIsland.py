#Treasure Island
#Choose your own adventure

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
gameOver = False

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

print("You're at a cross road. Where do you want to go?\n Type \"left\" or \"right\"\n")
choice1 = input("Left or Right\n").lower()

if choice1 == "left":
    print("You fell into a hole. Game over")
    gameOver = True
elif choice1 != "right":
    print("You can't type. Game over")
    gameOver = True

if gameOver:
    quit()


print("You come to a lake. There is an island in the middle of the lake.\n Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
choice2 = input("Swim or Wait\n").lower()

if choice2 == "wait":
    print("You die waiting for a boat that never comes. Game over")
    gameOver = True
elif choice2 != "swim":
    print("You can't type. Game over")
    gameOver = True

if gameOver:
    quit()


print("You arrive at the island unharmed? There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
choice3 = input("Which door? Red, Yellow, or Blue?\n").lower()

if choice3 == "blue":
    print("A freezing wind turns you to ice. Game over")
elif choice3 == "red":
    print("It is a room full of fire. Game over")
elif choice3 == "yellow":
    print("You find a room of gold. You win")
else:
    print("You can't type. Game over")

quit()