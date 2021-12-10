input = [x.strip() for x in open('input6-1.txt')]
# input = [x.strip() for x in open('testinput.txt')]
# print(input)
grid = [[] for _ in range(1000)]

for row in grid:
    for _ in range(1000):
        row.append(0)

def toggle(combined_list):
    for i in combined_list:
        y = i[0]
        x = i[1]
        grid[y][x] += 2

def turn_on(combined_list):
    for i in combined_list:
        y = i[0]
        x = i[1]
        grid[y][x] += 1

def turn_off(combined_list):
    for i in combined_list:
        y = i[0]
        x = i[1]
        if grid[y][x] != 0:
            grid[y][x] -= 1

def parse(line):
    line_list = line.split(' ')
    command = line_list[-4]
    first_coord = line_list[-3]
    second_coord = line_list[-1]
    y1 = int(first_coord.split(',')[0])
    x1 = int(first_coord.split(',')[1])
    y2 = int(second_coord.split(',')[0])
    x2 = int(second_coord.split(',')[1])
    listy = list(range(y1,y2+1))
    listx = list(range(x1,x2+1))
    combined_list=[]
    for y in listy:
        for x in listx:
            combined_list.append((y,x))
    if command == "toggle":
        toggle(combined_list)
    elif command == "on":
        turn_on(combined_list)
    elif command == "off":
        turn_off(combined_list)
    else:
        print("Command logic is wrong")

for i in input:
    parse(i)

light_power = 0

for line in grid:
    for light in line:
        light_power += light

print(light_power)