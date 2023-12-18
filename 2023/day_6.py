import aocd

data = aocd.get_data(day=6, year=2023).split('\n')

def parse_data(data):
    time = list(map(int, [item for item in data[0].split(':')[1].strip().split(' ') if item != '']))
    distance = list(map(int, [item for item in data[1].split(':')[1].strip().split(' ') if item != '']))
    return time, distance


def calculate_distance(time, distance):
    calculated_distances = []
    for i in range(1,time+1):
        current_distance = (i * (time-i))
        if current_distance > distance:
            calculated_distances.append(current_distance)
    return len(calculated_distances)

def task_1(data):
    times, distances = parse_data(data)
    answer = 1
    for time, distance in zip(times, distances):
        answer *= calculate_distance(time, distance)
    print(answer)

def task_2(data):
    times, distances = parse_data(data)
    # concatting the list objects to a single number
    times, distances = [int("".join(map(str, times)))], [int("".join(map(str, distances)))]
    answer = 1
    for time, distance in zip(times, distances):
        answer *= calculate_distance(time, distance)
    print(answer)

task_2(data)
