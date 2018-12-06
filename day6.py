from collections import Counter
import pprint

with open('data/day6.txt', 'r') as f:
    points = [tuple(int(coord) for coord in line.strip().split(',')) for line in f]

offset_x = min(points, key=lambda k: k[0])[0]
offset_y = min(points, key=lambda k: k[1])[1]

points = map(lambda p: (p[0]-offset_x, p[1]-offset_y), points)

max_x = max(points, key=lambda k: k[0])[0]
max_y = max(points, key=lambda k: k[1])[1]

field = list()
for x in xrange(0, max_x):
    field.append([-2] * max_y)

safe_field_size = 0


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for y in xrange(0, max_y):
    for x in xrange(0, max_x):
        min_d = 10000
        sum_d = 0
        for i, point in enumerate(points):
            mh = manhattan(point, (x, y))
            sum_d += mh
            if min_d > mh or mh == 0:
                min_d = mh
                field[x][y] = i
            elif min_d == mh:
                field[x][y] = -1
        if sum_d < 10000:
            safe_field_size += 1

outer_points = list()

for x in xrange(0, max_x):
    i = field[x][0]
    i1 = field[x][max_y-1]
    if i > -1 and i not in outer_points:
        outer_points.append(i)
    if i1 > -1 and i1 not in outer_points:
        outer_points.append(i1)

for y in xrange(0, max_y):
    i = field[0][y]
    i1 = field[max_x-1][y]
    if i > -1 and i not in outer_points:
        outer_points.append(i)
    if i1 > -1 and i1 not in outer_points:
        outer_points.append(i1)


flat_field = list()
for line in field:
    for entry in line:
        if entry not in outer_points:
            flat_field.append(entry)

data = Counter(flat_field)
print "puzzle 1:", data[max(data, key=data.get)]
print "puzzle 2:", safe_field_size
