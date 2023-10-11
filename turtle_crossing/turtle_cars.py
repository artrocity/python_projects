# Import libraries
import random
from turtle import Turtle

# Define constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Create car model
    def create_car(self):
        if random.randint(1, 4) == 1: 
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))  
            self.cars.append(new_car)
    
    # Create random cars for turtle to dodge
    def move_cars(self):
        for car in self.cars[:]:
            car.backward(self.car_speed)

            # Check if car went out of bounds
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    # Increase car speed
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
