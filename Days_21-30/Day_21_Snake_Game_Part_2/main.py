from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
board = ScoreBoard()

screen.update()
speed = 0.1
direction = "r"

def go_up():
    global direction
    direction = 'u'
def go_right():
    global direction
    direction = 'r'
def go_left():
    global direction
    direction = 'l'
def go_down():
    global direction
    direction = 'd'

screen.onkeypress(go_up, 'w')
screen.onkeypress(go_right, 'd')
screen.onkeypress(go_left, 'a')
screen.onkeypress(go_down, 's')
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    sleep(speed)
    snake.move(direction)
    head = snake.head()

    # Detect collision with food
    if head.distance(food) < 15:
        snake.eat()
        food.spawn()
        board.add_score()

    # Detect collision with wall
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        game_is_on = False

    # Detect collision with tail
    if snake.collision():
        game_is_on = False

board.game_over()

screen.exitonclick()