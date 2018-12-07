from collections import defaultdict
from copy import copy


with open('data/day7.txt', 'r') as f:
    lines = [line.strip() for line in f]


graph = defaultdict(list)
graph2 = defaultdict(list)
for line in lines:
    split = line.split(' ')
    graph[split[1]].extend(split[7])

for k in graph.keys():
    graph[k] = sorted(graph[k])

graph2 = copy(graph)

flatvalues = [item for sublist in graph.values() for item in sublist]

end = list(set([value for value in flatvalues if value not in graph.keys()]))[0]

done_list = ''

while len(graph) > 0:
    available = sorted([key for key in graph.keys() if key not in flatvalues])[0]
    done_list = done_list + available
    for item in graph.pop(available):
        if item in flatvalues:
            flatvalues.remove(item)


print "Puzzle 1:", done_list + end

graph = graph2

flatvalues = [item for sublist in graph.values() for item in sublist]

starts = [key for key in graph.keys() if key not in flatvalues]
ends = [key for key in flatvalues if key not in graph.keys()]

for end in ends:
    graph[end] = ['[']

graph['['] = [']']

flatvalues = [item for sublist in graph.values() for item in sublist]


seconds = 0
base_work = 60
worker_count = 5
workers = list()


for i in range(worker_count):
    workers.append({'on': '?', 'till': -1})

available_in = {key: 0 for key in starts}

while len(graph) > 0:
    lazy = [workers.index(worker) for worker in workers if worker['till'] <= seconds]

    if not lazy:
        seconds += 1
        continue

    available = [key for key in graph.keys() if (available_in.get(key, -1) <= seconds and key not in flatvalues)]

    pairs = zip(lazy, available)
    for pair in pairs:
        workers[pair[0]]['on'] = pair[1]
        workers[pair[0]]['till'] = seconds + ord(pair[1]) - 64 + base_work

        for item in graph.pop(pair[1]):
            available_in[item] = max(workers[pair[0]]['till'], available_in.get(item, -1))
            if item in flatvalues:
                flatvalues.remove(item)
    seconds += 1

print "Puzzle 2:", seconds - 1
