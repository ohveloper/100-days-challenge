from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    # .tracer()로 멈췄던 애니메이션을 다시 작동 시기큰 함수
    screen.update()
    # 잠시 멈췄다가 다시 진행 시키는 함수
    time.sleep(0.1)
    # 스네이크 움직여!
    snake.move()



screen.exitonclick()