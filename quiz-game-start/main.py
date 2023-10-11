from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Write a for loop ot iterate over the question_data.
question_bank = []
for item in range(len(question_data)):
    text = question_data[item]["text"]
    answer = question_data[item]["answer"]
    question = Question(text, answer)
    question_bank.append(question)    


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

