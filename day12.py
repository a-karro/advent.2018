v = ['.', '#']
changes = {}
for x in [v1 + v2 + v3 + v4 + v5 for v1 in v for v2 in v for v3 in v for v4 in v for v5 in v]:
    changes[x] = '.'

with open('data/day12.txt', 'r') as f:
    init_state = f.readline().split(':')[1].strip()
    f.readline()
    for line in f.readlines():
        line = line.strip().split(' => ')
        changes[line[0]] = line[1]

generations = 20
offset = generations + 2
current_state = '.' * offset + init_state + '.' * offset


def calc_len(state, offset_, mega_offset=0):
    puzzle1 = 0
    for n in range(0 - offset_, len(state) - offset_):
        if state[n + offset_] == '#':
            puzzle1 += n + mega_offset
    return puzzle1


def get_next_state(state):
    next_state = state
    for init, change in changes.iteritems():
        change_pos = -1
        while True:
            change_pos = state.find(init, change_pos + 1)
            if change_pos > 0:
                next_state = next_state[:change_pos + 2] + change + next_state[change_pos + 3:]
            else:
                break
    return next_state


end_state = current_state
for gen in xrange(generations):
    end_state = get_next_state(end_state)

print "Puzzle 1:", calc_len(end_state, offset)

generations = 500
offset = generations + 2
current_state = '.' * offset + init_state + '.' * offset

end_state = current_state
cnt = 0
length = 0
future = 50000000000
while True:
    cnt += 1
    current_end_state = end_state.rstrip('.').lstrip('.')
    end_state = get_next_state(end_state)
    if end_state.rstrip('.').lstrip('.') == current_end_state:
        break
    else:
        length = calc_len(end_state, offset, mega_offset=future - cnt)

print "Puzzle 2:", length
