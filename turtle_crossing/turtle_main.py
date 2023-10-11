# Import libraries
import time
from turtle import Screen
from turtle_player import Player
from turtle_cars import CarManager
from turtle_scoreboard import Scoreboard

# Initialize classes
screen = Screen()
screen.tracer(0) # Removes animations in the beginning as units are taking their places
player = Player()
scoreboard = Scoreboard()
cars = CarManager()

# Set up the screen
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Move the turtle
screen.listen()
screen.onkey(player.move_up, "Up")

# Play the game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Turtle Completes level
    if player.ycor() > 310:
        scoreboard.update_level()
        player.reset_position()
        cars.increase_speed()

    for car in cars.cars:
        if player.distance(car) < 20: 
            game_is_on = False
            scoreboard.game_over()

# Exit the screen on click
screen.exitonclick()
        
        
