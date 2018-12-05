from requests import get
from os.path import expanduser, exists

def getlines(challenge, debug=True):
    cachepath = f'day{challenge}/input.txt'
    if debug:
        lines = open(f'day{challenge}/debug_input.txt').readlines()
    if exists(cachepath):
        lines = open(cachepath).readlines()
    else:
        input = get(f'https://adventofcode.com/2018/day/{challenge}/input', cookies={'session': open(expanduser('~/.aoc_session')).read().strip()}).text
        lines = input.split('\n')
        open(cachepath, 'w').write(input)
    if lines[-1] == '':
        return lines[:-1]
    return lines
