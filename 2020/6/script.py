from collections import Counter

def task1():
    with open('data.txt') as f:
        data = f.read().split('\n\n')
        data = [list(set(x.replace('\n', ''))) for x in data]
        data = [len(x) for x in data]
    print(sum(data))

def task2():
    with open('data.txt') as f:
        data = f.read().split('\n\n')
        people = [person.count('\n') + 1 for person in data]
        data = [x.replace('\n', '') for x in data]
        output = [(v, Counter(k)) for k,v in zip(data, people)]
    
    total_people = 0
    for line in output:
        letter_counts = [x for x in line[1].values()]
        for letter in letter_counts:
            if letter == line[0]:
                total_people += 1
    print(total_people)
    
task1()
task2()