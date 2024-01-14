import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing")
screen.bgcolor("white")
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_car()
    cars.move_cars()

screen.exitonclick()