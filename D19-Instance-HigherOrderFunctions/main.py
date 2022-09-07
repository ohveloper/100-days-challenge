from turtle import Turtle, Screen

# TODO: W = Forwards
# TODO: S = Backwards
# TODO: A = Counter-Clockwise
# TODO: D = Clockwise
# TODO: C = Clear drawing

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

class HeadControl:
    def __init__(self):
        self.heading = 0

    def counter_clockwise(self):
        self.heading += 10
        tim.setheading(self.heading)

    def clockwise(self):
        self.heading -= 10
        tim.setheading(self.heading)

# 좌, 우로 헤딩을 옮기기 위한 객체
turn = HeadControl()

# method 사용 이후 입력을 받아서 작동 시켜줌
screen.listen()

# 함수안에 함수를 호출할때는 () 쓰지 않는다. 왜? 바로 불러와지니까 , 클릭할때까지 기다리게 하기 위해
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn.counter_clockwise)
screen.onkey(key="d", fun=turn.clockwise)
screen.onkey(key="c", fun=tim.reset)
screen.exitonclick()