import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

segment_list = []
start_pos = [(0, 0), (-20, 0), (-40, 0)]
for pos in start_pos:
    segment_ = Turtle("square")
    segment_.penup()
    segment_.color("white")
    segment_.goto(pos)
    segment_list.append(segment_)
    

screen.update()

game_on = True

while game_on:
    screen.update()    
    time.sleep(0.2)

    for i in range(len(segment_list) - 1, 0, -1):
        segment_list[i].goto(segment_list[i - 1].xcor(), segment_list[i - 1].ycor())
    
    segment_list[0].forward(20)

screen.exitonclick()