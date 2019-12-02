import os


def fuel_calculator_helper(mass):
    return (mass // 3) - 2


def fuel_calculator(mass):
    fuel = mass
    total = 0
    while (fuel > 0):
        fuel = max(fuel_calculator_helper(fuel), 0)
        total += fuel
    return total


filepath = f'{os.getcwd()}\Q1\input.txt'
f = open(filepath, 'r')
# calcuate total fuel cost
total = 0
for line in f:
    mass = int(line)
    total += fuel_calculator(mass)
f.close()

print(total)
