import turtle as t
FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-275, 265)
        self.level = 1
        self.score_writer()

    def score_writer(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", font=FONT)

    def increase_level(self):
        self.level += 1
        self.score_writer()
