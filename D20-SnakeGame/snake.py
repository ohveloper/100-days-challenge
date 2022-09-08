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
        print(self.segments[0].heading())
        # self.segments[0].right(90)

    # 0 > right
    # 270 > down
    # 180 > left
    # 90 > up
    def left(self):
        head = self.segments[0].heading()
        if head == 90:
            self.segments[0].left(90)
        elif head == 270:
            self.segments[0].right(90)
    def right(self):
        head = self.segments[0].heading()
        if head == 90:
            self.segments[0].right(90)
        elif head == 270:
            self.segments[0].left(90)

    def up(self):
        head = self.segments[0].heading()
        if head == 0:
            self.segments[0].left(90)
        elif head == 180:
            self.segments[0].right(90)

    def down(self):
        head = self.segments[0].heading()
        if head == 0:
            self.segments[0].right(90)
        elif head == 180:
            self.segments[0].left(90)
