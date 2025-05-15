def add(*args):
    """
    Add all the numbers in the list args.
    :param args: list of numbers
    :return: sum of all numbers in args
    """
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))  # Output: 15
print(add(10, 20, 30))  # Output: 60
print(add(1.5, 2.5, 3.5))  # Output: 7.5
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Output: 55


# Kwargs
def calculate(n, **kwargs):
    """
    Calculate the value of n based on the kwargs provided.
    :param n: initial value
    :param kwargs: dictionary of operations to perform on n
    :return: final value of n after applying operations
    """
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

# Tests
print(calculate(2, add=3, multiply=5))  # Output: 25
print(calculate(10, add=5, multiply=2))  # Output: 30
print(calculate(1, add=1, multiply=10))  # Output: 20
print(calculate(0, add=0, multiply=1))  # Output: 0
print(calculate(5, add=10, multiply=0))  # Output: 0
print(calculate(3, add=2, multiply=4))  # Output: 20