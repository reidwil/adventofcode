import os

with open(os.path.abspath('3_data/sample.txt')) as f:
    sample = f.read().splitlines()

def task1(input):
    bit_depth = len(input[0])
    print(input)

task1(sample)