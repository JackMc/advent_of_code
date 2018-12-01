total_freq = 0
totals_seen = {0}
stop = False

while not stop:
    with open('input.txt') as input:
        for line in input:
            frequency_change = int(line.strip())
            total_freq += frequency_change
            if total_freq not in totals_seen:
                totals_seen.add(total_freq)
            else:
                print(f'First total seen twice: {total_freq}')
                stop = True
                break
