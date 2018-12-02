from utils import getlines
import re
from collections import defaultdict
import operator
import itertools
import string

lower = string.ascii_lowercase

orig_item = getlines(5)[0]
#orig_item = open('day5/debug_input.txt').readlines()[0].strip()

vals = []

for letter in lower:
    item = orig_item
    item = item.replace(letter, '')
    item = item.replace(letter.upper(), '')
    print(f'trying letter {letter}')
    any_letters = True
    while any_letters:
        for letter in lower:
            old_item = item
            item = item.replace(f'{letter}{letter.upper()}', '')
            item = item.replace(f'{letter.upper()}{letter}', '')
            if item != old_item:
                break
        else:
            any_letters = False
    vals.append(len(item))
print(min(vals))
