import pokedex
import os

def print_logo():
    print("""
  ___ ___ .__       .__                       /\ .____                                             
 /   |   \|__| ____ |  |__   ___________     / / |    |    ______  _  __ ___________               
/    ~    \  |/ ___\|  |  \_/ __ \_  __ \   / /  |    |   /  _ \ \/ \/ // __ \_  __ \              
\    Y    /  / /_/  >   Y  \  ___/|  | \/  / /   |    |__(  <_> )     /\  ___/|  | \/              
 \___|_  /|__\___  /|___|  /\___  >__|    / /    |_______ \____/ \/\_/  \___  >__|                 
       \/   /_____/      \/     \/        \/             \/                 \/                     
__________       __                                  ___________    .___.__  __  .__               
\______   \____ |  | __ ____   _____   ____   ____   \_   _____/  __| _/|__|/  |_|__| ____   ____  
 |     ___/  _ \|  |/ // __ \ /     \ /  _ \ /    \   |    __)_  / __ | |  \   __\  |/  _ \ /    \ 
 |    |  (  <_> )    <\  ___/|  Y Y  (  <_> )   |  \  |        \/ /_/ | |  ||  | |  (  <_> )   |  \ 
 |____|   \____/|__|_  \___  >__|_|  /\____/|___|  / /_______  /\____ | |__||__| |__|\____/|___|  / 
                     \/    \/      \/            \/          \/      \/                         \/  
    """)

def guess_a():
    answer = None
    while answer is None:
        answer = input("Who has the higher number in the pokedex? Type 'A' or 'B': ").lower()
        if answer != 'a' and answer != 'b':
            answer = None
            print('Invalid answer, please try again.')
    if answer == 'a':
        return True
    return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_play():
    total_score = 0
    game_over = False

    pokemon_db = pokedex.Original_Pokemon_Database()
    pokemon_list = pokemon_db.get_new_list()
    compare_pokemon = pokemon_list.pop()

    while len(pokemon_list) > 0 and not game_over:
        against_pokemon = pokemon_list.pop()
        print(f"Compare A: {compare_pokemon}")
        print("VS")
        print(f"Against B: {against_pokemon}")
        if guess_a():
            game_over = not pokemon_db.compare_pokemon(compare_pokemon, against_pokemon)
        else:
            game_over = not pokemon_db.compare_pokemon(against_pokemon, compare_pokemon)
            compare_pokemon = against_pokemon
        if not game_over:
            total_score += 1
            clear_screen()
            print_logo()
            print(f"You're right! Current score: {total_score}.")

    print(f"Sorry, that's wrong. Final score: {total_score}") 

print_logo()
game_play()