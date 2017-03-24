import re

f = open("input").read().split("\n")

def decrypt(data, cipher):
    answer = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for s in data:
        if s in alphabet:
            answer += alphabet[(alphabet.index(s)+cipher) % 26]
        else:
            answer += s
    return answer
            
answer = 0
for line in f:
    arr = line.split("-")
    data  =" ".join(arr[:-1])
    sector_id = int(re.search('\d+', arr[-1]).group(0))
    decrypt_data = decrypt(data, sector_id)
    if decrypt_data.find("north") > -1:
        print decrypt(data, sector_id), sector_id