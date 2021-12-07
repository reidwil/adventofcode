with open('3/3_data/sample.txt') as f:
    sample = f.read().splitlines()

def task1(input):
    bit_depth = len(input[0])
    for item in input:
        for line in item:
            print(line)
    print(bit_depth)

task1(sample)