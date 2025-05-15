from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

keys = {"w": False, "s": False, "a": False, "d": False}

def move():
    if keys["w"]:
        pen.forward(10)
    if keys["s"]:
        pen.backward(10)
    if keys["a"]:
        pen.left(5)
    if keys["d"]:
        pen.right(5)
    screen.ontimer(move, 50)  # Call move every 50 milliseconds

def key_press(key):
    keys[key] = True

def key_release(key):
    keys[key] = False

screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")
screen.onkeyrelease(lambda: key_release("s"), "s")
screen.onkeypress(lambda: key_press("a"), "a")
screen.onkeyrelease(lambda: key_release("a"), "a")
screen.onkeypress(lambda: key_press("d"), "d")
screen.onkeyrelease(lambda: key_release("d"), "d")

screen.listen()
move()
screen.exitonclick()