with open('data.txt') as f:
    data = f.read().splitlines()

def get_placement(array, directions, decision, front):
    for letter in directions:
        midpoint = round((array[0] + array[1]) / 2)
        if letter == front:
            array[1] = midpoint - 1 
        else:
            array[0] = midpoint
    return array[0] if decision == front else array[1]


def b_tree(array):
    row_options = [0, 127]
    seat_options = [0, 7]

    adjusted_row_placement = array[0:6]
    deciding_row_placement = array[6]
    adjusted_seat_placement = array[7:9]
    deciding_seat_placement = array[9]

    correct_row = get_placement(row_options, adjusted_row_placement, deciding_row_placement, 'F')
    correct_seat = get_placement(seat_options, adjusted_seat_placement, deciding_seat_placement, 'L')

    return (correct_row * 8) + correct_seat

seat_ids = []
for row in data:
    seat_ids.append(b_tree(row))
    set_seats = set(seat_ids)

seat_counts = set_seats.pop() + 1
for seat in set_seats:
    if seat_counts != seat:
        print(f"Your seat is: {seat - 1}")
        break
    seat_counts += 1