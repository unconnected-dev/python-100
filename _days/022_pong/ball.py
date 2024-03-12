from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(0, 0)

        self.x_move = 8
        self.y_move = 8
    
    def move_ball(self) -> None:
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
    
    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()