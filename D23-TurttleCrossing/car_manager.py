from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        if random.randint(0, 5) == 0:
            new_car = Turtle("square")
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=3)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randrange(-240, 240))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.bk(STARTING_MOVE_DISTANCE)
