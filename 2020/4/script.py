with open('data.txt') as f:
    data = f.read()
    data = data.split('\n\n')
    data = [item.replace('\n', ' ') for item in data]
    data = [dict(item.split(':')) for item in data]
#    data = [dict(item.split(':')) for item in data]

keys = ['byr:', # (Birth Year)
        'iyr:', # (Issue Year)
        'eyr:', # (Expiration Year)
        'hgt:', # (Height)
        'hcl:', # (Hair Color)
        'ecl:', # (Eye Color)
        'pid:'  # (Passport ID)
]

print(data)