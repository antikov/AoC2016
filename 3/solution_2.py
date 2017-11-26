f = open("input")

def check_valid(x,y,z):
    return x+y>z and x+z>y and y+z>x

answer = 0
triangle_array = []
for line in f:
    (x,y,z) = map(int, line.split())
    triangle_array.append([x,y,z])
    if len(triangle_array) == 3:
        answer += 1 if check_valid(triangle_array[0][0], triangle_array[1][0], triangle_array[2][0]) else 0
        answer += 1 if check_valid(triangle_array[0][1], triangle_array[1][1], triangle_array[2][1]) else 0
        answer += 1 if check_valid(triangle_array[0][2], triangle_array[1][2], triangle_array[2][2]) else 0

        triangle_array = []

print (answer)
