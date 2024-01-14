from turtle import Turtle

FONT_STYLE = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()

        self.player_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()

    def display_score(self) -> None:
        self.clear()
        self.write(f"{self.player_score}", align="center", font=FONT_STYLE)

    def increase_player_score(self) -> None:
        self.player_score += 1
        self.display_score()
    
    def reset_score(self) -> None:
        self.player_score = 0
        self.display_score()