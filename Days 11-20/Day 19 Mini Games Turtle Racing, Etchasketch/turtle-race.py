from turtle import Turtle, Screen, textinput
from random import choice

possible_choices = ["purple", "blue", "green", "yellow", "orange", "red"]
turtles = []
winner = None
screen = Screen()
screen.setup(width=500, height=400)

for color in possible_choices:
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    turtles.append(new_turtle)

turtle_choise = textinput("Make your bet", "Who will win the race? Enter a color")

for i, turtle in enumerate(turtles):
    turtle.setposition(-225, 100 - i * 30)

while winner is None:
    turtle = choice(turtles)
    turtle.forward(5)
    current_x, current_y = turtle.position()
    if current_x >= 230:
        winner = turtle

if winner.fillcolor() == turtle_choise:
    print(f"Congradulations {turtle_choise} won!")
else:
    print(f"You lose. The {winner.fillcolor()} is the winner.")

screen.exitonclick()