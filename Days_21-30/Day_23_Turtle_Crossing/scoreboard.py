FONT = ("Courier", 12, "bold")
from turtle import Turtle

# Scoreboard class to keep track of the level
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.goto(-250, 270)
        self.level = 1
        self.hideturtle()
        self.show_level()

    def add_level(self):
        self.level = self.level + 1 
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=FONT)
