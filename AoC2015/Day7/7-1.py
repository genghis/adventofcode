input = [x.strip() for x in open('input7-1.txt')]
# print(input)

result = {}
circuit = []

for i in input:
    front, back = front,back = i.split(' -> ')
    result[back] = front

def execute_circuit(wire):
    step = result[wire]
    if 'AND' in step or 'OR' in step or 'LSHIFT' in step or 'RSHIFT' in step:
        a,b,c = step.split(' ')
        match b:
            case 'AND':
                result[wire] = result[a]&result[c]
            case 'OR':
                result[wire] = result[a]|result[c]
            case 'LSHIFT':
                result[wire] = result[a]<<int(c)
            case 'RSHIFT':
                result[wire] = result[a]>>int(c)
    elif 'NOT' in front:
        a,b = front.split(' ')
        result[wire] = ~result[b]
    else:
        result[wire] = int(step)

def build_circuit(wire):
    circuit = []
    if result[wire[0]]:
        next_instruction = result[wire]
        if 'AND' in wire or 'OR' in wire or 'LSHIFT' in wire or 'RSHIFT' in wire:
            a,b,c = wire.split(' ')
            circuit.extend(a)
            circuit.extend(c)
            build_circuit(next_instruction)
        else:        
            circuit.extend(result[wire])
            build_circuit(next_instruction)
    else:
        return circuit

print(build_circuit('a'))
# def parse(string):
#     print(string)
#     front,back = string.split(' -> ')
    # if 'AND' in front or 'OR' in front or 'LSHIFT' in front or 'RSHIFT' in front:
    #     a,b,c = front.split(' ')
    #     match b:
    #         case 'AND':
    #             result[back] = result[a]&result[c]
    #         case 'OR':
    #             result[back] = result[a]|result[c]
    #         case 'LSHIFT':
    #             result[back] = result[a]<<int(c)
    #         case 'RSHIFT':
    #             result[back] = result[a]>>int(c)
    # elif 'NOT' in front:
    #     a,b = front.split(' ')
    #     result[back] = ~result[b]
    # else:
    #     result[back] = int(front)

# for i in input:
#     parse(i)

# print(result['a'])