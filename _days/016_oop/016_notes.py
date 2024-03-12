#Basic Turtle Objects
import turtle
from turtle import Turtle, Screen

if False:
    # anObject = turtle.Turtle()
    anObject = Turtle()
    anObject.forward(100)

    myScreen = Screen()
    print(f"{myScreen.canvheight}")
    myScreen.exitonclick()


#Basic PrettyTable Objects
from prettytable import PrettyTable

myTable = PrettyTable()
myTable.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
myTable.add_column("Type", ["Electric", "Water", "Fire"])

myTable.align = "l"
print(myTable)