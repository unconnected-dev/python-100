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
screen.onkeypress(paddle_1.up, "w")
screen.onkeypress(paddle_1.down, "s")

screen.onkeypress(paddle_2.up, "Up")
screen.onkeypress(paddle_2.down, "Down")

screen.onkey(scoreboard.shutdown, "Escape")

while scoreboard.game_on:
    screen.update()
    time.sleep(0.05)
    screen.update()
    ball.move_ball()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with left paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect collision with right paddle
    if ball.distance(paddle_2) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    

    #Detect paddle miss
    if ball.xcor() > 390:
        ball.reset_ball()
        scoreboard.increase_p2_score()

    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.increase_p1_score()
        

screen.exitonclick()