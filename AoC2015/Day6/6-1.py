input = [x.strip() for x in open('input6-1.txt')]
grid = []

for i in range(1000):
    grid.append([])

for row in grid:
    for i in range(1000):
        row.append(0)

def toggle(combined_list):
    for i in combined_list:
        y = i[0]
        x = i[1]
        if grid[y][x] == 0:
            grid[y][x] = 1
        else:
            grid[y][x] = 0

def turn_on(combined_list):
    for i in combined_list:
        y = i[0]
        x = i[1]
        grid[y][x] = 1

def turn_off(combined_list):
    for i in combined_list:
        y = i[0]
        x = i[1]
        grid[y][x] = 0

def parse(line):
    line_list = line.split(' ')
    command = line_list[-4]
    first_coord = line_list[-3]
    second_coord = line_list[-1]
    y1 = int(first_coord.split(',')[0])
    x1 = int(first_coord.split(',')[1])
    y2 = int(second_coord.split(',')[0])
    x2 = int(second_coord.split(',')[1])
    listy = [x for x in range(y1,y2+1)]
    listx = [x for x in range(x1,x2+1)]
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

lights_on = 0

for line in grid:
    for light in line:
        if light == 1:
            lights_on += 1

print(lights_on)