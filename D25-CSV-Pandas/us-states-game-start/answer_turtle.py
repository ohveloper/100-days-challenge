from turtle import Turtle

class AnswerTutle:
    def __init__(self):
        self.answer_list = []
        # self.answer_cnt = len(self.answer_list)

    # 정답 추가
    def add_answer(self, answer, x, y):
        new_answer = Turtle()
        new_answer.penup()
        new_answer.hideturtle()
        new_answer.goto(x,y)
        new_answer.write(answer, align="center")

        self.answer_list.append(new_answer)


