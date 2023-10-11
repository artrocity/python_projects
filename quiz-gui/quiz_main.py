# Import Libraries
from quiz_ui import QuizUI
from quiz_brain import QuizBrain

#Define Constants

# Initialize Classes
brain = QuizBrain()
ui = QuizUI(quiz_brain=brain)

# Play the quiz game
ui.display_next_question()

# Keep Window open until user closes it
ui.root_tk_loop()

