input = list(open('input.txt').read())

floor = 0

for v in input:
    if v == ')':
        floor -= 1
    else:
        floor += 1

print(floor)