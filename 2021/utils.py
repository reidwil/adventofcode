import requests
from typing import Union
from os import PathLike

def read_input(day: int, year: int = 2021):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    data = requests.get(url)
    return(data)

def read_input_from_file(filepath: Union[PathLike, None], split: bool = False):
    with open(filepath, 'r') as f:
        if split:
            data = f.read().split()
        else:
            data = f.read()
    return data