total_freq = 0

with open('input.txt') as input:
    for line in input:
        frequency_change = int(line.strip())
        total_freq += frequency_change

print(f'Total frequency: {total_freq}')
