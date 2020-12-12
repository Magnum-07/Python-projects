from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, align=ALIGNMENT, font=FONT)
