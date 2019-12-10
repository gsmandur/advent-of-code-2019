import os


def calculate_orbits(tree, root):
    if root == None:
        return 0, 0
    if root not in tree:
        # leaf node if no children exist
        return 1, 0
    count = 0
    sum = 0
    print(f'child = {tree[root]}')
    for child in tree[root]:
        cur_count, cur_sum = calculate_orbits(tree, child)
        count += cur_count
        sum += cur_sum
    return count+1, sum + count


# build graph using dict implementation with inputs
tree = {}
direct_orbits = 0
filepath = f'{os.getcwd()}/Q6/input.txt'
with open(filepath, 'r') as f:
    data = f.read().splitlines()
    for orbit in data:
        a, b = orbit.split(')')
        if a not in tree:
            tree[a] = []
        tree[a].append(b)

        direct_orbits += 1

count, num_orbits = calculate_orbits(tree, "COM")
print(num_orbits)
