input = [x.strip() for x in open('input.txt')]
total = 0
for i in input:
    l,w,h = i.split('x')
    l,w,h = int(l), int(w), int(h)
    extra = min([l*w,w*h,l*h])
    present = 2*l*w + 2*w*h + 2*l*h + extra
    total += present

print(total)