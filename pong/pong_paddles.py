# Import libraries
from turtle import Turtle

# Creating Constants
UP = 90
DOWN = 270

class Paddles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.make_paddle()
        self.goto(position)

    # Positioning and creating paddles
    def make_paddle(self):
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.penup()
        
    # Move the paddle
    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
