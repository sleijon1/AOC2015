import hashlib
key = "bgvyzdsv"
for i in range(10000000):
    md5 = hashlib.md5((key + str(i)).encode())
    if md5.hexdigest()[0:6] == '0'*6:
        break
print(f"Solution part 1: {i}")

