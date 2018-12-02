from utils import getlines
import re
from collections import defaultdict
import operator

input = getlines(4)

timestampre = re.compile('\[1518-(\d+)-(\d+) (\d+):(\d+)\]')
guardre = re.compile('].*(\d+)')

events = []

for line in input:
    month, day, hour, minute = timestampre.match(line).groups()
    month = int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)
    print(month, day, hour, minute)
    if 'asleep' in line:
        event = 'asleep'
        guard = -1
    elif 'wakes' in line:
        event = 'wake'
        guard = -1
    elif 'begins' in line:
        event = 'begins'
        guard = int(re.findall('\d+', line)[-1])
    events.append((month, day, hour, minute, event, guard))

events = sorted(events)

minute_sleep_times = defaultdict(lambda: 0)

for event in events:
    if event[4] == 'begins':
        current_guard = event[5]
    elif event[4] == 'asleep':
        start_time = event
    elif event[4] == 'wake':
        for i in range(start_time[3], event[3]):
            minute_sleep_times[(current_guard, i)] += 1

print(max(minute_sleep_times.items(), key=operator.itemgetter(1))[0])
