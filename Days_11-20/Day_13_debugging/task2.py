# Original problem code.
from random import randint
dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# Solution 6 is out side of the scope
# change line 4 to be 0,5 to align with the list.
# or change line 4 to be dice_num = randint(1, 6) - 1
# or change line 5 print(dice_images[dice_num-1])