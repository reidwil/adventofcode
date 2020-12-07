from itertools import combinations

with open('data.csv') as f:
    data = f.read().splitlines()
    data = [int(i) for i in data]


def compare(array, depth, n = 2020):
    """
    generates a list of all possible combinations of the array passed into it split by 'combinations'
    we then check if any number combinations = n and then multiply those numbers together 
    """
    output = 1
    combos = list(combinations(array,depth))
    specific_numbers = [x for x in combos if sum(x) == n]
    for x in specific_numbers[0]:
        output *= x
    print(specific_numbers)
    return output

print(compare(data, 2))
# 567171
print(compare(data, 3))
# 212428694