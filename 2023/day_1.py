import aocd #This gets me the Advent of Code data

literal_digits = ['one','two','three','four','five','six','seven','eight','nine']

def add_first_and_last_digit_and_literals(line: [str]) -> int:
    """given a list object, return the concat of first and last digit"""
    digits = []
    for i, item in enumerate(line):
        if line[i].isdigit():
            digits.append(item)
        for d, val in enumerate(literal_digits):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit+last_digit)


def task1():
    data = aocd.get_data(day=1, year=2023).split('\n')
    output = 0
    for row in data:
        output += add_first_and_last_digit_and_literals(row)
    print(output)



def task2():
    data = aocd.get_data(day=1, year=2023).split('\n')
    output = 0
    for line in data:
        output += add_first_and_last_digit_and_literals(line)
        print(output)
    
task2()