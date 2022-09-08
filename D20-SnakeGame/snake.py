from turtle import Turtle
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()

    def make_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setposition(position)
            self.segments.append(new_segment)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            # 현재 세그먼트 바로 앞전 세그먼트의 x,y 값을 추출해서 현재 세그먼트의 위치를 수정
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        # 맨 앞 세그먼트를 앞으로 이동
        self.segments[0].fd(MOVE_DISTANCE)
        # self.segments[0].right(90)