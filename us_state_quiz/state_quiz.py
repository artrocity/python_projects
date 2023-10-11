# Import libraries
from turtle import Turtle, Screen
import pandas as pd
from state_quiz_mechanics import Mechanics

#Set Contstants
GAME_IMAGE = "blank_states_img.gif"

# Initialize the classes
screen = Screen()
turtle = Turtle()
mechanics = Mechanics()

# Set up the screen
screen.title("Can you name all the States")
screen.addshape(GAME_IMAGE)
turtle.shape(GAME_IMAGE)

# Configure answer table for user's guesses
answer_data = pd.read_csv("50_states.csv")
states = answer_data.state.to_list()

#Start the game
while len(mechanics.correct_guesses) < 50:
    # Prompt player for a guess
    guess = mechanics.get_guess()

    if guess == "Exit":
        missing_states = [state for state in states if state not in mechanics.correct_guesses]
        new_data = pd.DataFrame(missing_states, columns=["States to Learn"])
        new_data.to_csv("States_to_Learn.csv", index=False)
        break

    # Check if guess is in 50 states
    if guess in states:
        coordinates = mechanics.get_coordinates(guess)
        mechanics.write_state(guess, coordinates)