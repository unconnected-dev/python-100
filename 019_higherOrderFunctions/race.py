#Race
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
screen.bgcolor("grey")
player_choice = screen.textinput(title="Pick one", prompt="Which will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

arrows = []

y_pos = 130
for i in range(len(colors)):
    arrow = Turtle()
    arrow.shapesize(3, 3)
    arrow.color(colors[i])
    arrow.penup()
    arrow.goto(x=-210, y=y_pos)
    y_pos -= 50
    arrows.append(arrow)


race_on = False
if player_choice:
    race_on = True

while race_on:
    
    for arrow in arrows:
        arrow.forward(random.randint(0, 10))
    



screen.exitonclick()