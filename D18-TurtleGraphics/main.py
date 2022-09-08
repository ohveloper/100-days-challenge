# 이 방식도 한번만 호출 하는것 이라면 가급적 사용하지 말자.
# 중간에 작성된 코드의 혼란을 막기 위해서
# from turtle import Turtle, Screen

# alias 활용
import turtle as t
import random as r
# import heroes

# 모듈에 담겨있는 모것을 임포트 할수 있음
# 단점은 어디서 import된 것인지 알수 없다는것!
# 사용하지 말자
# from turtle import *

tim = t.Turtle()
tim.shape("turtle")
# tim.hideturtle()
tim.color("purple1")

# challenge 1 : make square
# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)

# challenge 2 : make 점선
# flag = -1
# for _ in range(15):
#     if flag == -1:
#         tim.pencolor("black")
#     else:
#         tim.pencolor("white")
#     tim.fd(10)
#     flag *= -1

# 문서를 꼼꼼히 읽어보자.
# 요구 조건을 꼼꼼히 살피자
# for _ in range(15):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()

# challenge 3 : 삼각형 ~ 10각형까지 도형을 순서대로 각각 다른 색상으로 그린다.
# circle = 360
# for i in range(3,11):
#     angle = circle / i
#     pen_color = (r.random(), r.random(), r.random())
#     for _ in range(i):
#         tim.pencolor(pen_color)
#         tim.right(angle)
#         tim.fd(100)

# challenge 4 : Draw a Random Walk
# 선 더 굵게, 더 빠르게

# turn = [0, 90, 180, 270] # 360을 0으로 바꾸자
# tim.speed(0)
# tim.pensize(10)
# for _ in range(300):
#     pen_color = (r.random(), r.random(), r.random())
#     print(pen_color)
#     tim.pencolor(pen_color)
#     tim.fd(20)
#     tim.setheading(r.choice(turn))


# challenge 5 : 튜플 활용해서 r,g,b 컬러 생성하는 함수 만들자.
# tim.speed(0)
# tim.pensize(10)
# t.colormode(255)
# def random_color():
#     red = r.randint(0, 255)
#     green = r.randint(0, 255)
#     blue = r.randint(0, 255)
#     return (red, green, blue)
# #
# def random_work(how_many_work):
#     turn = [0, 90, 180, 270]
#     for _ in range(how_many_work):
#         pen_color = random_color()
#         tim.pencolor(pen_color)
#         tim.fd(20)
#         tim.setheading(r.choice(turn))
#
# random_work(400)

# challenge 6 : Make a Spirograph

t.colormode(255)
def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return (red, green, blue)

tim.speed("fastest")
tim.pensize(1)

def draw_spirograph(gap):
    for i in range(0, 360, gap):
        tim.pencolor(random_color())
        tim.circle(120, 360)
        tim.setheading(i)

draw_spirograph(10)






screen = t.Screen()
screen.exitonclick()
