from turtle import Turtle, Screen
import random

# Initialize the screen class and size of screen
screen = Screen()
screen.setup(width=500, height=400)

# Prompt user for winner prediction
user_choice = screen.textinput(title="Turtle Race", prompt="Which turtle will win the race, choose a color: ")

# Initialize and create 6 Turtle instances
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
turtle_racers = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle])
    turtle_racers.append(new_turtle)

# Start Turtle Race
is_race_started = False
if user_choice:
    is_race_started = True

winner = None
while is_race_started:
    for turtle in turtle_racers:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

        # Check if turtle crosses the finish line
        if turtle.xcor() > 230:
            is_race_started = False
            winner = turtle.pencolor()
            break

# Display the winner
if winner:
    if winner == user_choice:
        print(f"You've won! The {winner} turtle is the winner!")
    else:
        print(f"You've lost! The {winner} turtle is the winner!")

# Screen on-click
screen.exitonclick()
