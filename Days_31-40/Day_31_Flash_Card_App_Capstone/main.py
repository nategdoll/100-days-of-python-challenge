import tkinter as tk
from tkinter import messagebox
import pandas as pd
from random import choice

# ---------------------------- CONSTANTS ------------------------------- #
FOLDER_PATH = "Days_31-40/Day_31_Flash_Card_App_Capstone"
FLASH_CARD_FILE = f"{FOLDER_PATH}/data/german_english.csv"
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_IMG = f"{FOLDER_PATH}/images/card_front.png"
CARD_BACK_IMG = f"{FOLDER_PATH}/images/card_back.png"
RIGHT_IMG = f"{FOLDER_PATH}/images/right.png"
WRONG_IMG = f"{FOLDER_PATH}/images/wrong.png"

german_data = pd.read_csv(FLASH_CARD_FILE)
german_flash_cards = {row.German: row.English for (index, row) in german_data.iterrows()}
current_card = ()

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card
    current_card = choice(list(german_flash_cards.items()))
    canvas.itemconfig(title, text="German", fill="black")
    canvas.itemconfig(word, text=current_card[0], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    show_btn.config(text="Show Answer", command=show_answer)
    show_btn.grid(column=1, row=1)
    wrong_btn.grid_forget()
    right_btn.grid_forget()

def show_answer():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card[1], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)
    show_btn.grid_forget()
    wrong_btn.grid(column=0, row=1)
    right_btn.grid(column=2, row=1)

def correct_answer():
    global current_card
    if current_card in german_flash_cards.items():
        del german_flash_cards[current_card[0]]
    next_card()

def incorrect_answer():
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas for Flash Card
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file=CARD_FRONT_IMG)
card_back_img = tk.PhotoImage(file=CARD_BACK_IMG)
card_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")
canvas.grid(column=1, row=0)

# Buttons
wrong_btn_img = tk.PhotoImage(file=WRONG_IMG)
wrong_btn = tk.Button(image=wrong_btn_img, command=incorrect_answer, highlightthickness=0)
wrong_btn.grid(column=0, row=1)
wrong_btn.grid_forget()

right_btn_img = tk.PhotoImage(file=RIGHT_IMG)
right_btn = tk.Button(image=right_btn_img, command=correct_answer, highlightthickness=0)
right_btn.grid(column=2, row=1)
right_btn.grid_forget()

show_btn = tk.Button(padx=10, pady=10, text="Start", font=("Arial", 20), bg="lime", command=next_card, highlightthickness=0)
show_btn.grid(column=1, row=1)

window.mainloop()