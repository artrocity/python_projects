# Import Libraries
from turtle import Turtle
import random

# Food color list for snake to eat
food_color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

# Create a subclass for the snake food
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()

        # Create food
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh_food_position()

    # Refresh location after initial contact with the snake
    def refresh_food_position(self):
        self.color(random.choice(food_color_list))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)