import os


def intcode(data):
    ''' modify and return updated data list '''
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


filepath = f'{os.getcwd()}/Q2/input.txt'
with open(filepath, 'r') as f:
    data = f.read().split(',')
    data = [int(x) for x in data]

# update postion 1 and 2 as required
data[1] = 12
data[2] = 2

intcode(data)
print(data)
