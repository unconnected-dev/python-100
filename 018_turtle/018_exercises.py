#Draw Square
from random import randint


if False:
    from turtle import Turtle, Screen

    turtleObj = Turtle()
    turtleObj.shape("triangle")
    turtleObj.color("black")

    #Draw Square
    if False:
        for i in range(4):
            turtleObj.forward(100)
            turtleObj.right(90)

    screen = Screen()
    screen.exitonclick()


#Dashed Line
if False:
    from turtle import Turtle, Screen

    turtleObj = Turtle()
    turtleObj.shape("triangle")
    turtleObj.color("black")
    
    #Draw Dashed Square
    if True:
        for i in range(4):
            for i in range(5):
                turtleObj.forward(10)
                turtleObj.penup()
                turtleObj.forward(10)
                turtleObj.pendown()

            turtleObj.right(90)

    screen = Screen()
    screen.exitonclick()


#Draw All Shapes From Triangle to Decagon
if True:
    from turtle import Turtle, Screen

    turtleObj = Turtle()
    turtleObj.shape("triangle")
    turtleObj.color("black")

    for j in range(3, 10):
        ang = 360 / j

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
        turtleObj.color(hex_color)
        
        for i in range(j):
            turtleObj.forward(50)
            turtleObj.right(ang)
    
    screen = Screen()
    screen.exitonclick()