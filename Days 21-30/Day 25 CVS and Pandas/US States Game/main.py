import turtle
import pandas as pd

states_data = pd.read_csv("50_states.csv")
# Set index to first column (state names) to make it easier to access the data
states_data.set_index("state", inplace=True)
state_dictionary = states_data.to_dict(orient="index")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# How to get the coordinates of a mouse click to map the state name to the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

game_on = True
guessed_states = []
correct_guesses = 0
while game_on:
    answer_state = screen.textinput(title=f"({correct_guesses}/50) Guess the State ", prompt="What's another state's name?")
    if answer_state in state_dictionary.keys() and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        correct_guesses += 1
        x = state_dictionary[answer_state]["x"]
        y = state_dictionary[answer_state]["y"]
        # Create a turtle to write the state name on the map
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(answer_state, align="center", font=("Arial", 8, "normal"))

    elif answer_state == "Exit":
        game_on = False
