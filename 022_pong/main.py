from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")

screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")

screen.onkey(scoreboard.shutdown, "Escape")

while scoreboard.game_on:
    screen.update()
    ball.move_ball()
    time.sleep(0.03)

screen.exitonclick()