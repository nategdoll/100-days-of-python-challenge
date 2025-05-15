from turtle import Screen, Turtle
from random import randint

length = 100

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
for sides in range(3, 11):
    angle = 0
    red = float(randint(0, 255)/255.0)
    green = float(randint(0, 255)/255.0)
    blue = float(randint(0, 255)/255.0)
    timmy_the_turtle.pencolor(red,green,blue)
    turn = 360/sides
    while angle < 360:
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(turn)
        angle += turn


keep_alive = input()