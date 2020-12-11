with open('data.txt') as f:
    data = f.read().splitlines()

def is_tree(down, right):
    adjusted_right = right % len(data[0]) # resetting after 'right' is past array length
    return data[down][adjusted_right] == '#'

def get_output(down_increment, right_increment):
    trees = 0
    down = 0
    right = 0

    while down < len(data):
        if is_tree(down, right):
            trees += 1
        down += down_increment
        right += right_increment
    
    return trees