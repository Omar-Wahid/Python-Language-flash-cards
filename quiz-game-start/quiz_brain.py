class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}. {question.text}? true or false: ")
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, right_answer):
        if answer.lower() == right_answer.lower():

            self.score += 1
            print(f"that's right, score is {self.score}")
        else:
            print("wrong, idiot!")
