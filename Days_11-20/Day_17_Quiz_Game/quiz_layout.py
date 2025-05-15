class Quiz:

    def __init__(self, q_list):
        self.questions = q_list
        self.score = 0
        self.question_num = 0

    def still_has_questions(self):
        if len(self.questions) > 0:
            return True
        return False
    
    def input_answer(self, text):
        answer = None
        while answer is None:
            answer = input(f"Q.{self.question_num}: {text}: ").lower()
            if answer not in ('true', 'false'):
                print("Sorry that answer is not allowed please type 'True' or 'False'")
                answer = None
        return answer
    
    def next_question(self):
        self.question_num += 1
        question = self.questions.pop()
        answer = self.input_answer(question.text)

        if answer == question.answer:
            self.score += 1
            print(f"You got it right!")
            print(f"Your current score is: {self.score}/{self.question_num}")
        else:
            print(f"That's wrong.")
            print(f"Your current score is: {self.score}/{self.question_num}")


