input = open('input.txt').read()

biosanta = input[1::2]
robosanta = input[0::2]
answer={(0,0)}

def deliver(santatype):
    location=[0,0]
    for i in santatype:
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

deliver(biosanta)
deliver(robosanta)

print(len(answer))