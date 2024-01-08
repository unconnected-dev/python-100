#Regular Import
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

#Import All
#Avoid using
if False:
    from turtle import * 

    turtleObj = Turtle()
    
#ALias
if False:
    import turtle as t

    turtleObj = t.Turtle()