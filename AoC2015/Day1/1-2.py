input = list(open('input.txt').read())

floor = 0

for i,v in enumerate(input):
    if v == ')':
        floor -= 1
    else:
        floor += 1
    if floor == -1:
        print(i+1)
        break