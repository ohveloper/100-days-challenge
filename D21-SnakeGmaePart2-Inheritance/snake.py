from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)


    def add_snake(self, position):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setposition(position)
            self.segments.append(new_segment)

    def extend(self):
        self.add_snake(self.segments[-1].position())

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            # 현재 세그먼트 바로 앞전 세그먼트의 x,y 값을 추출해서 현재 세그먼트의 위치를 수정
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        # 맨 앞 세그먼트를 앞으로 이동
        self.segments[0].fd(MOVE_DISTANCE)
        # print(self.segments[0].heading())
        # self.segments[0].right(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
