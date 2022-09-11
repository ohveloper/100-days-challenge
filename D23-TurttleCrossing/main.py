import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.onkey(player.move, "Up")

game_is_on = True
time_speed = 0.1

while game_is_on:
    time.sleep(time_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()


    if player.is_at_finish_line():
        scoreboard.add_score()
        player.reset_player()
        car_manager.level_up()

    for car in car_manager.cars:
        # car보다 아래 있을때
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()