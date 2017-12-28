def decompress_len(input):
    pos = 0
    output = 0
    while input.find("(", pos) != -1:
        left = input.find("(", pos)
        right = input.find(")", pos)
        temp = input[left + 1:right].split("x")
        size, count = int(temp[0]), int(temp[1])
        output += len(input[pos:left])
        output += count * decompress_len(input[right + 1: right + 1 + size])
        pos = right + size + 1
    output += len(input[pos:])
    return output

input = open("input").read().strip()
print(decompress_len(input))