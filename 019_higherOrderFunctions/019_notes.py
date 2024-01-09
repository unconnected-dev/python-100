#Listener
if False:
    from turtle import Turtle, Screen

    turtleObj = Turtle()
    screen = Screen()

    def move_forward():
        turtleObj.forward(10)

    screen.listen()
    screen.onkey(key="space", fun=move_forward)

    screen.exitonclick()