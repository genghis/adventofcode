import hashlib

input = 'bgvyzdsv'
added = 0
zeroes = False

while zeroes == False:
    added += 1
    chunk = input+str(added)
    result = hashlib.md5(chunk.encode()).hexdigest()
    if result[0:5:] == '00000':
        zeroes = True

print(added)