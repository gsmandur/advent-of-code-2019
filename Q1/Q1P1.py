import os


def fuel_calculator(mass):
    return (mass // 3) - 2


filepath = f'{os.getcwd()}/Q1/input.txt'
f = open(filepath, 'r')
# calcuate total fuel cost
total = 0
for line in f:
    mass = int(line)
    total += fuel_calculator(mass)
f.close()

print(total)
