def bot_add_value(bots,bot,value):
    if bot in bots:
        bots[bot].append(value)
    else:
        bots[bot] = [value]


instructions = open("input.txt").read().strip().split("\n")
output = {}
bots = {}
index = 0
while instructions:
    temp = instructions[index].split()
    if temp[0] == "value":
        value = int(temp[1])
        bot = int(temp[5])
        bot_add_value(bots, bot, value)
        del instructions[index]
    elif temp[0] == "bot":
        bot = int(temp[1])
        if bot in bots and len(bots[bot]) > 1:
            value_low, value_high = min(bots[bot]), max(bots[bot])
            low, high = int(temp[6]), int(temp[11])
            if temp[5] == "bot":
                bot_add_value(bots, low, value_low)
            else:
                output[low] = value_low
            if temp[10] == "bot":
                bot_add_value(bots,high, value_high)
            else:
                output[high] = value_high
            if value_low == 17 and value_high == 61:
                print("Part 1:",bot)
            del instructions[index]
        else:
            index += 1
            if index == len(instructions):
                index = 0
print("Part 2:",output[0]*output[1]*output[2])