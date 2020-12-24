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

# task 1
get_output(1,3)

# task 2
get_output(1,1)
get_output(3,1)
get_output(5,1)
get_output(7,1)
get_output(1,2)
