import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

a_snake = Snake()
a_food = Food()

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

    #Detect collision with food
    if a_snake.head.distance(a_food) < 15:
        a_food.refresh()
        # a_snake.add_segment()

screen.exitonclick()