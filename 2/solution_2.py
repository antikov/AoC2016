f = open("input")
keypad = {
    "1" : {"D" : "3"},
    "2" : {"R" : "3", "D" : "6"},
    "3" : {"L" : "2", "R" : "4", "U" : "1", "D" : "7"},
    "4" : {"L" : "3", "D" : "8"},
    "5" : {"R" : "6"},
    "6" : {"L" : "5", "R" : "7", "U" : "2", "D" : "A"},
    "7" : {"L" : "6", "R" : "8", "U" : "3", "D" : "B"},
    "8" : {"L" : "7", "R" : "9", "U" : "4", "D" : "C"},
    "9" : {"L" : "8"},
    "A" : {"R" : "B", "U" : "6"},
    "B" : {"L" : "A", "R" : "C", "U" : "7", "D" : "D"},
    "C" : {"L" : "B", "U" : "8"},
    "D" : {"U" : "B"}
}
now  = "5"
key = ""
for line in f:
    for s in line:
        now = now if s not in keypad[now] else keypad[now][s]

    key = key + now
print (key)
