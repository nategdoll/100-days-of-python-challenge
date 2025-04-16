import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
level_board = Scoreboard()
character = Player()
cars = CarManager()

screen.listen()
screen.onkeypress(character.go_forward, "w")
screen.onkeypress(character.go_backward, "s")
screen.onkeypress(character.go_left, "a")
screen.onkeypress(character.go_right, "d")

screen.update()

game_is_on = True
while game_is_on:
    # Check if character is at the finish line
    if character.is_at_finish_line():
        level_board.add_level()
        character.restart()
        cars.level_up()
    # Move cars and check for collision
    if cars.move_cars_check_collision(character.position()):
        level_board.game_over()
        game_is_on = False
    # Generate new cars
    if randint(1, 10) in (1, 4, 7):
        cars.generate_car()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()