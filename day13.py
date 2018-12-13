import copy


chars = '/-\\|+'
cart_loc = 'v^><'
new_direction_turns = [
        [3, 2, 1, 0],
        [0, 0, 0, 0],
        [2, 3, 0, 1]
    ]

new_directions_intersect = [
        [2, 0, 3],
        [3, 1, 2],
        [1, 2, 0],
        [0, 3, 1]
    ]

x_offsets = [0, 0, 1, -1]
y_offsets = [1, -1, 0, 0]

with open('data/day13.txt', 'r') as f:
    lines = f.readlines()

y_size = len(lines)
x_size = max(len(line.rstrip('\n')) for line in lines)

grid = [[-1] * x_size for _ in xrange(y_size)]

carts = list()

for y, line in enumerate(lines):
    for x, char in enumerate(line.rstrip('\n')):
        if char in cart_loc:
            cart = {'coords': (x, y), 'rotate': 0, 'dir': cart_loc.find(char)}
            grid[y][x] = 1 if char in '<>' else 3
            carts.append(cart)
        else:
            grid[y][x] = chars.find(char)


def index_(l, obj):
    try:
        return l.index(obj)
    except ValueError:
        return -1


def recalc_cart_positions(_carts, _grid):
    list_len = -1
    first_strike = None
    while list_len < len(_carts):
        list_len = len(_carts)
        remove = [-1, -1]
        for i, c in enumerate(_carts):
            remove[0] = i
            _x, _y = c['coords']
            new_x = _x + x_offsets[c['dir']]
            new_y = _y + y_offsets[c['dir']]
            remove[1] = index_([cc['coords'] for cc in _carts], (new_x, new_y))
            if remove[1] > -1:
                first_strike = first_strike or (new_x, new_y)
                break
        if remove[0] > -1 and remove[1] > -1:
            _carts.pop(max(remove))
            _carts.pop(min(remove))
    for i, c in enumerate(_carts):
        _x, _y = c['coords']
        new_x = _x + x_offsets[c['dir']]
        new_y = _y + y_offsets[c['dir']]
        c['coords'] = (new_x, new_y)
        c['coords'] = (new_x, new_y)
        if _grid[new_y][new_x] in (0, 2):  # turns
            c['dir'] = new_direction_turns[(_grid[new_y][new_x])][c['dir']]
        elif _grid[new_y][new_x] == 4:  # intersection
            c['dir'] = new_directions_intersect[c['dir']][c['rotate']]
            c['rotate'] = (c['rotate'] + 1) % 3

    res = []
    cc = [cc['coords'] for cc in _carts]
    for c in _carts:
        if cc.count(c['coords']) == 1:
            res.append(c)
        else:
            first_strike = first_strike or c['coords']
    return res, first_strike


def run_carts(_carts, _grid, stop_on_crash=True):
    crashed = None
    while not (crashed and stop_on_crash):
        _carts, crashed = recalc_cart_positions(_carts, _grid)
        if stop_on_crash and crashed:
            return crashed
        if len(_carts) == 1:
            return _carts[0]['coords']


print run_carts(copy.deepcopy(carts), grid, stop_on_crash=True)
print run_carts(carts, grid, stop_on_crash=False)
