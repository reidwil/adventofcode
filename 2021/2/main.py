with open('2/2_data/data.txt') as f:
    data = f.read().split('\n')
    data = [input.split(' ') for input in data]


def task1(input: str):
    output: list = [0, 0]
    for line in input:
        if line[0] == 'forward':
            output[0] += int(line[1])
        elif line[0] == 'down':
            output[1] += int(line[1])
        else:
            output[1] -= int(line[1])
    print(output[0] * output[1])


task1(data)

def task2(input: str):
    aim:int = 0
    output: list = [0, 0, aim]
    for line in input:
        if line[0] == 'forward':
            output[0] += int(line[1])
            output[1] += int(line[1]) * output[2]
        elif line[0] == 'down':
            output[2] += int(line[1])
        else:
            output[2] -= int(line[1])
    print(output[0] * output[1])

task2(data)