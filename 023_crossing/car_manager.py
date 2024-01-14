from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        """Randomly generates a car 25% of the time"""
        if random.randint(0, 3) == 3:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.setheading(180)

            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))

            self.cars.append(car)
    
    def move_cars(self) -> None:
        for car in self.cars:
            car.forward(self.car_speed)
    
    def increase_cars_speed(self) -> None:
        self.car_speed += MOVE_INCREMENT