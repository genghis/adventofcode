input = [x.strip() for x in open('input5-1.txt')]
nice_list = []

def nice(word):
    condition1 = False
    condition2 = False
    for i in range(len(word)-2):
        window = word[i:i+3]
        if window[0] == window[-1]:
            condition1 = True
    for ind, letter in enumerate(word):
        if ind < len(word)-2:
            chunk = letter+word[ind+1]
            messy = word.replace(chunk,' ',1)
            if chunk in messy:
                condition2 = True
    return condition1 and condition2

for i in input:
    if nice(i):
        nice_list.append(i)

print(len(nice_list))