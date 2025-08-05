import smtplib
import datetime as dt
import json
from random import choice

def get_random_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    return choice(quotes).strip()

def send_birthday_email(name, to_email):
    # This function can be expanded to check a database or file for birthdays
    # For now, it will just send a birthday email
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    # Note: Make sure to enable "Less secure app access" in your Google account settings

    subject = f"Happy Birthday {name}!"
    body = "Wishing you a wonderful birthday filled with joy and happiness!"
    quote = get_random_quote()
    body += f"\n\nHere's a quote for you:\n{quote}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="",
            msg=f"Subject:{subject}\n\n{body}")

def get_birthdays():
    # This function can be expanded to read from a json file.
    with open("birthdays.json", "r") as file:
        birthdays_json = json.load(file)
        birthdays = birthdays_json.get("birthdays", {})
    return birthdays

def check_today_birthdays():
    today = dt.datetime.now()
    birthdays = get_birthdays()
    
    for birthday in birthdays:
        name = birthday.get("name")
        birthday_date = birthday.get("birthday")
        email = birthday.get("email")

        birthday_date = dt.datetime.strptime(birthday, "%Y-%m-%d")

        if birthday_date.month == today.month and birthday_date.day == today.day:
            print(f"Today is {name}'s {today.year - birthday_date.year} birthday!")
            send_birthday_email(name, email)