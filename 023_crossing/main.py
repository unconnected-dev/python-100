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
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    #Detect car collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_on = False

    #Detect crossing
    if player.ycor() >= 280:
        player.return_to_start()
        car_manager.increase_cars_speed()
        

screen.exitonclick()