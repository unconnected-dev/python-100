from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")

start_pos = [(0, 0), (-20, 0), (-40, 0)]

for pos in start_pos:
    segment_ = Turtle("square")
    segment_.color("white")
    segment_.goto(pos)

screen.exitonclick()