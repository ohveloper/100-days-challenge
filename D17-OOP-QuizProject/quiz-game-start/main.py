from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_question():
    new_quiz.next_question()

final_score = new_quiz.score
last_quiz_number = new_quiz.question_number

print(f"You've completed the quiz")
print(f"Your final score was: {final_score}/{last_quiz_number}")
