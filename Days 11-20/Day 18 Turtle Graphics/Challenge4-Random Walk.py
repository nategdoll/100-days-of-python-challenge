from turtle import Screen, Turtle
from random import randint, choice

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

def choose_color():
    red = float(randint(0, 255)/255.0)
    green = float(randint(0, 255)/255.0)
    blue = float(randint(0, 255)/255.0)
    return (red, green, blue)

def choose_direction():
    DIRECTIONS = (0, 90, 180, 270)
    return choice(DIRECTIONS)

length = 10
for _ in range(100):
    timmy_the_turtle.pencolor(choose_color())
    timmy_the_turtle.right(choose_direction())
    timmy_the_turtle.forward(length)


keep_alive = input()