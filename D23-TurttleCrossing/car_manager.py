from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=3)
        self.color(COLORS[random.randint(0, 5)])
        self.goto(300, random.randrange(-240, 240))
        self.move_increment = MOVE_INCREMENT


    def move_car(self):
        x = self.xcor() - MOVE_INCREMENT
        y = self.ycor()
        self.goto(x ,y)

    def reset_speed(self):
        self.move_increment += 10