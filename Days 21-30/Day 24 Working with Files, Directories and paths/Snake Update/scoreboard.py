from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.high_score = self.get_high_score()
        self.new_hs_flag = False
        self.hideturtle()
        self.show_score()

    def add_score(self):
        self.score = self.score + 1
        self.check_new_high_score()
        self.show_score()

    def get_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except:
            return 0

    def check_new_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_hs_flag = True

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score},\tHigh Score: {self.high_score}", False, align="center", font=("Times New Roman", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Times New Roman", 12, "normal"))
        if self.new_hs_flag:
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))