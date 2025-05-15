from turtle import Turtle

UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake():
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.gen_segment(-20*i, 0)

    def gen_segment(self, x, y):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(x, y)
        self.snake.append(turtle)

    def set_direction_and_move(self, turtle, direction, current_direction):
        if direction == 'r' and current_direction != LEFT:
            turtle.setheading(RIGHT)
        elif direction == 'u' and current_direction != DOWN:
            turtle.setheading(UP)
        elif direction == 'l' and current_direction != RIGHT:
            turtle.setheading(LEFT)
        elif direction == 'd' and current_direction != UP:
            turtle.setheading(DOWN)
        turtle.forward(20)

    def head(self):
        return self.snake[0]

    def move(self, direction):
        head_x, head_y = self.snake[0].position()
        cur_direction = self.snake[0].heading()
        turtle = self.snake.pop()
        turtle.goto(head_x, head_y)
        self.set_direction_and_move(turtle, direction, cur_direction)
        self.snake.insert(0, turtle)

    def eat(self):
        tail_x, tail_y = self.snake[-1].position()
        self.gen_segment(tail_x, tail_y)
        
    def collision(self):
        for segment in self.snake[1:]:
            if self.head().distance(segment) < 10:
                return True
        return False