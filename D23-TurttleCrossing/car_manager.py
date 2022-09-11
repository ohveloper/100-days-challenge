from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(0, 2) == 0:
            new_car = Turtle("square")
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randrange(-240, 240))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.bk(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT