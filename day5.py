with open('data/day5.txt', 'r') as f:
    polymer = ''.join(line.strip() for line in f)


def react(poly):
    while True:
        cur_len = len(poly)
        for x in xrange(ord('A'), ord('Z')+1):
            poly = poly.replace(chr(x)+chr(x+32), '').replace(chr(x+32)+chr(x), '')
        if cur_len == len(poly):
            break
    return len(poly)


print "puzzle 1:", react(str(polymer))

min_poly = 10000000

for i in xrange(ord('A'), ord('Z')+1):
    sample = react(polymer.replace(chr(i), '').replace(chr(i+32), ''))
    if min_poly > sample:
        min_poly = sample

print "Puzzle 2: ", min_poly
