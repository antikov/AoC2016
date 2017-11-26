commands = open("input").read().split(", ")

directions = {
    "N": { "R" : "E", "L" : "W", "x" : 0, "y" : 1},
    "E": { "R" : "S", "L" : "N", "x" : 1, "y" : 0},
    "S": { "R" : "W", "L" : "E", "x" : 0, "y" : -1},
    "W": { "R" : "N", "L" : "S", "x" : -1, "y" : 0}
}
visited = [(0,0)]

direction = "N"
x = 0
y = 0
for command in commands:
    rotation = command[0]
    distance = int(command[1:])
    direction = directions[direction][rotation]
    start_x, start_y = x, y
    x = x + distance * directions[direction]["x"]
    y = y + distance * directions[direction]["y"]

    while(start_x != x):
        start_x = start_x + directions[direction]["x"]
        if (start_x, start_y) in visited:
            print (abs(start_x) + abs(start_y))
            exit(0)
        visited.append((start_x, start_y))

    while(start_y != y):
        start_y = start_y + directions[direction]["y"]
        if (start_x, start_y) in visited:
            print (abs(start_x) + abs(start_y))
            exit(0)
        visited.append((start_x, start_y))
