# https://adventofcode.com/2021/day/1
from os import read
from utils import read_input_from_file


def task1(input: list) -> None:
    previous: int = None
    counter:int = 0
    for item in input:
        if not previous:
            previous = item
            continue
        if item > previous:
            counter += 1
        previous = item
    print(f"{counter}")

task_1_data = read_input_from_file('1_data/1.txt', split=True)
task1(task_1_data)


def task2(input: list):
    previous: int = None
    counter: int = 0
    position: int = 0
    input = list(map(int, input))
    for _ in input:
        this_three = input[position:position+3]
        if not previous:
            previous = sum(this_three)
            position += 1
            continue
        if sum(this_three) > previous:
            counter += 1
        previous = sum(this_three)

        position += 1
    print(f"{counter}")

task_2_data = read_input_from_file('1_data/1.txt', split=True)
task2(task_2_data)