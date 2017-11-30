import re

def has_abba(text):
    regex = r"([a-z])([a-z])\2\1"
    abba = re.search(regex, text)
    if abba and abba.group(1) != abba.group(2):
        return True
    return False

assert has_abba("abba[mnop]qrst") == True
assert has_abba("abcd[bddb]xyyx") == True
assert has_abba("aaaa[qwer]tyui") == False
assert has_abba("ioxxoj[asdfgh]zxcvbn") == True

def check_tls(ip):
    # part 1 - check abba inside []
    regex = r"\[([a-z]+)\]"
    inside = re.findall(regex,ip)
    for part in inside:
        if has_abba(part):
            return False

    #part 2 - check abba outside []
    regex = r"\[[a-z]+\]"
    outside = re.split(regex, ip)
    for part in outside:
        if has_abba(part):
            return True

    return False

iplist = open("input").read().strip().split("\n")
print(sum(map(check_tls,iplist)))
