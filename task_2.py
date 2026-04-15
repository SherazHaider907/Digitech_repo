# get odd numbers
def get_odds(numbers):
    odds = []
    for num in numbers:
        if num % 2 != 0:
            odds.append(num)
    return odds

# get even numbers
def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

# get prime numbers
def get_primes(numbers):
    primes = []
    
    for num in numbers:
        if num <= 1:
            continue  
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# Taking input

numbers = []
for i in range(10):
    numbers.append(int(input("Enter number: ")))


# Calling functions
odds = get_odds(numbers)
evens = get_evens(numbers)
primes = get_primes(numbers)

# Printing results
print("\n--- Results ---")

print("Odd Numbers:", odds if odds else "None found")
print("Even Numbers:", evens if evens else "None found")
print("Prime Numbers:", primes if primes else "None found")