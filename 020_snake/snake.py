from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        for position in START_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position) -> None:
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend_snake(self) -> None:
        self.add_segment(self.segments[-1].position())

    def move_snake(self) -> None:
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        
        self.segments[0].forward(SNAKE_SPEED)
    
    def up(self) -> None:
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)
    
    def down(self) -> None:
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)
    
    def left(self) -> None:
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
    
    def right(self) -> None:
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
    