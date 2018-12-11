serial = 7400
size = 300

grid = [[0] * size for _ in xrange(size)]


for y in xrange(size):
    for x in xrange(size):
        rack_id = (x + 1) + 10
        power = (rack_id * (y + 1) + serial) * rack_id
        power = (power // 100) % 10 - 5
        grid[y][x] = power


def sum_row(_x, _y, length):
    return sum(grid[_y][_x + c] for c in xrange(length))


def sum_col(_x, _y, length):
    return sum(grid[_y + c][_x] for c in xrange(length))


def get_power_rangers(range_size):
    box = sum(grid[_y][_x] for _x in xrange(range_size) for _y in xrange(range_size))
    cx = cy = -1
    cell_sum = -size * size * 9
    for _y in xrange(size - range_size):
        cur_box = box
        for _x in xrange(size - range_size):
            box = box - sum_col(_x, _y, range_size) \
                      + sum_col(_x + range_size, _y, range_size)
            if box > cell_sum:
                cell_sum = box
                cx = _x + 1
                cy = _y + 1
        box = cur_box - sum_row(0, _y, range_size) \
                      + sum_row(0, _y + range_size, range_size)

    return cell_sum, cx + 1, cy


three = get_power_rangers(3)

print "Puzzle 1: %d,%d" % (three[1], three[2])

max_box = (-size * size * 9, 0, 0)
s = 0
for c in range(2, size - 1):
    k = get_power_rangers(c)
    if k[0] > max_box[0]:
        max_box = k
        s = c

print "Puzzle 2: %d,%d,%d" % (max_box[1], max_box[2], s)
