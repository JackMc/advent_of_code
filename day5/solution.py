from utils import getlines
import re
from collections import defaultdict
import operator
import itertools
import string

lower = string.ascii_lowercase

item = getlines(5)[0]

any_letters = True
while any_letters:
    for letter in lower:
        old_item = item
        item = item.replace(f'{letter}{letter.upper()}', '')
        item = item.replace(f'{letter.upper()}{letter}', '')
        if item != old_item:
            print(f'Replaced {letter}{letter.upper()} or {letter.upper()}{letter}')
            break
    else:
        any_letters = False
print(len(item))
