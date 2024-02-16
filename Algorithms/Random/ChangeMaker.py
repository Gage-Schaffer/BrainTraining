# Change maker using a greedy algorithm

import math

dollarAmount = float(input())

numbQuarters = math.floor(dollarAmount / .25)
dollarAmount -= round(numbQuarters * .25, 2)

dollarAmount = round(dollarAmount, 2)
numbDimes = math.floor(dollarAmount / .10)
dollarAmount -= round(numbDimes * .10, 2)

dollarAmount = round(dollarAmount, 2)
numbNickels = math.floor(dollarAmount / .05)
dollarAmount -= round(numbNickels * .05, 2
                      )
dollarAmount = round(dollarAmount, 2)
numbPennies = math.floor(dollarAmount / .01)
dollarAmount -= round(numbPennies * .01, 2)

print("Converting Change.......")
print("Number of Quarters: ", numbQuarters)
print("Number of Dimes: ", numbDimes)
print("Number of Nickels: ", numbNickels)
print("Number of Pennies: ", numbPennies)