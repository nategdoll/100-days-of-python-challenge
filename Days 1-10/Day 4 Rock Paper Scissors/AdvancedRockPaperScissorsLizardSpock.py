# Advanced From the minds of the writers of The Big Bang Theory.
# Comes this advanced edition of the Game.
from random import choice

player_wins = 0
computer_wins = 0
ties = 0

def print_rules():
    print('''
Rules Of the Game:
    Scissors cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    (and as it always has) Rock crushes Scissors
          ''')

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
    
def print_lizard():
    print('''

---.___________
        _______)
---.________)
     
          ''')
    
def print_spock():
    print('''
    ⌠⌒|
 ⌠⌒⌉| |   ◜﹆◜﹆
 | ||⩧|  / // /
 |_|| | /-//=/
 | || |/ // /
 ( || | // /
 |         .______
 |         __⫫____)
  |       |
          ''')

options = {
    "0": print_rock, 
    "1": print_paper,
    "2": print_scissors,
    "3": print_lizard,
    "4": print_spock
    }

wins = {
    "0": { # Rock
            "2": "Rock crushes Scissors",
            "3": "Rock crushes Lizard"
        },
    "1": { # Paper
            "0": "Paper covers Rock",
            "4": "Paper disproves Spock"
        },
    "2": { # Scissors
            "1": "Scissors cuts Paper",
            "3": "Scissors decapitates Lizard"
        },
    "3": { # Lizard
            "4": "Lizard poisons Spock",
            "1": "Lizard eats Paper"
        },
    "4": { # Spock
            "2": "Spock smashes Scissors",
            "0": "Spock vaporizes Rock"
        }
}

def players_choice():
    pick = None

    while pick == None:
        pick = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, or 4 for Spock\n")
        if pick not in options.keys():
            print(f"I am sorry but ({pick}) is not a valid option. Please try again.")
    options[pick]()
    return pick

def computer_choice():

    print("Computer choses:")
    opponent = choice(list(options.keys()))
    options[opponent]()

    return opponent

def print_outcome(winner, loser):
    print(wins[winner][loser])

def compare_choices(players, computers):
    global ties
    global player_wins
    global computer_wins

    if players == computers:
        print("Tie Game!")
        ties += 1
    elif computers in wins[players].keys():
        print_outcome(winner=players, loser=computers)
        print("You Win")
        player_wins += 1
    else:
        print_outcome(winner=computers, loser=players)
        print("You Lose")
        computer_wins += 1

def print_scoreboard():
    global ties
    global player_wins
    global computer_wins

    print(f'''
Current Scores:
    *Player   - {player_wins}
    *Computer - {computer_wins}
    *Ties     - {ties}
          ''')

def main_game():
    play_again = "y"

    while play_again == "y":
        players_move = players_choice()
        computers_move = computer_choice()
        compare_choices(players=players_move, computers=computers_move)

        print_scoreboard()
        play_again = input("Would you like to play again? enter Y for yes\n").lower()

    print("Thank you for playing have a great day!")

def main():
    menu_choice = None

    while menu_choice is None:
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print("For rules please type 0")
        print("For main game please type 1")
        menu_choice = input()

        if menu_choice != "0" and menu_choice != "1":
            print("Sorry that did not match the options.")
    
    if menu_choice == "0":
        print_rules()
        main()
    else:
        main_game()

main()