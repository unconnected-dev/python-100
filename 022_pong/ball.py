from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(0, 0)
    
    def move_ball(self) -> None:
        self.goto(self.xcor() + 10, self.ycor() + 10)