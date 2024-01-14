from turtle import Turtle

FONT_STYLE = ("Arial", 18, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

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
        self.write(f"Score: {self.score} - - High Score: {self.high_score}", align="center", font=FONT_STYLE)
    
    def display_game_over(self) -> None:
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT_STYLE)
    
    def reset_scoreboard(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        
        self.score = 0
        self.display_score()
