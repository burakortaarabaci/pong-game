from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(position)

    def right_up(self):
        self.forward(20)

    def right_down(self):
        self.backward(20)

    def left_up(self):
        self.forward(20)

    def left_down(self):
        self.backward(20)



