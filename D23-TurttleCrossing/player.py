from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        # x = self.xcor()
        # y = self.ycor() + MOVE_DISTANCE
        # self.goto(x, y)
        self.fd(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)


