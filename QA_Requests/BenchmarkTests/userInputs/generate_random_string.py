import random
import string

chars = string.ascii_lowercase + string.digits
random_string = ''.join(random.choices(chars, k=6))
N = 10
random_number = random.randint(100,19999)

def fetch_random_string():
    return random_string

def fetch_phone_number():
    min = pow(10, N - 1)
    max = pow(10, N) - 1
    return str(random.randint(min, max))

def fetch_random_digit():
    return str(random_number)

