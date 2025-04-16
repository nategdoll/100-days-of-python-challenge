from auction_art import print_gavel
import os

auction = {}

def get_bidder():
    global auction
    bidder = input ("What is your name?: ")
    if bidder in auction.keys():
        print(f"I am sorry but we already have a {bidder}, please try again.")
        return get_bidder()
    return bidder

def get_bid():
    try:
        return float(input("What's your bid?: $"))
    except:
        print("I am sorry but an error occure please put your bid as a whole numberic value.")
        return get_bid()

def another_bidder():
    other_bidders = None
    while other_bidders == None:
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if other_bidders != 'yes' and other_bidders != 'no':
            other_bidders = None
    if other_bidders == 'yes':
        return True
    return False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder():
    global auction
    name = ""
    high_bid = -1
    for key, value in auction.items():
        if value > high_bid:
            name = key
            high_bid = value
    print(f"The winner is Jenny with a bid of ${high_bid:.2f}.")

def main():
    global auction
    auction_continues = True

    while auction_continues:
        bidder = get_bidder()
        bid = get_bid()
        auction[bidder] = bid
        auction_continues = another_bidder()
        clear_console()

    highest_bidder()

main()