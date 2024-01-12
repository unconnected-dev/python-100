import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

a_snake = Snake()

game_on = True

while game_on:
    screen.update()    
    time.sleep(0.2)

    a_snake.move_snake()


screen.exitonclick()