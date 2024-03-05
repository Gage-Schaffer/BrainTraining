"""
Project Euler - Problem 15 - Lattice Paths
https://projecteuler.net/problem=15

Synopsis: How many lattice paths are in a 20x20 grid
"""
import math

grid_x = 20
grid_y = 20


def binomial_coefficient(x, y):
    """
    https://mathworld.wolfram.com/LatticePath.html

    We can solve for the number of Lattice Paths on a grid by
    using the binomial coefficient C(a + b, a) which simplifies
    to (a + b)! / a! * ((a + b) - a)!
    or, in the actual formula
    n! / k! * (n - k)!
    """
    n = x + y
    k = x
    calc = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    print(calc)


binomial_coefficient(grid_x, grid_y)

# Expected Output: 137846528820
