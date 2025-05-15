print("Welcome to the Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0

# Todo: work out how much they need to pay based on their size choice.
if size == "S":
    total += 15
elif size == "M":
    total += 20
else:
    total += 25

# Todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

# Todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}.")