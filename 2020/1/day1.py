from itertools import combinations

with open('data.csv') as f:
    data = f.read().splitlines()
    data = [int(i) for i in data]


def compare(array, depth, n = 2020):
    output = 1
    combos = list(combinations(array,depth))
    specific_numbers = [x for x in combos if sum(x) == n]
    for x in specific_numbers[0]:
        output *= x
    return output