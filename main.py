from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    text = (question["question"])
    answer = (question["correct_answer"])
    new_questtion = Question(text, answer)

    question_bank.append(new_questtion)



quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print(f"your final score was {quiz.score}/{quiz.question_number}")

