"""
Project Euler - Problem 7 - Longest Collatz Sequence
https://projecteuler.net/problem=14

Synopsis: Find the starting number < 1,000,000 that produces that longest Collatz chain
"""


def collatz(number):
    n = number                                      # Using buffer to retain original number
    steps = 0                                       # Step counter
    while n != 1:

        if n % 2 == 0:                              # Applying the formula
            n /= 2
        else:
            n = (3 * n) + 1

        steps += 1                                  # Incrementing the step counter

    return steps


l1 = [x for x in range(1,1000001)]


longest_steps = {"number" : 0, "steps" : 0}
for idx, i in enumerate(l1):
    steps = collatz(i)
    if steps >= longest_steps["steps"]:
        longest_steps["steps"] = steps
        longest_steps["number"] = i

print(longest_steps)

# Expected Output: {'number': 837799, 'steps': 524}