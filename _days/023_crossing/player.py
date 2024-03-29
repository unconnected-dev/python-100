from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self) -> None:
        self.forward(MOVE_DISTANCE)
    
    def return_to_start(self) -> None:
        self.goto(STARTING_POSITION)