from base import Question
from data import questions
from functions import QuizFunctions
from header import head

print(head)
question_list = []
for question in questions:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_list.append(new_question)

quiz = QuizFunctions(question_list)

while quiz.has_questions():
    quiz.next()

print("Quiz Completed")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")