def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
while not at_goal():
    if wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
    else:
        turn_right()
        if not wall_in_front():
            move()
    
# Instructors Method
#while front_is_clear():
#    move()
#turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()