from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:        
        random_x=random.randint(-14, 14) * 20
        random_y=random.randint(-14, 14) * 20
        self.goto(random_x, random_y)
