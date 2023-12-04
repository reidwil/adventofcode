from collections import defaultdict
import aocd

data = aocd.get_data(day=4, year=2023).split('\n')

def find_matches(list1, list2):
    """given two lists, find the length of matched values"""
    return len(set(list1) & set(list2))

def double(number):
    result = 0
    if number == result:
        return result
    result += 2**(number-1)
    return result


def task1(data):
    result = 0
    for row in data:
        first, rest = row.split('|')
        _, card = first.split(':')
        card_nums = [int(x) for x in card.split()]
        rest_nums = [int(x) for x in rest.split()]
        match_count = find_matches(card_nums, rest_nums)
        score = double(match_count)
        result += score
    print(result)


def task2(data):
    result = defaultdict(int)
    for i, row in enumerate(data):
        result[i] += 1
        first, rest = row.split('|')
        _, card = first.split(':')
        card_nums = [int(x) for x in card.split()]
        rest_nums = [int(x) for x in rest.split()]
        match_count = find_matches(card_nums, rest_nums)
        for j in range(match_count):
            result[i+1+j] += result[i]
    print(sum(result.values()))

task1(data)
task2(data)