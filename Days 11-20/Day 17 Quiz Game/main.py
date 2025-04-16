from question_model import Question
from questions_answers import question_data
from quiz_layout import Quiz
from grade import LetterGrade

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"].lower()
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

letter_grade = LetterGrade(quiz.score, quiz.question_num)
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_num}")
print(f"Which gives a percent of {letter_grade.score:.2f} and a letter grade of {letter_grade.letter}")