# Import Libraries
from tkinter import *
from quiz_brain import QuizBrain

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        # Initalize class
        self.root = Tk()
        self.brain = quiz_brain
        # Set Font
        self.FONT = ("Courier", 24, "normal")

        # Initialize class methods
        self.load_photos()
        self.set_file_icon()
        self.setup_screen()
        self.set_score()
        self.setup_screen_buttons()

    # Load the photos
    def load_photos(self) -> None:
        try:
            self.check_mark_image = PhotoImage(file="./images/true.png")
            self.x_image = PhotoImage(file="./images/false.png")
            self.icon_image = PhotoImage(file="./images/quiz_ico.png")
        except FileNotFoundError as e:
            print("Error: ", str(e))

    # Set the file icon
    def set_file_icon(self) -> None:
        self.root.wm_iconphoto(False, self.icon_image)

    # Set up the screen
    def setup_screen(self) -> None:
        self.root.title("Can you beat this quiz?")
        self.root.config(width=500, height=700)
        self.root.config(padx=50, pady=50)
        self.canvas = Canvas(width=400, height=400, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

    # Add Score Label
    def set_score(self) -> None:
        self.score_label = Label(text="Score: 0", font=self.FONT)
        self.score_label.grid(row=0, column=0, columnspan=2)

    # Add Buttons
    def setup_screen_buttons(self) -> None:
        self.check_mark_button = Button(image=self.check_mark_image, highlightthickness=0, command=self.true_pressed)
        self.check_mark_button.grid(row=2, column=0)
        self.x_button = Button(image=self.x_image, highlightthickness=0, command=self.false_pressed)
        self.x_button.grid(row=2, column=1)

    # When user selects the Check Mark Button
    def true_pressed(self) -> str:
        self.handle_user_answer("True")

    # When user select the 
    def false_pressed(self) -> str:
        self.handle_user_answer("False")

    # Checks user answer via the QuizBrain Class
    def handle_user_answer(self, user_answer:str) -> None:
        is_correct = self.brain.check_quesiton_answer(user_answer)
        if is_correct:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.brain.score}")
        else:
            self.canvas.config(bg="red")

        self.root.update_idletasks()
        self.root.after(1000, self.display_next_question())

    # Displays the current question
    def display_question(self, question_text: str) -> None:
        self.canvas.delete("question")
        self.canvas.create_text(
            200,
            200,
            text=question_text,
            font=self.FONT,
            width=350,
            tag="question",
            fill="black",
        )

    # Display the next question
    def display_next_question(self) -> None:
        self.canvas.config(bg="white")

        if self.brain.still_has_questions():
            question = self.brain.get_question()
            self.display_question(question)
        else:
            self.canvas.delete("question")
            self.canvas.create_text(
                200,
                200,
                text=f"You finished, You're score was {self.brain.score}!",
                font=self.FONT,
                width=350,
                tag="question",
                fill="black"
            )

    # Updates the question
    def update_question(self) -> None:
        if self.brain.still_has_questions():
            question = self.brain.get_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            #Show Current Score out of Possible Score(len questions list)
            pass

    def root_tk_loop(self) -> None:
        # Keep the window open until closed
        self.root.mainloop()