# Bare Minimum Project
    # print("Welcome to the Band Name Generator.")
    # city = input("What's the name of the city you grew up in?\n")
    # pet = input("What's your pet's name?\n")
    # print(f"Your band name could be {city} {pet}")

# Adding some spin on it.
# Instead of 2 fixed questions lets start by making it 2-3 questions.
    # In the event of 3 questions the middle one will always be a set question involving a verb.
# Then the question will be randomly selected from a set of existing question.
import random

questions = ("What's the name of the city you grew up in?\n",
             "What's your pet's name?\n",
             "What's your favorite color?\n",
             "What's your favorite animal?\n",
             "What's your favorite sport?\n",
             "What's a hobby of yours?\n")

verb_question = "What is a verb you vibe with?\n"

print("Welcome to the Band Name Generator.")
number_of_questions = random.randint(2,3)
used_questions = random.sample(questions, 2)

question_first = input(used_questions[0])

if number_of_questions == 3:
    question_verb = input(verb_question)

question_last = input(used_questions[1])

if number_of_questions == 3:
    print(f"Here are some ideas for band names:\n"+
          f"The {question_verb} {question_first} {question_last}\n"+
          f"{question_first}'s {question_verb} {question_last}\n"+
          f"{question_last}'s {question_verb} {question_first}\n")
    
else:
    print(f"Here are some ideas for band names:\n"+
          f"{question_first} {question_last}\n"+
          f"{question_last} {question_first}\n")