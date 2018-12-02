from requests import get
from os.path import expanduser

def getlines(challenge):
    lines = get(f'https://adventofcode.com/2018/day/{challenge}/input', cookies={'session': open(expanduser('~/.aoc_session')).read().strip()}).text.split('\n')
    if lines[-1] == '':
        return lines[:-1]
    return lines
