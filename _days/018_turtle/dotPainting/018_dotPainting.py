#Dot Painting
import colorgram
import random
import turtle as t
from turtle import Turtle, Screen

#Get Colors
image = "C:/_GitHub/python-100/018_turtle/dotPainting/leaves.jpg"
colors = colorgram.extract(image, 10)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

def randomColor():
    return random.choice(rgb_colors)

#Switch colormode for rgb
t.colormode(255)

turtleObj = Turtle()
turtleObj.penup()
turtleObj.speed(0)
turtleObj.hideturtle()

turtleObj.setheading(225)
turtleObj.forward(250)
turtleObj.setheading(0)

for i in range(10):
    for j in range(10):
        color = randomColor()
        turtleObj.dot(20, color)
        turtleObj.forward(40)
    
    #Go back to leftmost point
    turtleObj.setheading(90)
    turtleObj.forward(40)
    turtleObj.setheading(180)
    turtleObj.forward(400)
    turtleObj.setheading(0)

screen = Screen()
screen.exitonclick()