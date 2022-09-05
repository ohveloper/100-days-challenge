from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# 질문 리스트를 만들기 위한 빈 배열
question_bank = []

# 로우 데이터를 사용에 필요한 데이터만 정제하여 question_bank에 담기 위한 반복문
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

# 정제된 질문 리스트를 담아서 새로운 객체를 생성
new_quiz = QuizBrain(question_bank)

# 퀴즈가 모두 끝날떄까지 바복하는 while loop
while new_quiz.still_has_question():
    new_quiz.next_question()

# 퀴즈를 모두 푼 이후 스코어를 알려주기 위한 변수선언
final_score = new_quiz.score
last_quiz_number = new_quiz.question_number

# 퀴즈 종료 이후 안내되는 문구
print(f"You've completed the quiz")
print(f"Your final score was: {final_score}/{last_quiz_number}")
