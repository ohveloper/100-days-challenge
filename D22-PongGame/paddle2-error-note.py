from turtle import Turtle


class Paddle(Turtle):
    # int 라고 써놔서 아무것도 되지 않았다....................
    # 몇번을 다시하고 비교하고 난리를 쳤는지.....
    # 자동완성과 내 손가락이 문제다 ㅠㅠㅠㅠ
    # 오늘의 교훈, 자동완성을 잘 활용하되 무지성으로 사용하지 말자.
    def __int__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def l_bar_up(self):
        x = self.xcor()
        y = self.ycor()
        y += 20
        self.goto(x, y)

    def l_bar_down(self):
        x = self.xcor()
        y = self.ycor()
        y -= 20
        self.goto(x, y)

    def r_bar_up(self):
        x = self.xcor()
        y = self.ycor()
        y += 20
        self.goto(x, y)

    def r_bar_down(self):
        x = self.xcor()
        y = self.ycor()
        y -= 20
        self.goto(x, y)


