from turtle import Turtle
STYLE = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 280)
        self.refresh()


    def add_score(self):
        self.score += 1
        self.clear()
        self.refresh()
        # print(self.score)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=STYLE)


    def refresh(self):
        self.write(f"score: {self.score}", align="center", font=STYLE)
