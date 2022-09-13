import time
import turtle
import pandas as pd
from answer_turtle import AnswerTutle

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
an_answer = AnswerTutle()
screen.tracer(0)


data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()
print(state_list)
# print(data)

flag = True
text_input = "Guess the State"
while len(an_answer.answer_list) < 50:
    screen.update()
    time.sleep(0.1)
    answer_state = screen.textinput(title=text_input, prompt="What's another state' name?").title()
    if (answer_state in state_list):
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        an_answer.add_answer(answer_state, x, y)
        text_input = f"{len(an_answer.answer_list)}/50 Guess the State"


# 화면 클릭하면 어딘지 알려주는 함수
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()