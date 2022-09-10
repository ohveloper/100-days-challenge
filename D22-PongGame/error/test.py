from turtle import Turtle

# 잘 되는지 보려고 테스트로 만들어본 페이지..
# 너무너무 잘되는 상속과 아규먼트 처리,,허헣헣ㅎ....
class Test(Turtle):
    def __init__(self, x):
        super(Test, self).__init__()
        self.x = x
        print(x)
        self.shape("square")