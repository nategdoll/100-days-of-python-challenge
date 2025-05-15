STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.restart()
        
    def restart(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def go_backward(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
