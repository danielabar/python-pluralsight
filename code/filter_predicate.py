from math import sqrt
from pprint import pprint as pp


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# list all primes less than 100
print([x for x in range(101) if is_prime(x)])

# maps numbers with exactly 3 divisors to a tuple of those divisors
prime_square_divisors = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}
pp(prime_square_divisors)
