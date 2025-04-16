from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_track = 3
        self.speed(self.speed_track)
        self.random_direction()

    def random_direction(self):
        self.x_move = randint(-15, 15)
        self.y_move = randint(-10, 10)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def speed_up(self):
        self.speed_track += 1
        self.speed(self.speed_track)

    def bounce_y(self):
        self.y_move *= -1
        self.speed_up()

    def bounce_x(self):
        self.x_move *= -1
        self.speed_up()

    def reset_position(self):
        self.goto(0, 0)
        self.speed(40)
        self.random_direction()