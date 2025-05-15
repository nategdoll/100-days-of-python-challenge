import tkinter as tk
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import choice, randint, sample, shuffle
LETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
SYMBOLS = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=')
NUMBERS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

def pick_value(selection_list, is_letter):
    if is_letter:
        return choice(selection_list).upper()
    return choice(selection_list)

def generate_password():
    generated_characters = []

    if (num_letters := int(password_strength2_entry.get())) != "":
        for _ in range(0, num_letters):
            generated_characters.append(pick_value(LETTERS, True))
    if (num_sympols := int(password_strength3_entry.get())) != "":
        for _ in range(0, num_sympols):
            generated_characters.append(pick_value(SYMBOLS, False))
    if (num_numbers := int(password_strength4_entry.get())) != "":
        for _ in range(0, num_numbers):
            generated_characters.append(pick_value(NUMBERS, False))
    if (total_length := int(password_strength1_entry.get())) != "":
        while len(generated_characters) < total_length:
            generated_characters.append(choice(LETTERS))

    # Randomize the order of the characters
    shuffle(generated_characters)
    # Join the characters to form the password
    generated_password = "".join(generated_characters)
    password_entry.delete(0, tk.END)  # Clear the entry field
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)  # Copy the password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
PASSWORD_FILE = "Days_21-30/Day_29_Password_Manager/passwords.txt"
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showerror(title="Error", message="Please fill in all fields.")
        return

    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        messagebox.showinfo(title="Success", message="Password saved successfully.")


#----------------------------- Field Validation ------------------------------- #
def validate_num_only(char):
    return char.isdigit()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

validation = window.register(validate_num_only)

# Logo Canvas
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="Days 21-30/Day 29 Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
## Password Strength Labels
password_rule_label = tk.Label(text="Password Rules:")
password_rule_label.grid(column=0, row=4, rowspan=4)
password_strength1_label = tk.Label(text="Password Length:")
password_strength1_label.grid(column=1, row=4)
password_strength2_label = tk.Label(text="Capital Letters:")
password_strength2_label.grid(column=1, row=5)
password_strength3_label = tk.Label(text="Symbols:")
password_strength3_label.grid(column=1, row=6)
password_strength4_label = tk.Label(text="Numbers:")
password_strength4_label.grid(column=1, row=7)

# Input Fields
website_entry = tk.Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # Focus on the website entry field
email_entry = tk.Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = tk.Entry(width=34)
password_entry.grid(column=1, row=3)
## Password Strength Input Fields
password_strength1_entry = tk.Entry(width=17, validate="key", validatecommand=(validation, "%S"))
password_strength1_entry.grid(column=2, row=4)
password_strength1_entry.insert(0, "12")  # Default value for password length
password_strength2_entry = tk.Entry(width=17, validate="key", validatecommand=(validation, "%S"))
password_strength2_entry.grid(column=2, row=5)
password_strength2_entry.insert(0, "2")  # Default value for number of capital letters
password_strength3_entry = tk.Entry(width=17, validate="key", validatecommand=(validation, "%S"))
password_strength3_entry.grid(column=2, row=6)
password_strength3_entry.insert(0, "2")  # Default value for number of symbols
password_strength4_entry = tk.Entry(width=17, validate="key", validatecommand=(validation, "%S"))
password_strength4_entry.grid(column=2, row=7)
password_strength4_entry.insert(0, "2")  # Default value for number of numbers

# Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password, width=14)
generate_password_button.grid(column=2, row=3)
add_button = tk.Button(text="Add", command=save_password, width=44)
add_button.grid(column=1, row=8, columnspan=2)

window.mainloop()