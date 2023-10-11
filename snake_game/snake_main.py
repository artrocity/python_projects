# Import libraries
from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from snake_scoreboard import Scoreboard

# Define 'Constant' for maximum level
MAX_LEVEL = 20

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# Initialize the Snake and Food class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keystrokes and move snake
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

# Initialize the game
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh_food_position()
        snake.extend_snake()
        if snake.level < MAX_LEVEL:
            snake.level += 1

    # Detect collision with wall
    if (
        snake.snake_head.xcor() < -290
        or snake.snake_head.xcor() > 290
        or snake.snake_head.ycor() < -290
        or snake.snake_head.ycor() > 290
    ):
        scoreboard.set_high_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.set_high_score()
            snake.reset_snake()

# Exit screen on click
screen.exitonclick()
