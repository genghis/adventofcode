input = [x.strip() for x in open('input5-1.txt')]

naughty_pairs = ['ab', 'cd', 'pq','xy']
doubles = [str(x+x) for x in 'abcdefghijklmnopqrstuvwxyz']
vowels = 'aeiou'
nice_list = []

def nice(word):
    wordvowels = [x for x in word if x in vowels]
    worddoubles = [x for x in doubles if x in word]
    wordnaughty = [x for x in naughty_pairs if x in word]
    if len(wordvowels) < 3:
        return False
    if not worddoubles:
        return False
    if wordnaughty:
        return False
    return True

for i in input:
    if nice(i):
        nice_list.append(i)

print(len(nice_list))