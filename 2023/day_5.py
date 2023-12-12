import aocd
data = aocd.get_data(day=5, year=2023)

def parse_data(data):
    seeds, *blocks = data.split('\n\n')
    seeds = list(map(int, seeds.split(':')[1].split()))
    return seeds, blocks

def task_1(data):
    seeds, blocks = parse_data(data)
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for x in seeds:
            for a, b, c in ranges:
                if x in range(b, b+c):
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new
    print(min(seeds))

task_1(data)
