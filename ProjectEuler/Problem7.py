"""
Project Euler - Problem 7 - 10001st Prime
https://projecteuler.net/problem=7
"""

import math
import time

prime_list = [2, 3, 5, 7]
i = 8

start = time.time()
while len(prime_list) != 10001:
    if i % 2 == 0:
        i += 1
        continue
    for x in range(3, round(math.sqrt(i)) + 1):
        if i % x == 0:
            break
        if x == round(math.sqrt(i)):
            prime_list.append(i)
            break
        x += 1
    i += 1

print(next(reversed(prime_list)))
end = time.time()
print(end - start, " seconds")
