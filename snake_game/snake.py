# Import libraries
from turtle import Turtle, Screen

screen = Screen()

# Set up constants
STARTING_POINTS = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.snake_segments = []
        self.create_snake()
        self.user_selected_move_distance()
        self.snake_head = self.snake_segments[0]
    
    # Set up the snake, 3 'turtle' instances
    def create_snake(self):
        for position in STARTING_POINTS:
            self.add_segment(position)

    # Reset the snake
    def reset_snake(self):
        for segment in self.snake_segments:
            segment.goto(1000,1000)
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]
    
    # Add segment to snake
    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snake_segments.append(new_snake)
    
    # Extend the snake
    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())
    
    # User selected level for move distance
    def user_selected_move_distance(self):
        while True:
            try:
                self.user_choice = screen.textinput(title="Select a level", prompt="Please select a level from 1-20")
                self.level = int(self.user_choice)
                if 1 <= self.level <= 20:
                    # Ensure initial move distance doesn't exceed 19
                    self.level = min(self.level, 19)
                    return self.level
                else:
                    pass
            except Exception as e:
                print("Please enter a number only: ", str(e))
    
    # Increase level
    def increase_level(self):
        self.level += 1
                
    # Move snake
    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(20)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)
    
    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
         self.snake_head.seth(LEFT)