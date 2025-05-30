import pandas as pd

nato = pd.read_csv("Days_21-30/Day_30_Update_Password_Manager/Challenge1/nato.csv")
# Create a dictionary from the DataFrame for quick lookup
nato_alphabet = {row.letter.lower(): row.code for (index, row) in nato.iterrows()}

# Prompt the user for a word and convert it to lowercase
def request_word():
    try:
        word = input("Enter a word: ").lower()
        nato_list = [nato_alphabet[letter] for letter in word]
        print(nato_list)
    except:
        print(f"Sorry, only letters in the alphabet are allowed. \nPlease try again.")
        return request_word()
    
# Main function to run the program
request_word()