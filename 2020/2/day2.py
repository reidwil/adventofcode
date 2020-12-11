import pandas

data = pandas.read_csv('data.txt', delimiter=' ')
# idk how do use pandas to get these in lists
passwords = [x for x in data['password']]
letters =   [x for x in data['letter']]
minimums =  [x for x in data['min']]
maximums =  [x for x in data['max']]
count = 0

for letter, password, mins, maxs in zip(letters, passwords, minimums, maximums):
    letter_count = password.count(letter)
    if letter_count >= mins:
        if letter_count <= maxs:
            count += 1

for letter, password, idx1, idx2 in zip(letters, passwords, minimums, maximums):
    idx1_exists = password[idx1-1].count(letter)
    idx2_exists = password[idx2-1].count(letter)
    if idx1_exists + idx2_exists == 1:
        count_2 += 1

print(f"counts of the first task: {count}\ncounts of the second task: {count_2}")