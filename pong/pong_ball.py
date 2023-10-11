# Import libraries
from turtle import Turtle, Screen
import time

# Initialize import class
screen = Screen()

class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.make_pong_ball()
        self.x_move = 0.8
        self.y_move = 0.8

    # Create the pong ball
    def make_pong_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.speed("slow")
    
    # Move the pong ball
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bounce the ball(wall)
    def bounce_ball(self):
        self.y_move *= -1
    
    # Bounce the ball(paddle)
    def bounce_back(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
        screen.update()
        time.sleep(2)
        self.bounce_back()