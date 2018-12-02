with open('data/day1_1.txt', 'r') as f:
    offset = 0
    for i in f:
        offset = offset + int(i)
print offset
