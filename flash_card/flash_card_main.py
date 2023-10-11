# Import Libraries
import random
import pandas as pd
from tkinter import *
from tkinter import messagebox

# Define Constants
BACKGROUND_COLOR = "#B1DDC6"
QUESTION_LABEL_FONT = ("Arial", 40, "italic")
QUESTION_ANSWER_FONT = ("Arial", 12, "bold")
QUESTION_FILE = "./data/js_questions.csv"
QUESTIONS_TO_LEARN = "./data/js_questions_to_learn.csv"

# Initialize the classes
root = Tk()
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Load Photos
try:
    flashcard_front = PhotoImage(file="./images/card_front.png")
    flashcard_back = PhotoImage(file="./images/card_back.png")
    correct_checkmark = PhotoImage(file="./images/right.png")
    wrong_x = PhotoImage(file="./images/wrong.png")
    program_icon = PhotoImage(file="./images/flash-card.png")
except FileNotFoundError as e:
    print("Error: ", str(e))

# Load flash card database and use pandas to read it
try:
    flashcard_data = pd.read_csv(QUESTION_FILE)
except FileNotFoundError as e:
    flashcard_data = pd.read_csv("./data/js_questions.csv")

# Create lists for questions
QUESTIONS_ANSWERED_RIGHT_LIST = []
QUESTIONS_TO_LEARN = flashcard_data.to_dict(orient="records")

# Set up the canvas for the front card(Question)
def set_card_front(question):
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=flashcard_front)
    canvas.create_text(400, 150, text="Question", fill="black", font=QUESTION_LABEL_FONT)
    canvas.create_text(400, 263, text=question, fill="black", font=QUESTION_ANSWER_FONT)

# Set up the Canvas for the back card(Answer)
def set_card_back(answer):
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=flashcard_back)
    canvas.create_text(400, 150, text="Answer", fill="white", font=QUESTION_LABEL_FONT)
    canvas.create_text(400, 263, text=answer, fill="white", font=QUESTION_ANSWER_FONT)

# Function to select a random question from the flash_card data
def get_random_question() -> str:
    return random.choice(QUESTIONS_TO_LEARN)

# Gets a new question
def get_next_question() -> str:
    global current_question
    current_question = get_random_question()
    set_card_front(current_question["Question"])

# Flips the card and shows the answer to the question
def show_answer():
    global current_question
    try:
        set_card_back(current_question["Answer"])
    except KeyError as e:
        print("The 'Answer' column is not found: ", str(e))

# Function for correct answer
def correct_answer():
    global current_question
    QUESTIONS_TO_LEARN.remove(current_question)
    QUESTIONS_ANSWERED_RIGHT_LIST.append(current_question)
    get_next_question()

# Function for wrong asnwer
def wrong_answer():
    global current_question
    wrong_answered_data = pd.DataFrame([current_question])
    wrong_answered_data.to_csv(QUESTIONS_TO_LEARN, mode="a", header=False, index=False)
    get_next_question()
    
# Chane program icon to flash card
root.wm_iconphoto(False, program_icon)

# Set up the screen
root.title("Learn Javascript")
root.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Get a random question
current_question = get_random_question()
set_card_front(current_question["Question"])
canvas.grid(row=1, column=1, columnspan=3)

# Create the buttons on the screen
wrong_button = Button(image=wrong_x, highlightthickness=0, bd=0, relief=FLAT, command=wrong_answer)
wrong_button.grid(row=2, column=1)
flip_card = Button(text="Flip Card", highlightthickness=0, bd=0, relief=FLAT, width=10, height=3, command=show_answer)
flip_card.grid(row=2, column=2)
correct_button = Button(image=correct_checkmark, highlightthickness=0, bd=0, relief=FLAT, command=correct_answer)
correct_button.grid(row=2, column=3)

print(flashcard_data.columns)
print(current_question)

# Keep screen open until closed
root.mainloop()