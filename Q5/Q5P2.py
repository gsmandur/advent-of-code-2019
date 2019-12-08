import os


def determine_values(data, pos, modes):
    ''' return the values needed '''


def increment(opcode):
    ''' determine the inc value to get to next instruction '''
    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        return 4
    elif opcode == 3 or opcode == 4:
        return 2
    elif opcode == 5 or opcode == 6:
        return 3


def intcode(data, inputs):
    ''' modify and return updated data list '''
    data = data.copy()
    i = 0
    # loop through opcodes
    while i < len(data):
        opcode = data[i] % 100
        # print(opcode)
        if opcode == 99:
            break

        # determine values based on the mode
        mode1 = (data[i] // 100) % 10
        mode2 = (data[i] // 1000) % 10

        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            v1 = data[i+1] if mode1 == 1 else data[data[i+1]]
            v2 = data[i+2] if mode2 == 1 else data[data[i+2]]
            p3 = data[i+3]

            if opcode == 1:
                data[p3] = v1 + v2
            elif opcode == 2:
                data[p3] = v1 * v2
            elif opcode == 7:
                data[p3] = int(v1 < v2)
            elif opcode == 8:
                data[p3] = int(v1 == v2)
        elif opcode == 3 or opcode == 4:
            v1 = data[i+1] if mode1 == 1 else data[data[i+1]]
            if opcode == 3:
                data[data[i+1]] = inputs
            elif opcode == 4:
                print(v1)
        elif opcode == 5 or opcode == 6:
            v1 = data[i+1] if mode1 == 1 else data[data[i+1]]
            v2 = data[i+2] if mode2 == 1 else data[data[i+2]]
            # print(f'v1 = {v1} - v2 = {v2}')
            if opcode == 5 and v1 != 0:
                i = v2
                continue
            elif opcode == 6 and v1 == 0:
                i = v2
                continue
        else:
            raise TypeError('unknown opcode used')
        i += increment(opcode)
    return data


filepath = f'{os.getcwd()}/Q5/input.txt'
with open(filepath, 'r') as f:
    data = f.read().split(',')
    data = [int(x) for x in data]

result = intcode(data, 5)
