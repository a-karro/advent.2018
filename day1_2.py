

with open('data/day1_1.txt', 'r') as f:
    changes = [int(i) for i in f]

seen = dict()

position = 0
offset = 0

while True:
    offset = offset + changes[position]
    if offset in seen:
        print offset
        break

    seen[offset] = 1

    position += 1
    if position == len(changes):
        position = 0
