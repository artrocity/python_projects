class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
            self.check_answer(user_answer, current_question.answer)
        else:
            print("You have completed this quiz challenge")
            print(f"Your final score was: {self.score}/ {self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"That's correct! The correct answer was {correct_answer}")
            self.score += 1
        else: 
            print(f"That was incorrect, the correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
