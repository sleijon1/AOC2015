import re

def valid_password(pw):
    double = False
    consec = False
    iol = False
    for i in range(len(pw)-3):
        if ord(pw[i]) == ord(pw[i+1])-1 \
           and ord(pw[i+1]) == ord(pw[i+2])-1:
            consec = True
    for n_allowed in 'iol':
        if n_allowed in pw:
            iol = True
            break
    double = len(re.findall(r'([a-z])\1', pw)) == 2
    return double and consec and not iol

def increment_password(pw):
    reverse = list(pw[::-1])
    carry = True
    i = 0
    while carry:
        if reverse[i] == 'z':
            reverse[i] = 'a'
            i += 1
        else:
            reverse[i] = chr(ord(reverse[i])+1)
            carry = False
    return ''.join(reverse[::-1])


def create_pw(inp):
    while not valid_password(inp):
        inp = increment_password(inp)
    return inp


INP = "cqjxjnds"
p1 = create_pw(INP)
print(f"Solution part 1: {p1}")
INP = increment_password(p1)
print(f"Solution part 2: {create_pw(INP)}")
