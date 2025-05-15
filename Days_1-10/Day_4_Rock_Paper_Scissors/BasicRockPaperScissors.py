# Basic requirements
from random import choice

def print_rock():
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    
def print_paper():
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')  
    
def print_scissors():
    print('''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)      
          ''')

options = {
    "0": print_rock, 
    "1": print_paper,
    "2": print_scissors
    }

pick = None
while pick == None:
    pick = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

    if pick not in options.keys():
        print(f"I am sorry but ({pick}) is not a valid option. Please try again.")

options[pick]()

print("Computer choses:")

opponent = choice(list(options.keys()))
options[opponent]()

if pick == opponent:
    print("It's a tie!")
elif ((pick == "0" and opponent == "2") or # Rock Crushes Scissors
      (pick == "1" and opponent == "0") or # Paper Covers Rock
      (pick == "2" and opponent == "1")): # Scissors Cuts Paper
    print("You Win")
else:
    print("You Loose")