from turtle import Screen, Turtle
# from paddle2 import Paddle
# from test import Test
from bar import Bar
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_bar = Bar((350, 0))
l_bar = Bar((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_bar.r_bar_up, "Up")
screen.onkey(r_bar.r_bar_down, "Down")
screen.onkey(l_bar.l_bar_up, "w")
screen.onkey(l_bar.l_bar_down, "s")

is_game_on = True
right_up = (10, 10)
right_down = (10, -10)

while is_game_on:
    time.sleep(0.1)
    # 중요 포인트, tracer(0)함수와 연결되어 활용
    screen.update()
    ball.move()

    # Detect collision with up wall
    if ball.ycor() > 280:
        ball.direction = right_down

    # Detect collision with right wall
    elif ball.xcor() > 380:
        is_game_on = False




screen.exitonclick()