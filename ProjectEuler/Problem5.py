"""
Project Euler - Problem 5 - Smallest Multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is divisible with no remainder by all of the numbers from 1 to 20?

"""


def smallest_multiple():
    current_number = 2520
    answer_found = False
    divisors = [i for i in range(1, 21)]
    while not answer_found:  # Since we are looking for an unknown number, I am using a while loop
        for divisor in divisors:
            if current_number % divisor == 0:
                if divisor == 20:
                    answer_found = True
                    print(current_number)
                    break
                continue
            else:
                current_number += 20
                break


smallest_multiple()

# Expected Answer: 232792560