from utils import getlines
import re
from collections import defaultdict
import operator
import itertools

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

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

events = sorted(events)

guard_sleep_times = defaultdict(lambda: [])

for event in events:
    if event[4] == 'begins':
        current_guard = event[5]
    elif event[4] == 'asleep':
        start_time = event
    elif event[4] == 'wake':
        for i in range(start_time[3], event[3]):
            guard_sleep_times[current_guard].append(i)

sleepiest_guard = max(guard_sleep_times.items(), key=lambda item: len(item[1]))[0]
print(sleepiest_guard)
sleepy_guard_sleep_minute = most_common(guard_sleep_times[sleepiest_guard])
print(sleepy_guard_sleep_minute)
