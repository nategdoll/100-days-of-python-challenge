from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep

def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)
    return screen

def draw_middle_line():
    line = Turtle()
    line.color("white")
    line.penup()
    line.goto(0, -300)
    line.setheading(90)
    for _ in range(15):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)
    line.hideturtle()

def main():
    screen = setup_screen()
    draw_middle_line()
    
    paddle_right = Paddle(250, 0)
    paddle_left = Paddle(-250, 0)
    ball = Ball()
    scoreboard = ScoreBoard()
    
    screen.update()

    screen.listen()
    screen.onkeypress(paddle_right.go_up, "Up")
    screen.onkeypress(paddle_right.go_down, "Down")
    screen.onkeypress(paddle_left.go_up, "w")
    screen.onkeypress(paddle_left.go_down, "s")

    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

        # Detect collision with paddles
        if (ball.distance(paddle_right) < 50 and ball.xcor() > 230) or (ball.distance(paddle_left) < 50 and ball.xcor() < -230):
            ball.bounce_x()

        # Detect when ball goes out of bounds
        if ball.xcor() > 280:
            ball.reset_position()
            scoreboard.increase_score_a()

        if ball.xcor() < -280:
            ball.reset_position()
            scoreboard.increase_score_b()

        sleep(0.05)

    screen.mainloop()

if __name__ == "__main__":
    main()