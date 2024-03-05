"""
Project Euler - Problem 16 - Power Digit Sum
https://projecteuler.net/problem=16

Synopsis: What is the sum of the digits that make up 2**1000
"""

# Need to store this number as a string to prevent overflow
long_number_str = str(2 ** 1000)


def sum_digits(number_str):
    sum = 0
    for digit in long_number_str:
        sum += int(digit)
    return sum


print(sum_digits(long_number_str))

# Expected Output: 1366
