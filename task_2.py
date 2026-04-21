def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_numbers():
    numbers = []
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except:
                print("Invalid input! Please enter a number.")
    return numbers


def get_odds(numbers):
    odds = []
    for num in numbers:
        if num % 2 != 0:
            odds.append(num)
    return odds

def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


def get_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes


numbers = get_numbers()

odds = get_odds(numbers)
evens = get_evens(numbers)
primes = get_primes(numbers)

print("\n--- RESULTS ---")

print("Odd Numbers:", odds if odds else "None found")
print("Even Numbers:", evens if evens else "None found")
print("Prime Numbers:", primes if primes else "None found")