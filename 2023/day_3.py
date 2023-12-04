import re

import aocd

data = aocd.get_data(day=3, year=2023).split('\n')

def find_links(data):
    """Take the data and create a list of lists for each numeric sequence"""
    output = []
    for row_index, string in enumerate(data):
        for match in re.finditer(r'\d+', string):
            number = int(match.group())  # The actual number
            start_index = match.start()  # Starting index of the number in the string
            end_index = start_index + len(str(number))
            output.append([row_index, start_index, end_index, number])
    return output

def find_special_chars(data):
    """Return list of lists consisting of [list_index, row_index] of a special char"""
    special_chars = []
    for list_index, row in enumerate(data):
        for row_index, char in enumerate(row):
            if not char.isalnum() and not char == '.':
                special_chars.append([list_index, row_index])
    return special_chars

def find_only_gears(data):
    special_chars = []
    for list_index, row in enumerate(data):
        for row_index, char in enumerate(row):
            if char == '*':
                special_chars.append([list_index, row_index])
    return special_chars

def find_matches(link_list, chars_list):
    result = 0
    for row_idx, list_index in chars_list:
        for list_row_index, start_idx, end_idx, number in link_list:
            if row_idx - 1 >= 0:
                if row_idx - 1 == list_row_index or row_idx + 1 == list_row_index or row_idx == list_row_index:
                    if list_index in range(start_idx-1, end_idx+1):
                        result += number
    print(result)


def find_close_matches(link_list, chars_list):
    result = 0
    for row_idx, list_index in chars_list:
        product = 1
        results = []
        for list_row_index, start_idx, end_idx, number in link_list:
            if row_idx - 1 >= 0:
                if row_idx - 1 == list_row_index or row_idx == list_row_index or row_idx + 1 == list_row_index:
                    if list_index in range(start_idx-1, end_idx+1):
                        results.append(number)
        if len(results) == 2:
            for num in results:
                product *= num
            result += product
    print(result)



def task1(data):
    link_list = find_links(data)
    chars_list = find_special_chars(data)
    find_matches(link_list, chars_list)

def task2(data):
    link_list = find_links(data)
    chars_list = find_only_gears(data)
    find_close_matches(link_list, chars_list)

task1(data)
task2(data)