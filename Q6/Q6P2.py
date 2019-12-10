import os
import collections


def bfs(graph, start, end):
    queue = collections.deque()
    visted = set()
    distance = {}

    distance[start] = 0
    visted.add(start)
    queue.append(start)
    while (queue):
        current = queue.popleft()
        if current == end:
            return distance[current]

        for child in graph[current]:
            if child not in visted:
                distance[child] = distance[current] + 1
                queue.append(child)
                visted.add(child)

    raise Exception('NOT FOUND')


filepath = f'{os.getcwd()}/Q6/input.txt'
with open(filepath, 'r') as f:
    data = f.read().splitlines()

# build graph
YOU, SANTA = None, None
graph = {}
for orbit in data:
    a, b = orbit.split(')')
    # init child arrays if needed
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    # add children
    graph[a].append(b)
    graph[b].append(a)

    # track out starting locations
    if b == 'YOU':
        YOU = a
    if b == 'SAN':
        SANTA = a

distance = bfs(graph, YOU, SANTA)

print(distance)
