input = [x.strip() for x in open('input.txt')]
total = 0
for i in input:
    l,w,h = i.split('x')
    l,w,h = int(l), int(w), int(h)
    bow = l*w*h
    face = min([l+l+w+w, w+w+h+h, l+l+h+h])
    total += face+bow

print(total)