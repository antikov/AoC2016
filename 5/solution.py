import hashlib

input = open("input").read().strip()

index = 0
password = ""

while (len(password) != 8):
    key = input + str(index)
    md5_hash = hashlib.md5(key.encode()).hexdigest()
    if (md5_hash[0:5] == "00000"):
        password += md5_hash[5]
        print (md5_hash, index)
    index += 1

print (password)
