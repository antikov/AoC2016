commands = open("input").read().split(", ")

directions = {
    "N": { "R" : "E", "L" : "W", "x" : 0, "y" : 1},
    "E": { "R" : "S", "L" : "N", "x" : 1, "y" : 0},
    "S": { "R" : "W", "L" : "E", "x" : 0, "y" : -1},
    "W": { "R" : "N", "L" : "S", "x" : -1, "y" : 0}
}

direction = "N"
x = 0
y = 0
for command in commands:
    rotation = command[0]
    distance = int(command[1:])
    direction = directions[direction][rotation]
    x = x + distance * directions[direction]["x"]
    y = y + distance * directions[direction]["y"]

print (abs(x) + abs(y))
