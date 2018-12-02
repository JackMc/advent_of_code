import re

import itertools
from collections import defaultdict

with open('input.txt') as input:
    claims = defaultdict(lambda: [])
    elves = set()
    lines = input.readlines()
    linere = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")
    for line in lines:
        elf, x, y, width, height = [int(x) for x in linere.match(line).groups()]
        elves.add(elf)
        for x_coord in range(x, x + width):
            for y_coord in range(y, y + height):
                claims[(x_coord,y_coord)].append(elf)
    print(f'Pt1: {len([claims[k] for k in claims if len(claims[k]) > 1])}')
    number_of_overlaps = defaultdict(lambda: [])

    for coord in claims:
        if len(claims[coord]) > 1:
            for elf in claims[coord]:
                if elf in elves: elves.remove(elf)
    print(f'pt2: {elves}')
