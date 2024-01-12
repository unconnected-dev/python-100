import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

a_snake = Snake()

screen.listen()
screen.onkey(a_snake.up, "Up")
screen.onkey(a_snake.down, "Down")
screen.onkey(a_snake.left, "Left")
screen.onkey(a_snake.right, "Right")

game_on = True

while game_on:
    screen.update()    
    time.sleep(0.15)

    a_snake.move_snake()


screen.exitonclick()