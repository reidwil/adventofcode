import re

with open('data.txt') as f:
    data = f.read().split('\n\n')
    data = [line.replace('\n', ' ') for line in data]

keys = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']

def task1():
    global data, keys
    counter = 0
    for line in data:
        # if all keys are in each line we add to the count
        if all(key in line for key in keys):
            counter += 1
    print(counter)


# Task 2

def checker(items):

    # Birth year (between 1920 and 2002)
    if items[0] == 'byr':
        return bool(int(items[1]) in range(1920, 2003))

    # Issue year (between 2010 and 2020)
    if items[0] == 'iyr':
        return bool(int(items[1]) in range(2010, 2021))

    # Experiation year (between 2020 and 2030)
    if items[0] == 'eyr':
        return bool(int(items[1]) in range(2020, 2031)) 
    
    # Height (if cm - between 150 and 193 | if in - between 59 and 76)
    if items[0] == 'hgt':
        if items[1].endswith('cm'):
            return bool(int(items[1].replace('cm','')) in range(150,194))
        else:
            return bool(int(items[1].replace('in','')) in range(59, 77))
    
    # Hair color (a # and then exactly six chars that are 0-9 or a-f)
    if items[0] == 'hcl':
        return bool(re.search("^#[a-f0-9]{6}$", items[1]))

    # Eye color needs to be one of exactly ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if items[0] == 'ecl':
        return bool(items[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

    # Passport ID is a nine-digit number (including leading zeros)
    if items[0] == 'pid':
        return bool(len(items[1]) == 9)

def task2():
    total_count = 0
    individual_count = 0
    global data, keys
    dicts = [line.split(':') for line in data]
    dicts = [line.split(' ') for line in data]
    for dict in dicts:
        for item in dict:
            output = [k for k in item.split(':')]
            if checker(output):
                individual_count += 1
        if individual_count >= 7:
            total_count += 1
        individual_count = 0
    print(total_count)
task1()
task2()