from datetime import datetime
import re
from collections import defaultdict
from collections import Counter


log = re.compile(r'\[(.*)\] (.*)')
guard_nr = re.compile(r'Guard #(\d.)')


def to_seconds(convert):
    return int((datetime.strptime(convert, '%Y-%m-%d %H:%M') - datetime(1500, 1, 1)).total_seconds())


with open('data/day4.txt', 'r') as f:
    timecards = sorted([{'sec': to_seconds(time), 'time': time.split(':')[1], 'data': data}
                        for line in f for (time, data) in re.findall(log, line)], key=lambda k: k['sec'])

current_guard = ''
interval_start = -1
interval_end = -1
sleepers = defaultdict(list)
for card in timecards:
    current_guard = card['data'].replace('Guard #', '').split()[0] if 'Guard' in card['data'] else current_guard
    interval_start = int(card['time']) if 'falls' in card['data'] else interval_start
    interval_end = int(card['time']) if 'wakes' in card['data'] else interval_end
    if interval_end > -1:
        sleepers[current_guard].extend(range(interval_start, interval_end))
        interval_start = interval_end = -1

sleepiest = max(sleepers, key=lambda key: len(sleepers[key]))

data = Counter(sleepers[sleepiest])
print "Puzzle 1: ", int(sleepiest) * data.most_common(1)[0][0]

sleeping = defaultdict(list)

for (sleeper, data) in sleepers.iteritems():
    for entry in data:
        sleeping[entry].append(int(sleeper))

the_minute = -1
sleeper = -1
max_times = -1

for minute, sleepers in sleeping.iteritems():
    data = Counter(sleepers).most_common(1)
    if max_times < data[0][1]:
        max_times = data[0][1]
        sleeper = data[0][0]
        the_minute = minute


print "Puzzle 2: ", sleeper*the_minute
