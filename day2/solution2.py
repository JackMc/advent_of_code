def differs_by_one_letter(line1, line2):
    count = 0
    for i, letter in enumerate(line1):
        if line2[i] != letter:
            count += 1
    return count == 1

two_counter = 0
three_counter = 0

with open('input.txt') as input:
    lines = input.readlines()
    for line1 in lines:
        for line2 in lines:
            if line1 == line2: break
            if differs_by_one_letter(line1.strip(), line2.strip()):
                print(line1, line2)
