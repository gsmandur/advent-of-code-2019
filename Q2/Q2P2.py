import os


def intcode(data):
    ''' modify and return updated data list '''
    data = data.copy()
    # loop through opcodes
    for i in range(0, len(data), 4):
        if data[i] == 99:
            break

        p1 = data[i+1]
        p2 = data[i+2]
        p3 = data[i+3]
        if data[i] == 1:
            data[p3] = data[p1] + data[p2]
        elif data[i] == 2:
            data[p3] = data[p1] * data[p2]
        else:
            raise TypeError('unknown opcode used')
    return data


filepath = f'{os.getcwd()}/Q2/input.txt'
with open(filepath, 'r') as f:
    data = f.read().split(',')
    data = [int(x) for x in data]

# find the pair of values that gives us the value 19690720
for noun in range(100):
    for verb in range(100):
        data[1] = noun
        data[2] = verb
        result = intcode(data)
        if result[0] == 19690720:
            print(f'{noun} - {verb}')
            break
