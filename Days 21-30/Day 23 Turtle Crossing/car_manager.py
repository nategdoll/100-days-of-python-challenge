COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import randint, choice

class CarManager():
    def __init__(self):
        self.movement_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        for _ in range(3):
            self.generate_car()

    def generate_car(self):
        car = Turtle("square")
        car.color(choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        y_position = randint(-240, 240)
        car.goto(300, y_position)
        self.cars.append(car)

    def move_cars_check_collision(self, player_location):
        for car in self.cars:
            car.forward(self.movement_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
            if car.distance(player_location) < 20:
                return True
        return False

    def level_up(self):
        self.movement_speed += MOVE_INCREMENT

    