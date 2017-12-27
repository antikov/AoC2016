import numpy as np
f = open("input").read().strip().split("\n")
matrix = np.zeros((6,50))
for line in f:
    temp = line.split()
    if (temp[0] == "rect"):
        x,y = list(map(int,temp[1].split("x")))
        matrix[:y,:x] = 1
    else:
        x = int(temp[2].split("=")[1])
        y = int(temp[4])
        if (temp[1] == "row"):
            matrix[x] = np.roll(matrix[x], y)
        else:
            matrix[:,x] = np.roll(matrix[:,x],y)
print(np.count_nonzero(matrix))

for i in range(6):
    s = []
    for j in range(10):
        s.append("".join(map(lambda x: "#" if x == 1 else " ",matrix[i,j*5:j*5+5])))
    print(" ".join(s))
