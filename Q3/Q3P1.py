import os
import sys


def save_coordinates(path):
    ''' save all the coordinates in a set '''
    visited = set()
    x = 0
    y = 0
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
            visited.add((x, y))
    return visited


filepath = f'{os.getcwd()}/Q3/input.txt'
with open(filepath, 'r') as f:
    path_1 = f.readline().split(',')
    path_2 = f.readline().split(',')

coordinates_1 = save_coordinates(path_1)
coordinates_2 = save_coordinates(path_2)

# find matching coordinates for the paths
intersection = coordinates_1.intersection(coordinates_2)

# find closest point to origin
min_distance = sys.maxsize
for pos in intersection:
    distance = abs(pos[0]) + abs(pos[1])
    min_distance = min(distance, min_distance)
print(min_distance)
