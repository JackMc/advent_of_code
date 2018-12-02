from collections import Counter

def has_three_letters(str):
    c = Counter(str)
    return len([k for k in c if c[k] == 3]) > 0

def has_two_letters(str):
    c = Counter(str)
    return len([k for k in c if c[k] == 2]) > 0

two_counter = 0
three_counter = 0

with open('input.txt') as input:
    for line in input:
        if has_two_letters(line.strip()):
            two_counter += 1
        if has_three_letters(line.strip()):
            three_counter += 1

print(two_counter * three_counter)
