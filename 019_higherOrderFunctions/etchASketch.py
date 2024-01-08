#Etch A Sketch
from turtle import Turtle, Screen

turtleObj = Turtle()
turtleObj.speed(0)
screen = Screen()

def move_forward():
    turtleObj.forward(10)

def move_backward():
    turtleObj.forward(-10)

def move_left():
    turtleObj.setheading(turtleObj.heading() - 10)

def move_right():
    turtleObj.setheading(turtleObj.heading() + 10)

def reset():
    screen.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="space", fun=reset)

screen.exitonclick()