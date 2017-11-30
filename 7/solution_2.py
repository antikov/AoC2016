import re

def get_all_aba(text):
	all_aba = []
	i = 0
	while i + 2 < len(text):
		if text[i] == text[i+2]:
			all_aba.append(text[i:i+3])
		i += 1
	return all_aba

def invert_aba(aba):
	return aba[1]+aba[0]+aba[1]

assert invert_aba("aba") == "bab"

def check_ssl(ip):
	# part 1 - gets all aba inside []
	regex = r"\[([a-z]+)\]"
	aba_inside = []
	inside = re.findall(regex,ip)
	for part in inside:
		aba_inside.extend(get_all_aba(part))
	aba_inside_invert = set(map(invert_aba,aba_inside))
	#part 2 - gets_all aba outside []
	aba_outside = []
	regex = r"\[[a-z]+\]"
	outside = re.split(regex, ip)
	for part in outside:
		aba_outside.extend(get_all_aba(part))
	return aba_inside_invert & set(aba_outside) != set()

iplist = open("input").read().strip().split("\n")
print(sum(map(check_ssl,iplist)))
