import re

import aocd
data = aocd.get_data(day=2, year=2023).split('\n')


MAX_PER_COLOR = {
    'red': 12, 
    'green': 13, 
    'blue': 14
}

def extract_game_ids(row):
    matches = re.findall(r'Game (\d+):', row)
    if matches:
        return int(matches[0])

def is_valid_game(row):
    game = row.split(':')[1]
    turns = game.strip().split('; ')
    for turn in turns:
        pairs = turn.split(', ')
        for pair in pairs:
            count, color = pair.split(' ')
            count = int(count)
            if count > MAX_PER_COLOR[color]:
                return False
    return True

def find_minimums(row):
    result = 1
    minimums = {color: 0 for color in MAX_PER_COLOR.keys()}
    game = row.split(':')[1]
    turns = game.strip().split('; ')
    for turn in turns:
        pairs = turn.split(', ')
        for pair in pairs:
            count, color = pair.split(' ')
            count = int(count)
            if count > minimums[color]:
                minimums[color] = count
    for val in minimums.values():
        result = result * val
    return result


def task1(data):
    game_ids = sum([extract_game_ids(row) for row in data if is_valid_game(row)])
    print(game_ids)

def task2(data):
    result = sum([find_minimums(row) for row in data])
    print(result)

task1(data)
task2(data)