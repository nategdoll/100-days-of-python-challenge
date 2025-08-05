# In the movie summer wars, the protagonist was able to hear a birthday and determine the day of the week someone was born.
# This code will simulate that.

month = input("Enter the month of birth (1-12): ")
day = input ("Enter the day of birth (1-31): ")
year = input("Enter the year of birth (e.g., 1990): ")

'''
    Year Code: (YY + (YY div 4))
    Month Code: January=0, February=3, March=3, April=6, May=1, June=4, July=6, August=2, September=5, October=0, November=3, December=5
    Century Code: 0=1900s, 1=2000s,
    Date Number: 1-31
    Leap Year Code: 0 if not a leap year, 1 if a leap year
    Day of the Week: 0=Sunday, 1=Monday, ..., 6=Saturday

    Formula: (Year Code + Month Code + Century Code + Date Number - Leap Year Code) mod 7

    Results are the same for both methods.
    Results: 0-6 (0=Sunday, 1=Monday, ..., 6=Saturday)
'''

def calculate_day_of_week(month, day, year):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    month_codes = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    century_code = (int(year) // 100) - 19
    yy = int(int(year) % 100)
    year_code = yy + (yy // 4)
    leap_year_code = 0 if (int(year) % 4 != 0 or (int(year) % 100 == 0 and int(year) % 400 != 0)) else 1

    month_code = month_codes[int(month) - 1]
    date_number = int(day)

    day_of_week = (year_code + month_code + century_code + date_number - leap_year_code) % 7
    return days_of_week[day_of_week]

print("Day of the week for the given date is:", calculate_day_of_week(month, day, year))