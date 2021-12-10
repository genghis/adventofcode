input = open('input.txt').read()

answer=set()

location=[0,0]

for i in input:
    match i:
        case '^':
            location[0] -= 1
        case 'v':
            location[0] += 1
        case '<':
            location[1] -= 1
        case '>':
            location[1] += 1
    answer.add(tuple(location))
print(len(answer))