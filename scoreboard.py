from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.write(f" {self.score_left} : {self.score_right} ", align="center", font=("Arial", 40, "normal"))
        self.hideturtle()

    def score_increase_l(self):
        self.score_left += 1
        self.write(f" {self.score_left} : {self.score_right} ", align="center", font=("Arial", 40, "normal"))
    def score_increase_r(self):
        self.score_right += 1
        self.write(f" {self.score_left} : {self.score_right} ", align="center", font=("Arial", 40, "normal"))
    def finish(self):
        self.goto(0, 0)
        self.write(" GAME FINISHED ", align="center", font=("Arial", 40, "normal"))
