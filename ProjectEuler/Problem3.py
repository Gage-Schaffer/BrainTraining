"""
Project Euler - Problem 3 - Largest Prime Factor

The prime factors of $13195$ are 5, 7, 13 and 29
What is the largest prime factor of the number 600851475143?

"""

import math
x = 600851475143


# Getting a list of all prime numbers up to sqrt(x) for reference to later
def sieve_of_eratosthenes():
    l1 = [i for i in range(2, math.ceil(math.sqrt(x)))]
    prime_list = []




