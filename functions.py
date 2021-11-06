class QuizFunctions:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def has_questions(self):
        return self.question_number < len(self.question_list)

    def next(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check(user_answer, current_question.answer)

    def check(self, user, correct):
        if user.lower() == correct.lower():
            self.score += 1
            print("You are right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
