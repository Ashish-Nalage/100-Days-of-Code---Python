from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.goto(-260,270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
