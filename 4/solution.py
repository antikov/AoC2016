import re

f = open("input").read().split("\n")

def get_checksum (data):
    letters_count = {}
    letters = []

    for s in data:
        if s in letters:
            letters_count[s] += 1
        else:
            letters.append(s)
            letters_count[s] = 1
    letters.sort(key = lambda x : str(letters_count[x]) + chr(ord('z')-ord(x)+ord('a')), reverse = True)
    return "".join(letters)[:5]

answer = 0
for line in f:
    arr = line.split("-")
    data  ="".join(arr[:-1])
    sector_id = int(re.search('\d+', arr[-1]).group(0))
    checksum = re.search('[a-z]+', arr[-1]).group(0)
    if get_checksum(data) == checksum:
        answer = answer + sector_id
print answer