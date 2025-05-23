
wrong_guess_0 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''

wrong_guess_1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''

wrong_guess_2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''

wrong_guess_3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''

wrong_guess_4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''

wrong_guess_5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''

wrong_guess_6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

hangman_progress = {
    6: wrong_guess_0,
    5: wrong_guess_1,
    4: wrong_guess_2,
    3: wrong_guess_3,
    2: wrong_guess_4,
    1: wrong_guess_5,
    0: wrong_guess_6,
}

game_title = """
 _ 
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
        """