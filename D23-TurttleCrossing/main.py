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


screen.onkey(player.move, "Up")

cars = []
game_is_on = True
time_speed = 0.1
while game_is_on:
    time.sleep(time_speed)
    screen.update()
    for i in cars:
        i.move_car()

    if random.randint(0,2) == 0:
        car = CarManager()
        cars.append(car)

    if player.ycor() > 280:
        scoreboard.add_score()
        player.reset_player()
        time_speed *= 0.7

    for car in cars:
        # car보다 아래 있을때
        if player.ycor() < car.ycor():
            if player.distance(car) < 35 and car.xcor() > player.xcor():
                game_is_on = False
                scoreboard.game_over()

        # car 보다 위에 있을때
        # else:
        #     if player.distance(car) < 35:
                # game_is_on = False


        # for car in cars:
        #     car.reset_speed()

    # cars = []


screen.exitonclick()