f = open("input")
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x,y = 1,1
key = ""
for line in f:
    for s in line:
        if (s == "L"):
            y = 0 if y == 0 else y - 1
        if (s == "R"):
            y = 2 if y == 2 else y + 1
        if (s == "U"):
            x = 0 if x == 0 else x - 1
        if (s == "D"):
            x = 2 if x == 2 else x + 1
            
    key = key + str(keypad[x][y])
print key