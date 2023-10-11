import turtle as t
import random

screen = t.Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

color_list = [(226, 226, 225), (236, 236, 239), (182, 65, 34), 
              (213, 149, 97), (14, 24, 42), (230, 237, 233), (239, 208, 94), 
              (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), 
              (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), 
              (49, 52, 127), (229, 175, 161), (165, 64, 70), (167, 141, 150), (98, 113, 112), 
              (160, 168, 165), (189, 190, 196), (217, 174, 180), (15, 25, 24), (79, 70, 43), 
              (183, 196, 189), (119, 121, 147), (248, 196, 4)]

timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")

# 10 x 10 = 100 dots
for _ in range(10):
    for _ in range(10):
        # Set position left
        timmy.setheading(0)
        # Select random color
        timmy.color(random.choice(color_list))
        timmy.fillcolor(random.choice(color_list))
        # Draw dot 20 in size
        timmy.pendown()
        timmy.begin_fill()
        timmy.circle(20)
        timmy.end_fill()
        timmy.penup()
        # Move right 50
        timmy.forward(80)
    # Set position
    timmy.goto(-1, timmy.ycor() + 80)

screen.exitonclick()