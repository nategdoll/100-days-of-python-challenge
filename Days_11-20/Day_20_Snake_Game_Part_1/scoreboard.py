from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.hideturtle()
        self.show_score()

    def add_score(self):
        self.score = self.score + 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Times New Roman", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Times New Roman", 12, "normal"))