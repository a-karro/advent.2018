
with open('data/day8.txt', 'r') as f:
    mess = [int(i) for line in f for i in line.strip().split()]


class Node(object):
    def __init__(self):
        self.children = []
        self.meta = []
        self.value = 0


def build_tree(data, tree=None):
    tree = tree or Node()
    children = data.pop(0)
    metadata = data.pop(0)
    for _ in xrange(children):
        tree.children.append(build_tree(data))

    for _ in xrange(metadata):
        tree.meta.append(data.pop(0))

    return tree


def sum_metadata(tree):
    sum_meta = 0
    for child in tree.children:
        sum_meta += sum_metadata(child)
    return sum_meta + sum(tree.meta)


def evaluate(tree):
    if not tree.children:
        tree.value = sum(tree.meta)
    else:
        if tree.value == 0:
            for m in tree.meta:
                if m - 1 < len(tree.children):
                    tree.value += evaluate(tree.children[m - 1])
    return tree.value


yggdrasil = build_tree(mess)
yggdrasil.value = evaluate(yggdrasil)

print "Puzzle 1: ", sum_metadata(yggdrasil)

print "Puzzle 2:", yggdrasil.value
