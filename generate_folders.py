import os

for number in range(11, 100, 10):
    last = number + 9
    top_dir = f"Days {number}-{last}"
    os.mkdir(top_dir)
    for sub_num in range(number, last+1):
        day_dir = f"Day {sub_num}"
        os.mkdir(f"{top_dir}/{day_dir}")