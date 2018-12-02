twos = 0
threes = 0
with open('data/day2_1.txt', 'r') as f:
    box_codes = [box_code.strip() for box_code in f.readlines()]

for box_code in box_codes:
    counters = dict()
    for char in box_code:
        counters[char] = counters.get(char, 0) + 1
    twos += 1 if 2 in counters.values() else 0
    threes += 1 if 3 in counters.values() else 0

print twos * threes
