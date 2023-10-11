# Import Libraries
from turtle import Turtle, Screen

# Define Constants
STARTING_POSITION = (0, -280)
STARTING_HEADING = 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Initialize classes
screen = Screen()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    # Create the turtle
    def create_player(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.seth(STARTING_HEADING)
        self.goto(STARTING_POSITION)
        self.speed("fastest")

    # Moves the turtle up along the y axis    
    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    # Reset turtle position
    def reset_position(self):
        self.goto(STARTING_POSITION)
        screen.update()
        

