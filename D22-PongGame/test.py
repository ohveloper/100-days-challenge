from turtle import Turtle

class Test(Turtle):
    def __init__(self, x):
        super(Test, self).__init__()
        self.x = x
        print(x)
        self.shape("square")