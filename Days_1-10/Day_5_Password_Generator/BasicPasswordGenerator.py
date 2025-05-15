# Basic requirements creating password generator
from random import choice, randint, sample, shuffle
print("Welcome to the PyPassword Generator!")

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=')
numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

def choose_int() -> int:
    try:
        value = int(input())
        return value
    except:
        print("An issue occured with your input please try typing just a whole number.")

print("How many letters would you like in your password?")
num_letters = choose_int()

print("How many symbols would you like in your password?")
num_sympols = choose_int()

print("How many numbers would you like in your password?")
num_numbers = choose_int()

generated_characters = []
generated_password = ""

def pick_value(selection_list, is_letter):
    if is_letter:
        if randint(0, 1) == 1:
            return choice(selection_list).upper()
    return choice(selection_list)

for number in range(0, num_letters):
    generated_characters.append(pick_value(letters, True))

for number in range(0, num_sympols):
    generated_characters.append(pick_value(symbols, False))

for number in range(0, num_numbers):
    generated_characters.append(pick_value(numbers, False))
    
print(generated_characters)
random_generated_characters = sample(generated_characters, len(generated_characters))
print(random_generated_characters)
generated_password = "".join(random_generated_characters)
print(f"Your password is: {generated_password}")

# Alternative
#print(generated_characters)
#shuffle(generated_characters)
#print(generated_characters)
#print(f"Your password is: {"".join(random_generated_characters)}")