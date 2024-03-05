"""
The collatz conjecture takes an initial number, and by putting the number through a
formula a number of times, will always return to one. This implementation allows the user to input a
number and will return the number of steps that it took to reach 1.
"""


def collatz(number):
    n = number  # Using buffer to retain original number
    steps = 0  # Step counter
    num_list = []  # Tracks all numbers that are calculated

    while n != 1:
        num_list.append(n)  # Appends the calculated number to the tracker

        if n % 2 == 0:  # Applying the formula
            n /= 2
        else:
            n = (3 * n) + 1

        steps += 1  # Incrementing the step counter

    answer_info = (steps, num_list)
    return answer_info  # Returns a tuple of (step count, number list)


starting_number = int(input("Input a starting number: "))
steps, highest_number = collatz(starting_number)  # Assigning variables to the returned tuple

# Print the results
print(f"The number of steps for {starting_number} to reach 1 was: {steps}")
print(f"The highest number reached during the algorithm was: {max(highest_number)}")
