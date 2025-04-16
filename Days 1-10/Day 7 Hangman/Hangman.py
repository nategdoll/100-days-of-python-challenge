from random import choice
from HangmanImages import *
from HangmanWords import words

def create_empty_string(length):
    empty_str = []
    for n in range(length):
        empty_str.append("_")
    return empty_str


word_to_guess = choice(words)
word_array = create_empty_string(len(word_to_guess))
guessed_letters = ""

win = False
guesses_left = 6
    
def print_word_to_guess():
    print(f"Word to guess: {''.join(word_array)}")

def letter_in(letter):
    if word_to_guess.find(letter) != -1:
        return True
    return False

def guess_a_letter():
    return input("Guess a letter: ").lower()

def print_lifes_left():
    global guesses_left
    print(hangman_progress[guesses_left])
    print(f'****************************{guesses_left}/6 Lives Left****************************')

def win_check():
    try:
        if word_array.index("_") < 0:
            return True
        return False
    except:
        return True

def correct_guess(letter):
    global win
    for index in range(len(word_to_guess)):
        if word_to_guess[index] == letter:
            word_array[index] = letter
    win = win_check()
    print(f"{''.join(word_array)}")
    if not win:
        print_lifes_left()

def incorrect_guess(letter):
    print(f"You guessed {letter}, that's not in the word. You losed a life.")
    global guesses_left
    guesses_left -= 1
    print_lifes_left()

print(game_title)

while not win and guesses_left > 0:
    print_word_to_guess()
    letter = guess_a_letter()
    if letter in guessed_letters:
        print(f"You already guessed {letter}, no lives lost.")
    elif letter_in(letter):
        guessed_letters += letter
        correct_guess(letter)
    else:
        guessed_letters += letter
        incorrect_guess(letter)
    

if win:
    print("CONGRADULATIONS YOU WIN!")
else:
    print(f"***********************IT WAS {word_to_guess}! YOU LOSE**********************")