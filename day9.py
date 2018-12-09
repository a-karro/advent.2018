from blist import blist


def marbles(high):
    i = 3
    while i <= high:
        yield i
        i += 1


def elves(gang_size):
    i = 3
    while True:
        yield i % gang_size
        i += 1


def insert_marble(_m, game_list, current):
    c = current + 2
    if c > len(game_list):
        c = 1
    game_list.insert(c, _m)
    return c


def get_7h_index(game_list, current):
    current = current - 7
    if current < 0:
        current = len(game_list) + current
    return current


with open('data/day9.txt', 'r') as f:
    data = f.readline().split()
    players = int(data[0])
    highest = int(data[6])


def run_game(player_count, marble_count):
    player = list([0] * player_count)

    game = blist([0, 2, 1])
    current_marble_pos = 1

    marble = marbles(marble_count)
    elf = elves(player_count)

    try:
        while True:
            m = next(marble)
            e = next(elf)
            if m % 23 == 0:
                player[e] += m
                current_marble_pos = get_7h_index(game, current_marble_pos)
                player[e] += game.pop(current_marble_pos)
            else:
                current_marble_pos = insert_marble(m, game, current_marble_pos)
    except StopIteration:
        return max(player)


print "Puzzle 1: ", run_game(players, highest)
print "Puzzle 2: ", run_game(players, highest * 100)
