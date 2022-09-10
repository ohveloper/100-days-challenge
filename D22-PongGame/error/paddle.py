from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def l_bar_up(self):
        x = self.xcor()
        y = self.ycor()
        y += 20
        self.goto(x, y)

    def l_bar_down(self):
        x = self.xcor()
        y = self.ycor()
        y -= 20
        self.goto(x, y)

    def r_bar_up(self):
        x = self.xcor()
        y = self.ycor()
        y += 20
        self.goto(x, y)

    def r_bar_down(self):
        x = self.xcor()
        y = self.ycor()
        y -= 20
        self.goto(x, y)