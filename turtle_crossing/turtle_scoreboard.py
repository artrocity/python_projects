# Import libaries
import time
from turtle import Screen, Turtle

# Define Constants
LEVEL_FONT = ("Courier", 24, "normal")
POINT_FONT = ("Courier", 30, "normal")
ALIGNMENT = "center"
SCOREBOARD_POSITION = (-280, 260)

# Initialize classes
screen = Screen()

class Scoreboard():
    def __init__(self):
        self.user_level = 1

        self.level_turtle = Turtle(visible=False)
        self.message_turtle = Turtle(visible=False)
        self.game_over_turtle = Turtle(visible=False)
        for turtle in [self.level_turtle, self.game_over_turtle, self.message_turtle]:
            turtle.penup()
            turtle.color("black")

        self.show_level()

    # Show scoreboard
    def show_level(self):
        self.level_turtle.goto(SCOREBOARD_POSITION)
        self.level_turtle.write(f"Level: {self.user_level}", font=LEVEL_FONT)

    # Update scoreboard level
    def update_level(self):
        self.message_turtle.goto(0, -275)
        self.message_turtle.write("Good job, Level Increasing!", align=ALIGNMENT, font=POINT_FONT)
        screen.update()
        time.sleep(2)
        self.message_turtle.clear()
        self.user_level += 1
        self.level_turtle.clear()
        self.show_level()

    def game_over(self):
        self.game_over_turtle.goto(0, -275)
        self.game_over_turtle.write(f"GAME OVER, Level reached: {self.user_level}", align=ALIGNMENT, font=POINT_FONT)
        screen.update()
        
