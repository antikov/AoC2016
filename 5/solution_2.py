import hashlib

input = open("input").read().strip()

index = 0
password = ["-"] * 8
print ("Start decrypting...")
while ("-" in password):
    md5_hash = md5.new(input + str(index)).hexdigest()
    if (md5_hash[0:5] == "00000"):
        print (md5_hash, index)
        if md5_hash[5] >= "0" and md5_hash[5] < str(len(password)) and password[int(md5_hash[5])] == "-":
            password[int(md5_hash[5])] = md5_hash[6]
            print ("".join(password))
    index += 1

print ("".join(password))
print ("Done.")
