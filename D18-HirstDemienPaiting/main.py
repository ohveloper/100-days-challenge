# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_rgb_list = []
# print(colors[0].rgb)
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_rgb_list.append((r,g,b))
#
# print(color_rgb_list)

import turtle as t
import random as r

color_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]
turtle = t.Turtle()
t.colormode(255)
turtle.penup()
turtle.speed("fastest")


# 몇칸을 그릴지 작성하는 함수
def color_dot(how_many):
    for j in range(how_many):
        # 50보 옆으로 움직여서
        turtle.fd(50)
        # 닷 찍기
        turtle.dot(20, r.choice(color_list))

# 몇줄을 그릴지 작동하는 함수
def hirst_painting(how_many):
    change = -50
    start = -250
    for i in range(how_many):
        # 시작하는 지점을 매 행마다 변경
        turtle.setposition(-250, start)
        # 행에 n개의 점을 찍는 함수를 불러온다
        color_dot(how_many)
        # y축을 위로 올려준다
        start -= change


hirst_painting(10)
turtle.hideturtle()

t.exitonclick()

