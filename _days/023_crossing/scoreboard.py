from turtle import Turtle

FONT_STYLE = ("Courier", 18, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()

        self.player_score = 0

        self.color("black")
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self) -> None:
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.player_score}", align="center", font=FONT_STYLE)

    def increase_player_score(self) -> None:
        self.player_score += 1
        self.display_score()
    
    def reset_score(self) -> None:
        self.player_score = 0
        self.display_score()
    
    def game_over(self) -> None:
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT_STYLE)