from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # Obtain High Score
        try:
            with open('data.txt', 'r') as file:
                self.high_score = int(file.read())
        except ValueError:
            self.high_score = 0

        # Define Turtle parameters       
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)