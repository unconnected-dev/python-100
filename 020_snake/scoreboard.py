from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()

    def increase_score(self) -> None:
        self.score += 1
        self.display_score()

    def display_score(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))