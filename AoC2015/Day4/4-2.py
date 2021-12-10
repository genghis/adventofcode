import hashlib

input = 'bgvyzdsv'
added = 0
zeroes = False

while not zeroes:
    added += 1
    chunk = input+str(added)
    result = hashlib.md5(chunk.encode()).hexdigest()
    if result[:6] == '000000':
        zeroes = True

print(added)