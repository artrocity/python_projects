# Import Libraries
import requests
import html
import random

# Set up Quiz Brain Class
class QuizBrain:
    def __init__(self) -> None:
        self.question_list =  []
        self.score = 0
        self.current_question = None
        self.get_data()

    # Check to see if there are still questions in the list
    def still_has_questions(self) -> bool:
        return len(self.question_list) > 0
        
    # Import API data and store data in a variable
    def get_data(self):
        self.quiz_response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
        self.quiz_response.raise_for_status()
        self.data = self.quiz_response.json()
        self.question_list = self.data["results"]
        
    # Get a random question and answer
    def get_question(self):
        self.current_question = random.choice(self.question_list)
        self.question_list.remove(self.current_question)
        print(self.current_question)
        return html.unescape(self.current_question["question"])

    def check_quesiton_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question["correct_answer"]
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False