from turtle import Turtle

CENTER = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=CENTER, font=FONT )

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=CENTER, font=FONT )
