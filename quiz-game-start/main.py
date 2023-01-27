from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q = Question(question["question"], question["correct_answer"])
    question_bank.append(q)

new_brain = QuizBrain(question_bank)

while new_brain.still_has_questions():
    new_brain.next_question()

