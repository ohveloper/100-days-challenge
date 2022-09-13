import time
import turtle

import pandas
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
answer_list = []
flag = True
text_input = "Guess the State"
while len(an_answer.answer_list) < 50:
    screen.update()
    time.sleep(0.1)
    answer_state = screen.textinput(title=text_input, prompt="What's another state' name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in state_list:
            if state not in answer_list:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if (answer_state in state_list):
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        an_answer.add_answer(answer_state, x, y)
        text_input = f"{len(an_answer.answer_list)}/50 Guess the State"
        answer_list.append(answer_state)

new_data = 0
for i in answer_list:
    new_data = data[data.state != i]
    # print(answer_list)
    print(new_data)



# 화면 클릭하면 어딘지 알려주는 함수
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()