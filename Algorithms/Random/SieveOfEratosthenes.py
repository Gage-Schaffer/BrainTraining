"""
The Sieve of Eratosthenes is an algorithm that is useful for finding prime numbers for up to a given limit.

This program takes an upper-bound and returns a list of all prime number below that number.
"""
import math

upper_bound = int(input("Type in the upper limit: "))


def sieve(upper_bound):
    l1 = [True for x in range(2, upper_bound)]
    for i in range(0, math.ceil(math.sqrt(upper_bound))):
        if l1[i] == True:
            pass


sieve(upper_bound)
