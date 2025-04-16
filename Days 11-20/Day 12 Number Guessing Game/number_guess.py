from random import randint

def print_logo():
    print("""
  ________                            ___________.__            _______               ___.                 
 /  _____/ __ __   ____   ______ _____\__    ___/|  |__   ____  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ |    |   |  |  \_/ __ \ /   |   \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \  |    |   |   Y  \  ___//    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > |____|   |___|  /\___  >____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                \/     \/        \/            \/    \/     \/     
    """)

number_to_guess = randint(1, 100)
number_of_guesses = 0

def check_answer(guess):
    global number_to_guess
    global number_of_guesses

    if guess == number_to_guess:
        print(f"You got it! The answer was {guess}.")
        return True
    elif guess < number_to_guess:
        print(f"Too low.")
    else:
        print(f"Too high.")
    number_of_guesses -= 1
    return False

def difficulty():
    global number_of_guesses
    choise = None

    while choise is None:
        choise = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if choise != 'easy' and choise != 'hard':
            print('Incorrect option dectected please try again.')
            choise = None

    if choise == 'easy':
        number_of_guesses = 10
    else:
        number_of_guesses = 5

def game_play():
    global number_of_guesses
    
    try:
        won = False
        while number_of_guesses > 0 and not won:
            print(f'You have {number_of_guesses} attempts remaining to guess the number.')
            guess = int(input('Make a guess: '))
            won = check_answer(guess)
        if not won:
            print("You've run out of guesses. I am sorry you loose.")

    except:
        print('An error occured please try again.')
        game_play()

print_logo()
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
difficulty()
game_play()