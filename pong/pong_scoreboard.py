# Import libraries
from turtle import Turtle

# Define Constants
LEFT_SCOREBOARD_POSITION = (-300, 280)
RIGHT_SCOREBOARD_POSITION = (300, 280)
POINT_POSITION = (0, 50)
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 20, "normal")
POINT_FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        
    # Create a scoreboard    
    def create_scoreboard(self, position):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)

    # Make a left scoreboard
    def left_scoreboard(self):
        self.create_scoreboard(LEFT_SCOREBOARD_POSITION)
        self.write(f"Player Score: {self.player1_score}", align=ALIGNMENT, font=SCORE_FONT)
        
    # Make a right scoreboard  
    def right_scoreboard(self):
        self.create_scoreboard(RIGHT_SCOREBOARD_POSITION)
        self.write(f"Player Score: {self.player2_score}", align=ALIGNMENT, font=SCORE_FONT)

    def point(self):
        self.color("white")
        self.penup()
        self.goto(POINT_POSITION)
        self.write("POINT", align=ALIGNMENT, font=POINT_FONT)

    def update_scores(self):
        self.clear()
        self.left_scoreboard()
        self.right_scoreboard()