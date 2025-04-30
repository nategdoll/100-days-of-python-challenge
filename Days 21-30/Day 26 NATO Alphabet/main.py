import pandas as pd
nato = pd.read_csv("nato.csv")
nato_alphabet = {row.letter.lower(): row.code for (index, row) in nato.iterrows()}

word = input("Enter a word: ").lower()
nato_list = [nato_alphabet[letter] for letter in word if letter in nato_alphabet]
print(nato_list)