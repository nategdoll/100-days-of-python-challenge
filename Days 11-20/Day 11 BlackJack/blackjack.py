from deckofcards import deck_of_cards
from random import shuffle
import os

def print_logo():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      '------'                           |__/  
          """)
    
def yes_no_question(question: str):
    answer = None

    while answer is None:
        answer = input(question).lower()

        if answer != 'y' and answer != 'n':
            print(f"{answer} is not a valid answer. Please try again.")
            answer = None

    return answer

def get_card(card):
    return card.value()

class hand_of_cards:
    def __init__(self):
        self.cards = []
        self.black_jack = False
        self.bust = False
        self.hand_value = 0

    def add_card(self, value):
        self.cards.append(value)
        self.set_hand_value()

    def set_hand_value(self):
        has_ace = False
        total_value = 0

        for card in self.cards:
            if card == 1:
                has_ace = True
            total_value += card

        if total_value <= 11 and has_ace:
            total_value += 10

        if total_value == 21:
            self.black_jack = True

        if total_value > 21:
            self.bust = True

        self.hand_value = total_value
    
    def show_hand(self, computer=False, end_game=False, computer_draw=False):
        if computer and end_game:
            print(f"Computer's final hand: {self.cards}, current score: {self.hand_value}")
        elif not computer and end_game:
            print(f"Your final hand: {self.cards}, current score: {self.hand_value}")
        elif not computer and not end_game:
            print(f"Your cards: {self.cards}, current score: {self.hand_value}")
        elif computer_draw:
            print(f"Computer's cards: {self.cards}, current score: {self.hand_value}")
        else:
            print(f"Computer's first card: {self.first_card()}")


    def black_jack_win(self):
        return self.black_jack

    def busted(self):
        return self.bust
    
    def first_card(self):
        card = self.cards[0]
        if card == 1:
            return 10 + card
        return card

def display_current_hand(your_cards, house_cards, computer_draw = False):
    your_cards.show_hand()
    house_cards.show_hand(True, False, computer_draw)

def determine_winner(your_cards, house_cards):
    your_cards.show_hand(False, True)
    house_cards.show_hand(True, True)
    if your_cards.black_jack_win():
        print(f"Black Jack, you win \U0001F600")
    elif your_cards.busted():
        print(f"You busted, you loose \U0001F614")
    elif your_cards.hand_value == house_cards.hand_value:
        print(f"Draw favors the house, you loose \U0001F614")
    elif your_cards.hand_value < house_cards.hand_value and not house_cards.busted():
        print(f"You loose \U0001F614")
    else:
        print(f"You win \U0001F600")

def game_play():
    deck = deck_of_cards
    shuffled_deck = list(deck.values())
    shuffle(shuffled_deck)

    your_cards = hand_of_cards()
    house_cards = hand_of_cards()

    # Deal out 2 cards to each player.
    for _ in range(2):
        your_cards.add_card(shuffled_deck.pop())
        house_cards.add_card(shuffled_deck.pop())

    display_current_hand(your_cards, house_cards)

    game_end = False
    if your_cards.black_jack_win():
        game_end = True
    else:
        while not game_end:
            another_card = yes_no_question("Type 'y' to get another card, type 'n' to pass:")
            if another_card == 'n':
                game_end = True
            else:
                your_cards.add_card(shuffled_deck.pop())
                if your_cards.black_jack_win() or your_cards.busted():
                    game_end = True
                display_current_hand(your_cards, house_cards)
        while not your_cards.black_jack_win() and not your_cards.busted() and not house_cards.busted() and house_cards.hand_value < 18:
            display_current_hand(your_cards, house_cards, True)
            house_cards.add_card(shuffled_deck.pop())
            print("house draws a card.")
    determine_winner(your_cards, house_cards)
    
def main():
    
    while yes_no_question("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print_logo()
        game_play()

    print(f'Thank you for playing have a good day!')

main()