from pathlib import Path
INPUT_LETTER_TEMPLATE = "Input/Letters/starting_letter.txt"
INPUT_INVITED_NAMES = "Input/Names/invited_names.txt"
PLACEHOLDER = "[name]"
OUTPUT_DIR = "Output/ReadyToSend"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
with open(INPUT_LETTER_TEMPLATE) as letter_file:
    letter_template = letter_file.read()
    with open(INPUT_INVITED_NAMES) as names_file:
        names = names_file.readlines()
        for name in names:
            stripped_name = name.strip()
            personalized_letter = letter_template.replace(PLACEHOLDER, stripped_name)
            with open(f"{OUTPUT_DIR}/letter_for_{stripped_name}.txt", mode="w") as output_file:
                output_file.write(personalized_letter)
