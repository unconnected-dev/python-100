
#Rock, Paper, Scissors
#Take user input and compare against random choice to see who the winner is

import random
import asciiArt


#Player input
choice = int(input("What do you choose?\nType 0 for Rock\n1 for Paper\n2 for Scissors\n"))
computerChoice = random.randint(0, 2)

#Display ascii art
print("You chose:\n")
print(asciiArt.art[choice])
print("Computer chose:\n")
print(asciiArt.art[computerChoice])


def compareChoices(loserOption, winnerOption):
        if(choice == computerChoice):
            print("You tied")
        elif(computerChoice == loserOption):
            print("You lose")
        elif(computerChoice == winnerOption):
            print("You win")
        else:
            print("This should not happen")


match choice:
    #Rock
    case 0:
        compareChoices(1, 2)
    #Paper
    case 1:
        compareChoices(2, 0)
    #Scissors
    case 2:
        compareChoices(0, 1)