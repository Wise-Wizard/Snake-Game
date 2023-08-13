from turtle import Turtle
ALIGNMENT = "center"
FONTSTYLE = ("Times New Roman", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("#FAF3F0")

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONTSTYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
