# Import libraries
import pandas as pd
from turtle import Turtle, Screen

# Define Constants
FONT = ("Courier", 8, "normal")

#Initialize classes
screen = Screen()

class Mechanics(Turtle):
    def __init__(self):
        super().__init__()
        self.correct_guesses = []
        self.title = f"{len(self.correct_guesses)} \ 50 States Correct"

    # Obtain guess from user
    def get_guess(self):
        self.state_guess = screen.textinput(title=self.title, prompt="Guess a state's name:")
        if self.state_guess:
            return self.state_guess.title()
        else:
            return None
     
    # Get coordinates for user guess
    def get_coordinates(self, guess):
        data = pd.read_csv("50_states.csv")
        if guess in data["state"].values:
            state_data = data[data["state"] == guess]
            x_cords = state_data["x"].values[0]
            y_cords = state_data["y"].values[0]

            # Update the title for correct guesses
            self.correct_guesses.append(guess)
            self.title = f"{len(self.correct_guesses)} / 50 States Correct"
            screen.title(self.title)

            return (x_cords, y_cords)
        else:
            return None

    # Write the guess
    def write_state(self, guess, coordinates):
        state_name = Turtle(visible=False)
        state_name.penup()
        state_name.goto(coordinates)
        state_name.write(guess, align="center", font=FONT)
        screen.update()