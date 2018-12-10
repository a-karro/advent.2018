import re

numbers = re.compile(r'-?\d+')

points = []
with open('data/day10.txt', 'r') as f:
    for line in f:
        points.append([int(i) for i in re.findall(numbers, line)])


def x_y_in_points(_x, _y):
    for point in points:
        if point[0] == _x and point[1] == _y:
            return True
    return False


def recalc_points(direction=1):
    _min_x = 2147483647
    _min_y = 2147483647
    _max_x = -2147483646
    _max_y = -2147483646
    for p in points:
        p[0] += p[2] * direction
        p[1] += p[3] * direction
        if _min_x > p[0]:
            _min_x = p[0]
        if _min_y > p[1]:
            _min_y = p[1]
        if _max_x < p[0]:
            _max_x = p[0]
        if _max_y < p[1]:
            _max_y = p[1]
    return abs(_max_x - _min_x), abs(_max_y - _min_y)


current_bounds = recalc_points(0)

counter = 0
while True:
    bounds = recalc_points()
    counter += 1
    if bounds[1] > current_bounds[1] or bounds[0] > current_bounds[0]:
        recalc_points(-1)
        counter += -1
        break
    current_bounds = bounds

min_x = min(point[0] for point in points)
min_y = min(point[1] for point in points)
max_x = max(point[0] for point in points)
max_y = max(point[1] for point in points)

print "Puzzle 1:\n"
for y in xrange(min_y, max_y+1):
    sstr = ''
    for x in xrange(min_x, max_x+1):
        if x_y_in_points(x, y):
            sstr = sstr + '#'
        else:
            sstr = sstr + ' '
    print sstr

print "\n\nPuzzle 2:", counter
