f = open("input").read().strip()
pos = 0
output = ""
while f.find("(",pos) != -1:
    left = f.find("(",pos)
    right = f.find(")",pos)
    temp = f[left+1:right].split("x")
    size, count = int(temp[0]), int(temp[1])
    output += f[pos:left]
    output += f[right + 1: right + 1 + size] * count
    pos = right + size + 1
output += f[pos:]
print(len(output))