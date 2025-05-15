import caesar_art
from caesar_cipher import *

def choose_encode() -> bool:
    choice = None

    while choice is None:
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

        if choice != 'encode' and choice != 'decode':
            print(f"I am sorry but {choice} is not valid please try again.")
            choice = None

    if choice == 'encode':
        return True
    return False

def choose_shift() -> int:
    try:
        return int(input("Type the shift number:\n"))
    except:
        print('An error occured the shift must be a whole number.')
        return choose_shift()
    
def choose_continue() -> bool:
    choice = None

    while choice is None:
        choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

        if choice != 'yes' and choice != 'no':
            print(f"I am sorry but {choice} is not valid please try again.")
            choice = None

    if choice == 'yes':
        return True
    return False


print(caesar_art.art_ceasar)
print(caesar_art.art_cipher)

to_continue = True

while to_continue:
    encode_choice = choose_encode()
    message = input("Type your message:\n").lower()
    shift = choose_shift()
    if encode_choice:
        print(f"Here's the encoded result: {encode(message, shift)}")
    else:
        print(f"Here's the decoded result: {decode(message, shift)}")
    to_continue = choose_continue()

print("Goodbyeencode")