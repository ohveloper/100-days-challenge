import time
from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_postition =[(0,0), (-20, 0), (-40, 0)]

segments = []

# 세그먼트들을 생성해서 최초 위치에 두고 위한 반복문
for position in starting_postition:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.setposition(position)
    segments.append(new_segment)

is_game_on = True

while is_game_on:
    # .tracer()로 멈췄던 애니메이션을 다시 작동 시기큰 함수
    screen.update()
    # 잠시 멈췄다가 다시 진행 시키는 함수
    time.sleep(0.1)

    # 맨뒤 뱀부터 바로 앞전 뱀위치로 옮기기 위한 반복문
    # range() 함수 뒤에서부터 카운트 하는법
    for segment_num in range(len(segments)-1, 0, -1):
        # 현재 세그먼트 바로 앞전 세그먼트의 x,y 값을 추출해서 현재 세그먼트의 위치를 수정
        new_x = segments[segment_num - 1].xcor()
        new_y = segments[segment_num - 1].ycor()
        segments[segment_num].goto(new_x, new_y)
    # 맨 앞 세그먼트를 앞으로 이동
    segments[0].fd(20)
    # segments[0].right(90)








screen.exitonclick()