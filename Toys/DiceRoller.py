"""
Takes an input such as "2d6", which then returns dice rolls.
The syntax of the roll is "*number of dice* d *number of sides*"

"""
import random


def roll_dice():
    user_input = input("Enter Dice Roll: ")
    dice, _, sides = user_input.partition("d")
    if _ == "" or sides == "":  # Check Input and return if the usage is wrong
        print("Usage: '2d6'")
        return
    results = []
    for i in range(int(dice)):
        roll_result = random.randint(1, int(sides))
        results.append(roll_result)

    return results


print(roll_dice())
