from turtle import Screen, Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

keep_alive = input()