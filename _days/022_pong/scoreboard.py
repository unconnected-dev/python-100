from turtle import Turtle

FONT_STYLE = ("Arial", 18, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.game_on = True
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()

    def display_score(self) -> None:
        self.clear()
        self.write(f"{self.p1_score} : {self.p2_score}", align="center", font=FONT_STYLE)

    def increase_p1_score(self) -> None:
        self.p1_score += 1
        self.display_score()
        
    def increase_p2_score(self) -> None:
        self.p2_score += 1
        self.display_score()
    
    def reset_score(self) -> None:
        self.p1_score = 0
        self.p2_score = 0
        self.display_score()
    
    def shutdown(self) -> None:
        self.game_on = False
