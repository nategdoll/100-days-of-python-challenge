from turtle import Screen, Turtle
from random import randint

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.speed("fastest")

def choose_color():
    red = float(randint(0, 255)/255.0)
    green = float(randint(0, 255)/255.0)
    blue = float(randint(0, 255)/255.0)
    return (red, green, blue)

for _ in range(72):
    timmy_the_turtle.pencolor(choose_color())
    timmy_the_turtle.circle(100, 360, 360)
    timmy_the_turtle.right(5)


screen = Screen()
screen.exitonclick()