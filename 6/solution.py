f = open("input").read().split("\n")
data = [[] for x in range(len(f[0]))]

for line in f:
    for i in range(0,len(line)):
        data[i].append(line[i])

answer = ""

for string in data:
    sor =  sorted(string, key = lambda x : string.count(x), reverse = True)
    answer += sor[0]

print (answer)
