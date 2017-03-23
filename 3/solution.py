f = open("input")

def check_valid(x,y,z):
    return x+y>z and x+z>y and y+z>x
answer = 0
for line in f:
    (x,y,z) = map(int, line.split())
    answer += 1 if check_valid(x,y,z) else 0
    
print answer