import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question_list in question_data:

    quest=Question(question_list["text"],question_list["answer"])
    question_bank.append(quest)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the Quiz!\nYour final score is {quiz.score}/{quiz.question_number}")




