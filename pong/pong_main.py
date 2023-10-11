# Import the libraries
from turtle import Screen
from pong_paddles import Paddles
from pong_ball import PongBall
from pong_scoreboard import Scoreboard
import time

# Initialize the classes 
screen = Screen()
right_paddle = Paddles((350, 0))
left_paddle = Paddles((-350, 0))
ball = PongBall()
scoreboard = Scoreboard()

# Create the screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Move paddles
screen.listen()

# Move left paddle
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# Move right paddle
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# Play the game
is_game_on = True
while is_game_on:
    screen.update()
    ball.move_ball()

    # Detect top wall collision
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_ball()

    # Detect paddle collision
    if (ball.distance(left_paddle) < 40 and ball.xcor() < -340)  or (ball.distance(right_paddle) < 40 and ball.xcor() > 340):
        ball.bounce_back()

    # Detect if the ball goes out of bounds
    if ball.xcor() < -400:
        scoreboard.player2_score += 1
        scoreboard.point()
        ball.reset_ball()
        
    elif ball.xcor() > 400:
        scoreboard.player1_score += 1
        scoreboard.point()
        ball.reset_ball()

    # Update the scores
    scoreboard.update_scores()


# Close screen with click
screen.exitonclick()

