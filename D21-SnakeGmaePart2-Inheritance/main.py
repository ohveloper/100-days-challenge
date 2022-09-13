from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

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

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        # food에 닿으면 새로운 위치로 food 옮김
        food.refresh()
        # 스코어를 += 1 한뒤 화면에 띄워줌
        score.add_score()
        # food 에 닿으면 맨 뒤에 하나 추가
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("hello")
        score.reset()
        snake.reset()

    # Detect collision with tail.
    # slicing 을 활용해 1번 idx segment 부터 반복하며 검사
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()
            snake.reset()



screen.exitonclick()