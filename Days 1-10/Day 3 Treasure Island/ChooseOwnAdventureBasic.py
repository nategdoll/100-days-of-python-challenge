# Basic requirements
print(""+
      "_________|___________________|___________________|___________________|________"+
      "|___________________|___________________|___________________|___________________|________"+
      "|___________________|___________________|___________________|___________________|________"+
      "/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/"+
      "/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/"+
      "/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/"+
      "/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/"+
      "/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/"+
      "/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/ ______/"+
      "*****************************************************************************************")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = None

while direction == None:
    direction = input("You're at a cross road. Where do you want to go?\n\t\tType \"left\" or \"right\"\n").lower()
    if direction != "right" and direction != "left":
        print("Incorrect response, please try again.")
        direction = None

if direction == "left":
    decision = None

    while decision == None:
        decision = input("You've come to a lake. There is an island in the middle of the lake.\n\tType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
        if decision != "wait" and decision != "swim":
            print("Incorrect response, please try again.")
            decision = None

    if decision == "wait":
        door = None

        while door == None:
            door = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose?\n").lower()
            if door != "red" and door != "yellow" and door != "blue":
                print("Incorrect response, please try again.")
                door = None

        if door == "red":
            print("It's a room full of fire. Game Over.....")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")


