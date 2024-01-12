from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED = 20

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self) -> None:
        for position in START_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def move_snake(self) -> None:
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        
        self.segments[0].forward(SNAKE_SPEED)
        