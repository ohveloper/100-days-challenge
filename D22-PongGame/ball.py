from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction = (10, 10)

    def move(self):
        x = self.xcor() + self.direction[0]
        y = self.ycor() + self.direction[1]
        self.goto(x, y)
