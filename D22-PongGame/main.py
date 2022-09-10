from turtle import Screen, Turtle
# from paddle2 import Paddle
# from test import Test
from bar import Bar


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# ttt = Test((1,2,3))
#
r_bar = Bar((350, 0))
l_bar = Bar((-350, 0))
# print(l_bar.color(), r_bar)

screen.listen()
screen.onkey(r_bar.r_bar_up, "Up")
screen.onkey(r_bar.r_bar_down, "Down")
screen.onkey(l_bar.l_bar_up, "w")
screen.onkey(l_bar.l_bar_down, "s")

is_game_on = True

while is_game_on:
    screen.update()




screen.exitonclick()