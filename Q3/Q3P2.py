import os
import sys


def save_coordinates(path):
    ''' save all the coordinates in a set '''
    visited = {}
    x = 0
    y = 0
    counter = 0
    for move in path:
        direction = move[0]
        distance = int(move[1:])
        # add the coordinates along a direction
        for _ in range(distance):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            else:
                y -= 1

            counter += 1
            if (x, y) not in visited:
                visited[(x, y)] = counter
    return visited


filepath = f'{os.getcwd()}/Q3/input.txt'
with open(filepath, 'r') as f:
    path_1 = f.readline().split(',')
    path_2 = f.readline().split(',')

coordinates_1 = save_coordinates(path_1)
coordinates_2 = save_coordinates(path_2)

# find matching coordinates for the paths
intersection = coordinates_1.keys() & coordinates_2.keys()
print(intersection)

# find intersecting point with the least steps
min_steps = sys.maxsize
for pos in intersection:
    steps = coordinates_1[pos] + coordinates_2[pos]
    min_steps = min(steps, min_steps)
    print(steps)

print(min_steps)
