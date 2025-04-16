# Enhanced Version.
# Every possible failure should give you a chance to survive.
# If you survice go back to the previous choice and try again.
# Since we give them a chance to survive we also want a chance that the treasure is a mimic.
from random import randint

# If you are rolling to survive you need a 4.
# If you are rolling to see if the chest is a mimic you only need above a 1.
def roll_for_survival(failure_message:str, survive_message:str, progress, chest:bool = False):
    roll = randint(1, 4)
    if roll == 4 or (chest and roll != 1):
        if survive_message is not None:
            print(survive_message)
        progress()
    else:
        end_game_death(failure_message)

def end_game_life():
    print("Congradulations you found the treasure!!")
    print(" You WIN!! Thank you for playing.")

def end_game_death(death):
    print(death)
    print("Game Over, Thank you for playing.")

def door_decision():
    door = None

    while door == None:
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose?\n").lower()
        if door != "red" and door != "yellow" and door != "blue":
            print("Incorrect response, please try again.")
            door = None

    if door == "red":
        roll_for_survival(failure_message="It's a room full of fire.", 
                          survive_message="The room you entered was full of fire.\n As you enter a strange light comes down around you and protects you. Maybe you should try another door.", 
                          progress=door_decision)
    elif door == "yellow":
        roll_for_survival(failure_message="You found a Chest!\nHowever, when you walk towards it you realize to late.....\nIT'S A MIMIC!", 
                          survive_message=None, 
                          progress=end_game_life,
                          chest=True)
    else:
        roll_for_survival(failure_message="You enter a room of beasts.", 
                          survive_message="As you start to open the blue door, you can hear growling behind the door. Maybe you should choose a different door.", 
                          progress=door_decision)

def lake_decision():
    decision = None

    while decision == None:
        decision = input("You've come to a lake. There is an island in the middle of the lake.\n\tType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
        if decision != "wait" and decision != "swim":
            print("Incorrect response, please try again.")
            decision = None

    if decision == "wait":
        door_decision()

    else:
        roll_for_survival(failure_message="You get attacked by an angry trout.", 
                          survive_message="You start swimming, but after 5 minutes the shore of the island doesn't seem to get any closer. You turn and go back.", 
                          progress=lake_decision)

def cross_road_decision():
    decision = None

    while decision == None:
        decision = input("You're at a cross road. Where do you want to go?\n\t\tType \"left\" or \"right\"\n").lower()
        if decision != "right" and decision != "left":
            print("Incorrect response, please try again.")
            decision = None

    if decision == "left":
        lake_decision()
    else: 
        roll_for_survival(failure_message="You fell into a hole.", 
                          survive_message="There was a hole in the road. You nearly fell in but barely survived. You head back to the cross road.", 
                          progress=cross_road_decision)
        

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/ _______
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross_road_decision()