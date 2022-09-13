from turtle import Turtle
STYLE = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
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

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")

        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=STYLE)

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=STYLE)
