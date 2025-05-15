def is_prime(num):
    for dividen in range(2, num):
        if num % dividen == 0:
            return False
    return True

# Get all prime numbers between 2 & 100
for num in range(2, 101):
    if is_prime(num):
        print(f'{num} is a prime number.')